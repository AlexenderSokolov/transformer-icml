"""Finite exact-rational algebra checks only; no RNG."""
from fractions import Fraction as F
n=0
for E in range(51):
 e=F(E,100);a=1-2*e
 for S in range(101):
  s=F(S,100);g=e+a*s;gp=a*s*(1-s)
  assert g-gp==e+a*s*s and (1-g)-gp==e+a*(1-s)**2 and 0<=gp<=min(g,1-g)
  for T in (F(0),F(1,5),F(1,2),F(1)):
   if g not in (0,1):
    derivative=gp*((1-T)/(1-g)-T/g);assert abs(derivative)<=1
   n+=1
for E in range(1,51):
 e=F(E,100);tau=e/3;lo=e-tau;hi=1-e+tau;assert 0<lo<=hi<1 and hi==1-lo
for e in [F(1,100),F(1,10),F(2,5)]:
 center=F(1,2);ideal=(center,center);actual=(center-e,center+e);assert min(actual)>=0 and max(actual)<=1 and max(actual)-actual[0]==2*e and all(abs(a-b)<=e for a,b in zip(ideal,actual))
print('PASS',n,'(smoothing,s,target) rational identities/derivatives; clipping intervals and nonnegative generic sharpness')
print('At e=0, s=0 or s=1 is a limiting infinite-logit case where CE derivative may be undefined; finite logits remain interior.')
