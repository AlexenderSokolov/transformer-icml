"""Independent exact diagnostics; no candidate code imports."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json,math
from math import factorial
OUT=Path(__file__).resolve().parent

def bank(word,M):
    j=[0]*4;c=[0]*4;d=[0]*4
    for i in range(M):
        u=2*word[i]+word[i+1]
        j[u]+=1
        c[u]+=word[i+2]==1-word[i]
        d[u]+=i<M//2
    return j+c+d

def means(p,M):
    j=[(1-p)**2,p*(1-p),p*(1-p),p*p]
    c=[p*(1-p)**2,p*p*(1-p),p*(1-p)**2,p*p*(1-p)]
    return j+c+[F(M//2,M)*x for x in j]

def quant(x,Q):
    # Fixed nearest rounding, upward at exact ties.
    return (2*x.numerator*Q+x.denominator)//(2*x.denominator)

sensitivity=[0]*12
expectation_cases=0
for M in range(2,8):
    totals={p:[F(0)]*12 for p in [F(1,8),F(1,5),F(1,4)]}
    for w in product((0,1),repeat=M+2):
        b=bank(w,M)
        for pos in range(M+2):
            v=list(w);v[pos]^=1
            other=bank(v,M)
            sensitivity=[max(z,abs(a-c)) for z,a,c in zip(sensitivity,b,other)]
        for p,total in totals.items():
            prob=p**sum(w)*(1-p)**(len(w)-sum(w))
            for i,x in enumerate(b):total[i]+=prob*x/M
    for p,total in totals.items():
        assert total==means(p,M)
        expectation_cases+=1
assert all(x<=2 for x in sensitivity[:4]+sensitivity[8:])
assert all(x<=3 for x in sensitivity[4:8])

# Exact derivative extrema: J derivatives and the two cubic C derivatives.
# C1'=1-4p+3p² decreases here; C2'=2p-3p² increases here.
a,b=F(1,8),F(1,4)
base_minima=[2*(1-b),1-2*b,1-2*b,2*a,
             1-4*b+3*b*b,2*a-3*a*a,1-4*b+3*b*b,2*a-3*a*a]
derivative_min=min(base_minima+[F(32,65)*x for x in base_minima[:4]])
assert derivative_min>=F(1,12)

# Isolate all roots with rational brackets, choose a certified root-free
# subinterval, and check coordinate margins exactly (no simulation).
cases=[]
for M in [64,65,127,10**10+1]:
  for h in range(7):
    Q=2**h
    brackets=[]
    for coord in range(12):
      left,right=means(a,M)[coord],means(b,M)[coord]
      increasing=right>left
      for k in range(Q):
        t=F(2*k+1,2*Q)
        if not min(left,right)<=t<=max(left,right):continue
        lo,hi=a,b
        for _ in range(50):
          mid=(lo+hi)/2;value=means(mid,M)[coord]
          if (value<t)==increasing:lo=mid
          else:hi=mid
        brackets.append((lo,hi))
    assert len(brackets)<=12*Q
    brackets.sort()
    gaps=[];last=a
    for lo,hi in brackets:
      if lo>last:gaps.append((last,lo))
      last=max(last,hi)
    if last<b:gaps.append((last,b))
    lo,hi=max(gaps,key=lambda z:z[1]-z[0])
    p0=(2*lo+hi)/3;p1=(lo+2*hi)/3
    assert p1-p0>=F(1,312*Q)
    codes=[];margin=F(1)
    for p in [p0,p1]:
      mu=means(p,M)
      codes.append(tuple(quant(x,Q) for x in mu))
      margin=min(margin,min(abs(x-F(2*k+1,2*Q)) for x in mu for k in range(Q)))
    assert codes[0]==codes[1]
    assert margin>=F(1,3744*Q)
    assert p1-p0<=F(1,24)
    cases.append({'M':M,'h':h,'threshold_roots_with_multiplicity':len(brackets),'separation':float(p1-p0),'threshold_margin':float(margin)})
assert F(9*(64+2),64*64)<=F(10,64)
C=500000000
assert C>30*3744**2
assert sum(F(6**i,factorial(i)) for i in range(11))>384
assert F(64,7)*F(1,256)==F(1,28)
assert F(1,56)<F(1,16)
assert 9*64>=4*(64+2)
assert C<25000**2
assert 64*25000==1600000
assert 131072+536088==667160
report={'status':'PASS','risk_constant_checks':'PASS_EXACT','exact_expectation_cases':expectation_cases,'exact_sensitivity_maxima':sensitivity,'exact_minimum_absolute_derivative':str(derivative_min),'rounding_cell_cases':cases,'notes':['Finite checks complement the analytic proof; not a proof over every M,h.','Independent code imports no author implementation.','All mean, derivative, sensitivity and cell-margin assertions use rational arithmetic.']}
(OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','expectation_cases':expectation_cases,'cell_cases':len(cases),'derivative_min':str(derivative_min),'sensitivity':sensitivity}))
