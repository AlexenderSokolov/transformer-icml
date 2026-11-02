#!/usr/bin/env python3
"""Independent exact-rational checks, not an emitted-network test."""
from fractions import Fraction as F
from collections import defaultdict
import json, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent

def tent(x): return 2*min(x,1-x)
def fold(x,h):
    for _ in range(h): x=tent(x)
    return x

def labels(x,h,J):
    q=1<<h; out=[]
    for _ in range(J):
        out.append((q*x).numerator//(q*x).denominator)
        x=fold(x,h)
    return tuple(out)

def decode(ks,h):
    q=1<<h; lo,hi=F(0),F(1); a,b=F(1),F(0)
    for k in ks:
        l,r=(F(k,q),F(k+1,q)) if k<q else (F(1),F(1))
        l,r=(l-b)/a,(r-b)/a
        lo,hi=max(lo,min(l,r)),min(hi,max(l,r))
        assert lo<=hi
        if k==q: return lo,hi
        a,b=(q*a,q*b-k) if k%2==0 else (-q*a,k+1-q*b)
    return lo,hi

cases=0; points=0; endpoints=0; finite=0; fine_branch=0
for h in range(1,5):
  q=1<<h
  for J in range(2,5):
    denom=q**J
    if denom>100000: continue
    # Every finest cell boundary plus midpoint independently checks all fibers.
    fibers=defaultdict(list)
    for num in range(2*denom+1):
      x=F(num,2*denom); ks=labels(x,h,J); lo,hi=decode(ks,h)
      assert lo<=x<=hi and hi-lo<=F(1,denom)
      assert (lo*denom).denominator==1
      fibers[ks].append(x); points+=1
      if q in ks:
        assert lo==hi==x
        endpoints+=1
    for xs in fibers.values(): assert max(xs)-min(xs)<=F(1,denom)
    cases+=1
    # All fractions A/m, with independent primitive lattice evaluation.
    for m in range(1,24):
      for count in range(m+1):
        for extra in (0,2):
          D=denom*(1<<extra); U=D*count//m; xhat=F(U,D)
          actual=[]; V=U
          for j in range(J):
            actual.append(q*V//D)
            for _ in range(h):
              r=max(0,V-D//2)
              nxt=2*V-4*r
              assert nxt==2*min(V,D-V)
              assert 0<=nxt<=D
              V=nxt; fine_branch+=1
          assert tuple(actual)==labels(xhat,h,J)
          lo,hi=decode(actual,h)
          assert 0<=F(count,m)-lo<=F(2,denom)
          # Direct ideal-vs-finite fold certificate.
          ideal=F(count,m); actual_x=xhat
          for j in range(J):
            assert abs(ideal-actual_x)<=F(1,q)
            ideal=fold(ideal,h); actual_x=fold(actual_x,h)
          finite+=1

result={'status':'PASS','scope':'finite exhaustive diagnostics; not proof or emitted-network audit',
        'geometry_parameter_cases':cases,'exact_rational_points':points,'singleton_endpoint_cases':endpoints,
        'finite_count_precision_cases':finite,'exact_integer_fold_steps':fine_branch,
        'theorem_sha256':hashlib.sha256((BASE/'FG001_theorem.md').read_bytes()).hexdigest()}
(BASE/'FG001_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
