#!/usr/bin/env python3
"""Exact author finite-nesting and domain-algebra diagnostics; not formal proof."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib,json,datetime
D=Path(__file__).resolve().parent;R=D.parent;counts=Counter()
proof=D/'KH002_histogram_domain_classification.md'
ph='970bfefb6041cdb989148819eb526c789d86591992375b84b05de2dd72bf9702'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(b,label):
 assert b,label
 counts[label]+=1
ck(h(proof)==ph,'candidate_hash')
ck(h(D/'revisions/KH002_initial_candidate.md')==ph,'actual_initial_snapshot')
for u in ['KH001','KA001','SC003','BT002']:
 q=json.loads((R/f'intake/{u}_acceptance.json').read_text())
 ck(h(R/q['proof'])==q['sha256'],'accepted_source_hash')
 if 'review_sha256' in q:ck(h(R/q['review'])==q['review_sha256'],'accepted_review_hash')
def mul(A,B):return [[sum(A[i][z]*B[z][j] for z in range(4)) for j in range(4)] for i in range(4)]
c=F(1,4096);records=[]
for n in [128,129,256]:
 M=n**24
 cases=[(b,n**k) for b,k in [(18,16),(20,18),(22,20)]]
 cases +=[(b,n**23) for b in [24,25,30,36,40,44,45,46]]
 for bexp,k in cases:
  actual=F(1,n**bexp);bw=max(actual,F(1,M));dw=F(1,n**(min(bexp,24)//2));T=int(1/(8*bw))
  ck(dw**2==bw,'witness_delta')
  ck(32<=k<=T and k*k>=4*M and k*dw>=6/c and dw**5*k**3>=2**20 and dw**3*k*k>=2**21,'complete_KH001_domain')
  ck(bw>=actual and bw>=F(1,M) and bw<=F(1,16),'actual_class_nesting')
  ck(k*k*actual>=1 and M*M*actual>=1,'actual_benchmark_squared_conditions')
  ck(k<=M and 2*k<=M,'legal_budget_and_nontrivial_comparison')
  ck((actual<F(1,M))==(bw!=actual),'metadata_change_only_if_needed')
  for j in sorted(set([k,2*k,(T+k)//2,T])):
   x=c*k/M;y=F(j,M);w=1-y-2*x;e=1-dw;a=c*k*e/j;t=x*dw/w
   P=[[1-a,a,0,0],[0,0,1-dw,dw],[e,1-e,0,0],[0,0,t,1-t]];v=[y,x,x,w];P2=mul(P,P)
   for u,z in product(range(4),repeat=2):
    ck(P2[u][z]>=bw*v[z],'witness_certificate_entries')
    ck(P2[u][z]>=actual*v[z],'actual_certificate_entries')
   r=F(1,2*M);p1=bw/(bw+r);p0=1-p1;nv=[p0*(1-bw),p0*bw,p1*r,p1*(1-r)]
   N=[[1-bw,bw,0,0],[0,0,r,1-r],[1-bw,bw,0,0],[0,0,r,1-r]];N2=mul(N,N)
   for u,z in product(range(4),repeat=2):ck(N2[u][z]>=actual*nv[z],'actual_null_certificate_entries')
   ck(a>=2*bw and N[0][1]==bw,'true_null_target_is_witness_not_actual')
   counts['finite_clean_family_cases']+=1
  records.append({'n':n,'M':str(M),'actual_beta':str(actual),'witness_beta':str(bw),'k':str(k),'k_squared_actual_beta':str(k*k*actual)})
# Domain-union equivalence can be checked without square roots by squaring positive quantities.
for M in [64,65,128,129,4096,10000]:
 for beta in [F(0),F(1,M**3),F(1,M*M),F(10,M*M),F(1,M),F(1,10),F(1)]:
  if beta>1:continue
  for B in [F(1),F(2),F(5,2),F(16),F(100)]:
   weak=M*M*beta<=B
   strong=beta>0 and beta*beta*M*B*B>=1
   # min(A,D)<=B iff A<=B or D<=B, comparing D via positive squares.
   min_le_B=(M*M*beta<=B) or (beta>0 and F(1)<=beta*beta*M*B*B)
   ck(min_le_B==(weak or strong),'exact_union_membership')
# Identity beta_w/sqrt(beta)=max(sqrt(beta),1/(M sqrt(beta))) squared.
for rec in records:
 M=int(rec['M']);beta=F(rec['actual_beta']);bw=F(rec['witness_beta'])
 ck(bw*bw/beta==max(beta,F(1,M*M)/beta),'third_scale_identity_squared')
ck(h(proof)==ph,'unchanged_candidate')
out={'unit':'KH002','status':'PASS_TESTED_INSTANCES_ONLY','proof_sha256':ph,'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'arithmetic':'Exact integer/Fraction calculations, positive square-root comparisons squared; no approximate pass/fail tests.','counts':dict(counts),'finite_records':records,'limitations':'Finite nesting/source/metadata and scalar checks only. Common-map quantifiers, asymptotic selection and arbitrary public-domain necessity require fresh full independent mathematical review.'}
(D/'KH002_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'counts':dict(counts)}))
