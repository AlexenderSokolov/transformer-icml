#!/usr/bin/env python3
"""Independent finite diagnostics, not a universal proof."""
import math, random, json
from fractions import Fraction
from pathlib import Path
rng=random.Random(202611020648)
checks=0
maxima={}
def verify(name,lhs,rhs,tol=2e-12):
 global checks
 checks+=1
 if lhs>rhs+tol*max(1,abs(rhs)): raise AssertionError((name,lhs,rhs))
 maxima[name]=max(maxima.get(name,0),lhs/rhs if rhs>0 else 0)
# Constants and all cutoffs, using exact arithmetic where possible.
assert 4+40+100+8192==8336
assert 2*8336==16672
assert 6*16672+64==100096<2**17
verify('statistical_constant',(2**14+4)*math.sqrt(32)+4+2,2**17)
verify('crossing_tail_max',8/math.e,3)
branches={k:0 for k in 'ABCD'}
for _ in range(30000):
 M=2**rng.uniform(6,45); beta=rng.choice([0,1,1/M**2,1/256,1/M,10**rng.uniform(-25,0)])
 Q=2**rng.randint(4,30); k=rng.randint(1,10000); z=k*Q
 e=max(math.sqrt(beta),1/M); t=M*e; s=1/math.sqrt(M)
 W=lambda z,t:(1+math.log1p(z/t))/z
 if beta>1/256:
  branches['A']+=1; verify('lower_branch_A',W(z,t),1/Q+2*s)
 elif z>M/4:
  branches['B']+=1; verify('lower_branch_B',W(z,t),5*s)
 elif z>M**.75:
  branches['C']+=1; verify('lower_branch_C',W(z,t),5*s)
 else:
  branches['D']+=1
  L=math.log1p(min(z/t,M/z)/8)/z
  verify('lower_branch_D',W(z,t),1/Q+24*L)
 a=math.sqrt(M); u=a/t; f=1+math.log1p(u)
 verify('threshold_sufficient',W(a*f,t),2/a)
 if beta*M*M>=1:
  A=6*M/z; G=1+math.log1p(1/(math.sqrt(beta)*A)); Gfinal=1+math.log1p(z/t)
  verify('precision_constant',(16672*A/M)*G+64/z,(2**17)*Gfinal/z)
  n=M*rng.uniform(.5,1)
  Gn=1+math.log1p(1/(max(math.sqrt(beta),1/n)*A))
  verify('short_suffix_log',Gn,G)
# Rational floor decoder tests include zero J, tiny bank and pure rows.
for _ in range(10000):
 M=rng.randint(64,5000); J=rng.randint(0,M); C=rng.randint(0,J)
 Q=2**rng.randint(4,12); k=rng.randint(1,10000); z=k*Q
 den=M+(k-1)*J
 n1=Q*k*C//den; n0=Q*k*(J-C)//den; N=n1+n0
 if N:
  p=Fraction(C,J); v=Fraction(n1,N); raw=Fraction(Q*k*J,den)
  assert abs(v-p)<=min(p,1-p)
  assert abs(v-p)<=min(1,2/raw)
  q=Fraction(rng.randint(0,1000),1000); A=Fraction(6*M,z)
  assert abs(v-q)<=min(q,A/(J+2))+Fraction(2,Q)+2*abs(p-q)
  checks+=3
 else:
  assert J<Fraction(4*M,z); checks+=1
# Exact finite-evaluator label bridge: common integer Taylor weight cancels.
for _ in range(10000):
 M=rng.randint(64,100000); C=rng.randint(0,M); h=rng.randint(4,40)
 Q=2**h; d=2**(4*(h+3)+rng.randint(0,30)); weight=rng.randint(1,10**20)
 O=(weight*d*C)//(M*weight)
 assert O//(d//Q)==(Q*C)//M
 assert (weight*d*0)//(M*weight)==0
 assert (weight*d*M)//(M*weight)==d
 checks+=3
# Full-support kernels: exact finite-horizon distribution/count dynamic programming.
def occupation(params,M,A,start):
 a,b,e,t=params
 P=[[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]]
 total=0.
 for target,q in enumerate(params):
  dp=[[0.]*(M+1) for _ in range(4)]; dp[start][0]=1.
  for j in range(M):
   nd=[[0.]*(M+1) for _ in range(4)]
   for i in range(4):
    for count,pr in enumerate(dp[i][:j+1]):
     if not pr: continue
     for dest,p in enumerate(P[i]):
      if p: nd[dest][count+(i==target)]+=pr*p
   dp=nd
  total+=sum(pr*min(q,A/(count+2)) for count,pr in enumerate(dp[target]))
 return total,P
for run in range(20):
 params=[rng.choice([.999,10**rng.uniform(-4,0),rng.random()]) for _ in range(4)]
 a,b,e,t=params; x=1/(e/a+2+b/t); pi=[x*e/a,x,x,x*b/t]
 M=rng.choice([64,80,128]); A=10**rng.uniform(-5,2)
 for start in range(4):
  val,P=occupation(params,M,A,start)
  P2=[[sum(P[i][k]*P[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
  beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4))
  G=1+math.log1p(1/(math.sqrt(beta)*A))
  verify('finite_weighted_occupation',val,4/math.sqrt(M)+16672*A*G/M)
  if start in (0,3): verify('finite_diagonal_occupation',val,8336*A*G/M)
result={'status':'PASS finite diagnostics only; not proof or root acceptance','seed':202611020648,'checks':checks,'branch_counts':branches,'max_observed_ratios':maxima}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
