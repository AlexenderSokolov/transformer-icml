import sys
if not __debug__: raise RuntimeError("Run without -O: verification assertions must remain enabled")
import math,itertools,json,hashlib
from pathlib import Path

def ln(h):
 m=sum(h)/len(h);d=math.sqrt(1+sum((x-m)**2 for x in h)/len(h));return [(x-m)/d for x in h]
def model(xs):
 h=[[x,-x,0,0,0,0] for x in xs]+[[0.]*6]
 v=[ln(x)[0] for x in h];first=[]
 for i,row in enumerate(h):
  z=sum(v[:i+1])/(i+1);out=row[:];out[2]+=z;out[3]-=z;first.append(out)
 v=[ln(x)[2] for x in first];second=[]
 for i,row in enumerate(first):
  z=sum(v[:i+1])/(i+1);out=row[:];out[4]+=z;out[5]-=z;second.append(out)
 logit=ln(second[-1])[4];prob=1/(1+math.exp(-logit))
 return prob,first,second
x=[1,1,1,-1,-1,-1];y=[1,1,-1,1,-1,-1]
qx,hx,sx=model(x);qy,hy,sy=model(y)
c0=math.sqrt(3)/2;f=lambda u:c0*u/math.sqrt(4/3+u*u/4)
diff=(f(1)-f(1/3))/7
assert sum(x)==sum(y) and x[-2:]==y[-2:]
assert hx[-1]==hy[-1]==[0.]*6
assert abs((sx[-1][4]-sy[-1][4])-diff)<1e-14
assert qx>qy
rows=[];checks=4;maxnorm=0
c=.25;kappa=math.sqrt(4+8/c**2);A=math.sqrt(2)*c0*kappa;G=math.sqrt(3)/4
for N in [3,4,6,8,10]:
 for theta in [-.5,0,.5]:
  mass=0;err=0;risk=0
  for xs in itertools.product([-1,1],repeat=N):
   p=.25
   for i in range(N-2):p*=(1+theta*xs[i]*xs[i+1]*xs[i+2])/2
   q,hs,ss=model(xs);mass+=p;err+=p*abs(q-.5);risk+=p*abs(q-(1+theta*xs[-2]*xs[-1])/2)
   maxnorm=max(maxnorm,max(math.sqrt(sum(t*t for t in h)) for h in hs+ss))
  assert abs(mass-1)<1e-12
  assert err<=G*3*A/math.sqrt(N+1);checks+=2
  rows.append({'N':N,'theta':theta,'mean_abs_error_from_public_reference':err,'prediction_risk':risk,'conservative_bridge_error_bound':G*3*A/math.sqrt(N+1)})
r={'counterexample':{'word_x':x,'word_y':y,'q_x':qx,'q_y':qy,'probability_difference':qx-qy,'second_read_difference':diff,'global_key_array_norms':[0,0]},'finite_checks':checks,'max_observed_all_row_state_norm':maxnorm,'source_average_rows':rows,'scope':'actual two-read PreLN summary counterexample and finite source-average checks; no general risk-counterexample'}
p=Path(__file__).parent;(p/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='source_average_rows'}))
(p/'RECEIPT.json').write_text(json.dumps({'sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.name!='RECEIPT.json' and f.is_file()}},indent=2)+'\n')
