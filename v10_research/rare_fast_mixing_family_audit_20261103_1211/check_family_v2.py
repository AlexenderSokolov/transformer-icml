#!/usr/bin/env python3
"""Exact rational checks, no RNG. Write unique JSONL, refuse overwrite."""
from fractions import Fraction as F
from itertools import product
import json, sys

STATES=('00','01','10','11')
def s(x): return str(x)
def matmul(A,B): return [[sum((A[i][k]*B[k][j] for k in range(4)),F(0)) for j in range(4)] for i in range(4)]
def rowmul(v,A): return [sum((v[k]*A[k][j] for k in range(4)),F(0)) for j in range(4)]
def setup(u,t):
 w=(1-u)/3; h=u*t/w
 P=[[1-t,t,0,0],[0,0,F(1,2),F(1,2)],[h,1-h,0,0],[0,0,F(1,2),F(1,2)]]
 return w,h,[u,w,w,w],[[F(z) for z in r] for r in P]
def rev(P,pi): return [[pi[j]*P[j][i]/pi[i] for j in range(4)] for i in range(4)]
def jmat(M): return [[s(v) for v in r] for r in M]
def check(u,t,tp,N):
 w,h,pi,P=setup(u,t); _,hp,pip,Q=setup(u,tp); P2=matmul(P,P); R=rev(P,pi); R2=matmul(R,R)
 assert pi==pip and rowmul(pi,P)==pi
 assert all(sum(row)==1 and all(0<=x<=1 for x in row) for row in P)
 assert all(P2[i][3]>=F(1,8) and R2[i][3]>=F(1,8) for i in range(4))
 assert sum(pi[i]*(P[i][1]+P[i][3]) for i in range(4))==2*w
 # Explicit exact trajectory and terminal-conditional row departure occupancies.
 # For terminal 00 the expected counts equal reverse-chain state occupations,
 # with edge reversal swapping forward row to reverse row.
 probs=[]; total=F(0); end=F(0); fcounts=[F(0)]*4; edges=[[F(0)]*4 for _ in range(4)]
 for bits in product('01',repeat=N):
  bits=''.join(bits); states=[STATES.index(bits[j:j+2]) for j in range(N-1)]; p=pi[states[0]]; q=pi[states[0]]
  for a,b in zip(states,states[1:]): p*=P[a][b]; q*=Q[a][b]
  total+=p
  if bits[-2:]=='00':
   end+=p
   for a,b in zip(states,states[1:]): fcounts[a]+=p; edges[a][b]+=p
  probs.append({'word':bits,'P':s(p),'Q':s(q),'terminal':bits[-2:]})
 assert total==1 and end==u
 cond_edges=[[z/u for z in row] for row in edges]
 # reversed row-occupancy predicts backward count coefficients for kl(t||tp), kl(h||hp)
 v=[F(1),F(0),F(0),F(0)]; occ=[F(0)]*4
 for _ in range(N-2):
  occ=[a+b for a,b in zip(occ,v)]; v=rowmul(v,R)
 backward=[sum(cond_edges[a][b] for a in range(4)) for b in range(4)]
 assert occ==backward
 # For each reverse row, conditional first predecessor has fixed Bernoulli law;
 # this verifies chain-rule coefficient exactly.
 if occ[0]: assert cond_edges[2][0]==occ[0]*t
 if occ[1]: assert cond_edges[0][1]==occ[1]*h
 return {'inputs':{'u':s(u),'w':s(w),'t':s(t),'tp':s(tp),'N':N},'h':s(h),'hp':s(hp),'pi':list(map(s,pi)),'P':jmat(P),'P2':jmat(P2),'reverse_P':jmat(R),'reverse_P2':jmat(R2),'path_total':s(total),'terminal_00_probability':s(end),'conditional_forward_edge_counts':jmat(cond_edges),'reverse_expected_occupation':list(map(s,occ)),'full_KL_coefficients':['(N-2)*u='+s((N-2)*u),'(N-2)*w='+s((N-2)*w)],'conditional_KL_coefficients':[s(occ[0]),s(occ[1])], 'path_probabilities':probs,'assertions':'PASS'}

cases=[(F(1,100),F(1,4),F(3,4)),(F(1,5),F(1,4),F(3,4)),(F(249,1000),F(3,4),F(1,4)),(F(1,10000),F(1,2),F(9,16))]
out=sys.argv[1]
with open(out,'x',encoding='utf-8') as f:
 for c in cases:
  for N in (2,3,4,7):
   r=check(*c,N); f.write(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n')
print('PASS: 16 exact rational input cases, all 624 deterministic paths; full per-word probabilities in JSONL; no sampling')
