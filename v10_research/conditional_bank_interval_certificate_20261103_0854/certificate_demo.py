#!/usr/bin/env python3
"""Deterministic exact rational interval demo. No NumPy, random calls, or external writes.

Taylor exp and log bounds are proved in the adjacent research note. The 1/1000
actual-implementation error is a conditional premise, NOT a measured error.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial

N=50

def exp_pos(x):
    assert x>=0
    k=0
    while x>Q(1,2):
        x/=2; k+=1
    terms=[x**j/factorial(j) for j in range(N+1)]
    lower=sum(terms,Q(0)); first=x**(N+1)/factorial(N+1)
    upper=lower+first/(1-x/Q(N+2))
    return lower**(2**k),upper**(2**k)

def expq(x):
    if x>=0:return exp_pos(x)
    a,b=exp_pos(-x);return 1/b,1/a

def tanh_bounds(x):
    a,b=expq(2*x)
    return (a-1)/(a+1),(b-1)/(b+1)

def log_unit_bounds(x):
    assert 1<=x<=2
    y=(x-1)/(x+1)
    lo=2*sum((y**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    return lo,lo+2*y**(2*N+1)/(Q(2*N+1)*(1-y*y))

def logq(x):
    assert x>0
    if x<1:
        a,b=logq(1/x); return -b,-a
    k=0
    while x>2: x/=2; k+=1
    a,b=log_unit_bounds(x); c,d=log_unit_bounds(Q(2))
    return a+k*c,b+k*d

def score_bounds(x):
    # One active hidden unit: r=tanh(x). q=1/16+(7/8)*sigmoid(r).
    rl,rh=tanh_bounds(x)
    al,ah=expq(-rh); bl,bh=expq(-rl)
    ql=Q(1,16)+Q(7,8)/(1+ah)
    qh=Q(1,16)+Q(7,8)/(1+bl)
    # q in [ql,qh]; log monotone. Endpoint interval arithmetic deliberately
    # makes no cancellation or derivative assumption.
    lql,lqh=logq(ql)[0],logq(qh)[1]
    l1l,l1h=logq(1-qh)[0],logq(1-ql)[1]
    return -Q(1,4)*lqh-Q(3,4)*l1h,-Q(1,4)*lql-Q(3,4)*l1l

def bank(word):
    m=len(word)-2;l=m//2;u=word[-2:]
    hits=[(i,word[i+2]) for i in range(m) if word[i:i+2]==u]
    return (len(hits),sum(b for i,b in hits),
            sum(i<l for i,b in hits),sum(b for i,b in hits if i<l))

h=(0,0,0,0); words=[h]
for (i,) in combinations(range(2),1):
    w=list(h); w[i]^=1; words.append(tuple(w))
records=[]
for w in words:
    J,C,D,E=bank(w); x=Q(J-C,2); L,U=score_bounds(x)
    records.append((w,(J,C,D,E),x,L,U))
assert [r[2] for r in records]==[Q(1),Q(1,2),Q(0)]
assert all(r[4]-r[3]<Q(1,10**20) for r in records)
assert all(records[0][3]-r[4]>Q(189,6400) for r in records[1:])
# This tests an abstract uniformly bounded implementation error, not NumPy.
epsilon=Q(1,1000)
assert all(records[0][3]-r[4]-2*epsilon>Q(881,32000) for r in records[1:])
for w,b,x,L,U in records:
    print('word=', ''.join(map(str,w)), 'bank=',b,'x=',str(x),
          'ideal_CE_approx=',format(float((L+U)/2),'.16g'),
          'rational_interval_width_less_than=1e-20')
print('PASS: exact rational endpoint comparisons imply every competitor gap > 189/6400')
print('PASS: under the hypothetical uniform actual-error premise 1/1000, actual gap > 881/32000')
