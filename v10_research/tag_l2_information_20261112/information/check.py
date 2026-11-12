import math,itertools,json
from fractions import Fraction
if not __debug__:raise RuntimeError('assertions required')
a=.5;sig=math.sqrt(1.5)
def ln(h):
 mu=sum(h)/len(h);s=math.sqrt(1+sum((v-mu)**2 for v in h)/len(h))
 return [(v-mu)/s for v in h]
def logistic(x):return 1/(1+math.exp(-x))
rows=[];err=0.;checks=0;maxnorm=0
for N in [2,3,4,6,8,10]:
 T=N+1;D=T+a*(1-2**-N);codes=[];preds=[];kl=0
 for xs in itertools.product([-1,1],repeat=N):
  hs=[]
  for j,x in enumerate(xs,1):
   k=math.log1p(a*2**-j);r=math.sqrt(1-k*k)
   hs.append([x,-x,k,-k,r,-r,1,-1,0,0,0,0])
  hs.append([0,0,0,0,math.sqrt(2),-math.sqrt(2),1,-1,0,0,0,0])
  z=list(map(ln,hs));q=[sig*v[6] for v in z];k=[sig*v[2] for v in z];val=[sig*v[0] for v in z];out=[]
  for i,h in enumerate(hs):
   w=[math.exp(q[i]*kk) for kk in k[:i+1]];H=sum(ww*vv for ww,vv in zip(w,val))/sum(w);U=sum(val[:i+1])/(i+1)
   C=D/(a*T)*H-U/a;hh=h[:];hh[8]+=C;hh[9]-=C;out.append(hh);maxnorm=max(maxnorm,math.sqrt(sum(x*x for x in hh)))
  exact=sum((Fraction(x,2**j) for j,x in enumerate(xs,1)),Fraction())/T
  pred=logistic(ln(out[-1])[8]);reference=logistic(float(exact)/math.sqrt(1.5+float(exact)**2/6))
  err=max(err,abs(pred-reference));assert abs(pred-reference)<1e-14
  codes.append(exact);preds.append(pred)
  ps=[]
  for theta in [.25,-.25]:
   p=.25
   for j in range(N-2):p*=(1+theta*xs[j]*xs[j+1]*xs[j+2])/2
   ps.append(p)
  kl+=ps[0]*math.log(ps[0]/ps[1]);checks+=1
 codes.sort();assert all(codes[j+1]-codes[j]==Fraction(2,2**N*T) for j in range(len(codes)-1));assert len(set(preds))==2**N
 p=.625;r=.375;target=(N-2)*(p*math.log(p/r)+(1-p)*math.log((1-p)/(1-r)))
 assert abs(kl-target)<1e-12
 rows.append(dict(N=N,words=2**N,exact_code_spacing=str(Fraction(2,2**N*T)),float_output_min_spacing=min(b-a for a,b in zip(sorted(preds),sorted(preds)[1:])),pushforward_KL=kl,innovation_KL=target))
print(json.dumps(dict(status='pass',actual_all_row_words=checks,max_formula_error=err,max_physical_state_norm=maxnorm,rows=rows,scope='candidate fixed-depth exact-real information-retention realization; no bounded-gain inverse decoder'),indent=2))
