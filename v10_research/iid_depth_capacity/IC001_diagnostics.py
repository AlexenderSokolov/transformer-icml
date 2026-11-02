#!/usr/bin/env python3
"""Finite exact arithmetic corroboration, not uniform proof."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,math
ROOT=Path(__file__).resolve().parent

def times(h,r):
    return list(range(0,r,h))+[r] if r else [0]
def tent(x): return 2*min(x,1-x)
def labels(x,h,r):
    out=[]; wanted=set(times(h,r)); q=2**h
    for t in range(r+1):
        if t in wanted: out.append((q*x).__floor__())
        x=tent(x)
    return out

def decode(ks,h,r):
    q=2**h; ts=times(h,r); lo,hi=F(0),F(1); a,b=1,0
    for j,k in enumerate(ks):
        if k==q:
            z=F(1-b,a); assert lo<=z<=hi
            return z,z
        ends=sorted([(F(k,q)-b)/a,(F(k+1,q)-b)/a])
        lo=max(lo,ends[0]); hi=min(hi,ends[1]); assert lo<=hi
        if lo==hi:return lo,hi
        if j+1<len(ts):
            e=ts[j+1]-ts[j]; v=k//2**(h-e)
            if v%2:a,b=-2**e*a,v+1-2**e*b
            else:a,b=2**e*a,2**e*b-v
    return lo,hi

def main():
    geometry=finite=capacity=0; negative_orient=0; singletons=0
    for h in range(1,5):
        q=2**h
        for J in range(2,5):
            for r in range((J-1)*h+1):
                K=q*2**r
                # Exhaust all cell boundaries/midpoints when small, sample reproducibly otherwise.
                indices=range(2*K+1) if K<=2048 else sorted(set([0,1,2*K-1,2*K]+[i*2*K//1024 for i in range(1025)]))
                for i in indices:
                    x=F(i,2*K); ks=labels(x,h,r); lo,hi=decode(ks,h,r)
                    assert lo<=x<=hi and hi-lo<=F(1,K)
                    assert K%lo.denominator==0 and K%hi.denominator==0
                    assert len(ks)<=J
                    singletons+=lo==hi;geometry+=1
                for m in range(1,25):
                    for A in range(m+1):
                        x=F(A,m)
                        for P in [h+r,h+r+2]:
                            D=2**P; U=D*A//m; xhat=F(U,D)
                            ks=labels(xhat,h,r);lo,hi=decode(ks,h,r)
                            assert 0<=x-lo<=F(2,K)
                            ideal=x;fin=xhat
                            for _ in range(r+1):
                                assert abs(ideal-fin)<=F(1,q)
                                assert (fin*D).denominator==1
                                ideal=tent(ideal);fin=tent(fin)
                            finite+=1
    # Integer exact verification of selected ceil(log2(sqrt M/Q)) via squared comparisons.
    for J in range(2,6):
        for h in range(1,9):
            q=2**h
            for M in list(range(1,257))+[q*q-1,q*q,q*q+1,q**(2*J)-1,q**(2*J),q**(2*J)+1,10**30]:
                r0=0
                while (q*2**r0)**2<M:r0+=1
                r=min((J-1)*h,r0);K=q*2**r
                assert K*K>=min(M,q**(2*J))
                assert len(times(h,r))<=J
                capacity+=1
    data={'status':'PASS','geometry_cases':geometry,'singleton_cases':singletons,'finite_precision_cases':finite,'capacity_cases':capacity,'limitations':'Finite exact corroboration, not proof or emitted network audit','theorem_sha256':hashlib.sha256((ROOT/'IC001_theorem.md').read_bytes()).hexdigest()}
    (ROOT/'IC001_diagnostics.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data))
if __name__=='__main__':main()
