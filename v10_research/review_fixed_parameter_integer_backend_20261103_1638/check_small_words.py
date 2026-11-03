from itertools import product
from decimal import Decimal, getcontext
getcontext().prec=80
for n in range(2,9):
 L=n+2;s=(L-1).bit_length();b=16*s;H=1<<b;F=H*H;z=F-H
 for _ in range(b): z=z*z//F
 r=H*z//F; T=[H]
 for _ in range(b):T.append(T[-1]*r//H)
 def att(scores,vals):
  a=max(scores); weights=[T[a-t] if a-t<=b else 0 for t in scores];W=sum(weights)
  return H*sum(w*x for w,x in zip(weights,vals))//(2*W)
 def snap(a):return 2*max(a-H//4,0)-2*max(a-3*H//4,0)
 mx=Decimal(0)
 for xs in product((0,1), repeat=n):
  vals=[1,1]+[2*x for x in xs]; t=[]
  for i in range(1,L+1):
   ss=[]
   for h in (1,2):ss.append(snap(att([2*i*(i-h)*j-i*j*j for j in range(1,i+1)],vals[:i])))
   t.append(ss)
   if i>=4: assert ss[0] == vals[i-2]*H//2
   if i>=5: assert ss[1] == vals[i-3]*H//2
  S=xs[-2:]; C=J=0
  for k in range(2,n):
   if xs[k-2:k]==S:J+=1;C+=xs[k]
  anchor=2*S[0]+S[1]; g=[]
  for k in range(n):g.append(k>=2 and 2*xs[k-2]+xs[k-1]==anchor)
  scores=[n,n]+[n if q else 0 for q in g];Q=att(scores,vals)
  diff=abs(Decimal(Q)/H-Decimal(C+1)/Decimal(J+2));mx=max(mx,diff)
  bound=Decimal(n)/2*(-Decimal(n)).exp()+Decimal(3)/(Decimal(L)**7)
  assert diff <= bound
 print(n, 2**n, 'max_diff',format(mx,'.6g'), 'bound',format(bound,'.6g'))
