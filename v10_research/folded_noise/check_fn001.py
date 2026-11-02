#!/usr/bin/env python3
"""Finite exact diagnostics only; no replacement for FN001 proof."""
from fractions import Fraction as F
from math import comb, exp
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent

def labels(A,M,h,J,P,delta,attack):
    D=1<<P; Q=1<<h
    U=D*A//M
    us=[U]
    for j in range(1,J):
        for _ in range(h): U=2*min(U,D-U)
        us.append(U)
    if attack and abs(F(us[0],D)-F(1,2))<=delta: us[0]=D//2
    return tuple(Q*u//D for u in us),us

cases=matched=outside=0
for m in range(1,11):
  M=1<<m
  for h in range(1,5):
    for J in (2,3,4):
      P=max(m,J*h)
      for delta in (F(1,4*(1<<h)),F(1,1<<h),F(1,2)):
        for A in range(M+1):
          a,ua=labels(A,M,h,J,P,delta,True)
          b,ub=labels(M-A,M,h,J,P,delta,True)
          clean,uc=labels(A,M,h,J,P,delta,False)
          assert F(uc[0],1<<P)==F(A,M)
          assert ua[1:]==ub[1:]
          assert abs(F(ua[0]-uc[0],1<<P))<=delta
          assert ua[1:]==uc[1:]
          if abs(F(A,M)-F(1,2))<=delta:
            assert a==b; matched+=1
          else:
            assert a==clean; outside+=1
          cases+=1
# Exact subprobability masses for pinned terminal pair (or none), small M.
probs=[]
for M in (4,16,64,256):
  for r in (0,2):
    for delta in (F(1,8),F(1,4),F(1,2)):
      p=F(1,2)+delta/2; n=M-r
      gate=sum((F(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1)
                if abs(F(r//2+k,M)-F(1,2))<=delta),F(0))
      w=(p*(1-p))**(r//2)
      # Each paired sequence on pinned pattern has equal probability.
      for k in range(n+1):
        assert w*p**k*(1-p)**(n-k)==w*(1-p)**(n-k)*p**k
      bound=max(0,1-2*exp(-M*float(delta)**2/2))
      assert float(gate)+1e-14>=bound
      probs.append({'M':M,'r':r,'delta':str(delta),'gate_probability_exact':str(gate),
                    'matched_mass_exact':str(w*gate),'risk_lower_exact':str(delta*w*gate/2),
                    'hoeffding_gate_lower':bound})
# Below-half-grid asymptotic examples: exact exhaustive count collisions.
separation=[]
for h in (2,3,4,5):
  Q=1<<h; M=Q**4; delta=F(1,4*Q); P=max(4*h,3*h)
  count=0
  for A in range(M//2-int(M*delta),M//2+int(M*delta)+1):
    if abs(F(A,M)-F(1,2))<=delta:
      a,_=labels(A,M,h,3,P,delta,True)
      b,_=labels(M-A,M,h,3,P,delta,True)
      assert a==b; count+=1
  lower=float(delta/2*(F(1,4)-delta*delta/4))*max(0,1-2*exp(-M*float(delta)**2/2))
  separation.append(dict(Q=Q,M=M,P=P,delta=str(delta),matched_counts=count,
                         terminal_risk_lower=lower,clean_upper=1/(2*M**.5)+2/Q**3))
# Preserve negative-control floor-rounding failure.
_,u=labels(1,3,1,2,2,F(1,8),False)
_,v=labels(2,3,1,2,2,F(1,8),False)
assert u[0]+v[0]!=4 and u[1:]!=v[1:]
files=['FN001_theorem.md','check_fn001.py']
out=dict(status='PASS',scope='finite exact diagnostic, not formal verification',
         exhaustive_count_cases=cases,gate_matches=matched,outside_gate_identity=outside,
         exact_probability_cases=probs,separation=separation,
         negative_control={'M':3,'P':2,'A':1,'rails_U':u,'complement_rails_U':v},
         sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files})
(ROOT/'FN001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('exact_probability_cases','sha256')},indent=2))
