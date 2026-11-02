"""Fresh reviewer diagnostics: exact arithmetic plus witness/tube algebra. Not proof."""
from fractions import Fraction as F
from pathlib import Path
import math,random,json,hashlib
random.seed(731901)
counts={k:0 for k in ['finite_pair','monotone','witness','active_atoms','harmonic_real_gamma','selection']}
def g(x,L):
 u=x;v=F(0)
 for j in range(L):
  v+=F(1,2**j)*max(F(0),u-F(1,4));u=min(F(1),4*u)
 return v+F(1,2**L)*u
def inv(v,L):
 pts=[F(0)]+[F(1,4**j) for j in range(L,0,-1)]+[F(1)]
 for a,b in zip(pts,pts[1:]):
  ga,gb=g(a,L),g(b,L)
  if ga<=v<=gb:return a+(v-ga)*(b-a)/(gb-ga)
 raise AssertionError((v,L))
def finite(x,L,h):
 P=max(h+L+4,4*h+4*(L+3));D=2**P;U=(x*D).__floor__();V=0
 for j in range(L):
  V+=max(0,U-D//4)//2**j;U=min(D,4*U)
 W=V+U//2**L
 # generic FA explicit /2 floor, followed by coarse cut
 return ((W//2)*2**h)//D
for L in range(8):
 for h in [4,5,8]:
  last=-1
  for i in range(257):
   x=F(i,256);Z=finite(x,L,h);assert Z>=last;last=Z
   assert 0<=g(x,L)-F(2*Z,2**h)<F(3,2**h)
   counts['monotone']+=1
  for _ in range(200):
   M=random.randint(64,4096);a=random.randint(0,M);b=random.randint(0,M-a)
   x0,x1=F(a,M),F(b,M);Q=2**h;gam=2**L
   Z0,Z1=finite(x0,L,h),finite(x1,L,h)
   y0,y1=inv(F(2*Z0,Q),L),inv(F(2*Z1,Q),L)
   if Z0+Z1:
    xm,ym=(x0,y0) if x0>=x1 else (x1,y1)
    assert ym>0 and xm<16*ym
    p=x1/(x0+x1);v=y1/(y0+y1);assert abs(v-p)<=32*p
   else:assert x0+x1 < F(6,gam*Q)+F(18,Q*Q)
   counts['finite_pair']+=1
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
for M in [64,65,127,256,1024,65536]:
 for e in [F(1,M),F(1,16),F(1,32),F(1,64)]:
  if e<F(1,M):continue
  for p in [F(i,32) for i in range(8,25)]:
   a=F(1,2*M);x=1/(e/a+2+2*p);pi=[x*e/a,x,x,2*p*x]
   P=[[1-a,a,0,0],[0,0,1-p,p],[e,1-e,0,0],[0,0,F(1,2),F(1,2)]]
   assert mm([pi],P)[0]==pi
   P2=mm(P,P)
   assert min(P2[i][j]-e*e*pi[j] for i in range(4) for j in range(4))>=0
   assert pi[0]>=F(1,4)
   counts['witness']+=1
   R=[[0,1-p,p],[1,0,0],[0,F(1,2),F(1,2)]];R2=mm(R,R);R3=mm(R2,R)
   assert min(row[1] for row in R2)>=F(1,8)
   assert min(row[0] for row in R3)>=F(1,8)
   counts['active_atoms']+=1
for _ in range(10000):
 M=10**random.uniform(math.log10(64),9);Q=2**random.uniform(0,math.log2(M/4));gam=10**random.uniform(0,max(0,math.log10(M/(4*Q))));z=gam*Q
 e=10**random.uniform(-math.log10(M),math.log10(1/16));U=min(1/(4*e),M*M/(4*z*z));J=math.floor(U+1e-12);u=z/M
 if J>100000:continue
 assert J>=4
 sm=sum(1/(1+u*j) for j in range(4,J+1))
 assert sm+1e-10>=math.log1p(u*J)/(8*u)
 assert u*J+1e-10>=min(z/(M*e),M/z)/8
 counts['harmonic_real_gamma']+=1
for _ in range(10000):
 x=10**random.uniform(-100,100);f=1+math.log1p(x);gam=2**math.ceil(math.log2(f))
 assert f<=gam<2*f+1e-12
 assert (1+math.log1p(gam*x))/gam<=2+1e-12
 counts['selection']+=1
base=Path(__file__).parent
proofs=['MD001_upper.md','MD001_binary_lower.md','MD001_theorem.md']
out={'status':'PASS','counts':counts,'total':sum(counts.values()),'source_sha256':{p:hashlib.sha256((base/p).read_bytes()).hexdigest() for p in proofs},'limitations':'Finite corroboration only; full mathematical and interface review is separate.'}
(base/'MD001_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
