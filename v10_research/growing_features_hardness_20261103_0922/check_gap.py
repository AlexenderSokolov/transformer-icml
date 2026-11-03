from fractions import Fraction
from math import isqrt
n=0
for power in range(2,12):
 M=1<<power;t=Fraction(1,M+2)
 for m in range(1,isqrt(M)+1):
  P=1<<(m-1).bit_length();Q=Fraction(3,2*M); dq=Fraction(1,2*M*P)
  slope=Fraction(8,M*(M+2)); g=Fraction(4,M*M*(M+2)*P)
  assert slope*dq==g
  for V in range(m+1):
   q=Q-V*dq
   assert Fraction(1,M)<=q<=Q and q>t
   assert q-t>=Fraction(2,M*(M+2)) and q*(1-q)<=Fraction(1,4)
   assert (q-t)/(q*(1-q))>=slope
   if V:assert Q-q>=dq
   n+=1
print('exact_rational_slope_and_gap_cases',n,'PASS')
