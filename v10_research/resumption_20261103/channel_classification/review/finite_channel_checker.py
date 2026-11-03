#!/usr/bin/env python3
"""Small exact-arithmetic corroboration only; not a proof of asymptotic claims.
Standalone standard-library script. Emits deterministic JSON; writes no files.
"""
from fractions import Fraction as F
from itertools import product
import json

CASES = {
    'identical': ([F(1,3), F(2,3)], [F(1,3), F(2,3)]),
    'disjoint': ([F(1), F(0)], [F(0), F(1)]),
    'nested_support': ([F(1), F(0), F(0)], [F(1,2), F(1,3), F(1,6)]),
    'both_exclusive': ([F(1,2), F(1,2), F(0)], [F(1,3), F(0), F(2,3)]),
    'equal_support_asymmetric': ([F(1,4), F(3,4), F(0)], [F(2,3), F(1,3), F(0)]),
    'reverse_nested_support': ([F(1,2), F(1,2)], [F(1), F(0)]),
}

def mul(xs):
    ans=F(1)
    for x in xs: ans*=x
    return ans

def law(rows, inputs, outputs):
    return mul(rows[b][y] for b,y in zip(inputs,outputs))

def run():
    report={}
    for name,rows in CASES.items():
        assert all(sum(row)==1 and all(p>=0 for p in row) for row in rows)
        alphabet=range(len(rows[0]))
        supports=[{y for y in alphabet if row[y]>0} for row in rows]
        lam=sum(min(rows[0][y],rows[1][y]) for y in alphabet)
        kind=('identical' if rows[0]==rows[1] else 'disjoint' if not supports[0]&supports[1]
              else 'equal_support_distinct' if supports[0]==supports[1] else 'unequal_overlap')
        entry={'classification':kind,'lambda':str(lam),'common_mass':{}}
        for R in range(5):
            words=list(product(range(2),repeat=R))
            mass=F(0)
            for v in product(alphabet,repeat=R):
                common=mul(min(rows[0][y],rows[1][y]) for y in v)
                values=[law(rows,w,v) for w in words]
                assert all(q>=common for q in values)
                assert min(values)==common
                mass+=common
            assert mass==lam**R
            entry['common_mass'][str(R)]=str(mass)
        if kind=='unequal_overlap':
            # Orient so row 1 has at least one exclusive symbol.
            if not supports[1]-supports[0]: rows=(rows[1],rows[0]); supports=supports[::-1]
            exclusive=supports[1]-supports[0]
            p=sum(rows[1][y] for y in exclusive)
            assert 0<p<1
            conditional=[]
            for bit,word in enumerate([(0,1),(1,0)]):
                outcomes={'correct':F(0),'wrong':F(0),'erasure':F(0),'impossible_double':F(0)}
                for v in product(alphabet,repeat=2):
                    prob=law(rows,word,v)
                    hits=[i for i,y in enumerate(v) if y in exclusive]
                    if len(hits)==2: outcomes['impossible_double']+=prob
                    elif not hits: outcomes['erasure']+=prob
                    else:
                        decoded=1 if hits[0]==0 else 0
                        outcomes['correct' if decoded==bit else 'wrong']+=prob
                assert outcomes=={'correct':p,'wrong':F(0),'erasure':1-p,'impossible_double':F(0)}
                conditional.append({k:str(v) for k,v in outcomes.items()})
            assert conditional[0]==conditional[1]
            entry['balanced_two_input_bec']={'p':str(p),'conditionals':conditional}
        if kind=='equal_support_distinct':
            kappa=max(max(rows[0][y]/rows[1][y],rows[1][y]/rows[0][y]) for y in supports[0])
            assert kappa>1
            for R in range(5):
                for v in product(alphabet,repeat=R):
                    probs=[law(rows,w,v) for w in product(range(2),repeat=R)]
                    assert max(probs)<=kappa**R*min(probs)
            entry['kappa']=str(kappa)
            entry['all_codeword_likelihood_comparison_R_0_to_4']=True
        report[name]=entry
    return {'status':'PASS','arithmetic':'fractions.Fraction exact','scope':'Finite corroboration only; no asymptotic proof or minimax computation. Feasible target used analytically is Cg+1, not every fixed constant.','cases':report}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
