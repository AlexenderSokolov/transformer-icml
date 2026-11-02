"""Exact rational diagnostics, not a formal proof or emitted circuit execution."""
from fractions import Fraction as F
from itertools import product
from math import log,sqrt,ceil
import json, pathlib, hashlib

def tv(a,b): return sum(abs(x-y) for x,y in zip(a,b))/2
counts={'histories':0,'instances':0,'zero_selected_block':0,'nonempty_all_floors_zero':0}
max_ratio=F(0)
for K, maxM in [(2,7),(3,4)]:
 for M in range(1,maxM+1):
  for hist in product(range(K),repeat=M+2):
   counts['histories']+=1
   pair=hist[-2:]
   triples=list(zip(hist[:-2],hist[1:-1],hist[2:]))
   C=[sum((a,b)==pair and c==d for a,b,c in triples) for d in range(K)]
   J=sum(C)
   q=[F(c+1,J+K) for c in C]
   for k in [1,2,3,8]:
    den=M+(k-1)*J
    nums={abc:0 for abc in product(range(K),repeat=3)}
    for a,b,c in triples: nums[a,b,c]+=k if (a,b)==pair else 1
    assert sum(nums.values())==den
    for Q in [1,2,4,16]:
     counts['instances']+=1
     bank={abc:Q*v//den for abc,v in nums.items()}
     selected=[bank[pair+(c,)] for c in range(K)]
     assert selected==[Q*k*c//den for c in C]
     s=sum(selected)
     if not s:
      counts['zero_selected_block']+=1
      if J: counts['nonempty_all_floors_zero']+=1
     p=[F(v,s) for v in selected] if s else [F(1,K)]*K
     grid=[(Q*v.numerator//v.denominator) for v in p[:-1]]
     grid.append(Q-sum(grid))
     out=[F(v,Q) for v in grid]
     assert min(out)>=0 and sum(out)==1
     assert tv(out,p)<=F(K-1,Q)
     if J:
      r=F(k*J,den)
      assert tv(p,[F(c,J) for c in C])<=min(F(1),K/(Q*r))
     bound=F(K,J+K)+min(F(1),F(K*(K+1)*M,k*Q*(J+K)))+F(2*K-1,Q)
     assert tv(out,q)<=bound
     max_ratio=max(max_ratio,tv(out,q)/bound)
# Integer schedule and analytic envelopes over a broader numerical grid.
def psi(x):return 1 if x>=1 else (0 if x==0 else x*(1-log(x)))
for M in list(range(64,10000))+[2**a+d for a in range(14,100) for d in [-1,0,1]]:
 L=(M+1).bit_length(); Q=2**max(4,(L+1)//2)
 assert Q*Q>=M+1 and Q*Q<=4*(M+1)
 for K in [2,3,10,50]:
  D=K**5*(K+1)
  assert psi(D/(L*Q))<=3*D/Q+1e-12
for D in [1,3,27,100]:
 for r in [1,3,7]:
  H=3**(2*r);u=r*sqrt(40*D*H)
  for k in [1,2,7,100,1000000]:
   NB=ceil(8*k*u+4)+1
   assert NB<=k*(8*u+6)*(1+1e-14)
   assert (2+4*k*r)<=k*(2+4*r)
for z in [0.1,1,2,8,100,1e4,1e10,1e50]:
 for t in [1,2,4,10,100,1e8]:
  f=1+log(1+z/t);k=ceil(f)
  assert (1+log(1+k*z/t))/k<=2+1e-12
out={'status':'pass','scope':'Exact rational mathematical-map tests; not compiled finite network execution',**counts,'max_observed_error_to_bound_ratio':str(max_ratio),'schedule_and_constant_checks':'pass'}
p=pathlib.Path(__file__).with_name('SB001_diagnostics_v1.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
