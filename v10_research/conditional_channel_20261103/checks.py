#!/usr/bin/env python3
"""Finite corroboration, not universal proof. Run from any working directory."""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import hashlib,json,math
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
# Source hashes are checked against actual explicit root receipts, not this script.
units=[('CMF001','channel_margin_frontier_20261103','CANDIDATE.md'),('CAF001','channel_accuracy_frontier_20261103','CANDIDATE.md'),('UMC001','channel_uncertainty_20261103','CANDIDATE.md'),('UWC001','unknown_channel_whole_code_20261103','CANDIDATE.md'),('O2T001','resumption_20261103/order_two_transfer','CANDIDATE.md'),('WMC001','resumption_20261103/whole_message_cost','CANDIDATE.md'),('BCC001','resumption_20261103/channel_classification','CANDIDATE.md'),('BSC001','resumption_20261103/bsc_sharp','CHANNEL_LIKELIHOOD_LOWER.md')]
bindings=[]
for name,folder,filename in units:
    p=ROOT/'v10_research'/folder/filename
    receipt=p.parent/'ROOT_ACCEPTANCE.json'; r=json.loads(receipt.read_text())
    expected=r.get('candidate_sha256',r.get('artifacts',{}).get(filename))
    assert digest(p)==expected,(name,'source mismatch')
    bindings.append(dict(unit=name,source=str(p.relative_to(ROOT)),sha256=digest(p),receipt=str(receipt.relative_to(ROOT)),receipt_sha256=digest(receipt),accepted_hash_verified=True))
# Enumerate all vertex policies of a two-slot adaptive membership tree.
pair_cases=0; asymmetric_examples=0
for p in [F(1,8),F(1,3),F(1,2),F(3,4),F(7,8)]:
 for a in [F(0),p/100,p/4,(p/24)**2]:
  for gate in [0,1]:
   bits=[gate,1-gate]  # semantic 0=(0,1), semantic 1=(1,0)
   ranges={0:[F(0),a],1:[p-a,F(1)]}
   for qfirst,qsecond0,qsecond1 in product(ranges[bits[0]],ranges[bits[1]],ranges[bits[1]]):
    c=w=F(0)
    for e0,e1 in product([0,1],repeat=2):
     qsecond=[qsecond0,qsecond1][e0]
     prob=(qfirst if e0 else 1-qfirst)*(qsecond if e1 else 1-qsecond)
     if e0+e1==1:
      decoded=0 if e1 else 1
      if decoded==gate:c+=prob
      else:w+=prob
    assert c>=p-2*a and w<=a and c+w>=p/2
    pair_cases+=1
# Dynamic programming finds exact max over all error policies q(history) in [0,a].
# Extremizers at endpoints suffice because expectation affine in each row.
from functools import lru_cache
subset_cases=tail_cases=0
for n in range(1,9):
 for a in [F(1,16),F(1,5),F(1,3)]:
  for r in range(1,n+1):
   @lru_cache(None)
   def worst(t,k):
    if t==n:return F(k>=r)
    return max((1-q)*worst(t+1,k)+q*worst(t+1,k+1) for q in [F(0),a])
   assert worst(0,0)<=math.comb(n,r)*a**r
   tail_cases+=1
  for mask in range(1<<n):
   selected={i for i in range(n) if mask>>i&1}
   @lru_cache(None)
   def subset(t,ok):
    if t==n:return F(ok)
    return max((1-q)*subset(t+1,ok and t not in selected)+q*subset(t+1,ok) for q in [F(0),a])
   assert subset(0,True)==a**len(selected)
   subset_cases+=1
# Identity replacement marginals, exact common mass, and optimal uniform-code Bayes error.
replacement_words=code_cases=0
for R in range(1,7):
 words=list(product([0,1],repeat=R)); size=len(words)
 for a in [F(0),F(1,20),F(1,4),F(1,2)]:
  laws={h:{v:2*a/F(size)+(1-2*a if v==h else 0) for v in words} for h in words}
  for h,row in laws.items():
   assert sum(row.values())==1
   for i in range(R):assert sum(prob for v,prob in row.items() if v[i]!=h[i])==a
   assert all(prob>=2*a/F(size) for prob in row.values())
   replacement_words+=1
  for N in range(2,min(size,8)+1):
   code=words[:N]
   success=sum(max(laws[h][v] for h in code) for v in words)/N
   assert 1-success==2*a*(1-F(1,N))
   code_cases+=1
# A contradiction to conditional row fidelity on a reachable mismatch history.
for a in [F(1,100),F(1,5),F(1,3)]:
 joint_mismatch=2*a/F(4)
 first_mismatch=a
 assert joint_mismatch/first_mismatch==F(1,2)>a
# Finite arithmetic ledger for nested code, no full algebraic code implementation.
for B in range(1,10001):
 kc=(8*B-1).bit_length(); K=(B+kc-1)//kc
 assert kc>=3 and kc<=4*B and 4*K<=2**kc
 assert 48*K*kc<=240*B
 assert 4*K-8*kc*(K+1)<=-6*B
# General nominal mixture exact TV check at rational rows.
general_cases=0
for P in [(F(1),F(0),F(0)),(F(1,2),F(1,3),F(1,6)),(F(1,3),)*3]:
 for eta in [F(1,100),F(1,3),F(1)]:
  nu=(F(1,3),)*3;Q=[(1-eta)*p+eta*v for p,v in zip(P,nu)]
  tv=sum(abs(q-p) for p,q in zip(P,Q))/2
  assert tv<=eta
  general_cases+=1
report=dict(status='PASS_FINITE_CORROBORATION_NOT_UNIVERSAL_PROOF',adaptive_pair_vertex_cases=pair_cases,adaptive_subset_dp_cases=subset_cases,adaptive_tail_dp_cases=tail_cases,replacement_input_words=replacement_words,replacement_optimal_code_cases=code_cases,concatenation_arithmetic_B_values=10000,general_nominal_mixture_cases=general_cases,accepted_source_hashes_verified=len(bindings))
(HERE/'CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
(HERE/'SOURCE_BINDINGS.json').write_text(json.dumps(dict(unit='CCH001',status='AUTHOR_SOURCE_BINDINGS_NOT_ACCEPTANCE',sources=bindings,limits='Direct interfaces and model sections read; imported statistical and algebraic proofs not independently rederived. Hash identity is not proof validation.'),indent=2)+'\n')
print(json.dumps(report,indent=2))
