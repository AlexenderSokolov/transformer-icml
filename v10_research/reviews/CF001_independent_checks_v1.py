#!/usr/bin/env python3
"""Independent finite checks of CF001 interfaces; not a universal proof/emitter."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import random, math, json, hashlib
rng=random.Random(202611020439)
R={'status':'PASS','bank_cases':0,'compiled_cases':0,'scalar_cases':0,'mask_rows':0,'new_rejects':0}
names=('q1','v1','q2','v2','hv','h0','alpha','nu','f','rho')
@lru_cache(None)
def weights(M,K,h):
 p0=4*h+4*(M+K+3).bit_length()+64; P=4*(h+3)+256; D=1<<P
 logs=[]
 for d in (3,2):
  z=sum((F(2,(2*j+1)*d**(2*j+1)) for j in range(p0)),F(0))
  num=z.numerator*(1<<p0)//z.denominator
  logs.append(num*D//(1<<p0))
 a=2; J=8*(2*a)**2+2+P; cache={}
 for s in (0,logs[0],2*logs[0],logs[1],sum(logs)):
  t=D; w=D
  for j in range(1,J+1): t=t*(s+a*D)//(j*D); w+=t
  cache[s]=w
 return logs,D,cache

def banks(x,K,s,h,compile=False):
 Q=1<<h; M=len(x)-2; out={k:[F(0)]*(1 if k=='rho' else K) for k in names}; actual={}
 if compile: logs,D,cache=weights(M,K,h)
 for tag,ns in [('p1',('q1','v1')),('p2',('q2','v2')),('t',('hv','h0')),('z',('alpha','nu','f','rho'))]:
  sums={k:[0]*len(out[k]) for k in ns}; fs={k:[0]*len(out[k]) for k in ns}; den=fd=0
  for i in range(2,len(x)):
   u,v,c=x[i-2:i+1]; a,b=s; z=i==2
   if tag in ('p1','p2'):
    lam=1 if tag=='p1' else 2; iw=(1+(u==a))*(1+lam*(v==b)); bits={ns[0]:c,ns[1]:u}
    score=(logs[0]*(u==a)+logs[lam-1]*(v==b)) if compile else 0
   elif tag=='t':
    iw=1+(u==b); bits={'hv':v}; score=logs[0]*(u==b) if compile else 0
    if z: bits['h0']=v
   else:
    iw=1; bits={'alpha':u,'nu':v};score=0
    if z: bits.update(f=v,rho=0)
   den+=iw
   if compile: fw=cache[score];fd+=fw
   for k,j in bits.items():
    sums[k][j]+=iw
    if compile: fs[k][j]+=fw
  for k in ns:
   out[k]=[F(v,den) for v in sums[k]]
   if compile:
    actual[k]=[(D*v//fd)//(D//Q) for v in fs[k]]
    assert all(0<=v<=Q and abs(F(v,Q)-r)<F(2,Q) for v,r in zip(actual[k],out[k]))
 return out,actual

def test(x,K,s,h,compile=False):
 M=len(x)-2;Q=1<<h; ideal,m=banks(x,K,s,h,compile)
 if not compile:
  for k,arr in ideal.items():
   m[k]=[]
   for val in arr:
    v=Q*val;lo=max(0,math.ceil(v-2));hi=min(Q,math.floor(v+2))
    m[k].append(rng.choice([lo,hi,rng.randint(lo,hi)]))
 C=[0]*K; H=[0]*K
 for i in range(2,len(x)):
  H[x[i]]+=1
  if tuple(x[i-2:i])==s:C[x[i]]+=1
 a,b=s;dt=Q+m['alpha'][b]
 ds=[2*Q*(Q+lam*m['nu'][b])//(2*Q-m[k][a]) for lam,k in [(1,'v1'),(2,'v2')]]
 ac=[];yc=[]
 for c in range(K):
  g=dt*m['hv'][c]//Q-m['nu'][c]+m['rho'][0]*(tuple(x[-2:])==(b,c))-(dt*m['h0'][c]//Q-m['f'][c])
  ac.append(max(0,min(Q,ds[1]*m['q2'][c]//Q-ds[0]*m['q1'][c]//Q-g)))
  yc.append(max(0,min(Q,m['nu'][c]-m['f'][c]+m['rho'][0]*(x[-1]==c))))
 assert all(abs(F(v,Q)-F(c,M))<=F(76,Q) for v,c in zip(ac,C))
 assert all(abs(F(v,Q)-F(c,M))<=F(6,Q) for v,c in zip(yc,H))
 def norm(v):
  w=[Q*z//sum(v) for z in v[:-1]];return w+[Q-sum(w)]
 U=[M*v+Q for v in ac]; V=[M*v+Q for v in yc]; qm=norm(U);bm=norm(V)
 A=sum(C)+K; E=F(76*K*M,Q);amin=max(F(K),F(sum(U),Q)-E);eobs=min(F(1),E/amin)+F(8*K,Q)
 dq=sum(abs(F(u,Q)-F(c+1,A)) for u,c in zip(qm,C))/2
 db=sum(abs(F(u,Q)-F(c+1,M+K)) for u,c in zip(bm,H))/2
 assert dq<=min(F(1),E/A)+F(K,Q) and db<=F(7*K,Q) and dq+db<=eobs
 assert K<=amin<=A and amin>=A-2*E
 dhat=F(sum(abs(u-v) for u,v in zip(qm,bm)),2*Q);z=dhat-eobs
 pool=z<=0 or z*z<=min(F(1),F(K**5,M+1),F(4096*K,amin))
 d=sum(abs(F(c+1,A)-F(t+1,M+K)) for c,t in zip(C,H))/2
 old=d*d<=min(F(1),F(K**5,M+1),F(4096*K,A))
 assert not old or pool
 R['new_rejects']+=not pool;R['compiled_cases' if compile else 'bank_cases']+=1

for K in (3,4,7):
 for M in (64,65,127,1024,4096):
  for h in (4,8,16,24):
   for pat in ([0],[0,0,1,1],list(range(K)),None):
    x=[rng.randrange(K) if pat is None else pat[i%len(pat)] for i in range(M+2)]
    test(x,K,tuple(x[-2:]),h,compile=(K==3 and M<=127))
    for _ in range(3):test(x,K,(rng.randrange(K),rng.randrange(K)),h)
for M in range(64,1000):
 for t in range(1,M+4):
  size=1 if t<3 else min(t,M+2)-2
  assert 3*size>=t;R['mask_rows']+=1
for _ in range(50000):
 M=rng.choice([64,65,100,256,1024,10**6,10**12,10**30]);Q=2**rng.randint(4,150)
 beta=rng.choice([0,1,1/16,1/M,10**rng.uniform(-35,0)]);b=max(beta,1/M)
 x=Q/(M*b);y=M/Q;W=(1+math.log1p(x))/Q; f=1/math.sqrt(M)
 if beta>1/16:assert W<=1/Q+2*f+1e-15
 elif Q>M/4 or Q>M**.75:assert W<=5*f+1e-15
 else:assert W<=1/Q+24*math.log1p(min(x,y)/8)/Q+1e-15
 R['scalar_cases']+=1
R['scope']='Exact rational arbitrary compatible master errors and new positive-shift finite head examples; floating scalar sweep; not a proof, generic compiler certificate, resource measurement or risk simulation.'
R['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(R,indent=2))
