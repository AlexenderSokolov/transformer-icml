"""Additional v3 opposite-crossing exact-convolution diagnostics."""
import numpy as np,json,hashlib
from pathlib import Path
rng=np.random.default_rng(991483)
def series(P,start,target,M,A):
 d=np.zeros((M+1,4));d[0,start]=1;out=[]
 for j in range(M+1):
  out.append(float(d[:,target]@np.minimum(1,A/(np.arange(M+1)+2))))
  if j==M:break
  nd=np.zeros_like(d)
  for i in range(4):
   h=int(i==target);nd[h:j+h+1]+=d[:j+1,i,None]*P[i]
  d=nd
 return np.array(out)
maxerr=0.;cases=0;maxratio=0.
params=[rng.uniform(.0001,.9999,4) for _ in range(40)]
params += [np.array([.001,b,.4,t]) for b in [1e-8,.5,1-1e-8] for t in [1e-8,.1,1-1e-8]]
for a,b,e,t in params:
 P=np.array([[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]])
 x=1/(e/a+2+b/t);pi=np.array([x*e/a,x,x,x*b/t]);beta=np.min((P@P)/pi)
 for M in [8,16,64]:
  for A in [.01,.5,2.,10.]:
   f=series(P,0,1,M,A);g=series(P,0,2,M,A)
   U=np.zeros(M+1);U[1]=1-b
   for l in range(2,M+1):U[l]=b*t*(1-t)**(l-2)
   conv=np.convolve(f,U)[:M+1]
   err=float(np.max(np.abs(conv-g)));maxerr=max(maxerr,err)
   assert err<2e-12
   d0=max(np.sqrt(beta),1/M);bound=100*A/M*(1+np.log1p(1/(d0*A)))
   assert g[M]<=bound+1e-12
   maxratio=max(maxratio,g[M]/bound);cases+=1
out=dict(status='PASS',phase_convolution_cases=cases,max_exact_identity_error=maxerr,max_actual_bound_ratio=float(maxratio))
print(json.dumps(out,indent=2))
base=Path('v10_research/binary_arbitrary')
paths=[base/'BAI004_fullsupport_initial_delay_lemmas_v3.md',base/'BAI004_diagnostics_v1.py',base/'BAI004_diagnostics_v1.json',base/'BAI004_diagnostics_v2.py',Path('v10_research/score_precision/SB001_loglog_effective_score_budget_v2.md')]
(base/'BAI004_source_bindings_v3.json').write_text(json.dumps([dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in paths],indent=2)+'\n')
