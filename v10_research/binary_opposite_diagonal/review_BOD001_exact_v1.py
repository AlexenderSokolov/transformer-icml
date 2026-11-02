#!/usr/bin/env python3
"""Independent exact rational diagnostics, not a proof by testing."""
from fractions import Fraction as F
from itertools import product
import json, hashlib
from pathlib import Path
D=Path(__file__).resolve().parent
stats={"kernels":0,"positive_certificates":0,"density_checks":0,"count_checks":0,"trace_checks":0,"convolution_checks":0,"potential_checks":0,"survival_checks":0}
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def ident(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def dist(P,start,N):
    v={(start,0):F(1)}; out=[]
    for n in range(N+1):
        out.append(v)
        w={}
        for (i,j),u in v.items():
            for k,p in enumerate(P[i]):
                if p:w[k,j+(i==3)]=w.get((k,j+(i==3)),F(0))+u*p
        v=w
    return out
def exp_lower(x):
    # Odd Taylor polynomial is a global lower bound for exp(-x), x>=0,
    # by the signed integral remainder. Here x<=1 gives positive values.
    z=s=F(1)
    for j in range(1,32):z*= -x/j;s+=z
    assert s>0
    return s
N=24
cases=list(product([F(1,8),F(1,2),F(7,8)],repeat=4))
cases += [(F(1),F(1),F(1),F(1)),(F(1),F(1,8),F(1),F(1,2)),(F(1,1000),F(1,2),F(1,2),F(1,1000)),(F(1,2),F(1,1000),F(1,1000),F(1,2))]
max_beta_hit=F(0);max_density_ratio=F(0)
for a,b,e,t in cases:
    stats['kernels']+=1
    P=[[1-a,a,F(0),F(0)],[F(0),F(0),1-b,b],[e,1-e,F(0),F(0)],[F(0),F(0),t,1-t]]
    Z=e*t+2*a*t+a*b;pi=[e*t/Z,a*t/Z,a*t/Z,a*b/Z]
    P2=mm(P,P);beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4))
    assert mm([pi],P)[0]==pi
    rho=b+e-b*e;m=(rho+a*(2-b))/(a*b);lam=1/m
    h=[m,m-1/a,m+1+(e-1)/a,F(0)];H=max(h)
    assert m>=2 and m<=H<=m+1<=2*m and lam<=b<=rho
    for i in range(4):
        assert sum(P[i][j]*h[j] for j in range(4))-h[i]==-1+(1/pi[3] if i==3 else 0)
        stats['potential_checks']+=1
    if beta>0:
        stats['positive_certificates']+=1
        assert b*b>=beta*pi[3]
        assert beta*(pi[3]*t*H)**2<=25
        max_beta_hit=max(max_beta_hit,beta*(pi[3]*t*H)**2)
    # Killed row-vector calculation, independent of recurrence implementation.
    Q=[row[:3] for row in P[:3]]
    v=[F(1),F(0),F(0)];killed=[v];density=[F(0)]
    for n in range(1,N+1):
        density.append(v[1]*b);v=mm([v],Q)[0];killed.append(v)
        recurrence=F(0) if n<2 else a*b*sum(((1-rho)**j*killed[n-2-2*j][0] for j in range((n-2)//2+1)),F(0))
        assert density[n]==recurrence
        lb=exp_lower(lam*n/16)
        assert density[n]<=12*lam*lb
        max_density_ratio=max(max_density_ratio,density[n]/(12*lam*lb))
        stats['density_checks']+=1
    # Exact rational stronger survival envelope against rigorous exp lower bound.
    for initial in range(3):
        v=[F(i==initial) for i in range(3)]
        for n in range(N+1):
            assert sum(v)<=2*exp_lower(lam*n/16)
            stats['survival_checks']+=1
            v=mm([v],Q)[0]
    DW=dist(P,0,N);DC=dist(P,3,N)
    PN=ident(4);QN=ident(3)
    for n in range(1,N+1):
        PN=mm(PN,P);QN=mm(QN,Q)
        recip=sum((p/F(j) for (i,j),p in DC[n].items() if i==3),F(0))
        assert recip==(sum(PN[i][i] for i in range(4))-sum(QN[i][i] for i in range(3)))/n
        assert recip<=F(4,n);stats['trace_checks']+=1
    for A in [F(1,1000),F(1,3),F(2),F(100)]:
        f=[sum((p*min(t,A/(j+2)) for (i,j),p in ds.items() if i==3),F(0)) for ds in DC]
        for n in range(1,N+1):
            goal=sum((p*min(t,A/(j+2)) for (i,j),p in DW[n].items() if i==3),F(0))
            assert goal==sum((density[r]*f[n-r] for r in range(1,n+1)),F(0))
            stats['convolution_checks']+=1
            assert f[n]<=4*A/n
        Vcost=F(0);EV=F(0)
        for (i,j),p in DC[N].items():
            V=j+(i==3);EV+=p*V
            Vcost+=p*sum((min(t,A/(k+2)) for k in range(V)),F(0))
        assert Vcost==sum(f);stats['count_checks']+=1
        hnext=sum((p*sum(P[i][k]*h[k] for k in range(4)) for (i,j),p in DC[N].items()),F(0))
        assert EV==pi[3]*(N+1+hnext)
        assert EV<=pi[3]*(N+1+H)
        if beta>0:assert beta*(t*EV)**2<=100*(1+N*lam)**2
result={"status":"PASS_EXACT_RATIONAL_FINITE_DIAGNOSTICS", "horizon":N,"counts":stats,"max_beta_p_t_H_squared":str(max_beta_hit),"max_density_to_stronger_rational_envelope_ratio":str(max_density_ratio),"method":"Fraction throughout. Exponential envelope tested against strictly smaller rational odd-Taylor lower bound (31 terms). No floating point used. Finite checks do not prove universal claims.","limitations":"Moderate horizons, finite positive rational kernels and several beta-zero endpoint kernels; theorem constants justified by written review, not coverage."}
(D/'review_BOD001_exact_v1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
