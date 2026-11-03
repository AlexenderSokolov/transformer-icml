from fractions import Fraction
from itertools import product,combinations

def run(a,b,full=False):
 n=len(a); m=1<<(max(n*n,4)-1).bit_length(); k=n; A=sum(a); G=1<<(A-1).bit_length(); C=max(a); pad=a+(0,)*(m-n)
 assert m&(m-1)==0 and k*k<=m
 t=Fraction(1,m+2); Q=Fraction(3,2*m)
 subsets={sum(a[i] for i in range(n) if bits[i]) for bits in product((0,1),repeat=n)}
 seen=set()
 if full:
  masks=(comb for j in range(k+1) for comb in combinations(range(m),j))
 else:
  masks=([i for i in range(n) if bits[i]] for bits in product((0,1),repeat=n))
 for mask in masks:
  z=[0]*m
  for i in mask:z[i]=1
  values=[max(0,pad[i]-C+C*z[i]) for i in range(m)]
  S=sum(values); seen.add(S)
  assert S==sum(pad[i]*z[i] for i in range(m))
  r=-Fraction(abs(S-b),2*G)
  q=Q-Fraction(abs(S-b),2*m*G)
  assert -Fraction(1,2)<=r<=0 and Fraction(1,m)<=q<=Q and q>t
  assert (r==0)==(q==Q)==(S==b)
 assert seen==subsets
 return m,len(seen),b in seen
checks=0
for n in range(2,6):
 for a in product(range(1,5),repeat=n):
  for b in range(sum(a)+1):
   run(a,b);checks+=1
for a,b in [((1,2),0),((1,2),2),((1,2),3),((1,2,4),0),((1,2,4),6),((2,4,6),5),((2,4,6),12)]:
 print('full_masks',a,b,run(a,b,True));checks+=1
print('instances',checks,'PASS; deterministic exact rational checks only')
