#!/usr/bin/env python3
"""Independent finite tests of CB003. Integer/Fraction arithmetic only."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib,json,random
D=Path(__file__).resolve().parent;R=D.parent
counts={'large_full_words':0,'small_count_geometry':0,'strict_identity_cases':0,'all16_certificate':0,'small_exact_word_probabilities':0,'profile_domain':0,'accepted_receipt_hashes':0}
states=((0,0),(0,1),(1,0),(1,1))
def ceilroot(M):
 h=isqrt(M);return h+(h*h<M)
def edits(M,h,ell,t):
 N=M+2;lead=M+1-t
 x=bytearray([1])*lead+bytearray(t+1)
 z=x.copy();pos=list(range(2,h+3))+[lead+3*j-1 for j in range(1,ell+1)]
 for p in pos:z[p]^=1
 assert len(set(pos))==h+1+ell
 assert max(pos)<M and min(pos)>=0
 assert z[-2:]==x[-2:]==bytearray([0,0])
 assert sum(a!=b for a,b in zip(x,z))==h+1+ell
 return x,z,pos
def row00(z):
 J=C=0
 for u,v,w in zip(z,z[1:],z[2:]):
  if u==v==0:J+=1;C+=w
 return C,J
def count111(z):return sum(a==b==c==1 for a,b,c in zip(z,z[1:],z[2:]))
def Pmatrix(r):
 P=[[F(0) for _ in range(4)] for _ in range(4)]
 for i,(u,v) in enumerate(states):
  for bit in (0,1):P[i][states.index((v,bit))]=r if v!=bit else 1-r
 return P
for M in [2**20,2**20+1,2**20+123,2**22]:
 h=ceilroot(M);n=M//2;T=M//8
 for k in sorted(set([64*h,(64*h+T)//2,T])):
  for t in sorted(set([k,(k+T)//2,T])):
   ell=k//4
   assert 64*h<=k<=T and h+5<=M+1-t and h+3<=n+1<M+1-t
   assert 3*ell<=t-1
   x,z,pos=edits(M,h,ell,t)
   assert row00(x)==(0,t-1)
   C,J=row00(z)
   assert (C,J)==(ell+1,t-1-2*ell+h)
   assert z[:n+1].count(0)==h+1
   assert C>12*h and 0<C<=J<=2*t
   q=F(C,J);r=F(1,2*M)
   assert q>=F(k,8*t) and q-r>=F(k,16*t)
   assert h+1+ell<k
   assert k*k>=M
   counts['large_full_words']+=1;counts['profile_domain']+=1
 # Every row of the two-step pair kernel, not merely its stationary support.
 r=F(1,2*M);beta=F(1,M);P=Pmatrix(r)
 pi=[(r if u!=v else 1-r)/2 for u,v in states]
 assert all(sum((pi[i]*P[i][j] for i in range(4)),F(0))==pi[j] for j in range(4))
 for i in range(4):
  for j in range(4):
   P2=sum((P[i][a]*P[a][j] for a in range(4)),F(0))
   assert P2>=beta*pi[j]
   counts['all16_certificate']+=1
# Wider small combinatorial domain tests count identities independently of giant
# theorem thresholds. All geometry prerequisites are checked before execution.
for M in [32,48,64,96,128]:
 for h in range(1,7):
  for t in range(4,min(M//2,M-h-5)+1):
   for ell in range(1,(t-1)//3+1):
    if h+5>M+1-t:continue
    x,z,pos=edits(M,h,ell,t)
    assert row00(z)==(ell+1,t-1-2*ell+h)
    counts['small_count_geometry']+=1
# Exact one-flip source probability, including initial-pair factor, at small M.
for M in [8,16,32,64,128]:
 r=F(1,2*M)
 for t in range(2,M-1):
  x=[1]*(M+1-t)+[0]*(t+1)
  p=(1-r)/2
  for j in range(2,M+2):p*=r if x[j]!=x[j-1] else 1-r
  assert p==r/2*(1-r)**M and p>=F(1,8*M)
  counts['small_exact_word_probabilities']+=1
# Total-map recognition: a non-one-flip word is untouched.
def kernel(x,M,k):
 h=ceilroot(M);T=M//8
 if len(x)!=M+2:return x
 lead=0
 while lead<len(x) and x[lead]==1:lead+=1
 t=M+1-lead
 if not(k<=t<=T) or any(x[lead:]):return x
 z=x.copy()
 for p in range(2,h+3):z[p]=0
 for j in range(1,k//4+1):z[lead+3*j-1]=1
 return z
rng=random.Random(202611021335)
for _ in range(100):
 M=256;k=16
 x=bytearray(rng.randrange(2) for _ in range(M+2))
 assert kernel(x,M,k)==x
 counts['strict_identity_cases']+=1
for unit in ['AB003','CB002','SC003','BT002']:
 receipt=json.loads((R/f'intake/{unit}_acceptance.json').read_text())
 assert hashlib.sha256((R/receipt['proof']).read_bytes()).hexdigest()==receipt['sha256']
 counts['accepted_receipt_hashes']+=1
proof=D/'CB003_fixed_veto_bypass.md'
out={'status':'PASS_FINITE_INDEPENDENT_CHECKS','arithmetic':'Exact integers/Fraction throughout; large word probabilities use the analytic Bernoulli inequality rather than materializing giant rational powers','counts':counts,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'scope':'Explicit failure of W(AB003) only; not a full-history impossibility theorem or formal/external verification.'}
(D/'CB003_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
