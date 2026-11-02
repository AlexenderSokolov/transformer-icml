#!/usr/bin/env python3
"""Independent finite diagnostics, not proof; uses rational recursion for g."""
from fractions import Fraction as F
from math import sqrt, log, ceil
from pathlib import Path
import hashlib,json,random
ROOT=Path(__file__).resolve().parent
rng=random.Random(34117)
counts={k:0 for k in ('geometry','finite_purity','normalization','harmonic','late_matrix','precision_bootstrap')}

def g(x,L):
    if L==0:return x
    return g(min(F(1),4*x),L-1)/2+max(F(0),x-F(1,4))
def endpoints(L):return [F(0)]+[F(1,4**j) for j in range(L,0,-1)]+[F(1)]
def inv(z,L):
    bs=endpoints(L)
    for a,b in zip(bs,bs[1:]):
        ga,gb=g(a,L),g(b,L)
        if ga<=z<=gb:return a+(z-ga)*(b-a)/(gb-ga)
    raise AssertionError((z,L))
def finite(x,L,Q):
    D=16*2**L*Q; U=(D*x.numerator)//x.denominator;V=0
    for j in range(L):
        V+=max(0,U-D//4)//2**j;U=min(D,4*U)
    W=V+U//2**L
    Z=Q*W//(2*D)
    return F(W,D),inv(F(2*Z,Q),L)
for L in range(9):
    assert g(F(1),L)==F(3,2)-F(1,2**(L+1))
    bs=endpoints(L)
    slopes=[(g(b,L)-g(a,L))/(b-a) for a,b in zip(bs,bs[1:])]
    assert slopes==[2**L]+[2**j for j in range(L-1,-1,-1)]
    for _ in range(150):
        x=F(rng.randrange(10001),10000);y=x*F(rng.randrange(10001),10000)
        assert float(x-y)<= (2*sqrt(float(x))+2**(-L))*float(g(x,L)-g(y,L))+1e-14
        counts['geometry']+=1
    for Q in (16,32,128):
      for M in (1,3,7,16,37,100):
       for C in range(M+1):
        x=F(C,M);w,y=finite(x,L,Q)
        assert 0<=g(x,L)-w<=F(3,16*Q)
        assert 0<=y<=x
        assert float(x-y)<= (6*sqrt(float(x))+3/2**L)/Q+1e-14
        if C==0:assert w==y==0
        counts['finite_purity']+=1
for _ in range(3000):
    K=rng.choice((2,3,5));M=rng.randrange(1,300);L=rng.randrange(8);Q=2**rng.randrange(4,9)
    J=rng.randrange(M+1);cuts=sorted([0,J]+[rng.randrange(J+1) for i in range(K-1)])
    cs=[b-a for a,b in zip(cuts,cuts[1:])];xs=[F(c,M) for c in cs]
    ys=[finite(x,L,Q)[1] for x in xs];s=sum(ys)
    ps=[y/s for y in ys] if s else [F(1,K)]*K
    qs=[F(c+1,J+K) for c in cs]
    tv=sum(abs(p-q) for p,q in zip(ps,qs))/2
    bound=F(K,J+K)+6*sqrt(K*(K+1)*M/(J+K))/Q+min(1,3*K*(K+1)*M/(2**L*Q*(J+K)))
    assert float(tv)<=float(bound)+1e-12
    if J:
      tv0=sum(abs(p-F(c,J)) for p,c in zip(ps,cs))/2
      e=sum(xs)-s
      assert tv0<=min(1,e/F(J,M))
    counts['normalization']+=1
for M in (64,100,256,1024,4096,16384):
 for beta in (0,1/M,1/64,1/16):
  if beta>1/16:continue
  beta0=max(beta,1/M)
  for z in [1+ i*(M/4-1)/199 for i in range(200)]:
   J=int(min(1/(4*beta0),M*M/(4*z*z)))
   s=sum(1/(1+z*j/M) for j in range(2,J+1))
   rhs=M/(4*z)*log(1+(1/8)*min(z/(M*beta0),M/z))
   assert s+1e-9>=rhs
   counts['harmonic']+=1
# Direct triangular iteration, independently checking the late matrix envelope.
for T in (8,17,39):
 for a,b in ((0,1),(1,1),(2,3),(.1,.2)):
  for i in range(ceil(T/2),T):
   v=[0.]*(T+1);v[i]=1
   for L in range(1,9):
    pref=0;out=[0.]*(T+1)
    for t in range(1,T+1):
     pref+=v[t];out[t]=a*v[t]+b*pref/t
    v=out
    envelope=((a+b)**L-a**L)*(1+log(2))**(L-1)/T
    assert v[T]<=envelope+1e-8
    counts['late_matrix']+=1
for A in (2,3,8,31,1000):
 c=4
 while F(A*(c+5),2**(c-1))>1:c+=1
 for h in range(17):
  for d in range(40):
   t=d+2;P=4*h+c*t
   assert F(A**t*(P+1),2**P)<=F(1,2**h)
   counts['precision_bootstrap']+=1
sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'GD001_upper_derivation.md',ROOT/'GD001_lower_derivation.md',ROOT/'GD001_uniform_FA_extension.md']}
out={'status':'PASS','counts':counts,'source_sha256':sources,'limits':'Finite diagnostics supplement but do not replace proofs; uniform growing-depth FA recursion reviewed; diagnostics are not exhaustive architecture testing.'}
(ROOT/'GD001_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
