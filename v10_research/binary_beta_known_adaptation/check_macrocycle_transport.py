"""Contributor diagnostics for unreviewed macrocycle/Hamming notes."""
from fractions import Fraction as F
from itertools import product
from math import comb,isqrt
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
counts={'full_binary_words':0,'words_with_complete_cycles':0,'negative_binomial_identities':0,
        'same_beta_family_cases':0,'three_step_hit_bounds':0}

def cycles(s):
    Y=[s[i:i+2] for i in range(len(s)-1)]
    try:t=Y.index('00')
    except ValueError:return []
    ans=[]
    while True:
        try:u=Y.index('11',t+1);v=Y.index('00',u+1)
        except ValueError:break
        U=sum(z=='00' for z in Y[t:u]);V=sum(z=='11' for z in Y[u:v])
        ans.append((U,V));t=v
    return ans
for N in range(2,15):
    for bits in product('01',repeat=N):
        s=''.join(bits);uv=cycles(s)
        best=min(sum(ch=='0' for ch in s[:cut])+sum(ch=='1' for ch in s[cut:]) for cut in range(N+1))
        assert best>=sum(min(u,v) for u,v in uv),(s,uv,best)
        counts['full_binary_words']+=1
        if uv:counts['words_with_complete_cycles']+=1

for alpha in (F(1,11),F(1,3),F(2,3),F(1)):
 for delta in (F(1,13),F(1,4),F(3,4),F(1)):
    sigma=alpha+delta-alpha*delta
    for n in range(1,7):
     for k in range(0,17):
        geom_sum=sum((F(comb(l-1,n-1))*sigma**n*(1-sigma)**(l-n) for l in range(n,k+1)),F(0))
        bin_tail=sum((F(comb(k,z))*sigma**z*(1-sigma)**(k-z) for z in range(n,k+1)),F(0))
        assert geom_sum==bin_tail
        counts['negative_binomial_identities']+=1

states=((0,0),(0,1),(1,0),(1,1))
def matrix(a,b,e,t):
    theta=(a,b,1-e,1-t)
    return [[(theta[i] if z else 1-theta[i]) if v==u else F(0) for u,z in states] for i,(q,v) in enumerate(states)]
def square(P):
    return [[sum((P[i][h]*P[h][j] for h in range(4)),F(0)) for j in range(4)] for i in range(4)]
def hit3(P,i,target):
    if i==target:return F(1)
    d={i:F(1)}
    for _ in range(3):
        nxt={j:F(0) for j in range(4) if j!=target}
        for u,m in d.items():
            for j in nxt:nxt[j]+=m*P[u][j]
        d=nxt
    return 1-sum(d.values(),F(0))
for exponent in (20,24,28,32):
 M=10**exponent;rt=isqrt(M);k=M//10000;b=F(1,rt);e=1-b;h=b+e-b*e
 for c in (F(1,64),F(1,16),F(1,4),F(1)):
  for frac in (F(1,8),F(1,4),F(1,2),F(3,4),F(7,8)):
    j=int(M*frac);den=M-j-2*c*k
    x=c*k/M;y=F(j,M);w=1-y-2*x
    a=x*e/y;t=x*b/w;nu=c*k*b*e/h
    assert j>=800*k and den>=800*k and nu>=200
    assert 0<a<=F(1,800) and 0<t<=b/800
    pi=(y,x,x,w);P=matrix(a,b,e,t);P2=square(P);beta=F(1,M)
    assert all(sum((pi[i]*P[i][l] for i in range(4)),F(0))==pi[l] for l in range(4))
    assert all(P2[i][l]>=beta*pi[l] for i in range(4) for l in range(4))
    alpha=a*b/h;delta=t*e/h;sigma=alpha+delta-alpha*delta
    assert alpha==nu/j and delta==nu/den
    p=nu/(2*M)
    for target in (0,3):
        for i in range(4):
            assert hit3(P,i,target)>=p
            counts['three_step_hit_bounds']+=1
    n=nu.numerator//(100*nu.denominator);mean=(M//3)*p
    assert F(2*n+1)<=nu/40 and mean>=nu/8
    assert n>=nu/200 and k*sigma<=F(n,2)
    counts['same_beta_family_cases']+=1

out={'status':'PASS','review_status':'UNREVIEWED_CONTRIBUTOR_DIAGNOSTIC','arithmetic':'exact integers/Fraction throughout',
'counts':counts,'notes_sha256':hashlib.sha256((root/'macrocycle_transport_barrier_unreviewed.md').read_bytes()).hexdigest(),
'scope':'Finite Hamming geometry, geometric/binomial identities, and exact same-beta-family certificate/hitting/cost conditions; not an independent review or a universal-proof substitute.'}
(root/'macrocycle_transport_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
