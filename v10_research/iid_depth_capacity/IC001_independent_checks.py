#!/usr/bin/env python3
"""Independent reviewer checks. Exact rational enumeration, not a universal proof."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,math
HERE=Path(__file__).resolve().parent

def tent(x): return 2*min(x,1-x)
def times(h,r): return list(range(0,r,h))+[r] if r else [0]
def values(x,h,r):
    selected=set(times(h,r)); out=[]
    for t in range(r+1):
        if t in selected:out.append(x)
        x=tent(x)
    return out

def decode(labels,h,r):
    # Independently track integer affine functions on a rational interval.
    lo,hi=F(0),F(1); a,b=1,0; ts=times(h,r); Q=1<<h
    for j,k in enumerate(labels):
        counts['negative_orientation_stages']+=a<0
        if k==Q:
            x=F(1-b,a); assert lo<=x<=hi
            return x,x
        u,v=sorted((F(k,Q)-b,F(k+1,Q)-b))
        u,v=sorted((u/a,v/a));lo=max(lo,u);hi=min(hi,v)
        assert lo<=hi
        if lo==hi:return lo,hi
        if j+1<len(labels):
            e=ts[j+1]-ts[j];m=1<<e;branch=k//(Q//m)
            if branch%2:a,b=-m*a,branch+1-m*b
            else:a,b=m*a,m*b-branch
    return lo,hi

counts={'geometry':0,'finite_mean':0,'capacity':0,'branch_bins':0,'singletons':0,'negative_orientation_stages':0}
for J in range(2,5):
 for h in range(1,5):
  Q=1<<h
  for r in range((J-1)*h+1):
   if h+r>13:continue
   D=1<<(h+r)
   # Every finest cell endpoint and midpoint, including exact folds 0,1/2,1.
   for a in range(2*D+1):
    x=F(a,2*D);ys=values(x,h,r);labels=[int(Q*y) for y in ys]
    lo,hi=decode(labels,h,r)
    assert lo<=x<=hi and hi-lo<=F(1,D)
    assert D%lo.denominator==0 and D%hi.denominator==0
    counts['singletons']+=lo==hi
    counts['geometry']+=1
   # All coarse bins are contained in claimed branch, including shared endpoints.
   for e in range(1,h+1):
    for k in range(Q):
     v=k//(1<<(h-e))
     assert F(v,1<<e)<=F(k,Q)<=F(k+1,Q)<=F(v+1,1<<e)
     counts['branch_bins']+=1
   for P in (h+r,h+r+3):
    fine=1<<P
    for m in range(1,36):
     for A in range(m+1):
      x=F(A,m);u=fine*A//m;xh=F(u,fine)
      ys=values(xh,h,r);labels=[int(Q*y) for y in ys]
      lo,hi=decode(labels,h,r)
      assert 0<=x-lo<=F(1,D)+F(1,fine)<=F(2,D)
      ideal=x;actual=u
      for t in range(r+1):
       assert abs(ideal-F(actual,fine))<=F(1,Q)
       ideal=tent(ideal);actual=2*min(actual,fine-actual)
      assert actual in range(fine+1)
      counts['finite_mean']+=1
for J in range(2,8):
 for h in range(1,12):
  Q=1<<h;cap=(J-1)*h
  for M in list(range(1,501))+[2**k+delta for k in range(1,75) for delta in (-1,0,1)]:
   r=0
   while r<cap and Q*Q*4**r<M:r+=1
   assert 0<=r<=cap
   Deff=Q*2**r
   assert Deff*Deff>=min(M,Q**(2*J))
   # Test independently supplied positive capacity constants.
   for kappa in (F(1,16),F(1,2),F(1),F(2),F(16)):
    if Q**(2*J)>=kappa*kappa*M:
     assert Deff*Deff*max(F(1),1/kappa)**2>=M
   counts['capacity']+=1
result={'status':'PASS','theorem_sha256':hashlib.sha256((HERE/'IC001_theorem.md').read_bytes()).hexdigest(),'counts':counts,'notes':'Exact finite checks supplement mathematical review; no emitted-network or formal verification claim.'}
(HERE/'IC001_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
