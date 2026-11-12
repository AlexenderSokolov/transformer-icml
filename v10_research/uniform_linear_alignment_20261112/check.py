from fractions import Fraction as F
from itertools import product
import random,json
if not __debug__:raise RuntimeError('Run without -O')
rng=random.Random(20261112)
checks=0;cases=0;enumerations=0
for n in range(3,11):
 P=[[F(1,i+1) if j<=i else F(0) for j in range(n)] for i in range(n)]
 powers=[[[F(int(i==j)) for j in range(n)] for i in range(n)]]
 for degree in range(1,2*n+1):
  A=powers[-1]
  powers.append([[sum(A[i][k]*P[k][j] for k in range(n)) for j in range(n)] for i in range(n)])
 for case in range(12):
  degree=rng.randrange(2*n+1)
  co=[F(rng.randrange(-5,6),rng.randrange(1,6)) for _ in range(degree+1)]
  A=[[sum(co[k]*powers[k][i][j] for k in range(degree+1)) for j in range(n)] for i in range(n)]
  bias=[F(rng.randrange(-2,3),3) for _ in range(n)]
  for i in range(1,n):
   assert A[i][i]==sum(co[k]*F(1,i+1)**k for k in range(degree+1))
   assert A[i][i-1]==i*(A[i-1][i-1]-A[i][i]);checks+=2
  err=max(sum(abs(A[i][j]-int(j==i-1)) for j in range(n))+abs(bias[i]) for i in range(1,n))
  H=sum(F(1,k) for k in range(2,n))
  assert err*(H+2)>=H;checks+=1
  if n<=7 and case<2:
   direct=max(abs(sum(A[i][j]*x[j] for j in range(n))+bias[i]-x[i-1]) for x in product((-1,1),repeat=n) for i in range(1,n))
   assert direct==err;checks+=1;enumerations+=1
  cases+=1
print(json.dumps({'seed':20261112,'cases':cases,'assertions':checks,'full_sign_cube_comparisons':enumerations,'N_range':[3,10],'max_degree':20,'arithmetic':'exact Fraction','status':'pass'}))
