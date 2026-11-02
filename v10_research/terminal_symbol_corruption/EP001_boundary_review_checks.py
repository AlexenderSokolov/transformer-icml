#!/usr/bin/env python3
"""Fresh independent exact diagnostics; finite tests corroborate, not prove EP001."""
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt, log
from pathlib import Path
import hashlib,json,random
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
CAND=OUT/'EP001_endpoint_corruption.md'
EXPECTED='bf58470664861f28dbd8746d5b0c54eea1beadd98e87c2c80600b1ec68c796fa'
assert hashlib.sha256(CAND.read_bytes()).hexdigest()==EXPECTED
results={}
def tv(a,b): return sum(abs(x-y) for x,y in zip(a,b))/2
def pair(theta,K):
    return [[theta[a*K+b][d] if c==b else F(0) for c,d in product(range(K),repeat=2)] for a,b in product(range(K),repeat=2)]
def mul(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def stat(P):
    n=len(P); A=sp.Matrix(P).T-sp.eye(n); A[n-1,:]=sp.ones(1,n)
    z=sp.zeros(n,1); z[n-1]=1
    return [F(x) for x in A.inv()*z]
rng=random.Random(127135)
chains=[]
for K in (2,3,4):
    for rep in range(12):
        theta=[]
        for _ in range(K*K):
            w=[rng.randrange(1,10) for c in range(K)]; theta.append([F(x,sum(w)) for x in w])
        P=pair(theta,K); Pi=stat(P); Q=mul(P,P)
        beta=min(Q[u][v]/Pi[v] for u in range(K*K) for v in range(K*K))
        assert 0<beta<=1
        pi=[sum(Pi[c*K+d] for d in range(K)) for c in range(K)]
        assert [sum(Pi[u]*P[u][v] for u in range(K*K)) for v in range(K*K)]==Pi
        for u in range(K*K):
            for c in range(K):
                assert sum(Q[u][c*K+d] for d in range(K))==theta[u][c]
                assert theta[u][c]>=beta*pi[c]
            assert tv(theta[u],pi)<=1-beta
        chains.append((K,theta,P,Pi,beta))
results['random_rational_all_state_certificates']=len(chains)
# All-pair support extension, exact stationary enumeration, conditional endpoint Bayes lower.
prefixes=0;certs=0
for delta in (F(0),F(1,100),F(1,4),F(1,2),F(3,4),F(1)):
    alpha=min(delta/2,F(1,4)); beta=1-delta
    for K in (2,3,5):
        T=[[F(1,2)+(alpha if x==y else -alpha) if x<2 and y<2 else (F(1,2) if x>=2 and y<2 else F(0)) for y in range(K)] for x in range(K)]
        theta=[T[b] for a,b in product(range(K),repeat=2)]
        Pi=[F(1,2)*T[a][b] if a<2 else F(0) for a,b in product(range(K),repeat=2)]
        P=pair(theta,K);Q=mul(P,P)
        assert [sum(Pi[u]*P[u][v] for u in range(K*K)) for v in range(K*K)]==Pi
        assert all(Q[u][v]>=beta*Pi[v] for u in range(K*K) for v in range(K*K))
        certs+=1
    for N in (3,5,8):
        grouped={}
        for word in product(range(2),repeat=N):
            p=F(1,2)
            for a,b in zip(word,word[1:]): p*=F(1,2)+(alpha if a==b else -alpha)
            prefix=word[:-1]; probs=grouped.setdefault(prefix,[F(0),F(0)])
            probs[word[-1]]+=p
        total=F(0)
        for prefix,masses in grouped.items():
            mass=sum(masses);post=[p/mass for p in masses]
            assert sorted(post)==[F(1,2)-alpha,F(1,2)+alpha]
            targets=[F(1,2)-alpha,F(1,2)+alpha]
            loss=min(sum(post[i]*abs(z-targets[i]) for i in (0,1)) for z in targets)
            assert loss==alpha-2*alpha*alpha
            assert loss>=delta/8
            total+=mass*loss; prefixes+=1
        assert total==alpha-2*alpha*alpha
results['off_support_certificates']=certs
results['exact_erased_prefix_posteriors']=prefixes
# Exact vector martingale orthogonality/variance and pooled triangle inequality, arbitrary starts.
mart=0
for K,theta,P,Pi,beta in chains[:3]:
    for mu in (Pi,[F(int(u==0)) for u in range(K*K)], [F(1,K*K)]*(K*K)):
        M=4; var=F(0); condvar=F(0); cross=F(0); mean=[F(0)]*K
        for word in product(range(K),repeat=M+2):
            prob=mu[word[0]*K+word[1]];Ds=[];ms=[]
            for t in range(2,M+2):
                m=theta[word[t-2]*K+word[t-1]];prob*=m[word[t]];ms.append(m)
                Ds.append([F(int(c==word[t]))-m[c] for c in range(K)])
            sums=[sum(d[c] for d in Ds) for c in range(K)]
            var+=prob*sum(x*x for x in sums)
            condvar+=prob*sum(1-sum(x*x for x in m) for m in ms)
            cross+=prob*sum(sum(Ds[i][c]*Ds[j][c] for c in range(K)) for i in range(M) for j in range(i))
            mean=[mean[c]+prob*sums[c] for c in range(K)]
            empirical=[F(word[2:].count(c),M) for c in range(K)]
            target=theta[word[-2]*K+word[-1]]
            assert tv(empirical,target)<=sum(abs(x) for x in sums)/(2*M)+2*(1-beta)
        assert var==condvar and cross==0 and mean==[0]*K and var<=M
        mart+=1
results['exact_martingale_path_enumerations']=mart
# All clean/corrupted binary words, includes initial-only and adjacent endpoint edits.
perturb=0
for N in range(3,8):
    M=N-2
    for x in product(range(2),repeat=N):
        for y in product(range(2),repeat=N):
            edits=sum(a!=b for a,b in zip(x,y))
            px=[F(x[2:].count(c),M) for c in range(2)]
            py=[F(y[2:].count(c),M) for c in range(2)]
            assert tv(px,py)<=F(edits,M)
            perturb+=1
results['exhaustive_empirical_perturbations']=perturb
# Exact combinatorial ancillarity and all k lower-constant checks.
anc=0
for M in range(1,18):
    for k in range(M+1):
        for n in range(M+1):
            r=(k+1)*(n//(k+1));assert n-r<=k
            assert F(comb(M-r,n-r),comb(M,n)*comb(n,r))==F(1,comb(M,r));anc+=1
results['count_erasure_ancillarity_identities']=anc
const=0
for M in (64,65,100,127,128,1000,10000):
    N=M+2
    assert 3/(128*sqrt(N))>=1/(64*sqrt(M))
    h=1/(16*sqrt(N));kl=2*h*log((.5+h)/(.5-h))
    assert N*kl<=1/8
    for k in range(1,M+1):
        b=k+1
        assert F(1,32*(M//b+1))>=F(b,32*(M+b))>=F(k,96*M)
        const+=1
results['finite_domain_constant_cases']=const
results['candidate_sha256']=EXPECTED
results['status']='PASS'
(OUT/'EP001_boundary_review_checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
