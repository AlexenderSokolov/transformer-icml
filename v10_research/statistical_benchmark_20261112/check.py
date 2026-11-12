from fractions import Fraction as F
from itertools import product
from math import comb,sqrt
import json
if not __debug__:raise RuntimeError('assertions required')
states=list(product([-1,1],repeat=2));c=F(1,4)
def stationary(q):
 P=[[F(0) for _ in states] for _ in states]
 for j,(x,y) in enumerate(states):
  for z in [-1,1]:P[j][states.index((y,z))]=q[j] if z==1 else 1-q[j]
 A=[[P[j][i]-(i==j) for j in range(4)]+[F(0)] for i in range(3)]+[[F(1)]*4+[F(1)]]
 for k in range(4):
  t=next(j for j in range(k,4) if A[j][k]);A[k],A[t]=A[t],A[k];v=A[k][k];A[k]=[x/v for x in A[k]]
  for j in range(4):
   if j!=k:
    v=A[j][k];A[j]=[x-v*y for x,y in zip(A[j],A[k])]
 pi=[A[i][4] for i in range(4)]
 assert sum(pi)==1 and all(x>=c*c for x in pi)
 assert all(sum(pi[j]*P[j][i] for j in range(4))==pi[i] for i in range(4))
 return pi
rows=[];word_checks=0
for q in [[F(1,2)]*4,[F(1,4),F(3,4),F(3,4),F(1,4)],[F(1,4),F(1,2),F(3,4),F(1,2)],[F(3,4),F(1,4),F(1,2),F(3,4)]]:
 pi=stationary(q)
 for N in [3,4,6,8,10]:
  n=N-2;mass=F(0);risk=F(0);J1=[F(0)]*4;J2=J1[:];M2=J1[:];errs=J1[:]
  for xs in product([-1,1],repeat=N):
   p=pi[states.index(xs[:2])];J=[0]*4;A=[0]*4
   for i in range(n):
    u=states.index(xs[i:i+2]);p*=q[u] if xs[i+2]==1 else 1-q[u];J[u]+=1;A[u]+=xs[i+2]==1
   f=[max(c,min(1-c,(F(A[u])+F(1,2))/(J[u]+1))) for u in range(4)]
   term=states.index(xs[-2:]);mass+=p;risk+=p*abs(f[term]-q[term]);word_checks+=1
   for u in range(4):J1[u]+=p*J[u];J2[u]+=p*J[u]**2;M2[u]+=p*(A[u]-q[u]*J[u])**2;errs[u]+=p*abs(f[u]-q[u])
  assert mass==1 and risk<=sum(errs)
  for u in range(4):
   assert J1[u]==n*pi[u]
   assert J2[u]-J1[u]**2<=n*pi[u]/c**2
   assert M2[u]<=n*pi[u]/4
   assert float(errs[u])<=1/sqrt(float(n*pi[u]))+float((1+4/c**2)/(n*pi[u]))
  rows.append(dict(N=N,q=list(map(str,q)),selected_risk=str(risk),stationary_pair=list(map(str,pi))))
low=[]
for n in [1,4,9,16]:
 h=F(1,4*int(sqrt(n)));p=(1+h)/2;r=(1-h)/2
 overlap=sum(min(F(comb(n,k))*p**k*(1-p)**(n-k),F(comb(n,k))*r**k*(1-r)**(n-k)) for k in range(n+1))
 bayes=h*overlap/2;assert bayes>=h/3
 low.append(dict(n=n,h=str(h),exact_two_point_bayes=str(bayes),claimed_lower=str(h/3)))
spin=0
for N in [3,4,6,8]:
 n=N-2
 for theta in [F(-1,2),F(-1,4),F(0),F(1,4),F(1,2)]:
  risk=F(0)
  for xs in product([-1,1],repeat=N):
   zz=[xs[i]*xs[i+1]*xs[i+2] for i in range(n)];p=F(1,4)
   for z in zz:p*=(1+theta*z)/2
   th=max(F(-1,2),min(F(1,2),F(sum(zz),n)));risk+=p*abs(th-theta)/2
  p=(1+theta)/2
  exact=sum(F(comb(n,k))*p**k*(1-p)**(n-k)*abs(max(F(-1,2),min(F(1,2),F(2*k-n,n)))-theta)/2 for k in range(n+1))
  assert risk==exact;spin+=1
print(json.dumps(dict(status='pass',arithmetic='exact rational enumeration except displayed square-root upper-bound comparisons',general_word_checks=word_checks,general_rows=rows,spin_risk_identities=spin,binomial_minimax_checks=low,scope='standard statistical benchmark; not a new rate or neural construction'),indent=2))
