"""Finite floating-point corroboration of BAI003; not a proof."""
import json, hashlib
from pathlib import Path
import numpy as np

def weighted(R,start,target,q,M):
 d=np.zeros((M+1,3));d[0,start]=1
 for j in range(M):
  nd=np.zeros_like(d)
  for i in range(3):
   h=int(i==target)
   nd[h:j+h+1]+=d[:j+1,i,None]*R[i]
  d=nd
 return float(np.sum(d[:,target]*q/(1+q*np.arange(M+1))))

rng=np.random.default_rng(39821)
params=[(b,t) for b in [0,1e-7,.01,.5,.99,1] for t in [0,1e-7,.01,.5,.99,1]]
params += [tuple(rng.uniform(.001,.999,2)) for _ in range(80)]
params += [(10.**(-u),10.**(-v)) for u,v in rng.uniform(0,8,(30,2))]
worst_ratio=0.;min_reduction_slack=1.;max_coefficient_violation=0.;count=0
for b,t in params:
 R=np.array([[0,1-b,b],[1,0,0],[0,t,1-t]])
 for M in [8,16,64]:
  N=M+2; DA=np.zeros(N+1);DC=np.zeros(N+1);L=np.zeros(N+1)
  P=np.eye(3)
  for n in range(1,N+1):
   if n%2: DA[n]=b*(1-b)**((n-1)//2)
   if n>=2:DC[n]=t*(1-t)**(n-2)
   P=P@R
   L[n]=(np.trace(P)-(1-t)**n-(2*(1-b)**(n//2) if n%2==0 else 0))/n
   max_coefficient_violation=max(max_coefficient_violation,-L[n],L[n]-min(b,t,3/n))
  F=np.convolve(DA,DC)[:N+1];DCL=np.convolve(DC,L);DAL=np.convolve(DA,L)
  for start in range(3):
   for target,q in [(0,b),(2,t)]:
    w=weighted(R,start,target,q,M)
    assert w<=64/M+1e-11
    worst_ratio=max(worst_ratio,w*M/64);count+=1
    if start==1:continue
    if target==0:
     bound=L[M]+(b*(1-b)**(M//2)/(1+b*M/2) if M%2==0 else 0) if start==0 else DCL[M]+F[M+1]
    else:
     bound=L[M]+t*(1-t)**M/(1+t*M) if start==2 else DAL[M]+F[M+2]
    min_reduction_slack=min(min_reduction_slack,float(bound-w))
    assert w<=bound+1e-10,(b,t,M,start,target,w,bound)
  assert DCL[M]<=15/M+1e-11
  assert DAL[M]<=41/M+1e-11
  assert F[M+1]<=8/(M+1)+1e-11
assert max_coefficient_violation<1e-10
result=dict(status='PASS',parameter_pairs=len(params),weighted_DP_cases=count,
 max_ratio_to_uniform_bound=worst_ratio,min_run_reduction_slack=min_reduction_slack,
 max_renewal_coefficient_violation=max_coefficient_violation)
print(json.dumps(result,indent=2))
base=Path('v10_research/binary_arbitrary')
paths=[base/'BAI003_uniform_absorbing_binary_upper_v1.md',Path('v10_research/score_precision/SB001_loglog_effective_score_budget_v2.md'),Path('v10_research/binary_upper/BU001_weighted_return_upper_v2.md')]
(base/'BAI003_source_bindings_v1.json').write_text(json.dumps([dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in paths],indent=2)+'\n')
