from fractions import Fraction as F
import json, math
from pathlib import Path

def tent(x): return 2*min(x,1-x)
def it(x,k):
 for _ in range(k): x=tent(x)
 return x
def clip(x): return min(F(1),max(F(0),x))
def enc(t,k):
 N=2**k; v=it(t,k); A=it(t,k+1); B=it(t/2+F(1,8*N),k+2)
 u=max(F(0),F(1,2)-B)
 for _ in range(k): u=min(F(1),2*u)
 s=A/2+min(1-A,u)
 return clip((1+F(1,N))*v-F(1,2*N)),t-s/N

def geom(t,k):
 N=2**k; eta=F(1,2*N+2)
 if t==1:return F(0),F(1) # N even => final endpoint0
 i=int(N*t); r=N*t-i
 y=F(i,N)+max(F(0),r-(1-eta))/(N*eta)
 f=clip((r-eta)/(1-2*eta))
 return (f if i%2==0 else 1-f),y

def decode(q,k):
 N=2**k; eta=F(1,2*N+2); best=None
 for i in range(N):
  w=(clip(q[0]),F(i,N)); f=w[0] if i%2==0 else 1-w[0]
  t=(i+eta+(1-2*eta)*f)/N
  dist=sum((u-v)**2 for u,v in zip(q,w))
  if best is None or dist<best[0]:best=dist,t
  w=(F(1 if i%2==0 else 0), min(F(i+1,N),max(F(i,N),q[1])))
  t=F(i+1,N)-eta/N+eta*(w[1]-F(i,N))
  dist=sum((u-v)**2 for u,v in zip(q,w))
  if dist<best[0]:best=dist,t
 return best[1]

formula_cases=noise_cases=lattice_cases=0; max_ratio=0.
for h in range(3,8):
 for k in range(1,h-1):
  N=2**k; D=2**(2*h)
  for j in range(0,D+1,max(1,D//4096)):
   t=F(j,D); u=t+F(1,4*N)
   b0=2*u-4*max(F(0),u-F(1,2))+4*max(F(0),u-1)
   B=it(b0,k); A=it(t,k+1); v=it(t,k)
   assert B==it(t/2+F(1,8*N),k+2)
   z=min(1-A,N*max(F(0),F(1,2)-B)); ss=A/2+z
   for value in [u,b0,B,A,v,v/N,ss/N,*enc(t,k)]: assert (D*value).denominator==1
   assert (v*F(D,N)).denominator==1
   assert (A*F(D,2*N)).denominator==1 and (B*F(D,2*N)).denominator==1
   lattice_cases+=1
for k in range(1,6):
 N=2**k; eta=F(1,2*N+2)
 ts={F(j,2048) for j in range(2049)}
 for i in range(N):
  for r in [F(0),eta/2,eta,1-eta,1-eta/2,F(1)]:ts.add((i+r)/N)
 for t in ts:
  assert enc(t,k)==geom(t,k),(k,t,enc(t,k),geom(t,k))
  formula_cases+=1
 # All corner perturbations, boundary cases and moderate fine-grid coverage.
 Q=16*N;c=F(1,4); bound=4*(c+1)/(Q*N)+F(1,N*N)
 selected={F(j,128) for j in range(129)}|{(i+r)/N for i in range(N) for r in [F(0),eta/2,eta,1-eta,1-eta/2,F(1)]}
 for t in selected:
  w=enc(t,k)
  for ex in [-c/Q,F(0),c/Q]:
   for ey in [-c/Q,F(0),c/Q]:
    q=tuple(F(int(Q*clip(z+e)),Q) for z,e in zip(w,(ex,ey)))
    recovered=decode(q,k); error=abs(recovered-t)
    assert error<=bound,(k,t,q,error,bound)
    max_ratio=max(max_ratio,float(error/bound));noise_cases+=1
out={'status':'PASS','uniform_lattice_cases':lattice_cases,'formula_exact_cases':formula_cases,'adversarial_quantization_cases':noise_cases,'max_error_over_bound':max_ratio,'scope':'finite exact diagnostics, not proof or emitted-network certification'}
Path(__file__).with_name('RP001_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
