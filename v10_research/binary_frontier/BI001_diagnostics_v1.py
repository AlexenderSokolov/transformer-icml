"""Finite diagnostics only; not a proof, model check, or independent review."""
import numpy as np, json, math, hashlib
from pathlib import Path
out={}; residual=0.; cert=1.; atom=1.; terminal=1.
for M in [64,65,128,1000,1000000]:
 for beta in [0,1/M**2,1e-10,1e-6,1/256]:
  for p in np.linspace(.25,.75,101):
   a=1/(2*M);e=max(math.sqrt(beta),1/M);x=1/(e/a+2+2*p)
   pi=np.array([x*e/a,x,x,2*p*x])
   P=np.array([[1-a,a,0,0],[0,0,1-p,p],[e,1-e,0,0],[0,0,.5,.5]])
   residual=max(residual,abs(pi@P-pi).max(),abs(pi.sum()-1))
   cert=min(cert,(P@P-beta*pi).min())
   R=np.array([[0,1-p,p],[1,0,0],[0,.5,.5]])
   atom=min(atom,(R@R)[:,1].min());terminal=min(terminal,(R@R@R)[:,0].min())
out.update(stationarity_max_residual=float(residual),certificate_min_slack=float(cert),R2_common_B_min=float(atom),R3_terminal_A_min=float(terminal))
harm=1.
for J in range(4,300):
 for u in np.geomspace(1e-6,.25,200):
  h=sum(1/(1+u*j) for j in range(4,J+1))
  harm=min(harm,8*u*h/math.log1p(u*J))
out['harmonic_claim_min_ratio']=harm
# Exact path enumeration with arbitrary positional binary-window tables.
rng=np.random.default_rng(99431); worstvar=0.;worstder=0.
for j in range(4,13):
 for r in [1,2,3]:
  tab=rng.uniform(-1,1,size=(j,2**r))
  def moments(p):
   paths=[('1',0,1.)]
   for k in range(j-1):
    new=[]
    for bits,s,w in paths:
     for t,pr in enumerate([[0,1-p,p],[1,0,0],[0,.5,.5]][s]):
      if pr:new.append((bits+('1' if t in [0,2] else '0'),t,w*pr))
    paths=new
   ef=ef2=0.
   for bits,s,w in paths:
    f=sum(tab[k,int(('0'*r+bits[:k+1])[-r:],2)] for k in range(j))
    ef+=w*f;ef2+=w*f*f
   return ef,ef2-ef*ef
  for p in [.25,.4,.5,.6,.75]:
   mu,var=moments(p);h=1e-6;der=(moments(p+h)[0]-moments(p-h)[0])/(2*h)
   worstvar=max(worstvar,var/((34*r)**2*j));worstder=max(worstder,abs(der)/(34*r*j))
out.update(local_sum_variance_bound_max_ratio=worstvar,local_sum_derivative_bound_max_ratio=worstder)
base=Path(__file__).resolve().parent
out['evidence_status']='Author finite diagnostics; proof still requires independent audit.'
(base/'BI001_diagnostics_v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
