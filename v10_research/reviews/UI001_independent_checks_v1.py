#!/usr/bin/env python3
"""Independent UI001 audit. Exact rational finite checks, not a theorem proof."""
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
checks={}
# Exact conditional experiments; tiny m intentionally tests algebra, not .99 concentration.
records=[]
for n,r,m,kind in [(7,1,1,'ties'),(9,2,1,'huge'),(10,3,1,'huge'),(7,2,5,'all_selected')]:
 positions=list(range(2,n)); patterns=list(product([0,1],repeat=r))
 def window(i): return tuple(range(max(0,i-r+1),i+1))
 w={}; v={}
 for i in positions:
  scale=(2**80 if i==n//2 else 2**(i+2)) if kind=='huge' else 1
  for pat in patterns:
   k=sum(b<<j for j,b in enumerate(pat))
   w[i,pat]=1 if kind=='ties' else 1+scale*(k+1)
   v[i,pat]=F(((7*i+3*k)%9)-4,4)
 a={i:max(w[i,pat] for pat in patterns) for i in positions}
 selected=sorted(positions,key=lambda i:(-a[i],i))[:m]
 U=sorted(set(range(r))|set(range(n-r,n))|set(j for i in selected for j in window(i)))
 free=sorted(set(range(n))-set(U)); N=len(U)
 astar=max([a[i] for i in positions if i not in selected],default=0)
 q=F(1,4**r); archF=3**(2*r); L=r*archF+2*r; J=(2*r*L+1)/q; V=4*r*r*J/q
 assert m<=N<=L*m
 cases=heavy_cases=0; max_variance_ratio=F(0); max_derivative=F(0)
 for bv in product([0,1],repeat=N):
  fixed=dict(zip(U,bv)); successes=sum(all(fixed[j]==1 for j in window(i)) for i in selected)
  # For tied weights choose the all-one maximizing pattern by public tie-breaking.
  heavy=successes>=q*m/2
  W=sum(w[i,tuple(fixed[j] for j in window(i))] for i in selected)
  if heavy: assert W>=q*m*astar/2
  for p in [F(1,4),F(2,5),F(3,4)]:
   rows=[]
   for fv in product([0,1],repeat=len(free)):
    x=fixed|dict(zip(free,fv)); k=sum(fv); prob=p**k*(1-p)**(len(free)-k)
    score=F(k)/p-F(len(free)-k)/(1-p)
    den=sum(w[i,tuple(x[j] for j in window(i))] for i in positions)
    num=sum(w[i,tuple(x[j] for j in window(i))]*v[i,tuple(x[j] for j in window(i))] for i in positions)
    rows.append((prob,score,num,den))
   muA=sum(z[0]*z[2] for z in rows); mu=sum(z[0]*z[3] for z in rows)
   varA=sum(z[0]*(z[2]-muA)**2 for z in rows); varD=sum(z[0]*(z[3]-mu)**2 for z in rows)
   bound=2*r*r*sum(a[i]**2 for i in positions if i not in selected)
   assert varA<=bound and varD<=bound
   if bound: max_variance_ratio=max(max_variance_ratio,varA/bound,varD/bound)
   dA=sum(z[0]*z[1]*z[2] for z in rows); dD=sum(z[0]*z[1]*z[3] for z in rows)
   assert abs(dA)<=4*r*mu and abs(dD)<=4*r*mu
   dh=(dA*mu-muA*dD)/mu**2
   assert abs(dh)<=8*r
   max_derivative=max(max_derivative,abs(dh))
   intersect=[i for i in positions if i not in selected and set(window(i))&set(U)]
   disjoint=[i for i in positions if i not in selected and i not in intersect]
   assert len(intersect)<=r*N
   assert sum(a[i] for i in intersect)<=r*N*astar
   assert q*sum(a[i] for i in disjoint)<=mu
   if heavy:
    assert sum(a[i] for i in positions if i not in selected)<=J*mu
    assert max(varA,varD)<=V*mu**2/m
    heavy_cases+=1
   # Perfectly correlated second coordinate -A uses same denominator;
   # its variance and |derivative| are identical, so no independence premise.
   cases+=1
 records.append(dict(n=n,r=r,m=m,kind=kind,N=N,free=len(free),conditional_cases=cases,heavy_cases=heavy_cases,max_variance_ratio=str(max_variance_ratio),max_derivative=str(max_derivative)))
checks['conditional_exact']=records
# Truncated beta posterior integrals are rational for square N and rational endpoints.
posterior=[]
for N in [1,4,9,16,25,64,100]:
 root=isqrt(N); accepted=boundary=0; max_ratio=F(0)
 for t in range(N+1):
  def integral(a,b):
   return sum(F((-1)**j*comb(N-t,j),t+j+1)*(b**(t+j+1)-a**(t+j+1)) for j in range(N-t+1))
  lo,hi=F(1,4),F(3,4); y=F(t,N); p0=min(hi,max(lo,y)); Z=integral(lo,hi)
  left=max(lo,y-F(3,root)); right=min(hi,y+F(3,root))
  mass=integral(left,right)/Z if left<=right else F(0)
  if mass>=F(99,100):
   density=p0**t*(1-p0)**(N-t)/Z
   assert density<=128*root
   assert abs(N*(y-p0)/(p0*(1-p0)))<=16*root
   delta=F(1,64*root); sign=1 if p0<=F(1,2) else -1
   # Local integral / modal likelihood directly checks the asserted normalizer.
   a,b=sorted([p0,p0+sign*delta]); local=integral(a,b)/(p0**t*(1-p0)**(N-t))
   assert local>=F(1,128*root)
   max_ratio=max(max_ratio,density/root); accepted+=1; boundary+=p0 in (lo,hi)
 posterior.append(dict(N=N,T_cases=accepted,boundary_mode_cases=boundary,max_density_over_sqrtN=str(max_ratio)))
checks['posterior_exact']=posterior
# Constants, noninteger Q, branch threshold M=m, large local range.
constants=[]
for D,r in [(1,1),(2,2),(4,3),(1,64)]:
 H=3**(2*r); archF=D*H; q=F(1,4**r); L=r*archF+2*r; J=(2*r*L+1)/q; V=4*r*r*J/q
 C=max(1,400*archF*(2*r-1)/q**2,3200*archF*V); C=(C.numerator+C.denominator-1)//C.denominator if isinstance(C,F) else C
 assert F(4*archF*(2*r-1),1)/(q*q*C)<=F(1,100)
 assert F(32*archF*V,C)<=F(1,100)
 assert C>=r # Hence r>=n implies M<m for all Q>=1.
 for Q in [F(1),F(101,100),F(3,2),F(1000001,7)]:
  x=C*Q*Q; m=(x.numerator+x.denominator-1)//x.denominator
  assert m>=C*Q*Q and m<=(C+1)*Q*Q
  assert m+1<=(C+3)*Q*Q # maximal n in M<m branch
  assert m>=Q*Q # N>=m gives mesh count bound
 constants.append(dict(D=D,r=r,C=str(C)))
checks['constants_exact']=constants
checks['status']='PASS'
checks['scope']='Exact finite algebra corroboration only; no asymptotic proof, network execution, or novelty claim.'
(ROOT/'UI001_independent_checks_v1.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({'status':'PASS','conditional_cases':sum(x['conditional_cases'] for x in records),'heavy_cases':sum(x['heavy_cases'] for x in records),'posterior_T_cases':sum(x['T_cases'] for x in posterior),'posterior_boundary_modes':sum(x['boundary_mode_cases'] for x in posterior)}))
