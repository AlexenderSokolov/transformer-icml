#!/usr/bin/env python3
"""Exact rational finite diagnostics for NP001; not a uniform proof."""
from fractions import Fraction as F
from pathlib import Path
import sys,json,itertools,hashlib
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'robust_depth_capacity'))
from GN001_independent_geometry import curve,edges
from check_gn001_finite import Finite,nearest

def scale(tau):
    m=1
    while F(1,2**(m+1))>=tau:m+=1
    return m,F(1,2**m)
def quant(x,Q):return F((Q*min(F(1),max(F(0),x))).__floor__(),Q)
def main():
    attacks=selectors=0;reports=[]
    for h in range(1,11):
        Q=2**h
        for delta in [F(0),F(1,4*Q),F(1,Q),F(3,2*Q),F(1,17),F(1,4)]:
            if delta>F(1,4):continue
            tau=max(F(1,Q),delta);m,t=scale(tau)
            assert tau<=t<2*tau and 1<=m<=h
            if delta:
                outputs=set()
                for i in range(258):
                    a=F(i,257);k=(a/delta).__floor__();z=delta*k
                    assert 0<=a-z<delta and 0<=z<=1
                    assert quant(z,Q)==quant(delta*k,Q)
                    outputs.add(quant(z,Q));attacks+=1
                assert len(outputs)<= (1/delta).__floor__()+1
            for J in [2,3,4,7]:
                D=12*J;kap=2**J*(2*D)**(J-1)
                for M in [1,2,17,2**10,2**20,2**40]:
                    # Exact squared comparison of effective-capacity condition.
                    if tau**(-2*J)<kap**2*M:continue
                    if t*t*M<=1:
                        assert (3*t)**2<=F(9,M)
                    else:
                        k=1
                        while F(2**(2*k*(J-1)))<t*t*M:k+=1
                        N=2**k
                        assert N*D*t<=1
                        assert (t/N**(J-1))**2<=F(1,M)
                    selectors+=1
    # Noise independent of Q: same delta at different h, and non-Q-grid attacks.
    for N,J,h,delta in [(2,2,8,F(1,100)),(2,2,10,F(1,100)),(4,2,10,F(1,257)),(2,3,10,F(1,211)),(2,3,8,F(0))]:
        Q=2**h;tau=max(F(1,Q),delta);m,t=scale(tau);D=12*J
        assert N*D*t<=1
        es=edges(N,J);d=30*J*J*(N.bit_length());P=4*h+16*(d+2)
        xs={F(i,13) for i in range(14)}|{e[0] for e in es}|{e[1] for e in es}
        count=0
        for x in xs:
            f=Finite(P);actual=tuple(f.clip(z) for z in f.run(f.rho(x),N,J));ideal=curve(x,N,J)
            assert max(abs(a-b) for a,b in zip(actual,ideal))<=F(1,Q)
            assert f.ops<=d
            for signs in itertools.product([-1,0,1],repeat=J):
                q=tuple(quant(a+sign*delta,Q) for a,sign in zip(actual,signs))
                out=nearest(q,es)
                assert (out-x)**2<=72*J*tau*tau/N**(2*(J-1))
                count+=1
            if delta:
                q=tuple(quant(delta*(a/delta).__floor__(),Q) for a in actual)
                assert (nearest(q,es)-x)**2<=72*J*tau*tau/N**(2*(J-1))
                count+=1
        reports.append(dict(N=N,J=J,Q=Q,delta=str(delta),Q_delta=str(Q*delta),tau=str(tau),t=str(t),P=P,inputs=len(xs),attacks_checked=count))
    out=dict(status='PASS',scope='Finite rational diagnostics only, inherited independently checked GN geometry and explicit finite evaluator; not uniform proof',coarse_attack_scalar_cases=attacks,exact_statistical_selection_cases=selectors,finite_encoder_cases=reports)
    (HERE/'NP001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
