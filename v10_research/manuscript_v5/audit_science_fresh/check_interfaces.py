from fractions import Fraction as F
from pathlib import Path
import hashlib,json,itertools,math
out=Path(__file__).parent
counts={}
def ck(name,v):
 assert v,name
 counts[name]=counts.get(name,0)+1
def T(x):return 2*min(x,1-x)
def Te(x):return 2*x-4*max(0,x-F(1,2))+4*max(0,x-1)
def iterate(x,k):
 for _ in range(k):x=T(x)
 return x
def clip(x):return max(F(0),min(F(1),x))
def curve(t,N,j,nopause):
 if j==1:return (t,)
 k=N.bit_length()-1; L=N**(j-1); eta=F(1,2*L+2)
 A=iterate(t,k+1); B=iterate(Te(t+F(1,4*N)),k)
 s=A/2+min(1-A,L*max(0,F(1,2)-B)); S=t-s/N
 if nopause:u=clip((iterate(Te(t+eta/(2*N)),k-1)-eta/2)/(1-eta))
 else:
  v=iterate(t,k);u=clip(v+v/L-F(1,2*L))
 return curve(u,N,j-1,nopause)+(S,)
def edges(N,j,nopause):
 if j==1:return [(F(0),F(1),(F(0),),(F(1),))]
 child=edges(N,j-1,nopause);eta=F(1,2*N**(j-1)+2);res=[]
 for i in range(N):
  rows=child if i%2==0 else list(reversed(child))
  for a,b,x,y in rows:
   if i%2:a,b,x,y=1-b,1-a,y,x
   offset=0 if nopause else eta
   scale=1-eta if nopause else 1-2*eta
   res.append(((i+offset+scale*a)/N,(i+offset+scale*b)/N,x+(F(i,N),),y+(F(i,N),)))
  anchor=rows[-1][3] if i%2==0 else rows[-1][2]
  res.append((F(i+1,N)-eta/N,F(i+1,N),anchor+(F(i,N),),anchor+(F(i+1,N),)))
 return res
for j,N in [(2,2),(2,4),(2,8),(3,2),(3,4),(4,2)]:
 for no in [False,True]:
  es=edges(N,j,no)
  for a,b,x,y in es:
   for f in [F(0),F(1,7),F(1,2),F(6,7),F(1)]:
    t=a+(b-a)*f;pt=tuple(xx+(yy-xx)*f for xx,yy in zip(x,y))
    ck('curve_table_exact',curve(t,N,j,no)==pt)
   if no:ck('no_pause_positive_speed',sum((yy-xx)**2 for xx,yy in zip(x,y))>=(N**(j-1)*(b-a))**2)
  for e,f in zip(es,es[1:]):
   ck('path_continuity',e[3]==f[2])
   if no:ck('no_pause_tiling',e[1]==f[0])
  for i,e in enumerate(es):
   for f in es[i+2:]:
    dist=sum(max(F(0),max(min(a,b),min(c,d))-min(max(a,b),max(c,d)))**2 for a,b,c,d in zip(e[2],e[3],f[2],f[3]))
    ck('nonincident_separation',dist>=F(1,N*N))
  # nearest-edge rational projection, adversarial corners and endpoint samples
  Q=64*N
  for a,b,x,y in es[::max(1,len(es)//12)]:
   for lam in [F(0),F(1,2),F(1)]:
    t=a+(b-a)*lam;pt=curve(t,N,j,no)
    for signs in itertools.product([-1,1],repeat=j):
     # 1/Q finite tube plus 1/(3Q) attack, then Q floor
     q=tuple(F(math.floor(Q*clip(z+F(4*s,3*Q))),Q) for z,s in zip(pt,signs))
     options=[]
     for aa,bb,xx,yy in es:
      ax=next(k for k in range(j) if xx[k]!=yy[k]);v=max(min(xx[ax],yy[ax]),min(max(xx[ax],yy[ax]),q[ax]));w=list(xx);w[ax]=v
      dist=sum((u-vv)**2 for u,vv in zip(q,w));tt=aa+(bb-aa)*(v-xx[ax])/(yy[ax]-xx[ax]);options.append((dist,tt))
     tt=min(options,key=lambda z:z[0])[1]
     # squared bound with plateau allowance, c+finite+floor <=7/3
     excess=max(F(0),abs(tt-t)-(0 if no else F(j-1,N**j)))
     ck('adversarial_decode',excess**2<=F(8*j*49,9*Q*Q*N**(2*j-2)))
# Partial folding decoder independent closed-cell intersection
for h in range(1,5):
 Q=2**h
 for J in range(2,5):
  for r in range((J-1)*h+1):
   times=[0] if r==0 else list(range(0,r,h))+[r]
   for den in [2**(h+r),2**(h+r)+1]:
    for num in sorted(set([0,1,den//4,den//2,den-1,den])):
     x=F(num,den);ys=[iterate(x,t) for t in times];ks=[math.floor(Q*y) for y in ys];lo,hi=F(0),F(1);a,b=1,0
     for idx,k in enumerate(ks):
      if k==Q:lo=hi=(1-b)/a;break
      ends=sorted([(F(k,Q)-b)/a,(F(k+1,Q)-b)/a]);lo=max(lo,ends[0]);hi=min(hi,ends[1])
      if lo==hi:break
      if idx+1<len(times):
       e=times[idx+1]-times[idx];v=k//2**(h-e)
       a,b=(2**e*a,2**e*b-v) if v%2==0 else (-2**e*a,v+1-2**e*b)
     ck('partial_fold_endpoints',lo<=x<=hi and hi-lo<=F(1,Q*2**r))
# symmetric compander inverse bound: exact sqrt(x) using x=squared rational

def g(x,L):
 u=x;v=F(0)
 for j in range(L):v,u=v+F(1,2**j)*max(0,u-F(1,4)),min(1,4*u)
 return v+F(1,2**L)*u
for L in range(8):
 for i in range(33):
  x=F(i,32)**2
  for y in [F(0),F(1),x]+[F(n,64) for n in range(65)]:
   ep=abs(g(y,L)-g(x,L));ck('symmetric_inverse_leakage',abs(y-x)<=4*F(i,32)*ep+4*ep**2+2*ep/2**L)
# common real coarse attack and finite noise certificate
for h in range(1,10):
 Q=2**h
 for delta in [F(0),F(1,4),F(1,7),F(1,31),F(1,Q),F(1,3*Q)]:
  tau=max(F(1,Q),delta);m=1
  while F(1,2**(m+1))>=tau:m+=1
  ck('finite_scale_certificate',1<=m<=h and tau<=F(1,2**m)<2*tau)
  if delta:
   for i in range(65):
    a=F(i,64);k=math.floor(a/delta);att=delta*k
    ck('common_attack_oracle',0<=a-att<delta and math.floor(Q*att)==math.floor(Q*delta*k))
result={'status':'PASS','checks':counts,'total':sum(counts.values()),'scope':'Fresh independent exact rational finite checks; not universal proofs or emitted-evaluator verification.'}
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
