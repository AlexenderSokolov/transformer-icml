"""Independent CB005 structural checks. Exact rationals, no author code imports."""
import sympy as S
import itertools,json,hashlib
from pathlib import Path
from collections import Counter,defaultdict
R=S.Rational; counts=Counter(); root=Path(__file__).resolve().parents[1]
def ck(v,k):
 assert v,k
 counts[k]+=1
def binary(a,b,e,t):
 return S.Matrix([[1-a,a,0,0],[0,0,1-b,b],[e,1-e,0,0],[0,0,t,1-t]])
def stationary(P):
 d=P.rows; A=P.T-S.eye(d); A[d-1,:]=S.ones(1,d); B=S.zeros(d,1);B[d-1]=1
 return A.inv()*B
def hit(P,u):
 ids=[i for i in range(P.rows) if i!=u]; x=(S.eye(len(ids))-P.extract(ids,ids)).inv()*S.ones(len(ids),1)
 h=S.zeros(P.rows,1)
 for i,a in enumerate(ids):h[a]=x[i]
 return h
def joint(P,u,start,L):
 D={(start,0):S.Integer(1)}
 for _ in range(L):
  E=defaultdict(lambda:S.Integer(0))
  for (v,j),p in D.items():
   for w in range(P.rows):
    if P[v,w]:E[w,j+(v==u)]+=p*P[v,w]
  D=E
 return D
# Include nonirreducible and defective-return examples for reset identity.
base=[S.eye(3),S.Matrix([[0,1,0],[0,1,0],[1,0,0]]),S.Matrix([[0,1,0],[0,0,1],[1,0,0]])]
base += [binary(*q) for q in itertools.product([R(1,3),R(2,3)],repeat=4)]
base += [S.Matrix([[R(1,2),R(1,3),R(1,6)],[R(1,4),R(1,2),R(1,4)],[R(1,3),R(1,6),R(1,2)]])]
for P in base:
 d=P.rows
 for u in range(d):
  for v in range(d):
   if v==u:continue
   Q=P.copy();Q[u,:]=S.zeros(1,d);Q[u,v]=1
   ids=[i for i in range(d) if i!=u];K=Q.extract(ids,ids)
   alive=S.zeros(1,d);alive[v]=1
   F=[S.Integer(0)]*14
   for t in range(1,13):
    nex=alive*P;f=nex[u];nex[u]=0;alive=nex;F[t+1]=f
    ck(f<=R(d,t+1),'first_hit_density')
   # coefficient of sum F(z)^j/j at r, independently through convolutions
   conv=[S.Integer(1)]+[S.Integer(0)]*13; coeff=[S.Integer(0)]*14
   for j in range(1,14):
    conv=[sum(conv[r-s]*F[s] for s in range(r+1)) for r in range(14)]
    for r in range(1,14):coeff[r]+=conv[r]/j
   for r in range(1,14):ck(coeff[r]==(S.trace(Q**r)-S.trace(K**r))/r,'reset_reciprocal_trace')
# Irreducible heat kernel, Poisson equation, loop occupation, rational Doob likelihood.
for P in base[2:]:
 d=P.rows;p=stationary(P)
 for u in range(d):
  h=hit(P,u);H=max(h);Hb=max(H,1/p[u]);delta=S.zeros(d,1);delta[u]=1/p[u]
  ck(P*h-h==-S.ones(d,1)+delta,'hitting_poisson')
  z=R(3,4); ids=[i for i in range(d) if i!=u]
  hh=S.ones(d,1);sol=(S.eye(d-1)-z*P.extract(ids,ids)).inv()*(z*P.extract(ids,[u]))
  for a,v in enumerate(ids):hh[v]=sol[a]
  f=z*(P*hh)[u]
  Q=S.Matrix(d,d,lambda i,j:z*P[i,j]*hh[j]/(f if i==u else hh[i]))
  for i in range(d):ck(sum(Q.row(i))==1,'doob_rows')
  for r in range(1,8):
   loop=0
   for v in range(d):
    A=joint(P,u,v,r);B=joint(Q,u,v,r)
    loop+=sum(j*prob for (w,j),prob in A.items() if w==v)
    occupation=sum(j*prob for (w,j),prob in A.items())
    ck(occupation==p[u]*(r+(P**r*h)[v]-h[v]),'occupation_potential')
    ck((P**r)[v,u]<=4*d*p[u]*(1+H/R(r)),'target_heat_bound')
    for (w,j),prob in A.items():
     if w==u:
      ck(B.get((w,j),0)==prob*z**r/f**j/hh[v],'doob_joint_likelihood')
   ck(loop==r*(P**r)[u,u],'loop_rotation')
