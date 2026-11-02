#!/usr/bin/env python3
"""Finite exact diagnostics for RESC_binary_lemma; not formal verification."""
from fractions import Fraction as F
from itertools import product, combinations
from math import isqrt, sqrt
import hashlib, json, pathlib, random, time
BASE=pathlib.Path(__file__).resolve().parent

def compand(x,L):
    u=x;v=F(0)
    for j in range(L):
        old=u
        u=min(F(1),4*old)
        v+=F(1,2**j)*max(F(0),old-F(1,4))
    return v+F(1,2**L)*u

def inverse(z,L):
    points=sorted(set([F(0),F(1)]+[F(1,4**j) for j in range(L+1)]))
    for a,b in zip(points,points[1:]):
        ga,gb=compand(a,L),compand(b,L)
        if ga<=z<=gb:
            return a+(z-ga)*(b-a)/(gb-ga)
    raise AssertionError((z,L))

def upper_root(z,eps):
    if not eps:return F(0)
    p=0
    while F(1,2**p)>eps:p+=1
    num=z.numerator*2**(2*p);den=z.denominator
    j=isqrt(num//den)
    if j*j*den<num:j+=1
    ans=F(j,2**p)
    assert ans*ans>=z
    assert ans==0 or (ans-F(1,2**p))**2<z
    return ans

def row(word):
    target=word[-2:]
    out=[0,0]
    for i in range(len(word)-2):
        if word[i:i+2]==target:out[word[i+2]]+=1
    return out

def all_hist(word):
    h=[0]*8
    for i in range(len(word)-2):
        a,b,c=word[i:i+3];h[4*a+2*b+c]+=1
    return h

checks=0;histories=0;max_mass_ratio=0.;max_radius_ratio=0.;worst=None
start=time.time()

def check(word,corrupted,k,eps,L,signs):
    global checks,max_mass_ratio,max_radius_ratio,worst
    M=len(word)-2;eta=F(k,M);chi=2**L
    assert word[-2:]==corrupted[-2:]
    clean=row(word);edited=row(corrupted)
    x=[F(v,M) for v in clean];xp=[F(v,M) for v in edited]
    top=compand(F(1),L)
    y=[inverse(min(top,max(F(0),compand(v,L)+sgn*eps)),L) for v,sgn in zip(xp,signs)]
    for v,yp in zip(xp,y):
        assert abs(float(yp-v))<=4*float(eps)*sqrt(float(v))+4*float(eps*eps)+2*float(eps/chi)+1e-12
    d=sum(abs(a-b) for a,b in zip(x,y));r=sum(x);rhat=sum(y)
    tau=eta+eps*eps+eps/chi
    S=upper_root(rhat,eps)
    Bhat=12*eps*S+68*tau
    assert d<=Bhat,(word,corrupted,k,eps,L,signs,d,Bhat)
    if tau or eps:
        massbound=6*float(eps)*sqrt(float(r))+16*float(tau)
        radiusbound=18*float(eps)*sqrt(float(r))+132*float(tau)
        assert float(d)<=massbound+1e-12
        assert float(Bhat)<=radiusbound+1e-12
        if massbound:max_mass_ratio=max(max_mass_ratio,float(d)/massbound)
        if radiusbound:max_radius_ratio=max(max_radius_ratio,float(Bhat)/radiusbound)
    designated=1-word[-2];C=clean[designated];J=sum(clean)
    B=M*Bhat;tildeC=M*y[designated];tildeJ=M*rhat
    qhat=max(F(0),tildeC-B)/(tildeJ+B+2)
    assert F(0)<=qhat<=F(C,J+2)
    assert F(C,J+2)-qhat<=4*B/(J+2)
    p=F(C,J) if J else F(0)
    A=528*M*tau+2
    for q in [F(0),F(1,100),F(1,2),F(99,100),F(1)]:
        cleanerr=abs(p-q) if J else F(0)
        exact=2*cleanerr+min(q,(4*B+2)/(J+2))
        assert abs(qhat-q)<=exact
        split=2*float(cleanerr)+72*float(eps)*sqrt(M)/sqrt(J+2)+float(min(q,A/(J+2)))
        assert float(abs(qhat-q))<=split+1e-12
    checks+=1

# Exhaust every short binary history and <=2 edits (including adjacency), preserve final pair.
M=4
for word in product(range(2),repeat=M+2):
    hist=all_hist(word)
    for used in range(3):
        for mask in combinations(range(M),used):
            edited=list(word)
            for i in mask:edited[i]^=1
            edited=tuple(edited)
            assert sum(abs(a-b) for a,b in zip(hist,all_hist(edited)))<=6*used
            histories+=1
            for eps in [F(0),F(1,64),F(1,4)]:
                for L in [0,2]:
                    for signs in ([(0,0)] if not eps else product([-1,0,1],repeat=2)):
                        check(word,edited,used,eps,L,signs)
# Actual theorem domain: random long histories and edited words, including zero and full budgets.
rng=random.Random(202611021140)
for it in range(500):
    M=rng.choice([64,65,127,256])
    word=tuple(rng.randrange(2) for _ in range(M+2))
    k=rng.choice([0,1,2,M//3,M])
    used=rng.randrange(k+1)
    edited=list(word)
    for i in rng.sample(range(M),used):edited[i]^=1
    edited=tuple(edited);histories+=1
    eps=rng.choice([F(0),F(1,1024),F(1,64),F(1,8),F(1),F(3)])
    L=rng.choice([0,1,2,4,8]);signs=(rng.choice([-1,0,1]),rng.choice([-1,0,1]))
    check(word,edited,k,eps,L,signs)

sources=['RESC_binary_lemma.md','check_resc_binary_lemma.py']
report={'status':'PASS','meaning':'Exact finite algebra and actual compander perturbation diagnostics, not formal verification or an expected-risk test.',
        'row_reconstructions_checked':checks,'clean_edited_word_pairs':histories,
        'exhaustive_short_horizon':4,'random_theorem_domain_cases':500,
        'max_observed_clean_row_bound_ratio':max_mass_ratio,'max_observed_radius_upper_bound_ratio':max_radius_ratio,
        'sqrt_implementation':'Exact squared-integer comparisons; confidence/envelope algebra checked using Fraction.',
        'elapsed_seconds':time.time()-start,
        'sha256':{s:hashlib.sha256((BASE/s).read_bytes()).hexdigest() for s in sources}}
(BASE/'RESC_binary_lemma_diagnostics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
