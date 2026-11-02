"""Finite corroboration only: not a proof or original-network execution."""
import itertools, json, math, hashlib
from pathlib import Path
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(20261102)
out={"scope":"Finite corroboration only; no uniform theorem or emitted-network certification"}
# Arbitrary nonlinear Boolean tables, exact replacement majorants, top-m union.
max_vratio=max_dratio=max_tailratio=0.; cases=0
for N in range(4,9):
    X=np.array(list(itertools.product([0,1],repeat=N)))
    for rep in range(8):
        tables=rng.normal(size=(4,2**N)); cs=[]
        for f in tables:
            cs.append([max(abs(f[k]-f[k^(1<<(N-1-i))]) for k in range(2**N)) for i in range(N)])
        cs=np.array(cs); B=max(cs.sum(axis=1)); m=1+(rep%max(1,N//3))
        U=sorted(set([0]+[int(i) for c in cs for i in np.argsort(-c,kind='stable')[:m]]))
        free=[i for i in range(N) if i not in U]
        for y in itertools.product([0,1],repeat=len(U)):
            ids=np.where(np.all(X[:,U]==y,axis=1))[0]
            bits=X[ids][:,free]; ones=bits.sum(axis=1); nf=len(free)
            for p in [.25,.4,.5,.75]:
                prob=p**ones*(1-p)**(nf-ones)
                score=ones/p-(nf-ones)/(1-p)
                for f,c in zip(tables,cs):
                    mu=prob@f[ids]; var=prob@((f[ids]-mu)**2); deriv=(prob*score)@f[ids]
                    max_vratio=max(max_vratio,var/(B*B/(2*m)))
                    max_dratio=max(max_dratio,abs(deriv)/B)
                    if free: max_tailratio=max(max_tailratio,float(max(c[free]))/(B/m))
                    assert var<=B*B/(2*m)+1e-10 and abs(deriv)<=B+1e-10
                    cases+=1
out['conditional_boolean_tables']={'cases':cases,'max_variance_bound_ratio':max_vratio,'max_derivative_bound_ratio':max_dratio,'max_tail_bound_ratio':max_tailratio}
# Stable integration of truncated posteriors, including boundary modes.
max_density_ratio=0.; accepted=0; boundary=0
for n in [1,2,3,4,8,16,32,100,1000,10000]:
    ts=sorted(set([0,n]+list(range(n+1)) if n<=100 else [0,n]+[int(n*x) for x in np.linspace(.15,.85,151)]))
    for t in ts:
        z=t/n; p0=min(.75,max(.25,z))
        ell=lambda p:t*math.log(p)+(n-t)*math.log1p(-p)
        peak=ell(p0)
        g=lambda p:math.exp(ell(p)-peak)
        norm=quad(g,.25,.75,epsabs=1e-13,points=[p0])[0]
        lo=max(.25,z-3/math.sqrt(n)); hi=min(.75,z+3/math.sqrt(n))
        mass=quad(g,lo,hi,epsabs=1e-13,points=[p0] if lo<=p0<=hi else None)[0]/norm if hi>=lo else 0.
        if mass>=.99:
            ratio=1/norm/(128*math.sqrt(n)); max_density_ratio=max(max_density_ratio,ratio)
            assert ratio<=1+1e-10
            accepted+=1; boundary+=int(p0 in [.25,.75])
out['posterior']={'patterns_in_T':accepted,'boundary_modes_in_T':boundary,'max_density_bound_ratio':max_density_ratio}
# Row-sum bound includes all early coins and local-window multiplicity.
max_row_error=0.; max_local_ratio=0.
for T in [4,8,20,60]:
    A=np.tril(np.ones((T,T)))/np.arange(1,T+1)[:,None]
    for a,bb in [(.1,.3),(1,1),(2,.7)]:
        H=a*np.eye(T)+bb*A
        for depth in [1,2,4,8]:
            power=np.linalg.matrix_power(H,depth)
            max_row_error=max(max_row_error,float(np.max(abs(power.sum(axis=1)/(a+bb)**depth-1))))
            for r in [1,2,5]:
                c=np.array([sum(power[-1,i:min(T-1,i+r)]) for i in range(T-1)])
                ratio=sum(c)/(r*(a+bb)**depth); max_local_ratio=max(max_local_ratio,float(ratio))
                assert ratio<=1+1e-10
out['matrix_row_sums']={'max_relative_error':max_row_error,'max_local_influence_sum_ratio':max_local_ratio}
# Mesh and integer-box counts at adversarial translations and noninteger E.
for E in [0,.1,.5,1,2.7,100]:
    K=math.ceil(2*E+6)+1
    for center in np.linspace(-10,10,1001):
        count=max(0,math.floor(center+E+3)-math.ceil(center-E-3)+1)
        assert count<=K
out['label_box_counts']='PASS'
out['status']='PASS'
(ROOT/'IR001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
