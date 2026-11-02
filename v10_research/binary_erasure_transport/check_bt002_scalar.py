"""Finite stress check for BT002 scalar inequalities; not a replacement for proof."""
import math,json
count=0; worst1=0.;worst3=0.
for M in [64,65,100,256,1000,10000,10**6,10**9,10**12]:
 ks=sorted({1,2,3,4,8,16,M,max(1,int(M**.25)),max(1,int(M**.25)+1),max(1,int(M**.5)),max(1,int(M**.75)),max(1,int(M/math.log(M)))})
 for k in ks:
  if k>M:continue
  for e in [1/M,2/M,1/math.sqrt(M),.01,.1,1]:
   if e<1/M:continue
   for c in [2**-44,1e-9,1e-4,.01,1,10]:
    for C in [.01,1,4,8,100]:
     s=M**-.5;eps=k/M;A=1/(e*k);B=c*k/math.log(k+2)
     F=eps*(1+math.log1p(A));L=math.log1p(min(A/C,B))
     D=7+math.log(max(1,C))+6*math.log(max(1,2/c))
     rat=F/(D*max(s,eps,eps*L));assert rat<=1+1e-12
     worst1=max(worst1,rat);count+=1
    # Evaluate the sum by a direct finite loop when modest; otherwise
    # use its rigorous integral lower bound, making the test stronger.
    for C in [1,4,8,100]:
     U=min(1/(C*e),c*k*k/math.log(k+2));J=math.floor(U)
     for j0 in [1,6,100,4096,4097,10000]:
      T=0 if J<j0 else (sum(1/(1+j/k) for j in range(j0,J+1))/M if J-j0<10000 else eps*math.log((k+J+1)/(k+j0)))
      D=7+math.log(max(1,C))+6*math.log(max(1,2/c))
      rat=F/(D*(1+math.log1p(j0))*max(s,eps,T));assert rat<=1+1e-12
      worst3=max(worst3,rat);count+=1
out={'status':'PASS','inequalities_checked':count,'largest_SCALAR1_ratio':worst1,'largest_SCALAR3_ratio':worst3,'scope':'Finite diagnostics; proof in BT002_scalar_completion.md'}
print(json.dumps(out,indent=2))
open('v10_research/binary_erasure_transport/BT002_scalar_checks.json','w').write(json.dumps(out,indent=2)+'\n')
