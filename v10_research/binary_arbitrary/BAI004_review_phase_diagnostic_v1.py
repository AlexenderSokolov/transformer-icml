"""Fresh review of the NEW section9 convolution, not proof."""
import json,numpy as np
rng=np.random.default_rng(45113);maxerr=0.;cases=0;maxratio=0.
params=[tuple(rng.uniform(.001,.999,4)) for _ in range(80)]
params += [(a,b,e,t) for a,b,e,t in [(.1,0,.3,0),(.1,1,.3,1),(.001,.3,.2,.001),(.99,.01,.99,.99)]]
M=64;As=[.0001,.1,1.,10.,1000.]
for a,b,e,t in params:
 P=np.array([[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]])
 vals=[]
 for target in [1,2]:
  dp=np.zeros((M+1,4));dp[0,0]=1;v=np.zeros((len(As),M+1))
  for n in range(M+1):
   for j,A0 in enumerate(As):v[j,n]=np.sum(dp[:,target]*np.minimum(1,A0/(np.arange(M+1)+2)))
   if n==M:break
   nd=np.zeros_like(dp)
   for i in range(4):
    h=int(i==target);nd[h:n+h+1]+=dp[:n+1,i,None]*P[i]
   dp=nd
  vals.append(v)
 U=np.zeros(M+1);U[1]=1-b
 for l in range(2,M+1):U[l]=b*t*(1-t)**(l-2)
 for j,A0 in enumerate(As):
  conv=np.convolve(vals[0][j],U)[:M+1]
  err=float(np.max(abs(conv-vals[1][j])));maxerr=max(maxerr,err)
  assert err<1e-11;cases+=M
  if b>0 and t>0:
   x=1/(e/a+2+b/t);pi=np.array([x*e/a,x,x,x*b/t]);beta=float(np.min((P@P)/pi))
  else:beta=0
  for n in [8,15,16,31,64]:
   bound=min(1,100*A0/n*(1+np.log1p(1/(max(np.sqrt(beta),1/n)*A0))))
   assert vals[1][j,n]<=bound+1e-11
   maxratio=max(maxratio,vals[1][j,n]/bound)
print(json.dumps(dict(status='PASS',parameter_sets=len(params),convolution_horizon_comparisons=cases,
 maximum_convolution_absolute_error=maxerr,maximum_main_bound_ratio=maxratio),indent=2))
