from fractions import Fraction as F
from math import log1p,sqrt
import json
from pathlib import Path
out={}; kernels=0; floors=0; cases=0
for M in [64,65,256,10000]:
 for e in [F(1,M),F(1,16)]:
  if e<F(1,M): continue
  for p in [F(1,4),F(1,2),F(3,4)]:
   a=F(1,2*M); x=1/(e/a+2+2*p); pi=[x*e/a,x,x,2*p*x]
   P=[[1-a,a,0,0],[0,0,1-p,p],[e,1-e,0,0],[0,0,F(1,2),F(1,2)]]
   PP=[[sum(P[i][k]*P[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
   assert [sum(pi[i]*P[i][j] for i in range(4)) for j in range(4)]==pi
   assert all(PP[i][j]>=e*e*pi[j] for i in range(4) for j in range(4));kernels+=1
for qmassnum in range(1,321):
 qmass=F(qmassnum,16)
 for pn in range(65):
  p=F(pn,64); n1=(qmass*p).__floor__();n0=(qmass*(1-p)).__floor__(); N=n0+n1
  if N:
   assert abs(F(n1,N)-p)<=min(p,1-p,2/qmass);floors+=1
for M in [64,65,255,256,257,4096,65536,2**32]:
 for beta in [0,1/M**2,1/M,1/256,1/16,1]:
  for Q in [16,32,256,65536]:
   for k in [1,2,16,1024,2**32]:
    z=k*Q
    for binary in [False,True]:
     t=M*max(sqrt(beta) if binary else beta,1/M);W=(1+log1p(z/t))/z;s=1/sqrt(M)
     limit=1/256 if binary else 1/16
     if beta>limit: assert W<=1/Q+2*s+1e-15
     if z>M/4: assert W<=5*s+1e-15
     if z>M**.75: assert W<=5*s+1e-15
     if beta<=limit and z<=min(M/4,M**.75):
      L=log1p(min(z/t,M/z)/8)/z; assert W<=1/Q+24*L+1e-15
     cases+=1
out={'exact_binary_witness_checks':kernels,'exact_floor_cases':floors,'floating_scalar_surface_cases':cases,'status':'PASS','limitations':'Finite corroboration; does not prove universal statements. Rational kernels/floors exact; scalar log checks floating.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
