#!/usr/bin/env python3
"""Independent BK002 audit diagnostics; exact tested instances, not proof.
Written without importing or reading the author's checker.
"""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import hashlib, json, math

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'binary_beta_known_adaptation/BK002_full_history_supplied_beta_obstruction.md'
EXPECTED='e50381632af4825923138c086c34e7b3b082af381d4b9ec8f641825455c50e12'
assert hashlib.sha256(P.read_bytes()).hexdigest()==EXPECTED, 'Reviewed proof changed'
counts=defaultdict(int)
records=[]

def transition(a,d,tau,reference=False):
    p=[a,F(0) if reference else d,d,1-tau]
    return [[(2*(i%2)+b, (p[i] if b else 1-p[i]), b) for b in (0,1)] for i in range(4)]

def matrix(tab):
    z=[[F(0) for _ in range(4)] for _ in range(4)]
    for i,row in enumerate(tab):
        for j,p,b in row:z[i][j]+=p
    return z

def mul(P,Q):
    return [[sum(P[i][h]*Q[h][j] for h in range(4)) for j in range(4)] for i in range(4)]

def family(M,k,a):
    d=F(1,k); tau=F(1,4*M); e=1-d
    x=1/(e/a+2+d/tau)
    return d,tau,(e*x/a,x,x,x*d/tau)

