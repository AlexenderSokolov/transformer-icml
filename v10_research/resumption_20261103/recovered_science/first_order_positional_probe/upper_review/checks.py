#!/usr/bin/env python3
"""Independent finite checks, supplemental to the analytic audit; no source edits."""
from itertools import product
from fractions import Fraction as F
from math import comb, sqrt, log
import json
out={}
pairs=0; reconstruct=0; max_changes=[0,0,0]
def counts(w,u):
    N=len(w)-1
    return sum(x==u for x in w[:N]),sum(w[i]==u and w[i+1]!=u for i in range(N))
for N in range(1,8):
    words=list(product((0,1),repeat=N))
    for z in (0,1):
      for x in words:
        w=x+(z,); J,C=counts(w,z)
        for y in words:
          wp=y+(z,); Jp,Cp=counts(wp,z); k=sum(a!=b for a,b in zip(x,y)); pairs+=1
          assert abs(Jp-J)<=k and abs(Cp-C)<=2*k
          for r in range(1,N+2):
            m=min(r-1,N//2)
            O=sum(v==z for v in w[:N-m]); Op=sum(v==z for v in wp[:N-m])
            assert Op==Jp-sum(v==z for v in wp[N-m:N])
            assert abs(Op-O)<=k
            assert O>=sum(v==z for v in w[:N//2])
            reconstruct+=1
out['exhaustive_edit_checks']={'N':'1..7','protected_word_pairs':pairs,'all_window_checks':reconstruct,'result':'pass; tighter J/O <= k, C <= 2k'}
quant=0
for N in range(1,41):
 for k in range(1,N+1):
  b=k+1; D=2*(N//b+1)
  assert F(1,8*D)>=F(k+1,16*(N+k+1))>=F(k,48*N)
  for n in range(N+1):
   h=b*(n//b)
   assert 0<=n-h<=k
   assert F(comb(N-h,n-h),comb(N,n)*comb(n,h))==F(1,comb(N,h))
   quant+=1
out['quantizer_checks']={'N':'1..40','combinatorial_cases':quant,'result':'pass'}
assert 48*28==1344
assert 4*(6156+3078)==36936
assert 1024+1344+36936==39304
assert 2*2**3*1023==16368
assert 48*16368+36936==822600<2**20
assert 1536*26==39936
assert 1024+96+39936==41056<2**16
assert 96*2**17<2**24
for N in range(64,2001):
 assert 512/sqrt(N+1)+1160/N<=657/sqrt(N)
 assert 3/(128*sqrt(N+1))>=1/(64*sqrt(N))
 for r in range(1,N+2):
  m=min(r-1,N//2); L=1+log(N/(m+1)); ell=1+log((N+1)/r)
  assert m+1==min(r,N//2+1)
  assert L<=2*ell
out['constant_and_endpoint_checks']={'N':'64..2000; every r','result':'pass'}
print(json.dumps(out,indent=2))
