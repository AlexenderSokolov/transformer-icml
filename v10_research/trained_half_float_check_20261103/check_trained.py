#!/usr/bin/env python3
"""Fixed trained checkpoint on fixed words; no RNG, model constructor, or training."""
import os,sys,json,platform,hashlib
from pathlib import Path
from fractions import Fraction
import numpy as np
import mpmath as mp
R=Path(__file__).resolve().parents[2];pilotdir=R/'v10_research/learned_position_pilot_20261103';sys.path.insert(0,str(pilotdir));import pilot
OUT=Path(__file__).resolve().parent
checkpoint=pilotdir/'smoke_v1/checkpoints/half_edit_200.npz'
sources=[Path(__file__),pilotdir/'pilot.py',checkpoint,pilotdir/'smoke_v1/ARTIFACT_HASHES.json',R/'v10_research/float_readout_bound_20261103/REPORT.md',R/'v10_research/float_readout_bound_20261103/bounds.json',R/'v10_research/float_bank_deterministic_20261103/review_independent/check_fixed.py']
hash_file=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((pilotdir/'smoke_v1/ARTIFACT_HASHES.json').read_text()); assert hash_file(checkpoint)==manifest['checkpoints/half_edit_200.npz']
with np.load(checkpoint,allow_pickle=False) as z:
 assert str(z['mode'])=='half';params={k:z[k].copy() for k in ('a','W','b','v','c')}
assert all(np.all(np.isfinite(p)) for p in params.values())
def reject_constructor(*args,**kwargs):raise AssertionError('Random-initializing constructor must not be called')
pilot.Model.__init__=reject_constructor
model=pilot.Model.__new__(pilot.Model);model.mode='half';model.params=params
M=1025;L=M//2;A=np.ones(M+2,dtype=np.int8);B=A.copy();A[[515,518]]=0;B[[519,522]]=0
# Independent literal triple counting, as Python ints, to avoid dtype overflow.
def direct_bank(w):
 J=C=D=E=0;u=tuple(map(int,w[-2:]));rows=[]
 for i in range(M):
  x,y,z=map(int,w[i:i+3]);selected=(x,y)==u;J+=selected;C+=selected*z;D+=selected*(i<L);E+=selected*z*(i<L);rows.append((int(selected and not z),int(selected and z)))
 return (J,C,D,E),rows
ba,ea=direct_bank(A);bb,eb=direct_bank(B);assert ba==bb==(1021,1019,512,512);assert int(np.sum(A!=B))==4
# Independent implementation of the forward's data pipeline and operations.
def independent_forward(batch):
 arr=np.asarray([direct_bank(row)[1] for row in batch],dtype=np.float64)
 alpha=np.zeros((3,M),dtype=np.float64);alpha[0,:]=1/M;alpha[1,:L]=1/L;alpha[2,L:]=1/(M-L)
 f=np.einsum('hi,bic->bhc',alpha,arr,optimize=True)
 x=np.column_stack((f.reshape(len(batch),6),batch[:,-2:],np.full(len(batch),1/M)))
 pre=x@params['W']+params['b'];hidden=np.tanh(pre);logit=hidden@params['v']+params['c'][0]
 sig=np.empty_like(logit);pos=logit>=0;sig[pos]=1/(1+np.exp(-logit[pos]));ex=np.exp(logit[~pos]);sig[~pos]=ex/(1+ex)
 eps=(M+2.)**-2;q=eps+(1-2*eps)*sig
 return x,pre,hidden,logit,sig,q
