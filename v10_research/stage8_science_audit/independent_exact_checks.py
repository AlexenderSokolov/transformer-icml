#!/usr/bin/env python3
"""Fresh independent finite diagnostics for the stage-eight science audit.
Fractions throughout; logarithm/square-root comparisons use certified rational
intervals. Finite diagnostics corroborate, never prove, universal theorems.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb,isqrt,factorial
from collections import Counter,defaultdict
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
TARGETS=['v10_research/source_corruption_manuscript/'+n for n in ('corrupted_trajectories.tex','nonbinary_endpoint.tex','binary.tex')]+['v10_research/source_corruption_guide/guide_final_math_zh.md','v10_research/delivery_stage8/SCIENTIFIC_FREEZE.json']
target_snapshot={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in TARGETS}
counts=Counter()
def check(ok,key):
    assert ok,key
    counts[key]+=1
def mm(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def power(A,n):
    out=[[Q(i==j) for j in range(len(A))] for i in range(len(A))]
    for _ in range(n):out=mm(out,A)
    return out
def tv(a,b):return sum(abs(x-y) for x,y in zip(a,b))/2
def hist(w):return Counter(tuple(w[j:j+3]) for j in range(len(w)-2))
# Exhaustive historywise lower-envelope algebra with genuine overlapping edits.
for M in range(1,8):
 for w in product(range(2),repeat=M+2):
  H=hist(w); u=w[-2:]; d=1-u[0]; J=sum(v for key,v in H.items() if key[:2]==u); C=H[u+(d,)]
  for mask in range(1<<M):
   k=mask.bit_count(); z=tuple((x^((mask>>i)&1)) if i<M else x for i,x in enumerate(w)); Hp=hist(z)
   dist=sum(abs(H[key]-Hp[key]) for key in H.keys()|Hp.keys()); check(dist<=6*k,'histogram_edit_bound')
   if not k:continue
   Jp=sum(v for key,v in Hp.items() if key[:2]==u); Cp=Hp[u+(d,)]; B=6*k
   qhat=Q(max(Cp-B,0),Jp+B+2); check(0<=qhat<=Q(C,J+2),'binary_downward_envelope')
   # Endpoints q=0,1 suffice for key edge cases; an interior grid tests loss truncation.
   for q in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
    rhs=(2*abs(Q(C,J)-q) if J else 0)+min(q,Q(24*k+2,J+2))
    check(abs(qhat-q)<=rhs,'binary_pathloss')
# Exact boundary cost and biased merge marginal by enumerating cycle orders.
def cycle_words(r,l):
 for ids in combinations(range(r+l),l):
  ones=set(ids); seq=tuple('L' if i in ones else 'S' for i in range(r+l))
  yield seq,''.join('101' if c=='L' else '01' for c in seq)
def hamming(a,b):return sum(x!=y for x,y in zip(a,b))
for r in range(25):
 words=list(cycle_words(r,2)); target='01'*(r+3)
 check(Q(sum(hamming(w,target) for _,w in words),len(words))==Q(2*r,3)+3,'boundary_transport_exact')
for r in range(6):
 for l in range(2,7):
  accum=Counter();totalcost=0;num=0
  for seq,w in cycle_words(r,l):
   ids=[i for i,c in enumerate(seq) if c=='L']
   for a,b in zip(ids,ids[1:]):
    seq2=seq[:a]+('S',)*(b-a+2)+seq[b+1:]
    w2=''.join('101' if c=='L' else '01' for c in seq2)
    accum[seq2]+=1;totalcost+=hamming(w,w2);num+=1
  check(Q(totalcost,num)==3+Q(2*r,l+1),'merge_mean_exact')
  for seq,_ in cycle_words(r+3,l-2):
   gaps=[];n=0
   for c in seq:
    if c=='S':n+=1
    else:gaps.append(n);n=0
   gaps.append(n)
   density=sum(comb(v-1,2) if v>=3 else 0 for v in gaps)
   check(accum[seq]==density,'merge_preimage_density')
# All-state stationary witness and fifth-step common atom, rational parameters.
for p in [Q(i,16) for i in range(2,15)]:
 R=[[0,1-p,p],[1,0,0],[0,1,0]]; R5=power(R,5)
 check([row[0] for row in R5]==[2*p*(1-p),(1-p)**2,p],'reference_fifth_power')
 check(min(row[0] for row in R5)>=Q(1,64),'reference_common_atom')
 if not Q(1,4)<=p<=Q(3,4):continue
 for M in (64,65,100,256,1024):
  for e in set([Q(1,M),Q(1,16),Q(1,32),Q(1,64)]):
   if e<Q(1,M):continue
   a=Q(1,2*M); beta=e*e; x=1/(e/a+2+p/(1-e)); pi=[x*e/a,x,x,x*p/(1-e)]
   P=[[1-a,a,0,0],[0,0,1-p,p],[e,1-e,0,0],[0,0,1-e,e]]
   check(mm([pi],P)[0]==pi,'binary_witness_stationarity')
   P2=power(P,2)
   check(all(P2[i][j]>=beta*pi[j] for i in range(4) for j in range(4)),'binary_witness_allstate')
# Exact return-count law: path enumeration independent of cycle enumeration.
for p in (Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(7,8)):
 paths={('',0):Q(1)}
 for t in range(1,19):
  nxt={}
  for (word,state),prob in paths.items():
   steps=[(1,0,1-p),(2,1,p)] if state==0 else ([(0,1,Q(1))] if state==1 else [(1,0,Q(1))])
   for st,bit,pr in steps:nxt[(word+str(bit),st)]=prob*pr
  paths=nxt
  returns={word:prob for (word,st),prob in paths.items() if st==0}
  for l in range(t//3+1):
   if (t-3*l)%2:continue
   r=(t-3*l)//2
   words=list(cycle_words(r,l)); expected=(1-p)**r*p**l
   check(all(returns[w]==expected for _,w in words),'reference_microcanonical_path_mass')
   check(sum(returns[w] for _,w in words)==comb(r+l,l)*expected,'reference_count_probability')
for m in range(1,50):
 for l in range(m+1):
  p=Q(l,m)
  check(comb(m,l)*p**l*(1-p)**(m-l)>=Q(1,m+1),'exact_binomial_mode_mass')
# Grid inequalities, using rational t/k; no logs are needed.
for t in (1,4095,4096,4097,100000,2**40):
 for k in (1,2,4096,2**20,2**60):
  n=max(1,(3*2**18*t+k-1)//k)
  check(Q(3,4*n)<=Q(k,2**20*t),'bridge_grid_spacing')
  check(n+1<=2+Q(2**20*t,k),'bridge_grid_labels')
# Exact endpoint witness certificates, off-support starts included.
for K in (2,3,5):
 for delta in [Q(i,16) for i in range(17)]:
  alpha=min(delta/2,Q(1,4)); beta=1-delta
  T=[[Q(0) for _ in range(K)] for _ in range(K)]
  for y in range(K):
   T[y][0]=Q(1,2)+(alpha if y==0 else -alpha if y==1 else 0)
   T[y][1]=1-T[y][0]
  pi=[Q(1,2),Q(1,2)]+[Q(0)]*(K-2)
  Pi=[pi[x]*T[x][y] for x in range(K) for y in range(K)]
  P=[[Q(0) for _ in range(K*K)] for _ in range(K*K)]
  for x,y,z in product(range(K),repeat=3):P[x*K+y][y*K+z]=T[y][z]
  check(mm([Pi],P)[0]==Pi,'endpoint_stationarity')
  P2=power(P,2)
  check(all(P2[i][j]>=beta*Pi[j] for i in range(K*K) for j in range(K*K)),'endpoint_allstate_certificate')
  check(alpha-2*alpha*alpha>=delta/8,'endpoint_delta_floor')
  for u in range(K*K):
   marginal=[sum(P2[u][c*K+d] for d in range(K)) for c in range(K)]
   check(marginal==T[u%K] and all(marginal[c]>=beta*pi[c] for c in range(K)),'certificate_marginal_identity')
for delta in (Q(0),Q(1,8),Q(1,2),Q(3,4),Q(1)):
 alpha=min(delta/2,Q(1,4));T=[[Q(1,2)+alpha,Q(1,2)-alpha],[Q(1,2)-alpha,Q(1,2)+alpha]]
 for N in range(3,9):
  obs=defaultdict(lambda:defaultdict(Q))
  for w in product(range(2),repeat=N):
   pr=Q(1,2)
   for a,b in zip(w,w[1:]):pr*=T[a][b]
   obs[w[:-1]][T[w[-1]][1]]+=pr
  for o,masses in obs.items():
   zvals=list(masses); mass=sum(masses.values())
   loss=min(sum(pr*abs(z-target) for target,pr in masses.items()) for z in zvals)/mass
   check(loss==alpha-2*alpha*alpha,'erased_prefix_exact_Bayes_loss')
# Genuine second-order martingale second moment and arbitrary initial pairs.
rows={u:Q(v,5) for u,v in zip(product(range(2),repeat=2),(1,2,4,3))}
for init in ( {(0,0):Q(1)}, {(1,0):Q(1)}, {u:Q(1,4) for u in rows} ):
 for M in (1,2,4,6):
  emean=Q(0);esq=Q(0);variances=Q(0);cross=Q(0)
  for u,mass in init.items():
   for tail in product(range(2),repeat=M):
    w=u+tail;pr=mass; ds=[]; vv=[]
    for j,bit in enumerate(tail):
     p=rows[w[j:j+2]];pr*=p if bit else 1-p;ds.append(bit-p);vv.append(p*(1-p))
    emean+=pr*sum(ds);esq+=pr*sum(ds)**2;variances+=pr*sum(vv)
    cross+=pr*sum(ds[i]*ds[j] for i in range(M) for j in range(i+1,M))
  check(emean==0 and cross==0 and esq==variances,'pooled_martingale_exact_moments')
# Rational interval arithmetic: rigorous enclosures, no floating point tests.
NTERM=34

def log_small_interval(x):
 z=(x-1)/(x+1); assert 0<=z<=Q(1,3)
 s=Q(0);p=z
 for n in range(NTERM):s+=p/Q(2*n+1);p*=z*z
 lo=2*s; hi=lo+2*p/(Q(2*NTERM+1)*(1-z*z))
 return lo,hi
LOG2=log_small_interval(Q(2))
def log_interval(x):
 assert x>=1
 n=x.numerator.bit_length()-x.denominator.bit_length()
 if x<Q(2)**n:n-=1
 y=x/Q(2)**n;lo,hi=log_small_interval(y)
 return lo+n*LOG2[0],hi+n*LOG2[1]
def sqrt_interval(n):
 scale=10**45; a=isqrt(n*scale*scale)
 return Q(a,scale),Q(a+1,scale) if a*a!=n*scale*scale else Q(a,scale)
def log1p_bounds(lo,hi):return log_interval(1+lo)[0],log_interval(1+hi)[1]
for M in (64,65,81,100,127,256,1000,4096,10000,2**32,2**64,10**60):
 rl,rh=sqrt_interval(M)
 for e in sorted(set([Q(1,M),Q(2,M),Q(1,64),Q(1,16),Q(1,2),Q(1)])):
  if e<Q(1,M):continue
  xl,xh=1/(e*rh),1/(e*rl);ll,lh=log1p_bounds(xl,xh);fl,fh=1+ll,1+lh;Tl,Th=rl/fh,rh/fl
  check(Tl>=1 and Th<=rh,'tolerance_range_interval')
  floorlo=Tl.numerator//Tl.denominator;floorhi=Th.numerator//Th.denominator
  check(floorlo==floorhi,'tolerance_floor_certified')
  kmax=floorlo
  for k in sorted(set([0,1,kmax,max(1,kmax-1),min(M,kmax+1),M])):
   if not k:check(True,'tolerance_zero_budget');continue
   loglo,loghi=log_interval(1+1/(e*k));F_lo=Q(k,M)*(1+loglo);F_hi=Q(k,M)*(1+loghi)
   if k<=kmax:check(F_hi<=2/rh,'tolerance_integer_sufficiency')
   for A in (Q(1,8),Q(1,2),Q(1),Q(2),Q(10)):
    # Trigger necessity only when premise is rigorously true; disjoint false cases explicit.
    if F_hi<=A/rh:check(k<=A*max(A,1)*Tl,'tolerance_integer_necessity')
    elif F_lo>A/rl:check(True,'tolerance_premise_false')
    else:raise AssertionError('inconclusive tolerance interval')
# Finite scalar completion, including author empty/nonempty cutoff and arbitrary
# positive c, C>=1. Use a certified integral lower bound for the exact harmonic
# sum; proving the inequality with this smaller T is stronger for each test.
for M,k in ((64,1),(64,64),(65,4),(256,16),(4096,64),(2**40,2**30),(2**40,2**31),(2**80,2**40)):
 for e in (Q(1,M),Q(1,64),Q(1,16),Q(1)):
  if e<Q(1,M):continue
  for c,C,j0 in ((Q(1,8),1,1),(Q(1,2),8,3),(Q(1,2**44),8,4096)):
   ll,lh=log_interval(Q(k+2));ulo=min(1/(C*e),c*k*k/lh);uhi=min(1/(C*e),c*k*k/ll)
   jl=ulo.numerator//ulo.denominator;jh=uhi.numerator//uhi.denominator
   check(jl==jh,'scalar_cutoff_floor_certified')
   if jl<j0:
    Tlower=Q(0);check(True,'scalar_empty_sum_case')
   else:
    loglower=log_interval(Q(k+jl+1,k+j0))[0];Tlower=Q(k,M)*loglower
    check(True,'scalar_nonempty_sum_case')
   Fhi=Q(k,M)*(1+log_interval(1+1/(e*k))[1])
   Dlo=7+log_interval(Q(max(1,C)))[0]+6*log_interval(max(Q(1),2/c))[0]
   faclo=Dlo*(1+log_interval(Q(1+j0))[0]);rl,rh=sqrt_interval(M)
   check(Fhi<=faclo*max(1/rh,Q(k,M),Tlower),'scalar_completion_interval')

# Certified constant inequalities, algebraic radical elimination and logarithm intervals.
# 1024*sqrt(2*2^-44)+326/2^20 <1/1024 iff sqrt(2)<698/256.
check(Q(2)<Q(698,256)**2,'entropy_cutoff_constant_exact')
l4097=log_interval(Q(4097))
check((7+273*LOG2[1])*(1+l4097[1])<1830,'scalar_completion_constant_interval')
check(1830<2**11 and 4*(8192+1)**2*32 < (2**17-4)**2,'lower_and_upper_constant_slack')
check(target_snapshot=={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in TARGETS},'target_snapshot_stable')
result={'target_snapshot':target_snapshot,'status':'PASS','arithmetic':'Exact fractions, plus rigorous rational enclosures for logarithms and square roots','counts':dict(counts),'total_checks':sum(counts.values()),'scope':'Finite corroboration only, not a proof or formal verification. Small M tests are historywise algebra only and do not extend theorem domains.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'independent_exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
