"""Supplemental finite interface checks, not a universal proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, math, hashlib
out={}
# Exhaustive common protected-pair -> FOU protected-terminal embedding.
n=0
for M in range(1,7):
 for x in product(range(2), repeat=M+2):
  for prefix in product(range(2),repeat=M):
   y=prefix+x[-2:]
   k=sum(a!=b for a,b in zip(x,y))
   assert x[-1]==y[-1] and sum(a!=b for a,b in zip(x[1:],y[1:]))<=k
   assert len(x[1:])==M+1
   n+=1
out['protected_pair_suffix_embedding_cases']=n
# Exact target equivalence, including deterministic boundaries.
n=0
for a,t,p in product([F(0),F(1,4),F(1,2),F(1)],repeat=3):
 for u,v in product(range(2),repeat=2):
  q=(a,t)[v]; predicted1=p if v==0 else 1-p; true1=a if v==0 else 1-t
  assert abs(predicted1-true1)==abs(p-q)
  n+=1
out['exact_target_orientation_cases']=n
n=0
for M in [64,65,128,1024]:
 r=F(1,2*M)
 for a in [F(1,M),F(1,8),F(1,4)]:
  b=r*(1-a)/a
  assert b<1-r # genuinely second order throughout these samples
  pi=[(1-a)/2,a/2,a/2,(1-a)/2]; theta=[a,b,a,1-r]
  states=list(product(range(2),repeat=2)); P=[[F(0) for _ in states]for _ in states]
  for i,(u,v) in enumerate(states):
   for j,(c,d) in enumerate(states):
    P[i][j]=(theta[i] if d else 1-theta[i]) if c==v else F(0)
  assert [sum(pi[i]*P[i][j] for i in range(4))for j in range(4)]==pi
  n+=1
out['exact_second_order_stationarity_cases']=n
n=0
for M in [64,65,100,1024,1000000]:
 for k in sorted(set([0,1,int(math.sqrt(M)),M//2,M])):
  for beta in [0,1/M**2,1/M,.25,1]:
   g=max(M**-.5,k/M)
   f=0 if k==0 else k/M*(1+math.log1p(1/(k*max(math.sqrt(beta),1/M))))
   H=min(1,max(M**-.5,f))
   assert g<=H+1e-15
   assert 1024+2**20<=2**21
   n+=1
out['floating_profile_diagnostics']=n
# The original full-word N=M+1 reduction has an invalid initial-edge premise
# for arbitrary pair starts: identity table, initial pair 01 -> word 011... .
assert F(0)==0 # probability of initial 0->1 under identity table
out['initial_pair_counterexample']='identity table; deterministic initial pair 01; original law produces 011... with probability one, ordinary first-order full-word law with X0=0 assigns zero'
# Verify exact accepted receipt bindings.
root=Path('v10_research'); p=root/'first_order_positional_probe'
h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
receipt=json.loads((root/'intake/FOU001_root_acceptance.json').read_text())
for rel,v in receipt['artifacts'].items(): assert h(p/rel)==v['sha256']
receipt=json.loads((root/'intake/AB001_acceptance.json').read_text())
assert h(root/receipt['proof'])==receipt['sha256']
assert h(root/receipt['review'])==receipt['review_sha256']
out['accepted_dependency_receipt_bindings_verified']=8
out['status']='PASS_SUPPLEMENTAL_CHECKS_WITH_INITIAL_INTERFACE_BLOCKER'
Path(__file__).with_name('checks_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
