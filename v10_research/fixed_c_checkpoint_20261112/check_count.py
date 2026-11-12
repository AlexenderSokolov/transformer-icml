from fractions import Fraction as F
from itertools import product
import json

def law(n,t):
 d={(x+y,x,y):F(1,4) for x,y in product((-1,1),repeat=2)}
 for _ in range(2,n):
  e={}
  for (s,x,y),p in d.items():
   for z in (-1,1):
    key=s+z,y,z
    e[key]=e.get(key,0)+p*(1+t*x*y*z)/2
  d=e
 return d
checks=0
for n in range(2,11):
 for t in (F(1,4),F(1,2),F(-1,2)):
  a=law(n,t);b={}
  for x in product((-1,1),repeat=n):
   p=F(1,4)
   for i in range(n-2):p*=(1+t*x[i]*x[i+1]*x[i+2])/2
   k=sum(x),x[-2],x[-1];b[k]=b.get(k,0)+p
  assert a==b and sum(a.values())==1
  checks+=1
# Floating forward recursion; this is not a proof of rate.
rows=[]
for n in (8,16,32,64,128,256,512):
 a=law(n,0.5);b=law(n,-0.5)
 tv=sum(abs(v-b.get(k,0)) for k,v in a.items())/2
 rows.append({'N':n,'TV':tv,'sqrtN_times_TV':tv*n**0.5,'mass_error':abs(sum(a.values())-1)})
print(json.dumps({'exact_joint_law_checks':checks,'status':'pass','theta':0.5,'float_rows':rows},indent=2))
