"""Finite corroboration only; analytic bounds are in FULL_REVIEW.md. Stdlib only."""
from fractions import Fraction as F
from math import comb, exp, log, sqrt
from pathlib import Path
import json

cases=0
for p in [F(1,100), F(1,10), F(1,2), F(9,10), F(99,100)]:
    cap=(p/24)**2
    for alpha in [F(0),cap/100,cap/2,cap]:
        for q0 in [F(0),alpha/2,alpha]:
            for q1 in [p-alpha,p, min(F(1),p+alpha)]:
                c=q1*(1-q0); w=q0*(1-q1); e=1-c-w
                assert c>=p/2 and w<=alpha and e>=0
                for n in [1,2,3,7,16,31]:
                    abstain=F(0); wrong=F(0)
                    # Worst tie resolution: count all tied outcomes as errors.
                    for z in range(n+1):
                        for good in range(n-z+1):
                            mass=comb(n,z)*comb(n-z,good)*w**z*c**good*e**(n-z-good)
                            h=z+good
                            if h<p*n/4: abstain+=mass
                            elif z>=good: wrong+=mass
                    assert float(abstain)<=exp(-float(n*p*p/8))+1e-14
                    if alpha:
                        assert 8*3*alpha/p<=sqrt(float(alpha))+1e-15
                        assert float(wrong)<=exp(float(p*n/16)*log(float(alpha)))+1e-14
                    else: assert wrong==0
                    cases+=1
maj=0
for a in [F(1,16),F(1,100),F(1,10**6)]:
    for n in range(1,65):
        tail=sum((F(comb(n,k))*a**k*(1-a)**(n-k) for k in range((n+1)//2,n+1)), F(0))
        assert float(tail)<=float(a)**(n/4)+1e-14
        maj+=1
# Evaluate resource inequalities in log coordinates: no underflow for tiny radius.
lengths=0
for logM in [log(64),100,10000,1e9]:
    L=1+logM-log(2) # conservative asymptotic proxy solely for algebra test
    for p in [.01,.1,.5,.99]:
        for logInvAlpha in [log((24/p)**2),100,10000,1e12]:
            n=max(1, __import__('math').ceil(8/p**2*log(2**20*L)), __import__('math').ceil(8/p*logM/logInvAlpha))
            assert log(2**20*L)-n*p*p/8<=1e-8
            assert .5*logM-p*n/16*logInvAlpha<=1e-7
            lengths+=1
report={'status':'PASS_FINITE_CORROBORATION_ONLY','partial_block_tail_cases':cases,'disjoint_majority_cases':maj,'log_domain_length_cases':lengths,'uses_exact_rational_event_probabilities':True,'exponential_comparisons':'floating point with 1e-14 additive tolerance; not proof','scope':'No source statistical theorem checked by this program.'}
Path(__file__).with_name('checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
