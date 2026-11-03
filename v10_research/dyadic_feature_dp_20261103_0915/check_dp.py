from fractions import Fraction
from itertools import product,combinations

def bitwords(n): return product((0,1), repeat=n)
def rule(t,q,w,x,h):
 p2,p1=w
 a=(2+t%3)*x-(t%2)*p1+h[(t+1)%len(h)]-1
 b=(t%4-2)*x+p2*p1-(t%2)*p2
 return ((q+x)%3,(p1,x),(a,b))
def heads(t,q,w,x,h):
 p2,p1=w
 a1=1+x; v1=2*x-1
 a2=1+p1; v2=x+p1
 return (0,(p1,x),(a1*v1,a1,a2*v2,a2))
def dp(h,k,fun,d):
 M=len(h)-2; init=(0,(0,0),(0,)*d); cur={init:(0,())}
 for t in range(len(h)):
  nxt={}
  for (q,w,b),(cost,path) in cur.items():
   for x in ((0,1) if t<M else (h[t],)):
    c=cost+(t<M and x!=h[t])
    if c>k: continue
    q2,w2,inc=fun(t,q,w,x,h); key=(q2,w2,tuple(v+y for v,y in zip(b,inc)))
    if key not in nxt or c<nxt[key][0]:nxt[key]=(c,path+(x,))
  cur=nxt
 return cur
def brute(h,k,fun,d):
 M=len(h)-2; cur={}
 for j in range(k+1):
  for mask in combinations(range(M),j):
   z=list(h)
   for i in mask:z[i]^=1
   q=0;w=(0,0);b=(0,)*d
   for t,x in enumerate(z):
    q,w,inc=fun(t,q,w,x,h);b=tuple(v+y for v,y in zip(b,inc))
   key=(q,w,b)
   if key not in cur or j<cur[key][0]:cur[key]=(j,tuple(z))
 return cur
def utility(key):
 q,w,(a,b)=key
 return Fraction(a*a+2*b+3*q+w[0],abs(a)+abs(b)+2)
def validate(h,k,fun,d):
 aa=dp(h,k,fun,d); bb=brute(h,k,fun,d)
 assert set(aa)==set(bb) and all(aa[x][0]==bb[x][0] for x in aa)
 for key,(cost,z) in aa.items():
  assert z[-2:]==h[-2:] and cost==sum(x!=y for x,y in zip(z[:-2],h[:-2])) and cost<=k
  q=0;w=(0,0);b=(0,)*d
  for t,x in enumerate(z):
   q,w,inc=fun(t,q,w,x,h);b=tuple(v+y for v,y in zip(b,inc))
  assert (q,w,b)==key
 if d==2:
  assert max(map(utility,aa))==max(map(utility,bb))
 else:
  for q,w,(n1,d1,n2,d2) in aa:
   assert d1>0 and d2>0
   o1=Fraction(n1,2*d1);o2=Fraction(n2,2*d2)
   _,z=aa[(q,w,(n1,d1,n2,d2))]
   weights1=[1+x for x in z]
   prior=[0]+list(z[:-1])
   weights2=[1+x for x in prior]
   assert o1==sum(Fraction(a*(2*x-1),2) for a,x in zip(weights1,z))/sum(weights1)
   assert o2==sum(Fraction(a*(x+p),2) for a,x,p in zip(weights2,z,prior))/sum(weights2)
 return len(aa)
N=S=0
for M in range(1,6):
 for h in bitwords(M+2):
  for k in range(M+1):
   S+=validate(h,k,rule,2); N+=1
print('signed_finite_state_cases',N,'terminal_states',S,'PASS')
N=S=0
for M in range(1,5):
 for h in bitwords(M+2):
  for k in range(M+1):
   S+=validate(h,k,heads,4);N+=1
print('normalized_two_head_cases',N,'terminal_states',S,'PASS')
