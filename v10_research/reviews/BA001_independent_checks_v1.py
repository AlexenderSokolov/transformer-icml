"""Independent finite corroboration only; does not execute original network."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,math,hashlib
ROOT=Path(__file__).resolve().parents[1]
checks=0
maxima=dict(variance=0.,mean_derivative=0.,ratio_derivative=0.,influence=0.)
# Exhaustively enumerate small active suffixes, including r>n and an exact full-history side port.
for r in (1,3,70):
 M=64;n=M+2;j=5;b=5;a=1
 bits=list(product((0,1),repeat=j))
 words=[[2]*(n-j)+list(z) for z in bits]
 sides=sorted(set(tuple(x[:min(r,n)]+x[-min(r,n):]) for x in words))
 for side in sides:
  q=sum((k+3)*(z+1) for k,z in enumerate(side))
  vals=[]
  for x in words:
   sums=[0,0,0]
   for i in range(2,n):
    window=([3]*max(0,r-i-1)+x[max(0,i-r+1):i+1])
    code=sum((k+1)*(z+2) for k,z in enumerate(window))
    w=1+(11*i+7*q+code)%5
    # Two scalar outputs share the exact denominator; signs include negative values.
    sums[0]+=w*(1 if (code+q+i)%2 else -1)
    sums[1]+=w*(1 if (code+3*q+2*i)%3 else -1)
    sums[2]+=w
   vals.append(sums)
  for idx,z in enumerate(bits):
   for k in range(j):
    other=list(z);other[k]=1-other[k];ii=bits.index(tuple(other))
    for c in range(3):
     ratio=abs(vals[idx][c]-vals[ii][c])/(2*b*r)
     assert ratio<=1;maxima['influence']=max(maxima['influence'],ratio);checks+=1
  for p in (F(1,4),F(2,5),F(1,2),F(3,4)):
   prob=[p**sum(z)*(1-p)**(j-sum(z)) for z in bits]
   dp=[pr*(sum(z)/p-(j-sum(z))/(1-p)) for pr,z in zip(prob,bits)]
   mu=[sum(pr*v[c] for pr,v in zip(prob,vals)) for c in range(3)]
   deriv=[sum(pr*v[c] for pr,v in zip(dp,vals)) for c in range(3)]
   for c in range(3):
    var=sum(pr*(v[c]-mu[c])**2 for pr,v in zip(prob,vals))
    vr=var/(2*b*b*r*r*j);dr=abs(deriv[c])/(2*b*r*j)
    assert 0<=vr<=1 and dr<=1
    maxima['variance']=max(maxima['variance'],float(vr));maxima['mean_derivative']=max(maxima['mean_derivative'],float(dr));checks+=2
   for c in range(2):
    hd=(deriv[c]*mu[2]-mu[c]*deriv[2])/mu[2]**2
    hr=abs(hd)/F(4*b*r*j,a*M);assert hr<=1
    maxima['ratio_derivative']=max(maxima['ratio_derivative'],float(hr));checks+=1
# Verify all-state pair minorization, including unused symbol and zero-mass target pairs.
for M in (64,127,1000):
 for beta in (F(0),F(1,10000),F(1,16)):
  beta0=max(beta,F(1,M));alpha=F(1,2*M);eta=beta0-alpha
  for p in (F(1,4),F(2,5),F(3,4)):
   pi=[eta/beta0,alpha*(1-p)/beta0,alpha*p/beta0,F(0)]
   T=[[1-alpha,alpha*(1-p),alpha*p,F(0)],*[ [eta,(1-eta)*(1-p),(1-eta)*p,F(0)] for _ in range(2)],pi]
   assert all(sum(pi[x]*T[x][y] for x in range(4))==pi[y] for y in range(4))
   for u,v,x,y in product(range(4),repeat=4):
    assert T[v][x]*T[x][y]>=beta0*pi[x]*T[x][y];checks+=1
# Nonintegral Q, both cutoff endpoints, and stationary event lower.
min_event_ratio=1e99;min_harmonic_ratio=1e99
for M in (64,65,127,256,1025):
 for beta in (0,1e-8,1/M,0.02,1/16):
  beta0=max(beta,1/M);alpha=1/(2*M);eta=beta0-alpha
  for Q in (1,1.1,math.sqrt(2),math.pi,M/4-0.01,M/4):
   U=min(1/(4*beta0),M*M/(4*Q*Q));J=math.floor(U);u=Q/M
   assert 4<=J<=M/4 and J>=U/2 and Q*math.sqrt(J)/M<=.5+1e-12
   ss=sum(1/(1+u*j) for j in range(2,J+1));rhs=math.log1p(u*J)/(4*u)
   assert ss>=rhs;min_harmonic_ratio=min(min_harmonic_ratio,ss/rhs)
   assert u*J+1e-12>=min(Q/(M*beta0),M/Q)/8
   for j in range(2,J+1):
    ej=(1-alpha/beta0)*(1-alpha)*alpha*(1-alpha)**(M-j)*(1-eta)**(j-1)
    assert ej>=1/(32*M);min_event_ratio=min(min_event_ratio,ej*32*M);checks+=1
   checks+=3
 for Q in (math.sqrt(M)*(1+1e-10),M/4+0.01,M,1e9):
  if Q>math.sqrt(M): assert 1/(128*math.sqrt(M+2))>=1/(256*Q);checks+=1
  if Q>M/4: assert 2/(8192*M)<=1/(128*math.sqrt(M+2));checks+=1
out=dict(status='PASS',checks=checks,max_observed_bound_ratios=maxima,min_event_to_claim_ratio=min_event_ratio,min_harmonic_to_claim_ratio=min_harmonic_ratio,fixtures={'M_local':64,'j_local':5,'r':[1,3,70],'shared_denominator':True,'negative_values':True,'all_supported_boundary_queries':True,'noninteger_Q':True,'all_state_unused_symbol':True},limitations=['Finite corroboration, not proof of arbitrary tables.','Independent LLM audit, not external or formal review.','No original emitted-network execution.'],manuscript_sha256=hashlib.sha256((ROOT/'bounded_attention/BA001_bounded_local_attention_lower_v1.md').read_bytes()).hexdigest())
(ROOT/'reviews/BA001_independent_checks_v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
