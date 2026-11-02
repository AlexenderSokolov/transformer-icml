"""Exact rational diagnostic, not proof of missing transport theorem."""
from fractions import Fraction as F
from itertools import product
import json
from transport_lp import words
checks=0
for M,e,p in product([64,128,1024],[F(1,64),F(1,32),F(1,16)],[F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)]):
 if e<F(1,M):continue
 a=F(1,2*M); beta=e*e;x=1/(e/a+2+p/(1-e)); pi=[x*e/a,x,x,x*p/(1-e)]
 P=[[1-a,a,0,0],[0,0,1-p,p],[e,1-e,0,0],[0,0,1-e,e]]
 assert sum(pi)==1
 for v in range(4):assert sum(pi[u]*P[u][v] for u in range(4))==pi[v];checks+=1
 for u,v in product(range(4),repeat=2):assert sum(P[u][w]*P[w][v] for w in range(4))>=beta*pi[v];checks+=1
for s in range(30):
 xx=words(s,2); target='01'*(s+3)
 avg=F(sum(sum(a!=b for a,b in zip(x,target)) for x in xx),len(xx))
 assert avg==F(2*s,3)+3;checks+=1
for s,l in product(range(8),range(2,7)):
 xx=words(s,l); hist={}; totalcost=0
 for x in xx:
  # uniquely decode cycle string
  tiles=[];i=0
  while i<len(x):
   tile='01' if x[i]=='0' else '101'; assert x[i:i+len(tile)]==tile; tiles.append(tile);i+=len(tile)
  inds=[i for i,z in enumerate(tiles) if z=='101']
  for a,b in zip(inds,inds[1:]):
   y=''.join(tiles[:a]+['01']*(b-a+2)+tiles[b+1:]);hist[y]=hist.get(y,0)+1
   totalcost+=sum(u!=v for u,v in zip(x,y))
 assert F(totalcost,len(xx)*(l-1))==3+F(2*s,l+1);checks+=1
 for y in words(s+3,l-2):
  gaps=[];g=0;i=0
  while i<len(y):
   if y[i]=='0':g+=1;i+=2
   else:gaps.append(g);g=0;i+=3
  gaps.append(g)
  D=sum((h-1)*(h-2)//2 if h>=3 else 0 for h in gaps)
  assert hist.get(y,0)==D;checks+=1
print(json.dumps({'status':'PASS','exact_checks':checks,'scope':'stationarity, all-state certificate grid, boundary formula, failed-merge density and cost','missing_transport_theorem':'NOT CHECKED OR PROVED'},indent=2))
