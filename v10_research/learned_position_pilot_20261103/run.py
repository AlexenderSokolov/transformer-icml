"""Sealed exploratory smoke runner. BLAS threads fixed before importing NumPy."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
import argparse,copy,csv,hashlib,json,platform,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
import pilot
BASE=Path(__file__).resolve().parent
FILES=['protocol.json','PLAN.md','pilot.py','test_pilot.py','run.py']

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write_json(path,data):Path(path).write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
def write_csv(path,rows):
    with open(path,'w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def summary(x):
    x=np.asarray(x);return float(x.mean()),float(x.std(ddof=1)/np.sqrt(len(x)))

def seal():
    target=BASE/'PRE_RUN_HASHES.json'
    if target.exists():raise FileExistsError('seal exists; preserve original')
    write_json(target,{'sealed_utc':datetime.now(timezone.utc).isoformat(),'files':{f:digest(BASE/f) for f in FILES}})
    print(target.read_text())

def validate_seal():
    hashes=json.loads((BASE/'PRE_RUN_HASHES.json').read_text())['files']
    for file,expected in hashes.items():
        if digest(BASE/file)!=expected:raise RuntimeError('sealed file changed: '+file)
    return hashes

def run(out):
    hashes=validate_seal();cfg=json.loads((BASE/'protocol.json').read_text());out=Path(out)
    if not out.is_absolute():out=BASE/out
    out.mkdir(parents=True,exist_ok=False);(out/'checkpoints').mkdir()
    start=time.perf_counter();test=subprocess.run([sys.executable,str(BASE/'test_pilot.py')],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (out/'tests.log').write_text(test.stdout)
    if test.returncode:raise RuntimeError('unit tests failed, no training run')
    models={};alllogs=[];timings=[]
    for condition in cfg['conditions']:
        mode=condition.split('_')[0];mode='learned' if mode=='learned' else mode
        model=pilot.Model(cfg['model_seed'],mode);model.save(out/'checkpoints'/f'{condition}_0.npz')
        opt=pilot.Adam(model.params,**{k:v for k,v in cfg['training']['optimizer'].items() if k in ['readout_lr','pool_lr','beta1','beta2','epsilon']})
        rng=np.random.default_rng(cfg['training_seed']);t0=time.perf_counter();datahash=hashlib.sha256();logs=[]
        for step in range(cfg['training']['steps']):
            M=cfg['training']['horizons'][step%2];w,p=pilot.prior_batch(cfg['training']['batch_size'],M,rng)
            datahash.update(w.tobytes());datahash.update(p.tobytes());target=pilot.statistics(w)['B'];k=[1,int(np.sqrt(M)),M//8][step%3]
            clean_before=float(pilot.cross_entropy(target,model.predict(w)).mean());selected_fraction=0.;changed=0.
            if condition.endswith('_edit'):
                z,info=pilot.attack(model.predict,w,k,'training');selected_fraction=float(np.mean(info['selected']!=0));changed=float(np.mean(info['changed']))
                loss,grad=model.loss_grad(np.concatenate([w,z]),np.tile(target,2))
            else:loss,grad=model.loss_grad(w,target)
            opt.step(model.params,grad)
            if not all(np.all(np.isfinite(x)) for x in model.params.values()):raise FloatingPointError('nonfinite parameter')
            row=dict(condition=condition,step=step+1,M=M,k=k,objective=loss,clean_before=clean_before,gradient_l2=float(np.sqrt(sum(np.sum(g*g) for g in grad.values()))),pool_gradient_l2=float(np.linalg.norm(grad['a'])),pool_parameter_l2=float(np.linalg.norm(model.params['a'])),nonidentity_attack_fraction=selected_fraction,mean_changed=changed)
            logs.append(row)
            if step+1 in cfg['training']['checkpoints']:
                model.save(out/'checkpoints'/f'{condition}_{step+1}.npz')
                print(json.dumps({k:row[k] for k in ['condition','step','objective','clean_before','pool_parameter_l2']}),flush=True)
        elapsed=time.perf_counter()-t0;timings.append(dict(condition=condition,train_seconds=elapsed,paths=cfg['training']['steps']*cfg['training']['batch_size'],training_data_sha256=datahash.hexdigest()))
        write_csv(out/f'{condition}_training.csv',logs);alllogs.extend(logs);models[condition]=model
        print(json.dumps(timings[-1]),flush=True)
    write_csv(out/'training.csv',alllogs)
    if len(set(x['training_data_sha256'] for x in timings))!=1:raise RuntimeError('conditions used different training data')
    predictors={name:m.predict for name,m in models.items()}
    for name in ['learned_clean','learned_edit']:
        ablated=copy.deepcopy(models[name]);ablated.mode='uniform';predictors[name+'_uniform_ablation']=ablated.predict
    for name in cfg['evaluation']['baselines']:predictors[name]=lambda w,name=name:pilot.statistics(w)[name]
    rng=np.random.default_rng(cfg['test_seed']);cleanrows=[];stressrows=[];arrays={};datasets={};t_eval=time.perf_counter()
    for M in cfg['evaluation']['horizons']:
        w,p=pilot.prior_batch(cfg['evaluation']['clean_prior_paths'],M,rng);s=pilot.statistics(w);target=p[np.arange(len(w)),s['U']];b=s['B'];entropy=pilot.cross_entropy(b,b)
        datasets[f'clean_M{M}_words']=w;datasets[f'clean_M{M}_p']=p
        for name,predict in predictors.items():
            q=predict(w);tv=abs(q-target);ce=pilot.cross_entropy(b,q);mean,se=summary(tv);finite=bool(np.all(np.isfinite(ce)))
            if finite:ce_mean,ce_se=summary(ce);ex_mean,ex_se=summary(ce-entropy)
            else:ce_mean=ce_se=ex_mean=ex_se=None
            cleanrows.append(dict(condition=name,M=M,n=len(w),TV=mean,TV_MC_SE=se,conditional_CE=ce_mean,conditional_CE_MC_SE=ce_se,excess_KL=ex_mean,excess_KL_MC_SE=ex_se,infinite_loss_paths=int(np.sum(~np.isfinite(ce)))))
            arrays[f'clean_M{M}_{name}_tv']=tv
            if finite:arrays[f'clean_M{M}_{name}_excess']=ce-entropy
    for M in cfg['evaluation']['horizons']:
        for source,p0 in pilot.stress_sources(M).items():
            for initial in cfg['evaluation']['starts']:
                n=cfg['evaluation']['stress_paths_per_source_start'];p=np.repeat(p0[None],n,axis=0);w=pilot.simulate_words(p,np.full(n,initial),M,rng=rng);s=pilot.statistics(w);target=p[np.arange(n),s['U']]
                datasets[f'stress_M{M}_{source}_s{initial}_words']=w;datasets[f'stress_M{M}_{source}_s{initial}_p']=p
                for k in sorted(set([0,int(np.sqrt(M)),M//8])):
                    g=max(M**-.5,k/M)
                    for family in cfg['evaluation']['attack_families']:
                        for name,predict in predictors.items():
                            z,info=pilot.attack(predict,w,k,family);q=predict(z);tv=abs(q-target);mean,se=summary(tv)
                            if np.any(z[:,-2:]!=w[:,-2:]) or np.any(np.sum(z!=w,axis=1)>k):raise AssertionError('illegal attack')
                            stressrows.append(dict(condition=name,M=M,source=source,initial=initial,k=k,attack_family=family,n=n,TV=mean,TV_MC_SE=se,normalized_TV=mean/g,normalized_MC_SE=se/g,mean_changed=float(info['changed'].mean()),nonidentity_fraction=float(np.mean(info['selected']!=0))))
                            key=f'M{M}_{source}_s{initial}_k{k}_{family}_{name}';arrays[key+'_tv']=tv;arrays[key+'_attack']=info['selected']
                print(json.dumps(dict(evaluation_M=M,source=source,initial=initial)),flush=True)
    eval_seconds=time.perf_counter()-t_eval
    write_csv(out/'clean_evaluation.csv',cleanrows);write_csv(out/'stress_evaluation.csv',stressrows)
    np.savez_compressed(out/'evaluation_paths.npz',**datasets);np.savez_compressed(out/'trajectory_metrics.npz',**arrays)
    panel=[]
    for name in predictors:
        for M in cfg['evaluation']['horizons']:
            cells=[r for r in stressrows if r['condition']==name and r['M']==M]
            worst=max(cells,key=lambda r:r['normalized_TV']);panel.append(worst)
    write_csv(out/'descriptive_panel_maxima.csv',panel)
    # Profiles expose what moved; interpretation still requires controls and independent review.
    profile_rows=[]
    for name,model in models.items():
        for M in cfg['evaluation']['horizons']:
            alpha,_=model.pooling(M)
            for h in [1,2]:
                profile_rows.append(dict(condition=name,M=M,head=h,first_half_mass=float(alpha[h,:M//2].sum()),last_quarter_mass=float(alpha[h,3*M//4:].sum()),max_weight=float(alpha[h].max()),min_weight=float(alpha[h].min()),entropy=float(-np.sum(np.where(alpha[h]>0,alpha[h]*np.log(np.maximum(alpha[h],1e-300)),0)))))
    write_csv(out/'profiles.csv',profile_rows)
    result=dict(protocol_sha256=hashes['protocol.json'],code_hashes=hashes,environment=dict(python=sys.version,numpy=np.__version__,platform=platform.platform(),blas_threads=1),training=timings,evaluation_seconds=eval_seconds,total_seconds=time.perf_counter()-start,clean_results=cleanrows,finite_panel_descriptive_maxima=panel,limitations=cfg['limits'],status='EXPLORATORY_SMOKE_COMPLETED_NOT_REVIEW_ACCEPTED')
    write_json(out/'results.json',result)
    artifacts={str(p.relative_to(out)):digest(p) for p in sorted(out.rglob('*')) if p.is_file()}
    write_json(out/'ARTIFACT_HASHES.json',artifacts)
    print(json.dumps(dict(total_seconds=result['total_seconds'],evaluation_seconds=eval_seconds,status=result['status'])),flush=True)
    for name in cfg['conditions']:
        print(json.dumps(dict(condition=name,clean_excess=[r['excess_KL'] for r in cleanrows if r['condition']==name],descriptive_max_normalized_tv=[r['normalized_TV'] for r in panel if r['condition']==name])),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['seal','run']);p.add_argument('--output',default='smoke_v1');args=p.parse_args()
    seal() if args.command=='seal' else run(args.output)
