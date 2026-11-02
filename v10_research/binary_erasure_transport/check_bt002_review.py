"""Independent finite checks for BT002, not a replacement for the proof."""
from fractions import Fraction as F
from math import comb,log,sqrt,exp,ceil
import json

def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def power(A,n):
 B=[[F(i==j) for j in range(len(A))] for i in range(len(A))]
 for _ in range(n):B=mul(B,A)
 return B
counts={'fifth_power_entries':0,'return_count_identities':0,'binomial_mode_bounds':0,'grid_spacing':0,'scalar_sum_completion':0}
for p in map(F,['1/8','1/4','1/2','3/4','7/8']):
 R=[[F(0),1-p,p],[F(1),F(0),F(0)],[F(0),F(1),F(0)]]
 R5=power(R,5)
 for u,ex in enumerate([2*p*(1-p),(1-p)**2,p]):assert R5[u][0]==ex and ex>=F(1,64);counts['fifth_power_entries']+=1
 for t in range(2,31):
  mass=sum(F(comb(s+l,l))*p**l*(1-p)**s for l in range(t//3+1) for s in [(t-3*l)//2] if 2*s+3*l==t)
  assert mass==power(R,t)[0][0];counts['return_count_identities']+=1
for m in range(2,101):
 for l in range(1,m):
  p=F(l,m);mass=comb(m,l)*p**l*(1-p)**(m-l)
  assert mass>=F(1,m+1);counts['binomial_mode_bounds']+=1
for t in [4096,10**5,10**12]:
 for k in [1,100,10**6,10**15]:
  n=max(1,(3*2**18*t+k-1)//k)
  assert F(3,4*n)<=F(k,2**20*t)
  assert n+1<=2+F(2**20*t,k);counts['grid_spacing']+=1
assert 1024*sqrt(2*2**-44)+326/2**20<1/1024
assert 2*4096*exp(-4096/96)<1/128
# Scalar sum comparison avoids materializing enormous harmonic sums:
# use the proven integral lower proxy, making this a stronger check.
c=2**-44; C=8;j0=4096
D=7+log(max(1,C))+6*log(max(1,2/c))
for logM in [log(64),10,30,60,100,300]:
 M=exp(logM)
 for f in [0,.1,.249,.25,.4,.5,.75,.99,1]:
  k=max(1,min(M,exp(logM*f)))
  for g in [0,.1,.3,.7,1]:
   e=exp(-logM*g)
   A=1/(e*k);U=min(1/(C*e),c*k*k/log(k+2))
   Tproxy=(k/M)*max(0,log((k+U)/(k+j0)))
   target=(k/M)*(1+log(1+A))
   rhs=D*(1+log(1+j0))*max(M**-.5,k/M,Tproxy)
   assert target<=rhs*(1+1e-12);counts['scalar_sum_completion']+=1
print(json.dumps({'status':'PASS','checks':counts,'total':sum(counts.values()),'limits':'Finite exact/rational and floating scalar diagnostics; no formal verification.'},indent=2))
