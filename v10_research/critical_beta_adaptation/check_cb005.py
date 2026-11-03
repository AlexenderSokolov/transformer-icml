#!/usr/bin/env python3
"""Author diagnostics for CB005. Exact algebra/path tests; explicitly labeled float tails."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import random,math,hashlib,json
D=Path(__file__).resolve().parent;R=D.parent;rng=random.Random(202611021420)
C={'first_hit_density':0,'loop_rotation':0,'hitting_potential':0,'pointwise_kernel':0,'return_second_moment':0,'tilted_chain_exact':0,'tilted_path_identity':0,'joint_tail_float':0,'reflection_hitting_scale':0,'killing_edge_density':0,'scalar_assembly':0,'receipts':0}
def solve(A,b):
 n=len(b);a=[list(row)+[b[i]] for i,row in enumerate(A)]
 for j in range(n):
  q=next(i for i in range(j,n) if a[i][j]);a[j],a[q]=a[q],a[j]
  z=a[j][j];a[j]=[v/z for v in a[j]]
  for i in range(n):
   if i!=j:
    z=a[i][j]
    if z:a[i]=[a[i][k]-z*a[j][k] for k in range(n+1)]
 return [a[i][-1] for i in range(n)]
def mul(A,B):
 return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def powers(P,L):
 d=len(P);A=[[[F(i==j) for j in range(d)] for i in range(d)]]
 for _ in range(L):A.append(mul(A[-1],P))
 return A

def target(P,u):
 d=len(P);idx=[i for i in range(d) if i!=u]
 A=[[F(i==j)-P[i][j] for j in idx] for i in idx]
 hh=solve(A,[F(1)]*len(idx));h=[F(0)]*d
 for i,z in zip(idx,hh):h[i]=z
 mu=1+sum(P[u][j]*h[j] for j in range(d));p=1/mu;H=max(h);hb=max(H,mu)
 gg=solve(A,[1+2*sum(P[i][j]*h[j] for j in range(d)) for i in idx]);g=[F(0)]*d
 for i,z in zip(idx,gg):g[i]=z
 m2=1+2*sum(P[u][j]*h[j] for j in range(d))+sum(P[u][j]*g[j] for j in range(d))
 return p,H,hb,h,m2

def occupation(P,i,u,L):
 dp={(i,0):F(1)}
 for _ in range(L):
  nd={}
  for (v,k),mass in dp.items():
   kk=k+(v==u)
   for w,p in enumerate(P[v]):
    if p:nd[w,kk]=nd.get((w,kk),F(0))+mass*p
  dp=nd
 return sum((mass for (v,k),mass in dp.items() if v==u and F(k)>4*L*target(P,u)[0]+1),F(0))
for unit in ('SC003','BU001','BOD001'):
 rec=json.loads((R/f'intake/{unit}_acceptance.json').read_text());assert hashlib.sha256((R/rec['proof']).read_bytes()).hexdigest()==rec['sha256'];C['receipts']+=1
cases=[]
for d in (2,3,4):
 for z in range(8):
  P=[]
  for i in range(d):
   aa=[rng.randrange(1,20) for _ in range(d)]
   if z%2==0:aa[0]=1;aa[-1]*=10
   P.append([F(a,sum(aa)) for a in aa])
  cases.append(P)
 # Deterministic periodic cycles (irreducibility, no aperiodicity assumption).
 cases.append([[F(j==(i+1)%d) for j in range(d)] for i in range(d)])
for z,P in enumerate(cases):
 d=len(P);Pw=powers(P,32)
 for u in range(d):
  p,H,hb,h,m2=target(P,u)
  assert m2<=2*hb/p;C['return_second_moment']+=1
  for r in range(1,33):
   loop=sum((sum((Pw[j][v][u]*Pw[r-j][u][v] for j in range(r)),F(0)) for v in range(d)),F(0))
   assert loop==r*Pw[r][u][u];C['loop_rotation']+=1
   for v in range(d):
    cum=sum((Pw[j][v][u] for j in range(r)),F(0))
    assert cum==p*(r+sum(Pw[r][v][w]*h[w] for w in range(d))-h[v]);C['hitting_potential']+=1
    assert Pw[r][v][u]<=4*d*p*(1+H/r);C['pointwise_kernel']+=1
  for v in range(d):
   if v==u:continue
   dist=[F(i==v) for i in range(d)]
   for r in range(1,33):
    hit=sum(dist[i]*P[i][u] for i in range(d))
    assert hit<=F(d,r+1);C['first_hit_density']+=1
    dist=[sum(dist[i]*P[i][j] for i in range(d)) if j!=u else F(0) for j in range(d)]
  # Rational transform parameter xi has -log(xi)*Hbar<1/4, so all factor2 claims apply.
  xi=1-F(1,8)/hb;idx=[i for i in range(d) if i!=u]
  A=[[F(i==j)-xi*P[i][j] for j in idx] for i in idx]
  hs=solve(A,[xi*P[i][u] for i in idx]);hh=[F(1)]*d
  for i,x in zip(idx,hs):hh[i]=x
  f=xi*sum(P[u][j]*hh[j] for j in range(d))
  assert f>=F(3,4) and min(hh)>=F(3,4)
  Q=[[xi*P[i][j]*hh[j]/(f if i==u else hh[i]) for j in range(d)] for i in range(d)]
  assert all(sum(row)==1 for row in Q)
  pq,Hq,hbq,_,_=target(Q,u)
  assert pq<=2*p and Hq<=2*H and hbq<=2*hb;C['tilted_chain_exact']+=1
  if z<3:
   for start in range(d):
    for tail in product(range(d),repeat=4):
     path=(start,)+tail
     if path[-1]!=u:continue
     pp=qq=F(1)
     for i,j in zip(path,path[1:]):pp*=P[i][j];qq*=Q[i][j]
     J=sum(v==u for v in path[:-1])
     assert qq==pp*xi**4*f**(-J)/hh[start];C['tilted_path_identity']+=1
  if z<4:
   for l in (8,16,32,64):
    for start in range(d):
     actual=occupation(P,start,u,l)
     rhs=16*d*float(p)*(1+float(hb)/l)*math.exp(-l/(2*float(hb)))
     assert float(actual)<=rhs+1e-13;C['joint_tail_float']+=1
for b in (F(1,17),F(1,3),F(1,2),F(1)):
 for t in (F(1,19),F(1,4),F(2,3),F(1)):
  RR=[[F(0),1-b,b],[F(1),F(0),F(0)],[F(0),t,1-t]]
  pa,Ha,hba,_,_=target(RR,0);pc,Hc,hbc,_,_=target(RR,2)
  assert Ha==1+1/t and Hc==2/b
  assert pa*b*hba<=1 and pc*t*hbc<=1;C['reflection_hitting_scale']+=1
  for e in (F(1,11),F(1,2),F(1)):
   P=[[F(1),F(0),F(0),F(0)],[F(0),F(0),1-b,b],[e,1-e,F(0),F(0)],[F(0),F(0),t,1-t]]
   Pw=powers(P,33)
   for M in range(1,33):
    for i in (1,2,3):
     kill=e*Pw[M][i][2]
     assert kill==Pw[M+1][i][0]-Pw[M][i][0] and kill<=F(4,M+2);C['killing_edge_density']+=1
for M in range(64,10000):
 n=M//2
 assert n>=F(M,3)
 assert 288*4*40==46080<2**16
 assert 288*3*2+4==1732<2048
 assert 2**16+2**16==2**17;C['scalar_assembly']+=1
p=D/'CB005_all_start_critical_adaptation.md'
out={'status':'PASS_TESTED_INSTANCES_ONLY','counts':C,'arithmetic':'Exact Fraction/integer for algebra, kernels, transforms, paths, reflection and constants; joint_tail_float explicitly uses floating exp for tested tail inequalities only. Rational tilt xi is chosen within the proof lambda-domain, not falsely labeled exact exp(-1/(4Hbar)).','proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Finite author diagnostics; universal all-start theorem needs fresh full independent review. No mixing assertion.'}
(D/'CB005_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
