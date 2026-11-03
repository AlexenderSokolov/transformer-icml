#!/usr/bin/env python3
"""Independent finite corroboration only, not a proof of asymptotic theorem."""
import json, math
from fractions import Fraction as F
from pathlib import Path
out=Path(__file__).parent
cases=0; rowchecks=0; midchecks=0
for i in range(9):
 for j in range(i+1,9):
  p0,p1=F(i,8),F(j,8); d=p1-p0; tau=(p0+p1)/2
  midchecks+=1
  assert abs(tau-p0)==abs(tau-p1)==d/2
  for a in range(1,16):
   alpha=F(a,32)
   if not alpha<d/2: continue
   gamma=d/2-alpha
   q0=min(F(1),p0+alpha); q1=max(F(0),p1-alpha)
   assert q0<=tau-gamma and q1>=tau+gamma
   for R in range(1,33):
    e0=sum(F(math.comb(R,k))*q0**k*(1-q0)**(R-k) for k in range(R+1) if F(k,R)>=tau)
    e1=sum(F(math.comb(R,k))*q1**k*(1-q1)**(R-k) for k in range(R+1) if F(k,R)<tau)
    bound=math.exp(-2*R*float(gamma)**2)
    assert float(e0)<=bound+1e-14 and float(e1)<=bound+1e-14
    cases+=1
   delta=alpha/2
   s0=(1-delta)*p0+delta/2; s1=(1-delta)*p1+delta/2
   assert 0<s0<s1<1
   assert abs(s0-p0)<=alpha and abs(s1-p1)<=alpha
   rowchecks+=1
result={'status':'PASS','separate_conditional_error_checks':cases,'full_support_mixture_checks':rowchecks,'midpoint_boundary_checks':midchecks,'limits':'Binary-output rational endpoint examples only; analytic proof, arbitrary alphabets, and asymptotic necessity are separately reviewed.'}
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
