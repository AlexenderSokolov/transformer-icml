#!/usr/bin/env python3
"""Author exact diagnostics, finite instances only; not a proof of KH001."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product
import hashlib,json,datetime
D=Path(__file__).resolve().parent; proof=D/'KH001_histogram_strong_side_obstruction.md'
expected='311adf683a22370fe765f61045a96af4a201e611ceeb9136f53a2b1f8cc7fd27'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert h(proof)==expected
counts=Counter();c=F(1,4096);perm=[0,2,1,3]
def ck(v,key):
 assert v,key
 counts[key]+=1
def mul(A,B):return [[sum(A[i][z]*B[z][j] for z in range(4)) for j in range(4)] for i in range(4)]
def kernel(a,b,e,t):
 return [[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]]
def pi(a,b,e,t):
 x=1/(e/a+2+b/t);return [x*e/a,x,x,x*b/t]
def stationary(P,v):
 for j in range(4):ck(sum(v[i]*P[i][j] for i in range(4))==v[j],'stationarity')
def reverse(P,v):
 Q=[[v[j]*P[j][i]/v[i] for j in range(4)] for i in range(4)]
 for i,j in product(range(4),repeat=2):ck(Q[perm[i]][perm[j]]==P[i][j],'generic_reverse_entries')
# No symmetric-source assumption in reversal: all four exits independently vary.
for a,b,e,t in product([F(1,7),F(1,3),F(2,3),F(6,7)],repeat=4):
 P=kernel(a,b,e,t);v=pi(a,b,e,t);stationary(P,v);reverse(P,v)
 counts['generic_reverse_families']+=1

def hist(w):return Counter(w[i:i+3] for i in range(len(w)-2))
def J(w,s):return sum(w[i:i+2]==s for i in range(len(w)-2))
def canon(w):
 H=hist(w);edges=[w[i:i+3] for i in range(len(w)-2) if w[i:i+3] not in ('000','111')]
 z='11'+'1'*H['111']
 for edge in edges:
  ck(z[-2:]==edge[:2],'canonical_continuity')
  z+=edge[-1]
 z+='0'*H['000'];return z
for n in range(4,19):
 for mid in product('01',repeat=n-4):
  w='11'+''.join(mid)+'00';rev=w[::-1];z=canon(w)
  ck(J(rev,'00')==J(w,'00')+1,'reverse_00_departure_plus_one')
  ck(J(rev,'01')+J(rev,'10')==J(w,'01')+J(w,'10'),'reverse_cross_departures')
  ck(hist(w)==hist(z),'canonical_histogram')
  ck(z[:2]=='11' and z[-2:]=='00' and len(z)==n,'canonical_boundary_length')
  cross=J(w,'01')+J(w,'10')
  for j in range(2,n-1):
   null='1'*(n-j)+'0'*j;dist=sum(u!=v for u,v in zip(z,null))
   ck(dist<=3*cross+abs(J(w,'00')-j),'fixed_null_distance')
  counts['exhaustive_words']+=1

records=[]
# Complete finite-domain examples include beta=1/M and strictly stronger beta.
for n in [128,129,256]:
 for mexp,bexp,kexp in [(24,18,16),(24,20,18),(24,22,20),(24,24,22)]:
  M=n**mexp;delta=F(1,n**(bexp//2));beta=delta**2;k=n**kexp;T=(1/(8*beta)).numerator//(1/(8*beta)).denominator
  ck(M>=64 and F(1,M)<=beta<=F(1,16),'finite_beta_domain')
  ck(32<=k<=T and k*k>=4*M and k*delta>=6/c and delta**5*k**3>=2**20 and delta**3*k*k>=2**21,'complete_finite_k_domain')
  for j in sorted(set([k,2*k,(k+T)//2,T])):
   x=c*k/M;y=F(j,M);w=1-y-2*x;e=1-delta;a=c*k*e/j;t=x*delta/w;v=[y,x,x,w];P=kernel(a,delta,e,t)
   stationary(P,v);reverse(P,v)
   ck(v==pi(a,delta,e,t),'clean_stationary_formula')
   ck(0<a<=c and a>=delta and a>=2*beta and w>=F(3,4) and 0<t<=F(1,4),'clean_legal_bounds')
   P2=mul(P,P);P3=mul(P2,P);lam=c*k*delta/(4*j)
   for u,z in product(range(4),repeat=2):ck(P2[u][z]>=beta*v[z],'actual_beta_certificate_entry')
   for u in range(4):ck(P3[u][3]>=a*delta/2>=lam,'three_step_atom')
   ck(lam*M/4>=3 and w-F(1,4)>=F(1,2),'endpoint_mixing_bounds')
   fail1=384*F(j,1)/(c*delta*k*k)
   fail2=1792*F(j*j,1)/(c*delta*k**3)
   fail3=229376*F(j,1)/(delta*k*k)
   failbound=229376/(delta**5*k**3)+450560/(delta**3*k*k)
   ck(2*(fail1+fail2+fail3)<=failbound<=F(111,256)<F(1,2),'conditional_bad_event')
   ck(F(k,8)+F(k,32)+1<=F(3*k,16) and F(3*k,16)<F(k,4),'reverse_endpoint_correction_charge')
   ck(F(3*k,16)+F(k,4)<=F(7*k,16)<k,'strict_budget_bound')
   r=F(1,2*M);p1=beta/(beta+r);p0=1-p1;N=kernel(beta,1-r,1-beta,r);nv=[p0*(1-beta),p0*beta,p1*r,p1*(1-r)];N2=mul(N,N)
   stationary(N,nv)
   for u,z in product(range(4),repeat=2):ck(N2[u][z]>=beta*nv[z],'null_all_state_certificate_entry')
   ck(p1>=F(2,3) and (M+1-j)*r<=F(1,2) and (j-1)*beta<=F(1,8),'exact_prefix_Bernoulli_inputs')
   ck(p1*(1-M*r)*r*(1-beta*(j-1))>=F(1,8*M),'exact_word_lower_via_Bernoulli')
   ck(p1*r<=F(1,2*M),'exact_word_upper')
   counts['complete_finite_clean_families']+=1
  records.append({'n':n,'M_exponent':mexp,'beta_inverse_exponent':bexp,'k_exponent':kexp,'M':str(M),'beta':str(beta),'k':str(k),'T':str(T)})
# Moderate exact powers test the full null-word formula; these are structural
# checks, not claimed joint finite-theorem-domain cases.
for M in [64,65,128,256]:
 for beta in [F(1,M),F(2,M),F(1,16)]:
  if not F(1,M)<=beta<=F(1,16):continue
  r=F(1,2*M);p1=beta/(beta+r);T=int(1/(8*beta))
  for j in range(2,T+1):
   v=p1*(1-r)**(M+1-j)*r*(1-beta)**(j-1)
   ck(F(1,8*M)<=v<=F(1,2*M),'full_word_exact_probability_bounds')
# Coefficient reconstruction, all exact.
ck(2*1792/(64*c)==229376,'variance_coefficient')
ck(2*(384/c+229376)/8==450560,'linear_failure_coefficient')
ck(F(229376,2**20)+F(450560,2**21)==F(111,256),'failure_fraction')
ck(F(1,8)*F(1,4)*F(1,2)==F(1,64),'risk_positive_coefficient')
ck(F(1,2)*2==1,'risk_penalty_coefficient')
ck(h(proof)==expected,'unchanged_proof')
out={'unit':'KH001','status':'PASS_TESTED_INSTANCES_ONLY','proof_sha256':expected,'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'arithmetic':'Exact integers and Fractions only; no approximate pass/fail tests.','counts':dict(counts),'complete_domain_records':records,'limitations':'Finite corroboration only. Generic reversal and small-word tests are structural, not all full-theorem-domain instances. Coupling, conditional path law, stochastic-kernel quantifiers, analytic variance and curve limits require full independent proof review.'}
(D/'KH001_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'counts':dict(counts)}))
