"""Exact finite diagnostics, not proof or independent review."""
from fractions import Fraction as F
import random,json,hashlib,pathlib
rng=random.Random(41212)
counts={"gate_real_pseudocount_cases":0,"floor_and_coarsening_cases":0,"source_edits":0}
for _ in range(20000):
 J=rng.randrange(1000); J1=rng.randrange(J+1); C=rng.randrange(J+1); q=F(rng.randrange(1001),1000)
 # Independently perturbed counts, projected only to individual legality.
 Jp=max(F(0),F(J)+F(rng.randrange(-30,31),rng.randrange(1,100)))
 Cp=min(Jp,max(F(0),F(C)+F(rng.randrange(-30,31),rng.randrange(1,100))))
 Lp=max(F(0),F(J1)+F(rng.randrange(-30,31),rng.randrange(1,100)))
 d=max(abs(Jp-J),abs(Cp-C),abs(Lp-J1)); G=Jp>0 and 512*Lp>=Jp; H=1024*J1>=J; B=J>0 and 256*J1<J
 E=abs(F(C,J)-q) if J else F(0); out=Cp/Jp if G else F(0)
 rhs=E+8*d/(J+1)*H+q*B+(J<1026*d+1)+(J<513*d+1)
 assert abs(out-q)<=rhs
 if G and not H: assert J<1026*d
 if not G and not B and J>0: assert J<=513*d
 if G and H and J>0: assert abs(out-q)<=E+8*d/(J+1)
 counts['gate_real_pseudocount_cases']+=1
for M in range(64,72):
 for h in range(4,8):
  Q=2**h
  for P in range(h,h+3):
   D=2**P
   for A in range(M+1):
    a=F((D*A)//M,D)
    assert (Q*a)//1==(Q*A)//M
    for hc in range(4,h+1):
     Qc=2**hc; c=F((Qc*a)//1,Qc); b=F((Q*a)//1,Q)
     assert c==F((Qc*A)//M,Qc)
     assert 0<=a+c-b<=1
     assert F((Q*(a+c-b))//1,Q)==c
     counts['floor_and_coarsening_cases']+=1
for _ in range(500):
 M=rng.randrange(64,150); n=M//2; x=[rng.randrange(2) for _ in range(M+2)]; y=x[:]
 k=rng.randrange(M+1)
 for i in rng.sample(range(M),k): y[i]^=1
 def bank(x):
  t=[0]*8;l=[0]*4
  for j in range(M):
   u=2*x[j]+x[j+1];t[2*u+x[j+2]]+=1
   if j<n:l[u]+=1
  return t,l
 a,b=bank(x);c,d=bank(y)
 assert sum(abs(i-j) for i,j in zip(a,c))<=6*k
 assert max(abs(i-j) for i,j in zip(b,d))<=2*k
 assert x[-2:]==y[-2:]
 counts['source_edits']+=1
assert 1072176*6==6433056<2**23
assert F(23,2)<12
result={'status':'PASS','scope':'author exact diagnostics, not independent review or formal verification','counts':counts}
path=pathlib.Path(__file__).with_suffix('.json');path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
