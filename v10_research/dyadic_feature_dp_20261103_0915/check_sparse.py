from itertools import product
from math import comb
import runpy
ns=runpy.run_path('v10_research/dyadic_feature_dp_20261103_0915/check_dp.py')
rule=ns['rule']; cases=layers=0
for M in range(1,6):
 for h in product((0,1),repeat=M+2):
  for k in range(M+1):
   cur={(0,(0,0),(0,0)):0}
   for t in range(M+3):
    e=min(t,M); K=sum(comb(e,j) for j in range(min(k,e)+1))
    assert len(cur)<=K
    layers+=1
    if t==M+2:break
    nxt={}
    for (q,w,b),cost in cur.items():
     for x in ((0,1) if t<M else (h[t],)):
      c=cost+(t<M and x!=h[t])
      if c>k:continue
      q2,w2,inc=rule(t,q,w,x,h);key=(q2,w2,tuple(v+y for v,y in zip(b,inc)))
      if key not in nxt or c<nxt[key]:nxt[key]=c
    cur=nxt
   cases+=1
print('sparse_budget_cases',cases,'layers',layers,'PASS')
