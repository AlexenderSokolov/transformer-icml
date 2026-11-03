"""Finite exact gate probability checks; corroboration, not theorem proof."""
from fractions import Fraction as F
import json, math
out=[]
for M in [64,65,66,72,96,120,192]:
    a=F(1,M); b=1-a; H=M//2
    p=F(0); count=0
    for t in range(H,M-2):
        states=[(1,1)]*t
        cyc=[(1,0),(0,0),(0,1)]
        states += [cyc[(i-t)%3] for i in range(t,M+1)]
        u=states[M]
        J=sum(v==u for v in states[:M]); D=sum(v==u for v in states[:H])
        if (M-t)%3 in [0,1]:
            assert u in [(1,0),(0,0)] and J>0 and D==0
            assert not (J>0 and 512*D>=J)
            count+=1;p+=a*b**(t-1)
    assert count>=M/4
    assert float(p)>=1/(4*math.e)
    closed=None
    if M%6==0:
        n=M//6
        closed=a/(1-b**3)*(b**(3*n-1)*(1-b**(3*n))+b**(3*n+1)*(1-b**(3*n-3)))
        assert p==closed
    empirical=a*(b**M+b**(M-1)+b**(M-2))
    assert empirical<=3*a
    out.append(dict(M=M,qualifying_exits=count,gate_risk_lower=float(p),empirical_risk=float(empirical),closed_form_checked=closed is not None))
print(json.dumps(dict(status='PASS',checks=out,limiting_gate_risk=(2/3)*(math.exp(-.5)-math.exp(-1))),indent=2))
