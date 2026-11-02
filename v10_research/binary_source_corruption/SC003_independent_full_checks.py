#!/usr/bin/env python3
"""Fresh full-review diagnostics; finite corroboration, never a universal proof."""
import hashlib,itertools,json,math,random
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).with_suffix('.json')
rng=random.Random(202611020851)
counts={}
def tick(key,n=1): counts[key]=counts.get(key,0)+n

def hist(w):
    h=[0]*8
    for a,b,c in zip(w,w[1:],w[2:]): h[4*a+2*b+c]+=1
    return h

def row(h,u):
    d=1-(u//2)
    return h[2*u+d],h[2*u]+h[2*u+1]

def algebra(C,J,Cp,Jp,k,q):
    B=6*k; A=4*B+2
    assert abs(C-Cp)+abs((J-C)-(Jp-Cp))<=B
    z=Q(max(Cp-B,0),Jp+B+2)
    assert 0<=z<=Q(C,J+2)<=1
    assert Q(C,J+2)-z<=Q(4*B,J+2)
    if J:
        p=Q(C,J)
        assert 0<=p-z<=min(p,Q(A,J+2))
        assert abs(z-q)<=2*abs(p-q)+min(q,Q(A,J+2))
    else:
        assert z==0 and min(q,Q(A,2))==q
    tick('exact_algebra')

# All binary clean words and all editable masks, not only separated edits.
for M in range(1,8):
  for w in itertools.product(range(2),repeat=M+2):
    h=hist(w);u=2*w[-2]+w[-1];C,J=row(h,u)
    for mask in range(1<<M):
      k=mask.bit_count(); z=tuple(x^((mask>>i)&1) if i<M else x for i,x in enumerate(w))
      hp=hist(z);Cp,Jp=row(hp,u)
      assert sum(abs(x-y) for x,y in zip(h,hp))<=6*k
      assert z[-2:]==w[-2:]
      tick('exhaustive_word_masks')
      if k: algebra(C,J,Cp,Jp,k,Q((mask+sum(w))%5,4))
      else:
        assert hp==h
        assert Q(Cp+1,Jp+2)+Q(Jp-Cp+1,Jp+2)==1
        tick('k0_branch')
      wc=tuple(1-x for x in w);zc=tuple(1-x for x in z)
      assert row(hist(wc),3-u)==(C,J) and row(hist(zc),3-u)==(Cp,Jp)
      tick('symbol_complement_equivariance')

# Larger exact row perturbations exercise nonzero numerators and slack budgets.
for _ in range(40000):
    J=rng.randrange(0,10001); C=rng.randrange(J+1); k=rng.randrange(1,101); B=6*k
    dx=rng.randrange(-min(C,B),B+1)
    dy=rng.randrange(-min(J-C,B-abs(dx)),B-abs(dx)+1)
    Cp=C+dx;Jp=J+dx+dy
    algebra(C,J,Cp,Jp,k,Q(rng.randrange(101),100))
    if C==0: assert max(Cp-B,0)==0

# Independently compute the attack output probabilities from input/subset enumeration.
for M in range(1,9):
  for k in range(M+1):
    b=k+1
    for n in range(M+1):
      r=b*(n//b); probs={}
      for ones in itertools.combinations(range(M),n):
        for retained in itertools.combinations(ones,r):
          probs[retained]=probs.get(retained,Q(0))+Q(1,math.comb(M,n)*math.comb(n,r))
      assert len(probs)==math.comb(M,r)
      assert set(probs.values())=={Q(1,math.comb(M,r))}
      assert n-r<=k
      tick('exact_erasure_cells')

# Finite-domain constants, KL floors, weak-cutoff scalar and protected-label lower.
psi=lambda x: 1 if x>=1 else x*(1+math.log(1/x))
assert 2*8193*math.sqrt(32)+4<2**17
assert 16672*26==433472<2**19
assert 256*26+16==6672
for M in list(range(64,513))+[10**j for j in range(3,16)]:
  for k in sorted({1,M,max(1,M//2),max(1,int(math.sqrt(M)))}):
    z=M/k
    assert psi(416/z)<=416/z*(1+math.log1p(z))+1e-12
    b=k+1
    assert Q(1,32*(M//b+1))>=Q(b,32*(M+b))>=Q(k,96*M)
    tick('scalar_and_lower')
  N=M+2; d=1/(16*math.sqrt(N)); p=.5+d; pm=.5-d
  KL=p*math.log(p/pm)+(1-p)*math.log((1-p)/(1-pm))
  assert N*KL<=.125+1e-6
  assert 3/(128*math.sqrt(N))>=1/(64*math.sqrt(M))
  tick('clean_floor')

# Acceptance bindings and the exact editorial-only R011 difference.
receipts=[('SC001','source_symbol_corruption/SC001_theorem.md'),('SC002','source_symbol_corruption_mixing/SC002_theorem.md'),('BIF001','binary_all_start/BIF001_binary_all_initializations_frontier_v1.md'),('BAI003','binary_arbitrary/BAI003_uniform_absorbing_binary_upper_v2.md')]
for name,rel in receipts:
    r=json.loads((ROOT/'v10_research/intake'/f'{name}_acceptance.json').read_text())
    assert hashlib.sha256((ROOT/'v10_research'/rel).read_bytes()).hexdigest()==r['sha256']
    tick('accepted_proof_hashes')
rdir=ROOT/'cloud_work/conditions-20261028/research/resume_20261030'
r=json.loads((rdir/'R011_root_acceptance.json').read_text())
raw=(rdir/'R011_global_rates_and_constant_adaptation_v1.md').read_bytes()
assert hashlib.sha256(raw).hexdigest()==r['proof_sha256']
readable=(ROOT/'v10_intake/source/sources/dot-return/readable/proofs/R011_global_rates_and_constant_adaptation_v1.md').read_bytes()
assert readable.split(b'\n',2)[2]==raw
# Bind target so this run cannot be silently attributed to a later draft.
target=Path(__file__).with_name('SC003_theorem.md')
result={'status':'PASS','seed':202611020851,'target_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'checks':counts,'total_checks':sum(counts.values()),'constants':{'statistical_coefficient':2*8193*math.sqrt(32)+4,'corruption_coefficient':433472,'absorbing_coefficient':6672},'limitations':'Exact finite enumeration and scalar diagnostics corroborate only tested instances; universal claims require the written independent proof audit. Same-model independent LLM review, not formal or external review.'}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
