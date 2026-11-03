#!/usr/bin/env python3
"""Author exact finite checks for the boundary-window extension; not formal proof."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from itertools import product
import hashlib,json,datetime
D=Path(__file__).resolve().parent;counts=Counter();c=F(1,4096)
proof=D/'KH003_boundary_window_obstruction.md';ph='09adb8433d97011dbe7772ed9b0f1f903ed245d73299db02d7d6bc477fc358a4'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(v,l):
 assert v,l
 counts[l]+=1
ck(h(proof)==ph,'candidate_hash')
def H(w):return Counter(w[i:i+3] for i in range(len(w)-2))
def J(w,s):return sum(w[i:i+2]==s for i in range(len(w)-2))
def can(w):
 d=H(w);z='11'+'1'*d['111']
 for i in range(len(w)-2):
  t=w[i:i+3]
  if t not in ('000','111'):
   ck(z[-2:]==t[:2],'canonical_skeleton_continuity');z+=t[-1]
 return z+'0'*d['000']
# All small genuine constant-window examples, plus explicit last-zero indices.
for N in range(4,17):
 for middle in product('01',repeat=N-4):
  w='11'+''.join(middle)+'00';z=can(w);rev=w[::-1]
  for r in range(2,min(7,N//2)+1):
   B=(w[:r]=='1'*r and w[-r:]=='0'*r)
   if B:
    ck(H(w)['111']>=r-2 and H(w)['000']>=r-2,'genuine_window_loop_lower_bounds')
    ck(z[:r]==w[:r] and z[-r:]==w[-r:],'constant_window_preservation')
    ck(H(z)==H(w),'augmented_statistic_histogram')
    ck(rev[:r]=='0'*r and rev[-r:]=='1'*r,'reversed_original_window_event')
   if rev[-r:]!='1'*r:
    # E is automatic; q below is zero-based, m=q is departure index.
    q=max(i for i in range(N-r,N-2) if rev[i]=='0')
    ck(rev[q:q+3]=='011' and N-r<=q<=N-3,'last_zero_011_witness')
    ck((N-3)-(N-r)+1==r-2,'exact_last_window_departure_count')
  counts['exhaustive_words']+=1
# Exact DP from00. These are structural low-horizon tests, not claimed huge-domain cases.
for a,delta,tau in [(F(1,16),F(1,8),F(1,64)),(F(1,64),F(1,16),F(1,8)),(F(1,8),F(1,32),F(1,128))]:
 q=[a,delta,delta,1-tau]
 for M in [4,5,8,12,16,20]:
  for r in range(2,min(8,(M+2)//2)+1):
   # state, first-window-zero flag, current final1-run length
   law={(0,True,0):F(1)}
   for m in range(M):
    nxt=defaultdict(F);pos=m+3
    for (s,first,run),mass in law.items():
     for bit,p in [(0,1-q[s]),(1,q[s])]:
      ns=((s&1)<<1)|bit;nf=first and not(pos<=r and bit);nr=min(r,run+1) if bit else 0
      nxt[ns,nf,nr]+=mass*p
    law=nxt
   E=sum(v for (s,f,z),v in law.items() if s==3)
   firstbad=sum(v for (s,f,z),v in law.items() if not f)
   latebadE=sum(v for (s,f,z),v in law.items() if s==3 and z<r)
   badB_E=sum(v for (s,f,z),v in law.items() if s==3 and (not f or z<r))
   ck(firstbad<=1-(1-a)**(r-2)<=(r-2)*a,'first_window_DP_bound')
   ck(latebadE<=(r-2)*delta,'last_window_DP_bound')
   ck(badB_E<=firstbad+latebadE<=(r-2)*(a+delta),'joint_boundary_union')
   ck(E>0 and badB_E/E<=(r-2)*(a+delta)/E,'conditional_boundary_bound')
   counts['structural_boundary_DP_cases']+=1
records=[]
for n in [128,129,256]:
 M=n**24
 for bexp,kexp,rexp in [(18,16,1),(20,18,1),(22,20,1),(24,21,2),(24,22,1)]:
  delta=F(1,n**(bexp//2));beta=delta**2;k=n**kexp;r=n**rexp;T=int(1/(8*beta));q=16*c*r*k;J0=max(k,(q.numerator+q.denominator-1)//q.denominator)
  ck(F(1,M)<=beta<=F(1,16) and 32<=k<=T and k*k>=4*M and k*delta>=6/c and delta**5*k**3>=2**20 and delta**3*k*k>=2**21,'full_KH001_domain')
  ck(r<=F(k,4) and r*delta<=F(1,16) and J0<=T,'additional_window_domain')
  for j in sorted(set([J0,(J0+T)//2,T])):
   a=c*k*(1-delta)/j
   ck(a<=F(1,16*r) and 2*r*(a+delta)<=F(1,4),'boundary_probability_constants')
   ck(F(145,256)-F(1,4)==F(81,256)>F(1,4),'good_boundary_intersection')
   ck(F(j,2*M)*F(3,4)==F(3*j,8*M),'true_original_event_probability')
   ck(F(8*M,3*j)<=F(4*M,j),'conditional_clean_error_constant')
   ck(F(j)-F(5*k,16)>=F(11*k,16)>=r-2,'canonical_zero_loop_bound')
   ck(F(M)-j-F(3*k,8)>=F(53*M,64)>=r-2,'canonical_one_loop_bound')
   ck(3*F(k,16)+F(k,4)==F(7*k,16)<k,'strict_distance')
   ck(j>=4*r and M+2-j>=r,'actual_input_windows_fit')
   ck(F(1,8)*F(1,8)*F(1,2)==F(1,128),'positive_coefficient')
   ck(F(1,2)*4==2,'penalty_coefficient')
   counts['complete_finite_family_cases']+=1
  records.append({'n':n,'M':str(M),'beta':str(beta),'k':str(k),'r':str(r),'J0':str(J0),'T':str(T)})
ck(h(proof)==ph,'unchanged_candidate')
out={'unit':'KH003','status':'PASS_TESTED_INSTANCES_ONLY','proof_sha256':ph,'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'arithmetic':'Exact integer/Fraction only; no approximate pass/fail tests.','counts':dict(counts),'complete_finite_records':records,'limitations':'Structural small-word/DP checks are not full theorem-domain simulations. Probability conditioning, universal kernels/maps, analytic limits and inherited source interfaces require fresh full independent review.'}
(D/'KH003_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'counts':dict(counts)}))
