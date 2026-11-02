from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from pathlib import Path
import json,math
counts={}
def ck(n,v):assert v,n;counts[n]=counts.get(n,0)+1
# Exact scalar finite compander, includes generic final /2 floor.
def g(x,L):
 u=x;v=F(0)
 for j in range(L):v,u=v+F(1,2**j)*max(0,u-F(1,4)),min(1,4*u)
 return v+F(1,2**L)*u
def inv(z,L):
 pts=sorted(set([F(0),F(1)]+[F(1,4**j) for j in range(L+1)]))
 for a,b in zip(pts,pts[1:]):
  if g(a,L)<=z<=g(b,L):return a+(b-a)*(z-g(a,L))/(g(b,L)-g(a,L))
 raise AssertionError('inverse')
def fin(x,L,Q):
 P=Q.bit_length()-1+L+4;D=2**P;u=math.floor(D*x);v=0
 for j in range(L):v,u=v+max(0,u-D//4)//2**j,min(D,4*u)
 w=v+u//2**L;half=w//2;Z=Q*half//D
 return Z,inv(F(2*Z,Q),L)
for L in range(7):
 for Q in [16,32,64]:
  for a in range(33):
   for b in range(33-a):
    x,y=F(a,32),F(b,32);za,xa=fin(x,L,Q);zb,yb=fin(y,L,Q)
    ck('finite_monotone_zero',((x<=y)==(za<=zb) or za==zb) and (x!=0 or xa==0))
    if za+zb:
     p=x/(x+y);v=xa/(xa+yb)
     ck('binary_purity_clip',abs(v-p)<=32*p)
     largest=max(x,y);recon=xa if x>=y else yb
     ck('largest_positive_bank',largest<16*recon)
# FN full observation overlap with exact terminal pair, not discarded side information.
def tent(u,D):return 2*min(u,D-u)
for M in [2,4,8]:
 for Q in [2,4]:
  for delta in [F(1,4),F(1,2)]:
   laws=[];D=2**max(M.bit_length()-1,3*(Q.bit_length()-1));h=Q.bit_length()-1
   for p in [F(1,2)-delta/2,F(1,2)+delta/2]:
    law=defaultdict(F)
    for bits in product([0,1],repeat=M):
     cnt=sum(bits);u=D*cnt//M;rails=[u]
     for _ in range(2):
      for _ in range(h):u=tent(u,D)
      rails.append(u)
     if abs(F(rails[0],D)-F(1,2))<=delta:rails[0]=D//2
     key=tuple(Q*v//D for v in rails)+bits[-2:]
     law[key]+=p**cnt*(1-p)**(M-cnt)
    laws.append(law)
   overlap=sum(min(v,laws[1].get(k,F(0))) for k,v in laws[0].items())
   p=F(1,2)+delta/2;pin=p*(1-p);good=F(0)
   for bits in product([0,1],repeat=M-2):
    if abs(F(1+sum(bits),M)-F(1,2))<=delta:good+=p**sum(bits)*(1-p)**(M-2-sum(bits))
   ck('FN_protected_terminal_overlap',overlap>=pin*good)
# Actual-terminal occupation DP for genuinely stochastic homogeneous chains.
for P in [[[F(3,4),F(1,4)],[F(1,3),F(2,3)]],[[F(1),F(0)],[F(1,7),F(6,7)]]]:
 for initial in range(2):
  for target in range(2):
   dp={(initial,0):F(1)}
   for m in range(81):
    # store departures before terminal, target-specific; no terminal visit counted.
    if m:
     for w in [1,2,3]:
      prob=sum(v for (s,n),v in dp.items() if s==target and n<w)
      # per-target contribution <= whole UC; sum target handled separately below
      ck('terminal_occupation_target_bound',prob<=min(1,F(4*w,m+1)))
    nd=defaultdict(F)
    for (s,n),v in dp.items():
     for t,p in enumerate(P[s]):nd[t,n+(s==target)]+=v*p
    dp=nd
result={'status':'PASS','checks':counts,'total':sum(counts.values()),'scope':'Exact finite corroboration, not full-source-class proof.'}
(Path(__file__).parent/'markov_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
