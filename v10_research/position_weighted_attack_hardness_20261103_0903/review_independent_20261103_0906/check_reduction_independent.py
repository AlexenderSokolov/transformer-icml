"""Deterministic independent padded-mask, embedding and certificate audit. No RNG."""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,gzip,hashlib,sys
P=Path(__file__).resolve().parent
cases=[]
for n in (2,3):
 for a in product((1,2,3),repeat=n):
  for B in range(sum(a)+1):cases.append((a,B))
for a in [(1,3,4,6),(2,5,7,13),(2**512+1,2**511+3,7)]:
 for B in [0,a[0],sum(a),sum(a)-1]:cases.append((a,B))
# Fixed exact sources; no generated random words or model initialization.
def certificate(M):
 p=F(1,M*M); dist=[(1-p)**2,(1-p)*p,p*(1-p),p*p];P=[[F(0) for _ in range(4)] for _ in range(4)]
 for u in range(4):P[u][2*(u%2)]=1-p;P[u][2*(u%2)+1]=p
 assert all(sum(P[u][v]*P[v][w] for v in range(4))==dist[w] for u in range(4) for w in range(4)); assert sum(dist)==1 and (1-p)**(M+2)>=1-F(M+2,M*M)
 return p
casecount=maskcount=0; extras=0
with (P/'candidate_records.jsonl.gz').open('xb') as raw, gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as gz:
 for ci,(weights,B) in enumerate(cases):
  n=len(weights);M=1<<(max(n*n,4)-1).bit_length();A=sum(weights);C=max(weights);G=1<<(A-1).bit_length();k=n;t=F(1,M+2);ceiling=F(3,2*M);assert n*n<=M<2*n*n and (M&(M-1))==0 and k*k<=M and A<=G<2*A
  poss={sum(weights[i] for i in range(n) if bits[i]) for bits in product((0,1),repeat=n)}; assert certificate(M)==F(1,M*M);seen=set();count=0
  for j in range(k+1):
   for ix in combinations(range(M),j):
    z=[0]*M
    for i in ix:z[i]=1
    V=[]
    for i in range(M):
     ai=weights[i] if i<n else 0;position=(ai-C,0);token=(0,z[i]);embed=(position[0]+token[0],position[1]+token[1]);v=max(0,embed[0]+C*embed[1]);assert v==ai*z[i];V.append(v)
    attention=sum(V,F(0))/M;S=M*attention;assert S.denominator==1;S=int(S);seen.add(S);r=-F(max(S-B,0)+max(B-S,0),2*G);qd=ceiling-F(abs(S-B),2*M*G)
    assert -F(1,2)<=r<=0 and F(1,M)<=qd<=ceiling<=F(3,8) and qd>t and ((r==0)==(qd==ceiling)==(S==B));rec={'case':ci,'indices':ix,'S':S,'r':[r.numerator,r.denominator],'q_d':[qd.numerator,qd.denominator]};gz.write((json.dumps(rec,separators=(',',':'))+'\n').encode());count+=1
  assert seen==poss;extras+=int(B in poss);maskcount+=count;casecount+=1;rec={'type':'case','case':ci,'weights':weights,'B':B,'M':M,'k':k,'G':G,'C':C,'original_subset_sums':sorted(poss),'yes':B in poss,'masks':count};gz.write((json.dumps(rec,separators=(',',':'))+'\n').encode())
print('deterministic cases',casecount,'legal masks checked and preserved',maskcount,'yes',extras,'includes 512-bit weights and 4-item full padded budgets')
print('for each M, exact IID pair-chain P²=Pi for all 16 state pairs; Bernoulli zero-history union bound verified')
print('candidate records SHA256',hashlib.sha256((P/'candidate_records.jsonl.gz').read_bytes()).hexdigest())
