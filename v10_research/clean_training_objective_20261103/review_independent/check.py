import itertools, math, json, hashlib
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def counts(w):
 c=[[0,0] for _ in range(4)]
 for a,b,z in zip(w,w[1:],w[2:]):c[2*a+b][z]+=1
 return c
def mass(w):
 r=F(1,4)
 for a,b in counts(w):r*=F(math.factorial(a)*math.factorial(b),math.factorial(a+b+1))
 return r
words=0
for M in range(0,10):
 total=F(0)
 for w in itertools.product(range(2),repeat=M+2):
  mw=mass(w);total+=mw;assert mw>0
  c=counts(w);a,b=c[2*w[-2]+w[-1]]
  assert mass(w+(1,))/mw==F(b+1,a+b+2)
  assert mass(w+(0,))+mass(w+(1,))==mw
  words+=1
 assert total==1
ratios=0
for j in range(25):
 for c in range(j+1):
  for jj in range(25):
   for cc in range(jj+1):
    diff=abs(F(cc+1,jj+2)-F(c+1,j+2))
    assert diff<=F(abs(cc-c)+abs(jj-j),j+2)
    ratios+=1
import mpmath as mp
mp.mp.dps=70
def h(p):return -(p*mp.log(p) if p else 0)-((1-p)*mp.log(1-p) if p<1 else 0)
def kl(p,q):return -h(p)-p*mp.log(q)-(1-p)*mp.log(1-q)
entropy=0; slack=mp.mpf(1e10)
for eta in map(mp.mpf,['.5','.125','.01','.000001']):
 for ip in range(51):
  p=mp.mpf(ip)/50
  for iq in range(51):
   q=eta+(1-2*eta)*mp.mpf(iq)/50;d=abs(p-q)
   s=h(d)+d*mp.log((1-eta)/eta)-kl(p,q)
   assert s>=-mp.mpf('1e-60'), (eta,p,q,s)
   slack=min(slack,s);entropy+=1
slack=str(slack)
layer=0
for M in [64,100,1000,1000000]:
 for k in sorted(set([1,int(math.sqrt(M)),M//2,M])):
  a=192*k/(M+1);integ=1 if a>=1 else a*(1+math.log(1/a))
  assert integ<=192*k/M*(1+math.log(M/k))+1e-12;layer+=1
report={'status':'PASS','posterior_words_exact':words,'rational_ratio_cases':ratios,'entropy_grid_cases':entropy,'entropy_min_slack':slack,'layercake_cases':layer,'candidate_sha256':hashlib.sha256((root/'CANDIDATE.md').read_bytes()).hexdigest(),'scope':'Finite corroboration; not universal proof of accepted interfaces.'}
(root/'review_independent'/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
