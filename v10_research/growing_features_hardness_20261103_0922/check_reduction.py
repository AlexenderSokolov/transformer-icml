from fractions import Fraction
from itertools import product,combinations

def norm(formula):
 out=[]
 for clause in formula:
  s=set(clause)
  if any(-x in s for x in s):continue
  if not s:return None
  out.append(tuple(sorted(s)))
 return tuple(out)
def sat(formula,bits):
 return all(any((bits[abs(lit)-1]==1) if lit>0 else (bits[abs(lit)-1]==0) for lit in cl) for cl in formula)
def evalnet(formula,bits,mask=None):
 n=len(bits);m=len(formula);M=1<<(max(n*n,m*m,4)-1).bit_length();P=1<<(m-1).bit_length();k=n
 z=[0]*M
 if mask is None:z[:n]=bits
 else:
  for i in mask:z[i]=1
 assert k*k<=M and m*m<=M and sum(z)<=k
 s=[[int(i+1 in cl)-int(-(i+1) in cl) for i in range(M)] for cl in formula]
 cs=[sum(l<0 for l in cl) for cl in formula]
 fs=[];v=[]
 for j in range(m):
  w=[max(0,s[j][i]+z[i]-1)-max(0,-s[j][i]+z[i]-1) for i in range(M)]
  assert all(w[i]==s[j][i]*z[i] for i in range(M))
  bank=sum(w); a=Fraction(bank,M); L=cs[j]+M*a
  expected=sum((z[abs(l)-1] if l>0 else 1-z[abs(l)-1]) for l in formula[j])
  assert L==expected and L.denominator==1 and 0<=L<=3
  fs.append(bank);v.append(max(0,1-L))
 V=sum(v); Q=Fraction(3,2*M);q=Q-Fraction(V,2*M*P);t=Fraction(1,M+2)
 assert Fraction(1,M)<=q<=Q and q>t
 assert (q==Q)==(V==0)==sat(formula,z)
 if V:assert Q-q>=Fraction(1,2*M*P)
 return M,P,V,q,Q
for raw in [((1,1),(-1,2)),((1,-1),(2,)),((1,-1),),((1,),(-1,)),((1,1,1),),()]:
 no=norm(raw)
 for bits in product((0,1),repeat=2):
  assert (False if no is None else sat(no,bits))==sat(raw,bits)
assert norm(((),)) is None
num=assignments=0
for n in range(1,4):
 clauses=[]
 for size in range(1,min(3,n)+1):
  for inds in combinations(range(1,n+1),size):
   for signs in product((-1,1),repeat=size):clauses.append(tuple(i*s for i,s in zip(inds,signs)))
 for m in range(1,4):
  for formula in product(clauses,repeat=m):
   for bits in product((0,1),repeat=n):evalnet(formula,bits);assignments+=1
   num+=1
for formula in [((1,),(-1,)),((1,2,-3),(-1,2,3),(1,-2,3)),((1,-2),(2,-3),(-1,3))]:
 n=max(abs(l) for cl in formula for l in cl);m=len(formula);M=1<<(max(n*n,m*m,4)-1).bit_length();tested=0
 for j in range(n+1):
  for mask in combinations(range(M),j):
   z=[0]*(M+2)
   for i in mask:z[i]=1
   assert z[-2:]==[0,0]
   evalnet(formula,tuple(z[:n]),mask);tested+=1
 print('full_masks',formula,'M',M,'k',n,'masks',tested,'PASS')
print('normalized_formulae',num,'assignments',assignments,'PASS')
print('normalization_examples PASS; deterministic integer/Fraction checks only')
