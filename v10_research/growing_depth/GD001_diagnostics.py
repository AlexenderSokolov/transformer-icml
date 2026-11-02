from fractions import Fraction as F
from math import sqrt
import random,json,hashlib,pathlib
root=pathlib.Path(__file__).parent
rng=random.Random(71443)
def g(x,L):
 u=x;v=F(0)
 for j in range(L):v+=max(F(0),u-F(1,4))/2**j;u=min(F(1),4*u)
 return v+u/2**L
def inv(z,L):
 ends=[F(0)]+[F(1,4**j) for j in range(L,0,-1)]+[F(1)]
 for a,b in zip(ends,ends[1:]):
  ga,gb=g(a,L),g(b,L)
  if ga<=z<=gb:return a+(z-ga)*(b-a)/(gb-ga)
 raise AssertionError((z,L))
def finite(x,L,Q):
 D=16*2**L*Q;U=x.numerator*D//x.denominator;V=0
 for j in range(L):V+=max(0,U-D//4)//2**j;U=min(D,4*U)
 W=V+U//2**L;Z=Q*W//(2*D)
 return inv(F(2*Z,Q),L),F(W,D),F(2*Z,Q)
counts={'coordinates':0,'blocks':0,'bootstrap':0}
worst=0
for L in range(13):
 for Q in [16,32,128,512]:
  xs=[F(0),F(1)]+[F(a,4**j) for j in range(1,16) for a in [1,2,3]]
  xs += [F(rng.randrange(100001),100000) for _ in range(150)]
  for x in xs:
   y,w,z=finite(x,L,Q);gx=g(x,L)
   assert 0<=y<=x and 0<=gx-w<=F(3,16*Q) and 0<=gx-z<F(3,Q)
   assert float(x-y)<= (6*sqrt(float(x))+3/2**L)/Q+1e-14
   if x==0:assert y==w==z==0
   counts['coordinates']+=1
for _ in range(3000):
 K=rng.randrange(2,9);M=rng.randrange(64,100001);L=rng.randrange(10);Q=2**rng.randrange(4,12)
 J=rng.randrange(M+1);cs=[0]*K
 for _ in range(J):cs[rng.randrange(K)]+=1
 ys=[finite(F(c,M),L,Q)[0] for c in cs];s=sum(ys)
 p=[y/s for y in ys] if s else [F(1,K)]*K
 if J:
  tv=sum(abs(p[i]-F(cs[i],J)) for i in range(K))/2
  bound=min(1,6*sqrt(K*M/J)/Q+3*K*M/(2**L*Q*J))
  assert float(tv)<=bound+1e-14
  worst=max(worst,float(tv)/bound)
 counts['blocks']+=1
for A in [2,3,10,100,10000]:
 c=4
 while A*(c+5)*F(2)**(1-c)>1:c+=1
 for d in range(1,101):
  for h in range(20):
   t=d+2;P=4*h+c*t
   assert A**t*(P+1)*F(2)**(-P+h)<=1
   counts['bootstrap']+=1
out={'status':'PASS','seed':71443,'counts':counts,'worst_normalization_to_bound':worst,'proof_scope':'finite checks only; not formal verification','source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in root.glob('*derivation.md')}}
(root/'GD001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
