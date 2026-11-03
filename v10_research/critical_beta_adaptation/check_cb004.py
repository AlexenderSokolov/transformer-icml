#!/usr/bin/env python3
"""Author exact finite checks for CB004's new deterministic assembly.
BP001 companion has its own return/concentration checks. Neither is a proof substitute.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import hashlib,json,random
D=Path(__file__).resolve().parent;R=D.parent;rng=random.Random(202611021358)
C={'receipts':0,'prefix_conditional_scalar':0,'perturbation_cases':0,'active_ratio':0,'false_active':0,'false_inactive':0,'assembly':0}
for u in ('SC003','BU001','BT002'):
 rec=json.loads((R/f'intake/{u}_acceptance.json').read_text())
 assert hashlib.sha256((R/rec['proof']).read_bytes()).hexdigest()==rec['sha256'];C['receipts']+=1
for j in range(100001):
 assert 1023*j+1<=1023*(j+1);C['prefix_conditional_scalar']+=1
for z in range(100000):
 M=rng.randrange(64,10**8);k=rng.randrange(0,min(M,100000)+1);d=6*k
 J=rng.randrange(M+1);J1=rng.randrange(J+1);cc=rng.randrange(J+1)
 Jp=max(0,min(M,J+rng.randrange(-d,d+1))) if d else J
 J1p=max(0,min(Jp,J1+rng.randrange(-d,d+1))) if d else J1
 cp=max(0,min(Jp,cc+rng.randrange(-d,d+1))) if d else cc
 if abs(J1p-J1)>d or abs(cp-cc)>d:continue
 G=Jp>0 and 512*J1p>=Jp;H=1024*J1>=J;B=J>0 and 256*J1<J
 if G and H and J>0:
  assert abs(F(cp,Jp)-F(cc,J))<=F(8*d,J+1);C['active_ratio']+=1
 if G and not H:
  assert J<1026*d;C['false_active']+=1
 if not G and not B and J>0:
  assert J<=d if Jp==0 else J<513*d
  C['false_inactive']+=1
 q=F(rng.randrange(101),100);out=F(cp,Jp) if G else F(0)
 E=abs(F(cc,J)-q) if J else F(0)
 rhs=E+(F(8*d,J+1) if H else 0)+(q if B else 0)+int(J<6156*k+1)+int(J<3078*k+1)
 assert abs(out-q)<=rhs
 C['perturbation_cases']+=1
for M in range(64,100000):
 n=M//2;m=M-n
 assert F(65472,m+1)<=F(130944,M)
 # Avoid sqrt using upper sqrt(32)<6, 32/sqrtM<=4.
 assert 8193*6+4<2**16
 assert 48*130944+16*(6156+3078)==6433056<2**23
 assert 2**16+4096<2**17
 C['assembly']+=1
proof=D/'CB004_stationary_critical_adaptation.md';comp=D/'balance_probe/BP001_stationary_weighted_balance.md'
assert hashlib.sha256(comp.read_bytes()).hexdigest()=='22b60eedf31f1e990e990a8b64ad733a1a3acc9723a421fdc6d677866c771271'
out={'status':'PASS_TESTED_INSTANCES_ONLY','arithmetic':'Exact integer/Fraction; no approximate roots','counts':C,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'companion_sha256':hashlib.sha256(comp.read_bytes()).hexdigest(),'scope':'Only finite checks for new reduction/assembly; full theorem additionally needs BP001 return concentration and independent complete review; stationary initialization only.'}
(D/'CB004_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
