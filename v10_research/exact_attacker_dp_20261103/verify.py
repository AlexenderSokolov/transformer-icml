#!/usr/bin/env python3
"""Exhaustive DP versus flip-mask enumeration; standard library only."""
from itertools import product, combinations
import argparse

def full_update(bank, pair, c, i, m):
    a,b = pair; u=2*a+b
    x=list(bank)
    x[u]+=1
    x[4+u]+= (c == 1-a)
    x[8+u]+= (i < m//2)
    return tuple(x)

def selected_update(bank, pair, c, i, m, row):
    j,cc,d=bank
    if pair == row:
        j+=1; cc+=(c == 1-pair[0]); d+=(i<m//2)
    return (j,cc,d)

def states(h,k,selected=False):
    m=len(h)-2; assert m>=1 and 0<=k<=m
    row=tuple(h[-2:]); zero=(0,)* (3 if selected else 12)
    states={}
    for a,b in product((0,1), repeat=2):
        if any(t>=m and v!=h[t] for t,v in enumerate((a,b))): continue
        cost=sum(v!=h[t] for t,v in enumerate((a,b)) if t<m)
        if cost<=k: states[((a,b),zero)]=cost
    for t in range(2,m+2):
        nxt={}
        for (pair,bank),cost in states.items():
            for c in (0,1):
                if t>=m and c!=h[t]: continue
                cost2=cost+(t<m and c!=h[t])
                if cost2>k: continue
                b2=(selected_update(bank,pair,c,t-2,m,row) if selected
                    else full_update(bank,pair,c,t-2,m))
                key=((pair[1],c),b2)
                if cost2<nxt.get(key,m+1): nxt[key]=cost2
        states=nxt
    return {bank:cost for (suffix,bank),cost in states.items() if suffix==row}

def bank_of(z,selected=False):
    m=len(z)-2; row=tuple(z[-2:]); bank=(0,)*(3 if selected else 12)
    for i in range(m):
        pair=tuple(z[i:i+2]); c=z[i+2]
        bank=(selected_update(bank,pair,c,i,m,row) if selected
              else full_update(bank,pair,c,i,m))
    return bank

def brute(h,k,selected=False):
    m=len(h)-2; found={}
    for n in range(k+1):
        for flips in combinations(range(m),n):
            z=list(h)
            for i in flips: z[i]^=1
            bank=bank_of(z,selected)
            found[bank]=min(found.get(bank,m+1),n)
    return found

def run(max_m):
    cases=0
    for m in range(1,max_m+1):
        for h in product((0,1),repeat=m+2):
            for k in range(m+1):
                for selected in (False,True):
                    actual=states(h,k,selected)
                    expected=brute(h,k,selected)
                    assert actual==expected,(m,h,k,selected,actual,expected)
                    # Arbitrary deterministic exact readout/loss on the bank.
                    score=lambda b: sum((i+3)*(v*v+7*v) for i,v in enumerate(b))%101
                    assert max(map(score,actual))==max(map(score,expected))
                    cases+=1
        print(f'M={m}: complete; cumulative DP/brute comparisons={cases}',flush=True)
    print('PASS')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--max-m',type=int,default=6);run(p.parse_args().max_m)
