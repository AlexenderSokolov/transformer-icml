"""Finite exact corroboration only; does not prove the universal theorem."""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json, math, hashlib, random
out={}; checks=0
# Exact nested floors and legal coarse-noise shifts for arbitrary evaluator P>=h.
for M in [2,3,7,16,31,64,65,127,256]:
 for h in range(4,9):
  Q=2**h
  for P in [h,h+1,h+5]:
   D=2**P
   for hc in range(4,h+1):
    Qc=2**hc
    for C in range(M+1):
     a=F(D*C//M,D); coarse=F((Qc*a).__floor__(),Qc)
     assert coarse==F(Qc*C//M,Qc)
     assert F((Q*coarse).__floor__(),Q)==coarse
     assert 0<=a-coarse<F(1,Qc)
     assert ((a-coarse)*D).denominator==1
     fine=F((Q*a).__floor__(),Q); eta=coarse-fine
     assert (eta*Q).denominator==1 and abs(eta)<F(1,Qc)
     assert 0<=a+eta<=1 and F((Q*(a+eta)).__floor__(),Q)==coarse
     checks+=1
out['nested_floor_exact_checks']=checks
# Entire histogram Hamming edits, including adjacent positions, terminal protected.
def hist(word,K):
 c=[0]*(K**3)
 for a,b,d in zip(word,word[1:],word[2:]):c[(a*K+b)*K+d]+=1
 return c
checks=0
for K,M in [(2,5),(3,3)]:
 for word in product(range(K),repeat=M+2):
  c=hist(word,K)
  for k in range(3):
   for inds in combinations(range(M),k):
    for vals in product(range(K),repeat=k):
     changed=list(word)
     for i,x in zip(inds,vals):changed[i]=x
     cp=hist(changed,K)
     assert sum(abs(x-y) for x,y in zip(c,cp))<=6*k
     assert tuple(changed[-2:])==word[-2:]
     checks+=1
out['edit_histogram_checks']=checks
# Real/rational pseudo-count robust binary envelope, adversarial positive false counts.
r=random.Random(310011);checks=0
for _ in range(60000):
 J=r.randrange(101); C=r.randrange(J+1)
 u=F(r.randrange(501),r.randrange(1,15)); v=F(r.randrange(501),r.randrange(1,15))
 B=abs(u-C)+abs(v-(J-C))+F(r.randrange(9),7)
 n=max(u-B,0); qhat=n/(u+v+B+2); A=4*B+2
 assert 0<=qhat<=F(C,J+2)
 assert F(C,J+2)-qhat<=4*B/(J+2)
 for q in [F(0),F(1),F(r.randrange(101),100)]:
  rhs=(2*abs(F(C,J)-q) if J else 0)+min(q,A/(J+2))
  assert abs(qhat-q)<=rhs
 checks+=1
out['rational_lower_envelope_checks']=checks
# Clip and floor upper error is exact with rational perturbations, including saturation.
checks=0
for M in [3,64,127]:
 for Q,D in [(16,16),(16,256),(64,128)]:
  for C in range(M+1):
   a=F(D*C//M,D)
   for eta in [F(-1,4),F(-1,16),F(0),F(1,64),F(1,4)]:
    z=F((Q*min(1,max(0,a+eta))).__floor__(),Q)
    assert abs(z-F(C,M))<=abs(eta)+F(1,D)+F(1,Q)
    checks+=1
out['clipping_bound_checks']=checks
# Floating corroboration of scalar completion over endpoints/log-spaced domains.
checks=0; worst=0
for M in [64,65,128,1024,10**6,10**12]:
 for e in [1/M,1/math.sqrt(M),.125,1]:
  e=max(e,1/M)
  def f(x):return x*(1+math.log1p(1/(M*e*x))) if x else 0
  assert f(2/M)<=8/math.sqrt(M)
  for k in [0,1,int(math.sqrt(M)),M]:
   for Q in [16,64,2**20,2**50]:
    for delta in [0,1/(2*Q),1/Q,1/16,1/4]:
     x,y,z=k/M,delta,1/Q
     assert f(x+y+z)<=f(x)+f(y)+f(z)+1e-12
     if delta>=1/Q:
      Qc=max(16,2**math.ceil(math.log2(1/delta)))
      assert Qc<=Q and Q%Qc==0 and 1/Qc<=delta
      assert f(delta)<=4*f(1/Qc)+1e-12
     checks+=1
out['scalar_float_checks']=checks
out['status']='PASS_FINITE_CORROBORATION_NOT_PROOF'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
