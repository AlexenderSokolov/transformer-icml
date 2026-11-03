#!/usr/bin/env python3
"""Independent finite rational corroboration of AF001, not formal verification."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import hashlib,json
R=Path(__file__).resolve().parents[1]
checks=0
counts={}
def ck(x,tag):
 global checks
 assert x,tag
 checks+=1;counts[tag]=counts.get(tag,0)+1
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
expected='17860bb034c34c388d12ccb83b942dc88fb4bf88ee15c2d7d63df099a230ebd4'
proof=R/'binary_full_history_domain/AF001_full_history_domain_classification.md'
ck(sha(proof)==expected,'frozen_proof')
ck(proof.read_bytes()==(R/'reviews/AF001_audit_snapshots/AF001_received.md').read_bytes(),'snapshot')
receipts={}
for name in ['KA001_acceptance','BK002_acceptance','CB004_root_acceptance','CB005_root_acceptance','AB001_acceptance','KH002_acceptance','SC003_acceptance','BT002_acceptance']:
 p=R/'intake'/f'{name}.json';r=json.loads(p.read_text());receipts[str(p.relative_to(R))]=sha(p)
 ck(r['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW','receipt_status')
 ck(sha(R/r['proof'])==r['sha256'],'receipt_proof_hash')
 if 'review_sha256' in r:ck(sha(R/r['review'])==r['review_sha256'],'receipt_review_hash')
 for q,h in r.get('component_proofs',{}).items():ck(sha(R/q)==h,'receipt_component_hash')
# Domain equivalence, zero conventions, boundaries and weak-first overlap.
for M in list(range(64,193))+[255,256,4095,4096,4097,65536,10**12]:
 bs={F(0),F(1),F(1,M),F(1,M*M)}
 for B in [F(1),F(3,2),F(2),F(16),F(M),F(M*M)]:
  bs.update(b for b in [B/(M*M),1/(B*M),B/(2*M*M),2/(B*M)] if b<=1)
 for b in bs:
  G=0 if not b else min(M*M*b,1/(M*b))
  ck(G*G<=M,'bounded_horizon')
  for B in [F(1),F(3,2),F(2),F(16),F(M),F(M*M)]:
   weak=M*M*b<=B
   ck((G<=B)==(weak or b>=1/(B*M)),'union_equivalence')
   if G<=B and not weak:
    ck(b>0 and 1/(M*M*b)<=B/M,'strong_absorption_squared')
# Exact non-square actual certificates and every relevant rounding inequality.
witness_cases=0;non_square=0
for M in list(range(4096,4609))+[8191,8192,8193,65535,65536,65537,10**12]:
 lo=F(256,M*M);hi=F(1,16*M)
 for t in range(9):
  b=((8-t)*lo+t*hi)/8;k=isqrt(b.denominator//b.numerator);T=M//8
  ck(k*k*b<=1 and (k+1)**2*b>1,'exact_floor')
  ck(k*k*b>=F(9,16),'rounding_lower_squared')
  ck(k*k>=4*M and 16*k<=M and k<=T,'finite_BK_domain')
  ck(b<=F(1,k*k) and b<=F(1,M),'actual_class_nesting')
  ck(b>=F(1,M*M),'cutoff')
  ck(T+1>k and 2*T>k,'positive_logs')
  # 1+1/(k sqrt(b)) <=7/3 and exp(1)>1+1+1/2>7/3.
  ck(k*k*b>=F(9,16) and F(5,2)>F(7,3),'benchmark_log_bound')
  if M in [4096,4097,8191,65537,10**12]:
   d=F(1,k);tau=F(1,4*M)
   for a in [F(k,32*T),F(1,16),(F(k,32*T)+F(1,16))/2]:
    e=1-d;x=1/(e/a+2+d/tau);pi=[x*e/a,x,x,x*d/tau]
    theta=[a,d,d,1-tau];P=[[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):P[i][2*(i%2)]=1-theta[i];P[i][2*(i%2)+1]=theta[i]
    for j in range(4):ck(sum(pi[i]*P[i][j] for i in range(4))==pi[j],'witness_stationarity')
    for i in range(4):
     for j in range(4):
      p2=sum(P[i][l]*P[l][j] for l in range(4))
      ck(p2>=d*d*pi[j] and p2>=b*pi[j],'allstate_both_certificates')
    witness_cases+=1;non_square+=b!=d*d
# Exact asymptotic sequence samples, sparse horizons, and beta-blind counterexample domain.
for j in [4,5,8,16,32,64,128,1024,4096]:
 M=2**(4*j);b=F(1,2**(6*j));k=2**(3*j)
 ck(min(M*M*b,1/(M*b))==2**(2*j),'intermediate_sequence')
 ck(k*k==1/b and k*k>=4*M and k<=M//16,'sequence_budget')
 ck(F(isqrt(M),k)==F(1,2**j),'penalty_prefactor')
 ck(F(M//8+1,k)>2**(j-3),'diverging_log_argument')
 ck(min(F(M),1)==1,'beta_blind_union_G')
ck(F(32)*2048/3==F(65536,3),'penalty_constant')
ck(F(3,2048)/2/2==F(3,8192),'final_ratio_constant')
ck(2**16>4096 and 2**23>6433056,'upper_constants')
ck(sha(proof)==expected,'frozen_proof_end')
out={'status':'PASS','checks':checks,'counts':counts,'witness_cases':witness_cases,'non_square_actual_beta_witness_cases':non_square,'candidate_sha256':expected,'receipts':receipts,'scope':'Finite exact rational/integer corroboration only; limits and universal quantifiers reviewed analytically.'}
(R/'reviews/AF001_independent_exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
