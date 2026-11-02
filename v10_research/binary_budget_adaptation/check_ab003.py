#!/usr/bin/env python3
"""Exact pathwise and integer-threshold checks for AB003, finite diagnostics only."""
from fractions import Fraction as F
from pathlib import Path
import math,json,hashlib
ROOT=Path(__file__).resolve().parent
cases=0; active=0; inactive=0; min_slack=None
qs=[F(0),F(1,100),F(1,4),F(1,2),F(3,4),F(99,100),F(1)]
for M in [64,100,256,1000,4096]:
    sq=math.isqrt(M); ce=sq+(sq*sq<M); B=12*ce
    for k in sorted(set([0,1,max(1,sq//2),sq])):
        d=6*k
        assert 2*d<=B
        jvals=sorted(set(x for x in [0,1,d,d+1,B//2,B,B+1,2*B,M//2,M] if 0<=x<=M))
        deltas=sorted(set([-d,-d//2,-1,0,1,d//2,d]))
        for J in jvals:
            cvals=sorted(set(x for x in [0,1,d,d+1,B-d,B,B+1,J//2,J] if 0<=x<=J))
            for C in cvals:
                for u in deltas:
                    for v in deltas:
                        if abs(u)+abs(v)>d: continue
                        Cp=C+u; Qp=J-C+v; Jp=Cp+Qp
                        if min(Cp,Qp)<0 or Jp>M: continue
                        out=F(Cp,Jp) if Cp>B else F(0)
                        if Cp>B:
                            active+=1
                            assert J>0 and C>d
                            p=F(C,J); pp=F(Cp,Jp)
                            assert abs(pp-p)<=F(2*d,J)
                            assert pp<=4*p
                        else: inactive+=1
                        for q in qs:
                            E=abs(F(C,J)-q) if J else F(0)
                            tail=q if q and J*q<=3*B else F(0)
                            rhs=5*E+4*min(q,F(36*k,J+2))+tail
                            slack=rhs-abs(out-q)
                            assert slack>=0,(M,k,J,C,Cp,Jp,q,slack)
                            cases+=1
                            if min_slack is None or slack<min_slack:min_slack=slack
threshold_cases=0
for M in range(64,4097):
    sq=math.isqrt(M); ce=sq+(sq*sq<M); B=12*ce
    # Square both nonnegative sides of 64(3B+1)/(M+1)<=2600/sqrt(M).
    assert (64*(3*B+1))**2*M<=2600**2*(M+1)**2
    for q in [F(1,1000),F(1,7),F(1,2),F(1)]:
        x=F(3*B,q); w=x.numerator//x.denominator+1
        assert q*w<=3*B+q
        threshold_cases+=1
assert 5*8193*math.sqrt(32)+2600+16 <2**18
assert 4*600192<2**22
# Envelope subsequence illustration for b=sqrt(M)*log2(log2 M), capped at M.
envelope=[]
for n in [16,32,64,128,256,512,1024]:
    # Work with logs when giant exact M would add no information.
    ratio=math.log2(n); capratio=2**(n/4) if n<1024 else float('inf')
    kr=min(ratio,capratio)
    log_M_over_k=(n/2)*math.log(2)-math.log(kr)
    envelope.append(dict(log2M=n,k_over_sqrtM=kr,log_M_over_k=log_M_over_k))
proof='AB003_small_budget_hard_threshold.md'
out=dict(status='PASS_TESTED_INSTANCES_ONLY',pathwise_rational_cases=cases,
 active_row_configurations=active,inactive_row_configurations=inactive,
 minimum_pathwise_slack=str(min_slack),integer_threshold_cases=threshold_cases,
 exact_squared_constant_checks=4097-64,coefficient_checks='PASS',
 envelope_scalar_examples=envelope,proof_sha256=hashlib.sha256((ROOT/proof).read_bytes()).hexdigest(),
 limitations='Finite checks only; imported universal occupation and clean interfaces are not established by this script. Fresh full review is separate.')
(ROOT/'AB003_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='envelope_scalar_examples'},indent=2))
