"""Fixed natural-label study. No retries, checkpoint selection, or partial resumption.
Set OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 before execution.
"""
import argparse, contextlib, io, json, os, platform, shutil, sys, time, traceback
from pathlib import Path
import numpy as np
from core import *
from capture import dump, sha, now, make_archive, require_receipt, verify_local_payload

ROOT=Path(__file__).resolve().parent

def summarize(x):
    x=np.asarray(x,dtype=float)
    return {'n':len(x),'mean':float(x.mean()) if len(x) else None,
            'mc_se':float(x.std(ddof=1)/np.sqrt(len(x))) if len(x)>1 else None}

def fit_table(cells):
    table={}
    for J,C,y in cells:
        for j,c,t in zip(J,C,y):
            a=table.setdefault((int(j),int(c)),[0,0]);a[0]+=1;a[1]+=int(t)
    return table

def table_predict(table,J,C):
    return np.array([(table.get((int(j),int(c)),[0,0])[1]+1)/(table.get((int(j),int(c)),[0,0])[0]+2) for j,c in zip(J,C)])

def word_overlap(train,test):
    seen={w.tobytes() for a in train for w in a if a.shape[1]==test.shape[1]}
    return sum(w.tobytes() in seen for w in test)

def load_training(path,target):
    if target not in ('y','B'):raise ValueError('target')
    with np.load(path,allow_pickle=False) as a:
        return {**{k:a[k].copy() for k in ['H','U','J','C']},'target':a[target].copy()}

def check_sources(receipt=None):
    manifest=ROOT/'SOURCE_MANIFEST.json';binding=sha(manifest)
    require_receipt(receipt or ROOT/'source_receipt.json',ROOT/'source.zip','source',binding)
    verify_local_payload(ROOT,ROOT/'source.zip')
    for e in json.loads(manifest.read_text())['files']:
        if sha(ROOT/e['path'])!=e['sha256']:raise ValueError('changed source '+e['path'])
    return json.loads((ROOT/'protocol.json').read_text()),binding

def resources(cfg):
    if shutil.disk_usage(ROOT).free<cfg['min_free_disk_bytes']:raise RuntimeError('free disk below protocol floor')
    for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:
        if os.environ.get(k)!='1':raise RuntimeError(k+' must equal 1 before Python starts')

def prior_outputs(cfg,binding,rep,condition_index):
    for r in range(rep+1):
        for ci,c in enumerate(cfg['conditions']):
            if r==rep and ci>=condition_index:continue
            d=ROOT/'runs'/f'rep{r}'/c
            require_receipt(d/'receipt.json',d/'output.zip','output',binding)
            verify_local_payload(d,d/'output.zip')
            completed=json.loads((d/'COMPLETED.json').read_text())
            if completed.get('status')!='COMPLETE' or completed.get('steps')!=cfg['steps'] or (d/'FAILURE.txt').exists():raise ValueError('prior fit incomplete or failed')
            started=json.loads((d/'STARTED.json').read_text())
            if started.get('replicate')!=r or started.get('condition')!=c or started.get('source_manifest_sha256')!=binding:raise ValueError('output identity mismatch')

def save_npz(path,**arrays):
    with Path(path).open('xb') as f:
        np.savez_compressed(f,**arrays);f.flush();os.fsync(f.fileno())

def save_text(path,text):
    with Path(path).open('x',encoding='utf-8') as f:
        f.write(text);f.flush();os.fsync(f.fileno())

def environment():
    stream=io.StringIO()
    with contextlib.redirect_stdout(stream):np.show_config()
    return {'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),
            'threads':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},
            'numpy_config':stream.getvalue()}