# Boundary/floor-sensitive domain and a-grid checks. All are exact fractions.
domains=[]
for M in (256,257,263,272,280,288,319,320,511,512,513,1000,1024,2048,4095,4096,4097,10000,65536):
    lo=math.isqrt(4*M)
    if lo*lo<4*M:lo+=1
    T=M//8
    if lo>T:
        counts['empty_finite_domains']+=1
        continue
    ks=sorted(set((lo,(lo+T)//2,T)))
    for k in ks:
        domains.append((M,k))
        low=F(k,32*T)
        for a in (low,(3*low+F(1,16))/4,(low+F(1,16))/2,(low+3*F(1,16))/4,F(1,16)):
            d,tau,pi=family(M,k,a)
            P0=matrix(transition(a,d,tau)); P2=mul(P0,P0)
            assert sum(pi)==1 and all(v>0 for v in pi)
            assert all(sum(pi[i]*P0[i][j] for i in range(4))==pi[j] for j in range(4))
            assert a>=d and pi[1]<=F(k,4*M) and pi[3]>=F(1,3)
            expected=[[(1-a)**2,(1-a)*a,a*(1-d),a*d],[(1-d)**2,(1-d)*d,d*tau,d*(1-tau)],[(1-d)*(1-a),(1-d)*a,d*(1-d),d*d],[tau*(1-d),tau*d,(1-tau)*tau,(1-tau)**2]]
            assert P2==expected
            for i in range(4):
                for j in range(4):
                    assert P2[i][j]>=d*d*pi[j]
                    counts['alternative_certificate_entries']+=1
            counts['stationary_alternatives']+=1
        r=F(1,2*M)
        one=lambda u,v: r if u!=v else 1-r
        pi_star=[one(j//2,j%2)/2 for j in range(4)]
        for i in range(4):
            for j in range(4):
                exact=one(i%2,j//2)*one(j//2,j%2)
                assert exact>=2*r*pi_star[j]>=F(1,k*k)*pi_star[j]
                counts['null_certificate_entries']+=1
        for t in sorted(set((k,(k+T)//2,T))):
            for a in (F(k,32*t),F(3*k,64*t),F(k,16*t)):
                d,tau,pi=family(M,k,a)
                assert low<=a<=F(1,16)
                assert F(32*t,k)<=2/a
                # Multiply actual word probabilities instead of assuming manuscript exponents.
                v=F(1,2)*(1-r)**(M-t)*r*(1-r)**t
                w=pi[3]*(1-tau)**(M-t-1)*tau
                assert v==r*(1-r)**M/2
                assert F(1,8*M)<=v<=F(1,4*M)
                assert w>=F(1,16*M) and v<=4*w
                assert a>=2*r
                counts['prefix_density_instances']+=1

# Exact dynamic programming with an ordered-word hash: not a histogram statistic.
# h = binary value of the suffix modulo 7 retains order information.
def dp(t,a,d,tau,reference):
    tab=transition(a,d,tau,reference)
    mass={(2,0,0):F(1)}
    for _ in range(t):
        nxt=defaultdict(F)
        for (state,n,h),p in mass.items():
            for state1,q,b in tab[state]:
                if q:nxt[(state1,n+b,(2*h+b)%7)]+=p*q
        mass=nxt
    assert sum(mass.values())==1
    return mass

min_acc=None
for M,k,t in ((256,32,32),(320,36,40),(512,46,46),(512,46,64),(512,64,64),(1024,64,80)):
    assert k*k>=4*M and k<=t<=M//8
    for a in (F(k,32*t),F(3*k,64*t),F(k,16*t)):
        d,tau,pi=family(M,k,a)
        R=dp(t,a,d,tau,True)
        A=dp(t,a,d,tau,False)
        ref_g=sum(p for (st,n,h),p in R.items() if st==0 and n<=k)
        e_l=sum(n*p for (st,n,h),p in R.items())
        tail=sum(p for (st,n,h),p in R.items() if n>k)
        terminal=sum(p for (st,n,h),p in R.items() if st==0)
        assert e_l<=a*t<=F(k,16)
        assert tail<=F(1,16) and terminal>=(1-a)**2>=F(9,16)
        assert ref_g>=F(1,2)
        if min_acc is None or ref_g<min_acc:min_acc=ref_g
        # Test nonnegative full-ordered-word functionals and randomized decoding.
        r=F(1,2*M)
        for mode in ('zero','one','half','ordered','randomized_ordered','near_a'):
            def loss(h,target):
                q=F(h,6)
                if mode=='zero':return target
                if mode=='one':return 1-target
                if mode=='half':return abs(F(1,2)-target)
                if mode=='ordered':return abs(q-target)
                if mode=='randomized_ordered':return F(2,5)*abs(q-target)+F(3,5)*abs((1-q)-target)
                return abs(a+F(h,128)-target)
            lerr=sum(p*loss(h,a) for (st,n,h),p in A.items() if st==0)
            rerr=sum(p*loss(h,a) for (st,n,h),p in R.items() if st==0 and n<=k)
            nloss=sum(p*loss(h,r) for (st,n,h),p in R.items() if st==0 and n<=k)
            assert rerr<=4*lerr
            assert nloss>=a/4-4*lerr
            counts['ordered_functional_tests']+=1
        records.append({'M':M,'k':k,'t':t,'a':str(a),'acceptance':str(ref_g)})
        counts['exact_DP_cases']+=1

# Pathwise reference/actual ratios on structurally independent small tests.
# These do NOT purport to satisfy the theorem's finite M,k domain.
# They exhaust ordered suffixes to verify the mechanism, including rejection.
for k in (2,3,5):
    M=64;d=F(1,k);tau=F(1,4*M);a=F(1,8)
    def visit(bits,state,pr,pa,n,n01):
        h=len(bits)
        assert pa==pr*(1-d)**n01
        if h:
            if state==0 and n<=k:
                assert pa>=pr/4
                original=[1,1,0]+[0]*h
                changed=[1,1,0]+bits
                assert changed[-2:]==original[-2:]==[0,0]
                assert sum(x!=y for x,y in zip(original,changed))==n<=k
                assert changed[:3]==original[:3]
                counts['exhaustive_accepted_ordered_paths']+=1
        if h==14:return
        for b in (0,1):
            if state==1 and b==1:continue
            qr=([a,F(0),d,1-tau][state] if b else 1-[a,F(0),d,1-tau][state])
            qa=([a,d,d,1-tau][state] if b else 1-[a,d,d,1-tau][state])
            if qr:visit(bits+[b],2*(state%2)+b,pr*qr,pa*qa,n+b,n01+(state==1))
    visit([],2,F(1),F(1),0,0)

for k in range(2,300):
    assert F(k-1,k)**k>=F(1,4)
    counts['quarter_product_instances']+=1

# Coefficients are verified by exact arithmetic; logs are proved analytically.
assert F(1,4)*F(3,64)*F(1,8)==F(3,2048)
assert 4*4*2==32
assert F(32)*F(2048,3)==F(65536,3)
assert F(8193)*5*F(6)+2600+16<2**18 # sqrt(32)<6, a safe independent check
assert 4*600192<2**22

out={'status':'PASS_TESTED_INSTANCES_ONLY','independence':'No author checker imported or read; independently constructed transition matrices, full-word order-hash DP and ordered-path enumeration.','proof_sha256':EXPECTED,'arithmetic':'fractions.Fraction exact except display-only conversion','counts':dict(counts),'minimum_reference_acceptance':str(min_acc),'minimum_reference_acceptance_display':float(min_acc),'exact_DP_records':records,'limitations':'Finite diagnostics corroborate only tested instances; universal inequalities and integration/asymptotic arguments require the accompanying mathematical review.'}
result=Path(__file__).with_suffix('.json')
result.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'counts':out['counts'],'minimum_reference_acceptance_display':out['minimum_reference_acceptance_display']},indent=2))
