#!/usr/bin/env python3
"""Independent corroboration only; the universal argument is in REVIEW.md."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent

def stats(w):
    pairs=tuple(sum((a,b)==e for a,b in zip(w,w[1:])) for e in ((0,0),(0,1),(1,0),(1,1)))
    return pairs,sum(v==0 for v in w[:-1])

def relocate(w,r):
    lo,hi=r-1,len(w)-r
    segment=w[lo:hi+1]
    reduced=[segment[0]]
    loops=[0,0]
    for a,b in zip(segment,segment[1:]):
        if a==b: loops[a]+=1
        else: reduced.append(b)
    selected=None
    for i,a in enumerate(reduced):
        if a==1:
            for j in range(i+1,len(reduced)):
                if reduced[j]==0:
                    selected=(i,j);break
            break
    if selected is None:return None
    middle=[]
    for i,a in enumerate(reduced):
        middle.append(a)
        if i==selected[0]:middle.extend([1]*loops[1])
        if i==selected[1]:middle.extend([0]*loops[0])
    return w[:lo]+tuple(middle)+w[hi+1:]

nprob=nrel=nshift=nlemma=0
for N in range(1,12):
    coeff=Counter()
    for interior in product((0,1),repeat=N-1):
        w=(1,)+interior+(0,)
        p,j=stats(w);u=p[1];d=p[1]+p[2]
        coeff[j,u]+=1
        rp,rj=stats(w[::-1])
        assert (rj,rp[1],rp[1]+rp[2])==(j+1,u+1,d)
        nshift+=1
        for r in range(1,(N+1)//2+1):
            z=relocate(w,r)
            if z is None:continue
            assert len(z)==len(w) and stats(z)[0]==p
            assert z[:r]==w[:r] and z[-r:]==w[-r:]
            target=(1,)*(N+1-j)+(0,)*j
            assert sum(a!=b for a,b in zip(target,z))<=d+4*r-2
            if j:assert target[-1]==z[-1]==0
            nrel+=1
    for a,t in ((Q(1,5),Q(1,17)),(Q(1,4),Q(1,81920))):
        pi=a/(a+t)
        for j in range(N):
            for u in range(j+1):
                H=N-j
                lhs=pi*coeff[j,u]*a**u*(1-a)**(j-u)*t**(u+1)*(1-t)**(H-1-u) if u<H else Q(0)
                h=t*comb(H-1,u)*t**u*(1-t)**(H-1-u) if u<H else Q(0)
                rhs=pi*comb(j,u)*a**u*(1-a)**(j-u)*h
                assert lhs==rhs
                nprob+=1
        for H in range(1,N+1):
            assert sum(t*comb(H-1,u)*t**u*(1-t)**(H-1-u) for u in range(H))==t
# Test the abstract block inequality with chosen, possibly empty, ordered blocks.
for m in range(1,8):
    for w in product((0,1),repeat=m):
        for i in range(m+1):
            for e in range(i,m+1):
                if any(v!=1 for v in w[i:e]):continue
                for j in range(e,m+1):
                    for f in range(j,m+1):
                        if any(v!=0 for v in w[j:f]):continue
                        A1,A0=e-i,f-j
                        o=sum(w)-A1;z=m-sum(w)-A0
                        for q in range(m-A0+1):
                            target=(1,)*(m-A0-q)+(0,)*(A0+q)
                            dist=sum(a!=b for a,b in zip(w,target))
                            assert dist<=max(z+q,2*o+z-q)
                            nlemma+=1
c=Q(1,65536); A=4096
failure=2*((208+24576*c*c)/2**20+Q(16,A))
assert failure<Q(1,16)
assert Q(1,16)+Q(8,1024)<Q(1,2)
assert 2*c<=Q(1,64)
assert Q(1,32)+c/16<=Q(1,16)
assert Q(1,16)+Q(4,128)<1
assert Q(1,64)*c/Q(32)/8==Q(1,2**30)
assert 5*Q(1,2**30)<=c/32
out=dict(status='PASS',purpose='independent finite corroboration; not universal proof',N_range=[1,11],rational_word_mass_checks=nprob,relocations=nrel,reversal_checks=nshift,abstract_block_inequalities=nlemma,conditional_count_failure=str(failure))
(ROOT/'fresh_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
