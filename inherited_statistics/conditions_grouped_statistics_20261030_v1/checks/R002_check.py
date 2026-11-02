"""Finite diagnostic only, not proof or formal verification."""
import math, json, hashlib
from collections import defaultdict
from pathlib import Path

def family(K,beta,alpha=.25):
 m=(K-1)//4; L=2*m
 C=list(range(1,m+1)); U=list(range(m+1,2*m+1)); V=list(range(2*m+1,3*m+1)); W=list(range(3*m+1,4*m+1))
 c=[x for a in C for x in (a,0)]
 phases={0:[(1,0)],1:[(0,u) for u in U],2:[(u,v) for u in U for v in V],3:[(v,w) for v in V for w in W],4:[(w,0) for w in W]}
 for t in range(5,L): phases[t]=[(c[t],c[(t+1)%L])]
 Q={(a,b):{0:1.} for a in range(K) for b in range(K)}
 Q[(1,0)]={u:1/m for u in U}
 for u in U: Q[(0,u)]={v:1/m for v in V}
 probs={w:1/m for w in W}
 for j in range(m//2): probs[W[2*j]]=(1+alpha)/m; probs[W[2*j+1]]=(1-alpha)/m
 for u in U:
  for v in V: Q[(u,v)]=dict(probs)
 for w in W: Q[(w,0)]={c[6%L]:1.}
 for t in range(5,L): Q[(c[t],c[(t+1)%L])]={c[(t+2)%L]:1.}
 T={}
 for s,row in Q.items():
  z={a:(1-beta)*p for a,p in row.items()}; z[0]=z.get(0,0)+beta; T[s]=z
 return m,L,c,U,V,W,phases,Q,T

def initial(M,L,c,U,V,W):
 d=M%L;k=(2-d)%L;m=len(U)
 if k==0:return {(1,0):1.}
 if k==1:return {(0,u):1/m for u in U}
 if k==2:return {(u,v):1/m**2 for u in U for v in V}
 if k==3:return {(V[0],W[0]):1.}
 if k==4:return {(W[0],0):1.}
 return {(c[k],c[(k+1)%L]):1.}

results=[]
for beta in [.02,.2,.7]:
 K=13;m,L,c,U,V,W,phases,Q,T=family(K,beta)
 assert min(row.get(0,0)*T[(s[1],0)].get(0,0) for s,row in T.items())>=beta-1e-14
 for M in range(1,15):
  d=M%L;k=(2-d)%L;Vphase={0,1,2,4}|set(range(6,L,2));H=sum((k+t)%L in Vphase for t in range(M));S=M-H;q=M//L
  paths={h:p for h,p in initial(M,L,c,U,V,W).items()}
  for t in range(M):
   new={}
   for h,p in paths.items():
    for z,pz in T[h[-2:]].items():new[h+(z,)]=p*pz
   paths=new
  risk=massA=massAE=riskA=0.; jd=defaultdict(float)
  for h,prob in paths.items():
   endpoint=h[-2:];counts=defaultdict(int);j=0
   for t in range(M):
    if h[t:t+2]==endpoint: j+=1;counts[h[t+2]]+=1
   row=T[endpoint]
   loss=.5*sum(abs((counts[z]+1)/(j+K)-row.get(z,0)) for z in range(K))
   risk+=prob*loss
   A=all(h[t:t+2] in phases[(k+t)%L] for t in range(M+1))
   if A:
    massA+=prob;riskA+=prob*loss;jd[j]+=prob
    # Exact posterior all-symbol-failure probability, from finite likelihood.
    no=1.
    for t in range(M):
     z=h[t+2];row0=T[h[t:t+2]];no*=1-beta*(z==0)/row0[z]
    massAE+=prob*(1-no)
    assert all(h[t:t+2]!=(0,0) for t in range(M+1))
  delta=1-beta;D=min(1,beta+math.sqrt(m**3/(q+1))+K*m*m/(q+1))
  bound=delta**H*D+min(1-delta**H,beta*(2+K*math.log1p(M/K)))
  assert abs(sum(paths.values())-1)<1e-10
  assert abs(massA-delta**H)<1e-10
  assert abs(massAE-delta**H*(1-delta**S))<1e-10
  for j in range(q+1):
   expected=math.comb(q,j)*(1/m**2)**j*(1-1/m**2)**(q-j)
   assert abs(jd[j]/massA-expected)<1e-10
  assert riskA<=delta**H*D+1e-10
  assert risk<=bound+1e-10
  results.append(dict(K=K,M=M,beta=beta,paths=len(paths),H=H,S=S,risk=risk,bound=min(1,bound),mass_AE=massAE))
# Sharp local two-letter family, exact to floating tolerance.
sharp=[]
for beta in [.001,.03,.3,.9]:
 for h in [beta,(1+beta)/2,1.]:
  zeros={(0,0):1.,(1,0):h,(0,1):beta/h,(1,1):beta/h}
  assert min(v*zeros[(s[1],0)] for s,v in zeros.items())>=beta-1e-14
  v=1-h;lhs=(beta/h-beta)/(1-beta);rhs=beta*v/((1-beta)*(1-v))
  assert abs(lhs-rhs)<1e-12
  sharp.append(dict(beta=beta,h=h,residual=lhs))
# Critical-ray stable arithmetic (no huge paths materialized).
asym=[]
for K in [13,32,100,1000,10000,1000000]:
 M=K**5;beta=math.log(K)/M;m=(K-1)//4;L=2*m;q,d=divmod(M,L);k=(2-d)%L
 vp={0,1,2,4}|set(range(6,L,2));H=q*(m+1)+sum((k+j)%L in vp for j in range(d));S=M-H
 lam=math.log1p(-beta);a=math.exp(H*lam);e=a*(-math.expm1(S*lam));q0=math.exp((M//2)*lam)
 D=min(1,beta+math.sqrt(m**3/(q+1))+K*m*m/(q+1));upper=a*D+beta*(2+K*math.log1p(M/K))
 asym.append(dict(K=K,E_lower_over_q0=e/q0,K_times_family_upper=K*upper))
out=dict(status='PASS finite numerical diagnostics only',enumerations=results,sharp_local=sharp,critical=asym)
path=Path(__file__).with_name('R002_check_result.json');path.write_text(json.dumps(out,indent=2))
print(json.dumps(dict(status=out['status'],enumerations=len(results),critical=asym),indent=2))
