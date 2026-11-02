from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).parent
examples=[]
# Uniform pair stationary, heterogeneous second-order rows.
examples.append(('heterogeneous_binary',2,F(1,4),[[F(1,2),F(1,2)],[F(1,4),F(3,4)],[F(1,2),F(1,2)],[F(3,4),F(1,4)]],[F(1,4)]*4))
for K in [2,3]:
 beta=F(1,4); delta=1-beta
 th=[[delta*int(c==b)+beta/K for c in range(K)] for a in range(K) for b in range(K)]
 pi=[(delta*int(a==b)+beta/K)/K for a in range(K) for b in range(K)]
 examples.append((f'sticky_{K}',K,beta,th,pi))
examples.append(('absorbing_zero_mass',2,F(1,4),[[F(1),F(0)],[F(1,2),F(1,2)],[F(1,2),F(1,2)],[F(1,2),F(1,2)]],[F(1),F(0),F(0),F(0)]))
p=[F(1,3),F(2,3)]
examples.append(('iid_nonuniform',2,F(1,3),[p[:] for _ in range(4)],[x*y for x in p for y in p]))
checks=0; reports=[]; event_values={}
for name,K,beta,th,pi in examples:
 delta=1-beta; D=K*K; states=list(product(range(K),repeat=2))
 p=[sum(pi[c*K+d] for d in range(K)) for c in range(K)]
 assert all(sum(row)==1 and min(row)>=0 for row in th)
 assert sum(pi)==1
 assert all(sum(pi[a*K+b]*th[a*K+b][c] for a in range(K))==pi[b*K+c] for b,c in states)
 W={}
 for a,b,c,d in product(range(K),repeat=4):
  L=th[a*K+b][c]*th[b*K+c][d]
  assert L>=beta*pi[c*K+d]
  W[a,b,c,d]=1-beta*pi[c*K+d]/L if L else F(0)
 for z in [F(0),F(1,3),F(1)]:
  az=delta+beta*z
  A=[[th[s][c]-beta*(1-z)*p[c] for c in range(K)] for s in range(D)]
  H=[[A[a*K+b][c]*A[b*K+c][d]*W[a,b,c,d] for c,d in states] for a,b in states]
  assert all(sum(row)<=delta*az for row in H)
  B=[[x/(delta*az) for x in row] for row in H]
  # First-w charging for both K-member start-law families, fixed z.
  nus1=[[p[c]*A[b*K+c][d]/az for c,d in states] for b in range(K)]
  nus2=[[F(c==u)*p[d] for u,d in states] for c in range(K)]
  for nu in nus1+nus2:
   assert sum(nu)==1
   for w in [1,2]:
    total=F(0)
    for L in range(4):
     for path in product(range(D),repeat=L+1):
      if sum(s==path[-1] for s in path[:-1])>=w: continue
      v=nu[path[0]]
      for s,t in zip(path,path[1:]): v*=B[s][t]
      total+=v
    assert total<=D*w
    checks+=1
  maxM=6 if K==2 else 4
  for M in range(1,maxM+1):
   r,e=divmod(M,2); q0=delta**r
   for s0 in states:
    data=[]
    for out in product(range(K),repeat=M):
     path=s0+out
     pairs=[path[i]*K+path[i+1] for i in range(M+1)]
     J=sum(s==pairs[-1] for s in pairs[:-1])
     edge=[A[pairs[i]][path[i+2]] for i in range(M)]
     ww=F(1)
     for i in range(e,M,2): ww*=W[tuple(path[i:i+4])]
     val=ww
     for x in edge: val*=x
     derivative=F(0)
     for i in range(M):
      term=ww*beta*p[path[i+2]]
      for j,x in enumerate(edge):
       if i!=j: term*=x
      derivative+=term
     data.append((J,val,derivative))
    total=sum(x[1] for x in data)
    if z==1: assert total==q0
    if z==0: assert total<=delta**M
    for w in [1,2,M+1]:
     Z=sum(v for J,v,dv in data if J<w)
     der=sum(dv for J,v,dv in data if J<w)
     if r:
      bound=2*beta*az**(e+1)*(delta*az)**(r-1)*K**3*w+e*beta*(delta*az)**r
      assert der<=bound
     event_values[name,M,s0,w,z]=Z
     if z==1:
      E=Z-event_values[name,M,s0,w,F(0)]
      assert E>=0 and E<=min(q0,F(10)*q0*K**3*w/(M+1))
      if r:
       sharp=2*delta**(r-1)*(1-delta**(r+e+1))*K**3*w/(r+e+1)+e*delta**r*(1-delta**(r+1))/(r+1)
       assert E<=sharp
      bound=min(q0,delta**M+F(10)*q0*K**3*w/(M+1))
      assert Z<=bound
     checks+=1
 reports.append({'example':name,'K':K,'beta':str(beta),'max_M':maxM,'z_values':['0','1/3','1'],'initializations':'all deterministic pairs','status':'PASS'})
result={'status':'PASS','arithmetic':'exact Fraction','checks':checks,'examples':reports,'scope':'Finite diagnostics only, not proof or acceptance.'}
(ROOT/'R009_check_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
