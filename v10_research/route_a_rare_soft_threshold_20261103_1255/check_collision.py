#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json
out=Path(__file__).with_name('cases.jsonl')
def counts(seq):
 assert seq[-2:]=='00'; h=[(seq[i-2:i],int(seq[i])) for i in range(2,len(seq))]
 return len(h),sum(s=='00' for s,y in h),sum(y for s,y in h if s=='00'),sum(y for s,y in h)
with out.open('x') as f:
 z=0
 for n in range(1,9):
  for k in range(9):
   a='00'+'010100'*n+'10'+'10'*k+'0'
   for d in range(1,n+1):
    b='00'+'100100'*d+'010100'*(n-d)+'10'+'10'*k+'0'
    m,J,C1,T=counts(a);m2,J2,C2,T2=counts(b)
    assert (m,J,C1,T)==(6*n+3+2*k,2*n+1,n+1,2*n+k+1)
    assert (m2,J2,C2,T2)==(m,J,n+d+1,T)
    for g in (F(1,2),F(1),F(3)):
     q1=F(T+g*C1,m+g*J);q2=F(T+g*C2,m+g*J)
     p1=F(C1+1,J+2);p2=F(C2+1,J+2)
     e=(q2-q1)/2;hard=(p2-p1)/2
     assert e==g*d/(2*(m+g*J)) and hard==F(d,2*(J+2))
     row={'n':n,'k':k,'d':d,'gamma':str(g),'word1':a,'word2':b,'m':m,'J':J,'C1':C1,'C2':C2,'pooled_ones':T,'q1':str(q1),'q2':str(q2),'collision_radius':str(e),'minimax_fidelity_lower':str(hard)}
     f.write(json.dumps(row)+'\n');z+=1
print('PASS',z,'rational cases, all records retained')