def prepare(rep):
    cfg,binding=check_sources();resources(cfg)
    if rep not in range(cfg['replicates']):raise ValueError('replicate')
    prior_outputs(cfg,binding,rep,0)
    d=ROOT/'runs'/f'rep{rep}'/'inputs';d.mkdir(parents=True,exist_ok=False)
    dump(d/'STARTED.json',{'status':'INCOMPLETE_UNLESS_COMPLETED_FILE_EXISTS','at':now(),'replicate':rep,'source_manifest_sha256':binding})
    states={};start=time.monotonic();base=cfg['seed_base']+1000*rep
    try:
        for split,horizons,n,offset in [('train',cfg['train_horizons'],cfg['train_per_horizon'],10),('test',cfg['test_horizons'],cfg['test_per_horizon'],20)]:
            for i,M in enumerate(horizons):
                rng=np.random.Generator(np.random.PCG64(base+offset+i));initial=rng.bit_generator.state
                p=rng.random((n,4));starts=rng.integers(0,4,size=n);draws=rng.random((n,M+1))
                words,y=simulate_from_draws(p,starts,draws);H,U,J,C,B=statistics(words)
                save_npz(d/f'{split}_M{M}.npz',p=p,starts=starts,draws=draws,words=words,y=y,H=H,U=U,J=J,C=C,B=B)
                states[f'{split}_M{M}']={'seed':base+offset+i,'before':initial,'after':rng.bit_generator.state}
        rng=np.random.Generator(np.random.PCG64(base+30));before=rng.bit_generator.state
        init=initial_parameters(rng);states['initialization']={'seed':base+30,'before':before,'after':rng.bit_generator.state}
        rng=np.random.Generator(np.random.PCG64(base+40));before=rng.bit_generator.state
        batches=rng.integers(0,cfg['train_per_horizon'],size=(cfg['steps'],cfg['batch_size']))
        states['batches']={'seed':base+40,'before':before,'after':rng.bit_generator.state}
        save_npz(d/'optimization.npz',initial_parameters=init,batches=batches,horizons=np.array([cfg['train_horizons'][i%2] for i in range(cfg['steps'])]))
        dump(d/'RNG_STATES.json',states);dump(d/'ENVIRONMENT.json',environment())
        train=[np.load(d/f'train_M{M}.npz',allow_pickle=False) for M in cfg['train_horizons']]
        table=fit_table([(a['J'],a['C'],a['y']) for a in train]);dump(d/'empirical_table.json',[{'J':j,'C':c,'n':n,'ones':o} for (j,c),(n,o) in sorted(table.items())])
        overlap={}
        for M in cfg['test_horizons']:
            with np.load(d/f'test_M{M}.npz',allow_pickle=False) as a:
                overlap[str(M)]={'test_duplicate_word_count':len(a['words'])-len({w.tobytes() for w in a['words']}),'test_examples_matching_train_word':word_overlap([t['words'] for t in train],a['words']), 'test_duplicate_JC_count':len(a['J'])-len(set(zip(a['J'].tolist(),a['C'].tolist())))}
        for a in train:a.close()
        dump(d/'overlap.json',overlap)
        dump(d/'COMPLETED.json',{'status':'COMPLETE','at':now(),'elapsed_seconds':time.monotonic()-start})
    except BaseException:
        save_text(d/'FAILURE.txt',traceback.format_exc());raise
    finally:
        make_archive(d,sorted(p.name for p in d.iterdir() if p.is_file()),d/'input.zip','input',binding)
    print(str(d/'input.zip'),flush=True)

def metrics(p,B,y,q):
    return {'kl_B':kl(B,q),'kl_source':kl(p,q),'abs_source':np.abs(p-q),'abs_B':np.abs(B-q),'ce_label':ce(y,q)}

