"""Finite corroboration, not proof, of the new scalar tolerance corollary."""
import math,json
from pathlib import Path
n=0; max_ratio=0
for M in [64,65,127,128,1000,10000,10**6,10**12,10**24]:
 for e in [1/M, min(1,2/M),1/math.sqrt(M),.125,.5,1]:
  e=max(e,1/M); s=1/math.sqrt(M); f=1+math.log1p(1/(e*math.sqrt(M))); T=math.sqrt(M)/f
  assert 1<=T<=math.sqrt(M)
  for k in sorted(set([0,1,int(T),min(M,int(T)+1),int(math.sqrt(M)),M])):
   F=0 if k==0 else k/M*(1+math.log1p(1/(k*e)))
   if k<=math.floor(T):assert F<=2*s*(1+1e-12)
   if k:
    A=F/s
    assert k<=A*max(A,1)*T*(1+1e-12)
   n+=1
  ratio=(1+math.log1p(f/(e*math.sqrt(M))))/f
  assert ratio<=2
  max_ratio=max(max_ratio,ratio)
out={'status':'PASS','checks':n,'largest_continuous_sufficiency_ratio_tested':max_ratio,'scope':'Finite scalar corroboration only; analytic proof in Corollary 3.1; no process experiments'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
