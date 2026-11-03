#!/usr/bin/env python3
"""Synthetic clean-prior diagnostic. No training, attacks, or worst-case estimation."""
import argparse, csv, hashlib, json, platform, sys, time
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
BASE=Path(__file__).resolve().parent

def gate(J,C,D,u):
    accepted=(J>0)&(512*D>=J)
    a=np.divide(C,J,out=np.zeros(J.shape,dtype=float),where=accepted)
    return np.where(u//2==0,a,1-a),accepted

def finish(H,half,u):
    idx=np.arange(len(u));J=H[idx,u].sum(axis=1); d=1-u//2
    C=H[idx,u,d];D=half[idx,u];B=(H[idx,u,1]+1)/(J+2)
    A,accepted=gate(J,C,D,u)
    return dict(H=H,half=half,u=u,J=J,C=C,D=D,B=B,A=A,accepted=accepted)

def from_words(w):
    n,L=w.shape;M=L-2;idx=np.arange(n)
    H=np.zeros((n,4,2),dtype=np.int64);half=np.zeros((n,4),dtype=np.int64)
    for t in range(M):
        u=2*w[:,t]+w[:,t+1];H[idx,u,w[:,t+2]]+=1
        if t<M//2:half[idx,u]+=1
    return finish(H,half,2*w[:,-2]+w[:,-1])

def simulate(p,initial,M,rng=None,uniforms=None):
    p=np.asarray(p);initial=np.asarray(initial)
    if p.shape!=(len(initial),4) or not np.all(np.isfinite(p)) or np.any((p<0)|(p>1)):
        raise ValueError('invalid source probabilities')
    if M<0 or np.any((initial<0)|(initial>3)):raise ValueError('invalid M or initial pair')
    n=len(initial);idx=np.arange(n);u=initial.copy()
    H=np.zeros((n,4,2),dtype=np.int64);half=np.zeros((n,4),dtype=np.int64)
    for t in range(M):
        v=uniforms[t] if uniforms is not None else rng.random(n)
        c=(v<p[idx,u]).astype(np.int64)
        H[idx,u,c]+=1
        if t<M//2:half[idx,u]+=1
        u=2*(u%2)+c
    z=finish(H,half,u);z['p']=p[idx,u]
    assert np.all(H.sum(axis=(1,2))==M)
    assert np.all(half.sum(axis=1)==M//2)
    return z

def metrics(z,M):
    s=1/np.sqrt(M);b=z['B'];a=z['A'];p=z['p'];q=(1-2*s)*a+s
    assert np.all((b>0)&(b<1)) and np.all((a>=0)&(a<=1))
    assert np.all((q>=s)&(q<=1-s))
    h=-b*np.log(b)-(1-b)*np.log1p(-b)
    kl=b*(np.log(b)-np.log(q))+(1-b)*(np.log1p(-b)-np.log1p(-q))
    assert np.all(kl>=-1e-14)
    out=dict(cleanTV_B=abs(b-p),cleanTV_A=abs(a-p),cleanTV_Q=abs(q-p),excess_KL_B_Q=kl,entropy_B=h,expected_logloss_Q=h+kl,gate_rejection=(~z['accepted']).astype(float),J0=(z['J']==0).astype(float),gate_rejection_positive_J=((z['J']>0)&(~z['accepted'])).astype(float))
    assert all(np.all(np.isfinite(v)) for v in out.values())
    return out

def prepare():
    config=dict(protocol='CTO001 clean population synthetic diagnostic v1',horizons=[64,128,256,512,1024,2048,4096],trajectories_per_horizon=20000,seeds=[202611030064,202611030128,202611030256,202611030512,202611031024,202611032048,202611034096],rng='numpy.random.Generator(PCG64(seed))',draw_order='For each M: row probabilities shape (N,4); initial pair integers in [0,4); then M consecutive random(N) transition arrays.',prior='four independent Uniform[0,1) row probabilities and independent uniform initial pair; float64 implementation of continuous uniform prior',batches=100,batch_size=200,batch_partition='consecutive trajectory indices, fixed before simulation',MC_SE='sample standard deviation of 100 batch means (ddof=1) divided by sqrt(100)',interval='mean +/- 1.96 estimated MC SE, approximate, pointwise, not a theorem or simultaneous interval',observed_transitions='exactly M; no prediction label drawn',gate='d=1-first(terminal pair); accept iff J>0 and 512D>=J; designated C/J if accepted else 0; convert to probability of 1',smoothing='Q=(1-2/sqrt(M))*A+1/sqrt(M)',logarithms='natural; log1p(-p) for complementary log',no_A_logloss='A may equal 0 or 1 while B is strictly interior; its population logloss can be infinite. No epsilon clipping.',created_utc=datetime.now(timezone.utc).isoformat())
    (BASE/'config.json').write_text(json.dumps(config,indent=2)+'\n')
    hashes={f:hashlib.sha256((BASE/f).read_bytes()).hexdigest() for f in ['config.json','experiment.py','test_experiment.py']}
    source=BASE.parent/'clean_training_objective_20261103'
    hashes.update({f'../clean_training_objective_20261103/{f}':hashlib.sha256((source/f).read_bytes()).hexdigest() for f in ['CANDIDATE.md','ROOT_ACCEPTANCE.json','ROOT_REPLAY.json']})
    (BASE/'PRE_RUN_HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print('Protocol and hashes saved; no trajectories run.')

def run():
    hashes=json.loads((BASE/'PRE_RUN_HASHES.json').read_text())
    for f,h in hashes.items():assert hashlib.sha256((BASE/f).read_bytes()).hexdigest()==h,f
    cfg=json.loads((BASE/'config.json').read_text());start=time.perf_counter();records=[];batches=[];timings=[]
    for M,seed in zip(cfg['horizons'],cfg['seeds']):
        t=time.perf_counter();rng=np.random.Generator(np.random.PCG64(seed));n=cfg['trajectories_per_horizon']
        p=rng.random((n,4));initial=rng.integers(0,4,size=n)
        z=simulate(p,initial,M,rng=rng);out=metrics(z,M)
        out['weak_tail']=(np.minimum(p,1-p).min(axis=1)<1/np.sqrt(M)).astype(float)
        exact=1-(1-2/np.sqrt(M))**4
        for name,x in out.items():
            bm=x.reshape(cfg['batches'],cfg['batch_size']).mean(axis=1);mean=float(x.mean());se=float(bm.std(ddof=1)/np.sqrt(cfg['batches']))
            records.append(dict(M=M,metric=name,mean=mean,MC_SE=se,approx95_low=mean-1.96*se,approx95_high=mean+1.96*se,exact_weak_tail=exact if name=='weak_tail' else None))
            batches.extend(dict(M=M,metric=name,batch=i,mean=float(v)) for i,v in enumerate(bm))
        timings.append(dict(M=M,seconds=time.perf_counter()-t));print(json.dumps({'M':M,'seconds':timings[-1]['seconds'],'excess':float(out['excess_KL_B_Q'].mean()),'TV_B':float(out['cleanTV_B'].mean()),'TV_Q':float(out['cleanTV_Q'].mean())}),flush=True)
    for filename,rows in [('aggregates.csv',records),('batch_means.csv',batches)]:
        with (BASE/filename).open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    result=dict(environment=dict(python=sys.version,numpy=np.__version__,platform=platform.platform()),runtime_seconds=time.perf_counter()-start,timings=timings,results=records,config_sha256=hashes['config.json'])
    (BASE/'results.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['prepare','run']);a=parser.parse_args()
    prepare() if a.command=='prepare' else run()
