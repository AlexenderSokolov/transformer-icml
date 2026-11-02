from fractions import Fraction as F
from pathlib import Path
import json
n=0
for P in range(1,9):
 D=2**P
 for Z in range(-D,2*D+1):
  A=max(0,Z)-max(0,Z-D)
  assert 0<=A<=D
  for f in [F(0),F(1,7),F(1,2),F(1)]:
   assert abs(F(A,D)-f)<=abs(F(Z,D)-f);n+=1
result={'status':'PASS','checks':n,'claim':'Exact lattice cube clipping and nonexpansiveness; finite diagnostics only.'}
(Path(__file__).parent/'clip_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
