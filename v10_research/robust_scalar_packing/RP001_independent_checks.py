from fractions import Fraction as F
import json,hashlib
from pathlib import Path
BASE=Path(__file__).parent

def tent(x): return 2*x-4*max(x-F(1,2),0)
def chain(x,k):
 for _ in range(k): x=tent(x)
 return x
def clip(x): return min(F(1),max(F(0),x))
def network(t,N):
 k=N.bit_length()-1
 v=chain(t,k); A=chain(t,k+1); B=chain(t/2+F(1,8*N),k+2)
 u=max(F(0),F(1,2)-B)
 for _ in range(k): u=min(F(1),2*u)
 z=min(1-A,u); s=A/2+z
 return clip((1+F(1,N))*v-F(1,2*N)),t-s/N

def geom(t,N):
 eta=F(1,2*N+2)
 if t==1:return F(0),F(1) # N is even
 i=(t*N).__floor__();r=t*N-i
 f=clip((r-eta)/(1-2*eta))
 X=f if i%2==0 else 1-f
 Y=F(i,N)+max(F(0),r-(1-eta))/(eta*N)
 return X,Y

def decode(q,N):
 eta=F(1,2*N+2);best=None
 for i in range(N):
  x=clip(q[0]);y=F(i,N); f=x if i%2==0 else 1-x
  candidates=[(x,y,(i+eta+(1-2*eta)*f)/N)]
  x=F(1 if i%2==0 else 0); y=min(F(i+1,N),max(F(i,N),q[1]))
  candidates.append((x,y,F(i+1,N)-eta/N+eta*(y-F(i,N))))
  for x,y,t in candidates:
   dist=(x-q[0])**2+(y-q[1])**2
   if best is None or dist<best[0]:best=(dist,t,x,y)
 assert network(best[1],N)==best[2:]
 return best[1]

out={'formula_cases':0,'exact_grid_cases':0,'uniform_lattice_cases':0,'noise_label_cases':0,'local_inverse_cases':0,'max_error_over_bound':0.0}
for N in [2,4,8,16,32]:
 eta=F(1,2*N+2);Q=16*N;h=Q.bit_length()-1;k=N.bit_length()-1;p=2*h;P=p+2*k+6
 points={F(j,512) for j in range(513)}
 for i in range(N):
  for r in [F(0),eta/2,eta,eta+F(1,100*N),F(1,2),1-eta-F(1,100*N),1-eta,1-eta/2,F(1)]:points.add((i+r)/N)
 for t in sorted(points):
  w=network(t,N);assert w==geom(t,N),(N,t,w,geom(t,N));out['formula_cases']+=1
  # Coarse input lattice embedded into larger fractional lattice: endpoint rails exact.
  tp=F((t*(1<<p)).__floor__(),1<<p);wp=network(tp,N)
  assert all((z*(1<<P)).denominator==1 for z in wp);out['exact_grid_cases']+=1
  # Independently test the revised same-uniform-grid implementation and each divisibility.
  D=1<<p;v=chain(tp,k);A=chain(tp,k+1);u0=tp+F(1,4*N)
  ext=2*u0-4*max(u0-F(1,2),0)+4*max(u0-1,0)
  B=chain(ext,k)
  assert B==chain(tp/2+F(1,8*N),k+2)
  assert (v*(1<<(p-k))).denominator==1
  assert (A*(1<<(p-k-1))).denominator==1 and (B*(1<<(p-k-1))).denominator==1
  u=max(F(0),F(1,2)-B)
  for _ in range(k):u=min(F(1),2*u);assert (u*D).denominator==1
  z=min(1-A,u);s=A/2+z
  for val in [u0,ext,v,A,B,u,z,s,v/N,s/N]:assert (val*D).denominator==1
  assert (clip(v+v/N-F(1,2*N)),tp-s/N)==wp
  out['uniform_lattice_cases']+=1
  # Enumerate every feasible floor label coordinate for the c=1/4 perturbation cube.
  c=F(1,4); ranges=[]
  for z in w:
   lo=(clip(z-c/Q)*Q).__floor__();hi=(clip(z+c/Q)*Q).__floor__()
   ranges.append(range(lo,hi+1))
  bound=4*(c+1)/(Q*N)+F(1,N*N)
  for ix in ranges[0]:
   for iy in ranges[1]:
    td=decode((F(ix,Q),F(iy,Q)),N);err=abs(td-t)
    assert err<=bound,(N,t,ix,iy,err,bound)
    out['noise_label_cases']+=1;out['max_error_over_bound']=max(out['max_error_over_bound'],float(err/bound))
 # Exact local inverse lemma checked without irrational arithmetic: sqrt2*d <= 2 maxcoordinate distance.
 pts=sorted(points)
 for t in pts:
  for dt in [F(0),eta/N,F(1,8*N*N),F(1,4*N*N)]:
   u=min(F(1),t+dt);wt=network(t,N);wu=network(u,N);D=sum((x-y)**2 for x,y in zip(wt,wu))
   if D<F(1,N*N):
    excess=max(F(0),abs(t-u)-2*eta/N)
    assert excess**2*N*N<=2*D,(N,t,u,D,excess)
    out['local_inverse_cases']+=1
out['theorem_sha256']=hashlib.sha256((BASE/'RP001_theorem.md').read_bytes()).hexdigest()
out['status']='PASS'
(BASE/'RP001_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
