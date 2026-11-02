"""Exact finite combinatorial checks; not a formal verification of SC001."""
from itertools import combinations
from fractions import Fraction
from math import comb, log
import json
from pathlib import Path
checks=0
for l in range(11):
 for b in range(1,13):
  for n in range(l+1):
   r=b*(n//b)
   prob=Fraction(comb(l-r,n-r),comb(l,n)*comb(n,r))
   assert prob==Fraction(1,comb(l,r))
   assert n-r<=b-1
   checks+=1
# Enumerate actual random-deletion kernel, rather than just testing factorial identity.
enumerated=0
for l in range(8):
 for b in range(1,9):
  for n in range(l+1):
   r=b*(n//b); dist={}
   for ones in combinations(range(l),n):
    for retained in combinations(ones,r):
     dist[retained]=dist.get(retained,Fraction(0))+Fraction(1,comb(l,n)*comb(n,r))
   assert len(dist)==comb(l,r)
   assert all(v==Fraction(1,comb(l,r)) for v in dist.values())
   enumerated+=1
finite=0
for M in range(2,501):
 assert (1-1/M)**M>=.25-1e-14
 for k in range(1,M+1):
  b=k+1
  bound=b/(128*M)*log(1+(M-1)/b)
  psi=(k/M)*(1+log(M/k))
  assert bound+1e-14>=psi/512
  finite+=1
out={'status':'PASS','factorial_cases':checks,'enumerated_kernel_cases':enumerated,
     'finite_domain_inequalities':finite,
     'scope':'Finite diagnostics only; no Monte Carlo and no formal verification.'}
Path(__file__).with_name('SC001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
