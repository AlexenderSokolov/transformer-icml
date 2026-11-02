#!/usr/bin/env python3
"""Fresh reviewer checks; exact finite diagnostics, not universal verification."""
from fractions import Fraction as Q
from itertools import product,combinations
from math import comb
from pathlib import Path
import hashlib,json,random
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
states=((0,0),(0,1),(1,0),(1,1));rnd=random.Random(202611021326)
counts={'receipts':0,'matrix_stationarity_all16':0,'trace_probabilities':0,'lambda_bound':0,'future_endpoint':0,'near_occupation_dp_stack_comparison':0,'weighted_future_dp':0,'pathwise_trace_balance':0,'strict_hamming_prefix':0,'singleton_support':0,'scalar_assembly':0}
def Pmake(a,b,e,t):
 p=(a,b,1-e,1-t);ans=[[Q(0)]*4 for _ in range(4)]
 for i,(_,v) in enumerate(states):
  for z in (0,1):ans[i][states.index((v,z))]=p[i] if z else 1-p[i]
 return ans

def mm(P,R):return [[sum((P[i][z]*R[z][j] for z in range(4)),Q(0)) for j in range(4)] for i in range(4)]
def eye():return [[Q(i==j) for j in range(4)] for i in range(4)]
def power(P,n):
 A=eye()
 for _ in range(n):A=mm(A,P)
 return A

def prob_small(P,start,n,K):
 dp={(start,0):Q(1)}
 for _ in range(n):
  nd={}
  for (i,c),v in dp.items():
   cc=c+(i!=3)
   if cc>K:continue
   for j,p in enumerate(P[i]):
    if p:nd[j,cc]=nd.get((j,cc),Q(0))+v*p
  dp=nd
 return [sum((v for (i,c),v in dp.items() if i==j),Q(0)) for j in range(4)]
def binom(n,p):return [Q(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)]
def bincompare(m,d,K,a):
 l=binom(m,d);r=binom(K,a)
 return sum((p*sum(r[j:],Q(0)) for j,p in enumerate(l) if j<=K),Q(0))
for unit in ['SC003','AB003','CB001']:
 r=json.loads((ROOT/f'intake/{unit}_acceptance.json').read_text())
 assert hashlib.sha256((ROOT/r['proof']).read_bytes()).hexdigest()==r['sha256']
 counts['receipts']+=1
for idx in range(96):
 a,b,e,t=[Q(rnd.randint(1,49),50) for _ in range(4)]
 if idx%4==0:t=Q(1,rnd.randint(100,3000))
 if idx%4==1:b=Q(1,rnd.randint(100,3000))
 x=1/(e/a+2+b/t);y=x*e/a;w=x*b/t;pi=(y,x,x,w)
 P=Pmake(a,b,e,t);P2=mm(P,P)
 beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4))
 assert 0<beta<=1 and all(sum((pi[i]*P[i][j] for i in range(4)),Q(0))==pi[j] for j in range(4))
 assert all(P2[i][j]>=beta*pi[j] for i in range(4) for j in range(4));counts['matrix_stationarity_all16']+=1
 H=b+e-b*e;alpha=a*b/H;delta=t*e/H
 assert b/H==b+(1-b)*(1-e)*(b/H)
 assert e/H==e+(1-e)*(1-b)*(e/H)
 assert 0<alpha<=1 and 0<delta<=1;counts['trace_probabilities']+=1
 lam=min(a,a*y/w)
 assert lam==min(a,a*delta/alpha)
 assert beta*lam*lam<=9*delta*delta;counts['lambda_bound']+=1
 for q in [0,1,2,5,11,23]:
  assert a*power(P,q)[3][0]<=lam;counts['future_endpoint']+=1
 if idx<16:
  for n,K in [(2,0),(5,1),(8,3),(12,2),(64,2),(64,8)]:
   bc=bincompare(n-K,delta,K,alpha);future=power(P,7)
   for start in range(4):
    z=prob_small(P,start,n,K)
    assert z[3]<=bc
    counts['near_occupation_dp_stack_comparison']+=1
    weighted=a*sum((z[j]*future[j][0] for j in range(4)),Q(0))
    # NP3 has a sqrt term; rearrange and square only if its rational part is insufficient.
    remainder=max(Q(0),weighted-Q(24*K,n))
    assert beta*remainder*remainder<=Q(208*208,n*n)
    counts['weighted_future_dp']+=1
# All finite words, not probability-weighted: diagonal visits and transition balance.
for n in range(1,13):
 for word in product((0,1),repeat=n+2):
  Y=list(zip(word,word[1:]))
  if Y[-1]!=(1,1):continue
  visits=[(j,s) for j,s in enumerate(Y) if s in ((0,0),(1,1))]
  l11=[];l00=[]
  for (_,u),(_,v) in zip(visits,visits[1:]):
   (l11 if u==(1,1) else l00).append(int(u!=v))
  J11=sum(s==(1,1) for s in Y[:-1]);J00=sum(s==(0,0) for s in Y[:-1])
  assert len(l11)==J11 and len(l00)==J00 and sum(l11)<=sum(l00)
  K=n-J11
  if K<=n//2:
   assert sum(l11[:n-K])<=sum(l00) and J00<=K
  counts['pathwise_trace_balance']+=1
# The Hamming-prefix implication is pointwise, with protected final pair.
for M in range(2,8):
 n=M//2;prefix=n+1
 for word in product((0,1),repeat=M+2):
  for k in range(min(2,M)+1):
   for inds in combinations(range(M),k):
    z=list(word)
    for i in inds:z[i]^=1
    assert z[-2:]==list(word[-2:])
    clean0=prefix-sum(word[:prefix]);obs0=prefix-sum(z[:prefix])
    assert abs(clean0-obs0)<=k
    for h in range(prefix+1):
     if obs0<=h:assert clean0<=h+k
    counts['strict_hamming_prefix']+=1
# Unsupported starts under an absorbing diagonal.
for absorbing in [0,3]:
 for a,b,e,t in [(Q(0),Q(1,4),Q(3,4),Q(1,3)),(Q(2,3),Q(2,3),Q(1,4),Q(0))]:
  if (absorbing==0 and a) or (absorbing==3 and t):continue
  P=Pmake(a,b,e,t)
  for start in range(4):
   z=prob_small(P,start,9,3);future=power(P,4)
   weighted=a*sum((z[j]*future[j][0] for j in range(4)),Q(0))
   assert weighted==0
   counts['singleton_support']+=1
for M in range(64,10001):
 n=M//2
 assert Q(96,n)<=Q(288,M) and Q(416,n)<=Q(1248,M)
 assert 1572<2**11 and 288<2**9
 counts['scalar_assembly']+=1
proof=HERE/'CB002_near_prefix_veto_partial.md'
result={'status':'PASS_TESTED_INSTANCES_ONLY','arithmetic':'exact Fraction and integer throughout; squared comparisons avoid approximate roots','counts':counts,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'scope':'Independent finite diagnostics for the partial risk-increment theorem only. Not formal verification or full-adaptation evidence.'}
(HERE/'CB002_independent_exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
