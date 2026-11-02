#!/usr/bin/env python3
"""Finite corroboration only; exact certificates plus floating scalar grids."""
from fractions import Fraction as Q
from math import log1p,log,sqrt,exp,floor,comb
import json,hashlib
from pathlib import Path
out={'status':'PASS','scope':'finite diagnostics, not universal proof','counts':{}}
c=0
for M in [64,65,67,100,255,256,1000]:
 for beta0 in sorted(set([Q(1,M),Q(1,16),Q(1,32),Q(1,64)])):
  if beta0<Q(1,M):continue
  for p in [Q(1,4),Q(1,2),Q(3,4)]:
   a=Q(1,2*M);e=beta0-a;pi=[e/beta0,a*(1-p)/beta0,a*p/beta0,Q(0)]
   T=[[1-a,a*(1-p),a*p,Q(0)],[e,(1-e)*(1-p),(1-e)*p,Q(0)],[e,(1-e)*(1-p),(1-e)*p,Q(0)],pi]
   assert all(sum(row)==1 for row in T)
   assert all(sum(pi[y]*T[y][v] for y in range(4))==pi[v] for v in range(4))
   for x in range(4):
    for y in range(4):
     for u in range(4):
      for v in range(4):
       assert T[y][u]*T[u][v]>=beta0*pi[u]*T[u][v];c+=1
   L=int(1/(4*beta0))
   assert 4<=L<=M//4
   for j in range(2,L+1):
    w=pi[0]*T[0][0]*(1-a)**(M-j)*a*(1-e)**(j-1)
    assert w>=Q(1,32*M)
out['counts']['exact_all_pair_minorization']=c
c=0
for l in range(15):
 for b in range(1,17):
  for n in range(l+1):
   r=b*(n//b)
   assert Q(comb(l-r,n-r),comb(l,n)*comb(n,r))==Q(1,comb(l,r));c+=1
out['counts']['exact_erasure']=c
c=0;minratio=1e99
for M in [64,65,66,67,100,128,255,256,1000,10000,10**6]:
 for beta in sorted(set([0,1/M,0.5/M,2/M,1/64,1/32,1/16,0.1,0.5,1])):
  beta0=max(beta,1/M)
  for k in sorted(set([1,2,3,int(sqrt(M)),M//4,M//2,M-1,M])):
   eps=k/M;F=eps*(1+log1p(1/(beta0*k)));b=k+1
   iid=b/(32*(M+b))
   lower=iid
   if beta0<=1/16:
    L=floor(1/(4*beta0));rare=b/(2048*M)*log1p((L-1)/b)
    assert rare+1e-15>=eps*log1p(1/(beta0*k))/16384
    lower=max(lower,rare)
   assert lower+1e-15>=F/32768
   minratio=min(minratio,lower/(F/32768))
   for K in [3,4,10]:
    D=12*K**4;z=M/k
    psi=lambda x:1 if x>=1 else x*(1-log(x))
    if beta>=1/M:
     eta=(1-beta)**(M//4)
     assert eta*psi(D/z)<=5*D*F+1e-12
     upper=12*K*K*eps*(17+log1p(80/(beta*k)))+eta*psi(D/z)
     bound=(12*K*K*(17+log(80))+60*K**4)*F
     assert upper<=bound+1e-10
    else: assert psi(6*K**4/(z*(M+1)/M))<=6*K**4*F+1e-12
    c+=1
out['counts']['floating_scalar_cases']=c;out['minimum_tested_lower_margin_ratio']=minratio
out['failures']=[]
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
