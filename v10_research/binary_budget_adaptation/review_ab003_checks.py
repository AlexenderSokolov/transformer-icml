"""Independent exact-rational finite diagnostics for AB003, not a universal proof."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib,json,random
ROOT=Path(__file__).resolve().parent
rng=random.Random(202611021202)
counts={'relaxed_count_configs':0,'critical_probability_checks':0,'active_configs':0,
        'inactive_configs':0,'threshold_bias_floor_checks':0,'finite_M_constants':0,'scaled_envelope_configs':0}
minimum_margin=None;minimum_case=None

def check(M,k,J,C,Jp,Cp,L=1):
    global minimum_margin,minimum_case
    B=12*L*(isqrt(M)+(isqrt(M)**2!=M));d=6*k
    assert 0<=C<=J<=M and 0<=Cp<=Jp<=M
    assert abs(Cp-C)<=d and abs(Jp-J)<=d and 2*d<=B
    pp=F(Cp,Jp) if Cp>B else F(0)
    p=F(C,J) if J else F(0)
    A=36*k
    qs={F(0),F(1),p,pp,min(F(1),F(A,J+2))}
    threshold=F(3*B,J) if J else None
    if threshold is not None and threshold<=1: qs.add(threshold)
    # Exact breakpoints suffice for a piecewise-linear expression, apart from the
    # threshold's right limit, checked separately by dropping that bias at equality.
    for q in qs:
        E=abs(p-q) if J else F(0)
        weighted=min(q,F(A,J+2))
        bias=q if q and (J*q<=3*B) else F(0)
        lhs=abs(pp-q);rhs=5*E+4*weighted+bias
        assert lhs<=rhs,(M,k,J,C,Jp,Cp,q,lhs,rhs)
        if threshold is not None and q==threshold:
            assert lhs<=5*E+4*weighted,('threshold right limit',M,k,J,C,Jp,Cp,q)
        counts['critical_probability_checks']+=1
        margin=rhs-lhs
        if minimum_margin is None or margin<minimum_margin:
            minimum_margin=margin;minimum_case=(M,k,J,C,Jp,Cp,str(q))
        if q:
            w=(3*B*q.denominator)//q.numerator+1
            assert q*w<=3*B+q
            counts['threshold_bias_floor_checks']+=1
    counts['relaxed_count_configs']+=1
    if L>1: counts['scaled_envelope_configs']+=1
    counts['active_configs' if Cp>B else 'inactive_configs']+=1

for M in (64,65,81,100,121,144,145,256,257,1024,4096,65536):
    root=isqrt(M);B=12*(root+(root*root!=M))
    for k in sorted({0,1,root//2,root}):
        d=6*k
        cases={(0,0,0,0),(M,0,M,0),(M,M,M,M)}
        for J in sorted({0,1,min(M,B//2),min(M,B),min(M,B+1),M}):
            for C in sorted({0,J,min(J,B//2),min(J,B),min(J,B+1)}):
                for dj in sorted({-d,0,d}):
                    Jp=max(0,min(M,J+dj))
                    for dc in sorted({-d,0,d}):
                        Cp=max(0,min(Jp,C+dc));cases.add((J,C,Jp,Cp))
        for _ in range(350):
            J=rng.randrange(M+1);C=rng.randrange(J+1)
            Jp=max(0,min(M,J+rng.randint(-d,d)))
            Cp=max(0,min(Jp,C+rng.randint(-d,d)))
            cases.add((J,C,Jp,Cp))
        for J,C,Jp,Cp in cases: check(M,k,J,C,Jp,Cp)

# Scaled-envelope version: same deterministic inequality with B_L and k up to L sqrt(M).
for M in (64,257,4096,65536):
    for L in (2,3,7,37):
        for k in sorted({0,1,min(M,L*isqrt(M)),min(M,max(1,L*isqrt(M)//2))}):
            d=6*k
            for _ in range(120):
                J=rng.randrange(M+1);C=rng.randrange(J+1)
                Jp=max(0,min(M,J+rng.randint(-d,d)))
                Cp=max(0,min(Jp,C+rng.randint(-d,d)))
                check(M,k,J,C,Jp,Cp,L)
            B=12*L*(isqrt(M)+(isqrt(M)**2!=M))
            assert (64*(3*B+1))**2*M<=(2600*L)**2*(M+1)**2
        assert ((2**18-2600)*L-16)**2>(5*8193)**2*32
assert F(8,3)/F(3,1024)==F(8192,9)

# Exactly squared comparisons avoid floating square-root error in the finite constants.
for M in range(64,100001):
    root=isqrt(M);B=12*(root+(root*root!=M))
    assert 4*B*B<=729*M
    assert (64*(3*B+1))**2*M<=2600**2*(M+1)**2
    counts['finite_M_constants']+=1
assert (2**18-2616)**2>(5*8193)**2*32
assert 4*16672*36==2400768<2**22
assert 256*36+16==9232
sources=[ROOT/'AB003_small_budget_hard_threshold.md',ROOT.parent/'binary_source_corruption/SC003_theorem.md',
ROOT.parent/'binary_all_start/BIF001_binary_all_initializations_frontier_v1.md',
ROOT.parent/'binary_arbitrary/BAI003_uniform_absorbing_binary_upper_v2.md',ROOT/'AB001_joint_blindness_obstruction.md']
result={'status':'PASS','arithmetic':'exact integers and Fraction throughout','counts':counts,
'minimum_tested_pathwise_margin':str(minimum_margin),'minimum_margin_case':minimum_case,
'source_sha256':{str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
'scope':'New pathwise inequality, count boundary cases, fixed-row floor accounting, and finite constants checked on stated cases; inherited stochastic interfaces separately audited in the full review. No formal verification claim.'}
(ROOT/'review_ab003_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
