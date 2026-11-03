#!/usr/bin/env python3
"""Finite corroboration only: not a code benchmark or proof of asymptotics."""
from fractions import Fraction as F
from math import comb
from itertools import product
import json
from pathlib import Path

def ceilfrac(x): return -(-x.numerator//x.denominator)
def tail_error(m,p,tau,b):
 return sum((F(comb(m,j))*p**j*(1-p)**(m-j) for j in range(m+1) if (F(j,m)>=tau)!=bool(b)), F(0))
# Different true channel rows, including asymmetric perturbations, all share one nominal threshold.
p0,p1,alpha=F(1,8),F(7,8),F(1,8)
d=p1-p0; gamma=d/2-alpha; m=ceilfrac(4/gamma**2); tau=(p0+p1)/2
primitive_cases=0
for b,pnom in enumerate((p0,p1)):
 for t in range(17):
  p=pnom-alpha+2*alpha*F(t,16)
  assert 0<=p<=1
  assert tail_error(m,p,tau,b)<=F(1,256)
  primitive_cases+=1
# Tie-inclusive pairwise event: non-identical error probabilities do not hurt.
pair_cases=0
for s in range(1,49):
 probs=[F(1,256*(1+j%3)) for j in range(s)]
 dist=[F(1)]
 for p in probs:
  out=[F(0)]*(len(dist)+1)
  for j,v in enumerate(dist): out[j]+=v*(1-p);out[j+1]+=v*p
  dist=out
 assert sum(dist[(s+1)//2:])<=F(1,8)**s
 pair_cases+=1
for B in range(1,100001):
 k=(8*B-1).bit_length();q=2**k;K=(B+k-1)//k;n=4*K;ell=12*k
 assert 8*B<=q<16*B and n<=q and k>=3 and k<=4*B
 assert n*ell<=240*B
 assert 4*K-8*k*(K+1)<=-6*k*K-8*k<=-6*B
 assert k-3*(ell//4)==-8*k
# Exact small-volume check supplements the all-k entropy proof.
for k in range(3,101):
 ell=12*k;V=sum(comb(ell,j) for j in range(ell//4))
 assert 2**ell>=2**k*V
payload_cases=0
for M in range(1,11):
 for z in product((0,1),repeat=M+2):
  # Full arrays versus streaming counters; all words, including impossible-source words.
  tr=[[0,0],[0,0]]; ah=[0,0];tri=[[[0,0],[0,0]],[[0,0],[0,0]]];ah2=[[0,0],[0,0]]
  for j in range(M+2):
   if j>=2:
    i=j-1;tr[z[i]][z[j]]+=1
    if i<=M//2: ah[z[i]]+=1
    h=j-2;tri[z[h]][z[h+1]][z[j]]+=1
    if h<M//2: ah2[z[h]][z[h+1]]+=1
  t=z[-1];J=sum(z[i]==t for i in range(1,M+1));C=sum(z[i]==t and z[i+1]!=t for i in range(1,M+1));A=sum(z[i]==t for i in range(1,M//2+1))
  assert (J,C,A)==(sum(tr[t]),tr[t][1-t],ah[t])
  a,b=z[-2:];direction=1-a
  J2=sum(z[i:i+2]==(a,b) for i in range(M));C2=sum(z[i:i+2]==(a,b) and z[i+2]==direction for i in range(M));A2=sum(z[i:i+2]==(a,b) for i in range(M//2))
  assert (J2,C2,A2)==(sum(tri[a][b]),tri[a][b][direction],ah2[a][b])
  for jj,cc,aa,orient,first in ((J,C,A,t,True),(J2,C2,A2,direction,False)):
   gate=int(512*aa>=jj);qh=F(cc,jj) if jj and gate else F(0)
   p=qh if ((orient==0) if first else (orient==1)) else 1-qh
   assert 0<=p<=1
  payload_cases+=1
out={'status':'PASS_FINITE_CORROBORATION_NOT_FORMAL_PROOF','primitive_rational_cases':primitive_cases,'primitive_m':m,'pairwise_nonidentical_probability_cases':pair_cases,'parameter_B_range':[1,100000],'greedy_volume_k_range':[3,100],'exhaustive_payload_words':payload_cases,'payload_M_range':[1,10],'executed_full_code':False}
print(json.dumps(out,indent=2,sort_keys=True))
