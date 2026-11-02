#!/usr/bin/env python3
"""Exact finite author diagnostics for BK002; not universal proof or independent review."""
from fractions import Fraction as F
from pathlib import Path
import math,json,hashlib
HERE=Path(__file__).resolve().parent
STATES=[(0,0),(0,1),(1,0),(1,1)]
def mat(theta):
 P=[[F(0)]*4 for _ in range(4)]
 for i,(u,v) in enumerate(STATES):
  for bit in [0,1]:P[i][STATES.index((v,bit))]=theta[i] if bit else 1-theta[i]
 return P
def square(P):return [[sum(P[i][h]*P[h][j] for h in range(4)) for j in range(4)] for i in range(4)]
counts={'family_stationarity_all16_certificate':0,'prefix_ratio_exact_powers':0,'density_inequality':0,'reference_acceptance_dp':0,'ordered_path_domination':0,'strict_budget_endpoint':0,'one_quarter_sequence':0}
min_accept=(F(1),None)
for M in [256,288,512,1024,4096,16384,65536]:
 T=M//8;k0=math.isqrt(4*M);k0+=(k0*k0<4*M)
 if k0>T:continue
 for k in sorted(set([k0,(k0+T)//2,T])):
  delta=F(1,k);tau=F(1,4*M);r=F(1,2*M);beta=delta*delta;e=1-delta
  for t in sorted(set([k,(k+T)//2,T])):
   for a in [F(k,32*t),F(3*k,64*t),F(k,16*t)]:
    x=1/(e/a+2+delta/tau);pi=[x*e/a,x,x,x*delta/tau];w=pi[3]
    assert a>=delta and a<=F(1,16) and w>=F(1,3) and x<=F(k,4*M)
    P=mat([a,delta,delta,1-tau]);P2=square(P)
    assert [sum(pi[h]*P[h][j] for h in range(4)) for j in range(4)]==pi
    assert all(P2[i][j]>=beta*pi[j] for i in range(4) for j in range(4))
    counts['family_stationarity_all16_certificate']+=1
    assert F(32*t,k)<=2/a;counts['density_inequality']+=1
    assert w*tau*F(3,4)>=F(1,16*M)
    if M<=1024:
     v=(r/2)*(1-r)**M;pref=w*(1-tau)**(M-t-1)*tau
     assert F(1,8*M)<=v<=F(1,4*M) and pref>=F(1,16*M) and v/pref<=4
     counts['prefix_ratio_exact_powers']+=1
    if t<=64:
     dp={(2,0):F(1)}
     theta=[a,F(0),delta,F(0)]
     for _ in range(t):
      nd={}
      for (state,ones),p in dp.items():
       u,v=STATES[state]
       for bit in [0,1]:
        ns=STATES.index((v,bit));nones=ones+bit
        prob=theta[state] if bit else 1-theta[state]
        if prob and ns!=3 and nones<=k:nd[(ns,nones)]=nd.get((ns,nones),F(0))+p*prob
      dp=nd
     acc=sum(p for (state,ones),p in dp.items() if state==0)
     assert acc>=F(1,2)
     counts['reference_acceptance_dp']+=1
     if acc<min_accept[0]:min_accept=(acc,{'M':M,'k':k,'t':t,'a':str(a)})
for k in range(2,513):
 assert (1-F(1,k))**k>=F(1,4);counts['one_quarter_sequence']+=1
# Full ordered suffix enumeration checks the local likelihood lemma at small horizons.
# This deliberately checks the lemma's wider domain, not the giant theorem domain.
for k in [4,8,16]:
 delta=F(1,k);e=1-delta
 for a in sorted(set([delta,F(1,4)])):
  for t in range(2,17):
   def walk(state,bits,probR,probQ):
    if len(bits)==t:
     if state!=0 or sum(bits)>k:return
     assert probQ>=probR/4
     counts['ordered_path_domination']+=1
     M=64;original=[1]*(M+1-t)+[0]*(t+1)
     out=original[:-t]+bits
     assert len(out)==M+2 and out[-2:]==[0,0]
     assert sum(x!=y for x,y in zip(original,out))==sum(bits)<=k
     counts['strict_budget_endpoint']+=1
     return
    u,v=STATES[state]
    for bit in [0,1]:
     pr=([a,F(0),delta,F(0)][state] if bit else 1-[a,F(0),delta,F(0)][state])
     pq=([a,delta,delta,F(0)][state] if bit else 1-[a,delta,delta,F(0)][state])
     if pr:walk(STATES.index((v,bit)),bits+[bit],probR*pr,probQ*pq)
   walk(2,[],F(1),F(1))
assert F(32)*F(2048,3)==F(65536,3)
proof='BK002_full_history_supplied_beta_obstruction.md'
out={'status':'PASS_TESTED_INSTANCES_ONLY','arithmetic':'Fraction exact; no floating-point probability checks',
 'counts':counts,'minimum_acceptance_exact':str(min_accept[0]),'minimum_acceptance_float':float(min_accept[0]),'minimum_acceptance_case':min_accept[1],
 'proof_sha256':hashlib.sha256((HERE/proof).read_bytes()).hexdigest(),
 'limitations':'Finite cases only. Small ordered-path enumeration checks a component lemma over a wider parameter domain; it does not purport to enumerate full theorem histories. Common-a integration and all-domain arguments require fresh full review.'}
(HERE/'BK002_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
