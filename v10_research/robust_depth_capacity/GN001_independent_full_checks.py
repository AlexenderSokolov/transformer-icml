#!/usr/bin/env python3
"""Exact finite checks of rational conversion, affine bound, bootstrap and choice of N."""
from fractions import Fraction as F
from pathlib import Path
import json

def rho(x,p):return F((x.numerator*(1<<p))//x.denominator,1<<p)
def main():
    conversion=affine=bootstrap=capacity=0
    for p in range(1,17):
        eps=F(1,1<<p)
        for a in range(-37,38):
            for b in range(1,34):
                x=F(a,b); y=rho(x,p)
                assert 0<=x-y<eps
                conversion+=1
        # Exact affine full-product/single-floor primitive with signed coefficient and bias conversion.
        for a in [F(-13,7),F(-1,3),F(2,7),F(4)]:
            for x in [F(-5,7),F(-1,3),F(0),F(2,3),F(1)]:
                for b in [F(-5,11),F(1,6)]:
                    xf=rho(x,p); af=rho(a,p); bf=rho(b,p)
                    yf=rho(af*xf+bf,p); ideal=a*x+b
                    eta=abs(xf-x); bound=abs(a)*eta+eps*(abs(x)+eta)+2*eps
                    assert abs(yf-ideal)<=bound
                    affine+=1
    for A in [2,3,8,64,1000]:
        c=4
        while A*(c+5)*F(2)**(1-c)>1:c+=1
        for d in range(1,101):
            for h in range(1,17):
                P=4*h+c*(d+2)
                assert A**(d+2)*(P+1)*F(2)**(-P)<=F(1,1<<h)
                bootstrap+=1
    for J in range(2,6):
        for c in [0,1,3]:
            B2=16*J*(c+2)**2
            kappasquared=(4*B2)**(J-1)
            for h in range(1,13):
                Q=1<<h
                for M in list(range(1,501))+[10**r for r in range(3,19)]:
                    if Q**(2*J)<kappasquared*M:continue
                    if Q*Q>=M:
                        capacity+=1;continue
                    N=2
                    while Q*Q*N**(2*(J-1))<M:N*=2
                    assert N*N*B2<=Q*Q
                    assert Q*Q*N**(2*(J-1))>=M
                    # log2 N < 1 + log2(sqrt(M)/Q)/(J-1), squared integer equivalent.
                    assert (N//2)**(2*(J-1))*Q*Q<M
                    capacity+=1
    out=dict(status='PASS',arithmetic='exact Fraction and integers',signed_rational_conversions=conversion,affine_error_bounds=affine,uniform_bootstrap_checks=bootstrap,capacity_choice_checks=capacity,scope='Finite diagnostics, not exhaustive network verification')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