# Singleton starts: killed/reflected count laws and first-hit hazard equality.
for b,e,t in itertools.product([R(0),R(1,3),R(1)],repeat=3):
 P=binary(0,b,e,t); RR=S.Matrix([[0,1-b,b],[1,0,0],[0,t,1-t]])
 if b*t:
  p=stationary(RR);ha=hit(RR,0);hc=hit(RR,2)
  ck(max(ha)==1+1/t,'singleton_HA');ck(max(hc)==2/b,'singleton_HC')
  ck(p[0]*b*max(max(ha),1/p[0])<=1,'singleton_weighted_A')
  ck(p[2]*t*max(max(hc),1/p[2])<=1,'singleton_weighted_C')
 for start in [1,2,3]:
  for L in range(1,9):
   ck(e*(P**L)[start,2]==(P**(L+1))[start,0]-(P**L)[start,0],'singleton_absorption_density')
   for u in [1,3]:
    A=joint(P,u,start,L);B=joint(RR,u-1,start-1,L)
    for (w,j),prob in A.items():
     if w==u:ck(prob<=B.get((w-1,j),0),'singleton_joint_domination')
# Exact exponential-tail comparisons via a rational upper enclosure of exp(x).
def exp_upper(x):
 term=S.Integer(1); total=term
 for j in range(1,81):
  term*=x/j;total+=term
 ratio=x/82
 assert ratio<1
 return total+(term*x/81)/(1-ratio)
for P in [base[2],base[3],base[-1],binary(R(1,8),R(3,4),R(1,4),R(1,8))]:
 d=P.rows;p=stationary(P)
 for u in range(d):
  h=hit(P,u);Hb=max(max(h),1/p[u])
  for v in range(d):
   for L in [8,24,48]:
    D=joint(P,u,v,L)
    upper=sum(prob for (w,j),prob in D.items() if w==u and j>4*L*p[u]+1)
    lower=sum(prob for (w,j),prob in D.items() if j<L*p[u]/16)
    ck(upper*exp_upper(R(L)/(2*Hb))<=16*d*p[u]*(1+Hb/L),'joint_upper_tail_exact_exp_enclosure')
    ck(lower*exp_upper(R(L)/(8*Hb))<=2,'lower_tail_exact_exp_enclosure')

# Freeze exact candidate/dependencies and verify actual acceptance bindings.
for name in ['BU001','SC003','BT002','CB004','BP001']:
 path=root/'intake'/(name+('_root_acceptance.json' if name in ['CB004','BP001'] else '_acceptance.json'))
 rec=json.loads(path.read_text());ck(hashlib.sha256((root/rec['proof']).read_bytes()).hexdigest()==rec['sha256'],'receipt_proof_hash')
 for f,h in rec.get('component_proofs',{}).items():ck(hashlib.sha256((root/f).read_bytes()).hexdigest()==h,'receipt_component_hash')
 if 'review_sha256' in rec:ck(hashlib.sha256((root/rec['review']).read_bytes()).hexdigest()==rec['review_sha256'],'receipt_review_hash')
old=json.loads((root/'critical_beta_adaptation/CB004_BP001_independent_review_bindings.json').read_text())
for f,h in old['files'].items():ck(hashlib.sha256((root/f).read_bytes()).hexdigest()==h,'frozen_dependency_binding')
ck(288*4*40==46080 and 46080<2**16,'fullsupport_constant')
ck(288*3*2+4==1732 and 1732<2048,'singleton_constant')
ck(48*130944+16*(6156+3078)==6433056<2**23,'corruption_constant')
out={'status':'PASS','arithmetic':'Exact sympy rationals/integers; no floating tolerances','checks':dict(counts),'total':sum(counts.values()),'limits':'Finite structural checks, not formal verification. Doob likelihood checked at rational discount 3/4; tail comparisons use exact rational exp upper enclosures. Universal claims rest on the written proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
