from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,sys

def spline(x,k,kind,m):
    if x == 1: j=k-1
    else: j=(x*k).numerator//(x*k).denominator
    a,b=F(j,k),F(j+1,k)
    def f(z): return z*z if kind=='square' else 1/(1+F(m,2)*z)
    return f(a)+(f(b)-f(a))*(x-a)*k

def prod(x,y,k,m):
    return 2*(spline((x+y)/2,k,'square',m)-spline(x/2,k,'square',m)-spline(y/2,k,'square',m))
def clip(x,l,h): return max(F(l),min(F(h),x))
def enc(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,tuple): return [enc(x) for x in v]
    if isinstance(v,dict): return {k:enc(x) for k,x in v.items()}
    return v

out_path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('perturbation_cases_v2.jsonl')
counts=[0,0,0]; worst=(F(-1),None)
with out_path.open('x',encoding='utf8') as f:
 for N in range(3,8):
  m=N-2
  for word in product((0,1),repeat=N):
   s=word[-2:]; hist=[(word[i-2:i],word[i]) for i in range(2,N)]
   J=sum(k==s for k,y in hist); C=sum(y for k,y in hist if k==s); C_all=sum(y for k,y in hist)
   q=F(C_all+C,m+J); r=F(C_all,m); h=F(J,m); A=F(C,m); B=F(C+1,J+2)
   assert (1+h)*q-r==A
   if J==0: assert B==F(1,2)
   counts[0]+=1; counts[1]+=(J==0)
   for K in (1,2,3,4):
    for case_index,shifts in enumerate([(0,0,0)]+list(product((-1,0,1),repeat=3))):
     qp,rp,hp=[clip(x+F(d,10),0,1) for x,d in zip((q,r,h),shifts)]
     eq,er,eh=abs(qp-q),abs(rp-r),abs(hp-h)
     pqh=prod(hp,qp,K,m); a0=qp-rp+pqh
     ac=clip(a0,0,hp); z=(m*ac+1)/F(m+2)
     hk=spline(hp,K,'reciprocal',m); pzh=prod(z,hk,K,m)
     out=clip(F(m+2,2)*pzh,0,1)
     first=F(m,1)/(2+m*max(h-eh,0))*((1+h)*eq+er+3*eh+F(3,2*K*K))
     second=F(m+2,2*K*K)*(F(3,2)+F(m*m,16)); bound=first+second; err=abs(out-B)
     assert err<=bound,(word,K,shifts,err,bound)
     if bound and err/bound>worst[0]: worst=(err/bound,(word,K,shifts,err,bound))
     rec={'N':N,'m':m,'word':word,'terminal_query':s,'K':K,'case_index':case_index,'shifts_tenths':shifts,'J':J,'C':C,'C_all':C_all,'q':q,'r':r,'h':h,'A':A,'B':B,'q_prime':qp,'r_prime':rp,'h_prime':hp,'e_q':eq,'e_r':er,'e_h':eh,'P_hq':pqh,'A0':a0,'Aclip':ac,'z':z,'H_K':hk,'P_zH':pzh,'network_output':out,'absolute_error':err,'bound_first':first,'bound_second':second,'bound_total':bound,'passed':err<=bound}
     f.write(json.dumps(enc(rec),sort_keys=True,separators=(',',':'))+'\n')
     counts[2]+=1
print('words',counts[0],'zero-count words',counts[1],'spline-and-perturbation checks',counts[2])
print('largest observed error/bound:',worst)
print('case file:',out_path)
