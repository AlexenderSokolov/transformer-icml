#!/usr/bin/env python3
"""Independent SB001 v2 corroboration; exact rational finite tests, not a proof."""
import itertools, math, hashlib, json, pathlib, random
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCE='v10_research/score_precision/SB001_loglog_effective_score_budget_v2.md'
EXPECTED='d10086be4d358e322872daffad4dd10572588d6dcffaecbffefc409df6a217b7'
assert hashlib.sha256((ROOT/SOURCE).read_bytes()).hexdigest()==EXPECTED
counts={}
def tv(a,b): return sum(abs(x-y) for x,y in zip(a,b))/2
def run_history(x,K,Q,k):
    M=len(x)-2; pair=x[-2:]; C=[0]*K; bank=[0]*(K**3); den=0
    for i in range(2,len(x)):
        p=x[i-2:i]; w=k if p==pair else 1; den+=w
        bank[(p[0]*K+p[1])*K+x[i]]+=w
        if p==pair:C[x[i]]+=1
    J=sum(C)
    z=[Q*a//den for a in bank] # full bank, not selected-only computation
    zc=z[(pair[0]*K+pair[1])*K:(pair[0]*K+pair[1]+1)*K]
    s=sum(zc); p=[F(a,s) for a in zc] if s else [F(1,K)]*K
    out=[F((Q*a)//1,Q) for a in p[:-1]];out +=[1-sum(out)]
    q=[F(a+1,J+K) for a in C]
    assert sum(out)==1 and min(out)>=0
    A=F(K*(K+1)*M,k*Q)
    rhs=F(K,J+K)+min(1,A/(J+K))+F(2*K-1,Q)
    assert tv(out,q)<=rhs
    if J:
        r=F(k*J,M+(k-1)*J)
        assert tv(p,[F(a,J) for a in C])<=min(1,F(K,Q)/r)
        assert min(1,F(K,Q)/r)<=F(K,Q)+min(1,A/(J+K))
    return s==0,J==0
n=zero=empty=0
for K,maxN in [(2,9),(3,7)]:
    for N in range(3,maxN+1):
        for x in itertools.product(range(K),repeat=N):
            for Q,k in itertools.product([1,2,16],[1,2,7]):
                zz,ee=run_history(x,K,Q,k);n+=1;zero+=zz;empty+=ee
counts['exact_history_tests']={'cases':n,'all_zero_selected_blocks':zero,'zero_match_histories':empty}
# Integer operating point, including the first allowed M and bitlength jumps.
ms=set(range(64,10000))|{2**j+d for j in range(7,1000) for d in [-2,-1,0,1,2]}
for M in ms:
    L=(M+1).bit_length(); h=max(4,(L+1)//2);Q=2**h
    assert M+1<=Q*Q<=4*(M+1)
    assert Q<=2**L-1
counts['integer_schedule_tests']=len(ms)
def psi(x):return 1 if x>=1 else x*(1-math.log(x)) if x else 0
n=0
for K in [2,3,5,10,100]:
    D=K**5*(K+1)
    for z in [10**(j/4) for j in range(-24,101)]:
        assert psi(D/z)<=D*(1+math.log1p(z))/z*(1+1e-12)
        for t in [1,1.01,2,4,16,100,10000]:
            G=1+math.log1p(z/t)
            # Worst envelope used in residual proof.
            eps=min(1,math.e*math.exp(-t/4))
            assert eps*psi(2*D/z)<=10*D*G/z*(1+1e-12)
            stat=2*K**3*(K+1)*(17+math.log1p(480*z/(K*(K+1)*t)))/z
            assert stat<=48*K**3*(K+1)*G/z*(1+1e-12)
            n+=1
counts['scalar_envelope_tests']=n
n=0
for x in [10**(j/8) for j in range(-128,193)]:
    f=1+math.log1p(x);k=math.ceil(f)
    assert (1+math.log1p(k*x))/k<=2+1e-12
    for cp in [.01,.3,1,2,100]:
        # Q^2/M <= c_+^2 yields min(Q/t,M/Q)>=x/max(1,c_+^2).
        a=1/(8*max(1,cp**2))
        assert math.log1p(a*x)>=min(1,a)*math.log1p(x)*(1-1e-12)
        n+=1
counts['mixing_choice_and_log_comparison_tests']=n
n=0
for D,r,k in itertools.product([1,2,27,64],[1,3,5],[1,2,7,100,100000]):
    H=3**(2*r);u=r*math.sqrt(40*D*H);N=math.ceil(8*k*u+4)+1
    assert N<=k*(8*u+6)*(1+1e-15)
    # Logarithmic comparison avoids enormous powers.
    left=math.log(H)+math.log(2+4*k*r)+D*math.log(N)
    right=math.log(H)+math.log(2+4*r)+D*math.log(8*u+6)+(D+1)*math.log(k)
    assert left<=right+1e-10;n+=1
counts['BA_constant_tests']=n
out={'status':'PASS','source_sha256':EXPECTED,'checks':counts,'limits':'Independent finite corroboration, not formal verification, not emitted-network execution, not a statistical theorem replacement.'}
p=ROOT/'reviews/SB001_independent_checks_v2.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