mp.mp.dps=100
mpf=lambda f:mp.mpf(float(f).as_integer_ratio()[0])/float(f).as_integer_ratio()[1]
exactx=[mp.mpf(2)/M,mp.mpf(1019)/M,mp.mpf(0),mp.mpf(1),mp.mpf(2)/(M-L),mp.mpf(507)/(M-L),mp.mpf(1),mp.mpf(1),mp.mpf(1)/M]
ideal_hidden=[mp.tanh(sum(exactx[i]*mpf(params['W'][i,j]) for i in range(9))+mpf(params['b'][j])) for j in range(32)]
ideal_logit=sum(ideal_hidden[j]*mpf(params['v'][j]) for j in range(32))+mpf(params['c'][0]);eps=mp.mpf(1)/(M+2)**2;ideal_q=eps+(1-2*eps)/(1+mp.exp(-ideal_logit));t=mp.mpf(340)/341;ideal_ce=-t*mp.log(ideal_q)-(1-t)*mp.log(1-ideal_q)
source_hashes={str(p.relative_to(R)):hash_file(p) for p in sources};bound=json.loads((R/'v10_research/float_readout_bound_20261103/bounds.json').read_text());entry=next(x for x in bound['checkpoints'] if x['path']==str(checkpoint.relative_to(R)));assert entry['sha256']==hash_file(checkpoint);bound_m=next(x for x in entry['results'] if x['M']==M)
print('NUMPY CONFIGURATION',flush=True);np.show_config();print('NUMPY RUNTIME',flush=True);np.show_runtime()
res={'scope':'Deterministic two fixed words, one trained checkpoint, no sampling, no model initialization or training; no global guarantee','environment':{'python':sys.version,'numpy':np.__version__,'mpmath':mp.__version__,'mp_dps':mp.mp.dps,'platform':platform.platform(),'threads':{k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')}},'sources_sha256':source_hashes,'M':M,'editable_hamming':4,'zeros_A':[515,518],'zeros_B':[519,522],'bank':ba,'target_exact':'340/341','ideal_math':{'logit':mp.nstr(ideal_logit,90),'prediction':mp.nstr(ideal_q,90),'ce':mp.nstr(ideal_ce,90)},'conditional_bound':bound_m,'batches':{}}
for name, batch in [('AB',np.stack([A,B])),('BA',np.stack([B,A])),('AA',np.stack([A,A])),('BB',np.stack([B,B])),('A',A[None,:]),('B',B[None,:])]:
 assert batch.dtype==np.int8 and batch.flags.c_contiguous
 q,c=model.forward(batch,cache=True);x,pre,h,logit,sig,indq=independent_forward(batch)
 assert np.array_equal(x.view(np.uint64),c['x'].view(np.uint64));assert np.array_equal(h.view(np.uint64),c['hidden'].view(np.uint64));assert np.array_equal(sig.view(np.uint64),c['s'].view(np.uint64));assert np.array_equal(indq.view(np.uint64),q.view(np.uint64))
 target=pilot.statistics(A[None,:])['B'][0];loss=pilot.cross_entropy(np.full(len(batch),target),q)
 rows=[]
 for i in range(len(batch)):
  rows.append({'features_hex':[float(v).hex() for v in x[i]],'preactivation_hex':[float(v).hex() for v in pre[i]],'hidden_hex':[float(v).hex() for v in h[i]],'logit_hex':float(logit[i]).hex(),'logit':float(logit[i]),'prediction_hex':float(q[i]).hex(),'prediction':float(q[i]),'target_float_hex':float(target).hex(),'ce_hex':float(loss[i]).hex(),'ce':float(loss[i]),'absolute_logit_error_vs_100_digit_ideal':mp.nstr(abs(mpf(logit[i])-ideal_logit),35),'absolute_q_error_vs_100_digit_ideal':mp.nstr(abs(mpf(q[i])-ideal_q),35),'absolute_ce_error_vs_100_digit_ideal':mp.nstr(abs(mpf(loss[i])-ideal_ce),35)})
 res['batches'][name]={'shape':list(batch.shape),'strides':list(batch.strides),'rows':rows}
 print(name, 'features1',[r['features_hex'][1] for r in rows], 'logit',[r['logit_hex'] for r in rows], 'q',[r['prediction_hex'] for r in rows], 'CE',[r['ce_hex'] for r in rows], 'abs_logit_error',[r['absolute_logit_error_vs_100_digit_ideal'] for r in rows],flush=True)
print('target',float(target).hex(),'ideal logit',mp.nstr(ideal_logit,35),'conditional R at tau_h=0',bound_m['logit_error_at_tau_zero'],flush=True)
print('INDEPENDENT FORWARD MATCH: bitwise x, tanh hidden, sigmoid and q for all batches; bounds comparisons are diagnostic only',flush=True)
(OUT/'trained_results.json').write_text(json.dumps(res,indent=2)+'\n')
