#!/usr/bin/env python3
"""Fresh rational finite audit; no candidate imports. Run from any directory."""
from fractions import Fraction as F
from itertools import product
from math import comb, ceil, exp, log, sqrt
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]

def solve(A,b):
    T=[list(row)+[v] for row,v in zip(A,b)]; n=len(b)
    for j in range(n):
        i=next(i for i in range(j,n) if T[i][j]); T[j],T[i]=T[i],T[j]
        d=T[j][j]; T[j]=[v/d for v in T[j]]
        for i in range(n):
            if i!=j:
                d=T[i][j]; T[i]=[v-d*w for v,w in zip(T[i],T[j])]
    return [r[-1] for r in T]

def mat(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def stationary(P):
    reach=[[bool(P[i][j]) or i==j for j in range(4)] for i in range(4)]
    for k in range(4):
        for i in range(4):
            for j in range(4): reach[i][j]|=reach[i][k] and reach[k][j]
    classes={tuple(j for j in range(4) if reach[i][j] and reach[j][i]) for i in range(4)}
    closed=[s for s in classes if all(not P[i][j] for i in s for j in range(4) if j not in s)]
    if len(closed)!=1:return None
    S=closed[0]; n=len(S)
    A=[[P[i][j]-F(i==j) for i in S] for j in S[:-1]]+[[F(1)]*n]
    vals=solve(A,[F(0)]*(n-1)+[F(1)])
    return [vals[S.index(i)] if i in S else F(0) for i in range(4)]

count=dict(kernels=0,positive_certificates=0,zero_support=0,hitting_targets=0,moment_inequalities=0,count_cases=0,floor_cases=0,decoder_cases=0)
maxratio=0.0
for a,b,e,t in product([F(0),F(1,8),F(1,2),F(7,8),F(1)],repeat=4):
    count['kernels']+=1
    P=[[1-a,a,F(0),F(0)],[F(0),F(0),1-b,b],[e,1-e,F(0),F(0)],[F(0),F(0),t,1-t]]
    p=stationary(P)
    if p is None:continue
    S=[i for i in range(4) if p[i]]; P2=mat(P,P)
    beta=min(P2[i][j]/p[j] for i in range(4) for j in S)
    if not beta:continue
    count['positive_certificates']+=1; count['zero_support']+=len(S)<4
    y,x,xx,w=p; assert x==xx and y*a==x*e and w*t==x*b
    assert e*e>=beta*y or not x
    assert b*b>=beta*w or not x
    flip=[0,2,1,3]
    for i in S:
        for j in S:assert p[j]*P[j][i]/p[i]==P[flip[i]][flip[j]]
    for s,q in enumerate([a,F(1),F(1),t]):
        if not p[s] or not q:continue
        U=[i for i in S if i!=s]; A=[[F(i==j)-P[i][j] for j in U] for i in U]
        hits=solve(A,[F(1)]*len(U)); H=max(hits,default=F(0)); h=dict(zip(U,hits)); h[s]=F(0)
        assert beta*(p[s]*q*H)**2<=25
        maxratio=max(maxratio,float(beta*(p[s]*q*H)**2))
        if len(S)==4:
            if s==0:assert [h[i] for i in [1,2,3]]==[(b+2*t)/(e*t),(b+2*t)/(e*t)-b/t-1,(b+2*t)/(e*t)+(1-b)/t-1]
            if s==1:assert [h[i] for i in [0,2,3]]==[1/a,1+e/a,1/t+1+e/a]
        count['hitting_targets']+=1
        Hbar=max(H,1/p[s]); assert beta*(p[s]*q*Hbar)**2<=36
        moms={1:h}
        for m in range(2,5):
            rhs=[1+sum(F(comb(m,k))*sum(P[i][j]*moms[k][j] for j in U) for k in range(1,m)) for i in U]
            vals=solve(A,rhs); moms[m]=dict(zip(U,vals)); moms[m][s]=F(0)
        factorial=1
        for m in range(1,5):
            factorial*=m
            ret=1+sum(F(comb(m,k))*sum(P[s][j]*moms[k][j] for j in U) for k in range(1,m+1))
            if m==1:assert ret==1/p[s]
            assert ret<=factorial*Hbar**(m-1)/p[s]
            assert all(moms[m][i]<=factorial*Hbar**(m-1)*h[i] for i in U)
            count['moment_inequalities']+=1
        # Reversed target is flip(s); conjugacy makes this forward law equivalent.
        ss=flip[s]; dist={(ss,0):F(1)}
        for M in range(1,33):
            nxt={}
            for (i,n),v in dist.items():
                for j in S:
                    if P[i][j]:nxt[j,n+(j==ss)]=nxt.get((j,n+(j==ss)),F(0))+v*P[i][j]
            dist=nxt
            if M not in [1,2,7,32]:continue
            mu=M*p[s]; tail=sum(v for (i,n),v in dist.items() if n<mu/16)
            assert float(tail)<=2*exp(-sqrt(float(beta))*float(mu*q)/48)+1e-14
            for amp in [F(1,100),F(1),F(100)]:
                val=sum(v*min(q,amp/(n+2)) for (i,n),v in dist.items())
                rhs=float(amp/mu)*(17+log(1+96/(sqrt(float(beta))*float(amp))))
                assert float(val)<=rhs+1e-12
                count['count_cases']+=1

for d in range(1,65):
    for n in range(d+1):
        ph=F(n,d)
        for L in [F(i,7) for i in range(1,141)]:
            n0=(L*(1-ph)).__floor__(); n1=(L*ph).__floor__(); N=n0+n1
            if not N:continue
            err=abs(F(n1,N)-ph)
            assert err<=min(ph,1-ph) and err<=min(1,2/L)
            for q in [F(0),F(1,8),F(1,2),F(1)]:assert err<=min(q,2/L)+abs(ph-q)
            count['floor_cases']+=1
for M,Q,kappa in product([1,2,64,65,1000],[16,32,256],[1,2,17,10000]):
    z=kappa*Q
    for J in range(1,M+1):
        r=F(kappa*J,M+(kappa-1)*J)
        assert 2/(Q*r)<=F(2,Q)+F(6*M,z*(J+2))
        if Q*r<2:assert J<F(4*M,z)
        count['decoder_cases']+=1
result={'status':'PASS','counts':count,'largest_exact_squared_hitting_ratio_float':maxratio,'exact_arithmetic':'Fraction for kernels, all-state certificate, hitting equations, moments, floors, decoder algebra; transcendental tail/BU1 checks numerical only','limitations':'Finite diagnostic corroboration, not proof or external review.'}
path=ROOT/'reviews/BU001_independent_checks_v1.json'; path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
