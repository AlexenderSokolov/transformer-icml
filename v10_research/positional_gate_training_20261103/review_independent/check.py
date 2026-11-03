"""Independent PGT001 diagnostics. No author-script imports or modifications."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import factorial,ceil
import hashlib,json
import mpmath as mp
mp.mp.dps=500
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
UNIT=HERE.parent
out={}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
bind=json.loads((UNIT/'SOURCE_BINDINGS.json').read_text())
for entry in bind['sources']:
 p=ROOT/entry['path']; assert digest(p)==entry['sha256']; assert p.stat().st_size==entry['bytes']
for name,entry in bind['artifacts'].items():
 p=UNIT/name; assert digest(p)==entry['sha256']; assert p.stat().st_size==entry['bytes']
cto=ROOT/'v10_research/clean_training_objective_20261103'
receipt=json.loads((cto/'ROOT_ACCEPTANCE.json').read_text())
assert receipt['candidate_sha256']==digest(cto/'CANDIDATE.md')
cb=json.loads((cto/'SOURCE_BINDINGS.json').read_text())
transitive=[]
for e in cb['sources']:
 if 'positional_manuscript_finite_20261102/' in e['path'] or e['path'].endswith('positional_finite_manuscript_root_acceptance.json'):
  assert digest(ROOT/e['path'])==e['sha256']; transitive.append(e['path'])
out['source_hashes']={'direct':len(bind['sources']),'author_artifacts':len(bind['artifacts']),'transitive':transitive}

def observation(word):
 n=len(word)-2; u=word[-2:]; visits=[i for i in range(n) if word[i:i+2]==u]
 j=len(visits); h=sum(word[i+2] for i in visits); first=sum(i<n//2 for i in visits)
 gate=j>0 and 512*first>=j; fallback=u[0]; bayes=Q(h+1,j+2)
 designated=1-fallback
 c=sum(word[i+2]==designated for i in visits)
 a=Q(c,j) if gate else Q(0)
 a1=a if designated==1 else 1-a
 return j,h,first,gate,fallback,bayes,a1,(bayes if gate else Q(fallback))
def mass(word):
 r=Q(1,4)
 for u in product((0,1),repeat=2):
  h=[sum(word[i:i+2]==u and word[i+2]==v for i in range(len(word)-2)) for v in (0,1)]
  r*=Q(factorial(h[0])*factorial(h[1]),factorial(sum(h)+1))
 return r
words=edits=0; populations=[]
for n in range(8):
 tot=0
 for w in product((0,1),repeat=n+2):
  j,h,d,g,f,b,a,bg=observation(w); prob=mass(w);tot+=prob;words+=1
  assert mass(w+(1,))==prob*b
  assert a==(Q(h,j) if g else f)
  assert abs(bg-a)<=(Q(1,j+2) if g else 0)
  assert Q(1,n+2)<=b<=Q(n+1,n+2)
  if n==7: populations.append((prob,g,abs(b-f)))
  if n<=5:
   for mask in product((0,1),repeat=n):
    z=tuple(v^mask[i] if i<n else v for i,v in enumerate(w)); k=sum(mask)
    jp,hp,dp,gp,fp,bp,ap,bgp=observation(z); edits+=1
    assert fp==f and max(abs(jp-j),abs(hp-h),abs(dp-d))<=6*k
    if k==0: assert abs(bgp-ap)<=Q(1,j+2)
    elif j>=12*k: assert jp>=Q(j,2) and abs(bgp-ap)<=2*Q(1,j+1)
    else: assert abs(bgp-ap)<=1
 assert tot==1
out['exact_words']=words;out['exact_legal_edits']=edits
count=0
for j in range(100):
 for denominator in range(2,40):
  for numerator in range(1,denominator):
   t=Q(numerator,denominator); x=1/t-1
   assert (Q(1,j+1)>t)==(j<ceil(x))
   assert 1<=ceil(x)<=1/t;count+=1
out['integer_layer_cake_cases']=count
# Exact identity, including both fallback orientations.
count=0
for den in range(2,23):
 for num in range(1,den):
  b=Q(num,den)
  for f in (0,1):
   for o in (Q(1,100),Q(1,2),Q(99,100)):
    q=o*b+(1-o)*f; dp=o*(1-o)*(b-f); d=abs(b-f)
    deriv=(q-b)*dp/(q*(1-q)); simple=-(1-o)**2*d/(1-o*d)
    assert deriv==simple and -1<simple<0; count+=1
out['exact_gradient_cases']=count
# True threshold word, equality accepted; symbol complement tests orientation.
boundaries=[]
for tail in (513,514):
 w=(0,0)+(1,)*(1024-tail)+(0,)*tail
 for complement in (0,1):
  z=tuple(v^complement for v in w);j,h,d,g,f,b,a,bg=observation(z)
  assert j==tail-1 and d==1 and g==(tail==513)
  boundaries.append({'J':j,'D':d,'F':f,'G':g})
out['actual_boundary_words']=boundaries
maxerr=mp.mpf(0);grid=0
for n in (64,65,1024,10**12):
 K=mp.log(n)/2;s=1/mp.sqrt(n)
 for gate in (0,1):
  for f in (0,1):
   for bprob in (mp.mpf(1)/(n+2),mp.mpf('0.4'),mp.mpf(n+1)/(n+2)):
    d=abs(bprob-f)
    def o(bias):return 1/(1+mp.exp(-bias-(2*gate-1)*K))
    def ce(bias):
     w=o(bias)
     return -d*mp.log(w*d)-(1-d)*mp.log1p(-w*d)
    for bias in (-60,-1,0,1,60):
     w=o(bias);deriv=-(1-w)**2*d/(1-w*d)
     err=abs(mp.diff(ce,bias)-deriv);maxerr=max(maxerr,err);assert err<mp.mpf('1e-75')
     eps=(1-w)*d; assert eps<=min(1,mp.exp(K-bias))
     if bias==0:
      q=w*bprob+(1-w)*f; eta=1/((mp.sqrt(n)+1)*(n+2))
      assert min(q,1-q)>=eta-mp.mpf('1e-100')
      assert abs(q-(bprob if gate else f))<=s/(1+s)
     grid+=1
out['high_precision']={'cases':grid,'digits':mp.mp.dps,'max_derivative_error':str(maxerr)}
# Independent exact-prior population M=7, stable scalar conditional loss.
K=mp.log(7)/2
rows=[(mp.mpf(p.numerator)/p.denominator,g,mp.mpf(d.numerator)/d.denominator) for p,g,d in populations]
def lg(b):
 loss=mp.mpf(0);grad=mp.mpf(0)
 for p,g,d in rows:
  o=1/(1+mp.exp(-b-(2*g-1)*K))
  loss+=p*(-d*mp.log(o*d)-(1-d)*mp.log1p(-o*d))
  grad-=p*(1-o)**2*d/(1-o*d)
 return loss,grad
runs=[]
for a in (mp.mpf('0.01'),mp.mpf('3'),mp.mpf('1000')):
 b=mp.mpf(0);initial=lg(b)[0]
 for t in range(30):
  old,grad=lg(b);new=b-a*grad;loss,_=lg(new)
  assert 0<new-b<a and loss<old;b=new
 runs.append({'step':str(a),'iterations':30,'final_bias':str(b),'initial_loss':str(initial),'final_loss':str(lg(b)[0])})
out['population_dynamics']={'M':7,'outside_theorem_range':True,'runs':runs}
out['status']='PASS'
(HERE/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
