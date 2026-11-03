#!/usr/bin/env python3
"""Exact finite corroboration, not a proof or independent review."""
from itertools import product
from math import comb, factorial
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import hashlib, json

def counts(w):
    return Counter(zip(w,w[1:]))
def quantities(w):
    c=counts(w)
    return sum(x==0 for x in w[:-1]),c[0,1],c[0,1]+c[1,0]
def transform(w,r):
    N=len(w)-1;l=r-1;h=N-r+1
    interior=w[l:h+1]
    sk=[interior[0]];loops=Counter()
    for a,b in zip(interior,interior[1:]):
        if a==b: loops[a]+=1
        else: sk.append(b)
    one=next((i for i,x in enumerate(sk) if x==1),None)
    zero=next((i for i,x in enumerate(sk) if x==0 and one is not None and i>one),None)
    if zero is None:return None
    out=[]
    for i,x in enumerate(sk):
        out.append(x)
        if i==one:out += [1]*loops[1]
        if i==zero:out += [0]*loops[0]
    return tuple(w[:l])+tuple(out)+tuple(w[h+1:])

def main():
    nwords=ncoeff=nreloc=nreverse=nshift=nbeta=nskel=0
    for N in range(1,15):
        coefficients=Counter()
        for middle in product((0,1),repeat=N-1):
            w=(1,)+middle+(0,)
            j,u,d=quantities(w);nwords+=1
            coefficients[j,u]+=1
            jr,ur,dr=quantities(w[::-1])
            assert (jr,ur,dr)==(j+1,u+1,d);nreverse+=1
            for r in range(1,(N+1)//2+1):
                v=transform(w,r)
                if v is None:continue
                assert len(v)==len(w) and counts(v)==counts(w)
                assert v[:r]==w[:r] and v[-r:]==w[-r:]
                target=(1,)*(N+1-j)+(0,)*j
                distance=sum(x!=y for x,y in zip(v,target))
                assert distance<=d+4*r-2,(N,w,r,v,distance,d)
                if j>=1:assert v[-1]==target[-1]==0
                nreloc+=1
        for j in range(N):
            H=N-j
            for u in range(j+1):
                expected=comb(j,u)*comb(H-1,u) if u<=H-1 else 0
                assert coefficients[j,u]==expected,(N,j,u)
                ncoeff+=1
                if u>=1:
                    beta=F(factorial(u-1)*factorial(j-u),factorial(j))
                    assert comb(j,u)*beta==F(1,u);nbeta+=1
        for t in (F(1,3),F(1,7),F(1,19)):
            for H in range(1,N+1):
                assert sum(t*comb(H-1,u)*t**u*(1-t)**(H-1-u) for u in range(H))==t
                nskel+=1
        for j in range(1,N+1):
            w=(1,)*(N+1-j)+(0,)*j
            assert quantities(w)[0]==j-1;nshift+=1
    # Exact rational finite-domain implications that do not involve N logarithms.
    c=F(1,2**16);A=2**12
    failure=2*((208+24576*c*c)/2**20+F(16,A))
    assert failure<F(1,16)
    assert F(1,16)+F(8,1024)<F(1,2)
    assert 2*c<=F(1,64)
    assert F(1,32)+c/16<=F(1,16)
    assert F(1,16)+F(4,128)<1
    # Stationarity and common-atom checks are exact on representative parameters.
    nstat=0
    for a in (F(1,4),F(1,5),F(1,7)):
        for t in (F(1,19),F(1,31)):
            pi0=t/(a+t);pi1=a/(a+t)
            assert pi0*a==pi1*t
            assert pi0*(1-a)+pi1*t==pi0
            assert 1-t>=a;nstat+=1
    p=Path(__file__)
    out={'status':'PASS','scope':'exact finite combinatorics and rational constants; not independent review','N_range':[1,14], 'words':nwords,'skeleton_coefficients':ncoeff,'relocations':nreloc,'reversal_checks':nreverse,'null_suffix_shift_checks':nshift,'beta_cancellations':nbeta,'skeleton_mass_checks':nskel,'stationarity_checks':nstat,'conditional_count_failure_bound':str(failure),'script_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
