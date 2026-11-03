"""Independent exact-rational finite diagnostics; not a universal proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, hashlib
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[2]
def clip(x,a,b): return min(b,max(a,x))
def ceil(x): return -((-x.numerator)//x.denominator)
stats={k:0 for k in ['clipping_cases','pathwise_cases','loss_checks','zero_J','zero_delta','fractional_delta','gate_equalities','accepted','rejected','false_accept_status','false_reject_status','ceiling_cases','quantization_cases','word_edit_pairs']}
def check(j,c,d,bj,bc,bd,delta):
    assert 0<=bc<=bj and 0<=bd<=bj
    assert max(abs(bj-j),abs(bc-c),abs(bd-d))<=delta
    G=bj>0 and 512*bd>=bj; H=1024*d>=j; B=j>0 and 256*d<j
    w1=max(1,ceil(1026*delta)); w2=max(1,ceil(513*delta))
    assert w1+w2<=1539*delta+2
    if G and not H: assert j<1026*delta and j<w1; stats['false_accept_status']+=1
    if not G and not B and j>0:
        assert (j<=delta if bj==0 else j<513*delta) and j<w2
        stats['false_reject_status']+=1
    qhat=bc/bj if G else F(0)
    if j and G and H: assert abs(qhat-F(c,j))<=8*delta/(j+1)
    for q in {F(0),F(1,3),F(1,2),F(1),F(c,j) if j else F(0),qhat}:
        rhs=(abs(F(c,j)-q) if j else 0)+8*delta*H/(j+1)+q*B+int(j<w1)+int(j<w2)
        assert abs(qhat-q)<=rhs, (j,c,d,bj,bc,bd,delta,q)
        # Both orientations produce precisely the same binary-TV loss.
        assert abs((1-qhat)-(1-q))==abs(qhat-q)
        stats['loss_checks']+=1
    stats['pathwise_cases']+=1; stats['zero_J']+=j==0; stats['zero_delta']+=delta==0
    stats['fractional_delta']+=delta.denominator!=1
    stats['gate_equalities']+=512*bd==bj
    stats['accepted' if G else 'rejected']+=1

# Sequential projection, including negative estimates and moving upper endpoints.
for j in range(7):
 for c,d in product(range(j+1),repeat=2):
  for e in map(F,[0,F(1,1026),F(1,2),1,3]):
   for a,b,f in product([-1,0,1],repeat=3):
    bj=clip(F(j)+a*e,F(0),F(6)); bc=clip(F(c)+b*e,F(0),bj); bd=clip(F(d)+f*e,F(0),bj)
    assert abs(bj-j)<=e and abs(bc-c)<=e and abs(bd-d)<=e
    stats['clipping_cases']+=1
    check(j,c,d,bj,bc,bd,e)
# Large integer counts near all three gate cutoffs, with tiny real deviations.
for j in [1,255,256,257,511,512,513,514,1023,1024,1025,1026,1027,2052]:
 for c in {0,j//2,j}:
  for d in {0,1,j//1024,j//512,j//256,min(j,j//256+1)}:
   for delta in {F(0),F(1,4096),F(1,1026),F(1,513),F(1,2),F(1),F(j,1026),F(j,513),F(j,2)}:
    for a,b,f in product([-1,0,1],repeat=3):
     bj=clip(F(j)+a*delta,F(0),F(4096)); bc=clip(F(c)+b*delta,F(0),bj); bd=clip(F(d)+f*delta,F(0),bj)
     check(j,c,d,bj,bc,bd,delta)
    # Exact acceptance equality and either strict side for real D.
    for eps in [F(-1,4096),F(0),F(1,4096)]:
     bj=F(j); bc=F(c); bd=clip(F(j,512)+eps,F(0),bj)
     check(j,c,d,bj,bc,bd,max(delta,abs(bd-d)))
# Integer strict-tail conversion at, below and above fractional boundary.
for scale in [513,1026]:
 for n in range(20):
  for eps in [F(-1,4096),F(0),F(1,4096),F(1,2)]:
   delta=max(F(0),(n+eps)/scale); w=max(1,ceil(scale*delta))
   for j in range(22):
    if j<scale*delta: assert j<w
    stats['ceiling_cases']+=1
# Exact nearest-grid quantization, deterministic lower tie rule.
for m in range(1,130):
 for h in range(9):
  scale=2**h
  for n in range(m+1):
   x=F(n,m); a=(x*scale).__floor__(); b=min(scale,a+1)
   rounded=F(a if x-F(a,scale)<=F(b,scale)-x else b,scale)
   assert abs(m*rounded-n)<=F(m,2*scale)
   assert 0<=rounded<=1 and 0<=rounded*scale<=scale
   assert scale.bit_length()==h+1
   stats['quantization_cases']+=1
# Exhaustive small-word single edits: endpoints fixed, all bank coordinates.
def bank(w):
 m=len(w)-2; out=[]
 for u in product([0,1],repeat=2):
  idx=[i for i in range(m) if tuple(w[i:i+2])==u]
  out += [len(idx),sum(w[i+2]==1-u[0] for i in idx),sum(i<m//2 for i in idx)]
 return out
for m in range(1,9):
 for w in product([0,1],repeat=m+2):
  b=bank(w)
  for i in range(m):
   z=list(w); z[i]^=1
   assert tuple(z[-2:])==w[-2:]
   assert max(abs(x-y) for x,y in zip(b,bank(z)))<=6
   stats['word_edit_pairs']+=1
assert 8*130944+16*(1026+513)==1072176
assert 6*1072176==6433056 and 1072176//2==536088
out={'status':'PASS','arithmetic':'fractions.Fraction exact rational; integer comparisons only','counts':stats,'limits':'Finite diagnostics only. No source-law probability theorem or all-real proof inferred from enumeration.'}
(BASE/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
