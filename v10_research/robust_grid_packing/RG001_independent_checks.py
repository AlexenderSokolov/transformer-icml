from fractions import Fraction as F
from itertools import product
import json, hashlib
from pathlib import Path
D=Path(__file__).parent

def tent(t): return 2*t-4*max(F(0),t-F(1,2))
def iterate(t,k):
 for _ in range(k):t=tent(t)
 return t

def curve(t,j,k,track=None):
 if j==1:return (t,)
 N=2**k; L=N**(j-1)
 def rec(x):
  if track is not None:track.append(x)
  return x
 v=rec(iterate(t,k)); A=rec(iterate(t,k+1))
 x=rec(t+F(1,4*N)); b=rec(2*x-4*max(F(0),x-F(1,2))+4*max(F(0),x-1));B=rec(iterate(b,k))
 b=rec(max(F(0),F(1,2)-B))
 for _ in range((j-1)*k):b=rec(min(F(1),2*b))
 z=rec(min(1-A,b));s=rec(A/2+z);S=rec(t-s/N)
 u=rec(min(F(1),max(F(0),v+rec(v/L)-F(1,2*L))))
 return curve(u,j-1,k,track)+(S,)

def pieces(j,k):
 if j==1:return [(F(0),F(1),(F(0),),(F(1),))]
 N=2**k;L=N**(j-1);eta=F(1,2*L+2);child=pieces(j-1,k);out=[]
 for i in range(N):
  for lo,hi,x,y in (child if i%2==0 else reversed(child)):
   if i%2:lo,hi,x,y=1-hi,1-lo,y,x
   a=(i+eta+(1-2*eta)*lo)/N;b=(i+eta+(1-2*eta)*hi)/N
   out.append((a,b,x+(F(i,N),),y+(F(i,N),)))
  end=out[-1][3];out.append((F(i+1,N)-eta/N,F(i+1,N),end,end[:-1]+(F(i+1,N),)))
 return out

def dist2_edges(a,b):
 return sum(max(F(0),min(x,y)-max(u,v),min(u,v)-max(x,y))**2 for x,y,u,v in zip(a[2],a[3],b[2],b[3]))
checks=[]
for j,k in [(2,1),(2,2),(3,1),(3,2),(4,1)]:
 ps=pieces(j,k);N=2**k
 for a,b,x,y in ps:
  for f in [F(0),F(1,3),F(1,2),F(1)]:
   assert curve(a+(b-a)*f,j,k)==tuple(v+(w-v)*f for v,w in zip(x,y))
 for a,b in zip(ps,ps[1:]):
  assert a[3]==b[2] and a[1]<=b[0]
  assert b[0]-a[1]<=F(j-1,2*N**j)
  assert curve((a[1]+b[0])/2,j,k)==a[3]
 assert ps[0][0]<=F(j-1,2*N**j)
 for ia,a in enumerate(ps):
  for b in ps[ia+2:]:assert dist2_edges(a,b)>=F(1,N*N)
 for t in [F(i,257) for i in range(258)]:
  p=curve(t,j,k); assert all(0<=x<=1 for x in p)
 checks.append({'J':j,'k':k,'edges':len(ps),'piece_formula_and_separation':'PASS'})
# Test denominator budget on dyadic inputs and all recorded noninteger ops.
for j,k in [(2,1),(3,1),(3,2),(4,1),(5,1)]:
 e=j*(k+4)+j+2;G=(j-1)*(j-2)*k//2;P=e+G
 for i in range(0,257):
  t=F((2**e*i)//256,2**e);tr=[];curve(t,j,k,tr)
  assert all((x*2**P).denominator==1 for x in tr)
 checks.append({'J':j,'k':k,'P':P,'uniform_grid_recorded_ops':'PASS'})
res={'status':'PASS','scope':'Exact rational finite diagnostics, not proof or emitted-network audit','checks':checks,'theorem_sha256':hashlib.sha256((D/'RG001_theorem.md').read_bytes()).hexdigest()}
(D/'RG001_independent_checks.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
