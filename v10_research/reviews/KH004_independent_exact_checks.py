#!/usr/bin/env python3
"""Fresh KH004 reviewer diagnostics. Exact finite tests, not formal verification.
Does not import or execute author diagnostics or earlier reviewer checks.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
from math import isqrt
import hashlib,json
import sympy as s
R=Path(__file__).resolve().parents[1]; counts=Counter(); inputs={}; examples={}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def chk(v,label):
 if not v:raise AssertionError(label)
 counts[label]+=1
def bind(p):inputs[str(p.relative_to(R))]=sha(p)
proof=R/'binary_certificate_adaptation_phase/KH004_constant_crossing_window_obstruction.md'
for p in [proof,R/'reviews/KH004_audit_snapshots/KH004_received.md']:
 chk(sha(p)=='ec332fdd75eed3401f389804f4f1ed21a46b1bc1d8a8c09f68088676e47da814','frozen_bytes');bind(p)
for unit in ['KH001','KH002','KH003','BK001','SC003','BT002']:
 rp=R/f'intake/{unit}_acceptance.json'
 if unit=='KH003':rp=R/'intake/KH003_root_acceptance.json'
 rec=json.loads(rp.read_text());bind(rp)
 chk(rec['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW','accepted_status')
 p=R/rec['proof'];chk(sha(p)==rec['sha256'],'accepted_proof_bytes');bind(p)
 p=R/rec['review'];bind(p)
 if 'review_sha256' in rec:chk(sha(p)==rec['review_sha256'],'accepted_review_bytes')
 for n,h in rec.get('component_proofs',{}).items():
  p=R/n;chk(sha(p)==h,'accepted_components');bind(p)
# Every inherited final KH003 review binding, including transitive proofs/receipts.
p=R/'reviews/KH003_independent_review_bindings.json';bind(p)
for n,h in json.loads(p.read_text())['files'].items():
 p=R/n;chk(sha(p)==h,'inherited_review_binding');bind(p)
# Symbolic kernel algebra independent of manuscript matrix.
x,y=s.symbols('x y',positive=True); w=1-y-2*x;a=x/(2*y);t=x/(2*w)
P=s.zeros(4)
for state,q in enumerate([a,s.Rational(1,2),s.Rational(1,2),1-t]):
 P[state,2*(state%2)]=1-q;P[state,2*(state%2)+1]=q
pi=s.Matrix([[y,x,x,w]]); RR=s.zeros(4)
for i,j in enumerate([0,2,1,3]):RR[i,j]=1
for z in pi*P-pi:chk(s.simplify(z)==0,'symbolic_stationarity')
rev=s.diag(y,x,x,w).inv()*P.T*s.diag(y,x,x,w)
for z in RR*rev*RR-P:chk(s.simplify(z)==0,'symbolic_reversal')
expected=s.Matrix([[(1-a)**2,(1-a)*a,a/2,a/2],[s.Rational(1,4),s.Rational(1,4),t/2,(1-t)/2],[(1-a)/2,a/2,s.Rational(1,4),s.Rational(1,4)],[t/2,t/2,(1-t)*t,(1-t)**2]])
for z in P*P-expected:chk(s.simplify(z)==0,'all16_symbolic_square')
c=F(1,4096)
# Feasible huge integer cases, including genuinely growing windows beyond M^(1/6).
finite=[]
for exponent,rpow in [(120,0),(180,30),(240,50),(360,100)]:
 M=2**exponent;r=2 if not rpow else 2**rpow
 # M is perfect cube. k=floor(sqrt((M/r)*M^(2/3))) exactly.
 k=isqrt((M//r)*2**(2*exponent//3)); beta=F(1,M);T=M//8;J=max(k,(16*c*r*k).__ceil__())
 assumptions=[k<=T,k>=64/c,k**3>=2**22*M**2,k*k>=2**23*M,4*r<=k,r*c*k/M<=F(1,16),16*r/(c*k)<=F(1,16),J<=T]
 for v in assumptions:chk(v,'finite_domain')
 for j in sorted({J,(J+T)//2,T}):
  xx=c*k/M;yy=F(j,M);ww=1-yy-2*xx;aa=c*k/(2*j);tt=xx/(2*ww);lam=c*k/(16*j)
  p=P.subs({x:s.Rational(xx.numerator,xx.denominator),y:s.Rational(yy.numerator,yy.denominator)})
  pp=p*p;ppp=pp*p;pis=[yy,xx,xx,ww]
  for u in range(4):
   for v in range(4):chk(pp[u,v]>=beta*pis[v],'all16_rational_certificate')
   chk(ppp[u,3]>=lam,'common_atom')
  chk(aa>=2*beta,'target_separation')
  chk(1/(1+lam*(M//3))<=8/(c*k)<=F(1,8),'endpoint_mixing')
  m=M+2-r
  chk(m>=M//2 and m//3>=M//8,'late_index_floors')
  chk(1/(1+lam*(m//3))<=16/(c*k),'late_mixing')
  chk(2*r*aa<=F(1,16),'early_conditioned_cost')
  chk(r*(xx+16/(c*k))<=F(1,8),'late_conditioned_cost')
  fail=2*(1536*j/(c*k*k)+7168*j*j/(c*k**3)+F(917504*j,k*k))
  chk(fail<=F(917504*M*M,k**3)+F(1802240*M,k*k)<=F(111,256),'conditioned_concentration')
 finite.append({'M':str(M),'r':str(r),'k':str(k),'J0':str(J)})
# Exact threshold arithmetic, checked independently from inequalities.
chk(F(917504,2**22)==F(7,32),'variance_threshold')
chk(F(1802240,2**23)==F(55,256),'linear_threshold')
chk(1-F(111,256)-F(3,16)==F(97,256)>F(81,256)>F(1,4),'intersection_slack')
chk(3*16*32==1536,'coupling_constant')
chk(7*16*64==7168,'zero_variance_constant')
chk(7*2*16*64**2==917504,'cross_variance_constant')
chk(2*7168*4096//64==917504 and 2*(1536*4096+917504)//8==1802240,'conditioned_constants')
# Independent exact asymmetric-null tests, including all-state ratios.
for M in [64,128,256]:
 for beta in [F(1,M),F(2,M),F(1,16)]:
  q=F(1,2*M);pi1=beta/(beta+q);pi0=1-pi1;transition=[[1-beta,beta],[q,1-q]]
  for u,v,ss,tt in product(range(2),repeat=4):
   ratio=transition[v][ss]/[pi0,pi1][ss]
   chk(ratio>=beta+q>=beta,'null_all16_certificate')
  for j in range(1,(1/(8*beta)).__floor__()+1):
   mass=pi1*(1-q)**(M+1-j)*q*(1-beta)**(j-1)
   chk(F(1,8*M)<=mass<=F(1,2*M),'exact_null_full_word_weights')
# Enumerate complete endpoint words; validate canonical path and fixed-j geometry.
def hist(w):return Counter(w[i:i+3] for i in range(len(w)-2))
def J(w,v):return sum(w[i:i+2]==v for i in range(len(w)-2))
def can(w):
 h=hist(w);z='11'+'1'*h['111']
 for i in range(len(w)-2):
  e=w[i:i+3]
  if e not in ('000','111'):
   chk(z[-2:]==e[:2],'legal_skeleton');z+=e[-1]
 return z+'0'*h['000']
def hd(v,w):return sum(a!=b for a,b in zip(v,w))
for N in range(4,17):
 for bits in product('01',repeat=N-4):
  w='11'+''.join(bits)+'00';z=can(w);h=hist(w);cross=J(w,'01')+J(w,'10');j0=J(w,'00')
  chk(len(z)==N and z[:2]=='11' and z[-2:]=='00' and hist(z)==h,'canonical_exact_statistic')
  chk(J(w[::-1],'00')==j0+1 and J(w[::-1],'01')+J(w[::-1],'10')==cross,'reverse_departure_shift')
  for j in range(2,N-1):chk(hd(z,'1'*(N-j)+'0'*j)<=3*cross+abs(j0-j),'fixed_j_hamming')
  for r in range(2,N//2+1):
   if w[:r]=='1'*r and w[-r:]=='0'*r:
    chk(z[:r]==w[:r] and z[-r:]==w[-r:],'genuine_windows_preserved')
   v=w[::-1]
   if v[-r:]!='1'*r:
    last=max(i for i in range(N-r,N-2) if v[i]=='0')
    chk(v[last:last+3]=='011' and N-r<=last<=N-3,'last_zero_flux_index')
  counts['endpoint_words']+=1
# Exact state/first-window/trailing-run dynamic program: no stationary-start shortcut.
for aa,tt in [(F(1,7),F(1,13)),(F(1,37),F(1,91)),(F(2,9),F(1,21))]:
 qs=[aa,F(1,2),F(1,2),1-tt]
 xx=1/(1/(2*aa)+2+1/(2*tt));pis=[xx/(2*aa),xx,xx,xx/(2*tt)]
 def prob(w,stationary=True):
  state=int(w[:2],2);out=pis[state] if stationary else F(state==0)
  for ch in w[2:]:
   b=int(ch);out*=qs[state] if b else 1-qs[state];state=2*(state%2)+b
  return out
 for N in range(4,11):
  for bits in product('01',repeat=N):
   w=''.join(bits);chk(prob(w)==prob(w[::-1]),'exact_word_reversal')
 for M in [4,7,12,23,40]:
  N=M+2
  for r in range(2,N//2+1):
   law={(0,True,0):F(1)};flux=F(0)
   for m in range(M):
    if m>=M+2-r:flux+=sum(v for (state,f,t),v in law.items() if state==1)/2
    nxt=defaultdict(F)
    for (state,f,t),v in law.items():
     for b in [0,1]:nxt[2*(state%2)+b,f and not(b and m+3<=r),min(r,t+1) if b else 0]+=v*(qs[state] if b else 1-qs[state])
    law=nxt
   pe=sum(v for (state,f,t),v in law.items() if state==3)
   early=sum(v for (state,f,t),v in law.items() if not f)
   late=sum(v for (state,f,t),v in law.items() if state==3 and t<r)
   bad=sum(v for (state,f,t),v in law.items() if state==3 and (not f or t<r))
   chk(sum(law.values())==1 and pe>0,'DP_normalization')
   chk(early==1-(1-aa)**(r-2)<=(r-2)*aa,'DP_early_exact')
   chk(late<=flux,'DP_late_unconditional_flux')
   chk(bad/pe<=(early+flux)/pe,'DP_condition_only_after_union')
# Independent random-map loss transfer on genuine original windows.
 for N in range(6,11):
  r=3;words=['11'+''.join(b)+'00' for b in product('01',repeat=N-4)]
  words=[w for w in words if w[:r]=='1'*r and w[-r:]=='0'*r]
  mass=sum(prob(w) for w in words)
  chk(mass==pis[0]*sum(prob(w[::-1],False) for w in words),'original_event_charged')
  def loss(w,target):
   h=hist(w);p=F(h['001']+1,h['000']+h['001']+2)
   return (abs(p-target)+2*abs((p+1)/2-target))/3
  clean=sum(prob(w)*loss(w,aa) for w in words)/mass
  for j in range(r,N-r+1):
   orig='1'*(N-j)+'0'*j;k=2;beta=aa/3;acc=F(0);risk=F(0)
   for w in words:
    z=can(w);ok=hd(z,orig)<=k and z[:r]==orig[:r] and z[-r:]==orig[-r:]
    out=z if ok else orig;v=prob(w)/mass
    chk(hd(out,orig)<=k and out[-2:]==orig[-2:],'strict_kernel_all_outputs')
    if ok:
     acc+=v;chk((hist(z),z[:r],z[-r:])==(hist(w),w[:r],w[-r:]),'every_accepted_same_map_input')
    risk+=v*loss(out,beta)
   chk(risk>=acc*(aa-beta)-clean,'randomized_same_map_loss_transfer')
bind(Path(__file__).resolve())
for n,h in inputs.items():chk(sha(R/n)==h,'input_bytes_unchanged')
out={'status':'PASS','candidate_sha256':sha(proof),'assertions':sum(counts.values())-counts['endpoint_words'],'counts':dict(counts),'finite_cases':finite,'bound_inputs':inputs,'limitations':'Finite exact diagnostics corroborate the independent prose proof; not formal verification or exhaustive infinite-domain proof.'}
(R/'reviews/KH004_independent_exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','assertions':sum(counts.values())-counts['endpoint_words'],'counts':dict(counts)},indent=2))
