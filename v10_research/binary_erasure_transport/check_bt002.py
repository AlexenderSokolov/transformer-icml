"""Finite structural diagnostics for BT002; not formal proof or asymptotic testing."""
from fractions import Fraction as F
from math import comb,log,sqrt,ceil
from itertools import product
import json
checks=0

def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
for p in [F(i,8) for i in range(1,8)]:
 R=[[0,1-p,p],[1,0,0],[0,1,0]];R5=R
 for _ in range(4):R5=mm(R5,R)
 assert [row[0] for row in R5]==[2*p*(1-p),(1-p)**2,p];checks+=1
 assert min(row[0] for row in R5)>=F(1,64);checks+=1
 for t in range(2,26):
  # dynamic distribution over pair state and counts of completed short/long cycles
  # Independently enumerate completed cycle classes; compare to Markov return mass.
  masses=[F(1),F(0),F(0)]
  for _ in range(t):masses=[sum(masses[i]*R[i][j] for i in range(3)) for j in range(3)]
  total=F(0)
  for l in range(t//3+1):
   if (t-3*l)%2:continue
   s=(t-3*l)//2;m=s+l
   mass=comb(m,l)*p**l*(1-p)**s;total+=mass
   ph=F(l,m)
   mode=comb(m,l)*ph**l*(1-ph)**s
   assert mode>=F(1,m+1);checks+=1
  assert total==masses[0];checks+=1
for t,k in product([1,5,4095,4096,8192,10**6,10**12],[1,2,64,4096,10**6,10**12]):
 n=max(1,(3*(2**18)*t+k-1)//k)
 assert F(3,4*n)<=F(k,2**20*t);checks+=1
 assert n+1<=2+F(2**20*t,k);checks+=1
 assert 3+F(2**20*t,k)<=2**22*(1+F(t,k));checks+=1
assert 1024*sqrt(2*2**-44)+326/2**20<1/1024;checks+=1
assert 2*4096*__import__('math').exp(-4096/96)<1/128;checks+=1
assert 326*(1+sqrt(6))/sqrt(2)<1024;checks+=1
assert (7+273*log(2))*(1+log(4097))<1830<2048;checks+=1
assert F(1,32)-F(1,1024)>=F(1,64);checks+=1
assert F(1,64)-F(1,128)==F(1,128);checks+=1
print(json.dumps({'status':'PASS','structural_checks':checks,'scope':'exact reference powers, return-count probabilities, binomial-mode bound, rational grid cardinalities; numeric safe constants','does_not_claim':'formal verification or computational execution at huge entropy cutoff'},indent=2))
