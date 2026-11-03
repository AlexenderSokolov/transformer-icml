#!/usr/bin/env python3
"""Exact finite corroboration of FOT001; not independent review."""
from collections import Counter
from itertools import product
from math import comb, factorial
from fractions import Fraction as F
from pathlib import Path
import json, hashlib

def pairs(w): return Counter(zip(w,w[1:]))
def triples(w): return Counter(zip(w,w[1:],w[2:]))
def relocate(w,r):
    M=len(w)-2; l=r-2; h=M-r+2
    vertices=list(zip(w,w[1:])); sk=[vertices[l]]; loops=Counter()
    for i in range(l,h):
        a,b=vertices[i:i+2]
        if a==b: loops[a]+=1
        else: sk.append(b)
    p=next((i for i,s in enumerate(sk) if s==(1,1)),None)
    q=next((i for i,s in enumerate(sk) if s==(0,0) and p is not None and i>p),None)
    if q is None:return None
    interior=[]
    for i,s in enumerate(sk):
        interior.append(s)
        if i==p:interior.extend([s]*loops[1,1])
        if i==q:interior.extend([s]*loops[0,0])
    out=vertices[:l]+interior+vertices[h+1:]
    assert all(a[1]==b[0] for a,b in zip(out,out[1:]))
    return out[0]+tuple(s[1] for s in out[1:])

stats=Counter()
for N in range(2,15):
    cc=Counter()
    for mid in product((0,1),repeat=N-1):
        w=(1,)+mid+(0,); pc=pairs(w); v,u=pc[0,0],pc[0,1]; cc[v,u]+=1
        stats['start1_end0_words']+=1
        if w[:2]!=(1,1) or w[-2:]!=(0,0):continue
        tr=triples(w); j=sum(n for (a,b,c),n in tr.items() if (a,b)==(0,0))
        cross=sum(n for (a,b,c),n in tr.items() if a!=b)
        assert j==v-1 and cross==pc[0,1]+pc[1,0]
        rev=pairs(w[::-1]);assert rev[0,1]==u+1 and rev[0,0]==v
        stats['pair_endpoint_shifts']+=1
        for r in range(2,(N+1)//2+1):
            z=relocate(w,r)
            if z is None:continue
            assert len(z)==len(w) and triples(z)==tr
            assert z[:r]==w[:r] and z[-r:]==w[-r:]
            target=(1,)*(N+1-j)+(0,)*j
            distance=sum(a!=b for a,b in zip(z,target))
            assert distance<=3*cross+4*r-5
            if j>=2:
                assert z[-2:]==target[-2:]==(0,0)
                assert sum(n for (a,b,c),n in triples(target).items() if (a,b)==(0,0))==j-2
            stats['relocations']+=1
    for v in range(N+1):
        for u in range(N+1):
            H=N-v-u
            expected=comb(v+u,u)*comb(H-1,u) if H>=1 and u<=H-1 else 0
            assert cc[v,u]==expected
            stats['mixture_coefficients']+=1
            if u>=1:
                beta=F(factorial(u-1)*factorial(v),factorial(u+v))
                assert comb(v+u,u)*beta==F(1,u)
                stats['beta_integrals']+=1
for t in [F(1,100),F(1,4),F(1,2),F(3,4)]:
    R=[F(1),1-t]
    for n in range(41):
        if n>=2:R.append((1-t)*R[-1]+t*R[-2])
        total=sum(F(comb(n-u,u))*t**u*(1-t)**(n-2*u) for u in range(n//2+1))
        assert total==R[n] and 0<=total<=1
        stats['renewal_identities']+=1
for a,t in [(F(1,4),F(1,10)),(F(1,10),F(1,100)),(F(1,4),F(1,4))]:
    T=[[1-a,a],[t,1-t]];pi=[t/(a+t),a/(a+t)]
    for b,d,s,z in product(range(2),repeat=4):
        P2=T[d][s]*T[s][z]; dest=pi[s]*T[s][z]
        assert P2/dest==T[d][s]/pi[s] and P2/dest>=a+t
        stats['certificate_entries']+=1
for N in range(64,513):
    beta=F(1,N-1);q=beta/2
    for j in range(2,N//8+1):
        mass=F(2,3)*(1-q)**(N-j)*q*(1-beta)**(j-1)
        assert mass>=F(1,8*N)
        stats['null_mass_checks']+=1
c=F(1,2**16);A=2**12;x=4096
failure=2*((224+24576*c*c)/2**20+F(16,A)+F(32,x))+F(16,x)
assert failure<F(1,16)
result={'status':'PASS','checks':dict(stats),'good_failure_bound_exact':str(failure),'candidate_sha256':hashlib.sha256(Path(__file__).with_name('FOT001_candidate.md').read_bytes()).hexdigest(),'scope':'Finite exact corroboration only; no independent review or acceptance.'}
Path(__file__).with_name('check_fot001_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
