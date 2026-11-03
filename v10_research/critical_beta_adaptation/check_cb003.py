#!/usr/bin/env python3
"""Finite exact author diagnostics for CB003; not universal proof."""
from pathlib import Path
from math import isqrt
from fractions import Fraction as F
from collections import Counter
import hashlib,json
D=Path(__file__).resolve().parent
C={'large_domain_exact_words':0,'small_local_count_checks':0,'null_certificates':0}
def counts(s):
 J=sum(s[i:i+2]==b'00' for i in range(len(s)-2))
 c=sum(s[i:i+3]==b'001' for i in range(len(s)-2))
 return c,J
# Exact local identities across a wide smaller domain, without claiming finite theorem threshold.
for h in (1,2,3,5,8,16):
 for k in (4*(h+1),8*(h+1),64*h):
  l=k//4
  for t in (k,2*k,4*k):
   M=16*t;n=M//2
   s=bytearray(b'1'*(M+1-t)+b'0'*(t+1));z=bytearray(s)
   z[2:h+3]=b'0'*(h+1)
   start=M+1-t
   for j in range(1,l+1):z[start+3*j-1]=ord('1')
   c,J=counts(z)
   assert (c,J)==(l+1,t-1-2*l+h)
   assert z[:n+1].count(ord('0'))==h+1 and z[-2:]==b'00'
   assert sum(a!=b for a,b in zip(s,z))==h+1+l<=k
   C['small_local_count_checks']+=1
for M in (2**20,2**22):
 h=isqrt(M)+(isqrt(M)**2<M);T=M//8;n=M//2
 for k in sorted(set((64*h,T//2,T))):
  if not 64*h<=k<=T:continue
  l=k//4
  for t in sorted(set((k,(k+T)//2,T))):
   s=bytearray(b'1'*(M+1-t)+b'0'*(t+1));z=bytearray(s)
   z[2:h+3]=b'0'*(h+1);start=M+1-t
   for j in range(1,l+1):z[start+3*j-1]=49
   c,J=counts(z)
   assert (c,J)==(l+1,t-1-2*l+h)
   assert c>12*h and J>0
   assert F(c,J)-F(1,2*M)>=F(k,16*t)
   assert z[:n+1].count(48)==h+1 and z[-2:]==b'00'
   assert sum(a!=b for a,b in zip(s,z))==h+1+l<=k
   C['large_domain_exact_words']+=1
for M in (64,128,256,1024):
 r=F(1,2*M);T=[[1-r,r],[r,1-r]];pi={(i,j):T[i][j]/2 for i in range(2) for j in range(2)}
 for u in range(2):
  for v in range(2):
   for s in range(2):
    for z in range(2):assert T[v][s]*T[s][z]>=2*r*pi[s,z]
 assert (r/2)*(1-r)**M>=F(1,8*M)
 C['null_certificates']+=1
p=D/'CB003_fixed_veto_bypass.md'
out={'status':'PASS_TESTED_INSTANCES_ONLY','arithmetic':'exact binary words, integers and Fraction','counts':C,'proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Only W(AB003) failure; not unrestricted critical-curve impossibility.'}
(D/'CB003_author_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
