#!/usr/bin/env python3
"""Exact finite diagnostics for PE1; not a proof, benchmark or SRC emulator."""
from fractions import Fraction as F
from itertools import product
from math import ceil
import hashlib
import json
from pathlib import Path


def relu(x):
    return max(0, x)


def bounded_clean(y):
    return 2 * relu(y-F(1,4))-2*relu(y-F(3,4))


def full_clean(j,Q):
    return relu(j-(Q//2-1))-relu(j-Q//2)


def extract(A,h):
    residue=A
    result=[]
    for j in range(h,-1,-1):
        bit=relu(residue-(2**j-1))-relu(residue-2**j)
        assert bit in (0,1)
        residue-=2**j*bit
        assert 0<=residue<2**j
        result.append((j,bit))
    assert residue==0
    assert sum(2**j*bit for j,bit in result)==A
    return result


def max_clique(adj):
    best=0
    def visit(size, candidates):
        nonlocal best
        if size+candidates.bit_count()<=best: return
        if not candidates:
            best=max(best,size); return
        while candidates:
            if size+candidates.bit_count()<=best: return
            v=(candidates & -candidates).bit_length()-1
            candidates &= ~(1<<v)
            visit(size+1,candidates & adj[v])
        best=max(best,size)
    visit(0,(1<<len(adj))-1)
    return best


def run():
    checks={'extractors':0,'bounded_cleaner':0,'full_cleaner':0,'capacity':0,
            'l1_repeat_received':0,'l1_overlap_boundary':0}
    for h in range(2,10):
        Q=2**h
        for A in range(Q+1):
            extract(A,h); checks['extractors']+=1
        for bit in (0,1):
            for j in range(Q+1):
                dist=abs(F(j,Q)-bit)
                if dist<=F(1,4):
                    assert bounded_clean(F(j,Q))==bit
                    checks['bounded_cleaner']+=1
                if dist<F(1,2):
                    assert full_clean(j,Q)==bit
                    checks['full_cleaner']+=1
    for L in range(1,5):
        for e in range(L+1):
            s=(L//(2*e+1))+1
            for m in (1,2):
                points=list(product(range(L+1),repeat=m))
                adj=[]
                for u in points:
                    mask=0
                    for j,v in enumerate(points):
                        if max(abs(a-b) for a,b in zip(u,v))>2*e:
                            mask|=1<<j
                    adj.append(mask)
                got=max_clique(adj)
                assert got==s**m,(L,e,m,got,s**m)
                checks['capacity']+=1
    for Q in (2,4,8):
        for r in (1,2,3):
            D=(r*Q-1)//2
            for bit in (0,1):
                z=(1+Q*bit,)*r
                for w in product(range(1,2*Q+1),repeat=r):
                    if sum(abs(a-b) for a,b in zip(w,z))<=D:
                        S=sum(v-1 for v in w)
                        decoded=int(S>=r*Q//2)
                        assert decoded==bit,(Q,r,D,bit,w)
                        checks['l1_repeat_received']+=1
            w=(1+Q//2,)*r
            assert sum(abs(v-1) for v in w)==r*Q//2
            assert sum(abs(v-(Q+1)) for v in w)==r*Q//2
            checks['l1_overlap_boundary']+=1
    p0,p1=F(1,4),F(3,4)
    overlap=F(0)
    for bits in product((0,1),repeat=3):
        n=sum(bits)
        overlap+=min(p0**n*(1-p0)**(3-n),p1**n*(1-p1)**(3-n))
    assert overlap==F(5,16)
    lower=F(1,2)*overlap/2
    assert lower==F(5,64)
    return {'status':'PASS','checks':checks,'iid_3_overlap':str(overlap),
            'iid_risk_lower':str(lower),
            'limitations':'Finite diagnostics only; no universal proof, full SRC execution, training, physical fault experiment or measured cost.'}

if __name__=='__main__':
    result=run()
    root=Path(__file__).resolve().parent
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result,indent=2))
    (root/'diagnostics.json').write_text(json.dumps(result,indent=2)+'\n')
