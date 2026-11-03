#!/usr/bin/env python3
"""Finite diagnostics; not a replacement for the analytic proofs."""
import itertools, math, json, hashlib
from pathlib import Path
from fractions import Fraction as F
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent

def counts(w):
    h=[[0,0] for _ in range(4)]
    for i in range(len(w)-2):h[2*w[i]+w[i+1]][w[i+2]]+=1
    return h

def mass(w):
    out=F(1,4)
    for x,y in counts(w):out*=F(math.factorial(x)*math.factorial(y),math.factorial(x+y+1))
    return out

def bayes(w):
    c=counts(w)[2*w[-2]+w[-1]]
    return F(c[1]+1,sum(c)+2)

def H(p):
    return -sum(x*math.log(x) for x in (p,1-p) if x>0)
def kl(p,q):
    return sum(x*math.log(x/y) for x,y in ((p,q),(1-p,1-q)) if x>0)

out={'purpose':'Exact finite diagnostics and numerical sanity checks, not formal proof or independent review.'}
nwords=0
for M in range(0,11):
    total=F(0)
    groups={}
    for w in itertools.product((0,1),repeat=M+2):
        nwords+=1
        pw=mass(w); b=bayes(w)
        assert pw>0 and 0<b<1
        assert mass(w+(1,))/pw==b
        assert mass(w+(0,))+mass(w+(1,))==pw
        total+=pw
        key=(tuple(map(tuple,counts(w))),w[-2:])
        assert groups.setdefault(key,b)==b
        c=counts(w)[2*w[-2]+w[-1]];j=sum(c)
        if j: assert abs(b-F(c[1],j))<=F(1,j+2)
    assert total==1
out['exact_word_posterior_and_normalization']={'M_range':[0,10],'words':nwords,'pass':True}
# Every legal single-bit edit on small words; all probability ratios exact.
edits=0
for M in range(1,9):
    for w in itertools.product((0,1),repeat=M+2):
        j=sum(counts(w)[2*w[-2]+w[-1]])
        for i in range(M):
            z=list(w);z[i]^=1;z=tuple(z)
            assert abs(bayes(w)-bayes(z))<=min(F(1),F(12,j+2))
            edits+=1
out['exact_add_one_edit_bound']={'single_edit_pairs':edits,'pass':True}
# General ratio perturbation identity beyond reachable Markov count pairs.
ratios=0
for j in range(21):
 for c in range(j+1):
  for jp in range(21):
   for cp in range(jp+1):
    assert abs(F(c+1,j+2)-F(cp+1,jp+2))<=F(abs(c-cp)+abs(j-jp),j+2)
    ratios+=1
out['exact_ratio_perturbation']={'count_pairs':ratios,'pass':True}
# The two-step pair transition identity, checked symbolically with polynomials.
import sympy as sp
p=sp.symbols('p0:4')
P=sp.zeros(4)
for a,b,c in itertools.product((0,1),repeat=3):P[2*a+b,2*b+c]=p[2*a+b] if c else 1-p[2*a+b]
P2=P*P
for a,b,c,d in itertools.product((0,1),repeat=4):
 expected=(p[2*a+b] if c else 1-p[2*a+b])*(p[2*b+c] if d else 1-p[2*b+c])
 assert sp.expand(P2[2*a+b,2*c+d]-expected)==0
x=sp.symbols('x')
assert sp.expand(1-(1-2*x)**4)==8*x-24*x*x+32*x**3-16*x**4
out['symbolic_pair_and_prior_identities']={'entries':16,'pass':True}
# Entropy bound with 50-digit arithmetic, avoiding floating endpoint drift.
import mpmath as mp
mp.mp.dps=50
def mh(p):
    return -sum(x*mp.log(x) for x in (p,1-p) if x>0)
def mk(p,q):
    return sum(x*mp.log(x/y) for x,y in ((p,q),(1-p,1-q)) if x>0)
entropy_tests=0; minimum_slack=mp.inf
for estr in ('1e-8','1e-4','.01','.125','.25','.5'):
 eta=mp.mpf(estr)
 for i in range(51):
  pp=mp.mpf(i)/50
  for j in range(51):
   q=eta+(1-2*eta)*j/50;delta=abs(pp-q)
   slack=mh(delta)+delta*mp.log((1-eta)/eta)-mk(pp,q)
   assert slack>=mp.mpf('-1e-40'),(eta,pp,q,slack)
   minimum_slack=min(minimum_slack,slack);entropy_tests+=1
minimum_slack=str(minimum_slack)
out['numerical_entropy_inequality']={'cases':entropy_tests,'minimum_slack':minimum_slack,'pass':True}
D=131081
assert D==131072+8+1
assert 2**17+2**23+1==8519681
out['constants']={'D':D,'large_M_threshold':(2*D)**2,'robust_factor':2**17+2**23+1}
# Verify hash agreement of imported manuscript and ACG against their acceptance receipts.
prefix=Path('v10_research/resumption_20261103/recovered_science')
receipt=json.loads((ROOT/prefix/'intake/positional_finite_manuscript_root_acceptance.json').read_text())
checks=[]
for f in ('main.tex','sections/proofs_positive.tex','sections/proofs_negative.tex','sections/proofs_finite_horizon.tex'):
 path=prefix/'positional_manuscript_finite_20261102'/f
 digest=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
 assert digest==receipt['artifacts'][f]['sha256']
 checks.append(str(path))
a=Path('v10_research/approximate_gate_statistics_20261103')
ar=json.loads((ROOT/a/'ROOT_ACCEPTANCE.json').read_text())
assert hashlib.sha256((ROOT/a/'CANDIDATE.md').read_bytes()).hexdigest()==ar['candidate_sha256']
out['source_receipt_hash_checks']={'manuscript':checks,'ACG':True,'pass':True}
(BASE/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
