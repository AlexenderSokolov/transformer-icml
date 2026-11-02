import numpy as np
max_main=0; max_coeff_excess=0; cases=0
for b,t in [(.5,.5),(.001,.8),(.8,.001),(1e-6,1e-6),(.999,.999),(.01,.99),(.99,.01),(.2,.3)]:
 R=np.array([[0,1-b,b],[1,0,0],[0,t,1-t]],float)
 for M in [8,9,16,31,64,100]:
  nmax=M+2
  DA=np.zeros(nmax+1);DC=DA.copy()
  for n in range(1,nmax+1):
   if n%2:DA[n]=b*(1-b)**((n-1)//2)
   if n>=2:DC[n]=t*(1-t)**(n-2)
  F=np.convolve(DA,DC)[:nmax+1]
  # Nonnegative series accumulation, avoiding nearly singular log cancellation.
  L=np.zeros_like(F);fk=F.copy()
  for k in range(1,nmax//3+1):
   L+=fk/k;fk=np.convolve(fk,F)[:nmax+1]
  convA=np.convolve(DA,L)[:nmax+1];convC=np.convolve(DC,L)[:nmax+1]
  for init in range(3):
   for target,q in [(0,b),(2,t)]:
    d=np.zeros((3,M+1));d[init,0]=1
    for time in range(M):
     nxt=np.zeros_like(d)
     for s in range(3):
      counts=d[s]
      if s==target:
       counts=np.concatenate(([0.],counts[:-1]))
      nxt+=R[s,:,None]*counts[None,:]
     d=nxt
    val=np.sum(d[target]*q/(1+q*np.arange(M+1)))
    max_main=max(max_main,val*M/64)
    if init==0 and target==0:
     exceptional= b*(1-b)**(M//2)/(1+b*M/2) if M%2==0 else 0
     upper=L[M]+exceptional
    elif init==2 and target==0:upper=convC[M]+F[M+1]
    elif init==2 and target==2:upper=L[M]+t*(1-t)**M
    elif init==0 and target==2:upper=convA[M]+F[M+2]
    else:continue
    max_coeff_excess=max(max_coeff_excess,val-upper)
    assert val<=upper+1e-12,(b,t,M,init,target,val,upper)
    assert val<=64/M+1e-12
    cases+=1
print({'exact_terminal_DP_vs_run_coefficient_comparisons':cases,'max_coefficient_excess':max_coeff_excess,'max_ratio_to_64_over_M':max_main})
