from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
out=Path(__file__).with_name('refined_port_cases.jsonl')
def clip(x):return max(F(0),min(F(1),x))
ct=0;ct10=0
with out.open('x') as f:
 for N in range(3,8):
  m=N-2
  for a in product((0,1),repeat=N):
   s=a[-2:]; hist=[(a[i-2:i],a[i]) for i in range(2,N)]
   J=sum(z==s for z,y in hist);C=sum(y for z,y in hist if z==s);T=sum(y for z,y in hist)
   h=F(J,m);r=F(T,m);B=F(C+1,J+2)
   for g in (F(1,2),F(1),F(3)):
    q=F(T+g*C,m+g*J)
    for sh in product((-1,0,1),repeat=3):
     qp,rp,hp=[clip(x+F(d,100)) for x,d in zip((q,r,h),sh)]
     eq,er,eh=[abs(x-y) for x,y in zip((q,r,h),(qp,rp,hp))]
     bp=clip(F(m*((1+g*hp)*qp-rp)/g+1,m*hp+2));error=abs(bp-B)
     den=h-eh+F(2,m)
     b9=((1/g+h)*eq+er/g+(abs(q-B)+eq)*eh)/den if den>0 else None
     if b9 is not None:assert error<=b9
     for u in (F(1,8),F(1,5)):
      if u/2<=h<=3*u/2 and eh<=u/4:
       b10=(6+4/(g*u))*eq+4*er/(g*u)+4*eh/u*(1/(1+g*u/2)+F(2,m*u+4)+eq)
       assert error<=b10;ct10+=1
     f.write(json.dumps({'word':''.join(map(str,a)),'gamma':str(g),'shifts':sh,'J':J,'C':C,'error':str(error),'bound9':None if b9 is None else str(b9)})+'\n');ct+=1
print('PASS',ct,'full port cases; equation10 subcases',ct10)
