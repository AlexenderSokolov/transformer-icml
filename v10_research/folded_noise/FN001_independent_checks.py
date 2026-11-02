"""Independent exact count-law and fine-grid diagnostics; not a proof substitute."""
from fractions import Fraction as F
from math import comb, exp
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def labels(A,M,h,J,P,delta):
    D=2**P; Q=2**h
    u=D*A//M
    assert F(u,D)==F(A,M)
    rails=[u]
    for j in range(J-1):
        for _ in range(h): u=2*min(u,D-u)
        rails.append(u)
    v=rails.copy()
    if abs(F(v[0],D)-F(1,2))<=delta: v[0]=D//2
    assert all(abs(F(a-b,D))<=delta for a,b in zip(rails,v))
    return tuple(Q*a//D for a in v),rails

def law(M,p,h,J,P,delta,side):
    ans={}
    # Endpoint patterns enumerated explicitly, not dropped from observations.
    patterns=[()] if not side else [(0,0),(0,1),(1,0),(1,1)]
    for s in patterns:
        r=len(s); k=sum(s); w=p**k*(1-p)**(r-k)
        for b in range(M-r+1):
            pr=w*comb(M-r,b)*p**b*(1-p)**(M-r-b)
            key=(labels(b+k,M,h,J,P,delta)[0],s)
            ans[key]=ans.get(key,F(0))+pr
    assert sum(ans.values())==1
    return ans

collision_cases=0; law_cases=0; min_margin=None
for m in range(1,8):
    M=2**m
    for h in range(1,4):
      for J in range(2,5):
       P=max(m,J*h)
       for delta in [F(1,2),F(1,4),F(1,8),F(1,4*2**h)]:
        for A in range(M+1):
            left,rails=labels(A,M,h,J,P,delta)
            right,other=labels(M-A,M,h,J,P,delta)
            assert rails[1:]==other[1:]
            if abs(F(A,M)-F(1,2))<=delta: assert left==right
            collision_cases+=1
        if m>5: continue
        p=F(1,2)+delta/2
        for side in [False,True]:
            r=2 if side else 0
            L=law(M,p,h,J,P,delta,side); R=law(M,1-p,h,J,P,delta,side)
            overlap=sum(min(v,R.get(k,F(0))) for k,v in L.items())
            w=(p*(1-p))**(r//2)
            conditional=sum(F(comb(M-r,b))*p**b*(1-p)**(M-r-b)
                            for b in range(M-r+1)
                            if abs(F(b+r//2,M)-F(1,2))<=delta)
            coupled=w*conditional
            assert overlap>=coupled
            assert float(conditional)+1e-14>=max(0,1-2*exp(-float(M*delta**2)/2))
            law_cases+=1
# Preserve explicit non-admitted rounding failure.
M=3; P=2; A=1; D=2**P
assert D*A//M + D*(M-A)//M == D-1
out={'status':'PASS','collision_cases':collision_cases,'exact_observation_law_cases':law_cases,
     'retained_side_observations':'all four exact terminal pairs; fixed initial bits identical',
     'finite_rounding_counterexample':{'M':3,'P':2,'A':1,'fine_numerators':[1,2],'sum':3,'required_sum':4},
     'theorem_sha256':hashlib.sha256((ROOT/'FN001_theorem.md').read_bytes()).hexdigest(),
     'limitations':'Exact finite diagnostics only; Hoeffding numerical checks are supplemental, not proof.'}
(ROOT/'FN001_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
