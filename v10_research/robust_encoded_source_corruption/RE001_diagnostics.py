#!/usr/bin/env python3
"""RE001 finite diagnostics. Exact arithmetic checks, not a proof/full network audit.

Terminal arithmetic slice uses the accepted common-weight pool cancellation,
then actual signed finite affine operations in the compander/snake. It does not
emit or audit every dense attention/mask slot in the symbolic resource ledger.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import isqrt
import hashlib,json,random,sys,time
D=Path(__file__).resolve().parent;ROOT=D.parent
sys.path.insert(0,str(ROOT/'robust_depth_capacity'))
from check_gn001_finite import Finite,nearest
from GN001_independent_geometry import curve,edges

def clip(x,lo=F(0),hi=F(1)):return min(hi,max(lo,x))
def comp(x,L):
 u=x;v=F(0)
 for j in range(L):
  old=u;u=min(F(1),4*old);v+=F(1,2**j)*max(F(0),old-F(1,4))
 return v+F(1,2**L)*u

def inv(z,L):
 pts=sorted({F(0),F(1),*(F(1,4**j) for j in range(L+1))})
 for a,b in zip(pts,pts[1:]):
  ga,gb=comp(a,L),comp(b,L)
  if ga<=z<=gb:return a+(z-ga)*(b-a)/(gb-ga)
 raise AssertionError((z,L))

def finite_prebank(freq,L,N,R,P):
 f=Finite(P);u=f.rho(freq);v=F(0)
 for j in range(L):
  old=u
  rel=f.rel(f.aff(-F(1,4),(1,old)))
  v=f.aff(0,(1,v),(F(1,2**j),rel))
  u=f.minimum(F(1),f.aff(0,(4,old)))
 t=f.aff(0,(F(1,2),v),(F(1,2**(L+1)),u))
 raw=f.run(t,N,R) if N>1 else (t,)+(F(0),)*(R-1)
 # Exact PRE-FAULT working-lattice clip via actual signed affine differences.
 bank=tuple(f.aff(0,(1,f.rel(z)),(-1,f.rel(f.aff(-1,(1,z))))) for z in raw)
 ideal=curve(comp(freq,L)/2,N,R) if N>1 else (comp(freq,L)/2,)+(F(0),)*(R-1)
 return bank,ideal,f.ops

def histogram(word,K):
 h=[0]*(K**3)
 for a,b,c in zip(word,word[1:],word[2:]):h[(a*K+b)*K+c]+=1
 return h

def upper_root(z,eps):
 p=0
 while F(1,1<<p)>eps:p+=1
 a=z.numerator*(1<<(2*p));b=z.denominator;j=isqrt(a//b)
 if j*j*b<a:j+=1
 S=F(j,1<<p)
 assert S*S>=z and (j==0 or F(j-1,1<<p)**2<z)
 return S

def assert_sqrt_bound(value,constant,coef,r):
 # value <= constant+coef*sqrt(r), exactly with nonnegative quantities.
 assert constant>=0 and coef>=0 and r>=0
 if value>constant:assert (value-constant)**2<=coef**2*r,(value,constant,coef,r)

start=time.time();histchecks=0
for K,M in [(2,5),(3,3)]:
 for word in product(range(K),repeat=M+2):
  a=histogram(word,K)
  for prefix in product(range(K),repeat=M):
   edited=prefix+word[-2:];k=sum(x!=y for x,y in zip(word,edited));b=histogram(edited,K)
   assert sum(abs(x-y) for x,y in zip(a,b))<=6*k
   base=(word[-2]*K+word[-1])*K
   assert sum(a[base:base+K])==sum(word[j:j+2]==word[-2:] for j in range(M))
   histchecks+=1

# Fixed small prototypes: actual finite composed arithmetic and legal geometric noise.
rng=random.Random(202611021147);finite_checks=0;noise_checks=0;rowchecks=0;emptyfalse=0
max_ops=0;max_precut=F(0);prototype_reports=[]
for R,N,Q,L in [(2,2,512,0),(2,4,1024,3),(3,2,1024,6),(2,1,64,3)]:
 h=Q.bit_length()-1;P=384;delta=F(1,Q);rho=delta;u=rho+F(2,Q)
 eps=F(8*R)*u/N**(R-1) if N>1 else 2*u
 assert N==1 or 4*R*u*N<=1
 es=edges(N,R) if N>1 else None
 cache={}
 def encode_scalar(freq,signs):
  global finite_checks,noise_checks,max_ops,max_precut
  if freq not in cache:
   actual,ideal,ops=finite_prebank(freq,L,N,R,P)
   assert all(0<=v<=1 and (v*(1<<P)).denominator==1 for v in actual)
   err=max(abs(a-b) for a,b in zip(actual,ideal));assert err<=F(1,Q)
   max_precut=max(max_precut,err);max_ops=max(max_ops,ops);finite_checks+=1
   cache[freq]=(actual,ideal)
  actual,ideal=cache[freq]
  received=tuple(F((Q*clip(a+sg*delta)).__floor__(),Q) for a,sg in zip(actual,signs))
  assert all(abs(a-b)<=u for a,b in zip(received,ideal))
  th=nearest(received,es) if N>1 else received[0]
  z=clip(2*th,F(0),comp(F(1),L));y=inv(z,L)
  assert abs(z-comp(freq,L))<=eps
  assert_sqrt_bound(abs(y-freq),4*eps*eps+2*eps/(2**L),4*eps,freq)
  noise_checks+=1
  return received,y
 # Every noise corner per frequency includes endpoints and compander breakpoints.
 frequencies={F(i,64) for i in range(65)}|{F(1,4**j) for j in range(L+1)}
 for freq in frequencies:
  for signs in product([-1,0,1],repeat=R):encode_scalar(freq,signs)
 for K in [2,3]:
  for it in range(24):
   M=[64,65,127][it%3]
   if it==0:word=(0,)*M+(1,1)
   elif it==1:word=(0,)*(M+2)
   else:word=tuple(rng.randrange(K) for _ in range(M+2))
   k=[0,1,2,M//4,M][it%5];edited=list(word)
   for pos in rng.sample(range(M),k):edited[pos]=(edited[pos]+rng.randrange(1,K))%K
   edited=tuple(edited)
   # Encoder input is only edited word. Clean word enters tests AFTER cut creation.
   edited_counts=histogram(edited,K);S=edited[-2:];received=[];decoded=[]
   for value in edited_counts:
    signs=tuple(rng.choice([-1,0,1]) for _ in range(R))
    label,y=encode_scalar(F(value,M),signs);received.append(label);decoded.append(y)
   # Post-cut usable tuple: (received labels, exact S, public parameters).
   # Independently recompute every decoder result from ONLY that tuple.
   checkdecoded=[]
   for label in received:
    th=nearest(label,es) if N>1 else label[0]
    checkdecoded.append(inv(clip(2*th,F(0),comp(F(1),L)),L))
   assert decoded==checkdecoded
   clean=histogram(word,K);base=(S[0]*K+S[1])*K
   xs=[F(v,M) for v in clean[base:base+K]];ys=decoded[base:base+K]
   r=sum(xs);rhat=sum(ys);de=sum(abs(a-b) for a,b in zip(xs,ys))
   eta=F(k,M);tau=eta+eps*eps+eps/(2**L)
   constant=12*eta+8*K*eps*eps+2*K*eps/(2**L)
   # Exact comparison without irrational sqrt(Kr).
   assert_sqrt_bound(de,constant,4*eps,F(K)*r)
   pred=[(y+F(1,M))/(rhat+F(K,M)) for y in ys]
   cleanpred=[(x+F(1,M))/(r+F(K,M)) for x in xs]
   assert sum(pred)==1 and min(pred)>=0
   tv=sum(abs(a-b) for a,b in zip(pred,cleanpred))/2
   assert tv<=de/(r+F(K,M))
   if r==0 and rhat>0:emptyfalse+=1
   if K==2:
    Sroot=upper_root(rhat,eps);Bhat=12*eps*Sroot+68*tau
    assert de<=Bhat
    assert_sqrt_bound(Bhat,132*tau,18*eps,r)
    d=1-S[0];J=sum(clean[base:base+2]);C=clean[base+d]
    B=M*Bhat;qh=max(F(0),M*ys[d]-B)/(M*rhat+B+2)
    assert 0<=qh<=F(C,J+2)
    p=F(C,J) if J else F(0)
    for q in [F(0),F(1,10),F(1,2),F(1)]:
     empirical=abs(p-q) if J else F(0)
     assert abs(qh-q)<=2*empirical+min(q,(4*B+2)/(J+2))
   rowchecks+=1
 prototype_reports.append(dict(R=R,N=N,Q=Q,L=L,P_diagnostic=P,unique_frequencies=len(cache),epsilon=str(eps)))

# Exact public-scale selection, finite M including large values; no real oracle.
schedulechecks=0;scalar=0;packed=0
for R in range(2,6):
 for M in [64,65,127,256,1023]+[2**j+r for j in range(12,81,4) for r in [-1,0,1]]:
  j=(M.bit_length()-1)//2;t0=F(1,1<<j)
  assert t0*t0*M>=1 and t0*t0*M<4
  m=(M+1).bit_length();L=(m-1).bit_length();chi=1<<L
  assert m<=chi<2*m
  for h in range(1,31):
   Q=1<<h
   for rho in [F(0),F(1,Q),F(1,64),F(3,2*Q)]:
    u=rho+F(2,Q)
    if u<=t0:
     assert 2*u<=2*t0;scalar+=1
    elif u**R<=t0/(8*R)**(R-1):
     N=2
     while t0*N**(R-1)<u:N*=2
     assert N==2 or t0*(N//2)**(R-1)<u
     assert 4*R*u*N<=1
     assert F(8*R)*u/N**(R-1)<=8*R*t0
     packed+=1
    else:continue
    schedulechecks+=1

# Explicit pre-fault clip tests outside the cube, beyond naturally reached examples.
clipchecks=0
for P in [0,1,7,19]:
 f=Finite(P)
 for z in [F(-3),F(-1,1<<P),F(0),F(1,1<<P),F(1),F(1)+F(1,1<<P),F(4)]:
  actual=f.aff(0,(1,f.rel(z)),(-1,f.rel(f.aff(-1,(1,z)))))
  assert actual==clip(z) and 0<=actual<=1
  for target in [F(0),F(1,3),F(1)]:assert abs(actual-target)<=abs(z-target)
  clipchecks+=1

files=[D/'RE001_theorem.md',Path(__file__),ROOT/'robust_depth_capacity/check_gn001_finite.py',ROOT/'robust_depth_capacity/GN001_independent_geometry.py']
out=dict(status='PASS',scope='Exact finite diagnostics, not formal verification, statistical expectation Monte Carlo, or a full emitted-network/resource audit.',histogram_edit_pairs=histchecks,actual_finite_composed_frequency_evaluations=finite_checks,noisy_geometric_reconstructions=noise_checks,actual_corrupted_word_pipeline_rows=rowchecks,empty_clean_rows_with_false_reconstructed_mass=emptyfalse,max_actual_affine_count=max_ops,precut_error_strictly_below_grid=True,prototype_settings=prototype_reports,finite_scale_certificate_cases=schedulechecks,scalar_schedules=scalar,packed_schedules=packed,explicit_pre_fault_clip_cases=clipchecks,all_radical_inequalities_checked_by_exact_squaring=True,elapsed_seconds=time.time()-start,sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
(D/'RE001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
