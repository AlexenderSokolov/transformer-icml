from fractions import Fraction as F
from pathlib import Path
import math, random, hashlib, json, itertools
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent
r=random.Random(804711)
checks={}
n=0
for M in range(64,98):
 for p in range(4,10):
  D=2**p
  for C in range(M+1):
   a=F(D*C//M,D)
   for hc in range(4,p+1):
    Qc=2**hc
    coarse=F((Qc*a).__floor__(),Qc)
    assert coarse==F(Qc*C//M,Qc)
    assert 0<=a-coarse<F(1,Qc)
    assert ((a-coarse)*D).denominator==1
    for h in range(hc,p+1):
     Q=2**h
     assert F((Q*coarse).__floor__(),Q)==coarse
     fine=F((Q*a).__floor__(),Q)
     shift=coarse-fine
     assert (shift*Q).denominator==1
     assert 0<=-shift<F(1,Qc)
     assert 0<=a+shift<=1
     assert F((Q*(a+shift)).__floor__(),Q)==coarse
     n+=1
checks['exact_finite_nested_coarsening_cases']=n
n=0
for _ in range(35000):
 C=F(r.randrange(100),r.randrange(1,9)); other=F(r.randrange(100),r.randrange(1,9)); J=C+other
 Cp=F(r.randrange(100),r.randrange(1,9)); op=F(r.randrange(100),r.randrange(1,9)); Jp=Cp+op
 B=abs(Cp-C)+abs(op-other)+F(r.randrange(5),7)
 q=F(r.randrange(65),64)
 est=max(Cp-B,0)/(Jp+B+2)
 assert 0<=est<=C/(J+2)<=1
 assert C/(J+2)-est<=4*B/(J+2)
 A=4*B+2
 if J:
  assert abs(est-q)<=2*abs(C/J-q)+min(q,A/(J+2))
 else: assert abs(est-q)<=min(q,A/(J+2))
 n+=1
checks['exact_fractional_binary_envelope_cases']=n
n=0
for K in range(2,8):
 for _ in range(1500):
  u=[F(r.randrange(50),r.randrange(1,10))+1 for _ in range(K)]
  v=[F(r.randrange(50),r.randrange(1,10))+1 for _ in range(K)]
  A=sum(u); B=sum(v)
  tv=sum(abs(x/A-y/B) for x,y in zip(u,v))/2
  assert tv<=min(1,sum(abs(x-y) for x,y in zip(u,v))/A)
  n+=1
checks['exact_addone_stability_cases']=n
n=0
M=6
words=list(itertools.product(range(2),repeat=M+2))
def hist(w):
 c=[0]*8
 for j in range(M): c[4*w[j]+2*w[j+1]+w[j+2]]+=1
 return c
for w in words:
 c=hist(w)
 for bits in itertools.product(range(2),repeat=M):
  v=bits+w[-2:]; k=sum(a!=b for a,b in zip(w,v)); cp=hist(v)
  assert sum(abs(a-b) for a,b in zip(c,cp))<=6*k
  n+=1
checks['exact_symbol_edit_histogram_cases_small_M']=n
n=0
for _ in range(30000):
 M=2**r.uniform(6,45); e=2**r.uniform(-math.log2(M),0)
 def f(x): return 0 if not x else x*(1+math.log1p(1/(M*e*x)))
 x,y,z=[2**r.uniform(-60,1) for j in range(3)]
 assert f(x+y+z)<=f(x)+f(y)+f(z)+1e-12
 assert f(x+y+z)<=3*max(f(x),f(y),f(z))+1e-12
 assert f(2/M)<=8/math.sqrt(M)+1e-12
 delta=2**r.uniform(-30,-2); Q=2**r.randrange(4,35)
 if delta>=1/Q:
  Qc=max(16,2**math.ceil(math.log2(1/delta)))
  assert Qc<=Q and 1/Qc<=delta+1e-15
  assert f(delta)<=4*f(1/Qc)+1e-12
 n+=1
checks['floating_scalar_corrob_cases_not_proof']=n
bindings={}
for unit in ['SC002','SC003','BT002','BS001','BF001','BIF001','BC001','IU001','AU001']:
 receipt=ROOT/'intake'/f'{unit}_acceptance.json'
 obj=json.loads(receipt.read_text()); p=ROOT/obj['proof']; sha=hashlib.sha256(p.read_bytes()).hexdigest()
 assert sha==obj['sha256'],unit
 bindings[str(p.relative_to(ROOT))]=sha
 bindings[str(receipt.relative_to(ROOT))]=hashlib.sha256(receipt.read_bytes()).hexdigest()
checks['accepted_dependency_sha256_matches']=9
result={'status':'PASS','checks':checks,'scope':'Exact finite identities/pathwise algebra plus sampled floating scalar corroboration; not universal theorem proof or formal verification. Small M edit tests are algebra only, outside risk theorem domain.','reviewed_proof_sha256':hashlib.sha256((BASE/'JP001_theorem.md').read_bytes()).hexdigest(),'source_bindings':bindings}
(BASE/'JP001_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='source_bindings'},indent=2))
