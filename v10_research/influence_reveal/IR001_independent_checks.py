"""Independent reviewer finite checks; not formal proof or author diagnostics."""
from fractions import Fraction as F
import math, random, json, hashlib
from pathlib import Path
rng=random.Random(281107)
checks={}
# Arbitrary nonlinear hypercube tables; exact conditional moments and product derivative.
cases=0
for trial in range(12):
    N=7
    vals=[F(rng.randrange(-30,31),10) for _ in range(1<<N)]
    c=[max(abs(vals[x]-vals[x^(1<<i)]) for x in range(1<<N)) for i in range(N)]
    B=sum(c)
    top=sorted(range(N),key=lambda i:(-c[i],i))[:3]
    # union adds boundary bit; sometimes duplicates selected influences.
    U=sorted(set(top+[trial%N])); free=[i for i in range(N) if i not in U]
    assert all(c[i]<=B/3 for i in free)
    for yy in range(1<<len(U)):
      fixed=sum(((yy>>j)&1)<<i for j,i in enumerate(U))
      for p in [F(1,4),F(2,5),F(1,2),F(3,4)]:
        mean=F(0); second=F(0); deriv_score=F(0)
        for xx in range(1<<len(free)):
          x=fixed+sum(((xx>>j)&1)<<i for j,i in enumerate(free))
          k=xx.bit_count(); w=p**k*(1-p)**(len(free)-k)
          mean+=w*vals[x]; second+=w*vals[x]**2
          deriv_score+=w*vals[x]*(F(k)/p-F(len(free)-k)/(1-p))
        deriv_flip=F(0)
        for i in free:
          other=[j for j in free if j!=i]
          for xx in range(1<<len(other)):
            x=fixed+sum(((xx>>j)&1)<<k for j,k in enumerate(other))
            k=xx.bit_count(); w=p**k*(1-p)**(len(other)-k)
            deriv_flip+=w*(vals[x|(1<<i)]-vals[x])
        assert deriv_flip==deriv_score
        assert abs(deriv_flip)<=sum(c[i] for i in free)<=B
        var=second-mean**2
        assert var<=sum(c[i]**2 for i in free)/2<=B**2/6
        cases+=1
checks['exact_nonlinear_conditional_cases']=cases
# Test the analytic mode-segment lower normalizer, including boundary modes.
posterior_cases=0; max_drop=0
for n in list(range(1,257))+[500,1000,10000,1000000]:
  ts=range(n+1) if n<=256 else sorted(set([0,n,n//2,n//4,3*n//4]+[min(n,max(0,int(n*z+a*math.sqrt(n)))) for z in [.25,.75] for a in [-3,-1,0,1,3]]))
  for t in ts:
    z=t/n; p0=min(.75,max(.25,z))
    if abs(z-p0)>3/math.sqrt(n)+1e-14: continue
    slope=abs(n*(z-p0)/(p0*(1-p0)))
    assert slope<=16*math.sqrt(n)+1e-8
    direction=1 if p0<=.5 else -1
    delta=1/(64*math.sqrt(n)); p1=p0+direction*delta
    # Stable log likelihood difference.
    drop=-(t*math.log(p1/p0)+(n-t)*math.log((1-p1)/(1-p0)))
    assert drop<=.25+1/512+1e-8
    assert drop<math.log(2)
    max_drop=max(drop,max_drop); posterior_cases+=1
checks['posterior_mode_segment_cases']=posterior_cases
checks['max_loglikelihood_drop']=max_drop
# Nonnegative causal row-stochastic matrix majorant, exact rational powers/local windows.
def matmul(X,Y):
 return [[sum((X[i][k]*Y[k][j] for k in range(len(X))),F(0)) for j in range(len(X))] for i in range(len(X))]
matrix_cases=0
for N in range(2,10):
 T=N+1
 for a,bb in [(F(0),F(1)),(F(1,3),F(2,5)),(F(2),F(3))]:
  H=[[a*(i==j)+(bb/F(i+1) if j<=i else 0) for j in range(T)] for i in range(T)]
  P=[[F(i==j) for j in range(T)] for i in range(T)]
  for depth in range(1,7):
    P=matmul(P,H)
    assert all(sum(row)==(a+bb)**depth for row in P)
    for r in range(1,N+2):
      ci=[sum(P[-1][u] for u in range(i,min(N,i+r))) for i in range(N)]
      assert sum(ci)<=r*sum(P[-1][:-1])<=r*(a+bb)**depth
      matrix_cases+=1
checks['exact_matrix_locality_cases']=matrix_cases
# Quantized tube bound for negative translated coordinates, real Q and noninteger E.
for _ in range(10000):
 q=rng.uniform(1,100); E=rng.uniform(0,7); center=rng.uniform(-100,100)
 aa=center+rng.uniform(-(E+2)/q,(E+2)/q)
 k=math.floor(q*aa)
 assert abs(k-q*center)<=E+3+1e-10
 left=q*center-E-3; right=q*center+E+3
 count=max(0,math.floor(right)-math.ceil(left)+1)
 assert count<=math.ceil(2*E+6)+1
checks['real_grid_negative_tube_cases']=10000
# All constant inequalities used in final reduction.
assert math.exp(1/12)-1<=1/11
assert 1/(2*math.sqrt(11))<1/4
assert 1-200*math.exp(-18)>.99
assert .98-.25>=.5
assert .99/16>=1/32
checks['constant_checks']='PASS'
checks['status']='PASS'
root=Path(__file__).parent
checks['reviewed_theorem_sha256']=hashlib.sha256((root/'IR001_theorem.md').read_bytes()).hexdigest()
(root/'IR001_independent_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
