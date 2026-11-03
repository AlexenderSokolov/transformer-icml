from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
p=Path(__file__).with_name('population_cases.jsonl')
def clip(x):return max(F(1,4),min(F(3,4),x))
ct=0
with p.open('x') as f:
 for u,g,L in product((F(1,16),F(1,8),F(3,16)),(F(0),F(1,2),F(1),F(3),F(9)),(F(0),F(1,2),F(1),F(2),F(5),F(20))):
  mu=F(2)*(1-u)/3;lam=g*u/(1+g*u)
  vals=[]
  for t in (F(1,4),F(3,4)):
   q=(mu+g*u*t)/(1+g*u);h=u;r=mu;lh=g*h/(1+g*h)
   pred=clip(F(1,2)+L*(q-(1-lh)*r-lh/2)); vals.append(abs(pred-t))
  opt=max(F(0),1-L*lam)/4
  assert max(vals)==opt
  f.write(json.dumps({'u':str(u),'gamma':str(g),'Lq':str(L),'lambda':str(lam),'loss_minus':str(vals[0]),'loss_plus':str(vals[1]),'population_opt':str(opt)})+'\n');ct+=1
print('PASS',ct,'exact rational population cases')
