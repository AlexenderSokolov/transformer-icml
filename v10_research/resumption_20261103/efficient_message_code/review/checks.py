#!/usr/bin/env python3
"""Independent finite diagnostics, not a proof or full channel-code implementation."""
import hashlib, json, random
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def deg(p): return p.bit_length()-1

def rem(a,b):
    while a and deg(a)>=deg(b): a ^= b << (deg(a)-deg(b))
    return a

def field(k):
    for P in range(1<<k,1<<(k+1)):
        if all(rem(P,d) for j in range(1,k//2+1) for d in range(1<<j,1<<(j+1))): return P
    raise AssertionError('irreducible not found')

def diagnostic(k,K,seed):
    P=field(k); q=1<<k; n=4*K
    assert n<=q
    def mul(a,b):
        c=0
        while b:
            if b&1:c^=a
            a<<=1
            if a&q:a^=P
            b>>=1
        return c
    def power(a,n):
        z=1
        while n:
            if n&1:z=mul(z,a)
            a=mul(a,a);n>>=1
        return z
    def inv(a):
        assert a
        return power(a,q-2)
    def ev(f,x):
        z=0
        for a in f[::-1]:z=mul(z,x)^a
        return z
    def nullvec(A):
        A=[r[:] for r in A]; rows=len(A);cols=len(A[0]);piv=[];at=0
        for c in range(cols):
            r=next((r for r in range(at,rows) if A[r][c]),None)
            if r is None:continue
            A[at],A[r]=A[r],A[at];z=inv(A[at][c]);A[at]=[mul(v,z) for v in A[at]]
            for r in range(rows):
                if r!=at and A[r][c]:
                    z=A[r][c];A[r]=[v^mul(z,w) for v,w in zip(A[r],A[at])]
            piv.append(c);at+=1
            if at==rows:break
        free=[c for c in range(cols) if c not in piv]
        if not free:return None
        v=[0]*cols;v[free[0]]=1
        for r,c in enumerate(piv):v[c]=A[r][free[0]]
        return v
    def trim(f):
        while f and f[-1]==0:f.pop()
        return f
    def decode(r):
        A=[]
        for x,y in enumerate(r):
            xp=[1]
            for j in range(1,2*K):xp.append(mul(xp[-1],x))
            A.append(xp+[mul(y,z) for z in xp[:K+1]])
        v=nullvec(A)
        if v is None:return None
        Q=trim(v[:2*K]);E=trim(v[2*K:]);assert E
        quot=[0]*max(0,len(Q)-len(E)+1)
        while Q and len(Q)>=len(E):
            j=len(Q)-len(E);z=mul(Q[-1],inv(E[-1]));quot[j]=z
            for i,e in enumerate(E):Q[i+j]^=mul(z,e)
            trim(Q)
        if Q or len(trim(quot))>K:return None
        quot += [0]*(K-len(quot))
        if sum(ev(quot,x)!=y for x,y in enumerate(r))>K:return None
        return quot
    rng=random.Random(seed);cases=0
    for trial in range(30):
        f=[rng.randrange(q) for _ in range(K)] if trial else [0]*K
        cw=[ev(f,x) for x in range(n)]
        for e in range(K+1):
            r=cw[:]
            positions=([0]+rng.sample(range(1,n),e-1)) if e else []
            for i in positions:r[i]^=rng.randrange(1,q)
            assert decode(r)==f,(k,K,trial,e)
            cases+=1
    return {'k':k,'K':K,'irreducible':P,'corrected_cases':cases,'evaluation_zero_errors_included':True}

for B in range(1,100001):
    k=(8*B-1).bit_length();q=1<<k;K=(B+k-1)//k;n=4*K
    assert k>=3 and 8*B<=q<16*B and n<=q and k<=4*B
    assert 4*K*k<=20*B
    assert 4*K-8*k*(K+1)<=-6*k*K-8*k<=-6*B
result={'status':'PASS','parameter_B_range':[1,100000],
        'BW_tests':[diagnostic(k,K,123+k+K) for k,K in [(3,1),(4,2),(4,3),(5,4),(7,3),(8,5)]],
        'limits':'Finite arithmetic diagnostics only. Does not execute inner exhaustive search, channel sampling, or benchmark full construction.'}
result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(ROOT/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
