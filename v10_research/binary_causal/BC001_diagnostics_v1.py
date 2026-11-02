"""Exact finite corroboration only; no universal proof claim."""
from fractions import Fraction as F
from itertools import product
import json, math, hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
checks={}; n=0
for M in [1,2,3,7,16,63,64,65,127,1000]:
 for h in [0,1,4,7,11]:
  P=4*(h+3)+1; d=1<<P; Q=1<<h
  a=1; J=8*(2*a)**2+2+P
  term=d; W=term
  for j in range(1,J+1):
   term=term*(d*a)//(j*d); W+=term
  assert W>0
  for c in range(M+1):
   O=(W*d*c)//(M*W)
   assert O//(d//Q)==Q*c//M
   if c==0: assert O==0
   if c==M: assert O==d
   n+=1
checks['exact_FA_equal_weight_nested_floors_cases']=n

def mm(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
for p in [F(i,64) for i in range(16,49)]:
 R=[[0,1-p,p],[1,0,0],[0,F(1,2),F(1,2)]]
 R2=mm(R,R);R3=mm(R2,R)
 assert all(row[1]>=F(1,8) for row in R2)
 assert all(row[0]>=F(1,8) for row in R3)
checks['exact_reference_minorization_parameter_cases']=33
# Enumerate arbitrary nonlinear functions on active paths, check finite-difference
# derivative and variance against L=34*Gamma bounds. f=sum bits squared / M²
# has per-symbol influence <=2*j/M² <= 2/M (Gamma=2).
cases=0
for j in range(4,11):
 for p in [F(1,4),F(1,2),F(3,4)]:
  R=[[0,1-p,p],[1,0,0],[0,F(1,2),F(1,2)]]
  paths=[(0,1,F(1),F(0))] # state, number of emitted ones incl first 1, weight, derivative
  for _ in range(j-1):
   out=[]
   for s,k,w,dw in paths:
    for t in range(3):
     v=R[s][t]
     dv=(-1 if t==1 else 1 if t==2 else 0) if s==0 else 0
     if v: out.append((t,k+(t!=1),w*v,dw*v+w*dv))
   paths=out
  M=64
  mean=sum(w*F(k*k,M*M) for s,k,w,dw in paths)
  var=sum(w*(F(k*k,M*M)-mean)**2 for s,k,w,dw in paths)
  deriv=sum(dw*F(k*k,M*M) for s,k,w,dw in paths)
  assert var<=F(68**2*j,M*M)
  assert abs(deriv)<=F(68*j,M)
  cases+=1
checks['nonlinear_reference_exact_moment_cases']=cases
cases=0
for M in [64,65,127,256,1024,10**6,10**12]:
 for beta in [0,1/M**2,1/M,1/256,1/255,1]:
  for h in range(4,65):
   Q=2**h;e=max(math.sqrt(beta),1/M);t=M*e;s=M**-.5
   W=(1+math.log1p(Q/t))/Q
   if beta>1/256: assert W<=1/Q+2*s+1e-12
   elif Q>M/4 or Q>M**.75: assert W<=5*s+1e-12
   else:
    L=math.log1p(min(Q/t,M/Q)/8)/Q
    assert W<=1/Q+24*L+1e-12
   cases+=1
checks['completion_float_cases']=cases
checks['status']='PASS; finite diagnostics only'
(HERE/'BC001_diagnostics_v1.json').write_text(json.dumps(checks,indent=2)+'\n')
# Direct immutable dependency bindings, including exact acceptance receipts.
root=HERE.parent
names=['causal_attention/CA001_causal_bounded_softmax_candidate_v3.md','causal_attention/FA001_finite_arithmetic_bridge_v3.md','causal_attention/CF001_finite_causal_risk_frontier_v1.md','causal_attention/CA001_boundary_branch_causality_scope_note_v1.md','binary_frontier/BI001_binary_rare_suffix_lower_v2.md','binary_upper/BU001_weighted_return_upper_v2.md','binary_stationary_frontier/BS001_binary_stationary_frontier_v1.md','score_precision/SB001_loglog_effective_score_budget_v2.md']
names += ['intake/'+name+'_acceptance.json' for name in ['CA001','FA001','CF001','BI001','BU001','BS001','SB001']]
names += ['binary_causal/BC001_binary_stationary_causal_frontier_v1.md','binary_causal/BC001_diagnostics_v1.py','binary_causal/BC001_diagnostics_v1.json','binary_causal/BC001_revision_note_v1.md']
bind={'unit':'BC001','status':'AUTHOR_CANDIDATE','files':[{'path':name,'sha256':hashlib.sha256((root/name).read_bytes()).hexdigest()} for name in names]}
(HERE/'BC001_source_bindings_v1.json').write_text(json.dumps(bind,indent=2)+'\n')
print(json.dumps(checks,indent=2))
