#!/usr/bin/env python3
"""Independent finite checks of UI001 lemmas, not a proof or model execution."""
import itertools, json, math, pathlib, hashlib
import numpy as np
from scipy.integrate import quad
ROOT=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(731991)
records=[]
# Exhaust conditional experiments with arbitrary positional tables and extreme range.
for kap in [1.,1e4,1e18,1e100]:
 n,r,m=12,2,2
 positions=list(range(2,n)); pats=list(itertools.product([0,1],repeat=r))
 w={(i,p):math.exp(float(rng.uniform(0,math.log(kap)))) for i in positions for p in pats}
 v={(i,p):float(rng.uniform(-1,1)) for i in positions for p in pats}
 a={i:max(w[i,p] for p in pats) for i in positions}
 selected=sorted(positions,key=lambda i:-a[i])[:m]
 U=sorted(set([0,1,n-2,n-1]+[j for i in selected for j in range(i-r+1,i+1)]))
 free=[i for i in range(n) if i not in U]
 astar=max([a[i] for i in positions if i not in selected],default=0)
 max_vratio=max_deriv=0.; count=0
 for bv in itertools.product([0,1],repeat=len(U)):
  bits=dict(zip(U,bv)); W=sum(w[i,tuple(bits[j] for j in range(i-r+1,i+1))] for i in selected)
  # This diagnostic uses the exact selected known mass rather than requiring
  # the theorem's very loose heavy event at tiny m.
  for p in [.25,.43,.75]:
   rows=[]
   for fv in itertools.product([0,1],repeat=len(free)):
    x=bits|dict(zip(free,fv)); k=sum(fv)
    prob=p**k*(1-p)**(len(free)-k)
    score=k/p-(len(free)-k)/(1-p)
    den=sum(w[i,tuple(x[j] for j in range(i-r+1,i+1))] for i in positions)
    num=sum(w[i,tuple(x[j] for j in range(i-r+1,i+1))]*v[i,tuple(x[j] for j in range(i-r+1,i+1))] for i in positions)
    residual_den=sum(w[i,tuple(x[j] for j in range(i-r+1,i+1))] for i in positions if i not in selected)
    residual_num=sum(w[i,tuple(x[j] for j in range(i-r+1,i+1))]*v[i,tuple(x[j] for j in range(i-r+1,i+1))] for i in positions if i not in selected)
    rows.append((prob,score,num,den,residual_num,residual_den))
   muA=sum(t[0]*t[2] for t in rows); mu=sum(t[0]*t[3] for t in rows)
   resA=sum(t[0]*t[4] for t in rows); resD=sum(t[0]*t[5] for t in rows)
   varA=sum(t[0]*(t[4]-resA)**2 for t in rows); varD=sum(t[0]*(t[5]-resD)**2 for t in rows)
   bound=2*r*r*sum(a[i]**2 for i in positions if i not in selected)
   # deterministic selected-only cases have floating point residual variance
   ratio=max(varA,varD)/bound if bound else 0
   assert ratio<=1+1e-10,(kap,ratio)
   derivative=(sum(t[0]*t[1]*t[4] for t in rows)-muA/mu*sum(t[0]*t[1]*t[5] for t in rows))/mu
   assert abs(derivative)<=8*r+1e-8
   q=4**(-r); overlaps=[i for i in positions if i not in selected and set(range(i-r+1,i+1))&set(U)]
   disjoint=[i for i in positions if i not in selected and i not in overlaps]
   assert sum(a[i] for i in overlaps)<=r*len(U)*astar*(1+1e-12)
   assert q*sum(a[i] for i in disjoint)<=mu*(1+1e-12)
   max_vratio=max(max_vratio,ratio); max_deriv=max(max_deriv,abs(derivative)); count+=1
 records.append(dict(kappa=kap,conditional_cases=count,revealed_bits=len(U),variance_bound_max_ratio=max_vratio,max_curve_derivative=max_deriv))
# Check posterior normalizer lower bound through the specific local interval,
# avoiding inaccurate integration across an extremely narrow full posterior.
posterior=[]
for N in [1,2,10,100,10000,1000000]:
 for y0 in [0,.25-3/math.sqrt(N),.25,.5,.75,.75+3/math.sqrt(N),1]:
  t=min(N,max(0,round(y0*N))); y=t/N
  if max(.25-y,y-.75,0)>3/math.sqrt(N)+1e-14: continue
  p0=min(.75,max(.25,y)); delta=1/(64*math.sqrt(N)); sign=1 if p0<=.5 else -1
  ell=lambda p:t*math.log(p)+(N-t)*math.log1p(-p)
  base=ell(p0)
  local=quad(lambda z:math.exp(ell(p0+sign*z)-base),0,delta,epsabs=1e-13)[0]
  assert local>=1/(128*math.sqrt(N))*(1-1e-8)
  posterior.append(dict(N=N,t=t,local_normalizer_scaled=local*math.sqrt(N)))
# Constant and probability arithmetic, including r=1.
constants=[]
for D,r in [(1,1),(2,2),(4,3)]:
 H=3**(2*r); F=D*H; q=4**(-r); L=r*F+2*r; J=(2*r*L+1)/q; V=4*r*r*J/q
 C=math.ceil(max(1,400*F*(2*r-1)/q**2,3200*F*V))
 assert 4*F*(2*r-1)/(q*q*C)<=.01+1e-15
 assert 32*F*V/C<=.01+1e-15
 constants.append(dict(D=D,r=r,C=C,heavy_failure=4*F*(2*r-1)/(q*q*C),tube_failure=32*F*V/C))
assert .99-200*math.exp(-18)>.98
assert 16/64+8/64**2<math.log(2)
out=dict(status='PASS',warning='Finite corroboration only, not formal proof or original-network execution',conditional_experiments=records,posterior_local_integrals=posterior,constants=constants)
(ROOT/'UI001_diagnostics_v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status='PASS',conditional_cases=sum(x['conditional_cases'] for x in records),posterior_cases=len(posterior))))
