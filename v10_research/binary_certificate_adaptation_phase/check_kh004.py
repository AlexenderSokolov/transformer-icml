#!/usr/bin/env python3
"""Author exact diagnostics for KH004, not formal verification."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter,defaultdict
import hashlib,json,datetime
D=Path(__file__).resolve().parent;R=D.parent;counts=Counter();c=F(1,4096)
p=D/'KH004_constant_crossing_window_obstruction.md';ph='ec332fdd75eed3401f389804f4f1ed21a46b1bc1d8a8c09f68088676e47da814'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(b,s):
 assert b,s
 counts[s]+=1
def mul(A,B):return [[sum(A[i][z]*B[z][j] for z in range(4)) for j in range(4)] for i in range(4)]
def kernel(a,t):return [[1-a,a,0,0],[0,0,F(1,2),F(1,2)],[F(1,2),F(1,2),0,0],[0,0,t,1-t]]
def mv(v,P):return [sum(v[i]*P[i][j] for i in range(4)) for j in range(4)]
ck(h(p)==ph,'candidate_hash');ck(h(D/'revisions/KH004_initial_candidate.md')==ph,'actual_snapshot')
for u in ['KH001','SC003','BT002']:
 q=json.loads((R/f'intake/{u}_acceptance.json').read_text());ck(h(R/q['proof'])==q['sha256'],'accepted_source_hash')
records=[]
for n in [256,257,512]:
 for mexp,bexp,kexp,rexp in [(24,24,17,6),(60,60,41,18),(12,12,9,2),(24,20,17,2),(24,22,17,4)]:
  M=n**mexp;beta=F(1,n**bexp);k=n**kexp;r=n**rexp;T=int(1/(8*beta));q=16*c*r*k;J0=max(k,(q.numerator+q.denominator-1)//q.denominator)
  ck(F(1,M)<=beta<=F(1,16) and M>=64,'finite_beta_domain')
  ck(k<=T and k>=64/c and k**3>=2**22*M*M and k*k>=2**23*M,'finite_concentration_domain')
  ck(r>=2 and r<=F(k,4) and F(r)*c*k/M<=F(1,16) and F(16*r)/(c*k)<=F(1,16) and J0<=T,'finite_window_domain')
  for j in sorted(set([J0,(J0+T)//2,T])):
   x=c*k/M;y=F(j,M);w=1-y-2*x;a=c*k/(2*j);t=x/(2*w);v=[y,x,x,w];P=kernel(a,t);P2=mul(P,P);P3=mul(P2,P);lam=c*k/(16*j)
   ck(mv(v,P)==v and sum(v)==1,'stationary_family')
   ck(w>=F(3,4) and 0<a<=c/2 and 0<t<=F(1,4),'legal_probabilities')
   for u,z in product(range(4),repeat=2):ck(P2[u][z]>=beta*v[z],'all_sixteen_clean_certificate')
   ck(a>=2*beta,'true_target_gap')
   for u in range(4):ck(P3[u][3]>=a/4>=lam,'three_step_atom')
   ck(lam*M/4>=c*k/8 and 1/(1+lam*M/4)<=8/(c*k)<=F(1,8),'endpoint_contraction')
   ck(1/(1+lam*M/8)<=16/(c*k),'late_mixing_bound')
   fail=2*(1536*F(j)/(c*k*k)+7168*F(j*j)/(c*k**3)+917504*F(j)/(k*k))
   upper=917504*F(M*M)/(k**3)+1802240*F(M)/(k*k)
   ck(fail<=upper<=F(111,256),'conditioned_concentration')
   ck(a<=F(1,32*r) and 2*r*a<=F(1,16),'first_boundary')
   ck(F(r)*x+F(16*r)/(c*k)<=F(1,8),'late_boundary')
   ck(2*r*a+F(r)*x+F(16*r)/(c*k)<=F(3,16),'joint_boundary')
   ck(F(1)-F(111,256)-F(1,4)==F(81,256)>F(1,4),'retained_mass')
   ck(F(j)-F(5*k,16)>=F(11*k,16)>=r-2,'zero_loop_boundary')
   ck(F(M)-j-F(3*k,8)>=F(53*M,64)>=r-2,'one_loop_boundary')
   q0=F(1,2*M);p1=beta/(beta+q0);p0=1-p1;nv=[p0*(1-beta),p0*beta,p1*q0,p1*(1-q0)]
   N=[[1-beta,beta,0,0],[0,0,q0,1-q0],[1-beta,beta,0,0],[0,0,q0,1-q0]];N2=mul(N,N)
   for u,z in product(range(4),repeat=2):ck(N2[u][z]>=beta*nv[z],'all_sixteen_null_certificate')
   ck(p1*(1-M*q0)*q0*(1-beta*(j-1))>=F(1,8*M),'whole_null_word_Bernoulli_lower')
   counts['complete_finite_family_cases']+=1
  # Diagnostics distinguish a valid old baseline from genuinely enlarged domain.
  old_delta_sq=beta
  # squared comparison delta^5*k^3>=2^20 avoids irrational square root
  old_threshold_pass=(beta**5*k**6>=2**40)
  if beta==F(1,M) and not old_threshold_pass:counts['critical_cases_outside_old_concentration_domain']+=1
  if beta==F(1,M) and r**6>M:counts['critical_cases_above_old_width_power']+=1
  records.append({'n':n,'M_exponent':mexp,'beta_inverse_exponent':bexp,'k_exponent':kexp,'r_exponent':rexp,'M':str(M),'beta':str(beta),'k':str(k),'r':str(r),'J0':str(J0),'T':str(T),'old_concentration_threshold_pass':old_threshold_pass})
# Symbolically-derived constants reconstructed exactly.
ck(2*7168/(64*c)==917504,'quadratic_variance_coefficient')
ck(2*(1536/c+917504)/8==1802240,'linear_variance_coefficient')
ck(F(917504,2**22)+F(1802240,2**23)==F(111,256),'failure_constant')
ck(F(1,8)*F(1,8)*F(1,2)==F(1,128) and F(1,2)*4==2,'risk_constants')
# Independent of huge finite domain: exact time-inhomogeneous marginals of small
# constant-crossing chains test late-state union bounds and generic atom mixing.
for a,t in [(F(1,8),F(1,16)),(F(1,32),F(1,64)),(F(1,4),F(1,8))]:
 P=kernel(a,t);x=1/(F(1,2)/a+2+F(1,2)/t);pi=[x/(2*a),x,x,x/(2*t)];lam=a/8
 for M in [8,12,16,20]:
  marg=[ [F(1),F(0),F(0),F(0)] ]
  for m in range(M):marg.append(mv(marg[-1],P))
  for m in range(M+1):
   alpha=(1-lam)**(m//3)
   ck(abs(marg[m][1]-x)<=alpha,'structural_marginal_mixing')
  for r in range(2,min(6,M//2)+1):
   law={(0,True,0):F(1)}
   for m in range(M):
    new=defaultdict(F)
    for (s,first,run),mass in law.items():
     qb=P[s][((s&1)<<1)|1]
     for bit,prob in [(0,1-qb),(1,qb)]:
      ns=((s&1)<<1)|bit;nf=first and not(m+3<=r and bit);nr=min(r,run+1) if bit else 0
      new[ns,nf,nr]+=mass*prob
    law=new
   E=sum(v for (s,f,z),v in law.items() if s==3)
   bad=sum(v for (s,f,z),v in law.items() if s==3 and z<r)
   union=sum(marg[m][1]*F(1,2) for m in range(M+2-r,M))
   mixunion=sum((x+(1-lam)**(m//3))*F(1,2) for m in range(M+2-r,M))
   ck(bad<=union<=mixunion,'late_011_union_DP')
   ck(E>0 and bad/E<=union/E,'actual_conditional_DP')
   counts['structural_late_window_DP_cases']+=1
ck(h(p)==ph,'unchanged_candidate')
out={'unit':'KH004','status':'PASS_TESTED_INSTANCES_ONLY','proof_sha256':ph,'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'arithmetic':'Exact integer/Fraction, no floating-point pass/fail tests.','counts':dict(counts),'complete_finite_records':records,'limitations':'Small-horizon DP/mixing examples are structural, not joint huge-domain cases. Analytic conditional concentration, universal kernels, canonicalization interface and asymptotic growing-window proof require fresh full review. Old domain failures indicate genuine extension, not defects in the valid KH003 baseline.'}
(D/'KH004_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'counts':dict(counts)}))
