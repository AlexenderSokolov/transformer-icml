#!/usr/bin/env python3
"""Independent SC002 finite corroboration; not proof or formal verification."""
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb, log, log1p, sqrt
from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent
counts={}; worst={}
# Exact all-state symbol and pair certificates, including one unused symbol.
n=0; ev=0
for M in (64,65,66,67,100,256):
 for beta in sorted(set((Q(1,M),Q(1,32),Q(1,16)))):
  if beta<Q(1,M): continue
  for p in (Q(1,4),Q(1,3),Q(1,2),Q(3,4)):
   a=Q(1,2*M); e=beta-a; pi=[e/beta,a*(1-p)/beta,a*p/beta,Q(0)]
   T=[[1-a,a*(1-p),a*p,Q(0)],[e,(1-e)*(1-p),(1-e)*p,Q(0)],[e,(1-e)*(1-p),(1-e)*p,Q(0)],pi]
   assert sum(pi)==1
   for v in range(4): assert sum(pi[y]*T[y][v] for y in range(4))==pi[v]
   pairs=list(product(range(4),repeat=2)); Pi={(u,v):pi[u]*T[u][v] for u,v in pairs}
   for x,y in pairs:
    for u,v in pairs:
     assert T[y][u]*T[u][v]>=beta*Pi[u,v]; n+=1
   L=int(1/(4*beta)); assert 4<=L<=M/4
   for j in range(2,L+1):
    w=Pi[0,0]*(1-a)**(M-j)*a*(1-e)**(j-1)
    assert w>=Q(1,32*M); ev+=1
counts['exact_all_pair_minorization_entries']=n;counts['exact_event_bounds']=ev
# Enumerate erasure distribution, not merely algebraic identity.
n=0
for l in range(9):
 for b in range(1,11):
  for total in range(l+1):
   r=b*(total//b); out={}
   for ones in combinations(range(l),total):
    for remain in combinations(ones,r):
     out[remain]=out.get(remain,Q(0))+Q(1,comb(l,total)*comb(total,r))
   assert len(out)==comb(l,r)
   assert set(out.values())=={Q(1,comb(l,r))}; n+=1
counts['exact_enumerated_erasure_cases']=n
# Finite-domain lower scalars, including all k and beta0 cutoff cases.
n=0; ratio=1e100
for M in range(64,513):
 for beta in sorted(set([1/M,1/16,1/32,2/M])):
  if not 1/M<=beta<=1/16: continue
  L=int(1/(4*beta)+1e-12)
  for k in range(1,M+1):
   b=k+1
   integral=b/(2048*M)*log1p((L-1)/b)
   claimed=(k/M)*log1p(1/(beta*k))/16384
   assert integral+1e-15>=claimed
   ratio=min(ratio,integral/claimed); n+=1
   iid=1/(32*(M//b+1)); assert iid+1e-15>=k/(96*M)
   F=k/M*(1+log1p(1/(beta*k)))
   assert max(k/(96*M),claimed)+1e-15>=F/32768
counts['lower_scalar_cases']=n;worst['minimum_integral_over_log_lower']=ratio
# Residual scalar envelope across both branches, huge z and real t.
def psi(x): return 1 if x>=1 else x*(1-log(x))
n=0;ratio=0
for K in (3,4,10,100):
 DD=12*K**4
 for M in (64,65,66,67,128,1000,10**6,10**12,10**30):
  for k in set((1,2,max(1,M//100),max(1,M//2),M)):
   z=M/k
   for beta in set((1/M, min(1,2/M), min(1,10/M), 1/16,1/2,1)):
    if beta<1/M: continue
    t=M*beta;eta=0 if beta==1 else (1-beta)**(M//4)
    F=(1+log1p(z/t))/z
    lhs=eta*psi(DD/z);rhs=5*DD*F
    assert lhs<=rhs*(1+1e-12);ratio=max(ratio,lhs/rhs);n+=1
counts['residual_envelope_cases']=n;worst['maximum_residual_over_envelope']=ratio
# IID KL and cleaned finite comparison.
for M in range(64,10001):
 N=M+2;d=1/(16*sqrt(N));kl=2*d*log((.5+d)/(.5-d))
 assert N*kl<=1/8+1e-12
 assert 3/(128*sqrt(N))>=1/(64*sqrt(M))
counts['iid_kl_and_clean_floor_cases']=9937
report={'status':'PASS','scope':'Independent finite diagnostics, exact rational for source/erasure, floating point for scalar and KL grids; not formal verification','theorem_sha256':hashlib.sha256((D/'SC002_theorem.md').read_bytes()).hexdigest(),'counts':counts,'worst_cases':worst}
(D/'SC002_review_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
