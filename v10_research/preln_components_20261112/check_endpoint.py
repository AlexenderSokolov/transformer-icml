import math,json,random

def norm(x):return math.sqrt(sum(t*t for t in x))
def ln(h,eps):
 m=sum(h)/len(h);v=sum((x-m)**2 for x in h)/len(h)
 return [(x-m)/math.sqrt(v+eps) for x in h]
def block(h,eps,K,sigma,which):
 y=ln(h,eps);out=h[:]
 if which==0:
  z=sigma*abs(y[4]+y[6])-1;out[10]+=z;out[11]-=z
 else:
  d=sigma*(max(0,-y[0]-K*y[10])-max(0,y[0]-K*y[10]))
  out[0]+=d;out[1]-=d
 return out
def sigmoid(x):return 1/(1+math.exp(-x))
def read(h,epsf,sf):return sigmoid(sf*ln(h,epsf)[0])
if __name__=='__main__':
 if not __debug__:raise RuntimeError('assertions required')
 rng=random.Random(20261112);clean=noisy=0;max_clean=max_err=max_ratio=0.
 for c in (.1,.25,.4):
  a=1-2*c;K=math.log((1-c)/c)+1
  for eps in (.01,.1,1.):
   s0=math.sqrt((2*K*K+6)/13+eps);s1=math.sqrt((2*K*K+8)/13+eps)
   B0=1+2*s0/math.sqrt(eps);B1=1+4*s1*max(1,K)/math.sqrt(eps)
   for epsf in (.02,.5):
    sf=math.sqrt((2*K*K+8)/13+epsf)
    for theta in (-a,-a/2,0,a/3,a):
     ell=math.log((1+theta)/(1-theta));r=math.sqrt(K*K-ell*ell)
     for x in (-1,1):
      for y in (-1,1):
       h=[ell,-ell,r,-r,x,-x,y,-y,1,-1,0,0,0];q=(1+theta*x*y)/2
       out=block(block(h,eps,K,s0,0),eps,K,s1,1)
       assert abs(sum(out))<1e-13
       assert abs(sum(v*v for v in out)-(2*K*K+8))<1e-12
       err=abs(read(out,epsf,sf)-q);assert err<2e-14
       max_clean=max(max_clean,err);clean+=1
       for mode in range(4):
        delta=1e-6;eta=delta/2
        def perturb(v,budget,site):
         if mode==0:d=[1.]*13
         elif mode==1:d=[-1.]*13
         elif mode==2:d=[1. if j==0 else 0. for j in range(13)]
         else:d=[rng.uniform(-1,1) for _ in range(13)]
         scale=budget/norm(d)
         return [a+scale*b for a,b in zip(v,d)]
        z=perturb(h,eta,0)
        z=perturb(block(perturb(z,delta,1),eps,K,s0,0),delta,2)
        z=perturb(block(perturb(z,delta,3),eps,K,s1,1),delta,4)
        bound=sf*(B1*(B0*(eta+delta)+2*delta)+delta)/(4*math.sqrt(epsf))
        err=abs(read(z,epsf,sf)-q)
        assert err<=bound+2e-14
        max_err=max(max_err,err);max_ratio=max(max_ratio,err/bound);noisy+=1
 print(json.dumps({'clean_cases':clean,'noisy_cases':noisy,'max_clean_probability_error':max_clean,'max_noisy_probability_error':max_err,'max_error_bound_ratio':max_ratio,'arithmetic':'float64 diagnostic, not interval certification','scope':'two-block paired-lane full-PreLN plus mandatory final-LN endpoint gadget only; estimator/logit-padding construction not tested'},indent=2))
