"""Exact finite diagnostics, not statistical proof or original emitter execution."""
from fractions import Fraction as F
from itertools import product
import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent

def tv(a,b):return sum(abs(x-y) for x,y in zip(a,b))/2
checks=0; nonempty=empty=0; max_ratio=F(0)
for K,maxM in [(2,6),(3,4)]:
 for M in range(1,maxM+1):
  N=M+2;n=N+1
  for x in product(range(K),repeat=N):
   e=lambda c:[int(j==c) for j in range(K)]
   inp=[e(c) for c in x]+[[0]*K]
   lag1=[inp[t-1] if t>=1 else inp[t] for t in range(n)]
   lag2=[inp[t-2] if t>=2 else inp[t] for t in range(n)]
   for Q in [16,32]:
    for W in [M,M*Q]:
     for t in range(n):
      keys=list(range(2,min(t,N-1)+1)) if t>=2 else [t]
      den=0;nums=[0]*K
      for i in keys:
       m=sum(a*b for a,b in zip(lag2[t],lag2[i]))+sum(a*b for a,b in zip(lag1[t],lag1[i]))
       assert m in (0,1,2)
       w=(1,W,W*W)[m]; den+=w
       for c in range(K):nums[c]+=w*inp[i][c]
      assert sum(nums)==den>0
      assert den<=M*W*W
      assert Q*max(nums)<=Q*M*W*W
      B=[F(a,den) for a in nums]
      z=[Q*a//den for a in nums]
      out=[F(a,Q) for a in z[:-1]]+[F(Q-sum(z[:-1]),Q)]
      assert sum(out)==1 and min(out)>=0
      assert tv(out,B)<=F(K-1,Q)
      checks+=1
      if t!=n-1:continue
      C=[sum(x[i-2:i]==x[-2:] and x[i]==c for i in range(2,N)) for c in range(K)]
      J=sum(C); q=[F(c+1,J+K) for c in C]
      if J:
       nonempty+=1
       emp=[F(c,J) for c in C]
       assert tv(B,emp)<=F(M,W*J)
      else:empty+=1
      if W==M:
       assert tv(B,q)<=min(F(1),F(2*K+1,J+K))
       assert tv(out,q)<=min(F(1),F(2*K+1,J+K))+F(K-1,Q)
      else:
       assert tv(B,q)<=F(K,J+K)+F(1,Q)
       assert tv(out,q)<=F(K,J+K)+F(K,Q)
# Integer threshold check, including noninteger A/t-K boundaries.
thresh=0
for K in range(2,12):
 for A in [F(K),F(2*K+1),F(K)+F(K+1,16)]:
  for j in range(101):
   for t in [F(i,37) for i in range(1,37)]:
    u=A/t-K;w=-(-u.numerator//u.denominator)
    assert (min(F(1),A/(j+K))>t)==(j<w)
    if u>0:assert w<=A/t
    thresh+=1
report={'status':'PASS','full_row_rational_checks':checks,'terminal_nonempty_checks':nonempty,'terminal_empty_checks':empty,'UC_integer_threshold_checks':thresh,'scope':'Exhaustive finite word tests for K=2,M<=6 and K=3,M<=4,Q=16,32, both W=M and W=MQ. Exact Fraction arithmetic. Not statistical risk simulation, original emitter execution, formal verification or independent review.'}
(OUT/'GW001_diagnostics_v1.json').write_text(json.dumps(report,indent=2)+'\n')
paths=[
'cloud_work/conditions-20261028/research/resume_20261030/R011_global_rates_and_constant_adaptation_v1.md',
'cloud_work/conditions-20261028/research/resume_20261030/R011_root_acceptance.json',
'cloud_work/conditions-20261028/handoff/DOT_CONDITIONS_20261028/sources/euler/SRC-proof.md',
'cloud_work/conditions-20261028/handoff/DOT_CONDITIONS_20261028/sources/euler/GU-proof.md',
'v10_research/bounded_attention/BA001_bounded_local_attention_lower_v1.md',
'v10_research/bounded_attention/BF001_encoder_family_frontier_v2.md',
'v10_research/growing_weight/GW001_growing_integer_weight_escape_v1.md']
manifest={'note':'BF001 v2 contextual only, not theorem dependency. R011 acceptance binds cited original-risk upper. New GW001 candidate pending independent review.','bindings':[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in paths]}
(OUT/'GW001_source_bindings_v1.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(report,indent=2))
