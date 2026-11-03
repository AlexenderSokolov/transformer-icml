from itertools import product,combinations,combinations_with_replacement
from fractions import Fraction
from math import isqrt
import gzip,json,sys

def litvalue(lit, assignment):
 return assignment[abs(lit)-1] if lit>0 else 1-assignment[abs(lit)-1]
def evaluate(formula,n,mask):
 m=len(formula); M=1<<(max(4,n*n,m*m)-1).bit_length(); P=1<<(m-1).bit_length()
 z=[int(i in mask) for i in range(M)]+[0,0]
 assert len(mask)<=n and n*n<=M and m*m<=M and z[-2:]==[0,0]
 bank=[]; literal=[]; violation=[]
 for clause in formula:
  local=[]
  for i in range(M):
   s=int((i+1) in clause)-int(-(i+1) in clause)
   x=z[i]
   v=max(0,s+x-1)-max(0,-s+x-1)
   assert v==s*x
   local.append(v)
  a=sum(local);c=sum(l<0 for l in clause); L=c+a
  direct=sum(litvalue(l,z) for l in clause)
  assert Fraction(sum(local),M)*M+c==direct==L and 0<=L<=3
  bank.append(a); literal.append(L); violation.append(max(0,1-L))
 V=sum(violation); q=Fraction(3,2*M)-Fraction(V,2*M*P);Q=Fraction(3,2*M);target=Fraction(1,M+2)
 assert Fraction(1,M)<=q<=Q<1 and target<q and (q==Q)==all(x>0 for x in literal)
 gap=Fraction(1,2*M*P); slope=Fraction(8,M*(M+2)); ce_gap=Fraction(4,M*M*(M+2)*P)
 assert slope*gap==ce_gap and (q-target)/(q*(1-q))>=slope
 if V: assert Q-q>=gap
 return {'M':M,'P':P,'mask':mask,'z':z,'bank':bank,'literal_counts':literal,'violations':violation,'q':[q.numerator,q.denominator],'Q':[Q.numerator,Q.denominator],'target':[target.numerator,target.denominator],'ce_gap':[ce_gap.numerator,ce_gap.denominator]}

count={'normalization':0,'formula_assignments':0,'formulae':0,'full_masks':0,'gap_grid':0}
with open(sys.argv[1],'xb') as f,gzip.GzipFile(fileobj=f,mode='wb',filename='',mtime=0) as out:
 def emit(r):out.write((json.dumps(r,separators=(',',':'))+'\n').encode())
 rawclauses=[()] + [x for length in (1,2,3) for x in product((-2,-1,1,2),repeat=length)]
 for raw in product(rawclauses,repeat=2):
  normalized=[]; contradiction=False
  for cl in raw:
   s=set(cl)
   if any(-a in s for a in s):continue
   if not s:contradiction=True;break
   normalized.append(tuple(sorted(s)))
  for bits in product((0,1),repeat=2):
   before=all(any(litvalue(l,bits) for l in cl) for cl in raw)
   after=not contradiction and all(any(litvalue(l,bits) for l in cl) for cl in normalized)
   assert before==after
   emit({'kind':'normalization','raw':raw,'normalized':normalized,'contradiction':contradiction,'assignment':bits,'truth':before});count['normalization']+=1
 for n in (1,2,3):
  clauses=[]
  for sz in range(1,min(3,n)+1):
   for idx in combinations(range(1,n+1),sz):
    for signs in product((-1,1),repeat=sz): clauses.append(tuple(x*s for x,s in zip(idx,signs)))
  for m in (1,2,3):
   for formula in combinations_with_replacement(clauses,m):
    for bits in product((0,1),repeat=n):
     mask=tuple(i for i,x in enumerate(bits) if x)
     result=evaluate(formula,n,mask)
     emit({'kind':'assignment','n':n,'formula':formula,'bits':bits,**result});count['formula_assignments']+=1
    count['formulae']+=1
 for formula,n in [(((1,),(-1,)),1),(((1,2,-3),(-1,2,3),(1,-2,3)),3),(((1,-2),(2,-3),(-1,3)),3),(((1,2),(-1,-2)),2)]:
  m=len(formula);M=1<<(max(4,n*n,m*m)-1).bit_length()
  for k in range(n+1):
   for mask in combinations(range(M),k):
    result=evaluate(formula,n,mask)
    emit({'kind':'full_mask','n':n,'formula':formula,**result});count['full_masks']+=1
 for power in range(2,13):
  M=1<<power
  for m in range(1,isqrt(M)+1):
   P=1<<(m-1).bit_length(); Q=Fraction(3,2*M);t=Fraction(1,M+2);dq=Fraction(1,2*M*P);lower=Fraction(8,M*(M+2))
   for V in range(m+1):
    q=Q-V*dq; derivative=(q-t)/(q*(1-q));assert derivative>=lower and Fraction(1,M)<=q<=Q
    emit({'kind':'gap','M':M,'m':m,'P':P,'V':V,'q':[q.numerator,q.denominator],'derivative':[derivative.numerator,derivative.denominator],'lower':[lower.numerator,lower.denominator]});count['gap_grid']+=1
print(json.dumps(count,sort_keys=True),'PASS')
