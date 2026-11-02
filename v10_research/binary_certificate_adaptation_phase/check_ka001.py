#!/usr/bin/env python3
"""Exact rounding/class-inclusion diagnostics for KA001, finite checks only."""
from fractions import Fraction as F
from pathlib import Path
import math,json,hashlib
D=Path(__file__).resolve().parent
STATES=[(0,0),(0,1),(1,0),(1,1)]
def matrix(theta):
 P=[[F(0)]*4 for _ in range(4)]
 for i,(a,b) in enumerate(STATES):
  for c in [0,1]:P[i][STATES.index((b,c))]=theta[i] if c else 1-theta[i]
 return P
counts={'rounded_actual_certificate_cases':0,'all_state_entries_at_actual_beta':0,'weak_algebra_cases':0,'non_square_reciprocal_certificates':0}
rows=[]
for M in [4096,4097,4100,5000,10000,65536,1000000,16777216]:
 low=F(256,M*M); high=F(1,16*M);T=M//8
 for q in range(17):
  beta=low+(high-low)*F(q,16)
  k=math.isqrt(beta.denominator//beta.numerator)
  assert k*k*beta<=1<(k+1)*(k+1)*beta
  assert k*k>=4*M and k<=M//16 and k<=T
  assert F(9,16)<=k*k*beta<=1
  assert beta<=F(1,k*k)
  if beta!=F(1,k*k):counts['non_square_reciprocal_certificates']+=1
  delta=F(1,k);e=1-delta;tau=F(1,4*M)
  for a in [F(k,32*T),F(k,32*k),F(1,16)]:
   x=1/(e/a+2+delta/tau);pi=[x*e/a,x,x,x*delta/tau]
   P=matrix([a,delta,delta,1-tau]);P2=[[sum(P[i][h]*P[h][j] for h in range(4)) for j in range(4)] for i in range(4)]
   assert [sum(pi[h]*P[h][j] for h in range(4)) for j in range(4)]==pi
   for i in range(4):
    for j in range(4):
     assert P2[i][j]>=beta*pi[j]
     counts['all_state_entries_at_actual_beta']+=1
  counts['rounded_actual_certificate_cases']+=1
  if q in [0,8,16]:rows.append({'M':M,'beta':str(beta),'k':k,'k_squared_beta':str(k*k*beta)})
for scale in [F(1),F(11,10),F(2),F(10),F(100)]:
 for M in [64,65,256,4096,1000000]:
  for k in sorted(set([1,2,math.isqrt(M),M//2,M])):
   z=F(M,k)
   assert 1+z<=scale*(1+z/scale)
   counts['weak_algebra_cases']+=1
# Conservative exact assembly constants using log80<5 and sqrt32<8.
assert 48*(17+5)+960<2**12
assert 32<8**2
proof='KA001_certificate_phase_partial.md'
out={'status':'PASS_TESTED_INSTANCES_ONLY','arithmetic':'Fraction and integer square roots exact; no floating-point probability checks',
 'counts':counts,'selected_rounding_records':rows,
 'proof_sha256':hashlib.sha256((D/proof).read_bytes()).hexdigest(),
 'limits':'Finite rounding, source inclusion and elementary algebra only. Accepted BK002 provides the full-word constrained-risk theorem; generic upper interfaces and asymptotic curve arguments require fresh full review.'}
(D/'KA001_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='selected_rounding_records'},indent=2))
