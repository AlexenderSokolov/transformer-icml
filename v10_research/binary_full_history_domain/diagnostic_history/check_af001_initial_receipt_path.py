#!/usr/bin/env python3
"""Author finite algebra/interface checks. CB005 remains conditional until receipt."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import isqrt
import hashlib,json,datetime
D=Path(__file__).resolve().parent;R=D.parent;counts=Counter()
proof=D/'AF001_full_history_domain_classification.md';ph='597d6f1473298fdbb6013b09134c2caff67aaf3dd9537180d577262e7e014072'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(v,k):
 assert v,k
 counts[k]+=1
def G(M,b):
 return F(0) if b==0 else min(M*M*b,1/(M*b))
ck(h(proof)==ph,'candidate_hash');ck(h(D/'AF001_initial_candidate.md')==ph,'initial_snapshot')
accepted=[]
for u in ['KA001','CB004','BK002','AB001','SC003','BT002','KH002']:
 p=R/f'intake/{u}_acceptance.json';q=json.loads(p.read_text())
 ck(h(R/q['proof'])==q['sha256'],'accepted_source_hash')
 if 'review_sha256' in q:ck(h(R/q['review'])==q['review_sha256'],'accepted_review_hash')
 accepted.append({'unit':u,'receipt':str(p.relative_to(R)),'proof_sha256':q['sha256']})
for M in [64,65,100,4096,4097,65536,10**12]:
 betas=[F(0),F(1,M**3),F(1,M*M),F(16,M*M),F(1,256*M),F(1,16*M),F(1,M),F(1,16),F(1)]
 for beta in betas:
  if beta>1:continue
  ck(G(M,beta)**2<=M,'finite_horizon_G_bound')
  for B in [F(1),F(2),F(7,2),F(16),F(256),F(10000)]:
   union=(M*M*beta<=B or beta>=1/(B*M))
   ck((G(M,beta)<=B)==union,'exact_union_equivalence')
   if G(M,beta)<=B:
    weak=M*M*beta<=B
    if beta==0:ck(weak,'zero_beta_weak_branch')
    if not weak:
     ck(beta>0 and beta>=1/(B*M),'public_selector_strong_branch')
     ck(1/(M*M*beta)<=B/M,'strong_statistical_absorption_squared')
 # The clean-beta0/attacked-beta1/M example admits supplied-beta selection only.
 ck(G(M,F(0))==0 and G(M,F(1,M))==1,'two_label_joint_blindness_domain')
 ck(M*M*F(0)<=1 and M*M*F(1,M)>1,'same_public_selector_different_beta_branches')
finite=[]
for M in [4096,4097,8192,12345,65536,10**8,10**16]:
 lo=F(256,M*M);hi=F(1,16*M)
 for f in [F(0),F(1,7),F(1,2),F(6,7),F(1)]:
  beta=lo+(hi-lo)*f;k=isqrt(beta.denominator//beta.numerator);T=M//8
  ck(k*k*beta<=1<(k+1)**2*beta,'exact_inverse_sqrt_floor')
  ck(F(256,M*M)<=beta<=F(1,16*M) and M>=4096,'KA001_finite_domain')
  ck(k*k>=4*M and k<=M//16 and k<=T,'legal_attack_integer_budget')
  ck(k*k*beta>=F(9,16),'rounded_actual_beta_scale')
  ck(F(k*k,M)>=F(9,16)/(M*beta),'clean_penalty_ratio_scale_squared')
  ck(F(M*M,k*k)>=M*M*beta,'harmonic_range_scale_squared')
  ck(T+1>k and 2*T>=T+1,'positive_logarithm_domain')
  ck(beta>=F(1,M*M),'actual_cutoff_is_sqrt_beta_squared')
  finite.append({'M':str(M),'beta':str(beta),'k':str(k),'G_full':str(G(M,beta))})
# Explicit sparse/unbounded selection examples: beta=M^-3/2, M=n^4.
for n in [16,32,128,1024]:
 M=n**4;beta=F(1,n**6);N=n*n
 ck(G(M,beta)==N,'unbounded_sparse_selection')
 ck(M*M*beta>=N and M*beta<=F(1,N) and M>=N*N,'selected_sequence_exact_implications')
# Fixed public band union remains bounded on deliberately alternating cases.
for j in range(1,20):
 M=64+j**4;beta=F(2,M*M) if j%2 else F(1,2*M)
 ck(G(M,beta)<=2,'oscillating_fixed_union')
# The upper is an inherited conditional interface, not an accepted source claim.
cb5=R/'critical_beta_adaptation/CB005_all_start_critical_adaptation.md'
cb5hash=h(cb5)
ck(cb5hash=='5e514451e88672533b5a376e43265b8a382ac0b59e816e3ef06212ea5be6db52','conditional_CB005_snapshot')
ck(h(proof)==ph,'unchanged_candidate')
out={'unit':'AF001','status':'PASS_FINITE_CHECKS_ALL_START_REMAINS_CONDITIONAL','proof_sha256':ph,'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'arithmetic':'Exact integers/Fractions and certified integer square-root floors; no approximate pass/fail tests.','counts':dict(counts),'accepted_sources':accepted,'conditional_dependency':{'path':str(cb5.relative_to(R)),'sha256':cb5hash,'status':'CANDIDATE_INTERFACE_NOT_YET_ACCEPTANCE_AUTHORITY'},'finite_lower_records':finite,'limitations':'Checks do not accept CB005, prove its generic occupation bound, certify universal-map/domain quantifiers or establish logarithmic/asymptotic limits. Fresh full review and CB005 root receipt are required.'}
(D/'AF001_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'counts':dict(counts),'conditional_CB005_sha256':cb5hash}))
