from fractions import Fraction as F
from pathlib import Path
import json,hashlib,itertools
import mpmath as mp
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
P=OUT.parent
mp.mp.dps=120
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='437d945df88004758d4153385fd00699dd33ea5bee378a4e2aebbf797a9fc642'
assert sha(P/'CANDIDATE.md')==expected
bindings=json.loads((P/'SOURCE_BINDINGS.json').read_text())
for v in bindings['sources']:
 p=ROOT/v['path']; assert sha(p)==v['sha256'] and p.stat().st_size==v['bytes']
CH=2**17+2**23+208; D=CH+1;c0=F(1,96);cB=F(1,2**30);T=2*D/cB;c=min(c0/(1+T),cB/4)
count=0
vals=[F(i,8) for i in range(9)]
for B,Fall,G,w0,w1,p in itertools.product(vals,[F(0),F(1)],[0,1],vals,vals,vals):
 H=G*B+(1-G)*Fall; w=w1 if G else w0;q=w*B+(1-w)*Fall
 rem=(1-w1)*G*(Fall-B)
 assert q==w0*B+(1-w0)*H+rem
 assert abs(rem)<=1-w1
 assert abs(q-p)<=w0*abs(B-p)+(1-w0)*abs(H-p)+abs(rem)
 assert abs(q-p)>=w0*abs(B-p)-(1-w0)*abs(H-p)-abs(rem)
 count+=1
# Exact pointwise derivative of conditional CE(B,q), without logs.
derivative=0
for B,Fall,w in itertools.product(vals[1:-1],[F(0),F(1)],vals[1:-1]):
 q=w*B+(1-w)*Fall; qp=w*(1-w)*(B-Fall);d=abs(B-Fall)
 grad=(q-B)*qp/(q*(1-q)); reduced=-(1-w)**2*d/(1-w*d)
 assert grad==reduced and -1<grad<0
 derivative+=1
# Abstract experiment arrays with different maximizers and different denominators.
# They exercise the risk supremum operation; they are not source witnesses.
suprema=0
for w0,w1 in itertools.product(vals,vals):
 experiments=[(F(1,8),F(1),F(0),0,F(1)),(F(1,4),F(0),F(1),1,F(0)),(F(1,2),F(3,8),F(0),1,F(7,8))]
 rb=[];rh=[];rq=[];re=[]
 for g,B,Fall,G,p in experiments:
  H=G*B+(1-G)*Fall;w=w1 if G else w0;q=w*B+(1-w)*Fall
  rb.append(abs(B-p)/g);rh.append(abs(H-p)/g);rq.append(abs(q-p)/g);re.append(abs((1-w1)*G*(Fall-B))/g)
 assert max(rq)<=w0*max(rb)+(1-w0)*max(rh)+max(re)
 assert max(rq)>=w0*max(rb)-(1-w0)*max(rh)-max(re)
 suprema+=1
factor=0
for x in [F(0),F(1,100),F(1),T-F(1),T,T+1,2*T,10*T,F(10**40)]:
 lo=max(c0,cB*x-D); hi=D+944*x
 assert c*(1+x)<=lo<=hi<=D*(1+x)
 factor+=1
# High-precision tests deliberately include huge horizons so binary floats cannot
# silently saturate sigmoid and turn the finite-bias family into its limit.
sig=lambda z: 1/(1+mp.exp(-z))
rows=[];hp=0
for M in [64,65,100,256,10**6,10**12,10**100,10**1000]:
 m=mp.mpf(M);ell=1+mp.log((m+2)/2);K=mp.log(m)/2;cap=K-mp.log(ell);s=1/mp.sqrt(m)
 assert cap>0 and mp.sqrt(m)>ell
 assert abs(ell*sig(cap-K)-ell/(1+ell))<mp.mpf('1e-110')
 assert ell/(1+ell)<1
 for b in [mp.mpf(0),cap/2,cap,cap+1,K,K+mp.log(ell),K+100]:
  w0=sig(b-K);w1=sig(b+K);x=ell*w0
  # For very large positive logits test complement in stable form.
  complement=sig(-b-K)
  assert complement<=s*mp.exp(-b)*(1+mp.mpf('1e-115'))
  assert 560+192*(1+mp.log(m))<=944*ell
  if b<=cap:assert x<1
  for Fall,B in [(mp.mpf(0),mp.mpf('0.25')),(mp.mpf(1),mp.mpf('0.75'))]:
   for G in [0,1]:
    z=b+(K if G else -K);w=sig(z);u=sig(-z);d=abs(B-Fall)
    # Stable expression for the CE derivative, strictly negative at finite bias.
    grad=-u*u*d/(1-w*d)
    assert -1<grad<0
  hp+=1
 rows.append({'M':str(M),'cap':mp.nstr(cap,35),'x_at_cap':mp.nstr(ell/(1+ell),35)})
report={'status':'PASS','candidate_sha256':expected,'source_bindings_sha256':sha(P/'SOURCE_BINDINGS.json'),'source_bindings_verified':len(bindings['sources']),'exact_mixture_loss_cases':count,'exact_conditional_derivative_cases':derivative,'exact_supremum_cases':suprema,'exact_factor_cases':factor,'high_precision_bias_cases':hp,'decimal_precision':mp.mp.dps,'CH':CH,'D':D,'c':str(c),'T':str(T),'horizons':rows,'limitations':'Finite algebraic diagnostics, not proof of imported stochastic results; no empirical population training or numerical minimax validation.'}
(OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
