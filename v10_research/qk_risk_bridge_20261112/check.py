import math,itertools,json,random
if not __debug__:raise RuntimeError('assertions required')
rng=random.Random(20261112);checks=0;ratio=0
for n in [3,8,32,128]:
 for d in [1,3,8]:
  for _ in range(20):
   q=[rng.uniform(-1,1) for j in range(d)];qn=math.sqrt(sum(v*v for v in q));q=[v/qn for v in q]
   K=[[rng.uniform(-1,1) for j in range(d)] for i in range(n)];kf=math.sqrt(sum(v*v for row in K for v in row));K=[[v/kf for v in row] for row in K]
   s=[sum(x*y for x,y in zip(row,q)) for row in K];S=max(map(abs,s));sn=math.sqrt(sum(v*v for v in s));ex=[math.exp(v) for v in s];w=[v/sum(ex) for v in ex]
   diff=sum(abs(v-1/n) for v in w);bound=2*math.exp(2*S)*sn/math.sqrt(n)
   assert diff<=bound+1e-14;assert sn<=1+1e-14;ratio=max(ratio,diff/bound);checks+=1
risks=[]
for N in [3,4,6,8,10]:
 # rank-one, nonzero, globally F=Q=1; values raw signs.
 k=[(j+1)/math.sqrt(sum(i*i for i in range(1,N+1))) for j in range(N)]
 ex=[math.exp(x) for x in k];w=[x/sum(ex) for x in ex];gain=2.;G=gain/4
 actual=reference=dist=0
 for xs in itertools.product([-1,1],repeat=N):
  tau=xs[-2]*xs[-1];v=sum(p*x for p,x in zip(w,xs));v0=sum(xs)/N
  pred=1/(1+math.exp(-gain*tau*v));pred0=1/(1+math.exp(-gain*tau*v0))
  assert abs(pred-pred0)<=G*abs(v-v0)+1e-14
  for th in [-.5,.5]:
   prob=.25
   for j in range(N-2):prob*=(1+th*xs[j]*xs[j+1]*xs[j+2])/2
   target=(1+th*tau)/2
   actual+=prob*abs(pred-target)/2;reference+=prob*abs(pred0-target)/2;dist+=prob*abs(pred-pred0)/2
 assert actual>=reference-dist-1e-13
 risks.append(dict(N=N,actual_risk=actual,uniform_reference_risk=reference,expected_prediction_difference=dist))
print(json.dumps(dict(status='pass',softmax_checks=checks,max_bound_ratio=ratio,exhaustive_risk_checks=risks,scope='single raw-value retrieval; nonzero globally norm-bounded QK; binary64 diagnostic'),indent=2))
