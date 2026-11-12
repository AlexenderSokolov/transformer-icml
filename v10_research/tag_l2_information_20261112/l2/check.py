from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib
if not __debug__:raise RuntimeError('Run without -O')
checks=0
# Exact maximally dependent selection examples and sharp equality.
for m in [2,4,8]:
 per=[F(1,m)]*m
 selected=F(1)
 assert sum(per)==selected;checks+=1
 for seed in range(30):
  table=[[F(((r+1)*(t+2)*(seed+3))%13-6,7) for t in range(m)] for r in range(m)]
  lhs=sum(table[t][t]**2 for t in range(m))/m
  rhs=sum(sum(x*x for x in row)/m for row in table)
  assert lhs<=rhs;checks+=1
# Rational probability spaces with nonuniform, dependent tag, vector-valued fluctuations.
for N in range(2,8):
 for theta in [F(-1,2),F(0),F(1,4)]:
  lhs=F(0);rhs=F(0);mass=F(0)
  for xs in product([-1,1],repeat=N):
   p=F(1,4)
   for j in range(N-2):p*=(1+theta*xs[j]*xs[j+1]*xs[j+2])/2
   tag=(2 if xs[-2]==1 else 0)+(1 if xs[-1]==1 else 0)
   Z=[]
   for r in range(4):
    z1=sum(F(((j+r)%3)-1)*x for j,x in enumerate(xs))/N
    z2=sum(F(((2*j+r)%5)-2)*x for j,x in enumerate(xs))/N
    Z.append(z1*z1+z2*z2)
   lhs+=p*Z[tag];rhs+=p*sum(Z);mass+=p
  assert mass==1 and lhs<=rhs;checks+=2
p=Path(__file__).parent;r={'exact_checks':checks,'scope':'dependent finite-tag L2 selection, including four terminal tags under small spin-source laws; no numerical architecture-risk certification'}
(p/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
(p/'RECEIPT.json').write_text(json.dumps({'sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.name!='RECEIPT.json' and f.is_file()}},indent=2)+'\n')
