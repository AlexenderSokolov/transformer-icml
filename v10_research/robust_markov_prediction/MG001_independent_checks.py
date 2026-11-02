from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
D=Path(__file__).parent

def g(x,L):
 u=x;v=F(0)
 for j in range(L):
  v+=max(F(0),u-F(1,4))/2**j
  u=min(F(1),4*u)
 return v+u/2**L

def inv(z,L):
 xs=[F(0)]+[F(1,4**j) for j in reversed(range(L+1))]
 for x,y in zip(xs,xs[1:]):
  a,b=g(x,L),g(y,L)
  if a<=z<=b:return x+(y-x)*(z-a)/(b-a)
 raise AssertionError((z,L))

# Exact rational tests: x square-rational so sqrt(x) is represented exactly.
n_inverse=0
for L in range(9):
 for i in range(33):
  s=F(i,32);x=s*s
  for j in range(65):
   y=F(j,64);eps=abs(g(y,L)-g(x,L))
   assert abs(y-x)<=4*s*eps+4*eps*eps+2*eps/2**L
   assert inv(g(y,L),L)==y
   n_inverse+=1

# Normalization is tested independently without compander assumptions, including
# true empty rows and positive spurious reconstructed mass.
n_norm=0
for K in [2,3]:
 for M in [1,7,64]:
  rows=list(product([F(0),F(1,8),F(1,2)],repeat=K))
  for x in rows:
   if sum(x)>1:continue
   for y in rows:
    A=sum(x)+F(K,M);B=sum(y)+F(K,M)
    tv=sum(abs((u+F(1,M))/A-(v+F(1,M))/B) for u,v in zip(x,y))/2
    assert tv<=sum(abs(u-v) for u,v in zip(x,y))/A
    n_norm+=1

# Entire binary second-order histories with exact probabilities. Each source
# has four unrelated transition probabilities, not an IID or stationary proxy.
tables=list(product([F(0),F(1)],repeat=4))+[
 (F(0),F(1,3),F(2,3),F(1)),
 (F(1,7),F(1,2),F(4,5),F(2,3)),
 (F(1),F(0),F(1,2),F(0))]
n_occ=0
for theta in tables:
 for initial in product([0,1],repeat=2):
  for M in range(1,9):
   probs=[F(0)]*(M+1)
   for future in product([0,1],repeat=M):
    hist=initial+future;p=F(1)
    for t in range(2,M+2):
     a,b=hist[t-2:t];q=theta[2*a+b]
     p*=q if hist[t] else 1-q
    terminal=hist[-2:]
    J=sum(hist[t:t+2]==terminal for t in range(M))
    probs[J]+=p
   assert sum(probs)==1
   for threshold in range(1,M+2):
    assert sum(probs[:threshold])<=min(F(1),F(16*threshold,M+1))
    n_occ+=1

# Nontrivial UC domain M>16 using deterministic second-order sources, where
# exact paths suffice (all arbitrary starts, all deterministic tables).
for theta in product([0,1],repeat=4):
 for initial in product([0,1],repeat=2):
  for M in [17,32,64,129]:
   hist=list(initial)
   for _ in range(M):hist.append(theta[2*hist[-2]+hist[-1]])
   terminal=tuple(hist[-2:]);J=sum(tuple(hist[t:t+2])==terminal for t in range(M))
   for threshold in range(1,M+2):
    assert F(J<threshold)<=min(F(1),F(16*threshold,M+1))
    n_occ+=1

# Nontrivial exact stochastic occupancy by dynamic programming separately
# for each possible terminal state; departure counts exclude time M.
for theta in tables[-3:]:
 for initial in product([0,1],repeat=2):
  for M in [17,32,64]:
   probs=[F(0)]*(M+1)
   for target in range(4):
    states={(2*initial[0]+initial[1],0):F(1)}
    for step in range(M):
     nxt={}
     for (s,k),p in states.items():
      kk=k+(s==target)
      for z in [0,1]:
       v=2*(s%2)+z;w=theta[s] if z else 1-theta[s]
       key=(v,kk);nxt[key]=nxt.get(key,F(0))+p*w
     states=nxt
    for (s,k),p in states.items():
     if s==target:probs[k]+=p
   assert sum(probs)==1
   for threshold in range(1,M+2):
    assert sum(probs[:threshold])<=min(F(1),F(16*threshold,M+1))
    n_occ+=1

out={'status':'PASS','scope':'Exact rational finite tests; not formal verification or a finite-evaluator/network audit','inverse_cases':n_inverse,'normalization_cases':n_norm,'occupation_cases':n_occ,'theorem_sha256':hashlib.sha256((D/'MG001_theorem.md').read_bytes()).hexdigest()}
(D/'MG001_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
