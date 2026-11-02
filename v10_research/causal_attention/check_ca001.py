#!/usr/bin/env python3
"""Finite diagnostics, not proof or all-operations arithmetic certification."""
import json, math, random
from pathlib import Path
random.seed(1001)
checks={}
max_ratio=0.0
for n in (2,3,8,25,80):
    A=[[1/(t+1) if i<=t else 0.0 for i in range(n)] for t in range(n)]
    P=[row[:] for row in A]
    for k in range(1,7):
        for t in range(n):
            for i in range(t+1):
                rhs=(1+math.log((t+1)/(i+1)))**(k-1)/(t+1)
                assert P[t][i]<=rhs+1e-12
                max_ratio=max(max_ratio,P[t][i]/rhs)
        P=[[sum(A[t][u]*P[u][i] for u in range(i,t+1)) if i<=t else 0.0 for i in range(n)] for t in range(n)]
checks['triangular_power_envelope']={'pass':True,'max_ratio':max_ratio,'sizes':[2,3,8,25,80],'depths':list(range(1,7))}
for n in (2,10,100,1000):
    for m in range(11):
        integral=sum(math.comb(m,k)*math.factorial(k) for k in range(m+1))
        finite=sum((1+math.log(n/i))**m for i in range(1,n+1))/n
        assert finite<=integral+1e-10
checks['squared_log_integral']={'pass':True,'powers':list(range(11))}
# h -> h + softmax(h_t*h_i)-weighted h_i. All h in [-1,1].
C=math.exp(2); a=1+2*C; b=3*C
ratios=[]
for trial in range(300):
    n=random.randint(1,40)
    x=[random.uniform(-1,1) for _ in range(n)]
    y=[random.uniform(-1,1) for _ in range(n)]
    def row(z,t):
        w=[math.exp(z[t]*z[i]) for i in range(t+1)]
        return z[t]+sum(w[i]*z[i] for i in range(t+1))/sum(w)
    for t in range(n):
        lhs=abs(row(x,t)-row(y,t))
        rhs=a*abs(x[t]-y[t])+b*sum(abs(x[i]-y[i]) for i in range(t+1))/(t+1)
        assert lhs<=rhs+1e-12
        ratios.append(lhs/rhs if rhs else 0)
checks['weight_change_recurrence']={'pass':True,'trials':300,'max_ratio':max(ratios)}
# Two zero-score averaging layers: n times input-1 influence diverges as H_n.
checks['early_token_uniform_inverse_n_counterexample']=[{'n':n,'n_times_influence':sum(1/i for i in range(1,n+1))} for n in (10,100,1000,10000)]
for M in (64,65,100,1000):
    T=M+3
    for j in range(2,M//4+1):
        assert M+3-j>=T/2 # first suffix coin is N-j+1=M+3-j
checks['rare_suffix_late_positions']={'pass':True}
# Explicit v2 mask: skip first two keys, terminal excludes synthetic key.
mask_ratios=[]
for M in (64,65,100,1000):
    T=M+3
    for t in range(1,T+1):
        keys=list(range(1,t+1)) if t<=2 else list(range(3,t+1 if t<T else T))
        assert len(keys)>=t/3
for trial in range(200):
    t=random.randint(3,60)
    keys=list(range(2,t)) # 0-based {3,...,t}
    x=[random.uniform(-1,1) for _ in range(t)]
    y=[random.uniform(-1,1) for _ in range(t)]
    def masked(z):
        w=[math.exp(z[-1]*z[i]) for i in keys]
        return z[-1]+sum(v*z[i] for v,i in zip(w,keys))/sum(w)
    lhs=abs(masked(x)-masked(y))
    rhs=(1+6*C)*abs(x[-1]-y[-1])+9*C*sum(abs(u-v) for u,v in zip(x,y))/t
    assert lhs<=rhs+1e-12
    mask_ratios.append(lhs/rhs if rhs else 0)
checks['public_dense_mask_v2']={'pass':True,'density':1/3,'trials':200,'max_ratio':max(mask_ratios)}
checks['status']='All finite diagnostics passed; candidate proof still requires independent review.'
path=Path(__file__).with_name('CA001_diagnostic.json')
path.write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
