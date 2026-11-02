#!/usr/bin/env python3
"""Exact finite diagnostic for BA001/BA002, not a proof of all instances."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json, hashlib, math
ROOT=Path(__file__).resolve().parent
STATES=[(0,0),(0,1),(1,0),(1,1)]

def kernel(theta):
    P=[[F(0) for _ in STATES] for _ in STATES]
    for i,(u,v) in enumerate(STATES):
        for c in [0,1]: P[i][STATES.index((v,c))]=theta[i] if c else 1-theta[i]
    return P

def matmul(A,B): return [[sum(A[i][z]*B[z][j] for z in range(4)) for j in range(4)] for i in range(4)]
def stationary(P,pi): return [sum(pi[i]*P[i][j] for i in range(4)) for j in range(4)]==pi

def accept(M,k,t,a):
    r=F(1,2*M); b=r*(1-a)/a
    theta=[a,b,a,1-r]
    # Exact sub-probability, discarding state 11 and >k emitted ones.
    dp={(2,0):F(1)}
    for _ in range(t):
        nd=defaultdict(F)
        for (state,n),p in dp.items():
            u,v=STATES[state]
            for c in [0,1]:
                ns=STATES.index((v,c)); nn=n+c
                if ns==3 or nn>k: continue
                nd[(ns,nn)]+=p*(theta[state] if c else 1-theta[state])
        dp=nd
    return sum(p for (state,n),p in dp.items() if state==0)

rows=[]; count_membership=0; count_acceptance=0; min_accept=(F(1),None)
for M in [64,65,127,128,256]:
    r=F(1,2*M); theta=[r,1-r,r,1-r]
    P=kernel(theta); P2=matmul(P,P); pi=[(1-r)/2,r/2,r/2,(1-r)/2]
    assert stationary(P,pi)
    ratios=[P2[i][j]/pi[j] for i in range(4) for j in range(4)]
    assert min(ratios)==F(1,M)
    assert (r/2)*(1-r)**M>=F(1,8*M)
    T=M//8
    kvals=sorted(set([1,2,max(1,T//2),T]))
    for k in kvals:
        tvals=sorted(set([k,(k+T)//2,T]))
        for t in tvals:
            for a in [F(k,8*t),F(3*k,16*t),F(k,4*t)]:
                b=r*(1-a)/a; pa=[(1-a)/2,a/2,a/2,(1-a)/2]
                P=kernel([a,b,a,1-r]); P2=matmul(P,P)
                assert F(1,M)<=a<=F(1,4) and 0<b<=F(1,2)
                assert stationary(P,pa)
                assert P2[1][2]/pa[2]==2*r*r*(1-a)/(a*a)
                v=(r/2)*(1-r)**M
                w=((1-a)/2)*(1-r)**(M-t-1)*r
                assert v/w==(1-r)**(t+1)/(1-a)<=F(4,3)
                assert F(8*t,k)<=2/a
                count_membership+=1
                success=accept(M,k,t,a)
                assert success>=F(1,4)
                count_acceptance+=1
                if success<min_accept[0]: min_accept=(success,dict(M=M,k=k,t=t,a=str(a)))
    rows.append(dict(M=M,T=T,null_min_certificate=str(F(1,M))))

# Full-word exact triple counts, Hamming budget and endpoint, all legal tested k,t.
count_words=0
for M in range(64,129):
    for k in range(1,(M-1)//4+1):
        for t in range(4*k,M):
            x=[1]*(M+1-t)+[0]*(t+1)
            z=x.copy(); start=M+1-t
            for j in range(1,k+1): z[start+3*j-1]=1
            assert len(z)==M+2 and sum(a!=b for a,b in zip(x,z))==k
            assert z[-2:]==x[-2:]==[0,0]
            hist=[0,0]
            for j in range(M):
                if z[j:j+2]==[0,0]: hist[z[j+2]]+=1
            assert sum(hist)==t-1-2*k and hist[1]==k
            qhat=F(k+1,t+1-2*k); r=F(1,2*M)
            assert qhat-r>=F(k,2*(t+1))
            count_words+=1

# Display asymptotic lower/H ratios for a hypothetical clean multiplier C=1.
scalar=[]
for exponent in [8,12,16,24,32,48,64,96,128]:
    M=2**exponent; k=math.isqrt(math.isqrt(M**3)) if exponent%4 else 2**(3*exponent//4)
    T=M//8; s=1/math.sqrt(M); eps=k/M
    main=3*eps/1024*math.log((T+1)/k)
    penalty=(8/3)*s*math.log(2*T/k)
    H=min(1,max(s,eps*(1+math.log1p(math.sqrt(M)/k))))
    scalar.append(dict(log2M=exponent,k=k,BA1_over_H=max(0,main-penalty)/H,main_over_H=main/H,penalty_over_H=penalty/H))

proofs=['BA001_joint_blindness_obstruction.md','BA002_addone_failure_and_open_beta_known.md']
report=dict(status='PASS_TESTED_INSTANCES_ONLY',exact_stationarity_certificate_checks=count_membership,
 exact_acceptance_cases=count_acceptance,minimum_acceptance={'value':str(min_accept[0]),'float':float(min_accept[0]),'case':min_accept[1]},
 full_word_edit_count_cases=count_words,source_rows=rows,asymptotic_scalar_examples=scalar,
 proof_hashes={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in proofs},
 limitations='Finite diagnostics corroborate only tested instances; they are not the universal proof, formal verification, or independent review.')
(ROOT/'BA001_author_diagnostics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['asymptotic_scalar_examples','source_rows']},indent=2))
