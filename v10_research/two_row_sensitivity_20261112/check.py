from fractions import Fraction as F
from random import Random
import math,json
if not __debug__:raise RuntimeError('assertions required')
rng=Random(20261112);cases=0;noncommuting=0;maxratio=0.
for N in [3,4,8,16,64]:
 for D in range(0,21):
  for _ in range(10):
   aa=[F(rng.randrange(9),8) for j in range(D)];bb=[F(rng.randrange(17),4) for j in range(D)]
   al=[a+b/(N-1) for a,b in zip(aa,bb)];be=[a+b/N for a,b in zip(aa,bb)];ga=[b/N for b in bb]
   x,y=F(1),F(0)
   for a,b,g in zip(al,be,ga):x,y=a*x,g*x+b*y
   exact=F(0)
   for r in range(D):
    t=ga[r]
    for l in range(r):t*=al[l]
    for l in range(r+1,D):t*=be[l]
    exact+=t
   assert y==exact
   pa=pb=F(1)
   for v in al:pa*=v
   for v in be:pb*=v
   assert y==(N-1)*(pa-pb)
   # Check this two-row recurrence against the complete prefix matrix.
   vec=[F(0)]*N;vec[-2]=F(1)
   for a,b in zip(aa,bb):vec=[a*v+b*sum(vec[:i+1])/F(i+1) for i,v in enumerate(vec)]
   assert vec[-1]==y and all(v==0 for v in vec[:-2])
   B=sum(bb,F(0));bound=float(B/N)*math.exp(float(B/(N-1)))
   assert float(y)<=bound+1e-12
   if bound: maxratio=max(maxratio,float(y)/bound)
   if D>=2 and ga[1]*al[0]+be[1]*ga[0]!=ga[0]*al[1]+be[0]*ga[1]:noncommuting+=1
   cases+=1
print(json.dumps(dict(status='pass',variable_coefficient_cases=cases,noncommuting_first_two_pairs=noncommuting,max_exp_bound_ratio=maxratio,arithmetic='exact Fraction products; float exponential bound comparison',scope='declared sensitivity recurrence only, not verification of a Transformer'),indent=2))
