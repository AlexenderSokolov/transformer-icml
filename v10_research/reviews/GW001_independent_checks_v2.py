"""Independent exact checks, not an emitted GW001 implementation or proof verifier."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, hashlib, random
ROOT=Path(__file__).resolve().parents[1]
counts=dict(histories=0,rows=0,empty_terminal=0,nonempty_terminal=0,uc=0,division=0,precision=0)
def tv(p,q): return sum(abs(a-b) for a,b in zip(p,q))/2
for k,maxm in [(2,7),(3,4)]:
 for m in range(1,maxm+1):
  for xs in product(range(k),repeat=m+2):
   counts['histories']+=1
   # Symbol-level shift construction independently of vector projection code.
   toks=list(xs)+[None]; n=len(toks)
   lag=lambda t,s:toks[t-s] if t>=s else toks[t]
   for a,q in [(1,16),(1,64),(16,16),(3,32)]:
    w=m*a
    for t in range(n):
     keys=range(2,min(t,m+1)+1) if t>=2 else [t]
     mass=[0]*k;den=0
     for i in keys:
      score=int(lag(t,1)==lag(i,1))+int(lag(t,2)==lag(i,2))
      ww=[1,w,w*w][score];den+=ww;mass[toks[i]]+=ww
     assert sum(mass)==den and 0<den<=m*w*w
     exact=[F(v,den) for v in mass]
     floor=[q*v//den for v in mass]
     out=[F(v,q) for v in floor[:-1]]+[F(q-sum(floor[:-1]),q)]
     assert min(out)>=0 and sum(out)==1
     assert tv(out,exact)<=F(k-1,q)
     counts['rows']+=1
     if t!=n-1:continue
     cs=[0]*k
     for i in range(m):
      if xs[i:i+2]==xs[-2:]:cs[xs[i+2]]+=1
     j=sum(cs); addone=[F(c+1,j+k) for c in cs]
     counts['nonempty_terminal' if j else 'empty_terminal']+=1
     discrepancy=F(k,j+k)+F(k+1,a*(j+k))
     assert tv(exact,addone)<=min(1,discrepancy)
     if j:assert tv(exact,[F(c,j) for c in cs])<=F(1,a*j)
     if a==q:assert tv(out,addone)<=F(k,j+k)+F(k,q)
# Actual-terminal UC via exact forward distributions (state, visit vector).
for d in [2,3]:
 kernels=[]
 for successors in product(range(d),repeat=d):
  kernels.append([[F(int(j==successors[i])) for j in range(d)] for i in range(d)])
 kernels += [[[F(1,d) for j in range(d)] for i in range(d)],
             [[F(1,2)*int(j==i)+F(1,2*d) for j in range(d)] for i in range(d)]]
 for p in kernels:
  allb=[]
  for start in range(d):
   dist={(start,(0,)*d):F(1)};series=[]
   for horizon in range(9):
    vals=[]
    for threshold in range(1,5):
     prob=sum(pr for (s,vis),pr in dist.items() if vis[s]<threshold)
     assert prob<=min(F(1),F(d*d*threshold,horizon+1));vals.append(prob);counts['uc']+=1
    series.append(vals)
    nxt={}
    for (s,vis),pr in dist.items():
     v=list(vis);v[s]+=1
     for u in range(d):
      key=(u,tuple(v));nxt[key]=nxt.get(key,F(0))+pr*p[s][u]
    dist={key:pr for key,pr in nxt.items() if pr}
   allb.append(series)
  for w in range(4):
   sup=[max(series[t][w] for series in allb) for t in range(9)]
   assert all(x>=y for x,y in zip(sup,sup[1:]))
   assert sum(sup)<=d*d*(w+1)
# Independent restoring division primitive and endpoint precision tests.
rng=random.Random(739)
for width in range(1,80):
 for _ in range(30):
  num=rng.randrange(1<<width);den=rng.randrange(1,1<<width) if width>1 else 1
  rem=quo=0
  for bit in range(width-1,-1,-1):
   rem=2*rem+((num>>bit)&1); assert rem<2*den
   take=int(rem>=den);rem-=take*den;quo=2*quo+take
  assert (quo,rem)==divmod(num,den);counts['division']+=1
for m in list(range(1,1000))+[2**j+o for j in range(1,500) for o in [-1,0,1]]:
 h=max(4,((m+1).bit_length()+1)//2)
 assert (1<<h)**2>=m+1;counts['precision']+=1
manifest=json.loads((ROOT/'v10_research/growing_weight/GW001_source_bindings_v2.json').read_text())
for entry in manifest['bindings']:
 assert hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest()==entry['sha256']
report={'status':'PASS','counts':counts,'source_bindings_verified':len(manifest['bindings']), 'limits':'Independent finite exact diagnostics; no original emitter, complete circuit execution, formal proof checking, or numerical-risk validation claimed.'}
(ROOT/'reviews/GW001_independent_checks_v2.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
