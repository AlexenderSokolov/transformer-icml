#!/usr/bin/env python3
"""Exact finite author diagnostics for CB002. Not independent review or proof."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib,json,random
D=Path(__file__).resolve().parent;R=D.parent;states=((0,0),(0,1),(1,0),(1,1));rng=random.Random(202611021326)
C={'source_receipts':0,'source_all16_endpoint_factor':0,'stack_event_word_checks':0,'occupation_stack_probability':0,'weighted_future_terminal':0,'support_boundary':0,'prefix_edit_implications':0}
def mat(a,b,e,t):
 th=(a,b,1-e,1-t);P=[[F(0)]*4 for _ in range(4)]
 for i,(u,v) in enumerate(states):
  for bit in (0,1):P[i][states.index((v,bit))]=th[i] if bit else 1-th[i]
 return P

def mul(P,Q):return [[sum((P[i][h]*Q[h][j] for h in range(4)),F(0)) for j in range(4)] for i in range(4)]
def power(P,n):
 out=[[F(i==j) for j in range(4)] for i in range(4)]
 while n:
  if n&1:out=mul(out,P)
  P=mul(P,P);n//=2
 return out

def occ(P,start,n):
 dp={(start,0):F(1)}
 for _ in range(n):
  nd={}
  for (i,K),mass in dp.items():
   kk=K+(i!=3)
   for j,p in enumerate(P[i]):
    if p:nd[j,kk]=nd.get((j,kk),F(0))+mass*p
  dp=nd
 return dp

def binom_le(m,d,K,a):
 # P(Bin(m,d)<=Bin(K,a)), independent.
 L=[F(comb(m,j))*d**j*(1-d)**(m-j) for j in range(m+1)]
 cum=[];s=F(0)
 for x in L:s+=x;cum.append(s)
 return sum((F(comb(K,j))*a**j*(1-a)**(K-j)*cum[min(j,m)] for j in range(K+1)),F(0))
for unit in ('SC003','AB003','CB001'):
 rec=json.loads((R/f'intake/{unit}_acceptance.json').read_text())
 assert hashlib.sha256((R/rec['proof']).read_bytes()).hexdigest()==rec['sha256'];C['source_receipts']+=1
for n in range(2,13):
 for bits in product((0,1),repeat=n+2):
  pairs=[states.index(bits[j:j+2]) for j in range(n+1)]
  if pairs[-1]!=3:continue
  visits=[v for v in pairs if v in (0,3)]
  departures=visits[:-1]
  J0=sum(v==0 for v in pairs[:-1]);J3=sum(v==3 for v in pairs[:-1]);K=n-J3
  assert departures.count(0)==J0 and departures.count(3)==J3
  b11=sum(u==3 and v==0 for u,v in zip(visits,visits[1:]));b00=sum(u==0 and v==3 for u,v in zip(visits,visits[1:]))
  assert b11<=b00 and J0<=K
  C['stack_event_word_checks']+=1
for z in range(24):
 a,b,e,t=[F(rng.randrange(1,20),20) for _ in range(4)]
 if z%3==0:t=F(1,200)
 x=1/(e/a+2+b/t);y=x*e/a;w=x*b/t;pi=(y,x,x,w);P=mat(a,b,e,t);P2=mul(P,P)
 beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4))
 assert all(sum(pi[i]*P[i][j] for i in range(4))==pi[j] for j in range(4))
 assert all(P2[i][j]>=beta*pi[j] for i in range(4) for j in range(4))
 H=b+e-b*e;alpha=a*b/H;delta=t*e/H;lam=min(a,a*y/w)
 assert beta*lam*lam<=9*delta*delta
 C['source_all16_endpoint_factor']+=1
 for n in ((8,16,64) if z<8 else (8,)):
  Ks=sorted(set([0,1,n//8,n//4,n//2,n]))
  bins={K:binom_le(n-K,delta,K,alpha) for K in Ks if K<=n//2}
  future={q:power(P,q) for q in (0,5,16)}
  for start in range(4):
   dp=occ(P,start,n)
   for K in Ks:
    if K<=n//2:
     p11=sum((mass for (v,k),mass in dp.items() if v==3 and k<=K),F(0))
     assert p11<=bins[K];C['occupation_stack_probability']+=1
    for q,Q in future.items():
     risk=a*sum((mass*Q[v][0] for (v,k),mass in dp.items() if k<=K),F(0))
     excess=max(F(0),risk-F(24*K,n))
     assert beta*excess*excess<=F(208,n)**2
     C['weighted_future_terminal']+=1
# Boundary tables satisfy the certificate at every unsupported state.
for th,pi in [((F(0),F(1,3),F(1,2),F(1,4)),(F(1),F(0),F(0),F(0))),((F(1,4),F(1,2),F(1,3),F(0)),(F(0),F(0),F(0),F(1)))]:
 P=mat(*th);P2=mul(P,P);support=[j for j,p in enumerate(pi) if p];beta=min(P2[i][j]/pi[j] for i in range(4) for j in support)
 assert beta>0
 for start in range(4):
  dp=occ(P,start,16)
  for K in (0,4,8,15,16):
   risk=th[0]*sum((mass for (v,k),mass in dp.items() if v==0 and k<=K),F(0))
   if K<16:assert risk==0
   C['support_boundary']+=1
for N in range(4,10):
 M=N-2;n=M//2
 for bits in product((0,1),repeat=N):
  clean=sum(x==0 for x in bits[:n+1])
  for mask in product((0,1),repeat=M):
   k=sum(mask);out=[x^(mask[i] if i<M else 0) for i,x in enumerate(bits)]
   observed=sum(x==0 for x in out[:n+1])
   assert clean<=observed+k and out[-2:]==list(bits[-2:])
   C['prefix_edit_implications']+=1
proof=D/'CB002_near_prefix_veto_partial.md'
out={'status':'PASS_TESTED_INSTANCES_ONLY','arithmetic':'Exact Fraction; square comparisons remove all square roots','counts':C,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'scope':'Safe veto risk increment only, not a standalone unknown-budget estimator theorem.'}
(D/'CB002_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
