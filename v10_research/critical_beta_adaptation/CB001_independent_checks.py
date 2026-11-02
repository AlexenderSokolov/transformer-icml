#!/usr/bin/env python3
"""Independent finite rational checks for CB001. Not a universal proof."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import random, hashlib, json
D=Path(__file__).resolve().parent
R=D.parent
states=((0,0),(0,1),(1,0),(1,1))
rng=random.Random(202611021314)
counts={'source_tables':0,'stationarity_and_all16_certificate':0,'endpoint_horizons':0,'run_dp_cases':0,'initial_run_cases':0,'boundary_support_cases':0,'entry_count_paths':0,'canonical_support_paths':0,'receipt_hashes':0}
def Pmat(a,b,e,t):
 th=(a,b,1-e,1-t)
 P=[[F(0) for _ in states] for _ in states]
 for i,(_,v) in enumerate(states):
  for bit in (0,1):P[i][states.index((v,bit))]=th[i] if bit else 1-th[i]
 return P
def mul(P,Q):return [[sum((P[i][h]*Q[h][j] for h in range(4)),F(0)) for j in range(4)] for i in range(4)]
def stationary(a,b,e,t):
 x=1/(e/a+2+b/t)
 return (x*e/a,x,x,x*b/t)
def run_event(P,M,L,init,bit=1):
 # Streak is capped at L+2; found remembers a run anywhere.
 initial=states[init]
 streak=2 if initial==(bit,bit) else (1 if initial[1]==bit else 0)
 d={(init,streak,streak>=L+2):F(1)}
 for _ in range(M):
  nd={}
  for (u,streak,found),mass in d.items():
   for v,p in enumerate(P[u]):
    if not p:continue
    streak2=min(L+2,streak+1) if states[v][1]==bit else 0
    key=(v,streak2,found or streak2>=L+2)
    nd[key]=nd.get(key,F(0))+mass*p
  d=nd
 terminal=0 if bit==1 else 3
 return sum((mass for (u,streak,found),mass in d.items() if u==terminal and found),F(0))

base=[F(1,1000),F(1,100),F(1,10),F(1,2),F(9,10),F(99,100)]
tables=[tuple(rng.choice(base) for _ in range(4)) for _ in range(70)]
tables += [(F(1,2),F(1,1000),F(1,2),F(1,1000)),(F(1,1000),F(1,2),F(1,2),F(1,2))]
max_scaled=F(0)
for a,b,e,t in tables:
 P=Pmat(a,b,e,t);pi=stationary(a,b,e,t);P2=mul(P,P)
 beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4))
 assert 0<beta<=1
 assert all(sum((pi[i]*P[i][j] for i in range(4)),F(0))==pi[j] for j in range(4))
 assert all(P2[i][j]>=beta*pi[j] for i in range(4) for j in range(4))
 y,x,_,w=pi
 assert b*b>=beta*w
 assert y==(1-w)*e/(e+2*a)
 assert a==t*w*(e+2*a)/(b*(1-w))
 z=min(a,t*e/b)
 assert beta*z*z<=4*t*t
 counts['source_tables']+=1;counts['stationarity_and_all16_certificate']+=1
 power=[[F(i==j) for j in range(4)] for i in range(4)]
 for h in range(17):
  assert w*power[3][0]<=y
  assert beta*(a*power[3][0])**2<=4*t*t
  counts['endpoint_horizons']+=1
  power=mul(power,P)
 for M in (4,7,12,20):
  L=M//2
  for init in range(4):
   prob=run_event(P,M,L,init)
   lhs=a*prob
   exact_fac=t*(1+M*t)*(1-t)**L
   scalar_fac=F(1,L+1)+F(2*M,(L+1)*(L+2))
   assert beta*lhs*lhs<=4*exact_fac*exact_fac
   assert exact_fac<=scalar_fac
   assert scalar_fac<=F(10,M)
   max_scaled=max(max_scaled,beta*lhs*lhs*F(M*M))
   counts['run_dp_cases']+=1
  # Initial ones: after L self-transitions, run remaining steps.
  remain=M-L
  PP=[[F(i==j) for j in range(4)] for i in range(4)]
  for _ in range(remain):PP=mul(PP,P)
  lhs=a*(1-t)**L*PP[3][0]
  assert beta*lhs*lhs<=4*t*t*(1-t)**(2*L)
  assert beta*lhs*lhs<=F(4,(L+1)**2)
  counts['initial_run_cases']+=1
# Boundary supports: all-state certificate and arbitrary-start event zero-weight check.
for a,b,e,t,pi in [(F(0),F(1,4),F(3,4),F(1,4),(F(1),F(0),F(0),F(0))),
                  (F(1,4),F(3,4),F(1,4),F(0),(F(0),F(0),F(0),F(1)))]:
 P=Pmat(a,b,e,t);P2=mul(P,P)
 beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4) if pi[j])
 assert beta>0
 for M in (4,8,12):
  for init in range(4):
   assert a*run_event(P,M,M//2,init,1)==0
   assert t*run_event(P,M,M//2,init,0)==0
   counts['boundary_support_cases']+=1
# Exhaustive combinatorial entry counting, independent of any source.
for N in range(2,14):
 for bits in product((0,1),repeat=N):
  ys=[bits[i:i+2] for i in range(N-1)]
  entries=sum(ys[s]==(1,1) and (s==0 or ys[s-1]!=(1,1)) for s in range(len(ys)))
  exits=sum(ys[s]==(1,1) and ys[s+1]!=(1,1) for s in range(len(ys)-1))
  assert entries<=1+exits
  counts['entry_count_paths']+=1
# Small exact canonical support analogue: any canonicalized word close to monotone
# inherits N111 >= M-j-3k and its full N111 leading loop run.
def hist(s):
 d={z:0 for z in product((0,1),repeat=3)}
 for i in range(len(s)-2):d[s[i:i+3]]+=1
 return d
def canonical(s):
 H=hist(s)
 skeleton=[s[i+2] for i in range(len(s)-2) if s[i:i+3] not in ((0,0,0),(1,1,1))]
 return tuple([1]*(H[(1,1,1)]+2)+skeleton+[0]*H[(0,0,0)])
for M in range(8,13):
 for middle in product((0,1),repeat=M-2):
  s=(1,1)+middle+(0,0);z=canonical(s)
  H=hist(z)
  assert z[:H[(1,1,1)]+2]==(1,)*(H[(1,1,1)]+2)
  for j in range(2,M//2+1):
   null=(1,)*(M+2-j)+(0,)*j
   k=sum(q!=r for q,r in zip(z,null))
   assert H[(1,1,1)]>=M-j-3*k
   counts['canonical_support_paths']+=1
for unit in ['SC003','AB003','BK001','BK002']:
 receipt=json.loads((R/f'intake/{unit}_acceptance.json').read_text())
 assert hashlib.sha256((R/receipt['proof']).read_bytes()).hexdigest()==receipt['sha256']
 counts['receipt_hashes']+=1
proof=D/'CB001_long_run_veto_partial.md'
out={'status':'PASS_FINITE_INDEPENDENT_CHECKS','arithmetic':'exact fractions/integers throughout; square-root inequalities squared only after verifying nonnegative sides','counts':counts,'max_beta_M2_loss2_in_run_DP':str(max_scaled),'proof_sha256_at_check':hashlib.sha256(proof.read_bytes()).hexdigest(),'limits':'Finite checks do not establish universal proof, formal verification, external review, or arbitrary-corruption adaptation. General mathematical audit is separate.'}
(D/'CB001_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
