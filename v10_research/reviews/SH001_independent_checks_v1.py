#!/usr/bin/env python3
"""Independent finite corroboration, not a proof or emitted-network test."""
from fractions import Fraction as F
from itertools import product
from math import sqrt, log1p, exp, ceil, floor
from pathlib import Path
import json, hashlib
out={'status':'PASS','cutoff_cases':0,'necessity_cases':0,'local_moment_cases':0,'influence_checks':0}
mins={'event_ratio':100.,'harmonic_ratio':100.}
for M in [64,65,127,128,255,1024,10000]:
 for beta in [0,1/(2*M),1/M,1/32,1/16]:
  b=max(beta,1/M)
  for k in [1,1.5,2,3.125,8,16]:
   for Q in [1,1.25,sqrt(M)/2,sqrt(M),M/(4*k),M/(4*k)*(1-1e-9)]:
    z=k*Q
    if Q<1 or z>M/4: continue
    U=min(1/(4*b),M*M/(4*z*z)); J=floor(U+1e-12)
    assert J>=4 and J>=U/2-1e-10 and J<=M/4+1e-10
    assert b*J<=.25+1e-12 and z*sqrt(J)/M<=.5+1e-12
    u=z/M
    assert u*J+1e-12>=min(z/(M*b),M/z)/8
    harmonic=sum(1/(1+u*j) for j in range(2,J+1))
    ratio=harmonic/(log1p(u*J)/(4*u)); assert ratio>=1-1e-12
    mins['harmonic_ratio']=min(mins['harmonic_ratio'],ratio)
    a=1/(2*M); eta=b-a
    for j in [2,J]:
     event=(1-a/b)*(1-a)*a*(1-a)**(M-j)*(1-eta)**(j-1)
     ratio=event*32*M; assert ratio>=1-1e-10
     mins['event_ratio']=min(mins['event_ratio'],ratio)
    out['cutoff_cases']+=1
# Numerically choose a conservative F, and test the exact branches used.
for cp in [.001,.1,1,2,10,1e3]:
 FF=max(16.,16+8*log1p(16*cp*cp))
 for s in [FF+i/4 for i in range(401)]:
  assert (exp(s-1)-1)/(8*cp*cp*s)>=exp(s/2)-1
 for M in [64.,1e4,1e12,1e30,1e100]:
  for q in [.25,.5,1]:
   Q=cp*sqrt(M)*q
   if Q<1: continue
   for beta in [0,1/M,1/sqrt(M),1/16,.07,1]:
    b=max(beta,1/M); x=Q/(M*b); f=1+log1p(x)
    ki=ceil(f); assert ki<=2*f and (1+log1p(ki*x))/ki<=2
    for k in [1,1.5,max(1,f/2),f,2*f]:
     z=k*Q
     if beta>1/16: assert f<=1+2*cp+1e-12
     elif z>M/4: assert k>=f/(4*cp*(.125+cp))-1e-12
     elif f>FF and k<f:
      assert log1p(k*x/8)>=f/2-1e-12
      assert log1p(M/(8*k*Q))>=f/2-1e-12
     out['necessity_cases']+=1
# Exact rational, positional/query-dependent local tables, negative values,
# and boundary overlap (r=70>n). Freeze each s BEFORE taking moments.
M=64; n=M+2; j=4; words=list(product([0,1],repeat=j))
for r in [1,3,70]:
 histories={bits:(2,)*(n-j)+bits for bits in words}
 sides=set(h[:min(r,n)]+h[-min(r,n):] for h in histories.values())
 for k in [F(1),F(3,2),F(4)]:
  for s in sides:
   sid=sum((i+1)*(a+1) for i,a in enumerate(s))
   for d in [0,1]:
    sums={}
    for bits,h in histories.items():
     A=F(0); den=F(0)
     for i in range(2,n):
      win=h[max(0,i-r+1):i+1]
      code=sum((a+1)*(t+3) for t,a in enumerate(win))+17*i+11*d+sid
      w=1+(k-1)*F(code%7,6); v=F((code*5+3)%9-4,4)
      A+=w*v; den+=w
     sums[bits]=(A,den)
    for bits in words:
     for t in range(j):
      other=bits[:t]+(1-bits[t],)+bits[t+1:]
      for col in [0,1]:
       assert abs(sums[bits][col]-sums[other][col])<=2*k*r
       out['influence_checks']+=1
    for p in [F(1,4),F(1,2),F(3,4)]:
     probs={bits:p**sum(bits)*(1-p)**(j-sum(bits)) for bits in words}
     means=[sum(probs[b]*sums[b][c] for b in words) for c in [0,1]]
     deriv=[sum(probs[b]*(F(sum(b))/p-F(j-sum(b))/(1-p))*sums[b][c] for b in words) for c in [0,1]]
     for c in [0,1]:
      var=sum(probs[b]*(sums[b][c]-means[c])**2 for b in words)
      assert var<=2*k*k*r*r*j and abs(deriv[c])<=2*k*r*j
     hp=(deriv[0]*means[1]-means[0]*deriv[1])/means[1]**2
     assert abs(hp)<=4*k*r*j/F(M)
     assert means[1]>=M and abs(means[0]/means[1])<=1
     out['local_moment_cases']+=1
out.update(mins)
root=Path(__file__).resolve().parents[1]
target=root/'score_precision/SH001_sharp_weight_ratio_threshold_v1.md'
out['target_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
