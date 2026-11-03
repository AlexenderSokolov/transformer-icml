#!/usr/bin/env python3
"""Independently test full half-histogram DP and four-coordinate flow reconstruction."""
from itertools import product, combinations

def reconstruct(n, start, end, free):
    a,b,c,d=free
    delta=lambda u:int(end==u)-int(start==u)
    e=b+delta((0,0)); f=delta((0,1))-b+c+d; g=d-delta((1,1))
    h=n-(a+b+c+d+e+f+g)
    return (a,b,c,d,e,f,g,h)

def hist(z,m):
    hh=[0]*8; rr=[0]*8; split=m//2
    for i in range(m):
        triple=4*z[i]+2*z[i+1]+z[i+2]
        (hh if i<split else rr)[triple]+=1
    initial=tuple(z[:2]); middle=tuple(z[split:split+2]); end=tuple(z[-2:])
    assert reconstruct(split,initial,middle,hh[:4])==tuple(hh)
    assert reconstruct(m-split,middle,end,rr[:4])==tuple(rr)
    return initial,tuple(hh),tuple(rr)

def dp(z,k):
    m=len(z)-2; split=m//2
    # State: initial, current pair, split pair or None, first-half free, second-half free.
    st={}
    for x in product((0,1),repeat=2):
        if any(t>=m and x[t]!=z[t] for t in range(2)): continue
        c=sum(x[t]!=z[t] for t in range(2) if t<m)
        if c<=k: st[(x,x,x if split==0 else None,(0,)*4,(0,)*4)]=c
    for t in range(2,m+2):
        i=t-2; new={}
        for (initial,pair,mid,left,right),cost in st.items():
            for bit in (0,1):
                if t>=m and bit!=z[t]: continue
                nc=cost+(t<m and bit!=z[t])
                if nc>k: continue
                idx=4*pair[0]+2*pair[1]+bit
                arr=list(left if i<split else right)
                if idx<4: arr[idx]+=1
                nl,nr=(tuple(arr),right) if i<split else (left,tuple(arr))
                np=(pair[1],bit); nm=np if i+1==split else mid
                key=(initial,np,nm,nl,nr)
                new[key]=min(new.get(key,m+1),nc)
        st=new
    out={}
    for (ini,pair,mid,l,r),cost in st.items():
        key=(ini,reconstruct(split,ini,mid,l),reconstruct(m-split,mid,pair,r))
        out[key]=min(out.get(key,m+1),cost)
    return out

def brute(z,k):
    m=len(z)-2; out={}
    for n in range(k+1):
        for flips in combinations(range(m),n):
            q=list(z)
            for i in flips: q[i]^=1
            key=hist(q,m);out[key]=min(out.get(key,m+1),n)
    return out

if __name__=='__main__':
    import sys
    maxm=int(sys.argv[1]) if len(sys.argv)>1 else 5
    tests=0
    for m in range(1,maxm+1):
        for z in product((0,1),repeat=m+2):
            for k in range(m+1):
                assert dp(z,k)==brute(z,k),(m,z,k)
                tests+=1
        print('M=',m,'cumulative comparisons=',tests,flush=True)
    print('PASS')
