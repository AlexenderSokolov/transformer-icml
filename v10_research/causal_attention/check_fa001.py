#!/usr/bin/env python3
"""FA001 exact-integer diagnostics; not a formal proof."""
from decimal import Decimal, localcontext
from fractions import Fraction
import json
from pathlib import Path

def dec(x):
    if isinstance(x,Fraction): return Decimal(x.numerator)/Decimal(x.denominator)
    return Decimal(x)
def grid(x,D): return (x.numerator*D)//x.denominator

def weight(S,D,a,P):
    A=2*a; J=8*A*A+2+P
    t=D; W=D
    for j in range(1,J+1):
        t=(t*S)//(j*D); W+=t
    return W,J

def head(xs,t,P,branch,masked=True):
    D=1<<P; a=3
    # q=.5*x+.25; k=.25*x-.25; v=.75*x-.5, exact affine microsteps.
    aff=lambda X,c,b:(grid(c,D)*X+D*grid(b,D))//D
    q=aff(xs[t],Fraction(1,2),Fraction(1,4))
    den=num=0
    keys=[i for i in range(t+1) if not masked or t<2 or i>=1]
    for i in keys:
        k=aff(xs[i],Fraction(1,4),Fraction(-1,4))
        v=aff(xs[i],Fraction(3,4),Fraction(-1,2))
        score=(q*k)//D
        W,_=weight(score+a*D,D,a,P)
        den+=W; num+=W*v
    assert den>=len(keys)*D
    return num//den

def finite(seq,P,branch,masked):
    D=1<<P
    xs=[grid(Fraction(x,2)+Fraction(branch,8),D) for x in seq]+[0]
    for _ in range(2):
        os=[head(xs,t,P,branch,masked) for t in range(len(xs))]
        # x' = .25*x + .5*ReLU(o+.5) -.125.
        xs=[(grid(Fraction(1,4),D)*x+grid(Fraction(1,2),D)*max(0,o+D//2)-D*(D//8))//D for x,o in zip(xs,os)]
    return Decimal(xs[-1])/D

def ideal(seq,branch,masked):
    xs=[Decimal(x)/2+Decimal(branch)/8 for x in seq]+[Decimal(0)]
    for _ in range(2):
        out=[]
        for t,x in enumerate(xs):
            keys=[i for i in range(t+1) if not masked or t<2 or i>=1]
            q=x/2+Decimal(1)/4
            ws=[(q*(xs[i]/4-Decimal(1)/4)).exp() for i in keys]
            o=sum(w*(Decimal(3)*xs[i]/4-Decimal(1)/2) for i,w in zip(keys,ws))/sum(ws)
            out.append(x/4+max(Decimal(0),o+Decimal(1)/2)/2-Decimal(1)/8)
        xs=out
    return xs[-1]

def main():
    report={'status':'PASS','scope':'exact-integer diagnostic only; not independent proof acceptance'}
    with localcontext() as ctx:
        ctx.prec=100
        cases=0; max_ratio=Decimal(0)
        for P in [4,8,16,32]:
            D=1<<P; a=2; A=2*a; H=3**A
            for S in [0,1,D//3,D,3*D,4*D]:
                W,J=weight(S,D,a,P); exact=(Decimal(S)/D).exp()
                err=exact-Decimal(W)/D
                assert W>=D and err>=-Decimal('1e-90')
                bound=Decimal(H*J+1)/D
                assert err<=bound
                cases+=1
        report['exp_cases']=cases
        # General signed-value ratio lemma, using exact rational arithmetic.
        ratios=0
        for m in [1,2,7,97,1000]:
            wi=[Fraction(2+(i%3)) for i in range(m)]
            wh=[w+Fraction((-1)**i,16) for i,w in enumerate(wi)]
            vi=[Fraction((i%7)-5,3) for i in range(m)]
            vh=[v-Fraction(1,32) for v in vi]
            oi=sum(w*v for w,v in zip(wi,vi))/sum(wi)
            of=sum(w*v for w,v in zip(wh,vh))/sum(wh)
            assert abs(of-oi)<=Fraction(1,32)+2*Fraction(5,3)*Fraction(1,16)
            # Exact finite normalization and signed-floor error.
            D=256; W=[int(w*D) for w in wh]; V=[grid(v,D) for v in vh]
            N=sum(w*v for w,v in zip(W,V)); Z=sum(W); O=N//Z
            assert 0<=Fraction(N,Z*D)-Fraction(O,D)<Fraction(1,D)
            assert Z>=m*D
            ratios+=1
        report['signed_ratio_keycounts']=[1,2,7,97,1000]
        network=[]
        for P in [8,16,24]:
            worst=Decimal(0)
            for n in [1,2,7,31]:
                seq=[((i*7+i//3)%3)-1 for i in range(n)]
                for branch in [0,1]:
                    for masked in [False,True]:
                        err=abs(finite(seq,P,branch,masked)-ideal(seq,branch,masked))
                        worst=max(worst,err)
                        # A generous local diagnostic envelope, not proof constant C_*.
                        assert err<=Decimal(100*(P+1))/(1<<P)
            network.append({'P':P,'max_abs_error':str(worst),'max_error_in_grid_units':str(worst*(1<<P))})
        report['two_layer_signed_network']=network
        report['network_cases']=3*4*2*2
        # Verify constructive precision inequality for representative large constants.
        choices=[]
        for Cstar in [1,10,10**6,10**30]:
            C=1
            while Cstar*(C+5)>(1<<C): C+=1
            for h in range(101):
                P=4*h+C
                assert Cstar*(P+1)*(1<<h)<=(1<<P)
            choices.append({'C_star':str(Cstar),'C_arch':C})
        report['precision_choices']=choices
    target=Path(__file__).with_name('FA001_diagnostic.json')
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__': main()
