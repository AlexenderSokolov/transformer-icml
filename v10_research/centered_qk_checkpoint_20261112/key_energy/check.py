import math,itertools,json
if not __debug__:raise RuntimeError('assertions required')
def ln(h):
 mu=sum(h)/6;s=math.sqrt(1+sum((v-mu)**2 for v in h)/6)
 return [(v-mu)/s for v in h]
def sigmoid(x):return 1/(1+math.exp(-x))
def Phi(x):return sigmoid(math.sqrt(3)*x/math.sqrt(4+x*x))
checks=0;err=0.;physicalmax=0
for N in [2,3,4,6,8]:
 for xs in itertools.product([-1,1],repeat=N):
  hs=[[x,-x,1,-1,0,0] for x in xs]+[[0,0,1,-1,0,0]]
  zz=list(map(ln,hs));qs=[math.sqrt(4/3)*z[2] for z in zz];ks=[math.sqrt(5/3)*z[0] for z in zz]
  out=[]
  for i,h in enumerate(hs):
   ew=[math.exp(qs[i]*ks[j]) for j in range(i+1)];A=sum(w*k for w,k in zip(ew,ks))/sum(ew)
   hh=h[:];hh[4]+=A;hh[5]-=A;out.append(hh)
   physicalmax=max(physicalmax,math.sqrt(sum(v*v for v in hh)))
  pred=sigmoid(ln(out[-1])[4]);H=sum(math.exp(x)*x for x in xs)/(sum(math.exp(x) for x in xs)+1)
  err=max(err,abs(pred-Phi(H)));assert abs(pred-Phi(H))<1e-14
  centered=sum((k-sum(ks)/(N+1))**2 for k in ks)
  assert abs(centered-(N-sum(xs)**2/(N+1)))<1e-12
  checks+=1
risks=[]
for N in [8,16,32,64,128,256,512]:
 actual=ref=diff=0.
 for k in range(N+1):
  p=math.comb(N,k)/2**N;m=(2*k-N)/N
  H=(m+math.tanh(1))/(1+m*math.tanh(1)+1/(N*math.cosh(1)))
  a=Phi(H);u=Phi(m*N/(N+1))
  actual+=p*abs(a-.5);ref+=p*abs(u-.5);diff+=p*abs(a-u)
 risks.append(dict(N=N,actual_theta0_risk=actual,uniform_reference_risk=ref,expected_prediction_difference=diff))
for N in [4,8,32,128]:
 p=[(-1)**i for i in range(1,N+1)];e=[math.exp(x) for x in p];w=[v/sum(e) for v in e]
 assert abs(sum(abs(v-1/N) for v in w)-math.tanh(1))<1e-13
 assert abs(sum(v*x for v,x in zip(w,p))-math.tanh(1))<1e-13
print(json.dumps(dict(status='pass',all_row_network_words=checks,max_formula_error=err,max_physical_norm=physicalmax,risk_limit=Phi(math.tanh(1))-.5,finite_binomial_risks=risks,scope='float64 actual all-row full-PreLN and exact-binomial weighted theta0 diagnostic; no noise certificate'),indent=2))
