#!/usr/bin/env python3
"""Finite exact diagnostics only; not proof of universal SC003."""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json, math, hashlib
ROOT=Path(__file__).resolve().parent

def row(word):
    u=word[-2:]; d=1-u[0]
    vals=[word[i+2] for i in range(len(word)-2) if word[i:i+2]==u]
    return sum(v==d for v in vals),len(vals),2*u[0]+u[1]

def pred(word,k):
    c,j,_=row(word)
    return F(c+1,j+2) if not k else F(max(c-6*k,0),j+6*k+2)

checks=0; scenarios=[]
# Canonical q values: generic full support, absorbing 00, absorbing 11,
# degenerate crossing alternation, deterministic paths, iid.
kernels=[tuple(map(F,x)) for x in [('1/3','2/5','1/4','3/7'),('0','1/3','1/5','1/2'),('2/7','1/3','2/5','0'),('0','0','0','0'),('1','1','1','1'),('1/3','1/3','2/3','2/3')]]
M=6
for qs in kernels:
  for init in product((0,1),repeat=2):
    for k in (1,2):
      risk=F(0); bound=F(0); mass=F(0)
      for suffix in product((0,1),repeat=M):
        word=init+suffix; prob=F(1)
        for i in range(M):
          q=qs[2*word[i]+word[i+1]]
          prob*=q if word[i+2]==1-word[i] else 1-q
        if not prob: continue
        c,j,u=row(word); q=qs[u]; A=24*k+2
        rhs=(2*abs(F(c,j)-q) if j else 0)+min(q,F(A,j+2))
        worst=F(0)
        for n in range(k+1):
          for ix in combinations(range(M),n):
            z=list(word)
            for i in ix:z[i]=1-z[i]
            z=tuple(z); h=pred(z,k)
            assert abs(h-q)<=rhs
            assert z[-2:]==word[-2:]
            worst=max(worst,abs(h-q)); checks+=1
        risk+=prob*worst; bound+=prob*rhs; mass+=prob
      assert mass==1 and risk<=bound
      scenarios.append({'q':list(map(str,qs)),'start':list(init),'k':k,'worst_risk':str(risk),'pathwise_bound_expectation':str(bound)})
scalar_checks=0
for M in (64,65,127,256,1000,1000000):
 for k in sorted({1,2,M//8,M//2,M}):
  A=24*k+2
  assert k<=A<=26*k
  for beta in (0.,M**-2/2,M**-2,1/M,1/16,1.):
   e0=max(math.sqrt(beta),1/M); F0=k/M*(1+math.log1p(1/(k*e0)))
   if beta>=M**-2:
    occ=16672*A/M*(1+math.log1p(1/(math.sqrt(beta)*A)))
    assert occ<=433472*F0*(1+1e-14)
   else:
    z=16*A/(M+1); psi=1 if z>=1 else z*(1+math.log(1/z))
    assert psi<=416*F0*(1+1e-14)
   assert 256*A/M+16/(M+2)<=6672*k/M*(1+1e-14)
   scalar_checks+=1
assert 2*(8192+1)*math.sqrt(32)+4<2**17
assert 433472<2**19
out={'status':'PASS','exact_full_path_checks':checks,'exact_kernel_start_budget_scenarios':len(scenarios),'scalar_domain_checks':scalar_checks,'scenarios':scenarios,'limitation':'Finite diagnostics; constants/occupation theorems require written proof and accepted imports.'}
(ROOT/'SC003_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='scenarios'},indent=2))
