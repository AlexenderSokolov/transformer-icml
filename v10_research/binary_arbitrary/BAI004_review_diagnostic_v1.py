"""Fresh reviewer finite corroboration, not a proof."""
import json
import numpy as np
rng=np.random.default_rng(44602)
scalar_n=0;main_n=0;trace_n=0;max_main_ratio=0.;max_count_ratio=0.
for k in range(500):
 if k<250:a,b,e,t=rng.uniform(.001,.999,4)
 else:a,b,e,t=10.**(-rng.uniform(.01,6,4))
 P=np.array([[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]])
 x=1/(e/a+2+b/t);pi=np.array([x*e/a,x,x,x*b/t]);beta=float(np.min((P@P)/pi))
 M=[8,16,64,256][k%4]
 assert np.max(abs(pi@P-pi))<1e-12
 K=min(1/e,(1+M*t)/b)
 if beta*M*M>=1:
  assert K<=12*(1+M*a)/np.sqrt(beta)+1e-9;scalar_n+=1
 # Truncated killed-excursion count at times0,...,M.
 T=P[1:,1:];v=np.array([1.,0,0]);EN=0.
 for n in range(M+1):
  EN+=v[0];v=v@T
 assert EN<=K+1e-8
 max_count_ratio=max(max_count_ratio,EN/K)
 v=np.array([0.,1,0,0]);EV=0.
 for n in range(M+1):EV+=v[1];v=v@P
 assert EV<=(1+M*a)*K+1e-8
 # Direct terminal-A local-time law fromW.
 if k<100:
  d=np.zeros((M+1,4));d[0,0]=1
  for n in range(M):
   nd=np.zeros_like(d)
   for i in range(4):
    h=int(i==1);nd[h:n+h+1]+=d[:n+1,i,None]*P[i]
   d=nd
  for A0 in [.0001,.01,.5,2.,10.,1000.]:
   val=float(np.sum(d[:,1]*np.minimum(1,A0/(np.arange(M+1)+2))))
   bound=min(1,40*A0/M*(1+np.log1p(1/(max(np.sqrt(beta),1/M)*A0))))
   assert val<=bound+1e-10
   max_main_ratio=max(max_main_ratio,val/bound);main_n+=1
# Independently verify general return-trace identity using count DP.
for _ in range(20):
 dstate=4;P=rng.uniform(0,1,(4,4));P/=P.sum(axis=1)[:,None]
 for s in range(4):
  T=np.delete(np.delete(P,s,0),s,1);dp=np.zeros((13,4));dp[0,s]=1
  for n in range(1,13):
   nd=np.zeros_like(dp)
   for i in range(4):
    h=int(i==s);nd[h:n+h]+=dp[:n,i,None]*P[i]
   dp=nd
   val=float(np.sum(dp[1:,s]/np.arange(1,13)))
   tr=(np.trace(np.linalg.matrix_power(P,n))-np.trace(np.linalg.matrix_power(T,n)))/n
   assert abs(val-tr)<1e-11 and val<=4/n+1e-11
   trace_n+=1
print(json.dumps(dict(status='PASS',source_cases=500,positive_gamma_scalar_checks=scalar_n,
 main_terminal_count_cases=main_n,general_trace_identity_cases=trace_n,
 max_main_ratio=max_main_ratio,max_truncated_count_ratio=max_count_ratio),indent=2))
