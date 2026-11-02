"""Independent exact finite checks for AB001/AB002; not a proof of infinite scope."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import hashlib,json,math

ROOT=Path(__file__).resolve().parent
STATES=((0,0),(0,1),(1,0),(1,1))
def pair_matrix(theta):
    out=[]
    for i,(x,y) in enumerate(STATES):
        out.append([((theta[i] if z==1 else 1-theta[i]) if y==v else F(0)) for v,z in STATES])
    return out
def square(P):
    return [[sum((P[i][j]*P[j][l] for j in range(4)),F(0)) for l in range(4)] for i in range(4)]
def continuation_accept(theta,t,k):
    # Exact law, with any 11 visit rejected immediately; accepted paths count <= k ones.
    d={(2,0):F(1)}
    for _ in range(t):
        nxt=defaultdict(F)
        for (i,n),mass in d.items():
            x,y=STATES[i]
            for z in (0,1):
                j=STATES.index((y,z)); nn=n+z
                if j==3 or nn>k: continue
                nxt[j,nn]+=mass*(theta[i] if z else 1-theta[i])
        d=nxt
    return sum((mass for (i,n),mass in d.items() if i==0),F(0))

counts={'null_certificate':0,'alternative_stationarity':0,'ratio_identity':0,'acceptance_dp':0,'kernel_strings':0,'scalar_integrals':0}
accept_min=None;accept_arg=None
for M in (64,65,96,128,257,512):
    r=F(1,2*M); beta=F(1,M);T=M//8
    theta_star=(r,1-r,r,1-r);P=pair_matrix(theta_star);P2=square(P)
    pi_star=((1-r)/2,r/2,r/2,(1-r)/2)
    assert all(sum((pi_star[i]*P[i][j] for i in range(4)),F(0))==pi_star[j] for j in range(4))
    ratios=[P2[i][j]/pi_star[j] for i in range(4) for j in range(4)]
    assert min(ratios)==beta
    counts['null_certificate']+=1
    v=r*F(1,2)*(1-r)**M
    assert v>=F(1,8*M)
    for k in sorted({1,2,3,max(1,T//2),T}):
        if k>T:continue
        for t in sorted({k,min(T,k+1),min(T,2*k),T}):
            lo,hi=F(k,8*t),F(k,4*t)
            for a in (lo,(lo+hi)/2,hi):
                assert F(1,M)<=a<=F(1,4)
                b=r*(1-a)/a;theta=(a,b,a,1-r)
                assert F(0)<b<=F(1,2)
                pi=((1-a)/2,a/2,a/2,(1-a)/2)
                Q=pair_matrix(theta);Q2=square(Q)
                assert all(sum((pi[i]*Q[i][j] for i in range(4)),F(0))==pi[j] for j in range(4))
                counts['alternative_stationarity']+=1
                assert Q2[1][2]/pi[2]==2*r*r*(1-a)/(a*a)
                w=(1-a)/2*(1-r)**(M-t-1)*r
                assert v/w==(1-r)**(t+1)/(1-a)<=F(4,3)
                assert F(8*t,k)<=2/a
                counts['ratio_identity']+=1
                pacc=continuation_accept(theta,t,k)
                assert pacc>=F(1,4),(M,k,t,a,pacc)
                counts['acceptance_dp']+=1
                if accept_min is None or pacc<accept_min:
                    accept_min=pacc;accept_arg=(M,k,t,str(a))
            h=sum((1/j for j in range(k,t+1)))
            assert h+1e-14>=math.log((t+1)/k)
            counts['scalar_integrals']+=1

for M in range(64,130):
    for k in range(1,(M-1)//4+1):
        # Every supported suffix for each tested M,k.
        for t in range(4*k,M):
            x='1'*(M+1-t)+'0'*(t+1)
            z=list(x);first_zero=M+1-t
            for j in range(1,k+1): z[first_zero+3*j-1]='1'
            z=''.join(z)
            assert len(x)==M+2 and z[-2:]==x[-2:]=='00'
            edit_positions=[i for i,(u,v) in enumerate(zip(x,z)) if u!=v]
            assert len(edit_positions)==k and max(edit_positions)<M
            J=sum(z[i:i+2]=='00' for i in range(M))
            C=sum(z[i:i+3]=='001' for i in range(M))
            assert (J,C)==(t-1-2*k,k)
            q=F(C+1,J+2);r=F(1,2*M)
            assert abs(q-r)>=F(k,2*(t+1))
            counts['kernel_strings']+=1

sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'AB001_joint_blindness_obstruction.md',ROOT/'AB002_addone_failure_and_open_beta_known.md')}
result={'status':'PASS','arithmetic':'Fraction exact except the explicitly labeled harmonic/log scalar diagnostic',
        'counts':counts,'minimum_acceptance_probability_exact':str(accept_min),
        'minimum_acceptance_probability_float':float(accept_min),'minimum_acceptance_case':accept_arg,
        'source_sha256':sources,'scope':'Independent finite diagnostics corroborate tested instances; full theorem is assessed separately in the mathematical review, not formally verified.'}
(ROOT/'review_joint_blindness_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
