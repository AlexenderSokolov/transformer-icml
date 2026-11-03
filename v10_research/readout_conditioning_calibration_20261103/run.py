import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
import argparse,csv,hashlib,json,platform,subprocess,sys,time,traceback
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
import calibration as c
BASE=Path(__file__).resolve().parent
FILES=['protocol.json','PLAN.md','test_calibration.py','calibration.py','run.py','../readout_conditioning_calibration_design_20261103/PROPOSAL.md','../learned_position_pilot_20261103/pilot.py']

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def js(path,obj):Path(path).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def csvwrite(path,rows):
    with open(path,'w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def seal():
    if (BASE/'PRE_RUN_HASHES.json').exists():raise FileExistsError('seal exists')
    js(BASE/'PRE_RUN_HASHES.json',dict(sealed_utc=datetime.now(timezone.utc).isoformat(),files={f:digest(BASE/f) for f in FILES},status='SEALED_BEFORE_CALIBRATION_SAMPLING'))
    print((BASE/'PRE_RUN_HASHES.json').read_text())
def verifyseal():
    hashes=json.loads((BASE/'PRE_RUN_HASHES.json').read_text())['files']
    for f,h in hashes.items():
        if digest(BASE/f)!=h:raise RuntimeError('sealed input changed: '+f)
    return hashes

def metrics(model,xprior,yprior,xcollision,ycollision):
    qp,hp=model.forward(xprior,cache=True);qc,hc=model.forward(xcollision,cache=True);kp=c.kl(yprior,qp);kc=c.kl(ycollision,qc)
    return dict(prior_KL=float(kp.mean()),prior_KL_MC_SE=float(kp.std(ddof=1)/np.sqrt(len(kp))),collision_KL=float(kc.mean()),balanced_KL=float(.5*(kp.mean()+kc.mean())),collision_max_abs_error=float(np.max(abs(qc-ycollision))),collision_mean_abs_error=float(np.mean(abs(qc-ycollision))),prior_saturation=float(np.mean(abs(hp['h'])>.99)),collision_saturation=float(np.mean(abs(hc['h'])>.99)),collision_q0=float(qc[0]),collision_q1=float(qc[1]),collision_q2=float(qc[2]),collision_q3=float(qc[3]))

def run(out):
    hashes=verifyseal();cfg=json.loads((BASE/'protocol.json').read_text());out=Path(out)
    if not out.is_absolute():out=BASE/out
    out.mkdir(parents=True,exist_ok=False);(out/'checkpoints').mkdir();start=time.perf_counter()
    try:
        check=subprocess.run([sys.executable,str(BASE/'test_calibration.py')],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (out/'tests.log').write_text(check.stdout)
        if check.returncode:raise RuntimeError('pre-sampling unit check failed; no calibration sampled or fit')
        # Sampling starts only after the seal and successful static/gradient checks.
        train,_=c.pilot.prior_batch(cfg['training_prior_words'],64,np.random.default_rng(cfg['training_data_seed']))
        validation,_=c.pilot.prior_batch(cfg['validation_prior_words'],64,np.random.default_rng(cfg['validation_data_seed']))
        collision=c.collision_words();boundary=c.collision_words(31,32)
        ytrain=c.literal_statistics(train)['Q'];yvalidation=c.literal_statistics(validation)['Q'];ycollision=c.literal_statistics(collision)['Q'];yboundary=c.literal_statistics(boundary)['Q']
        rng=np.random.default_rng(cfg['minibatch_seed']);steps=cfg['optimization']['steps'];ip=[];ic=[]
        for _ in range(steps):ip.append(rng.integers(0,len(train),64));ic.append(rng.integers(0,4,64))
        ip=np.array(ip);ic=np.array(ic)
        np.savez_compressed(out/'frozen_data.npz',train_words=train,validation_words=validation,collision_words=collision,boundary_words=boundary,train_Q=ytrain,validation_Q=yvalidation,collision_Q=ycollision,boundary_Q=yboundary,prior_batch_indices=ip,collision_batch_indices=ic)
        xtr=c.features(train,'half_normalized');xval=c.features(validation,'half_normalized');xcol=c.features(collision,'half_normalized');xbound=c.features(boundary,'half_normalized');allx=np.concatenate([xtr,xval,xcol,xbound]);ally=np.concatenate([ytrain,yvalidation,ycollision,yboundary])
        decoder_error=float(np.max(abs(c.decode_features(allx)-ally)))
        if decoder_error>1e-14:raise AssertionError('independent feature decoder failed')
        # Also compare the independently generated teacher to the original full-word statistic code.
        teacher_error=float(np.max(abs(c.pilot.statistics(np.concatenate([train,validation,collision,boundary]))['Q']-ally)))
        if teacher_error>1e-14:raise AssertionError('literal teacher mismatch')
        matcherr=0.
        for seed in cfg['initialization_seeds']:
            a=c.Readout(seed,'half_normalized');b=c.Readout(seed,'half_count_scaled');err=float(np.max(abs(a.predict(allx)-b.predict(allx))));matcherr=max(matcherr,err)
            if err>1e-14:raise AssertionError('initial prediction matching failed')
        js(out/'pre_fit_checks.json',dict(unit_tests_passed=True,feature_decoder_max_error=decoder_error,literal_teacher_max_error=teacher_error,matched_initialization_max_error=matcherr,collision_floor=c.collision_floor(),data_sha256=digest(out/'frozen_data.npz'),sampling_after_seal=True))
        print(json.dumps(dict(pre_fit_checks='passed',feature_decoder_max_error=decoder_error,matched_initialization_max_error=matcherr)),flush=True)
        allrows=[];allmetrics=[];final=[];times=[];predictions={}
        for seed in cfg['initialization_seeds']:
            for condition in cfg['conditions']:
                t0=time.perf_counter();model=c.Readout(seed,condition);opt=c.pilot.Adam(model.params,readout_lr=.003,beta1=.9,beta2=.999,epsilon=1e-8)
                xp=c.features(train,condition);xv=c.features(validation,condition);xc=c.features(collision,condition);xb=c.features(boundary,condition);rows=[]
                def checkpoint(step):
                    model.save(out/'checkpoints'/f'{condition}_{seed}_step{step}.npz')
                    tm=metrics(model,xp,ytrain,xc,ycollision);vm=metrics(model,xv,yvalidation,xc,ycollision)
                    if condition=='uniform_control' and vm['collision_KL']<c.collision_floor()-1e-12:raise AssertionError('uniform control violates collision information floor')
                    row=dict(condition=condition,seed=seed,step=step,**{f'train_{k}':v for k,v in tm.items()},**{f'validation_{k}':v for k,v in vm.items()},effective_W_l2=float(np.linalg.norm(model.effective_W())),raw_W_l2=float(np.linalg.norm(model.params['W'])),boundary_max_abs_error=float(np.max(abs(model.predict(xb)-yboundary))))
                    allmetrics.append(row);print(json.dumps({k:row[k] for k in ['condition','seed','step','validation_prior_KL','validation_collision_KL','validation_collision_max_abs_error']}),flush=True)
                    return row
                checkpoint(0)
                for step in range(steps):
                    x=np.concatenate([xp[ip[step]],xc[ic[step]]]);y=np.concatenate([ytrain[ip[step]],ycollision[ic[step]]]);loss,grad,cache=model.loss_grad(x,y)
                    if not np.isfinite(loss) or not all(np.all(np.isfinite(g)) for g in grad.values()):raise FloatingPointError('nonfinite loss or gradient')
                    opt.step(model.params,grad)
                    if not all(np.all(np.isfinite(v)) for v in model.params.values()):raise FloatingPointError('nonfinite parameter')
                    row=dict(condition=condition,seed=seed,step=step+1,minibatch_CE=loss,minibatch_KL=float(loss-c.pilot.cross_entropy(y,y).mean()),gradient_l2=float(np.sqrt(sum(np.sum(g*g) for g in grad.values()))),effective_W_l2=float(np.linalg.norm(model.effective_W())),raw_W_l2=float(np.linalg.norm(model.params['W'])),minibatch_saturation=float(np.mean(abs(cache['h'])>.99)))
                    row.update({f'W_gradient_row_{j}_l2':float(np.linalg.norm(grad['W'][j])) for j in range(9)});rows.append(row)
                    if step+1 in cfg['optimization']['checkpoints']:last=checkpoint(step+1)
                elapsed=time.perf_counter()-t0;last=dict(last,fit_seconds=elapsed,finite_fit_screen_pass=bool(last['validation_prior_KL']<=.01 and last['validation_collision_max_abs_error']<=.05))
                final.append(last);times.append(dict(condition=condition,seed=seed,seconds=elapsed));csvwrite(out/f'{condition}_{seed}_updates.csv',rows);allrows.extend(rows)
                prefix=f'{condition}_{seed}';predictions[prefix+'_train']=model.predict(xp);predictions[prefix+'_validation']=model.predict(xv);predictions[prefix+'_collision']=model.predict(xc);predictions[prefix+'_boundary']=model.predict(xb)
        csvwrite(out/'updates.csv',allrows);csvwrite(out/'checkpoint_metrics.csv',allmetrics);csvwrite(out/'final_metrics.csv',final);np.savez_compressed(out/'final_predictions.npz',**predictions)
        result=dict(status='BOUNDED_CALIBRATION_COMPLETED_NOT_INDEPENDENTLY_ACCEPTED',sealed_inputs=hashes,environment=dict(python=sys.version,numpy=np.__version__,platform=platform.platform(),blas_threads=1),total_seconds=time.perf_counter()-start,fits=times,final_results=final,condition_all_three_pass={cond:all(r['finite_fit_screen_pass'] for r in final if r['condition']==cond) for cond in cfg['conditions']},limitations=cfg['limits'])
        js(out/'results.json',result);js(out/'ARTIFACT_HASHES.json',{str(p.relative_to(out)):digest(p) for p in sorted(out.rglob('*')) if p.is_file()})
        print(json.dumps(dict(total_seconds=result['total_seconds'],condition_all_three_pass=result['condition_all_three_pass'],status=result['status'])),flush=True)
    except Exception as exc:
        js(out/'FAILURE.json',dict(status='STOPPED_ON_FAILED_CHECK',error_type=type(exc).__name__,error=str(exc),traceback=traceback.format_exc(),elapsed_seconds=time.perf_counter()-start));raise

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['seal','run']);p.add_argument('--output',default='calibration_v1');a=p.parse_args();seal() if a.command=='seal' else run(a.output)
