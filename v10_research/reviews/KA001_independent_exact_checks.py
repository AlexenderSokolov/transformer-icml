#!/usr/bin/env python3
"""KA001 independent exact-rational diagnostics; no author checker imported/read.
Finite checks corroborate calculations; they do not formally verify the theorem.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
from collections import Counter
import hashlib, json, datetime, difflib

ROOT=Path(__file__).resolve().parents[1]
TARGET='binary_certificate_adaptation_phase/KA001_certificate_phase_partial.md'
EXPECTED='5cf1f9ba5dca0e5cb7dd2a703bca163f87e46f5eb16ddf5563837d873e9072e7'
counts=Counter()

def check(condition, category):
    assert condition, category
    counts[category]+=1

def sha(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
check(sha(TARGET)==EXPECTED,'candidate_hash')
check((ROOT/TARGET).read_bytes()==(ROOT/'reviews/KA001_audit_snapshots/KA001_received.md').read_bytes(),'snapshot_identity')
accepted={}
for unit in ('BK002','AB003','SC003','BT002','SC002','IU001','AU001'):
    receipt=json.loads((ROOT/f'intake/{unit}_acceptance.json').read_text())
    check(sha(receipt['proof'])==receipt['sha256'],'accepted_proof_hash')
    for p,h in receipt.get('component_proofs',{}).items(): check(sha(p)==h,'accepted_component_hash')
    if 'review_sha256' in receipt: check(sha(receipt['review'])==receipt['review_sha256'],'accepted_review_hash')
    accepted[unit]={'proof':receipt['proof'],'sha256':receipt['sha256'],'receipt_sha256':sha(f'intake/{unit}_acceptance.json')}

# Exact rational interval for logarithms: positive-term atanh series after
# binary range reduction. The remainder is dominated by a geometric series.
def ln_unit(x,n=18):
    y=(x-1)/(x+1); y2=y*y
    total=F(0); power=y
    for j in range(n):
        total+=2*power/(2*j+1); power*=y2
    return total, total+2*power/((2*n+1)*(1-y2))
LN2=ln_unit(F(2))
def ln_bounds(x):
    x=F(x)
    assert x>0
    if x<1:
        lo,hi=ln_bounds(1/x); return -hi,-lo
    power=0
    while x>=2: x/=2; power+=1
    lo,hi=ln_unit(x)
    return lo+power*LN2[0],hi+power*LN2[1]

# Finite-band exact integer square-root rounding, including nonsquare beta.
rounding_cases=set()
def rounding(M,beta):
    beta=F(beta); lo=F(256,M*M); hi=F(1,16*M)
    check(lo<=beta<=hi,'input_finite_band')
    k=isqrt(beta.denominator//beta.numerator); T=M//8
    check(k*k*beta<=1<(k+1)*(k+1)*beta,'floor_inverse_sqrt')
    check(16*k*k*beta>=9,'k_delta_at_least_three_quarters_squared')
    check(k*k>=4*M and 1<=k<=T,'BK002_integer_domain')
    check(16*k<=M,'k_at_most_M_over_16')
    check(beta<=F(1,k*k) and beta<=F(1,M),'actual_beta_class_inclusion')
    check(beta>=F(1,M*M),'binary_cutoff_is_sqrt_beta')
    check(T+1>k and 2*T>k,'positive_log_arguments')
    rounding_cases.add((M,beta,k))
    return k

for M in range(4096,12289):
    lo,hi=F(256,M*M),F(1,16*M)
    for weight in (F(0),F(1,7),F(1,2),F(6,7),F(1)):
        rounding(M,lo+(hi-lo)*weight)
# At selected horizons, every intersecting reciprocal-square floor cell is
# tested at its boundaries/interior, with lower cell endpoint excluded.
for M in [4096,4097,4103,8191,8192,10000,16391,65537]:
    lo,hi=F(256,M*M),F(1,16*M)
    kmax=isqrt(lo.denominator//lo.numerator)
    kmin=isqrt(hi.denominator//hi.numerator)
    for k in range(kmin,kmax+1):
        left=max(lo,F(1,(k+1)*(k+1)))
        right=min(hi,F(1,k*k))
        if left<=right:
            if left>F(1,(k+1)*(k+1)): rounding(M,left)
            if right>F(1,(k+1)*(k+1)): rounding(M,right)
            if left<right: rounding(M,(left+right)/2)

# Rebuild the actual pair transition kernel from successor-bit probabilities.
states=[(0,0),(0,1),(1,0),(1,1)]
def matrix(theta):
    P=[[F(0) for j in range(4)] for i in range(4)]
    for i,(_,b) in enumerate(states):
        for bit in (0,1): P[i][states.index((b,bit))]=theta[i] if bit else 1-theta[i]
    return P

def square(P): return [[sum(P[i][r]*P[r][j] for r in range(4)) for j in range(4)] for i in range(4)]

witness_cases=0; nonsquare_witness_cases=0
sampled=sorted(rounding_cases,key=lambda x:(x[0],x[1]))
selected=sampled[::max(1,len(sampled)//120)] + sampled[:8] + sampled[-8:]
for M,beta,k in selected:
    T=M//8; delta=F(1,k); e=1-delta; tau=F(1,4*M)
    amin=F(k,32*T)
    for a in (amin,(amin+F(1,16))/2,F(1,16)):
        x=1/(e/a+2+delta/tau); Pi=[x*e/a,x,x,x*delta/tau]
        P=matrix([a,delta,delta,1-tau]); P2=square(P)
        check(sum(Pi)==1 and min(Pi)>0,'stationary_probability')
        for j in range(4): check(sum(Pi[i]*P[i][j] for i in range(4))==Pi[j],'stationarity_equations')
        for i in range(4):
            for j in range(4):
                check(P2[i][j]>=F(1,k*k)*Pi[j],'witness_certificate_all_entries')
                check(P2[i][j]>=beta*Pi[j],'actual_supplied_certificate_all_entries')
        check(Pi[3]>=F(1,3),'witness_11_stationary_mass')
        check(a>=delta,'a_at_least_reference_delta')
        witness_cases+=1; nonsquare_witness_cases+=beta!=F(1,k*k)
    r=F(1,2*M); T1=[[1-r,r],[r,1-r]]
    Pstar=matrix([r,1-r,r,1-r]); Pstar2=square(Pstar)
    Pistar=[T1[u][v]/2 for u,v in states]
    for i in range(4):
        for j in range(4):
            check(Pstar2[i][j]>=F(1,M)*Pistar[j]>=beta*Pistar[j],'null_certificate_all_entries')

# Proof constants: exact bounds avoid uncertified floating-point logarithms.
check(8192**2*32<65536**2,'clean_constant_squared')
check(48*(17+ln_bounds(F(80))[1])+960<4096,'generic_corruption_constant_log_interval')
check(F(7,3)<1+1+F(1,2),'log_7_over_3_less_than_one_via_exp_series')
check(F(32)*2048/3==F(65536,3),'constrained_risk_ratio_constant')

# Weak band comparison: enough to use the worst admissible cutoff D/M;
# D=1 is equality. Rational log intervals certify all strict scalar tests.
for D in (F(1),F(5,4),F(2),F(7,2),F(10),F(100),F(10**6)):
    for z in (F(1),F(5,4),F(2),F(16),F(96),F(97),F(1000),F(10**9)):
        if D==1:
            check(True,'weak_scalar_equal_D_one'); continue
        lz=ln_bounds(1+z); ld=ln_bounds(D); lzd=ln_bounds(1+z/D)
        check(1+lz[1]<=(1+ld[0])*(1+lzd[0]),'weak_band_log_comparison')
# Universal corruption scalar: Psi(96 k/(M+1))<=96 F0.
for M in (64,65,95,96,97,256,4096,4097,10**6):
    for k in sorted({1,2,max(1,M//96),max(1,M//8),M//2,M}):
        v=F(96*k,M+1); F0lo=F(k,M)*(1+ln_bounds(1+F(M,k))[0])
        psi_hi=F(1) if v>=1 else v*(1+ln_bounds(1/v)[1])
        check(psi_hi<=96*F0lo,'universal_Psi_comparison')

# Strong scalar log(1+u)<=u at rational exact u; c/sqrt M is exact
# for square horizons. Include c tiny/large and both beta0 branches.
for n in (8,9,16,64,1000,10**6):
    M=n*n
    for c in (F(1,1000),F(1,10),F(1),F(2),F(10)):
        if c>n: continue
        for beta in {c/n,(c/n+1)/2,F(1)}:
            beta0=max(beta,F(1,M))
            for k in {1,2,n,M//2,M}:
                u=1/(k*beta0)
                loghi=ln_bounds(1+u)[1]
                check(loghi<=u,'strong_log_bound')
                check(F(1,M)/beta0<=F(1,n)/c,'strong_residual_absorption')
                check(F(k,M)*(1+loghi)<=F(k,M)+F(1,n)/c,'strong_Fgen_bound')

# Exact scales for representative strictly intermediate curves. Ratios shown
# use rational logarithm intervals; these are illustrations, not limit proofs.
curves=[]
for name in ('power_three_halves','near_strong_boundary','near_weak_boundary'):
    for n in (16,32,64,128):
        if name=='power_three_halves': M=2**(4*n); beta=F(1,2**(6*n))
        elif name=='near_strong_boundary': M=2**(2*n); beta=F(1,M*n*n)
        else: M=2**(2*n); beta=F(n*n,M*M)
        k=rounding(M,beta); T=M//8
        lp=ln_bounds(F(T+1,k)); le=ln_bounds(F(2*T,k))
        # M is square on all examples, hence sqrt(M)/k exact.
        check(isqrt(M)**2==M,'curve_square_horizon')
        ratio_hi=F(65536,3)*F(isqrt(M),k)*le[1]/lp[0]
        curves.append({'curve':name,'n':n,'M':str(M),'beta':str(beta),'k':str(k),
                       'M_beta':str(M*beta),'M2_beta':str(M*M*beta),
                       'sqrtM_over_k':str(F(isqrt(M),k)),
                       'penalty_positive_ratio_upper_C_equals_1_approx':float(ratio_hi),
                       'positive_over_2epsilon_lower_approx':float(F(3,4096)*lp[0])})

check(sha(TARGET)==EXPECTED,'candidate_hash_end')
output={'unit':'KA001','status':'PASS_TESTED_INSTANCES_ONLY',
        'reviewed_candidate_sha256':EXPECTED,'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'independence':'Reviewer-written; no author diagnostic code imported or read before execution.',
        'arithmetic':'All assertions exact Fraction/integer arithmetic, including certified rational log intervals; approximate values only for illustrative curve display.',
        'counts':dict(counts),'total_assertions':sum(counts.values()),
        'distinct_finite_band_cases':len(rounding_cases),'witness_cases':witness_cases,
        'witness_cases_at_nonsquare_supplied_beta':nonsquare_witness_cases,
        'accepted_dependencies':accepted,'illustrative_curves':curves,
        'limitations':'Finite corroboration, not formal verification or a proof of asymptotic limits; proof, quantifiers, source-independent kernel, arbitrary-start transfer and partial scope are reviewed separately.'}
out=ROOT/'reviews/KA001_independent_exact_checks.json'; out.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':output['status'],'assertions':output['total_assertions'],'distinct_finite_band_cases':len(rounding_cases),'witness_cases':witness_cases,'nonsquare_witness_cases':nonsquare_witness_cases,'counts':dict(counts)},indent=2))
