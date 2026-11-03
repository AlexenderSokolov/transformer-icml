from fractions import Fraction as F
from itertools import product
import json, math
from pathlib import Path
nrow=nmix=nprod=0
rows=[]
for a in range(5):
 for b in range(5-a): rows.append((F(a,4),F(b,4),F(4-a-b,4),F(0)))
def aff(p,q):
 assert all(not x or y for x,y in zip(p,q))
 return sum((x*x/y for x,y in zip(p,q) if y),F(0))
for p0,p1 in product(rows,repeat=2):
 d=sum(map(abs,(x-y for x,y in zip(p0,p1))))/2
 if not d: continue
 mu=tuple((x+y)/2 for x,y in zip(p0,p1)); nu=tuple(y-x for x,y in zip(p0,p1))
 for s in (F(1,4),F(1,8),F(1,64),F(1,1024)):
  gamma=s*d; alpha=d/2-gamma
  q0=tuple(x-s*y for x,y in zip(mu,nu));q1=tuple(x+s*y for x,y in zip(mu,nu))
  assert sum(map(abs,(x-y for x,y in zip(q0,p0))))/2==alpha
  assert sum(map(abs,(x-y for x,y in zip(q1,p1))))/2==alpha
  zeta=1+32*s*s
  assert aff(q0,q1)<=zeta and aff(q1,q0)<=zeta
  assert aff(q0,mu)-1<=4*s*s and aff(q1,mu)-1<=4*s*s
  nrow+=1
  for u,v in product((F(0),F(1,3),F(1)),repeat=2):
   p=tuple(u*x+(1-u)*y for x,y in zip(q0,q1));q=tuple(v*x+(1-v)*y for x,y in zip(q0,q1))
   assert aff(p,q)<=zeta; nmix+=1
  if s==F(1,4):
   code=[tuple(x*y for x,y in product(a,b)) for a,b in product((q0,q1),repeat=2)]
   for a,b in product(code,repeat=2): assert aff(a,b)<=zeta*zeta; nprod+=1
scalar=0
for i,j in product(range(101),repeat=2):
 D=i/100; x=j/25
 assert max(math.sqrt(D)-math.sqrt(x),0)**2+1e-14>=D/2-x
 scalar+=1
for b in (1,2,100,8519682):
 for scale in (128,1024,1048576):
  root=16*b*scale; N=root//(16*b)+1
  spacing=F(8*b,root)
  assert F(1,4)+(N-1)*spacing<=F(3,4)
  assert N>=F(root,16*b)
  assert F(2*b,root)/spacing<=F(1,4)
report={'status':'PASS_FINITE_CORROBORATION_ONLY','exact_nominal_margin_cases':nrow,'exact_arbitrary_mixture_cases':nmix,'exact_product_pair_cases':nprod,'scalar_loss_inequality_numeric_cases':scalar,'grid_parameter_cases':12,'checks':'Exact rational row geometry, common-zero omission, two ordered affinities, KL proxy to midpoint, unrelated mixtures, product codeword affinities; numerical scalar bound and grid arithmetic. Not a proof of all real parameters or statistical imported lemma.'}
Path(__file__).with_name('checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,sort_keys=True))
