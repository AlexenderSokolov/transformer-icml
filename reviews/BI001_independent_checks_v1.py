#!/usr/bin/env python3
"""Independent exact finite diagnostics; not a proof or author-script reuse."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,itertools,random
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
a,e,p=s.symbols('a e p',positive=True)
P=s.Matrix([[1-a,a,0,0],[0,0,1-p,p],[e,1-e,0,0],[0,0,s.Rational(1,2),s.Rational(1,2)]])
x=1/(e/a+2+2*p); pi=s.Matrix([[x*e/a,x,x,2*p*x]])
assert all(s.simplify(v)==0 for v in pi*P-pi)
assert s.simplify(sum(pi)-1)==0
expected=s.Matrix([[(1-a)**2,(1-a)*a,a*(1-p),a*p],[(1-p)*e,(1-p)*(1-e),p/2,p/2],[e*(1-a),e*a,(1-e)*(1-p),(1-e)*p],[e/2,(1-e)/2,s.Rational(1,4),s.Rational(1,4)]])
assert all(s.simplify(v)==0 for v in P**2-expected)
R=s.Matrix([[0,1-p,p],[1,0,0],[0,s.Rational(1,2),s.Rational(1,2)]])
assert list((R**2)[:,1])==[p/2,1-p,s.Rational(1,4)]
assert list((R**3)[:,0])==[p/2,1-p,s.Rational(1,4)]
assert s.simplify(e*a/x-(e*e+e*a*(2+2*p)))==0
cert_cases=0; minimum_slack=None
for M in [64,65,128,1024,1000000]:
 for ee in sorted(set([s.Rational(1,M),s.Rational(1,32),s.Rational(1,16)])):
  if ee<s.Rational(1,M): continue
  beta=min(ee**2,s.Rational(1,256))
  for pp in [s.Rational(1,4),s.Rational(3,8),s.Rational(1,2),s.Rational(5,8),s.Rational(3,4)]:
   subs={a:s.Rational(1,2*M),e:ee,p:pp}
   pv=pi.subs(subs); mat=(P**2).subs(subs)
   assert pv[0]>=s.Rational(4,11)
   slacks=[mat[i,k]-beta*pv[k] for i in range(4) for k in range(4)]
   assert min(slacks)>=0
   minimum_slack=min(slacks) if minimum_slack is None else min(minimum_slack,min(slacks))
   cert_cases+=1

def paths(j,pp):
 rows={0:[(1,1-pp),(2,pp)],1:[(0,F(1))],2:[(1,F(1,2)),(2,F(1,2))]}
 out=[((0,),F(1),F(0))]
 for _ in range(j-1):
  new=[]
  for states,prob,dp in out:
   for nxt,w in rows[states[-1]]:
    dw=F(0) if states[-1]!=0 else F(-1 if nxt==1 else 1)
    new.append((states+(nxt,),prob*w,dp*w+prob*dw))
  out=new
 return out

def local_table(i,window,branch,kind,kappa):
 # Deterministic positional/query-dependent tables, no parameter dependence.
 seed=17*i+31*branch+sum((v+1)*(3**k) for k,v in enumerate(window))
 w=F(1+(seed%int(kappa)))
 v=F((seed*23)%13-6,6)
 return w if kind=='denominator' else w*v
local_cases=0; event_paths=0; max_var_ratio=F(0); max_derivative_ratio=F(0); max_martingale_ratio=F(0)
for j in range(4,11):
 for pp in [F(1,4),F(1,2),F(3,4)]:
  paths_j=paths(j,pp); assert sum(prob for _,prob,_ in paths_j)==1
  assert sum(prob for states,prob,_ in paths_j if states[-1]==0)>=F(1,8)
  M=64; aa=F(1,2*M); ee=F(1,M); xx=1/(ee/aa+2+2*pp); piw=xx*ee/aa
  for states,prob,dp in paths_j:
   bits=[0]*(M+2-j)+[1]+[1 if st in (0,2) else 0 for st in states[1:]]
   assert len(bits)==M+2
   nb=sum(st==1 for st in states[:-1])
   density=piw*(1-aa)**(M-j)*aa*(1-ee)**nb
   actual=piw
   for i in range(2,len(bits)):
    pair=tuple(bits[i-2:i]); one={(0,0):aa,(0,1):pp,(1,0):1-ee,(1,1):F(1,2)}[pair]
    actual*=one if bits[i] else 1-one
   assert actual==density*prob
   assert density>=F(1,32*M)
   event_paths+=1
  for r,branch,kind in itertools.product([1,2,3,5],[0,7],['numerator','denominator']):
   kappa=7; records=[]
   for states,prob,dp in paths_j:
    bits=[0]*(M+2-j)+[1]+[1 if st in (0,2) else 0 for st in states[1:]]
    val=sum(local_table(i,tuple(([2]*r+bits[:i+1])[-r:]),branch,kind,kappa) for i in range(2,len(bits)))
    records.append((states,prob,dp,val))
   mean=sum(prob*val for _,prob,_,val in records)
   var=sum(prob*(val-mean)**2 for _,prob,_,val in records)
   derivative=sum(dp*val for _,_,dp,val in records)
   bound=34*kappa*r
   assert var<=bound**2*j and abs(derivative)<=bound*j
   max_var_ratio=max(max_var_ratio,var/F(bound**2*j))
   max_derivative_ratio=max(max_derivative_ratio,abs(derivative)/F(bound*j))
   # Exhaustively evaluate every conditional Doob next-state range.
   for depth in range(1,j):
    children={}
    for states,prob,_,val in records:
     prefix=states[:depth]; child=states[depth]
     entry=children.setdefault(prefix,{}).setdefault(child,[F(0),F(0)])
     entry[0]+=prob; entry[1]+=prob*val
    for childmap in children.values():
     means=[num/den for den,num in childmap.values()]
     rg=max(means)-min(means)
     assert rg<=bound
     max_martingale_ratio=max(max_martingale_ratio,rg/F(bound))
   local_cases+=1
mp.mp.dps=80
harmonic_cases=0; min_harmonic_ratio=mp.inf
for M in [64,65,100,128,1024]:
 for ee in sorted(set([F(1,M),F(1,32),F(1,16)])):
  if ee<F(1,M): continue
  for z in [F(1),F(3,2),F(M,17),F(M,4)]:
   U=min(1/(4*ee),F(M*M)/(4*z*z)); J=U.numerator//U.denominator; u=z/M
   assert J>=4 and J<=F(M,4) and J>=U/2 and ee*J<=F(1,4) and z*z*J/F(M*M)<=F(1,4)
   assert u*J>=F(1,8)*min(z/(M*ee),M/z)
   # Rational sum exact; only logarithm comparison is high-precision numeric.
   sm=sum((1/(1+u*j) for j in range(4,J+1)),F(0))
   lhs=mp.mpf(sm.numerator)/sm.denominator
   uu=mp.mpf(u.numerator)/u.denominator
   rhs=mp.log1p(uu*J)/(8*uu)
   assert lhs>=rhs
   min_harmonic_ratio=min(min_harmonic_ratio,lhs/rhs); harmonic_cases+=1
files=['v10_research/binary_frontier/BI001_binary_rare_suffix_lower_v1.md','v10_research/bounded_attention/BA001_bounded_local_attention_lower_v1.md','v10_research/score_precision/SH001_sharp_weight_ratio_threshold_v1.md','v10_research/score_precision/SB001_loglog_effective_score_budget_v2.md','v10_research/range_uniform_iid/UI001_range_uniform_iid_floor_v1.md']
result={'status':'PASS_FINITE_DIAGNOSTICS_NOT_FORMAL_VERIFICATION','symbolic':['stationarity and normalization','full 4x4 P squared','R squared B column and R cubed A column','topology-specific beta obstruction identity'],'all_state_parameter_cases':cert_cases,'minimum_minorization_slack':str(minimum_slack),'enumerated_path_density_cases':event_paths,'positional_local_sum_cases':local_cases,'maximum_variance_bound_ratio':str(max_var_ratio),'maximum_derivative_bound_ratio':str(max_derivative_ratio),'maximum_Doob_range_bound_ratio':str(max_martingale_ratio),'cutoff_harmonic_cases':harmonic_cases,'minimum_harmonic_ratio_80digits':str(min_harmonic_ratio),'arithmetic':'SymPy symbolic + Fraction exact; harmonic logarithm only mpmath 80 digits','bindings':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files}}
out=ROOT/'reviews/BI001_independent_checks_v1.json';out.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps(result,indent=2))
