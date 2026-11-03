"""Exact finite diagnostics; not a substitute for the all-horizon proof."""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import json, hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent

def counts(x):
    M=len(x)-2
    out=[0]*12
    for i in range(M):
        a,b,c=x[i:i+3]; j=3*(2*a+b)
        out[j]+=1
        out[j+1]+=int(c==1-a)
        out[j+2]+=int(i<M//2)
    return tuple(out)

def means(M,p):
    j=((1-p)**2,p*(1-p),p*(1-p),p*p)
    c=(p*(1-p)**2,p*p*(1-p),p*(1-p)**2,p*p*(1-p))
    return tuple(v for a,b in zip(j,c) for v in (a,b,F(M//2,M)*a))

def roundq(x,Q):
    y=x*Q+F(1,2)
    return y.numerator//y.denominator

out={}
# Exhaustive finite expectations with overlapping pairs and triples, also odd M.
words=edges=0
for M in range(1,8):
    for p in (F(1,8),F(3,16),F(1,4)):
        sums=[F(0)]*12
        for x in product((0,1),repeat=M+2):
            n=sum(x); prob=p**n*(1-p)**(M+2-n); c=counts(x)
            for j in range(12): sums[j]+=prob*c[j]/M
        assert tuple(sums)==means(M,p)
    for x in product((0,1),repeat=M+2):
        c=counts(x); words+=1
        for i in range(M+2):
            y=list(x);y[i]^=1;d=counts(y);edges+=1
            assert all(abs(a-b)<=3 for a,b in zip(c,d))
            assert all(abs(c[j]-d[j])<=2 for j in range(12) if j%3!=1)
out['exhaustive']={'M':'1..7','p':['1/8','3/16','1/4'],'words':words,'bit_flip_edges':edges,'exact_expectations':True,'sensitivity':True}
# Analytic derivative polynomials, evaluated at endpoints and interior critical points.
def evalpoly(co,p): return sum(c*p**i for i,c in enumerate(co))
derivs=[(2,-2),(1,-2),(1,-2),(0,2)]  # magnitudes for J
cderivs=[(1,-4,3),(0,2,-3)]
def extrema(co):
    pts=[F(1,8),F(1,4)]
    if len(co)==3 and co[2]:
        v=-F(co[1],2*co[2])
        if pts[0]<v<pts[1]:pts.append(v)
    return min(evalpoly(co,p) for p in pts)
assert [extrema(c) for c in derivs]==[F(3,2),F(1,2),F(1,2),F(1,4)]
assert [extrema(c) for c in cderivs]==[F(3,16),F(13,64)]
assert F(1,3)*F(1,4)==F(1,12)
out['derivative_minima']={'J':[str(extrema(c)) for c in derivs],'C':[str(extrema(c)) for c in cderivs],'D_uniform_lower':'1/12'}
# Certified root-free rational gaps from exact monotonic bisection enclosures.
certs=[]
for M in (64,65,127):
    for h in range(9):
        Q=1<<h;left=F(1,8);right=F(1,4)
        roots=[]
        for coord in range(12):
            fl=means(M,left)[coord];fr=means(M,right)[coord]
            for k in range(Q):
                t=F(2*k+1,2*Q)
                if min(fl,fr)<=t<=max(fl,fr):
                    lo,hi=left,right
                    for _ in range(64):
                        mid=(lo+hi)/2;v=means(M,mid)[coord]
                        if (v<t)==(fl<fr):lo=mid
                        else:hi=mid
                    roots.append((lo,hi))
        roots.sort()
        gaps=[];cursor=left
        for lo,hi in roots:
            if lo>cursor:gaps.append((cursor,lo))
            cursor=max(cursor,hi)
        if cursor<right:gaps.append((cursor,right))
        a,b=max(gaps,key=lambda ab:ab[1]-ab[0]);L=b-a
        p0=a+L/3;p1=a+2*L/3
        assert len(roots)<=12*Q
        assert L>=F(1,104*Q)
        assert p1-p0>=F(1,312*Q)
        f0=means(M,p0);f1=means(M,p1)
        code0=tuple(roundq(v,Q) for v in f0);code1=tuple(roundq(v,Q) for v in f1)
        assert code0==code1
        margin=min(abs(v-F(2*k+1,2*Q)) for v in f0+f1 for k in range(Q))
        assert margin>=F(1,3744*Q)
        certs.append({'M':M,'h':h,'roots_with_duplicates':len(roots),'p0':str(p0),'p1':str(p1),'margin':str(margin),'codeword':code0})
out['certified_cells']=certs
# All numerical constants certified without floating-point exp/sqrt/log.
C=500000000
assert C>30*3744**2
assert sum(F(6**i,factorial(i)) for i in range(11))>384
assert 9*F(66,64)<10
assert F(1,56)<F(1,16)
assert C<25000**2
assert F(1,1248)>F(1,1600000)
assert 131072+536088==667160
out['constant_inequalities']=True
# Rounding expectation is not expectation of rounding (small exact witness).
M=1;p=F(1,8);Q=1;coord=0
mean_rounded=sum(p**sum(x)*(1-p)**(M+2-sum(x))*roundq(F(counts(x)[coord],M),Q) for x in product((0,1),repeat=M+2))
rounded_mean=roundq(means(M,p)[coord],Q)
assert mean_rounded!=rounded_mean
out['noncommutation_witness']={'M':M,'p':str(p),'Q':Q,'coordinate':'J00/M','E_rounded':str(mean_rounded),'rounded_E':rounded_mean}
out['status']='PASS_EXACT_FINITE_DIAGNOSTICS_NOT_THEOREM_PROOF'
print(json.dumps(out,indent=2,sort_keys=True))
