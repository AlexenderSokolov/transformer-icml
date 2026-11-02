"""Finite diagnostics, not proof or independent validation."""
import json, hashlib
from pathlib import Path
import numpy as np

def occupation(P, initial, M, A):
    n=len(P); result=0.; low=[]
    for s in range(n):
        d=np.zeros((M+1,n));d[0,initial]=1
        for time in range(M):
            nd=np.zeros_like(d)
            for i in range(n):
                shift=int(i==s)
                nd[shift:time+shift+1,:]+=d[:time+1,i,None]*P[i]
            d=nd
        result+=np.sum(d[:,s]*np.minimum(1,A/(np.arange(M+1)+2)))
        low.append(d[:,s].tolist())
    return result,low

rows=[]
for eta,b,t,e,M in [(.5,.5,.5,.001,64),(.25,.25,.75,.1,128),(.2,.7,.3,.9,64),(.5,.5,.5,0,512)]:
    delta=eta**3;R=np.array([[0,1-b,b],[1,0,0],[0,t,1-t]])
    P=np.array([[1,0,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]])
    beta=e*min(t,1-b)
    for start in [1,2,3]:
        A=2.0
        ref,rd=occupation(R,start-1,M,A)
        # Active contributions only from original absorbing source.
        orig,od=occupation(P,start,M,A)
        active=sum(np.sum(np.array(od[s])*np.minimum(1,A/(np.arange(M+1)+2))) for s in [1,2,3])
        assert active<=ref+1e-12
        assert ref<=16*A/(delta*M)+3*np.exp(-delta*M/64)+1e-12
        assert np.min(P@P-beta*np.array([1,0,0,0]))>=-1e-12
        rows.append(dict(eta=eta,b=b,t=t,e=e,M=M,start=start,beta=beta,
            active_functional=float(active),reflected_functional=float(ref),
            reflection_slack=float(ref-active),
            core_block_B_min=float((R@R)[:,1].min()),
            analytic_bound=float(16*A/(delta*M)+3*np.exp(-delta*M/64))))

# Exhaustive arithmetic checks of absorbing-terminal floor criterion.
arith=0
for M in [64,65,128,1024]:
 for Q in [16,32,64]:
  for kappa in [1,2,9]:
   for J in range(M+1):
    den=M+(kappa-1)*J
    floor=(Q*kappa*J)//den
    if floor==0:
     assert J<2*M/(kappa*Q)
    else:
     assert J>0
    arith+=1
out=dict(status='PASS',occupation_cases=rows,arithmetic_checks=arith)
print(json.dumps(out,indent=2))
base=Path('v10_research/binary_arbitrary')
paths=[base/'BAI002_absorbing_active_core_upper_v1.md',Path('v10_research/score_precision/SB001_loglog_effective_score_budget_v2.md'),base/'BAI001_arbitrary_initialization_obstructions_v1.md']
(base/'BAI002_source_bindings_v1.json').write_text(json.dumps([dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in paths],indent=2)+'\n')
