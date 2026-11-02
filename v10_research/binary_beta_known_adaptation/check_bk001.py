#!/usr/bin/env python3
"""Finite exact diagnostics for BK001, not universal proof or independent review."""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
from itertools import product
import json,hashlib
HERE=Path(__file__).resolve().parent
STATES=[(0,0),(0,1),(1,0),(1,1)]
def pmatrix(theta):
 P=[[F(0)]*4 for _ in range(4)]
 for i,(u,v) in enumerate(STATES):
  for bit in [0,1]:P[i][STATES.index((v,bit))]=theta[i] if bit else 1-theta[i]
 return P
def mul(A,B):return [[sum(A[i][h]*B[h][j] for h in range(4)) for j in range(4)] for i in range(4)]
def hist(word):return Counter(tuple(word[i:i+3]) for i in range(len(word)-2))
def canonical(word):
 hs=hist(word); triples=[tuple(word[i:i+3]) for i in range(len(word)-2)]
 return [1]*(hs[(1,1,1)]+2)+[t[2] for t in triples if t not in [(0,0,0),(1,1,1)]]+[0]*hs[(0,0,0)]
canon_count=0; distance_count=0
for M in range(2,17):
 for middle in product([0,1],repeat=M-2):
  word=[1,1]+list(middle)+[0,0]; z=canonical(word); hs=hist(word)
  assert len(z)==M+2 and z[:2]==[1,1] and z[-2:]==[0,0] and hist(z)==hs
  J00=hs[(0,0,0)]+hs[(0,0,1)]
  J01=hs[(0,1,0)]+hs[(0,1,1)]
  J10=hs[(1,0,0)]+hs[(1,0,1)]
  U=hs[(0,0,1)]; V=hs[(1,1,0)]
  assert hs[(1,0,0)]==U+1 and hs[(0,1,1)]==V-1
  assert U+V<=J01+J10
  E=M-hs[(0,0,0)]-hs[(1,1,1)]
  for j in range(2,M+1):
   null=[1]*(M+2-j)+[0]*j
   dist=sum(a!=b for a,b in zip(z,null))
   assert dist<=E+abs(hs[(0,0,0)]-j)
   assert dist<=3*(J01+J10)+abs(J00-j)
   distance_count+=1
  canon_count+=1
c=F(1,4096); member_count=0; scalar_count=0; ratio_rows=[]
for n in [8,9,16,32,64,128,512,4096,8192,10000]:
 M=n**10;k=n**9;delta=F(1,n**5);e=1-delta;x=c*k/M;beta=F(1,M);T=M//8
 js=sorted(set([k,min(k+1,T),(k+T)//2,T]))
 for j in js:
  y=F(j,M);w=1-y-2*x;a=x*e/y;t=x*delta/w
  assert a>=delta and 0<a<=c and w>=F(3,4) and 0<t<=F(1,4)
  pi=[y,x,x,w];P=pmatrix([a,delta,delta,1-t]);P2=mul(P,P);P3=mul(P2,P)
  assert [sum(pi[h]*P[h][i] for h in range(4)) for i in range(4)]==pi
  assert all(P2[u][v]>=beta*pi[v] for u in range(4) for v in range(4))
  lam=c*k/F(4*n**15)
  assert all(P3[u][3]>=a*delta/2>=lam for u in range(4))
  member_count+=1
 if n>=64:
  assert c*n**4/16>=2*n
  assert F(1)/(1+c*n**4/16)<=F(1,2*n)
  scalar_count+=1
 if n>=4096:
  fail=(1792/c+229376)/n**2
  assert fail<=F(231,512)<F(1,2)
  assert F(7*k,16)<k
  ratio_rows.append({'n':n,'conditional_failure_upper':str(fail),'lambda':str(c*k/F(4*n**15))})
assert (1792/c+229376)/4096**2==F(231,512)
proof='BK001_histogram_adaptation_obstruction.md'
out={'status':'PASS_TESTED_INSTANCES_ONLY','full_words_canonicalized':canon_count,'exact_distance_comparisons':distance_count,
 'exact_all_state_certificate_stationarity_atom_cases':member_count,'exact_conditioning_scalar_cases':scalar_count,
 'acceptance_rows':ratio_rows,'proof_sha256':hashlib.sha256((HERE/proof).read_bytes()).hexdigest(),
 'limits':'No giant-M word was materialized. Canonicalization exhaustive only at small M; explicit large-family matrix/constant checks are exact rational. Universal variance, conditional and constrained-risk proofs require independent full review.'}
(HERE/'BK001_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
