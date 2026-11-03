from fractions import Fraction as F
from pathlib import Path
import json
p=Path(__file__).with_name('reverse_moment_cases.jsonl')
def advance(P,M,V,T,g):
 P2=[F(0)]*4;M2=[F(0)]*4;V2=[F(0)]*4
 for i in range(4):
  for j in range(4):
   z=T[i][j];a=g(j)
   P2[j]+=z*P[i];M2[j]+=z*(M[i]+a*P[i]);V2[j]+=z*(V[i]+2*a*M[i]+a*a*P[i])
 return P2,M2,V2

def moments(T,m,kind):
 P=[F(1),F(0),F(0),F(0)];M=[F(0)]*4;V=[F(0)]*4
 # r counts Y_0..Y_(m-1), J counts Y_1..Y_m; Y_0=00 so initial r=0.
 g=(lambda j:F(j%2)) if kind=='r' else (lambda j:F(j==0))
 for _ in range(m-1 if kind=='r' else m):P,M,V=advance(P,M,V,T,g)
 assert sum(P)==1
 a=sum(M);return a,sum(V)-a*a
ct=0
with p.open('x') as f:
 for m in (512,768):
  for u in (F(1,8),F(3,16)):
   w=(1-u)/3
   for t in (F(1,4),F(3,4)):
    a=u*t/w;T=[[1-t,0,t,0],[a,0,1-a,0],[0,F(1,2),0,F(1,2)],[0,F(1,2),0,F(1,2)]]
    Ers,Vrs=moments(T,m,'r');Ej,Vj=moments(T,m,'J');Er=Ers/m;Vr=Vrs/(m*m);mu=2*w;v=m*u
    assert v>=60 and abs(Er-mu)<=F(16,m) and Vr<=F(61,m)
    assert abs(Ej-v)<=15 and Vj<=61*(v+15)
    f.write(json.dumps({'m':m,'u':str(u),'t':str(t),'mean_r':str(Er),'var_r':str(Vr),'mean_J':str(Ej),'var_J':str(Vj),'all_bounds':True})+'\n');ct+=1
print('PASS',ct,'exact rational reverse-chain moment cases; all records retained')
