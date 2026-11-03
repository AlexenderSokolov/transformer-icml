"""Independent finite diagnostics for BCJ001; not a proof."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,random,math
root=Path(__file__).resolve().parents[1]; here=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((here/'BCJ001_source_bindings.json').read_text()); binding_checks=[]
for x in manifest['dependencies_and_artifacts']:
 if 'unit' in x:
  for key,hkey in [('proof','proof_sha256'),('receipt','receipt_sha256')]:
   assert sha(root/x[key])==x[hkey]
  rec=json.loads((root/x['receipt']).read_text());assert rec['status']=='ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW';assert rec['sha256']==x['proof_sha256']
  for p,h in rec.get('component_proofs',{}).items():assert sha(root/p)==h
  binding_checks.append(x['unit'])
 else:assert sha(root/x['file'])==x['sha256']
rng=random.Random(202611021428); ncase=0; inconsistent=0
# Boundary-enriched samples: tiny real errors and gate thresholds, not only typical rows.
for J in [0,1,2,3,127,255,256,511,512,513,1023,1024,1025,100000]:
 for L in set([0,J,J//256,J//512,J//1024]):
  for d in [F(0),F(1,10000),F(1,1026),F(1,513),F(1,2),F(1),F(J,1026),F(J,513),F(J,2),F(J+1)]:
   for _ in range(20):
    C=rng.randrange(J+1); q=F(rng.randrange(1001),1000)
    Jp=max(F(0),J+d*rng.choice([-1,0,1]));Cp=min(Jp,max(F(0),C+d*rng.choice([-1,0,1])));Lp=max(F(0),L+d*rng.choice([-1,0,1]))
    # Projection can increase the original C error; measure true radius.
    e=max(abs(Jp-J),abs(Cp-C),abs(Lp-L));G=Jp>0 and 512*Lp>=Jp;H=1024*L>=J;B=J>0 and 256*L<J
    E=abs(F(C,J)-q) if J else 0;out=Cp/Jp if G else F(0)
    rhs=E+8*e/(J+1)*H+q*B+int(J<1026*e+1)+int(J<513*e+1)
    assert abs(out-q)<=rhs
    if G and not H:assert J<1026*e
    if not G and not B and J>0:
     assert J<=e if Jp==0 else J<513*e
    if G and H and J>0:assert abs(out-q)<=E+8*e/(J+1)
    ncase+=1;inconsistent+=Lp>Jp
nf=0
for M in [64,65,67,127,128,129,257]:
 for h in range(4,9):
  Q=1<<h
  for P in [h,h+1,h+7]:
   D=1<<P
   # Compute actual positive shifted recurrence, not ideal exp.
   T=D;W=T
   for j in range(1,34+P+1):T=T*D//(j*D);W+=T
   assert W>=D
   for A in range(M+1):
    a=F((W*D*A)//(M*W),D);assert a==F(D*A//M,D)
    assert int(Q*a)==Q*A//M
    for hc in range(4,h+1):
     Qc=1<<hc;b=F(int(Q*a),Q);c=F(int(Qc*a),Qc);eta=c-b
     assert c==F(Qc*A//M,Qc);assert abs(eta)<F(1,Qc);assert 0<=a+eta<=1;assert F(int(Q*(a+eta)),Q)==c
     nf+=1
nt=0
for d in [F(0),F(1,100000),F(1,1026),F(1,513),F(1,2),F(1),F(17,3),F(1000)]:
 ceil=lambda x:-(-x.numerator//x.denominator)
 assert ceil(1026*d+1)+ceil(513*d+1)<=1539*d+4;nt+=1
assert 8*130944+16*1539==1072176
assert 1072176*6==6433056<2**23
for M in range(64,10000):assert 8193*math.sqrt(32)/math.sqrt(M+1)+64/(M+1)<=2**16/math.sqrt(M)
for h in range(4,30):
 Q=1<<h;assert math.ceil(3*Q/2)+1<=2*Q
assert F(8*5,4)+F(4*3,8)==F(23,2)<12
out={'status':'PASS','scope':'Independent exact finite diagnostics; not formal proof','dependency_receipts_checked':binding_checks,'gate_cases':ncase,'inconsistent_half_exceeds_total_cases':inconsistent,'exact_evaluator_nested_floor_and_coarsening_cases':nf,'real_ceiling_cases':nt,'theorem_sha256':sha(here/'BCJ001_theorem.md')}
(here/'BCJ001_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
