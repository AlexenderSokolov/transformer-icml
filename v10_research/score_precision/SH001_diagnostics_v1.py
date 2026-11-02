#!/usr/bin/env python3
"""Finite scalar corroboration, not a proof or emitted-network execution."""
import math,json,hashlib,pathlib
base=pathlib.Path(__file__).resolve().parents[1]
counts={"cutoff_harmonic":0,"tube_mesh":0,"necessity_large_f":0,"upper_selection":0}
mins={"harmonic_ratio":float('inf'),"event_ratio":float('inf')}
for M in [64,65,127,256,1024,4096]:
 for beta in [0,1/(2*M),1/M,min(2/M,1/16),1/32,1/16]:
  b0=max(beta,1/M)
  for z in [1,1.01,2,math.sqrt(M),M/8,M/4]:
   if z>M/4: continue
   U=min(1/(4*b0),M*M/(4*z*z)); J=math.floor(U); u=z/M
   assert J>=4 and J>=U/2 and J<=M/4 and b0*J<=.25+1e-14
   assert z*math.sqrt(J)/M<=.5+1e-14
   assert u*J+1e-14>=min(z/(M*b0),M/z)/8
   s=sum(1/(1+u*j) for j in range(2,J+1)); target=math.log1p(u*J)/(4*u)
   assert s+1e-13>=target
   mins['harmonic_ratio']=min(mins['harmonic_ratio'],s/target)
   alpha=1/(2*M); eta=b0-alpha
   for j in [2,J]:
    e=(1-alpha/b0)*(1-alpha)*alpha*(1-alpha)**(M-j)*(1-eta)**(j-1)
    assert e>=1/(32*M)-1e-15
    mins['event_ratio']=min(mins['event_ratio'],e*32*M)
   counts['cutoff_harmonic']+=1
   for kappa in [1,1.01,1.5,2,math.pi,10,z]:
    Q=z/kappa
    if Q<1: continue
    for D,r in [(1,1),(2,3),(27,3)]:
     H=3**(2*r); t0=r*math.sqrt(40*D*H); c0=4*t0
     assert Q*2*kappa*t0*math.sqrt(J)/M<=t0+1e-9
     mesh=math.ceil(2*r*z*J/M)+1
     assert mesh<=(2+4*r)*(1+z*J/M)+1e-9
     counts['tube_mesh']+=1
for cp in [.01,.1,1,2,10,100]:
 F=max(2*(1+math.log(8)),16,8*math.log(max(math.e,16*cp*cp)))
 for f in [F+i/10 for i in range(2000)]:
  x=math.expm1(f-1)
  assert math.log1p(x/(8*cp*cp*f))>=f/2-1e-12
  assert math.log1p(x/8)>=f/2-1e-12
  counts['necessity_large_f']+=1
for x in [0,1e-12,.01,1,10,1e3,1e10,1e100]:
 f=1+math.log1p(x); k=math.ceil(f)
 assert f<=k<=2*f
 assert (1+math.log1p(k*x))/k<=2+1e-14
 counts['upper_selection']+=1
out={'status':'PASS','scope':'Finite scalar checks only; analytic theorem not certified by tests','counts':counts,'minimum_ratios':mins}
(base/'score_precision/SH001_diagnostics_v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
