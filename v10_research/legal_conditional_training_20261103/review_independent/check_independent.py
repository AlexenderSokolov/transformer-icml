from fractions import Fraction as F
from itertools import product,combinations
from collections import defaultdict
from math import comb,sqrt
M=5;k=2
sources=[([F(0),F(1),F(1,2),F(1)],[F(1),F(0),F(0),F(0)]),([F(1,4),F(1,2),F(0),F(1)],[F(0),F(1),F(0),F(0)]),([F(1,3),F(2,3),F(3,5),F(1,4)],[F(1,10),F(2,10),F(3,10),F(4,10)])];weights=[F(1,5),F(3,10),F(1,2)]
def details(w):
 C=[0]*8
 for i in range(len(w)-2):C[4*w[i]+2*w[i+1]+w[i+2]]+=1
 start=2*w[0]+w[1];end=2*w[-2]+w[-1];return (start,end,*C),C
def probability(w,t,mu):
 x=mu[2*w[0]+w[1]]
 for i in range(len(w)-2):
  p=t[2*w[i]+w[i+1]];x*=p if w[i+2] else 1-p
 return x
def acts(w):
 for j in range(k+1):
  for inds in combinations(range(M),j):
   z=list(w)
   for i in inds:z[i]=1-z[i]
   yield tuple(z)
def predict(w):return F((3*w[0]+2*w[1]+w[-1])%7,6)
groups=defaultdict(set);groupwords=defaultdict(int);massall=F();true=F();noise=F();regret=F();sup=F();labelnoise=F();labeloracle=F();positive=0
for word in product([0,1],repeat=M+2):
 t,counts=details(word);ws=[weights[i]*probability(word,*sources[i]) for i in range(len(sources))];mass=sum(ws);massall+=mass
 if not mass:continue
 positive+=1;tv=2*word[-2]+word[-1];qs=[source[0][tv] for source in sources];qbar=sum(w*q for w,q in zip(ws,qs))/mass;groups[t].add(qbar);groupwords[t]+=1;z=list(acts(word));base=max((predict(v)-qbar)**2 for v in z);var=sum(w*(q-qbar)**2 for w,q in zip(ws,qs))/mass;direct=max(sum(w*(predict(v)-q)**2 for w,q in zip(ws,qs))/mass for v in z);ymax=max((1-qbar)*predict(v)**2+qbar*(1-predict(v))**2 for v in z);oracle=(1-qbar)*max(predict(v)**2 for v in z)+qbar*max((1-predict(v))**2 for v in z)
 assert direct==base+var and ymax==base+qbar*(1-qbar);true+=mass*direct;noise+=mass*var;regret+=mass*base;sup+=mass*ymax;labelnoise+=mass*qbar*(1-qbar);labeloracle+=mass*oracle
assert massall==1 and all(len(s)==1 for s in groups.values()) and true==regret+noise and sup==regret+labelnoise and labeloracle>=sup
print('zero-transition/source-dependent-initial exact test positive words',positive,'groups',len(groups),'colliding groups',sum(n>1 for n in groupwords.values()))
print('mass',massall,'true risk',true,'source variance',noise,'regret',regret,'supervised',sup,'supervised additive noise',labelnoise,'label-aware',labeloracle)
for m in range(1,12):
 mapping={};canonical=set();nword=0
 for w in product([0,1],repeat=m+2):
  t,C=details(w);start,end=t[:2];a,b,c,d,e,f,g,h=C;deltas=[int(end==x)-int(start==x) for x in range(4)];rec=[a,b,c,d,b+deltas[0],deltas[1]-b+c+d,d-deltas[3],0];rec[-1]=m-sum(rec[:-1]);assert rec==C;key=(start,end,a,b,c,d)
  if key in mapping:assert mapping[key]==tuple(C)
  mapping[key]=tuple(C);canonical.add(t);nword+=1
 assert len(mapping)==len(canonical) and len(mapping)<=16*(m+1)**4
 print('flow M',m,'words',nword,'groups',len(mapping))
p=F(1,5); loss=lambda q:(1-p)*q*q+p*(1-q)**2; a,b,c=F(1,10),F(3,10),F(2,5); legal=max(loss(a),loss(b));oracle=(1-p)*max(a*a,b*b)+p*max((1-a)**2,(1-b)**2);assert (legal,loss(c),oracle)==(F(17,100),F(1,5),F(117,500));print('counterexample',legal,loss(c),oracle,'source squared', (a-p)**2,(c-p)**2)
for n in [1,2,4,10,50]:
 for pi in [F(1,100),F(1,5),F(1,2),F(1)]:
  moment=sum(F(comb(n,j))*pi**j*(1-pi)**(n-j)*F(1,j+1) for j in range(n+1));formula=(1-(1-pi)**(n+1))/((n+1)*pi);assert moment==formula and moment<=1/((n+1)*pi)
print('exact binomial occupancy identity verified for 20 (n,pi) cases')
