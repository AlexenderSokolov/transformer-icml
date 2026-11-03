#!/usr/bin/env python3
"""Finite author diagnostics for BP001. Exact algebra; explicitly numeric exponential tail comparisons."""
from fractions import Fraction as F
from pathlib import Path
from math import comb,exp
from itertools import product
import hashlib,json,random
D=Path(__file__).resolve().parent;R=D.parents[1]
S=((0,0),(0,1),(1,0),(1,1));rng=random.Random(202611021352)
C={'source_receipts':0,'stationary_all16':0,'target_hitting_moment_checks':0,'weighted_hitting_scales':0,'return_tail_numeric_comparisons':0,'path_reverse_window_identities':0,'exact_word_reversal':0}
def mat(a,b,e,t):
 th=(a,b,1-e,1-t);P=[[F(0)]*4 for _ in range(4)]
 for i,(_,v) in enumerate(S):
  for z in (0,1):P[i][S.index((v,z))]=th[i] if z else 1-th[i]
 return P

def solve(A,b):
 A=[list(row)+[z] for row,z in zip(A,b)];N=len(b)
 for i in range(N):
  j=next(j for j in range(i,N) if A[j][i]);A[i],A[j]=A[j],A[i]
  q=A[i][i];A[i]=[x/q for x in A[i]]
  for j in range(N):
   if j!=i:
    q=A[j][i];A[j]=[x-q*y for x,y in zip(A[j],A[i])]
 return [row[-1] for row in A]
def moments(P,s):
 ids=[i for i in range(4) if i!=s];A=[[F(i==j)-P[i][j] for j in ids] for i in ids];ms={0:[F(1)]*4}
 for r in (1,2,3):
  rhs=[1+sum(F(comb(r,l))*sum(P[i][j]*ms[l][j] for j in ids) for l in range(1,r)) for i in ids]
  x=solve(A,rhs);row=[F(0)]*4
  for i,v in zip(ids,x):row[i]=v
  ms[r]=row
 ret={r:1+sum(F(comb(r,l))*sum(P[s][j]*ms[l][j] for j in ids) for l in range(1,r+1)) for r in (1,2,3)}
 return ms,ret

def countlaw(P,s,start,n):
 dp={(start,0):F(1)}
 for _ in range(n):
  nd={}
  for (i,k),v in dp.items():
   kk=k+(i==s)
   for j,p in enumerate(P[i]):
    if p:nd[j,kk]=nd.get((j,kk),F(0))+v*p
  dp=nd
 return dp

def prob(P,pi,bits):
 pairs=[S.index(bits[j:j+2]) for j in range(len(bits)-1)]
 p=pi[pairs[0]]
 for i,j in zip(pairs,pairs[1:]):p*=P[i][j]
 return p
for unit in ('BU001','SC003'):
 rec=json.loads((R/'intake'/f'{unit}_acceptance.json').read_text());assert hashlib.sha256((R/rec['proof']).read_bytes()).hexdigest()==rec['sha256'];C['source_receipts']+=1
for z in range(36):
 a,b,e,t=[F(rng.randrange(1,20),20) for _ in range(4)]
 if z%4==0:b=F(1,200);e=1-b
 x=1/(e/a+2+b/t);pi=(x*e/a,x,x,x*b/t);P=mat(a,b,e,t)
 P2=[[sum(P[i][h]*P[h][j] for h in range(4)) for j in range(4)] for i in range(4)]
 beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4));gamma=(a,F(1),F(1),t)
 assert all(sum(pi[i]*P[i][j] for i in range(4))==pi[j] for j in range(4));assert all(P2[i][j]>=beta*pi[j] for i in range(4) for j in range(4));C['stationary_all16']+=1
 for s in range(4):
  ms,ret=moments(P,s);H=max(ms[1]);Hb=max(H,1/pi[s])
  assert ret[1]==1/pi[s] and Hb<=H+1
  for i in range(4):
   assert ms[2][i]<=2*Hb*ms[1][i] and ms[3][i]<=6*Hb*Hb*ms[1][i]
  assert ret[2]<=2*Hb*ret[1] and ret[3]<=6*Hb*Hb*ret[1]
  C['target_hitting_moment_checks']+=1
  assert beta*(pi[s]*gamma[s]*H)**2<=25
  assert beta*(pi[s]*gamma[s]*Hb)**2<=100;C['weighted_hitting_scales']+=1
  if z<6:
   for n in (4,16,64):
    for start in range(4):
     law=countlaw(P,s,start,n)
     low=sum((v for (_,k),v in law.items() if k<F(n)*pi[s]/16),F(0))
     high=sum((v for (_,k),v in law.items() if k>4*F(n)*pi[s]+1),F(0))
     assert float(low)<=2*exp(-n/(8*float(Hb)))+1e-12
     assert float(high)<=exp(-n/(2*float(Hb)))+1e-12
     C['return_tail_numeric_comparisons']+=2
 if z<3:
  for N in range(4,11):
   M=N-2;n=M//2;m=M-n
   for bits in product((0,1),repeat=N):
    rev=tuple(reversed(bits));assert prob(P,pi,bits)==prob(P,pi,rev);C['exact_word_reversal']+=1
    orig=[S.index(bits[j:j+2]) for j in range(M+1)];back=[S.index(rev[j:j+2]) for j in range(M+1)]
    for s in range(4):
     v=S.index(tuple(reversed(S[s])))
     assert sum(q==s for q in orig[:n])==sum(q==v for q in back[m+1:])
     assert sum(q==s for q in orig[n:M])==sum(q==v for q in back[1:m+1])
     C['path_reverse_window_identities']+=1
p=D/'BP001_stationary_weighted_balance.md'
out={'status':'PASS_TESTED_INSTANCES_ONLY','counts':C,'arithmetic':'Exact Fraction for algebra, moments, certificate and word laws; floating exp only for explicitly numeric tail comparisons','proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Stationary weighted imbalance only; no arbitrary-start gate-bias or standalone estimator claim.'}
(D/'BP001_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
