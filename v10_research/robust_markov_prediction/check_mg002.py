from fractions import Fraction as F
from pathlib import Path
import hashlib,json
D=Path(__file__).parent
cases=0;snakes=0;scalar=0;boundary=[]
# Integer upper bounds only: no square roots or logarithms in executable schedule.
for R in range(2,6):
 for c in [0,1,3]:
  B=4*R*(c+2);C=(2*B)**(R-1)
  for M in list(range(64,2049))+[2**j+r for j in range(12,81,4) for r in [-1,0,1]]:
   m=(M+1).bit_length();L=(m-1).bit_length();chi=2**L
   assert m<=chi<2*m
   for h in range(1,43):
    Q=2**h
    if Q**(2*R)<C*C*M:continue
    if Q*Q>=M:
     scalar+=1;N=1
     assert Q*Q>=M
    else:
     k=1
     while Q*Q*2**(2*k*(R-1))<M:k+=1
     N=2**k
     assert Q*Q*N**(2*(R-1))>=M
     if k>1:assert Q*Q*(N//2)**(2*(R-1))<M
     assert N*B<=Q
     snakes+=1
    cases+=1
# Explicit finite rational conversion, positive and negative, exact error < 2^-P.
conversion=0
for P in [2,5,11,31]:
 for a in range(-31,32):
  for b in range(1,33):
   v=F(a,b);z=F((v*2**P).__floor__(),2**P)
   assert 0<=v-z<F(1,2**P)
   conversion+=1
out={'status':'PASS','scope':'Exact integer schedule and rational conversion diagnostics, not all-parameter proof or emitted network audit','capacity_schedule_cases':cases,'snake_cases':snakes,'scalar_fallback_cases':scalar,'rational_conversion_cases':conversion,'theorem_sha256':hashlib.sha256((D/'MG002_partial_capacity_extension.md').read_bytes()).hexdigest()}
(D/'MG002_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
