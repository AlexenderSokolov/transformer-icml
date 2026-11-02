"""Finite corroboration, not universal proof or original-emitter execution."""
from fractions import Fraction as F
from itertools import product
import math,json,hashlib
from pathlib import Path
root=Path(__file__).parent
checks=0
max_var_ratio=0.;max_deriv_ratio=0.;max_ratio_deriv=0.;ratio_expectation_gap=0.
M=64;r=3;a=1;b=6
for j in [2,3,5,7]:
 words=[]
 for bits in product([0,1], repeat=j):
  x=[2]*(M+2-j)+list(bits)
  for s in range(3):
   for d in range(2):
    A=D=0
    for i in range(2,M+2):
     local=x[max(0,i-r+1):i+1]
     code=sum((z+1)*5**k for k,z in enumerate(local))
     w=1+(17*i+7*s+11*d+code)%6
     v=F(((13*i+3*s+7*d+code)%5)-2,2)
     A+=w*v;D+=w
    words.append((bits,s,d,A,F(D)))
 for p in [F(1,4),F(1,2),F(3,4)]:
  for s in range(3):
   for d in range(2):
    rows=[z for z in words if z[1:3]==(s,d)]
    means=[F(0),F(0)]; seconds=[F(0),F(0)];derivs=[F(0),F(0)];eratio=F(0)
    for bits,_,_,A,D in rows:
     k=sum(bits);weight=p**k*(1-p)**(j-k)
     score=F(k)/p-F(j-k)/(1-p)
     for q,z in enumerate([A,D]):
      means[q]+=weight*z;seconds[q]+=weight*z*z;derivs[q]+=weight*score*z
     eratio+=weight*A/D
    for q in range(2):
     var=seconds[q]-means[q]**2
     assert 0<=var<=2*b*b*r*r*j
     assert abs(derivs[q])<=2*b*r*j
     max_var_ratio=max(max_var_ratio,float(var/(2*b*b*r*r*j)))
     max_deriv_ratio=max(max_deriv_ratio,float(abs(derivs[q])/(2*b*r*j)))
     checks+=2
    assert means[1]>=a*M
    hd=(derivs[0]*means[1]-means[0]*derivs[1])/means[1]**2
    assert abs(hd)<=F(4*b*r*j,a*M)
    max_ratio_deriv=max(max_ratio_deriv,float(abs(hd)/F(4*b*r*j,a*M)))
    ratio_expectation_gap=max(ratio_expectation_gap,float(abs(eratio-means[0]/means[1])))
    checks+=2
assert ratio_expectation_gap>0 # fixture confirms ratio means is NOT mean ratio
for M in [64,128,257,1024,4096]:
 for beta0 in [1/M, min(2/M,1/16),1/16]:
  for Q in [1,2,4,8,16,M/8,M/4]:
   U=min(1/(4*beta0), M*M/(4*Q*Q));J=math.floor(U);u=Q/M
   assert J>=4 and J>=U/2 and J<=M/4 and beta0*J<=.25000000001
   assert Q*math.sqrt(J)/M<=.50000000001
   S=sum(1/(1+u*j) for j in range(2,J+1))
   assert S+1e-12>=math.log1p(u*J)/(4*u)
   assert u*J+1e-12>=min(Q/(M*beta0),M/Q)/8
   checks+=4
out={'status':'PASS','kind':'author finite exact local-sum and numerical cutoff corroboration','checks':checks,'max_variance_to_bound':max_var_ratio,'max_mean_derivative_to_bound':max_deriv_ratio,'max_ratio_curve_derivative_to_bound':max_ratio_deriv,'nonzero_ratio_of_means_vs_mean_ratio_gap':ratio_expectation_gap,'limitations':['not independent review','not formal verification','not original emitted-network execution','does not test every table or source'], 'manuscript_sha256':hashlib.sha256((root/'BA001_bounded_local_attention_lower_v1.md').read_bytes()).hexdigest()}
(root/'BA001_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
