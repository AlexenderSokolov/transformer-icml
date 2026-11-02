#!/usr/bin/env python3
"""Author finite exact checks for CB001; no proof/review substitute."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,random
D=Path(__file__).resolve().parent;R=D.parent
states=((0,0),(0,1),(1,0),(1,1))
rng=random.Random(202611021314)
counts={'accepted_source_hashes':0,'source_stationarity_all16':0,'endpoint_factor':0,'endpoint_transition':0,'longrun_all_starts_dp':0,'binomial_bounds':0,'bk001_prefix_bound':0}
def mat(a,b,e,t):
 th=(a,b,1-e,1-t)
 P=[[F(0)]*4 for _ in range(4)]
 for i,(u,v) in enumerate(states):
  for bit in (0,1):P[i][states.index((v,bit))]=th[i] if bit else 1-th[i]
 return P

def mul(P,Q):return [[sum((P[i][h]*Q[h][j] for h in range(4)),F(0)) for j in range(4)] for i in range(4)]
def event_mass(P,initial,M,L):
 threshold=L+2
 run=2 if initial==3 else (1 if initial==1 else 0)
 dp={(initial,min(run,threshold),run>=threshold):F(1)}
 for _ in range(M):
  nd={}
  for (i,run,seen),p in dp.items():
   for j,q in enumerate(P[i]):
    if not q:continue
    rr=min(threshold,run+1) if states[j][1] else 0
    key=(j,rr,seen or rr==threshold)
    nd[key]=nd.get(key,F(0))+p*q
  dp=nd
 return sum((p for (i,_,seen),p in dp.items() if i==0 and seen),F(0))
for unit in ['SC003','BT002','AB003','BK001','BK002']:
 receipt=json.loads((R/f'intake/{unit}_acceptance.json').read_text())
 assert hashlib.sha256((R/receipt['proof']).read_bytes()).hexdigest()==receipt['sha256']
 counts['accepted_source_hashes']+=1
for z in range(180):
 pars=[F(rng.randrange(1,100),100) for _ in range(4)]
 if z%3==0:pars[3]=F(1,rng.randrange(20,2000))
 a,b,e,t=pars;x=1/(e/a+2+b/t);y=x*e/a;w=x*b/t;pi=(y,x,x,w)
 P=mat(a,b,e,t);P2=mul(P,P)
 beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4))
 assert 0<beta<=1 and all(sum(pi[i]*P[i][j] for i in range(4))==pi[j] for j in range(4))
 assert all(P2[i][j]>=beta*pi[j] for i in range(4) for j in range(4))
 assert b*b>=beta*w and y==(1-w)*e/(e+2*a)
 counts['source_stationarity_all16']+=1
 endpoint=min(a,t*e/b)
 assert beta*endpoint*endpoint<=4*t*t
 counts['endpoint_factor']+=1
 H=[[F(int(i==j)) for j in range(4)] for i in range(4)]
 for h in range(17):
  assert w*H[3][0]<=y and a*H[3][0]<=endpoint
  counts['endpoint_transition']+=1
  H=mul(H,P)
 if z<24:
  for M in (2,3,4,8,12,20):
   L=M//2;scalar=F(1,L+1)+F(2*M,(L+1)*(L+2))
   for initial in range(4):
    risk=a*event_mass(P,initial,M,L)
    strong=t*(1+M*t)*(1-t)**L
    assert beta*risk*risk<=4*strong*strong
    assert beta*risk*risk<=4*scalar*scalar
    assert F(2)*scalar<=F(20,M)
    counts['longrun_all_starts_dp']+=1
for L in range(1,81):
 for i in range(101):
  t=F(i,100)
  assert t*(1-t)**L<=F(1,L+1)
  assert t*t*(1-t)**L<=F(2,(L+1)*(L+2))
  counts['binomial_bounds']+=1
for M in range(64,2049):
 k=M//8;j=M//8
 assert M-j-3*k>=M//2
 counts['bk001_prefix_bound']+=1
proof=D/'CB001_long_run_veto_partial.md'
out={'status':'PASS_TESTED_INSTANCES_ONLY','arithmetic':'Fraction exact throughout; square comparisons avoid floating square roots','counts':counts,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'scope':'Clean-risk increment and stated support checks only; no arbitrary-corruption or adaptation guarantee; no formal or external review.'}
(D/'CB001_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
