#!/usr/bin/env python3
"""Author deterministic boundary diagnostics; finite corroboration only."""
import math,json,hashlib
from pathlib import Path
checks=0
branches={k:0 for k in ('weak','strong_full','lower_A','lower_B','lower_C','lower_D')}
for M in [64,65,66,127,128,255,256,1024,65536,10**8,10**16]:
 for beta in sorted(set([0,1,1/256,1/M,1/M**2,math.nextafter(1/M**2,0),math.nextafter(1/M**2,1)])):
  for h in [4,5,8,16,30,60]:
   Q=2**h
   for k in [1,2,3,100,2**20]:
    z=k*Q;s=1/math.sqrt(M);e=max(math.sqrt(beta),1/M);t=M*e
    W=(1+math.log1p(z/t))/z
    if beta*M*M>=1:
     branches['strong_full']+=1
     A=6*M/z;G=1+math.log1p(1/(math.sqrt(beta)*A))
     assert 16672*A*G/M+64/z <=2**17*W*(1+1e-14)
     for n in set([math.ceil(M/2),M-1,M]):
      Gn=1+math.log1p(1/(max(math.sqrt(beta),1/n)*A))
      assert Gn<=G*(1+1e-14)
      assert 8336*A*G/n<=16672*A*G/M*(1+1e-14)
      checks+=2
    else:
     branches['weak']+=1
     v=96/z;psi=1 if v>=1 else v*(1+math.log(1/v))
     assert psi<=96*W*(1+1e-14)
    if beta>1/256: branches['lower_A']+=1; bound=1/Q+2*s
    elif z>M/4: branches['lower_B']+=1; bound=5*s
    elif z>M**.75: branches['lower_C']+=1; bound=5*s
    else:
     branches['lower_D']+=1
     bound=1/Q+24*math.log1p(min(z/t,M/z)/8)/z
    assert W<=bound*(1+1e-14)
    checks+=2
assert (16384+4)*math.sqrt(32)+6<2**17
assert 100096<2**17 and 2**18+3==262147
assert 8/math.e<3
result={'status':'PASS finite deterministic boundary checks only; not universal proof','checks':checks,'branches':branches,'proof_sha256':hashlib.sha256(Path(__file__).with_name('BIF001_binary_all_initializations_frontier_v1.md').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
