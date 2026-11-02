"""Independent finite corroboration; writes only this audit's JSON, never sources."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib, zipfile, math
from lxml import etree
from pypdf import PdfReader
root=Path(__file__).resolve().parents[1]
counts={}
def mm(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def power(a,n):
 out=[[F(i==j) for j in range(len(a))] for i in range(len(a))]
 for _ in range(n): out=mm(out,a)
 return out
kernels=[[[F(1,2),F(1,2)],[F(1,3),F(2,3)]],[[F(0),F(1)],[F(1),F(0)]],[[F(1),F(0)],[F(1,4),F(3,4)]],[[F(1,3)]*3]*3]
counts['exact_schur_return']=0
for p in kernels:
 for s in range(len(p)):
  dp={(s,0):F(1)}
  killed=[[p[i][j] for j in range(len(p)) if j!=s] for i in range(len(p)) if i!=s]
  for n in range(1,13):
   nxt={}
   for (i,c),v in dp.items():
    for j,pr in enumerate(p[i]): nxt[j,c+(i==s)]=nxt.get((j,c+(i==s)),F(0))+v*pr
   dp=nxt
   lhs=sum((v/c for (i,c),v in dp.items() if i==s and c),F(0))
   pn,kn=power(p,n),power(killed,n)
   rhs=(sum(pn[i][i] for i in range(len(p)))-sum(kn[i][i] for i in range(len(killed))))/n
   assert lhs==rhs and lhs<=F(len(p),n)
   counts['exact_schur_return']+=1
def g(x,L):
 if not L:return x
 return g(min(F(1),4*x),L-1)/2+max(F(0),x-F(1,4))
def inv(v,L):
 pts=sorted(set([F(0),F(1)]+[F(1,4**j) for j in range(L+1)]))
 for a,b in zip(pts,pts[1:]):
  ga,gb=g(a,L),g(b,L)
  if ga<=v<=gb:return a+(v-ga)*(b-a)/(gb-ga)
 raise AssertionError((v,L))
counts['exact_compander_floor_inverse']=0
for L in range(9):
 for Q in [16,32,128]:
  D=16*2**L*Q
  for m in [1,3,8,17,64,101]:
   for A in range(m+1):
    x=F(A,m);U=D*A//m;V=0
    for j in range(L):
     R=max(0,U-D//4);V+=R//2**j;U=min(D,4*U)
    W=V+U//2**L; z=Q*W//(2*D); y=inv(F(2*z,Q),L)
    assert 0<=g(x,L)-F(W,D)<=F(2**L+L+1,D)
    assert 0<=g(x,L)-F(2*z,Q)<F(3,Q) and 0<=y<=x
    if A==0: assert z==0 and y==0
    counts['exact_compander_floor_inverse']+=1
counts['exact_uniform_precision']=0
for A in range(2,25):
 c=4
 while A*(c+5)*F(2)**(1-c)>1:c+=1
 for d in [1,2,8,32,100]:
  for h in [4,5,16,32]:
   t=d+2;P=4*h+c*t
   assert F(A**t*(P+1),2**P)<=F(1,2**h)
   counts['exact_uniform_precision']+=1
gd=root/'depth_initialization_guide'; sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((gd/'SOURCE_BINDINGS.json').read_text())
for p,v in m['files'].items():assert sha(root/p)==v,p
q=json.loads((gd/'QA_RECEIPT.json').read_text())
for p,v in {**q['outputs'],**q['build_inputs']}.items():assert sha(gd/p)==v,p
with zipfile.ZipFile(gd/'Chinese-stage6-guide.docx') as z:
 xml=etree.fromstring(z.read('word/document.xml'))
 assert len(xml.xpath('//*[local-name()="oMath"]'))==180
 assert not any(n.startswith('word/media/') for n in z.namelist())
assert len(PdfReader(gd/'Chinese-stage6-guide.pdf').pages)==8
report={'status':'PASS','finite_checks':counts,'guide_source_hashes_verified':len(m['files']),'guide_OMML':180,'guide_pages':8,'limitation':'Finite corroboration, not universal or formal verification.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