def fit(rep,condition):
    cfg,binding=check_sources();resources(cfg)
    if rep not in range(cfg['replicates']) or condition not in cfg['conditions']:raise ValueError('condition')
    prior_outputs(cfg,binding,rep,cfg['conditions'].index(condition))
    inp=ROOT/'runs'/f'rep{rep}'/'inputs';ir=require_receipt(inp/'receipt.json',inp/'input.zip','input',binding);verify_local_payload(inp,inp/'input.zip')
    if not (inp/'COMPLETED.json').exists():raise ValueError('input generation incomplete')
    input_started=json.loads((inp/'STARTED.json').read_text())
    if input_started.get('replicate')!=rep or input_started.get('source_manifest_sha256')!=binding:raise ValueError('input identity mismatch')
    d=ROOT/'runs'/f'rep{rep}'/condition;d.mkdir(parents=True,exist_ok=False)
    dump(d/'STARTED.json',{'status':'INCOMPLETE_UNLESS_COMPLETED_FILE_EXISTS','at':now(),'replicate':rep,'condition':condition,'source_manifest_sha256':binding,'input_archive_sha256':ir['archive_sha256']})
    start=time.monotonic();learned=condition.startswith('learned');target=condition.split('_')[1]
    console=(d/'console.log').open('x',buffering=1);trajectory=[]
    try:
        with contextlib.redirect_stdout(console),contextlib.redirect_stderr(console):
            train={M:load_training(inp/f'train_M{M}.npz',target) for M in cfg['train_horizons']}
            with np.load(inp/'optimization.npz',allow_pickle=False) as a:p=a['initial_parameters'].copy();batches=a['batches'].copy();horizons=a['horizons'].copy()
            m=np.zeros_like(p);v=np.zeros_like(p)
            shapes={'parameters':(cfg['steps']+1,len(p)),'gradients':(cfg['steps'],len(p)),'first_moments':(cfg['steps']+1,len(p)),'second_moments':(cfg['steps']+1,len(p))}
            arrays={k:np.lib.format.open_memmap(d/(k+'.npy'),mode='w+',dtype=np.float64,shape=s) for k,s in shapes.items()};trajectory=list(arrays.values())
            for a in trajectory:a[:]=np.nan;a.flush()
            arrays['parameters'][0]=p;arrays['first_moments'][0]=m;arrays['second_moments'][0]=v
            for a in trajectory:a.flush()
            with (d/'steps.jsonl').open('x',buffering=1) as log:
                for i in range(cfg['steps']):
                    M=int(horizons[i]);batch=batches[i];a=train[M]
                    loss,g=loss_grad(p,a['H'][batch],a['U'][batch],M,a['target'][batch],learned)
                    previous_parameters=p.copy()
                    p,m,v=adam_step(p,g,m,v,i+1,cfg['optimizer'])
                    if not np.isfinite(loss) or not all(np.isfinite(x).all() for x in [p,g,m,v]):
                        save_npz(d/'FAILED_STEP.npz',previous_parameters=previous_parameters,candidate_parameters=p,gradient=g,first_moments=m,second_moments=v,loss=np.array(loss),step=np.array(i+1))
                        raise FloatingPointError('nonfinite step '+str(i+1))
                    arrays['parameters'][i+1]=p;arrays['gradients'][i]=g;arrays['first_moments'][i+1]=m;arrays['second_moments'][i+1]=v
                    for a in trajectory:a.flush()
                    log.write(json.dumps({'step':i+1,'M':M,'batch_loss_before_update':loss,'gradient_l2':float(np.linalg.norm(g)),'elapsed_seconds':time.monotonic()-start},allow_nan=False)+'\n');log.flush();os.fsync(log.fileno())
                    if (i+1)%100==0:print('step',i+1,'loss',loss,'seconds',time.monotonic()-start,flush=True)
            table={(a['J'],a['C']):[a['n'],a['ones']] for a in json.loads((inp/'empirical_table.json').read_text())};summary={}
            for M in cfg['test_horizons']:
                with np.load(inp/f'test_M{M}.npz',allow_pickle=False) as a:
                    H,U,J,C,B,y,ptrue,words=[a[k] for k in ['H','U','J','C','B','y','p','words']];pt=ptrue[np.arange(len(U)),U]
                    predictions={'model':predict(p,H,U,M,learned),'Bayes':B,'KT':(C+.5)/(J+1),'unigram':(words.sum(1)+1)/(words.shape[1]+2),'half':np.full(len(U),.5),'empirical_JC':table_predict(table,J,C)}
                    payload={'p_terminal':pt,'B':B,'y':y,'J':J,'C':C};cell={}
                    for name,q in predictions.items():
                        if not np.isfinite(q).all():raise FloatingPointError('nonfinite prediction')
                        payload[name+'_q']=q;mm=metrics(pt,B,y,q);cell[name]={}
                        for k,x in mm.items():payload[name+'_'+k]=x;cell[name][k]={'all':summarize(x),'rare_J_le_3':summarize(x[J<=cfg['rare_J_max']])}
                    save_npz(d/f'evaluation_M{M}.npz',**payload);summary[str(M)]=cell
            dump(d/'summary.json',summary);dump(d/'ENVIRONMENT.json',environment())
            dump(d/'COMPLETED.json',{'status':'COMPLETE','at':now(),'steps':cfg['steps'],'elapsed_seconds':time.monotonic()-start})
            print('COMPLETE',flush=True)
    except BaseException:
        save_text(d/'FAILURE.txt',traceback.format_exc());raise
    finally:
        for a in trajectory:a.flush()
        console.flush();os.fsync(console.fileno());console.close()
        make_archive(d,sorted(p.name for p in d.iterdir() if p.is_file()),d/'output.zip','output',binding)
    print(str(d/'output.zip'),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest='command',required=True)
    p=sp.add_parser('prepare');p.add_argument('--replicate',type=int,required=True)
    p=sp.add_parser('fit');p.add_argument('--replicate',type=int,required=True);p.add_argument('--condition',required=True)
    a=ap.parse_args()
    if a.command=='prepare':prepare(a.replicate)
    else:fit(a.replicate,a.condition)
