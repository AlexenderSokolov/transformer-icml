"""Finite floating-point diagnostics, not universal proof."""
import json, numpy as np
from pathlib import Path
rng=np.random.default_rng(202611020640)
out={'seed':202611020640,'kernels':0,'max_density_envelope_ratio':0.,'max_cumulative_bound_ratio':0.,'max_hit_mean_relative_error':0.,'max_final_bound_ratio':0.,'occupation_cases':0,'positive_beta_kernels':0}
for case in range(1200):
    vals=np.exp(rng.uniform(np.log(1e-5),0,4))
    if case%4==0: vals[rng.integers(4)]=1.
    a,b,e,t=map(float,vals)
    P=np.array([[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]])
    D=e*t+2*a*t+a*b; pi=np.array([e*t,a*t,a*t,a*b])/D
    beta=float(np.min((P@P)/pi[None,:]))
    out['positive_beta_kernels']+=int(beta>0)
    rho=b+e-b*e; m=(rho+a*(2-b))/(a*b); lam=1/m
    Hs=np.linalg.solve(np.eye(3)-P[:3,:3],np.ones(3)); H=max(Hs)
    out['max_hit_mean_relative_error']=max(out['max_hit_mean_relative_error'],abs(Hs[0]/m-1))
    w=np.array([1.,0,0]); v=np.array([0.,0,0,1.]); visit=1.
    for n in range(1,257):
        density=b*w[1]; w=w@P[:3,:3]
        ratio=density/(12*lam*np.exp(-lam*n/16))
        out['max_density_envelope_ratio']=max(out['max_density_envelope_ratio'],ratio)
        v=v@P; visit+=v[3]
        if beta>0:
            bound=10*(1+n*lam)/np.sqrt(beta)
            out['max_cumulative_bound_ratio']=max(out['max_cumulative_bound_ratio'],t*visit/bound)
    if case<180 and beta>0:
        M=64; dp=np.zeros((M+1,4)); dp[0,0]=1
        for n in range(M):
            nxt=np.zeros_like(dp)
            for state in range(4):
                shift=int(state==3)
                nxt[shift:n+shift+1,:]+=dp[:n+1,state,None]*P[state,None,:]
            dp=nxt
        for A0 in (.001,.1,1.,10.,100.):
            actual=float(dp[:,3]@np.minimum(t,A0/(np.arange(M+1)+2)))
            bound=8192*A0/M*(1+np.log1p(1/(np.sqrt(beta)*A0)))
            out['max_final_bound_ratio']=max(out['max_final_bound_ratio'],actual/bound)
            out['occupation_cases']+=1
    out['kernels']+=1
out['limitations']='Finite floating-point checks; no proof, no exact universal verification.'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
