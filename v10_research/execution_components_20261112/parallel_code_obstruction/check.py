import math,itertools,json,random
from fractions import Fraction as F
if not __debug__:raise RuntimeError('assertions required')
gamma=math.log(2);A=math.expm1(gamma);B=math.expm1(gamma/2);K=math.ceil(2*(A/B)**2)
rng=random.Random(20261112);cases=0;good=0;rows=[]
for d in [1,2,3]:
 for n in [4,8,12,16]:
  # Repeated codes directly exercise the crowded-cell regime; mixed codes exercise signs.
  for mode in ['same','mixed']:
   us=[]
   for i in range(n):
    v=[1.]+[0.]*(d-1) if mode=='same' else [rng.uniform(-1,1) for _ in range(d)]
    norm=math.sqrt(sum(x*x for x in v));us.append([x/norm for x in v])
   t=n-1;ww=[math.expm1(gamma*sum(a*b for a,b in zip(us[t],us[j]))) for j in range(t)]
   var=sum(w*w for w in ww);four=3*var*var-2*sum(w**4 for w in ww)
   assert four<=3*var*var+1e-10
   errors=tail=0
   for xs in itertools.product([-1,1],repeat=t):
    z=sum(w*x for w,x in zip(ww,xs));tail+=abs(z)>A+1e-12
    # average across fair target, with deterministic sign(0)=+1
    for target in [-1,1]:errors+=(1 if A*target+z>=0 else -1)!=target
   risk=errors/(2**n)
   if var>=2*A*A+1e-10:
    assert risk>=1/24-1e-12;good+=1
   rows.append(dict(d=d,n_keys=n,mode=mode,nuisance_variance=var,exact_enumerated_bit_error=risk));cases+=1
averages=[]
for N in [64,128,256]:
 total=F(0)
 for t in range(1,N):
  # All unit codes equal: corrected contrast sign is sign(sum_{j<=t}X_j).
  row=F(0)
  for k in range(t):
   z=2*k-(t-1)
   for target in [-1,1]:
    pred=1 if z+target>=0 else -1
    if pred!=target:row+=F(math.comb(t-1,k),2**t)
  total+=row
 avg=total/(N-1);bound=F(1,24)*max(F(0),1-F(K*5,N-1))
 assert avg>=bound
 averages.append(dict(N=N,average_error=float(avg),cover_bound=float(bound)))
# Verify the exact two-head normalization and self subtraction directly.
correction_checks=0
for i in [2,4,8,16]:
 us=[]
 for j in range(i):
  v=[rng.uniform(-1,1) for _ in range(3)];norm=math.sqrt(sum(x*x for x in v));us.append([x/norm for x in v])
 for _ in range(20):
  xs=[rng.choice([-1,1]) for j in range(i)]
  scores=[gamma*sum(a*b for a,b in zip(us[i-2],u)) for u in us]
  ew=list(map(math.exp,scores));den=sum(ew);H=sum(w*x for w,x in zip(ew,xs))/den;U=sum(xs)/i
  C=den/i*H-U-math.expm1(scores[-1])*xs[-1]/i
  ref=sum(math.expm1(s)*x for s,x in zip(scores[:-1],xs[:-1]))/i
  assert abs(C-ref)<1e-14;correction_checks+=1
print(json.dumps(dict(status='pass',same_code_average_checks=averages,correction_checks=correction_checks,cases=cases,variance_regime_cases=good,gamma=gamma,K=K,rows=rows,arithmetic='binary64 weights; exhaustive fair-sign enumeration',scope='tied positional-code scalar-sign interface, not arbitrary predictor risk'),indent=2))
