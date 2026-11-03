from fractions import Fraction as F
from itertools import product

def spline(x,k,kind,m):
    if x == 1: j=k-1
    else: j=(x*k).numerator//(x*k).denominator
    a,b=F(j,k),F(j+1,k)
    f=lambda z: z*z if kind=='square' else 1/(1+F(m,2)*z)
    return f(a)+(f(b)-f(a))*(x-a)*k

def prod(x,y,k,m):
    return 2*(spline((x+y)/2,k,'square',m)-spline(x/2,k,'square',m)-spline(y/2,k,'square',m))
def clip(x,l,h): return max(F(l),min(F(h),x))
counts=[0,0,0]; worst=(F(-1),None)
for N in range(3,8):
 m=N-2
 for word in product((0,1),repeat=N):
  s=word[-2:]; hist=[(word[i-2:i],word[i]) for i in range(2,N)]
  J=sum(k==s for k,y in hist); C=sum(y for k,y in hist if k==s); C_all=sum(y for k,y in hist)
  q=F(C_all+C,m+J); r=F(C_all,m); h=F(J,m); A=F(C,m); B=F(C+1,J+2)
  assert (1+h)*q-r==A
  if J==0: assert B==F(1,2)
  counts[0]+=1; counts[1]+=(J==0)
  for K in [1,2,3,4]:
   for shifts in [(0,0,0)]+list(product((-1,0,1),repeat=3)):
    qp,rp,hp=[clip(x+F(d,10),0,1) for x,d in zip((q,r,h),shifts)]
    eq,er,eh=abs(qp-q),abs(rp-r),abs(hp-h)
    ac=clip(qp-rp+prod(hp,qp,K,m),0,hp)
    z=(m*ac+1)/F(m+2)
    hk=spline(hp,K,'reciprocal',m)
    out=clip(F(m+2,2)*prod(z,hk,K,m),0,1)
    first=F(m,1)/(2+m*max(h-eh,0))*((1+h)*eq+er+3*eh+F(3,2*K*K))
    second=F(m+2,2*K*K)*(F(3,2)+F(m*m,16))
    err=abs(out-B); bound=first+second
    assert err<=bound,(word,K,shifts,err,bound)
    if bound and err/bound>worst[0]: worst=(err/bound,(word,K,shifts,err,bound))
    counts[2]+=1
print('words',counts[0],'zero-count words',counts[1],'spline-and-perturbation checks',counts[2]); print('largest observed error/bound:',worst)
