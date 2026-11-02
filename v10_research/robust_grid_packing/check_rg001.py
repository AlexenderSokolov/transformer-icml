from fractions import Fraction as F
import json, hashlib
from pathlib import Path
D=Path(__file__).parent

def T(x):return 2*x-4*max(0,x-F(1,2))
def C(x):return min(F(1),max(F(0),x))
def fold(x,k):
 for _ in range(k):x=T(x)
 return x

def formula(t,j,N):
 if j==1:return (t,)
 k=N.bit_length()-1;L=N**(j-1)
 v=fold(t,k);A=fold(t,k+1);x=t+F(1,4*N)
 B=fold(2*x-4*max(0,x-F(1,2))+4*max(0,x-1),k)
 z=min(1-A,L*max(0,F(1,2)-B));s=A/2+z
 return formula(C(v+v/L-F(1,2*L)),j-1,N)+(t-s/N,)

def edges(j,N):
 if j==1:return [(F(0),F(1),(F(0),),(F(1),))]
 L=N**(j-1);eta=F(1,2*L+2);out=[];child=edges(j-1,N)
 for i in range(N):
  for a,b,x,y in (child if i%2==0 else list(reversed(child))):
   if i%2:a,b,x,y=1-b,1-a,y,x
   out.append(((i+eta+(1-2*eta)*a)/N,(i+eta+(1-2*eta)*b)/N,x+(F(i,N),),y+(F(i,N),)))
  end=child[-1][3] if i%2==0 else child[0][2]
  out.append((F(i+1,N)-eta/N,F(i+1,N),end+(F(i,N),),end+(F(i+1,N),)))
 return out

def dist2(e,f):
 x,y=e[2:];u,v=f[2:];s=F(0)
 for a,b,c,d in zip(x,y,u,v):
  lo,hi=sorted((a,b));ll,hh=sorted((c,d));gap=max(F(0),lo-hh,ll-hi);s+=gap*gap
 return s
results=[]
for j,N in [(2,2),(2,4),(3,2),(3,4),(4,2),(4,4)]:
 es=edges(j,N);minimum=None;maxplateau=F(0);vmin=None;vmax=F(0)
 last=F(0)
 for z,(a,b,x,y) in enumerate(es):
  assert a>=last
  maxplateau=max(maxplateau,a-last);last=b
  for r in [F(0),F(1,3),F(1,2),F(1)]:
   t=a+(b-a)*r;expected=tuple(xx+(yy-xx)*r for xx,yy in zip(x,y))
   assert formula(t,j,N)==expected,(j,N,z,t)
  speed=sum(abs(yy-xx) for xx,yy in zip(x,y))/(b-a)
  vmin=speed if vmin is None else min(vmin,speed);vmax=max(vmax,speed)
  for f in es[z+2:]:
   dd=dist2(es[z],f);minimum=dd if minimum is None else min(minimum,dd)
 assert maxplateau<=F(j-1,2*N**j)
 assert vmin>=N**(j-1)
 assert vmax<=3*2**(j-2)*N**(j-1)
 assert minimum>=F(1,N*N)
 # Dense arbitrary-parameter formula check includes every stationary region.
 for n in range(1025):
  t=F(n,1024);p=formula(t,j,N)
  found=False
  for a,b,x,y in es:
   if a<=t<=b:
    r=(t-a)/(b-a);assert p==tuple(xx+(yy-xx)*r for xx,yy in zip(x,y));found=True;break
  if not found:
   prev=[e for e in es if e[1]<t]
   p0=prev[-1][3] if prev else es[0][2]
   assert p==p0
 results.append(dict(J=j,N=N,edges=len(es),minimum_nonincident_squared=str(minimum),maximum_plateau=str(maxplateau),minimum_speed=str(vmin),maximum_speed=str(vmax)))
(D/'RG001_diagnostics.json').write_text(json.dumps({'status':'PASS finite exact rational checks; not all-parameter proof','cases':results},indent=2)+'\n')
print(json.dumps(results,indent=2))

# Uniform-P lattice audit at every arithmetic primitive (small exhaustive means).
lattice_cases=[]
for J,k in [(2,1),(3,1),(3,2),(4,1),(4,2),(5,1)]:
 N=2**k;h=k+4;b=(3*2**(J-2)-1).bit_length()+1;p0=J*h+b;G=(J-1)*(J-2)*k//2;P=p0+G;Dfine=2**P
 count=[0]
 def ck(x):
  x=F(x);assert (x*Dfine).denominator==1,(J,k,P,x);count[0]+=1;return x
 def tp(x):
  r=ck(max(0,ck(x-F(1,2))));return ck(2*x-4*r)
 def fp(x,n):
  for _ in range(n):x=tp(x)
  return x
 def exact(t,j):
  if j==1:return (t,)
  L=N**(j-1);v=fp(t,k);A=tp(v);x=ck(t+F(1,4*N))
  r1=ck(max(0,ck(x-F(1,2))));r2=ck(max(0,ck(x-1)));B=fp(ck(2*x-4*r1+4*r2),k)
  z=ck(max(0,ck(F(1,2)-B)))
  for _ in range((j-1)*k):z=ck(min(1,ck(2*z)))
  z=ck(min(ck(1-A),z));s=ck(ck(A/2)+z);S=ck(t-ck(s/N));u=ck(C(ck(ck(v+ck(v/L))-F(1,2*L))))
  return exact(u,j-1)+(S,)
 for m in [1,2,3,5,8,17,31]:
  for Acount in range(m+1):
   scaled=F(Acount,m*2**G);pooled=F((scaled*Dfine).__floor__(),Dfine);t=ck(pooled)
   for _ in range(G):t=ck(2*t)
   assert t==F((F(Acount,m)*2**p0).__floor__(),2**p0)
   assert exact(t,J)==formula(t,J,N)
 lattice_cases.append(dict(J=J,k=k,P=P,p0=p0,G=G,checked_values=count[0]))
r=json.loads((D/'RG001_diagnostics.json').read_text());r['uniform_precision_cases']=lattice_cases
(D/'RG001_diagnostics.json').write_text(json.dumps(r,indent=2)+'\n')
print('Uniform-P lattice checks PASS',lattice_cases)
