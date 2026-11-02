"""Finite diagnostics for BAI004 v2, not formal verification."""
import numpy as np,json,hashlib
from pathlib import Path
rng=np.random.default_rng(481220)
max_bridge_ratio=0.;max_count_ratio=0.;max_risk_ratio=0.;pairs=0;DPcases=0

def chain(a,b,e,t):
 P=np.array([[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]])
 x=1/(e/a+2+b/t); pi=np.array([x*e/a,x,x,x*b/t]);beta=float(np.min((P@P)/pi))
 return P,pi,beta

def dp(P,start,s,M,A):
 d=np.zeros((M+1,4));d[0,start]=1
 for j in range(M):
  nd=np.zeros_like(d)
  for i in range(4):
   h=int(i==s)
   nd[h:j+h+1]+=d[:j+1,i,None]*P[i]
  d=nd
 return float(d[:,s]@np.minimum(1,A/(np.arange(M+1)+2)))

params=[]
for _ in range(2000):
 ps=10.**rng.uniform(-7,-.001,4)
 if rng.uniform()<.5:ps=1-ps
 params.append(ps)
for ps in params:
 a,b,e,t=map(float,ps);P,pi,beta=chain(a,b,e,t)
 for factor in [1,3,100]:
  M=int(np.ceil(factor/np.sqrt(beta)))
  lhs=min(1/e,(1+M*t)/b);rhs=12*(1+M*a)/np.sqrt(beta)
  assert lhs<=rhs*(1+1e-12)
  max_bridge_ratio=max(max_bridge_ratio,lhs/rhs);pairs+=1

for ps in [rng.uniform(.02,.98,4) for _ in range(30)]:
 a,b,e,t=map(float,ps);P,pi,beta=chain(a,b,e,t)
 for M in [8,32,64]:
  # Killed W excursion, A visits at0,...,M, including current endpoint.
  K=P[1:,1:];v=np.array([1.,0,0]);N=0.
  for n in range(M+1):N+=v[0];v=v@K
  cap=min(1/e,(1+M*t)/b)
  assert N<=cap+1e-11
  max_count_ratio=max(max_count_ratio,N/cap)
  for A in [.01,.5,2.,10.]:
   got=dp(P,0,1,M,A)
   d0=max(np.sqrt(beta),1/M)
   bound=40*A/M*(1+np.log1p(1/(d0*A)))
   assert got<=bound+1e-11
   max_risk_ratio=max(max_risk_ratio,got/bound);DPcases+=1
   swapped=dp(P,3,2,M,A)
   assert swapped<=bound+1e-11
   DPcases+=1
out=dict(status='PASS',scalar_bridge_cases=pairs,occupation_DP_cases=DPcases,
 max_bridge_ratio=max_bridge_ratio,max_truncated_count_ratio=max_count_ratio,
 max_actual_occupation_to_bound_ratio=max_risk_ratio)
print(json.dumps(out,indent=2))
base=Path('v10_research/binary_arbitrary')
paths=[base/'BAI004_fullsupport_initial_delay_lemmas_v2.md',Path('v10_research/score_precision/SB001_loglog_effective_score_budget_v2.md'),base/'BAI004_diagnostics_v1.py']
(base/'BAI004_source_bindings_v2.json').write_text(json.dumps([dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in paths],indent=2)+'\n')
