from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,random,hashlib
rng=random.Random(6006)
checks=paths=0
for K in (2,3):
 for case in range(12):
  beta=F(1,5); delta=1-beta
  t=[F(1)]+[rng.choice([beta,F(1,2),F(3,4),F(1)]) for _ in range(K-1)]
  th={}
  for a,b in product(range(K),repeat=2):
   if b==0:z=t[a]
   else:z=beta/t[b]+(1-beta/t[b])*rng.choice([F(0),F(1,3),F(1)])
   raw=[rng.randint(1,3) for _ in range(K-1)]; sm=sum(raw)
   th[a,b]=[z]+[(1-z)*x/sm for x in raw]
   assert z*t[b]>=beta
  h=lambda s:F(1) if s[1] else 1-t[s[0]]
  R={}
  for s in th:
   ph=sum(th[s][c]*h((s[1],c)) for c in range(K))
   assert ph<=(delta if s[1] else 1)*h(s)
   if h(s):
    R[s]={ (s[1],c):th[s][c]*h((s[1],c))/(h(s)*(delta if s[1] else 1)) for c in range(K) if h((s[1],c))}
    assert sum(R[s].values())<=1
  for M in range(1,7):
   # Arbitrary full-support initial law, not only zero-cut starts.
   mu={s:F(i+1,K*K*(K*K+1)//2) for i,s in enumerate(th)}
   records=[];hit=[F(0)]*(M+2)
   def rec(seq,p,rp):
    global paths
    if len(seq)==M+1:
     paths+=1
     J=sum(s==seq[-1] for s in seq[:-1]);n0=sum(s[1]==0 for s in seq[:-1]);hend=h(seq[-1])
     if hend:
      assert n0<=(M+1)//2
      assert rp==p*hend/delta**(M-n0)
     records.append((p,J,n0,hend,rp,seq[-1]))
     if (0,0) in seq:hit[seq.index((0,0))]+=p
     else:hit[M+1]+=p*th[seq[-1]][0] if seq[-1][1]==0 else 0
     return
    s=seq[-1]
    for c in range(K):
     u=(s[1],c);pp=th[s][c]
     if pp:rec(seq+[u],p*pp,rp*R.get(s,{}).get(u,0))
   for s in th:rec([s],mu[s],mu[s]*h(s))
   assert sum(x[0] for x in records)==1
   D=K*K-1;q0=delta**(M//2);L=(M+1)//2
   for tt in range(1,M+2):assert hit[tt]<=F(D,tt)
   for w in range(1,M+2):
    good=sum(p for p,j,z,hh,rp,s in records if j<w and hh>=F(1,2))
    charge=sum(rp*z for p,j,z,hh,rp,s in records if j<w and hh)
    assert charge<=K**3*w
    assert good<=2*delta**M+4*q0*K**3*w/M
    danger=sum(p for p,j,z,hh,rp,s in records if s!=(0,0) and s[1]==0 and hh<F(1,2))
    assert danger<=2*hit[M+1]
    if w<=M//2:
     absorb=sum(p for p,j,z,hh,rp,s in records if j<w and s==(0,0))
     assert absorb<=F(2*D*w,M)
     total=sum(p for p,j,z,hh,rp,s in records if j<w)
     assert total<=2*delta**M+F(8*w,M+1)*(K*K+q0*K**3)
    checks+=1
out={'status':'PASS','arithmetic':'exact Fraction','sources':24,'horizons_per_source':6,'threshold_checks':checks,'complete_positive_probability_histories':paths,'beta':'1/5','K':[2,3],'M':[1,2,3,4,5,6],'includes_t_equal_one':True,'notes':'Diagnostics only; no self-acceptance or formal verification.'}
p=Path(__file__).with_name('R006_check_result.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
