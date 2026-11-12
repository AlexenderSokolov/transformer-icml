import math,itertools,json
if not __debug__:raise RuntimeError('assertions required')
rows=[];checks=0
for N in [8,12,16]:
 for eps in [1/64,1/128]:
  rho=.5+eps;delta=rho**N;m=math.floor(math.log2(1/(16*eps)))
  weights=[math.expm1(delta*rho**k) for k in range(1,N)]
  # Normalize solely for stable finite diagnostics, not a free network operation.
  weights=[w/weights[0] for w in weights]
  failmass={th:0. for th in [-.5,0.,.5]};bad=0
  for xs in itertools.product([-1,1],repeat=N-1):
   dot=sum(w*x for w,x in zip(weights,reversed(xs)))
   pred=1 if dot>=0 else -1;target=xs[-1]
   if pred!=target:
    bad+=1
    assert len(xs)-1>=m and all(x==-target for x in xs[-1-m:-1])
    for th in failmass:
     p=.25
     for j in range(len(xs)-2):p*=(1+th*xs[j]*xs[j+1]*xs[j+2])/2
     failmass[th]+=p
   checks+=1
  assert max(failmass.values())<=(.75)**(m-1)+1e-12
  rows.append(dict(N=N,epsilon=eps,m=m,bad_words=bad,failure_probability=failmass))
# Asymptotic-parameter examples: actual misdecoding despite epsilon_N shrinking.
worst=[]
for N in [32,64,128,256]:
 eps=N**-2/16;rho=.5+eps;delta=rho**N
 ratio=sum(math.expm1(delta*rho**j)/math.expm1(delta*rho) for j in range(2,N))
 assert ratio>1
 worst.append(dict(N=N,epsilon=eps,tail_to_first_ratio=ratio))
print(json.dumps(dict(status='pass',word_checks=checks,finite_failure_rows=rows,shrinking_epsilon_worst_words=worst,scope='float64 normalized-coefficient scalar interface; not a compiled network or precision certificate'),indent=2))
