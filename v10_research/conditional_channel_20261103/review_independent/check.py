"""Independent finite rational checks; do not prove the universal theorem."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
import json

def bern_paths(bounds,n,event):
    # Dynamic programming: exact largest terminal event over all adaptive
    # Bernoulli policies with each conditional success in [0,bounds].
    def rec(h):
        if len(h)==n:return F(int(event(h)))
        a,b=rec(h+(0,)),rec(h+(1,))
        return max(a,(1-bounds)*a+bounds*b)
    return rec(())
checks=0
for n in range(1,8):
 for q in [F(1,16),F(1,4),F(1,2)]:
  for r in range(1,n+1):
   worst=bern_paths(q,n,lambda h:sum(h)>=r)
   exact=sum(F(comb(n,j))*q**j*(1-q)**(n-j) for j in range(r,n+1))
   assert worst==exact
   assert worst<=F(comb(n,r))*q**r
   checks+=1
  for S in combinations(range(n),min(3,n)):
   assert bern_paths(q,n,lambda h:all(h[i] for i in S))==q**len(S)
   checks+=1
# CAF: designated correct-slot E marginal in [p-alpha,1], wrong in [0,alpha].
# Each second-slot row is permitted to react to first observation.
pairs=0
asym=None
for p in [F(1,4),F(1,2),F(3,4)]:
 for a in [F(0),p/8,p/4]:
  # Physical input 0 then 1: first q0, second q1 conditioned on first.
  policies=list(product([F(0),a],[p-a,F(1)],[p-a,F(1)]))
  for q0,q10,q11 in policies:
   c=(1-q0)*q10;w=q0*(1-q11)
   assert c>=p-2*a and w<=a
   assert c>=p/2
   pairs+=1
  # Physical input 1 then 0.
  for q1,q00,q01 in product([p-a,F(1)],[F(0),a],[F(0),a]):
   c=q1*(1-q01);w=(1-q1)*q00
   assert c>=p-2*a and w<=a and c>=p/2
   pairs+=1
# Explicit time-dependent admissible policy breaks symmetry even without adaptation:
# nominal row0 E=0,row1 E=1/2; first-slot q0=alpha, second q0=0;
# both q1=1/2. Gate0 encoded 01; gate1 encoded10.
a=F(1,32)
asym={'gate0_correct':str((1-a)/2),'gate1_correct':str(F(1,2)),
      'gate0_wrong':str(a/2),'gate1_wrong':'0'}
assert (1-a)/2!=F(1,2)
# Global uniform replacement with weight eta. For every binary input word,
# marginals match noiseless nominal up to eta/2, and common mass eta is present.
replacement=0
for n in range(1,7):
 for eta in [F(1,16),F(1,4),F(1)]:
  for h in product([0,1],repeat=n):
   law={v:eta/F(2**n)+(1-eta)*int(v==h) for v in product([0,1],repeat=n)}
   assert sum(law.values())==1
   for i in range(n):
    err=sum(m for v,m in law.items() if v[i]!=h[i])
    assert err==eta/2
   assert all(m>=eta/F(2**n) for m in law.values())
   replacement+=1
# Coding arithmetic remains unchanged with predictable subset errors.
coding=0
for B in range(1,10001):
 k=(8*B-1).bit_length();K=(B+k-1)//k;n=4*K
 assert k>=3 and n<=2**k and k<=4*B
 assert 48*K*k<=240*B
 assert 4*K-8*k*(K+1)<=-6*B
 coding+=1
# Endpoint IID witnesses really meet the all-state pair certificate.
endpoint=0
states=list(product([0,1],repeat=2))
for bit in [0,1]:
 P={u:{v:F(int(v==(u[1],bit))) for v in states} for u in states}
 for u in states:
  for v in states:
   assert sum(P[u][w]*P[w][v] for w in states)==int(v==(bit,bit))
   endpoint+=1
# General nominal finite alphabets: common uniform replacement yields TV<=eta.
nominal=0
for rows in [([F(1),F(0)],[F(0),F(1)]),
             ([F(1,2),F(1,2),F(0)],[F(0),F(1,3),F(2,3)]),
             ([F(1,4),F(3,4)],[F(3,4),F(1,4)])]:
 for eta in [F(1,16),F(1,4),F(1)]:
  for row in rows:
   u=F(1,len(row)); mixed=[(1-eta)*p+eta*u for p in row]
   tv=sum(abs(a-b) for a,b in zip(row,mixed))/2
   assert tv<=eta
   nominal+=1
out={'status':'PASS','endpoint_all_state_pair_checks':endpoint,'general_nominal_marginal_checks':nominal,'adaptive_tail_subset_cases':checks,'adaptive_CAF_vertex_policies':pairs,'asymmetry_witness':asym,'global_replacement_codewords':replacement,'coding_arithmetic_cases':coding,'limitations':'Finite exact diagnostics; universal proof is analytic. No author checker imported.'}
print(json.dumps(out,indent=2,sort_keys=True))
