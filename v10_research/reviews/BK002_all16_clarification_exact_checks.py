#!/usr/bin/env python3
"""Narrow independent checks of BK002's immutable-source prose addendum."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
hashes={
'binary_beta_known_adaptation/BK002_full_history_supplied_beta_obstruction.md':'e50381632af4825923138c086c34e7b3b082af381d4b9ec8f641825455c50e12',
'reviews/BK002_independent_full_review.md':'41f6a35a5224271a6f8cc70a8b84e4099526257b47aef19eb6f64779ca41c3a4',
'binary_beta_known_adaptation/BK002_ALL16_ENUMERATION_CLARIFICATION.md':'cf871a79db047fd28f43e211431e344450e96cad3b94b0dc1f2b773fa7961a46'}
for p,h in hashes.items(): assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h
groups=[[(1,2),(3,1)],[(3,0)],[(0,3),(1,3),(2,3)],[(3,2)],
        [(1,1),(2,2)],[(0,1),(0,2),(2,1)],[(0,0),(1,0),(2,0),(3,3)]]
flat=[p for g in groups for p in g]
assert len(flat)==16 and set(flat)==set(product(range(4),repeat=2))
assert sum([2,1,3,1,2,2,4])==15 and sum(map(len,groups))==16
n=0
for M in [256,1024,4096,65536,10**8]:
    T=M//8
    for k in sorted(set([T,T//2,T//3])):
        if k*k<4*M: continue
        lo=F(k,32*T); hi=F(1,16)
        for a in sorted(set([lo,(lo+hi)/2,hi])):
            d=F(1,k); e=1-d; t=F(1,4*M); x=1/(e/a+2+d/t)
            pi=[x*e/a,x,x,x*d/t]
            P=[[1-a,a,0,0],[0,0,e,d],[e,d,0,0],[0,0,t,1-t]]
            P2=[[sum(P[i][h]*P[h][j] for h in range(4)) for j in range(4)] for i in range(4)]
            assert P2[0][2]==a*e==e*a==P2[2][1]
            assert d*d*x<=a*d*d/e<=a/12<=a*e
            assert all(P2[i][j]>=d*d*pi[j] for i,j in flat)
            n+=1
out={'status':'PASS','scope':'narrow all16 enumeration clarification, not theorem reacceptance',
     'source_hashes':hashes,'partition_sizes':list(map(len,groups)),
     'complete_disjoint_positions':len(flat),'exact_family_cases':n,
     'all16_inequalities':16*n,'newly_explicit_inequalities':n,
     'limits':'Finite examples corroborate only tested cases; the universal omitted-entry bound is the displayed accepted algebra.'}
(R/'reviews/BK002_all16_clarification_exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
