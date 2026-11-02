#!/usr/bin/env python3
"""Independent FA001 v2 diagnostics. Exact rationals only; no float/exp oracle."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json, hashlib

def dyadic_floor(num, exponent, P):
    # Compressed exponent route: never allocate 2**exponent when huge.
    shift=exponent-P
    if shift<=0: return num << (-shift)
    if shift>=abs(num).bit_length(): return -int(num<0)
    return num//(1<<shift)

def exp_interval(x, K):
    t=F(1); lo=t
    for j in range(1,K+1):
        t=t*x/j; lo+=t
    first=t*x/(K+1)
    r=x/(K+2)
    assert 0<=r<1
    return lo,lo+first/(1-r)

out={'scope':'independent exact finite diagnostics, not proof or cost benchmarks'}
conv=0
for P in [1,4,17]:
    for e in range(60):
        for n in [-257,-16,-1,0,1,16,257]:
            assert dyadic_floor(n,e,P)==(n*(1<<P))//(1<<e); conv+=1
    for n in [-257,-1,0,1,257]:
        assert dyadic_floor(n,1<<4096,P)==-int(n<0); conv+=1
out['compressed_exponent_conversion_cases']=conv
exps=0; tail=0; max_bits=0
for A in [2,4,6]:
    H=3**A
    for P in [1,3,8,17]:
        D=1<<P; J=8*A*A+2+P
        for S in sorted(set([0,1,D//3,D,A*D-1,A*D])):
            x=F(S,D); t=D; W=t; ideal=F(1); errsum=F(0)
            for j in range(1,J+1):
                prod=t*S; max_bits=max(max_bits,prod.bit_length())
                t=prod//(j*D); W+=t; ideal=ideal*x/j
                assert 0<=F(t,D)<=ideal
                errsum+=ideal-F(t,D)
            assert D<=W<=H*D
            assert errsum<=F(H*J,D)
            lo,hi=exp_interval(x,J+20)
            assert lo>=F(W,D)
            assert hi-F(W,D)<=F(H*J+1,D)
            exps+=1
    for j in range(8*A*A,8*A*A+100):
        assert F(A**j,factorial(j))<=F(1,1<<j); tail+=1
out['exp_interval_cases']=exps; out['odd_even_factorial_tail_cases']=tail
out['max_taylor_product_bits_observed']=max_bits
ratios=0
for m in [1,2,3,19,257]:
    for P in [1,3,8]:
        D=1<<P
        for polarity in [-1,1]:
            wi=[F(3+(i%5),2) for i in range(m)]
            wh=[w+F((-1)**i,4) for i,w in enumerate(wi)]
            vi=[F(polarity*((i%9)-5),4) for i in range(m)]
            vh=[v+F((-1)**i,2*D) for i,v in enumerate(vi)]
            # Quantize both approximants, then test lemma with actual discrepancies.
            W=[(w*D).__floor__() for w in wh]; V=[(v*D).__floor__() for v in vh]
            eta_w=max(abs(F(w,D)-z) for w,z in zip(W,wi))
            eta_v=max(abs(F(v,D)-z) for v,z in zip(V,vi))
            vm=max(abs(v) for v in vi)
            Z=sum(W); N=sum(w*v for w,v in zip(W,V)); O=N//Z
            ideal=sum(w*v for w,v in zip(wi,vi))/sum(wi)
            assert Z>=m*D
            assert 0<=F(N,Z*D)-F(O,D)<F(1,D)
            assert abs(F(O,D)-ideal)<=F(1,D)+eta_v+2*vm*eta_w
            ratios+=1
out['signed_normalization_cases']=ratios
choices=[]
for Cstar in [1,7,10**9,10**100]:
    C=1
    while Cstar*(C+5)>1<<C: C+=1
    for h in range(301):
        P=4*h+C
        assert Cstar*(P+1)*(1<<h)<=1<<P
        for O in [-1000001,-1,0,1,1000001]:
            assert (O//(1<<(P-h)))==((F(O,1<<P)*(1<<h)).__floor__())
    choices.append({'Cstar':str(Cstar),'Carch':C})
out['precision_choices']=choices
# Exact tiny grid-crossing witness: no label-agreement theorem.
P=8; h=2; ideal=F(1,4); actual=ideal-F(1,1<<P)
assert abs(actual-ideal)<=F(1,1<<h)
assert (ideal*(1<<h)).__floor__()!= (actual*(1<<h)).__floor__()
out['label_equality_counterexample']={'ideal':'1/4','actual':str(actual),'Q':4}
out['status']='PASS'
print(json.dumps(out,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
