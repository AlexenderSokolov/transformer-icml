#!/usr/bin/env python3
"""Exact signed full-product finite-affine diagnostics; not formal verification."""
from fractions import Fraction as F
from pathlib import Path
import json,itertools
from GN001_independent_geometry import curve,edges,dist2
class Finite:
    def __init__(self,P):self.D=1<<P;self.ops=0
    def rho(self,x):return F((x*self.D).__floor__(),self.D)
    def aff(self,b,*terms):
        self.ops+=1
        return self.rho(self.rho(b)+sum(self.rho(a)*x for a,x in terms))
    def rel(self,x):return max(F(0),x)
    def clip(self,x):return min(F(1),max(F(0),x))
    def tent(self,x,extended=False):
        z=self.rel(self.aff(-F(1,2),(1,x)))
        if extended:
            zz=self.rel(self.aff(-1,(1,x)))
            return self.aff(0,(2,x),(-4,z),(4,zz))
        return self.aff(0,(2,x),(-4,z))
    def iterate(self,x,k):
        for _ in range(k):x=self.tent(x)
        return x
    def minimum(self,x,y):return self.aff(0,(1,x),(-1,self.rel(self.aff(0,(1,x),(-1,y)))))
    def run(self,t,N,j):
        if j==1:return (t,)
        k=N.bit_length()-1;L=N**(j-1);eta=F(1,2*L+2)
        a=self.iterate(t,k+1)
        b=self.iterate(self.tent(self.aff(F(1,4*N),(1,t)),True),k)
        z=self.rel(self.aff(F(1,2),(-1,b)))
        for _ in range((j-1)*k):z=self.clip(self.aff(0,(2,z)))
        z=self.minimum(self.aff(1,(-1,a)),z)
        s=self.aff(0,(F(1,2),a),(1,z))
        stair=self.aff(0,(1,t),(-F(1,N),s))
        v=self.iterate(self.tent(self.aff(eta/(2*N),(1,t)),True),k-1)
        u=self.clip(self.aff(-eta/(2*(1-eta)),(1/(1-eta),v)))
        return self.run(u,N,j-1)+(stair,)
def nearest(q,es):
    candidates=[]
    for a,b,x,y in es:
        axis=next(i for i,(u,v) in enumerate(zip(x,y)) if u!=v)
        lo,hi=sorted((x[axis],y[axis]));z=list(x);z[axis]=min(hi,max(lo,q[axis]));z=tuple(z)
        r=(z[axis]-x[axis])/(y[axis]-x[axis]);candidates.append((dist2(q,z),a+(b-a)*r))
    return min(enumerate(candidates),key=lambda a:(a[1][0],a[0]))[1][1]
def main():
    reports=[]
    for N,J in [(2,2),(2,3),(2,4),(4,2),(4,3),(8,2)]:
        # Here 16 is a diagnostic precision choice, NOT a proved universal c_FA.
        # The all-history theorem constructs c_FA from actual fixed primitive bounds.
        h=8;Q=1<<h;k=N.bit_length()-1;d=30*J*J*(k+1);P=4*h+16*(d+2)
        es=edges(N,J);count=noise=0;maxerr=F(0);maxops=0
        xs={F(a,19) for a in range(20)}|{e[0] for e in es}|{e[1] for e in es}
        for x in xs:
            f=Finite(P);actual=tuple(f.clip(z) for z in f.run(f.rho(x),N,J));ideal=curve(x,N,J)
            err=max(abs(a-b) for a,b in zip(actual,ideal));assert err<=F(1,Q)
            assert f.ops<=d
            maxerr=max(maxerr,err);maxops=max(maxops,f.ops);count+=1
            for signs in itertools.product([-1,1],repeat=J):
                q=tuple(F((Q*min(F(1),max(F(0),a+F(s,Q)))).__floor__(),Q) for a,s in zip(actual,signs))
                recovered=nearest(q,es)
                # c=1 -> K^2=8 J (c+2)^2; exact squared comparison.
                assert (recovered-x)**2<=F(8*J*9,Q*Q*N**(2*(J-1)))
                noise+=1
        reports.append(dict(N=N,J=J,h=h,d_bound=d,max_scalar_affines=maxops,P=P,inputs=count,adversarial_corner_checks=noise,uniform_precut_pass=True,robust_inverse_pass=True,error_strictly_below_grid=maxerr<F(1,Q)))
    conversion=[]
    for P in [0,1,4,9]:
        f=Finite(P)
        for a in range(-19,20):
            for b in range(1,24):
                x=F(a,b);y=f.rho(x);assert 0<=x-y<F(1,1<<P)
        conversion.append(dict(P=P,cases=39*23,pass_all=True))
    out=dict(status='PASS',scope='Finite exact diagnostics, not a universal proof; generic GD theorem supplies uniform all-history guarantee',rational_signed_conversion=conversion,cases=reports)
    Path(__file__).with_name('GN001_finite_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
