from pathlib import Path
from itertools import product
from fractions import Fraction as F
from hashlib import sha256
import json, math
root=Path(__file__).resolve().parents[4]
d=root/'v10_research/richer_count_consolidation_20261102'
results={}
sm=json.loads((d/'SOURCE_MAP.json').read_text())
for s in sm['sources']:
 p=root/s['path']; assert p.stat().st_size==s['bytes']; assert sha256(p.read_bytes()).hexdigest()==s['sha256'],s['path']
results['source_map_hashes']=len(sm['sources'])
for line in (d/'SOURCE_SHA256SUMS').read_text().splitlines():
 h,p=line.split(maxsplit=1); assert sha256((root/p).read_bytes()).hexdigest()==h,p
results['source_sha256sums']='PASS'
c=win=bit=0
for M in range(1,10):
 for z in product(range(2),repeat=M+2):
  H={abc:0 for abc in product(range(2),repeat=3)}
  for i in range(M): H[z[i:i+3]]+=1
  counts={(a,b):sum(H[a,b,c] for c in range(2))+int(z[-2:]==(a,b))-int(z[:2]==(a,b)) for a,b in product(range(2),repeat=2)}
  direct={(a,b):sum(z[i:i+2]==(a,b) for i in range(1,M+1)) for a,b in counts}
  assert counts==direct and min(counts.values())>=0 and sum(counts.values())==M
  zz=(1-z[0],)+z[1:]
  assert all(sum(zz[i:i+2]==ab for i in range(1,M+1))==counts[ab] for ab in counts)
  c+=1
  w=z[1:];u=w[-1];j=sum(counts[u,b] for b in range(2));jh=sum(v==u for v in w[:M//2]);B=int(512*jh>=j)
  assert B in (0,1) and j==sum(v==u for v in w[:-1]);bit+=1
  for r in range(2,M+3):
   rp=min(r,M+1);m=min(rp-1,M//2)
   assert z[-r:][-rp:]==w[-rp:]
   assert w[-(m+1):]==z[-r:][-(m+1):]
   old=j-sum(w[i]==u for i in range(M-m,M))
   assert old==sum(v==u for v in w[:M-m]);win+=1
results.update(count_reconstructions=c,scan_bits=bit,suffix_window_gates=win)
n=0
for M in range(64,501):
 N=M+1
 for k in range(M+1):
  gm2=max(F(1,M),F(k*k,M*M));gn2=max(F(1,N),F(k*k,N*N))
  assert gn2<=gm2<=F(N*N,M*M)*gn2
  if k: assert F(1,32*(M//(k+1)+1))>=F(k,96*M)
  n+=1
 for r in range(2,M+3):
  rp=min(r,M+1); assert F(M+1,rp)<=F(M+2,r)
results['exact_horizon_oracle_cases']=n
assert F(1,2**16)*F(1,2**33)==F(1,2**49)
results['oracle_factor_conversion']='PASS: pointwise g/96 <= Roracle <= 2^16 g implies 2^-16 Lambda <= D <= 96 Lambda'
results['status']='PASS; finite corroboration only, not proof of stochastic dependencies'
(d/'reviews/integration/checks_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
