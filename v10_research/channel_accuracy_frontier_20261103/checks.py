"""Finite corroboration only; the analytic candidate carries the universal proof."""
from fractions import Fraction as F
from math import comb, exp, log
from pathlib import Path
import hashlib,json
cases=0; tails=0
for p in [F(1,20),F(1,4),F(1,2),F(3,4),F(19,20)]:
 a=(p/24)**2
 assert a<=p/4 and a<p/8
 for alpha in [F(0),a/100,a/2,a]:
  for q0 in [F(0),alpha/2,alpha]:
   for q1 in [p-alpha,p,p+alpha]:
    c=q1*(1-q0);w=q0*(1-q1);e=q0*q1+(1-q0)*(1-q1)
    assert c+w+e==1 and c>=p/2 and w<=alpha
    # Explicit event map with semantic gate 0=(0,1), 1=(1,0).
    for gate in (0,1):
     inputs=(0,1) if gate==0 else (1,0)
     out={'correct':F(0),'wrong':F(0),'erase':F(0)}
     for x in (0,1):
      for y in (0,1):
       prob=F(1)
       for bit,member in zip(inputs,(x,y)):
        q=q0 if bit==0 else q1
        prob*=q if member else 1-q
       decoded=None if x==y else (1 if x else 0)
       label='erase' if decoded is None else ('correct' if decoded==gate else 'wrong')
       out[label]+=prob
     assert out=={'correct':c,'wrong':w,'erase':e}
    for n in [1,2,3,8,20]:
     # Exact finite joint count probabilities; worst tie decoder chooses wrong.
     abst=F(0);err=F(0)
     for h in range(n+1):
      for z in range(h+1):
       mass=comb(n,h)*comb(h,z)*w**z*c**(h-z)*e**(n-h)
       if h<p*n/4:abst+=mass
       elif 2*z>=h:err+=mass
     assert float(abst)<=exp(-n*float(p)**2/8)+1e-14
     if alpha:
      assert float(err)<=exp(float(p)*n/16*log(float(alpha)))+1e-14
     else:assert err==0
     tails+=1
    cases+=1
# Disjoint-support majority probability, counting every tie as error.
majority=0
for alpha in [F(1,10**8),F(1,1000),F(1,16)]:
 for n in range(1,81):
  tail=sum(F(comb(n,k))*alpha**k*(1-alpha)**(n-k) for k in range((n+1)//2,n+1))
  assert float(tail)<=float(alpha)**(n/4)+1e-14
  majority+=1
p=Path(__file__).parent
out={'status':'PASS','limitations':'Finite exact-rational block/tail corroboration, not universal proof or independent review. Float exponential comparison tolerance 1e-14.','block_parameter_cases':cases,'partial_tail_cases':tails,'disjoint_majority_cases':majority,'candidate_sha256':hashlib.sha256((p/'CANDIDATE.md').read_bytes()).hexdigest()}
(p/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
