#!/usr/bin/env python3
"""Independent rational checks, not a proof or emitted-network audit."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
counts={"coarse_attacks":0,"scale_and_selector_cases":0,"statistical_snakes":0,"statistical_scalar":0,"geometric_decodes":0}
def floor(x): return x.numerator//x.denominator
def clip(x): return min(F(1),max(F(0),x))
def scale(q,delta):
    tau=max(F(1,q),delta); t=F(1,2)
    while t/2>=tau:t/=2
    assert tau<=t<2*tau
    return tau,t
def edges(j,n):
    if j==1:return [(F(0),F(1),(F(0),),(F(1),))]
    out=[];eta=F(1,2*n**(j-1)+2); lower=edges(j-1,n)
    for i in range(n):
        row=lower if i%2==0 else [(1-b,1-a,v,u) for a,b,u,v in lower[::-1]]
        for a,b,u,v in row:out.append(((i+(1-eta)*a)/n,(i+(1-eta)*b)/n,u+(F(i,n),),v+(F(i,n),)))
        end=out[-1][3]
        out.append((F(i+1,n)-eta/n,F(i+1,n),end,end[:-1]+(F(i+1,n),)))
    for e,f in zip(out,out[1:]):assert e[1]==f[0] and e[3]==f[2]
    return out
def point(e,t):
    a,b,u,v=e; z=(t-a)/(b-a)
    return tuple(x+z*(y-x) for x,y in zip(u,v))
def decode(es,q):
    best=None
    for a,b,u,v in es:
        axis=next(i for i in range(len(u)) if u[i]!=v[i])
        z=clip((q[axis]-u[axis])/(v[axis]-u[axis]))
        w=tuple(x+z*(y-x) for x,y in zip(u,v))
        ds=sum((x-y)**2 for x,y in zip(w,q));cand=(ds,a+(b-a)*z)
        if best is None or ds<best[0]:best=cand
    return best[1]
# Include non-dyadic budgets and near coarse boundaries; verify oracle simulation.
for q in [2,4,8,16,64,256]:
  for delta in [F(1,4),F(1,7),F(1,13),F(1,q),F(1,3*q),F(3,4*q)]:
    if delta>F(1,4):continue
    vals=set()
    for den in [q,2*q,3*q,257]:
      for num in range(den+1):
        a=F(num,den);k=floor(a/delta);v=delta*k
        assert 0<=a-v<delta and 0<=v<=1
        message=F(floor(q*v),q)
        assert message==F(floor(q*delta*k),q)
        vals.add(message);counts['coarse_attacks']+=1
    assert len(vals)<=floor(1/delta)+1
# Exact squared resource comparisons avoid floating point entirely.
for j in range(2,7):
 D=isqrt(144*j)
 if D*D<144*j:D+=1
 kappa=2**j*(2*D)**(j-1)
 for h in range(1,25):
  q=2**h
  for delta in [F(0),F(1,4),F(1,7),F(1,q),F(3,2*q),F(1,3*q),F(5,7*q)]:
   if delta>F(1,4):continue
   tau,t=scale(q,delta)
   maxM=floor(tau**(-2*j)/kappa**2)
   ms={1,2,3,16,100,max(1,maxM),max(1,maxM-1),maxM+1}
   for M in ms:
    counts['scale_and_selector_cases']+=1
    if tau**(-2*j)<kappa**2*M:continue
    assert t**(-2*j)>(2*D)**(2*(j-1))*M
    if t*t*M<=1:
      counts['statistical_scalar']+=1
      assert 9*tau*tau*M<=9
    else:
      n=2
      while n**(2*(j-1))<t*t*M:n*=2
      assert n*D*t<=1
      assert tau*tau*M<=n**(2*(j-1))
      counts['statistical_snakes']+=1
# New independent edge recursion: finite tube perturbation + real rational attack.
for j,n,h in [(2,2,8),(2,4,10),(3,2,9),(3,4,12)]:
 q=2**h;es=edges(j,n);D=isqrt(144*j)+1
 samples=[]
 for e in es:
  for r in [F(0),F(1,3),F(2,3),F(1)]:
   x=e[0]+r*(e[1]-e[0]);samples.append((x,point(e,x)))
 for delta in [F(0),F(1,3*q),F(1,q),F(3,2*q),F(1,1000)]:
  tau,t=scale(q,delta)
  if n*D*t>1:continue
  for x,p in samples:
   for signs in product([-1,1],repeat=j):
    a=tuple(clip(v+F(s,q)) for v,s in zip(p,signs))
    # Both aligned and opposite maximal perturbation, including clipping.
    for flip in [-1,1]:
      z=tuple(F(floor(q*clip(v+flip*s*delta)),q) for v,s in zip(a,signs))
      xhat=decode(es,z)
      assert (xhat-x)**2*n**(2*(j-1))<=72*j*tau*tau
      counts['geometric_decodes']+=1
result={'status':'PASS','method':'independently authored exact Fraction arithmetic; no imports from author diagnostics','counts':counts,'limitations':'Finite diagnostics do not prove the all-parameter theorem or audit the finite FA evaluator. Real-attack universality uses proof; tests use rational examples.','theorem_sha256':hashlib.sha256((ROOT/'NP001_theorem.md').read_bytes()).hexdigest()}
(ROOT/'NP001_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
