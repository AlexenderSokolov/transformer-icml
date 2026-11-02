"""Finite scalar corroboration, not proof or neural execution."""
import math,json,hashlib,pathlib,random
root=pathlib.Path(__file__).parent
rng=random.Random(741)
checks=0
maxratio=0

def g(x,L):
 u=x;v=0.
 for j in range(L):
  v+=2.**(-j)*max(0,u-.25);u=min(1,4*u)
 return v+2.**(-L)*u

def inv(a,L):
 lo=0.;hi=1.
 for _ in range(64):
  m=(lo+hi)/2
  if g(m,L)<a:lo=m
  else:hi=m
 return (lo+hi)/2

def finite(x,L,Q):
 D=16*2**L*Q; U=int(x*D);V=0
 for j in range(L):
  V+=max(0,U-D//4)//2**j;U=min(D,4*U)
 W=V+U//2**L
 return Q*W//(2*D)
for L in range(13):
 gamma=2**L
 for k in range(2001):
  x=k/2000;u=min(gamma*x,math.sqrt(x));v=g(x,L)
  assert u-1e-12<=v<=1.5*u+1e-12
  checks+=1
 for Q in [16,32,64,256,1024]:
  for _ in range(200):
   r=rng.random();p=rng.random();xs=[r*p,r*(1-p)]
   Z=[finite(x,L,Q) for x in xs];ys=[inv(2*z/Q,L) if z else 0. for z in Z]
   for x,z,y in zip(xs,Z,ys):
    assert -1e-10<=g(x,L)-2*z/Q<3/Q+1e-10
    assert y<=x+1e-10
   if sum(Z):
    i=max(range(2),key=lambda i:xs[i]);assert Z[i]>=1
    assert xs[i]<=16*ys[i]+1e-10
    v=ys[0]/sum(ys)
    assert abs(v-p)<=32*p+1e-10
    A=6*math.sqrt(2)/(Q*math.sqrt(r));B=6/(gamma*Q*r)
    assert abs(v-p)<=A+B+1e-9
    maxratio=max(maxratio,xs[i]/ys[i])
   else:assert r<=6/(gamma*Q)+18/Q**2+1e-10
   checks+=1
for M in [64,65,128,1024,10**6]:
 for k in range(101):
  z=1+(M/4-1)*k/100
  for t in range(101):
   e=1/M+(1/16-1/M)*t/100
   J=math.floor(min(1/(4*e),M*M/(4*z*z)))
   if J<4:continue
   u=z/M
   lhs=sum(1/(1+u*j) for j in range(4,J+1))
   rhs=math.log1p(u*J)/(8*u)
   assert lhs>=rhs-1e-10
   checks+=1
out={'status':'PASS','finite_checks':checks,'max_observed_largest_x_over_y':maxratio,'scope':'Scalar compander, downward finite program, purity, zero-bank bound and harmonic inequalities; not proof or full encoder execution.'}
(root/'MD001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
