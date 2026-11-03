from fractions import Fraction
from itertools import product
import gzip,json,sys
alpha=Fraction(15,16);error=Fraction(1,128)
sat=((1,2,3),(-1,2,3))
unsat=tuple(tuple(-(i+1) if b else i+1 for i,b in enumerate(bits)) for bits in product((0,1),repeat=3))
raw=((1,1,-2),(1,-1,2),(-3,-3,-3))
F=[('sat',sat),('unsat_eight',unsat),('repetitions_tautology',raw)]
def fr(x):return [x.numerator,x.denominator]
def literal(l,z):return z[abs(l)-1] if l>0 else 1-z[abs(l)-1]
counts={'formulas':0,'histories':0,'assignment_cases':0,'tautologies':0,'dummy_extra_cases':0}
with open(sys.argv[1],'xb') as rawfile,gzip.GzipFile(fileobj=rawfile,mode='wb',filename='',mtime=0) as out:
 def emit(a):out.write((json.dumps(a,separators=(',',':'))+'\n').encode())
 for name,formula in F:
  n=3;m=len(formula);M=1<<(max(n*n,m*m,128)-1).bit_length();P=1<<(m-1).bit_length();k=n;T=M+2;p=Fraction(1,M*M);C=Fraction(m,2*P);tau=(1+alpha)*C/2;lambda_bound=Fraction(T,M*M)
  assert k*k<=M and m*m<=M and M>=128 and C>Fraction(1,4) and C-alpha*C>Fraction(1,64)
  assert C-tau>error and tau-alpha*C>error and lambda_bound<=Fraction(1,64)
  normalized=[]
  for cl in formula:
   u=set(cl);taut=any(-v in u for v in u);normalized.append(None if taut else tuple(sorted(u)))
  counts['tautologies']+=sum(c is None for c in normalized)
  hs=[[0]*T,[1]*T,[i%2 for i in range(T)],[(i//3)%2 for i in range(T)]]
  emit({'kind':'formula','name':name,'raw_formula':formula,'normalized_clauses':normalized,'n':n,'m':m,'M':M,'P':P,'k':k,'p':fr(p),'C':fr(C),'tau':fr(tau),'alpha':fr(alpha),'accuracy':fr(error),'lambda_upper':fr(lambda_bound),'histories':hs})
  overall=-1
  for h in hs:
   counts['histories']+=1;best=-1
   for bits in product((0,1),repeat=n):
    reset=[i for i in range(n) if h[i]!=bits[i]];variants=[reset]
    if len(reset)<k:variants.append(reset+[n])
    for vi,mask in enumerate(variants):
     if vi:counts['dummy_extra_cases']+=1
     z=list(h)
     for i in mask:z[i]^=1
     assert tuple(z[:n])==bits and len(mask)<=k and z[-2:]==h[-2:]
     rows=[];banks=[];Ls=[];statuses=[]
     for cl in normalized:
      taut=cl is None;s=[0 if taut else int(i+1 in cl)-int(-(i+1) in cl) for i in range(M)];neg=1 if taut else sum(x<0 for x in cl);row=[]
      for i in range(M):
       x=z[i];a=max(0,s[i]+x-1);b=max(0,-s[i]+x-1);v=a-b;assert v==s[i]*x;row.append([s[i],x,a,b,v])
      bank=sum(a[4] for a in row);L=neg+M*Fraction(bank,M);assert L.denominator==1
      rows.append(row);banks.append(bank);Ls.append(int(L));statuses.append(int(L>0))
     assert statuses==[int(any(literal(v,z) for v in cl)) for cl in formula] and len(statuses)==m
     S=sum(statuses);q=p+Fraction(S,2*P);tv=abs(q-p)
     assert tv==Fraction(S,2*P) and p<=q<=Fraction(9,16)
     best=max(best,S);overall=max(overall,S);counts['assignment_cases']+=1
     emit({'kind':'case','name':name,'raw_formula':formula,'normalized_clauses':normalized,'n':n,'m':m,'M':M,'P':P,'k':k,'h':h,'assignment':bits,'mask':mask,'z':z,'position_relu':rows,'banks':banks,'literal_counts':Ls,'clause_satisfaction':statuses,'S':S,'p':fr(p),'q':fr(q),'tv':fr(tv),'C':fr(C),'tau':fr(tau),'alpha':fr(alpha)})
   emit({'kind':'history_summary','name':name,'h':h,'max_satisfied_by_assignments':best,'pointwise_optimum':fr(Fraction(best,2*P))})
   if name=='sat':assert best==m
   if name=='unsat_eight':assert Fraction(best,m)==Fraction(7,8)<alpha
  emit({'kind':'formula_summary','name':name,'m':m,'max_satisfied':overall,'expected_optimum_by_identity':fr(Fraction(overall,2*P)),'C':fr(C),'tau':fr(tau),'alphaC':fr(alpha*C)})
  counts['formulas']+=1
print(json.dumps(counts,sort_keys=True),'PASS')
