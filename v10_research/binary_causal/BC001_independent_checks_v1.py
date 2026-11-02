from fractions import Fraction as F
from pathlib import Path
import json, hashlib, math, itertools
BASE=Path(__file__).resolve().parents[1]
checks={}
def matmul(A,B):
 return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
count=0
for p in [F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)]:
 R=[[0,1-p,p],[1,0,0],[0,F(1,2),F(1,2)]]
 R2=matmul(R,R);R3=matmul(R2,R)
 assert min(row[1] for row in R2)>=F(1,8)
 assert min(row[0] for row in R3)>=F(1,8)
 for M in [64,65,128,1000]:
  a=F(1,2*M)
  for e in [F(1,M),F(1,32),F(1,16)]:
   if e<F(1,M):continue
   beta=e*e
   x=1/(e/a+2+2*p);pi=[x*e/a,x,x,2*p*x]
   P=[[1-a,a,0,0],[0,0,1-p,p],[e,1-e,0,0],[0,0,F(1,2),F(1,2)]]
   assert matmul([pi],P)[0]==pi
   P2=matmul(P,P)
   assert all(P2[s][t]>=beta*pi[t] for s in range(4) for t in range(4))
   count+=1
checks['exact_stationarity_minorization_cases']=count
count=0
for h in [4,5,8,12]:
 for extra in [1,7,23]:
  P=4*(h+3)+extra;d=1<<P;Q=1<<h
  for shift in [1,2,5]:
   A=2*shift;J=8*A*A+2+P;term=d;W=term
   for j in range(1,J+1):
    term=term*(d*shift)//(j*d);W+=term
   assert W>=d and W!=d
   for M in [1,2,3,7,64,65,127,256,1001]:
    for c in range(M+1):
     fine=(W*d*c)//(M*W)
     got=fine//(d//Q)
     assert got==(Q*c)//M
     assert c!=0 or got==0
     assert c!=M or got==Q
     count+=1
checks['exact_taylor_normalization_nested_floor_cases']=count
count=0
for n in [67,68,131,1003]:
 for t in range(1,n+1):
  keys=list(range(1,t+1)) if t<=2 else list(range(3,min(t,n-1)+1))
  assert len(keys)*3>=t and all(i<=t for i in keys)
  count+=1
checks['dense_mask_rows']=count
# Small exhaustive histories inspect actual eight-coordinate bit construction and final labels.
count=0
for N in range(3,11):
 M=N-2;h=4;P=31;d=1<<P;Q=1<<h;W=987654321
 for bits in itertools.product([0,1],repeat=N):
  counts=[0]*8
  for i in range(2,N):
   triple=bits[i-2:i+1]
   vals=[max(0,sum(int(u==v) for u,v in zip(triple,abc))-2) for abc in itertools.product([0,1],repeat=3)]
   assert sum(vals)==1
   counts=[x+y for x,y in zip(counts,vals)]
  labels=[((W*d*c)//(M*W))//(d//Q) for c in counts]
  assert labels==[Q*c//M for c in counts]
  count+=1
checks['exhaustive_histories_bit_features_histogram_labels']=count
# Independent scalar domain grid; floating diagnostic only, unlike preceding exact tests.
count=0
for M in [64,65,128,1000,10**6,10**12]:
 for beta in [0,1/M**2,1/M,1/256,1/255,1]:
  e=max(math.sqrt(beta),1/M);t=M*e;s=M**-.5
  for h in range(4,50):
   Q=2**h;W=(1+math.log1p(Q/t))/Q
   if beta>1/256: assert W<=1/Q+2*s+1e-12
   elif Q>M/4 or Q>M**.75: assert W<=5*s+1e-12
   else:
    L=math.log1p(min(Q/t,M/Q)/8)/Q
    assert W<=1/Q+24*L+1e-12
   count+=1
checks['floating_all_regime_completion_cases']=count
receipt_checks=[]
for unit in ['CA001','FA001','CF001','BI001','BU001','BS001','SB001']:
 r=json.loads((BASE/'intake'/f'{unit}_acceptance.json').read_text())
 actual=hashlib.sha256((BASE/r['proof']).read_bytes()).hexdigest()
 assert actual==r['sha256']
 receipt_checks.append(unit)
checks['accepted_source_hashes_verified']=receipt_checks
checks['status']='PASS; finite diagnostics only, not universal proof'
Path(__file__).with_suffix('.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
