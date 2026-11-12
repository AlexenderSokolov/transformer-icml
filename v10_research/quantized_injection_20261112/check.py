import math,itertools,json
if not __debug__:raise RuntimeError('Do not use -O')
checks=0; rows=[]
for N in (4,6,8,10):
 ps=[i/(N+1) for i in range(1,N+1)];vs=[2*math.sqrt(2)/math.sqrt(3+p*p) for p in ps]
 gs=[2*math.sqrt(2/3)*v*p for v,p in zip(vs,ps)];Z=math.exp(8/3)+sum(map(math.exp,gs));ws=[math.exp(g)*v/Z for g,v in zip(gs,vs)]
 for Delta in (1.,.5,.25):
  laws=[];epss=[]; ent=[]
  for th in (-.5,.5):
   law={};ey=0;mass=0
   for x in itertools.product((-1,1),repeat=N):
    pr=.25
    for j in range(2,N):pr*=(1+th*x[j-2]*x[j-1]*x[j])/2
    A=sum(w*s for w,s in zip(ws,x));y=math.floor(A/Delta+.5);key=(y,x[-2:]);law[key]=law.get(key,0)+pr;mass+=pr;ey+=pr*A*A
   exact=sum(w*w for w in ws)+2*sum(ws[i]*ws[j]*(th**(2*((j-i)//3)) if (j-i)%3==0 else 0) for i in range(N) for j in range(i+1,N))
   assert abs(mass-1)<1e-12 and abs(ey-exact)<1e-12;checks+=2
   eps=sum(v for (y,t),v in law.items() if y!=0)
   ref={(0,t):.25 for t in itertools.product((-1,1),repeat=2)}
   tv=.5*sum(abs(law.get(k,0)-ref.get(k,0)) for k in set(law)|set(ref))
   assert tv<=eps+1e-12;assert eps<=4*ey/Delta**2+1e-12;checks+=2
   marginal={}
   for (y,t),v in law.items():marginal[y]=marginal.get(y,0)+v
   ent.append(-sum(v*math.log2(v) for v in marginal.values()));laws.append(law);epss.append(eps)
  tv=.5*sum(abs(laws[0].get(k,0)-laws[1].get(k,0)) for k in set(laws[0])|set(laws[1]))
  assert tv<=sum(epss)+1e-12;checks+=1
  rows.append({'N':N,'Delta':Delta,'TV_plus_minus':tv,'tail_probabilities':epss,'H_Y_bits':ent,'Bayes_absolute_risk':.25*(1-tv)})
print(json.dumps({'seed':None,'method':'exhaustive binary64 enumeration','assertions':checks,'rows':rows},indent=2))
