from fractions import Fraction as F
from itertools import product
import json
if not __debug__:raise RuntimeError('assertions required')
signs=[-1,1];pairs=list(product(signs,repeat=2));triples=list(product(signs,repeat=3))
def model(r,s,t):
 pi={(x,y):(1+r*x*y)/4 for x,y in pairs}
 p={(x,y,z):(1+r*x*y+r*y*z+s*x*z+t*x*y*z)/8 for x,y,z in triples}
 q={(x,y):(1+(r*y+s*x+t*x*y)/(1+r*x*y))/2 for x,y in pairs}
 P=[[F(0)]*4 for _ in pairs]
 for i,(x,y) in enumerate(pairs):
  for z in signs:P[i][pairs.index((y,z))]=q[x,y] if z==1 else 1-q[x,y]
 return pi,p,q,P
feasible=0;rejected=0
for c in [F(1,10),F(1,4),F(2,5)]:
 a=1-2*c
 for r,s,t in product([F(i,10) for i in range(-5,6)],repeat=3):
  valid=abs(r+s)+abs(t)<=a*(1+r) and abs(r-s)+abs(t)<=a*(1-r)
  pi,p,q,P=model(r,s,t)
  assert valid==all(c<=x<=1-c for x in q.values())
  if not valid:rejected+=1;continue
  feasible+=1;assert sum(p.values())==1
  for x,y in pairs:
   assert sum(p[x,y,z] for z in signs)==pi[x,y]
   assert sum(p[z,x,y] for z in signs)==pi[x,y]
   assert sum(pi[u]*P[pairs.index(u)][pairs.index((x,y))] for u in pairs)==pi[x,y]
   assert pi[x,y]>=c*c
  assert sum(v*x for (x,y,z),v in p.items())==0
  assert sum(v*x*y for (x,y,z),v in p.items())==r
  assert sum(v*x*z for (x,y,z),v in p.items())==s
  assert sum(v*x*y*z for (x,y,z),v in p.items())==t
  for i,j in product(range(4),repeat=2):assert sum(P[i][k]*P[k][j] for k in range(4))>=c*c
c=F(1,4);r=F(1,10);s=F(1,20);t0=F(1,10);h=F(1,5)
mods=[model(r,s,t0-h),model(r,s,t0+h)];mid=model(r,s,t0)[2]
L1=L2=F(0)
for pi,p,q,P in mods:
 L1+=sum(pi[u]*abs(q[u]-mid[u]) for u in pairs)/2
 L2+=sum(pi[u]*(q[u]-mid[u])**2 for u in pairs)/2
assert L1==h/2==F(1,10);assert L2==h*h/(4*(1-r*r))==F(1,99)
path_checks=0;enumeration=[]
for t in [t0-h,t0+h]:
 pi,p,q,P=model(r,s,t)
 for N in [3,4,6,8]:
  mass=F(0);risk1=risk2=F(0);pairlaw={u:F(0) for u in pairs};zz=F(0)
  for xs in product(signs,repeat=N):
   prob=pi[xs[:2]]
   for i in range(N-2):prob*=q[xs[i:i+2]] if xs[i+2]==1 else 1-q[xs[i:i+2]]
   mass+=prob;u=xs[-2:];pairlaw[u]+=prob;risk1+=prob*abs(q[u]-mid[u]);risk2+=prob*(q[u]-mid[u])**2
   if N==4:zz+=prob*xs[0]*xs[3]
   path_checks+=1
  assert mass==1 and pairlaw==pi and risk1==L1 and risk2==L2
  rec=dict(t=str(t),N=N,L1=str(risk1),squared=str(risk2))
  if N==4:
   rec['adjacent_triple_product_covariance']=str(zz-t*t)
   assert zz!=t*t
  enumeration.append(rec)
print(json.dumps(dict(status='pass',arithmetic='exact Fraction',feasible_grid_models=feasible,rejected_grid_models=rejected,path_checks=path_checks,example_transition_tables=[{str(u):str(m[2][u]) for u in pairs} for m in mods],exact_common_template_L1=str(L1),exact_common_template_squared=str(L2),path_enumeration=enumeration,scope='source-family and template-risk algebra; not a numerical proof of the architecture L2 theorem'),indent=2))
