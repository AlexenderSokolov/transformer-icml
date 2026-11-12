#!/usr/bin/env python3
"""Fresh finite diagnostics; not a proof or a replay of historic evidence."""
from fractions import Fraction as F
from itertools import product
from collections import Counter, defaultdict
from math import comb
import json
import sys

if not __debug__:
    raise SystemExit('Refusing optimized Python: assertions must be enabled')

def stats(x):
    m = len(x)-2
    hist = Counter(tuple(x[i:i+3]) for i in range(m))
    j = sum(x[i:i+2] == (0,0) for i in range(m))
    cross = sum(x[i] != x[i+1] for i in range(m))
    return hist, j, cross

def relocate(x,r):
    m=len(x)-2; lo=r-2; hi=m-r+2
    edges=[tuple(x[i:i+3]) for i in range(m)]
    interior=edges[lo:hi]
    n1=interior.count((1,1,1)); n0=interior.count((0,0,0))
    keep=[e for e in interior if e not in ((1,1,1),(0,0,0))]
    vertices=[tuple(x[lo:lo+2])]+[e[1:] for e in keep]
    ones=[i for i,v in enumerate(vertices) if v==(1,1)]
    zeros=[i for i,v in enumerate(vertices) if v==(0,0)]
    if n1 and n0:
        if not ones or not any(z>ones[0] for z in zeros):
            return None
        i1=ones[0]; i0=next(z for z in zeros if z>i1)
    else:
        i1=ones[0] if n1 else -1
        i0=zeros[0] if n0 else -1
    rebuilt=[]
    for i in range(len(vertices)):
        if i==i1: rebuilt.extend([(1,1,1)]*n1)
        if i==i0: rebuilt.extend([(0,0,0)]*n0)
        if i<len(keep): rebuilt.append(keep[i])
    all_edges=edges[:lo]+rebuilt+edges[hi:]
    out=list(x[:2])
    for e in all_edges:
        assert tuple(out[-2:])==e[:2]
        out.append(e[2])
    return tuple(out)

def transport_checks():
    passed=skipped=0
    absent=ordered=0
    for m in range(2,15):
        for middle in product((0,1),repeat=m-2):
            x=(1,1)+middle+(0,0)
            hist,j,d=stats(x)
            for r in range(2,(m+2)//2+1):
                y=relocate(x,r)
                if y is None:
                    skipped+=1; continue
                assert len(y)==len(x)
                assert stats(y)[0]==hist
                assert y[:r]==x[:r] and y[-r:]==x[-r:]
                target=(1,)*(m+2-j)+(0,)*j
                dist=sum(a!=b for a,b in zip(y,target))
                assert dist<=3*d+4*r-5,(x,r,y,j,d,dist)
                if 2<=j<=m:
                    assert stats(target)[1]==j-2
                    assert target[-2:]==y[-2:]==(0,0)
                    assert dist==sum(a!=b for a,b in zip(y[:m],target[:m]))
                lo=r-2; hi=m-r+2
                e=[x[i:i+3] for i in range(lo,hi)]
                if (1,1,1) not in e or (0,0,0) not in e: absent+=1
                else: ordered+=1
                passed+=1
    return dict(passed=passed,ordered_both_loop_types=ordered,
                at_least_one_absent=absent,ineligible_both_types_skipped=skipped,
                horizons=[2,14])

def matrix(a,t):
    return ((1-a,a,F(0),F(0)),(F(0),F(0),F(1,2),F(1,2)),
            (F(1,2),F(1,2),F(0),F(0)),(F(0),F(0),t,1-t))

def skeleton(L,t):
    if L<1: return {}
    # B=0,C=1,D=2; marked/unmarked alternatives kept separately.
    dp={(2,0):F(1)}
    transitions={0:[(1,0,F(1,2)),(2,0,F(1,2))],
                 1:[(0,0,F(1,2)),(0,1,F(1,2))],
                 2:[(1,0,t),(2,0,1-t)]}
    for _ in range(L-1):
        nxt=defaultdict(F)
        for (state,u),mass in dp.items():
            for dest,mark,p in transitions[state]:
                nxt[dest,u+mark]+=mass*p
        dp=nxt
    return {u:mass/2 for (state,u),mass in dp.items() if state==1}

def mixture_checks():
    cases=mass_checks=bound_checks=0
    params=[(F(1,5),F(1,11)),(F(1,2),F(1,3)),
            (F(9,10),F(3,4)),(F(1,97),F(1,131)),(F(1,4),F(1,4))]
    for a,t in params:
        p=matrix(a,t); pi11=1/(1+t/a+4*t)
        for m in range(2,11):
            masses=defaultdict(F)
            for middle in product((0,1),repeat=m-2):
                x=(1,1)+middle+(0,0)
                mass=pi11
                for i in range(m):
                    mass*=p[2*x[i]+x[i+1]][2*x[i+1]+x[i+2]]
                hist,j,_=stats(x); u=hist[(0,0,1)]
                masses[j,u]+=mass
            for j in range(m+1):
                hs=skeleton(m-j,t)
                assert sum(hs.values())<=t
                bound_checks+=1
                for u in range(j+1):
                    expected=pi11*comb(j,u)*a**u*(1-a)**(j-u)*hs.get(u,F(0))
                    assert masses[j,u]==expected,(a,t,m,j,u,masses[j,u],expected)
                    mass_checks+=1
                for u0 in range(1,m+1):
                    # Exact upper bound after Pi_a(11)<=1 and beta integration.
                    beta_bound=sum((h/u for u,h in hs.items() if u>=u0 and u<=j),F(0))
                    assert beta_bound<=t/u0
                    bound_checks+=1
            cases+=1
    return dict(parameter_horizon_cases=cases,word_mass_identities=mass_checks,
                skeleton_and_integrated_upper_bounds=bound_checks,
                parameters=[[str(a),str(t)] for a,t in params],horizons=[2,10])

if __name__=='__main__':
    print(json.dumps({'transport':transport_checks(),'mixture':mixture_checks(),
                      'arithmetic':'exact Fraction; deterministic enumeration; no random seed',
                      'scope':'finite diagnostics for two lemmas only; not full lower theorem'},
                     sort_keys=True,indent=2))
