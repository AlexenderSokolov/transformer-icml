"""PGT001 exact/high-precision diagnostics. Not proofs of stochastic inputs."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product, combinations
from math import factorial
import hashlib, json
import mpmath as mp
mp.mp.dps=80
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent

def stats(w):
    M=len(w)-2; u=w[-2:]; inds=[i for i in range(M) if w[i:i+2]==u]
    J=len(inds); H=sum(w[i+2] for i in inds); D=sum(i<M//2 for i in inds)
    G=int(J>0 and 512*D>=J); F=u[0]; B=Q(H+1,J+2)
    A=Q(H,J) if G else Q(F); BG=B if G else Q(F)
    return J,H,D,G,F,B,A,BG

def mass(w):
    M=len(w)-2; ans=Q(1,4)
    for u in product((0,1),repeat=2):
        hs=[sum(w[i:i+2]==u and w[i+2]==c for i in range(M)) for c in (0,1)]
        ans*=Q(factorial(hs[0])*factorial(hs[1]),factorial(sum(hs)+1))
    return ans

checks={}; nwords=nedits=0
for M in range(9):
    total=Q(0)
    for w in product((0,1),repeat=M+2):
        nwords+=1; J,H,D,G,F,B,A,BG=stats(w); m=mass(w); total+=m
        assert Q(1,M+2)<=B<=1-Q(1,M+2)
        assert mass(w+(1,))==m*B
        assert abs(BG-A)<=Q(1,J+2)
        if M<=6:
            for mask in product((0,1),repeat=M):
                z=tuple(w[i]^mask[i] if i<M else w[i] for i in range(M+2))
                k=sum(mask); jp,hp,dp,gp,fp,bp,ap,bgp=stats(z); nedits+=1
                assert fp==F and abs(jp-J)<=6*k and abs(hp-H)<=6*k and abs(dp-D)<=6*k
                if k==0: assert abs(bgp-ap)<=Q(1,J+2)
                else:
                    assert abs(bgp-ap)<=2*Q(1,J+1)+int(J<12*k)
                    if J>=12*k: assert jp*2>=J and Q(1,jp+2)<=2*Q(1,J+1)
    assert total==1
checks['exact_word_posterior_and_orientation']={'words':nwords,'horizons':'0..8','mass_total':'1 at each horizon'}
checks['exhaustive_legal_edit_comparisons']={'pairs':nedits,'horizons':'0..6','all_edit_masks':True}

targeted=[]
for tail,expected_j,expected_g in [(513,512,1),(514,513,0)]:
 w=(0,0)+(1,)*(1024-tail)+(0,)*tail
 assert len(w)==1026
 for complement in (False,True):
  z=tuple(1-x for x in w) if complement else w
  J,H,D,G,F,B,A,BG=stats(z)
  assert (J,D,G)==(expected_j,1,expected_g)
  assert abs(BG-A)<=Q(1,J+2)
  targeted.append({'M':1024,'J':J,'D':D,'G':G,'F':F})
for w in [(0,)*66,(1,)*66,(0,1)*33,(1,)*64+(0,0),(0,)*64+(1,1)]:
 J,H,D,G,F,B,A,BG=stats(w)
 for k in [0,1,5,6,16,64]:
  z=tuple(1-x if i<k else x for i,x in enumerate(w))
  jp,hp,dp,gp,fp,bp,ap,bgp=stats(z)
  assert fp==F and abs(jp-J)<=6*k
  assert abs(bgp-ap)<=Q(1,J+2) if k==0 else abs(bgp-ap)<=2*Q(1,J+1)+int(J<12*k)
  if k and J>=12*k: assert jp*2>=J
 targeted.append({'M':64,'J':J,'D':D,'G':G,'F':F})
checks['actual_word_boundary_cases']=targeted

n=0
for j in range(30):
 for t in [Q(i,97) for i in range(1,97)]:
    x=1/t-1; ceilx=(x.numerator+x.denominator-1)//x.denominator
    assert (Q(1,j+1)>t)==(j<ceilx)
    assert 1<=ceilx<=1/t
    n+=1
checks['integer_layer_cake_boundaries']=n

n=0
for B in [Q(1,66),Q(1,5),Q(1,2),Q(4,5),Q(65,66)]:
 for F in (0,1):
  d=abs(B-F)
  for o in [Q(1,1000),Q(1,9),Q(1,2),Q(8,9),Q(999,1000)]:
    q=o*B+(1-o)*F; qp=o*(1-o)*(B-F)
    chain=(q-B)*qp/(q*(1-q))
    raw=-o*(1-o)**2*(B-F)**2/(q*(1-q))
    simple=-(1-o)**2*d/(1-o*d)
    assert chain==raw==simple and -1<simple<0
    n+=1
checks['exact_conditional_gradient_identities']=n

errors=[]; grid=0
for M in [64,65,512,1000000]:
 K=mp.log(M)/2
 for G in (0,1):
  for F in (0,1):
   for B in [mp.mpf(1)/(M+2),mp.mpf('.5'),1-mp.mpf(1)/(M+2)]:
    def o(b):return 1/(1+mp.exp(-b-(2*G-1)*K))
    def q(b):return o(b)*B+(1-o(b))*F
    def ce(b):return -B*mp.log(q(b))-(1-B)*mp.log(1-q(b))
    for b in map(mp.mpf,[-40,-3,0,4,40]):
     d=abs(B-F); grad=-(1-o(b))**2*d/(1-o(b)*d)
     err=abs(mp.diff(ce,b)-grad); errors.append(err)
     assert err<mp.mpf('1e-55')
     assert abs(q(b)-B)<=mp.exp(K-b)+mp.mpf('1e-70')
     if b==0:
      BG=B if G else F
      s=1/mp.sqrt(M)
      assert abs(q(b)-BG)<=s/(1+s)+mp.mpf('1e-70')
      eta=1/((mp.sqrt(M)+1)*(M+2))
      assert min(q(b),1-q(b))>=eta-mp.mpf('1e-70')
     grid+=1
checks['high_precision_conditional_grid']={'cases':grid,'decimal_digits':80,'max_derivative_error':str(max(errors)),'tolerance':'1e-55'}

# Small-horizon exact word distribution plus high-precision gradient dynamics.
# M=6 is an algebra/algorithm diagnostic, outside the theorem M>=64 range.
M=6; K=mp.log(M)/2; rows=[]
for w in product((0,1),repeat=M+2):
 J,H,D,G,F,B,A,BG=stats(w); pm=mass(w)
 rows.append((mp.mpf(pm.numerator)/pm.denominator,G,F,mp.mpf(B.numerator)/B.denominator))
def lossgrad(b):
 loss=mp.mpf(0); grad=mp.mpf(0)
 for p,G,F,B in rows:
  o=1/(1+mp.exp(-b-(2*G-1)*K)); q=o*B+(1-o)*F; d=abs(B-F)
  loss+=p*(-B*mp.log(q)-(1-B)*mp.log(1-q))
  grad-=p*(1-o)**2*d/(1-o*d)
 return loss,grad
runs=[]
for step in [mp.mpf(1),mp.mpf(100)]:
 b=mp.mpf(0); initial=lossgrad(b)[0]
 for t in range(100):
  l,g=lossgrad(b); bn=b-step*g; ln,gn=lossgrad(bn)
  assert bn>b and ln<l and 0<bn-b<step
  b=bn
 runs.append({'step':str(step),'steps':100,'b_final':str(b),'initial_loss':str(initial),'final_loss':str(lossgrad(b)[0])})
checks['finite_population_dynamics_diagnostic']={'M':M,'caveat':'outside theorem horizon; exact word masses, 80-digit arithmetic; no convergence or rate inferred','runs':runs}

cto=ROOT/'v10_research/clean_training_objective_20261103'
accept=json.loads((cto/'ROOT_ACCEPTANCE.json').read_text())
assert hashlib.sha256((cto/'CANDIDATE.md').read_bytes()).hexdigest()==accept['candidate_sha256']
checks['accepted_CTO001_hash']=accept['candidate_sha256']
# Verify imported source gates independently against their recorded hashes.
cb=json.loads((cto/'SOURCE_BINDINGS.json').read_text())
verified=[]
for entry in cb['sources']:
 if 'positional_manuscript_finite_20261102/' in entry['path'] or entry['path'].endswith('positional_finite_manuscript_root_acceptance.json'):
  p=ROOT/entry['path']; assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256']; verified.append(entry['path'])
checks['imported_source_hashes_verified']=verified
checks['status']='ALL_DIAGNOSTICS_PASS'
(HERE/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
