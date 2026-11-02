from itertools import combinations, product
from fractions import Fraction
from math import comb, log
from collections import defaultdict
import json

exchange_cases=0
for l in range(10):
 for b in range(1,12):
  for n in range(l+1):
   r=b*(n//b)
   masses=defaultdict(Fraction)
   for old in combinations(range(l),n):
    for remain in combinations(old,r):
     masses[remain]+=Fraction(1,comb(l,n)*comb(n,r))
   target=Fraction(1,comb(l,r))
   assert len(masses)==comb(l,r) and set(masses.values())=={target}
   exchange_cases+=1

bound_cases=0
min_ratio=(1e9,None)
for M in range(2,1001):
 for k in range(1,M+1):
  b=k+1
  integrated=b/(128*M)*log(1+(M-1)/b)
  psi=(k/M)*(1+log(M/k))
  assert integrated+1e-15>=psi/512
  ratio=integrated/(psi/512)
  if ratio<min_ratio[0]:min_ratio=(ratio,[M,k])
  bound_cases+=1

# Exhaustive one-edit histogram sensitivity and protected row agreement.
triple_cases=0
for N in range(3,8):
 for x in product(range(3),repeat=N):
  def counts(w):
   c=defaultdict(int)
   for i in range(N-2):c[w[i:i+3]]+=1
   return c
  c=counts(x)
  for pos in range(N-2):
   for new in range(3):
    z=x[:pos]+(new,)+x[pos+1:]
    cp=counts(z)
    assert z[-2:]==x[-2:]
    keys=set(c)|set(cp)
    assert sum(abs(c[a]-cp[a]) for a in keys)<=6
    S=x[-2:]
    row=sum(abs(c[S+(a,)]-cp[S+(a,)]) for a in range(3))
    assert row<=6
    triple_cases+=1
out={'exchangeability_exact_rational_cases':exchange_cases,'finite_constant_cases':bound_cases,'minimum_integrated_to_claimed_ratio':min_ratio,'exhaustive_single_edit_histogram_cases':triple_cases,'all_passed':True,'limits':'Finite diagnostics only, not proof or external/formal review.'}
stationary_cases=0
for M in range(2,101):
 a=Fraction(1,M)
 for p in [Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(3,4)]:
  pi=[Fraction(1,2),(1-p)/2,p/2]
  T=[[1-a,a*(1-p),a*p],[a,(1-a)*(1-p),(1-a)*p],[a,(1-a)*(1-p),(1-a)*p]]
  assert [sum(pi[i]*T[i][j] for i in range(3)) for j in range(3)]==pi
  for j in range(2,M+1):
   event=pi[0]*T[0][0]*(1-a)**(M-j)*a*(1-a)**(j-1)
   assert event==(1-a)**M/(2*M) and event>=Fraction(1,8*M)
   stationary_cases+=1
for M in range(2,10001):
 N=M+2; d=1/(16*N**.5)
 kl=2*d*log((.5+d)/(.5-d))*N
 assert kl<=1/8
out['stationary_exact_rational_event_cases']=stationary_cases
out['stationary_iid_KL_cases']=9999
print(json.dumps(out,indent=2))
