#!/usr/bin/env python3
# Deterministic rational enumeration; output new records exclusively.
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
out=Path(__file__).with_name('exact_cases.jsonl')

def lin(f,x,K):
    if x==1:return f(F(1))
    i=(x*K).__floor__(); a=F(i,K); z=x*K-i
    return f(a)*(1-z)+f(a+F(1,K))*z

def mul(x,y,K):
    s=lambda a:lin(lambda b:b*b,a,K)
    return 2*(s((x+y)/2)-s(x/2)-s(y/2))

def clamp(x,a,b):return max(a,min(b,x))
num=0; zero=0; nonzero=0; worst=F(0)
with out.open('x') as f:
 for N in range(3,10):
  m=N-2
  for word in product((0,1), repeat=N):
   s=tuple(word[-2:]); pairs=[tuple(word[i-2:i]) for i in range(2,N)]
   succ=word[2:]; J=sum(p==s for p in pairs); C=sum((p==s)*v for p,v in zip(pairs,succ)); total=sum(succ)
   q=F(total+C,m+J); r=F(total,m); h=F(J,m); p=F(C+1,J+2)
   assert (m*((1+h)*q-r)+1)/(m*h+2)==p
   zero+=J==0;nonzero+=J>0
   for K in (1,2,3,4,8):
    A=clamp(q-r+mul(h,q,K),F(0),h)
    z=F(m*A+1,m+2)
    R=lin(lambda x:1/(1+F(m,2)*x),h,K)
    pred=clamp(F(m+2,2)*mul(z,R,K),F(0),F(1))
    bound=F(m,2+J)*F(3,2*K*K)+F(m+2,2)*(F(3,2)+F(m*m,16))/(K*K)
    err=abs(pred-p); assert err<=bound,(N,word,K,err,bound)
    num+=1;worst=max(worst,err)
    f.write(json.dumps({'N':N,'word':''.join(map(str,word)),'J':J,'C':C,'K':K,'error':str(err),'upper':str(bound)})+'\n')
print('records',num,'zero_J',zero,'positive_J',nonzero,'max_error',str(worst));print('PASS')
