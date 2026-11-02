"""Exact finite diagnostics for MG001; not an all-parameter proof/network audit."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, hashlib
D=Path(__file__).parent

def comp(x,L):
 u=x;v=F(0)
 for j in range(L):
  v+=F(1,2**j)*max(0,u-F(1,4));u=min(1,4*u)
 return v+F(u,2**L)

def inv(z,L):
 bs=sorted({F(0),F(1),*(F(1,4**j) for j in range(L+1))})
 for a,b in zip(bs,bs[1:]):
  ga,gb=comp(a,L),comp(b,L)
  if ga<=z<=gb:return a+(z-ga)*(b-a)/(gb-ga)
 raise AssertionError((z,L))

def clip(x,lo=F(0),hi=F(1)):return min(hi,max(lo,x))
def tent(x):return 2*x-4*max(0,x-F(1,2))
def fold(x,k):
 for _ in range(k):x=tent(x)
 return x

def curve(t,R,N):
 if R==1:return (t,)
 k=N.bit_length()-1;ell=N**(R-1);v=fold(t,k);A=fold(t,k+1)
 b=t+F(1,4*N);B=fold(2*b-4*max(0,b-F(1,2))+4*max(0,b-1),k)
 z=min(1-A,ell*max(0,F(1,2)-B));s=A/2+z
 return curve(clip(v+v/ell-F(1,2*ell)),R-1,N)+(t-s/N,)

def segments(R,N):
 if R==1:return [(F(0),F(1),(F(0),),(F(1),))]
 child=segments(R-1,N);eta=F(1,2*N**(R-1)+2);out=[]
 for i in range(N):
  for a,b,x,y in (child if i%2==0 else reversed(child)):
   if i%2:a,b,x,y=1-b,1-a,y,x
   out.append(((i+eta+(1-2*eta)*a)/N,(i+eta+(1-2*eta)*b)/N,x+(F(i,N),),y+(F(i,N),)))
  end=out[-1][3]
  out.append((F(i+1,N)-eta/N,F(i+1,N),end,end[:-1]+(F(i+1,N),)))
 return out

def dec(q,es):
 best=None
 for a,b,x,y in es:
  j=next(j for j in range(len(q)) if x[j]!=y[j])
  f=clip((q[j]-x[j])/(y[j]-x[j]));z=tuple(xx+f*(yy-xx) for xx,yy in zip(x,y))
  d=sum((qq-zz)**2 for qq,zz in zip(q,z))
  if best is None or d<best[0]:best=d,a+f*(b-a)
 return best[1]

out={'status':'PASS','scope':'Exact finite rational diagnostics; not formal proof or emitted generic-FA network verification'}
ni=0
for L in range(7):
 for x in sorted({*(F(i,128) for i in range(129)),*(F(1,4**j) for j in range(L+1))}):
  assert inv(comp(x,L),L)==x
  for eps in [F(0),F(1,4096),F(1,64),F(1,4),F(1)]:
   for sign in [-1,0,1]:
    z=clip(comp(x,L)+sign*eps,F(0),comp(F(1),L));xh=inv(z,L)
    e=abs(xh-x);delta=4*eps**2+F(2,2**L)*eps
    # Equivalent exact check without evaluating sqrt(x).
    assert e<=delta or (e-delta)**2<=16*x*eps**2
    ni+=1
out['symmetric_inverse_cases']=ni
np=0
for R,N in [(2,2),(2,4),(3,2)]:
 Q=64*N;es=segments(R,N);c=F(1)
 for L in [0,2,5]:
  for x in [F(i,32) for i in range(33)]+[F(1,4**L)]:
   t=comp(x,L)/2;p=curve(t,R,N)
   for offsets in product([-2,0,2],repeat=R):
    # Combined finite +/-1/Q and adversarial +/-1/Q, then clip and floor.
    q=tuple(F((Q*clip(pp+F(off,Q))).__floor__(),Q) for pp,off in zip(p,offsets))
    th=dec(q,es);e=abs(th-t);plateau=F(R-1,N**R)
    # e <= 2sqrt(2R)(c+2)/(Q N^(R-1))+plateau, exact squared comparison.
    assert e<=plateau or (e-plateau)**2<=F(8*R*(c+2)**2,Q**2*N**(2*(R-1)))
    np+=1
out['robust_composed_curve_recovery_cases']=np
nr=0;zeros=0
for K in [2,3,4]:
 for M in [1,7,32]:
  for counts in product(range(4),repeat=K):
   if sum(counts)>M:continue
   xs=[F(v,M) for v in counts];r=sum(xs)
   for L,eps in [(0,F(1,64)),(3,F(1,128)),(6,F(1,1024))]:
    for signs in product([-1,1],repeat=K):
     xh=[inv(clip(comp(x,L)+s*eps,F(0),comp(F(1),L)),L) for x,s in zip(xs,signs)]
     a=r+F(K,M);b=sum(xh)+F(K,M)
     q=[(x+F(1,M))/a for x in xs];qh=[(x+F(1,M))/b for x in xh]
     assert sum(qh)==1 and min(qh)>=0
     tv=sum(abs(v-w) for v,w in zip(q,qh))/2;de=sum(abs(v-w) for v,w in zip(xs,xh))
     assert tv<=de/a
     delta=4*eps**2+F(2,2**L)*eps;rem=de-K*delta
     assert rem<=0 or rem**2<=16*eps**2*K*r
     if sum(counts)==0 and sum(xh)>0:zeros+=1
     nr+=1
out['add_one_row_cases']=nr;out['artificial_zero_row_mass_cases_handled']=zeros
nh=0
for M in range(1,9):
 for hist in product([0,1],repeat=M+2):
  bank={key:0 for key in product([0,1],repeat=3)}
  for j in range(M):bank[hist[j:j+3]]+=1
  S=hist[-2:];C=[bank[S+(b,)] for b in [0,1]]
  J=sum(hist[j:j+2]==S for j in range(M))
  assert sum(bank.values())==M and sum(C)==J
  assert C==[sum(hist[j:j+2]==S and hist[j+2]==b for j in range(M)) for b in [0,1]]
  nh+=1
out['actual_terminal_full_history_count_cases']=nh
# Nontrivial UC checks: all deterministic binary second-order maps, all starts.
nu=0
for table in product([0,1],repeat=4):
 for start in product([0,1],repeat=2):
  hist=list(start);vis=[0]*4
  for m in range(129):
   S=2*hist[-2]+hist[-1];J=vis[S]
   if m>=64:
    # A deterministic event of probability one must obey the UC bound.
    assert F(16*(J+1),m+1)>=1
    nu+=1
   vis[S]+=1;hist.append(table[S])
out['deterministic_arbitrary_start_nontrivial_occupation_cases']=nu
out['theorem_sha256']=hashlib.sha256((D/'MG001_theorem.md').read_bytes()).hexdigest()
(D/'MG001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
