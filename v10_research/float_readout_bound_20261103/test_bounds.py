#!/usr/bin/env python3
"""Finite deterministic checks of theorem ingredients, not a backend proof."""
from fractions import Fraction as F
from itertools import product
u=F(1,2**53)
def gamma(n):return n*u/(1-n*u)
checks=0
for M in range(2,8):
 L=M//2
 for w in product((0,1),repeat=M+2):
  U=w[-2:]; e=[(int(w[i:i+2]==U and w[i+2]==0),int(w[i:i+2]==U and w[i+2]==1)) for i in range(M)]
  J=sum(a+b for a,b in e);C=sum(b for a,b in e);D=sum(a+b for a,b in e[:L]);E=sum(b for a,b in e[:L])
  rails=[F(J-C,M),F(C,M),F(D-E,L),F(E,L),F(J-D-C+E,M-L),F(C-E,M-L)]
  slices=[e,e,e[:L],e[:L],e[L:],e[L:]]
  for i,(rail,z) in enumerate(zip(rails,slices)):
   n=len(z); v=0.0
   for pair in z:v+= (1.0/n)*pair[i%2]
   d=u+(1+u)*gamma(n-1)
   assert abs(F.from_float(v)-rail)<=d
   checks+=1
# Rational derivative certificate: g=e+(1-2e)s; g'=a*s*(1-s),
# 0<=g'<=min(g,1-g); each CE derivative is bounded by one.
for E in range(0,51):
 e=F(E,100); a=1-2*e
 for S in range(0,101):
  s=F(S,100);g=e+a*s;gp=a*s*(1-s)
  assert 0<=gp<=min(g,1-g)
  checks+=1
# Sharpness of selection gap 2 epsilon with arbitrary tie-breaking.
eps=F(1,10); ideal=[F(0),F(0)]; actual=[-eps,eps]
assert abs(actual[0]-ideal[0])==eps and abs(actual[1]-ideal[1])==eps
assert max(actual)-actual[0]==2*eps
print('PASS deterministic checks:',checks,'plus sharpness example; M=2..7 exhaustive input words, rational derivative grid')
