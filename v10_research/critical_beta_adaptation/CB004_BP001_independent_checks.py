#!/usr/bin/env python3
"""Fresh reviewer diagnostics, independent of the author/prior diagnostic code.

All arithmetic checks, including finite exponential-tail comparisons, use exact
fractions. These finite tests corroborate, but do not establish, the theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from collections import defaultdict, Counter
from pathlib import Path
import hashlib, json, random, time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EXPECTED = {
    'critical_beta_adaptation/CB004_stationary_critical_adaptation.md': 'a322c2fe08b76cf84f587b91e4ab504e2e02468e8c1a617fd7b868e14f643155',
    'critical_beta_adaptation/balance_probe/BP001_stationary_weighted_balance.md': '22b60eedf31f1e990e990a8b64ad733a1a3acc9723a421fdc6d677866c771271',
    'binary_upper/BU001_weighted_return_upper_v2.md': '2dc9cf9d13faa6cfa15fffd5ec83a67326ccc95eb6a63291c7b2349136b166f5',
    'binary_source_corruption/SC003_theorem.md': '4235fc6b9de9d04368354d22f15774d66965ca572f21f197e456537e9bcba837',
    'binary_erasure_transport/BT002_entropy_bridge_lower.md': '40d5345657b8f255cd1cef496fb84090aae18a6cd6bc7c083daa09c2ce913562',
    'binary_erasure_transport/BT002_scalar_completion.md': '4be9d338e0d3e6b840441f4356e77b71db4da9f1208d74bd85f4790539ba9026',
}
counts = Counter()
def check(cond, kind):
    assert cond, kind
    counts[kind] += 1

def solve(A, b):
    A = [[F(x) for x in row] + [F(rhs)] for row, rhs in zip(A,b)]
    n = len(b)
    for c in range(n):
        pivot = next((r for r in range(c,n) if A[r][c]), None)
        if pivot is None:
            return None
        A[c], A[pivot] = A[pivot], A[c]
        z = A[c][c]
        A[c] = [x/z for x in A[c]]
        for r in range(n):
            if r != c:
                z = A[r][c]
                A[r] = [x-z*y for x,y in zip(A[r],A[c])]
    return [A[r][-1] for r in range(n)]

def chain(a,b,e,t):
    return [[1-a,a,F(0),F(0)], [F(0),F(0),1-b,b],
            [e,1-e,F(0),F(0)], [F(0),F(0),t,1-t]]

def stationary(P):
    d = len(P)
    A = [[P[i][j] - (i==j) for i in range(d)] for j in range(d-1)]
    return solve(A + [[1]*d], [0]*(d-1)+[1])

def moments(P, s, rmax=6):
    d=len(P); other=[i for i in range(d) if i!=s]
    A=[[F(i==j)-P[i][j] for j in other] for i in other]
    ms = [[F(0)]*d]
    returns=[F(0)]
    for r in range(1,rmax+1):
        rhs=[F(1)+sum(F(comb(r,j))*sum(P[i][v]*ms[j][v] for v in other)
                       for j in range(1,r)) for i in other]
        vals=solve(A,rhs)
        assert vals is not None
        row=[F(0)]*d
        for i,val in zip(other,vals): row[i]=val
        ms.append(row)
        returns.append(F(1)+sum(F(comb(r,j))*sum(P[s][v]*ms[j][v] for v in other)
                                 for j in range(1,r+1)))
    return ms,returns

def exp_upper(x):
    """Exact rational upper enclosure for exp(x), x>=0, by Taylor + tail."""
    assert x>=0
    N=max(40,2*(x.numerator//x.denominator+1))
    term=F(1); total=term
    for j in range(1,N+1):
        term*=x/j; total+=term
    nxt=term*x/(N+1)
    return total+nxt/(1-x/F(N+2))

def check_return_tails(P, label):
    pi=stationary(P)
    assert pi and all(x>0 for x in pi)
    d=len(P)
    horizons={1,2,3,7,16,32,64,128}
    for s,p in enumerate(pi):
        ms,_=moments(P,s,2); hb=max(max(ms[1]),1/p)
        for start in range(d):
            dist={(start,0):F(1)}
            for l in range(1,129):
                nxt=defaultdict(F)
                for (i,c),mass in dist.items():
                    for j,prob in enumerate(P[i]):
                        if prob: nxt[j,c+(i==s)]+=mass*prob
                dist=nxt
                if l not in horizons: continue
                low=sum(v for (_,c),v in dist.items() if c<F(l)*p/16)
                high=sum(v for (_,c),v in dist.items() if c>4*l*p+1)
                # Multiplying by an UPPER enclosure of exp gives a sufficient
                # exact verification, without floating transcendental calls.
                check(low*exp_upper(F(l)/(8*hb))<=2,'exact_lower_visit_tail')
                check(high*exp_upper(F(l)/(2*hb))<=1,'exact_upper_visit_tail')

def summaries(bits):
    M=len(bits)-2; n=M//2; J=[0]*4; J1=[0]*4; C=[0]*4
    for i in range(M):
        s=2*bits[i]+bits[i+1]; J[s]+=1; J1[s]+=(i<n)
        C[s]+=(bits[i+2]==1-bits[i])
    return J,J1,C,2*bits[-2]+bits[-1]

def gate_checks(J,J1,C,Jp,J1p,Cp,k,kind):
    d=6*k; G=Jp>0 and 512*J1p>=Jp; H=1024*J1>=J
    B=J>0 and 256*J1<J
    check(not (G and not H) or J<1026*d,kind+'_active_switch')
    check(not ((not G) and (not B) and J>0) or J<513*d,
          kind+'_inactive_switch')
    if G and H and J>0:
        check(abs(F(Cp,Jp)-F(C,J))<=F(8*d,J+1),kind+'_normalization')
    for q in (F(0),F(1,3),F(1)):
        out=F(Cp,Jp) if G else F(0)
        E=abs(F(C,J)-q) if J else F(0)
        bound=E+F(8*d,J+1)*H+q*B+(J<6156*k+1)+(J<3078*k+1)
        check(abs(out-q)<=bound,kind+'_whole_reduction')

def main():
    started=time.time()
    for path,h in EXPECTED.items():
        check(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h,'proof_hash')
    for unit,path in [('BU001','binary_upper/BU001_weighted_return_upper_v2.md'),
                      ('SC003','binary_source_corruption/SC003_theorem.md'),
                      ('BT002','binary_erasure_transport/BT002_entropy_bridge_lower.md')]:
        receipt=json.loads((ROOT/'intake'/f'{unit}_acceptance.json').read_text())
        check(receipt['sha256']==EXPECTED[path] and receipt['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW','accepted_receipt')
    swap=[0,2,1,3]; eligible=0; full=0; singleton=0
    max_h=F(0); max_hbar=F(0)
    for a,b,e,t in product([F(j,4) for j in range(5)],repeat=4):
        P=chain(a,b,e,t); pi=stationary(P)
        if pi is None or min(pi)<0: continue
        P2=[[sum(P[i][v]*P[v][j] for v in range(4)) for j in range(4)] for i in range(4)]
        beta=min(P2[i][j]/pi[j] for i in range(4) for j in range(4) if pi[j])
        if beta<=0: continue
        eligible+=1
        support=[s for s in range(4) if pi[s]]
        check(len(support)==4 or (len(support)==1 and support[0] in (0,3)), 'positive_certificate_support')
        if len(support)==1:
            singleton+=1; s=support[0]
            check(P[s][s]==1 and (a if s==0 else t)==0,'singleton_zero_weight')
            continue
        full+=1; gamma=[a,F(1),F(1),t]
        for i in range(4):
            for j in range(4):
                check(pi[i]*P[i][j]==pi[swap[j]]*P[swap[j]][swap[i]],'reversed_pair_flux')
            check(pi[i]==pi[swap[i]] and gamma[i]==gamma[swap[i]],'reversal_mass_weight')
        for s,p in enumerate(pi):
            ms,rets=moments(P,s)
            H=max(ms[1]); hb=max(H,1/p)
            check(rets[1]==1/p,'exact_kac')
            check(1/p<=1+H,'positive_return_mean')
            sh=beta*(p*gamma[s]*H)**2
            shb=beta*(p*gamma[s]*hb)**2
            max_h=max(max_h,sh); max_hbar=max(max_hbar,shb)
            check(sh<=25,'weighted_hitting_scale')
            check(shb<=36,'weighted_hbar_scale')
            for r in range(1,7):
                for i in range(4):
                    check(ms[r][i]<=factorial(r)*hb**(r-1)*ms[1][i],'ordinary_moment_bound')
                check(rets[r]<=factorial(r)*hb**(r-1)*rets[1],'positive_return_moment_bound')
    # General finite irreducible tests include non-binary-chain kernels.
    generic=[
      [[F(1,16),F(3,16),F(1,4),F(1,2)] for _ in range(4)],
      [[F(int(j==(i+1)%4)) for j in range(4)] for i in range(4)],
      chain(F(1,8),F(1,2),F(1,4),F(3,4)),
      chain(F(1,2),F(3,4),F(1,2),F(1,8)),
    ]
    for z,P in enumerate(generic): check_return_tails(P,z)
    # Exact window identities on every binary word, no stochastic assumptions.
    for M in range(1,11):
        n=M//2; m=M-n
        for bits in product(range(2),repeat=M+2):
            J,J1,C,s=summaries(bits)
            Y=[2*bits[j]+bits[j+1] for j in range(M+1)]
            Z=[swap[y] for y in reversed(Y)]
            for u in range(4):
                check(J1[u]==sum(z==swap[u] for z in Z[m+1:M+1]),'exact_late_shifted_window')
                check(J[u]-J1[u]==sum(z==swap[u] for z in Z[1:m+1]),'exact_early_shifted_window')
    # All words and every edit mask at small horizons, including adjacent edits.
    for M in range(1,8):
        for bits in product(range(2),repeat=M+2):
            J,J1,C,s=summaries(bits)
            for mask in range(1<<M):
                edited=tuple(b^((mask>>i)&1) if i<M else b for i,b in enumerate(bits))
                Jp,J1p,Cp,sp=summaries(edited); k=mask.bit_count(); d=6*k
                check(s==sp and abs(Jp[s]-J[s])<=d and abs(J1p[s]-J1[s])<=d and abs(Cp[s]-C[s])<=d,'actual_hamming_counts')
                gate_checks(J[s],J1[s],C[s],Jp[s],J1p[s],Cp[s],k,'actual_word')
    # Larger integer synthetic counts target the exact 256/512/1024 boundaries.
    rng=random.Random(92041)
    for z in range(18000):
        k=rng.choice([0,1,2,7,64,1000]); d=6*k
        J=max(0,rng.choice([0,1,3078*k,6156*k,2*d,10**9])+rng.randrange(-2,3))
        J1=min(J,max(0,J//rng.choice([256,512,1024])+rng.randrange(-2,3)))
        Jp=max(0,J+rng.randint(-d,d)); J1p=min(Jp,max(0,J1+rng.randint(-d,d)))
        if abs(J1p-J1)>d: continue
        C=rng.choice([0,J//3,J//2,J]); Cp=min(Jp,max(0,C+rng.randint(-d,d)))
        if abs(Cp-C)>d: continue
        gate_checks(J,J1,C,Jp,J1p,Cp,k,'synthetic_counts')
    # Exact integer threshold checks, including equality and sub-unit lp.
    for den in (1,2,3,16,257):
        for num in range(1,3*den+1):
            x=F(num,den); K=(x.numerator+x.denominator-1)//x.denominator
            for L in range(0,min(20,K+3)):
                check((L<x)==(L<K),'lower_ceil_event')
            y=4*x; K2=y.numerator//y.denominator+1
            for L in range(0,min(20,K2+3)):
                check(not (L>y+1) or L>=K2+1,'upper_floor_event')
    for j in range(10001):
        check(F(1023*j+1,j+1)<=1023,'inverse_occupation_ratio')
    check(48*130944+16*(6156+3078)==6433056<2**23,'corruption_constant')
    check(8193*6+4<2**16,'statistical_constant_rational_upper')
    check(F(1,145)>F(1,256) and 2880<4096,'weighted_balance_constant')
    check(2**16+4096<2**17,'critical_curve_constant')
    # A useful explicit band comparison omitted as algebra in CB004:
    # ln(1+x)<=x => F <= k/M + 1/(M sqrt(beta)). No log test needed.
    output={
      'status':'PASS',
      'arithmetic':'exact Fraction arithmetic throughout; exp tails use rational upper Taylor enclosures',
      'proof_hashes':EXPECTED,
      'grid':{'kernels':625,'positive_all_state_certificates':eligible,'full_support':full,'singleton_support':singleton},
      'max_beta_times_weighted_hitting_squared':str(max_h),
      'max_beta_times_weighted_hbar_squared':str(max_hbar),
      'checks':dict(sorted(counts.items())), 'total_checks':sum(counts.values()),
      'runtime_seconds':round(time.time()-started,3),
      'limitations':'Finite corroboration only, not universal proof, formal verification, external peer review, root acceptance, or arbitrary-start adaptation.',
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE/'CB004_BP001_independent_checks.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__': main()
