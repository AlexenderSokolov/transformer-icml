"""Fixed inputs/checkpoint only: no RNG and no Model.__init__."""
import sys,os,hashlib,json,platform
from pathlib import Path
import numpy as np,mpmath as mp
ROOT=Path(__file__).resolve().parents[3];C=ROOT/'v10_research/learned_position_pilot_20261103';sys.path.insert(0,str(C));import pilot
path=C/'smoke_v1/checkpoints/half_edit_200.npz';result=json.load(open(Path(__file__).resolve().parents[1]/'trained_results.json'));digest=hashlib.sha256(path.read_bytes()).hexdigest();manifest=json.load(open(C/'smoke_v1/ARTIFACT_HASHES.json'));assert digest==manifest['checkpoints/half_edit_200.npz']==result['sources_sha256'][str(path.relative_to(ROOT))]
z=np.load(path,allow_pickle=False);assert str(z['mode'])=='half';param={k:z[k].copy() for k in ['a','W','b','v','c']};assert all(np.isfinite(v).all() for v in param.values());assert param['a'].shape==(2,8) and param['W'].shape==(9,32) and param['b'].shape==(32,) and param['v'].shape==(32,) and param['c'].shape==(1,)
def forbidden(*a,**k):raise AssertionError('Model.__init__ forbidden')
pilot.Model.__init__=forbidden;model=pilot.Model.__new__(pilot.Model);model.mode='half';model.params=param
M=1025;L=M//2;A=np.ones(M+2,dtype=np.int8);B=A.copy();A[[515,518]]=0;B[[519,522]]=0
assert int(np.sum(A!=B))==4 and tuple(A[-2:])==tuple(B[-2:])==(1,1)
def literal(w):
 u=tuple(map(int,w[-2:]));bank=[0,0,0,0];seq=[]
 for i in range(M):
  x,y,v=map(int,w[i:i+3]);match=(x,y)==u;bank[0]+=int(match);bank[1]+=int(match)*v;bank[2]+=int(match and i<L);bank[3]+=int(match and i<L)*v;seq.append((int(match and v==0),int(match and v==1)))
 return tuple(bank),seq
assert literal(A)[0]==literal(B)[0]==(1021,1019,512,512)
alpha=np.zeros((3,M));alpha[0]=1/M;alpha[1,:L]=1/L;alpha[2,L:]=1/(M-L)
def manual(w):
 e=np.array([literal(a)[1] for a in w],dtype=np.float64);f=np.einsum('hi,bic->bhc',alpha,e,optimize=True);x=np.column_stack([f.reshape(len(w),6),w[:,-2:],np.full(len(w),1/M)]);pre=x@param['W']+param['b'];hidden=np.tanh(pre);r=hidden@param['v']+param['c'][0];s=np.empty_like(r);pos=r>=0;s[pos]=1/(1+np.exp(-r[pos]));ex=np.exp(r[~pos]);s[~pos]=ex/(1+ex);eps=(M+2.)**-2;q=eps+(1-2*eps)*s;t=340/341;CE=-t*np.log(q)-(1-t)*np.log1p(-q);return x,hidden,r,s,q,CE
mp.mp.dps=120
def exact(v):
 a,b=float(v).as_integer_ratio();return mp.mpf(a)/b
x=[mp.mpf(2)/M,mp.mpf(1019)/M,mp.mpf(0),mp.mpf(1),mp.mpf(2)/(M-L),mp.mpf(507)/(M-L),mp.mpf(1),mp.mpf(1),mp.mpf(1)/M];h=[mp.tanh(sum(x[i]*exact(param['W'][i,j]) for i in range(9))+exact(param['b'][j])) for j in range(32)];r0=sum(h[j]*exact(param['v'][j]) for j in range(32))+exact(param['c'][0]);ep=mp.mpf(1)/(M+2)**2;q0=ep+(1-2*ep)/(1+mp.exp(-r0));t=mp.mpf(340)/341;ce0=-t*mp.log(q0)-(1-t)*mp.log(1-q0)
for key,value in [('logit',r0),('prediction',q0),('ce',ce0)]:assert abs(mp.mpf(result['ideal_math'][key])-value)<mp.mpf('1e-88'),(key,result['ideal_math'][key],mp.nstr(value,100))
print('checkpoint sha256',digest,'M',M,'protected endpoint 11; bank (1021,1019,512,512); Hamming 4')
print('environment',sys.version,'NumPy',np.__version__,'mpmath',mp.__version__,'mp.dps',mp.mp.dps,'platform',platform.platform(),'thread env',{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']});np.show_config()
for name,batch in [('AB',np.stack([A,B])),('BA',np.stack([B,A])),('AA',np.stack([A,A])),('BB',np.stack([B,B])),('A',A[None,:]),('B',B[None,:])]:
 assert batch.dtype==np.int8 and batch.flags.c_contiguous;q,cache=model.forward(batch,cache=True);x,h,r,s,p,ce=manual(batch);actualce=pilot.cross_entropy(np.full(len(batch),340/341),q);assert np.array_equal(cache['x'],x) and np.array_equal(cache['hidden'],h) and np.array_equal(cache['s'],s) and np.array_equal(q,p) and np.array_equal(actualce,ce)
 old=result['batches'][name];assert old['shape']==list(batch.shape) and old['strides']==list(batch.strides)
 for i,row in enumerate(old['rows']):
  assert row['features_hex']==[float(t).hex() for t in x[i]] and row['hidden_hex']==[float(t).hex() for t in h[i]] and row['logit_hex']==float(r[i]).hex() and row['prediction_hex']==float(q[i]).hex() and row['ce_hex']==float(ce[i]).hex()
 print(name,'input rail hex',[float(v).hex() for v in x[:,1]],'logit hex',[float(v).hex() for v in r],'prediction hex',[float(v).hex() for v in q],'CE hex',[float(v).hex() for v in ce],'absolute logit errors',[mp.nstr(abs(exact(v)-r0),18) for v in r])
print('ideal 120-digit logit',mp.nstr(r0,50),'q',mp.nstr(q0,50),'CE',mp.nstr(ce0,50),'q output same for all tested batches; no generalization implied')
print('independent pipeline shares NumPy einsum and matrix kernels, so bitwise cross-check is not an independent backend implementation; mpmath comparison is high precision, not interval certification')
