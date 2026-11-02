import numpy as np, json
rng=np.random.default_rng(20261102)
max_hit_ratio=0.; max_mgf_ratio=0.; count=0
for _ in range(10000):
 a,b,e,t=np.exp(rng.uniform(np.log(1e-7),0,4))
 P=np.array([[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]])
 x=1/(e/a+2+b/t); pi=np.array([x*e/a,x,x,x*b/t]); beta=np.min((P@P)/pi[None,:])
 for s,q in enumerate([a,1,1,t]):
  ids=[i for i in range(4) if i!=s]; T=P[np.ix_(ids,ids)]; h=np.linalg.solve(np.eye(3)-T,np.ones(3)); H=max(h)
  rat=np.sqrt(beta)*pi[s]*q*H; max_hit_ratio=max(max_hit_ratio,rat)
  lam=np.sqrt(beta)*pi[s]*q/24; u=np.exp(lam)
  hitpgf=np.linalg.solve(np.eye(3)-u*T,u*P[ids,s]); pgf=u*(P[s,s]+P[s,ids]@hitpgf)
  # Additive rather than relative log error robust for tiny lambda.
  rhs=np.exp(2*lam/pi[s]); max_mgf_ratio=max(max_mgf_ratio,pgf/rhs)
  if rat>5+1e-8 or pgf>rhs+1e-7: raise AssertionError((a,b,e,t,s,rat,pgf,rhs))
  count+=1
print(json.dumps(dict(cases=count,max_sqrtbeta_pq_H=max_hit_ratio,max_mgf_over_bound=max_mgf_ratio,seed=20261102,scope='finite corroboration only'),indent=2))
