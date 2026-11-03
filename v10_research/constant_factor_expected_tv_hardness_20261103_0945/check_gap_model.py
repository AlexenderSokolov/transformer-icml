from fractions import Fraction
from itertools import product
import gzip,json,sys
rho=Fraction(15,16);alpha=Fraction(29,32);assert alpha==Fraction(7,8)+Fraction(1,32) and rho>alpha
sat=((1,2,3),(-1,2,3))
unsat=tuple(tuple(-(i+1) if b else i+1 for i,b in enumerate(bits)) for bits in product((0,1),repeat=3))
raw=((1,1,-2),(1,-1,2),(-3,-3,-3))
F=[('sat',sat),('unsat_eight',unsat),('repetitions_tautology',raw)]
def frac(x):return [x.numerator,x.denominator]
def lit(l,z):return z[abs(l)-1] if l>0 else 1-z[abs(l)-1]
counts={'formulas':0,'histories':0,'assignment_cases':0,'tautologies':0,'dummy_extra_cases':0}
with open(sys.argv[1],'xb') as rawfile,gzip.GzipFile(fileobj=rawfile,mode='wb',filename='',mtime=0) as out:
 def emit(a):out.write((json.dumps(a,separators=(',',':'))+'\n').encode())
 for name,formula in F:
  n=3;m=len(formula);minimum=max(n*n,m*m,4,(8*(rho-alpha).denominator + (rho-alpha).numerator-1)//(rho-alpha).numerator);M=1<<(minimum-1).bit_length();P=1<<(m-1).bit_length();k=n;T=M+2;p=Fraction(1,M*M);C=Fraction(m,M*P);lam=Fraction(T,M*M)
  assert M>=Fraction(8,1)/(rho-alpha) and k*k<=M and m*m<=M and lam<=(rho-alpha)/4
  normalized=[]
  for cl in formula:
   u=set(cl); taut=any(-v in u for v in u); normalized.append(None if taut else tuple(sorted(u)))
  counts['tautologies']+=sum(c is None for c in normalized)
  pi0=(1-p)**T;assert pi0>=1-lam
  hs=[[0]*T,[1]*T,[i%2 for i in range(T)],[(i//3)%2 for i in range(T)]]
  emit({'kind':'formula','name':name,'raw_formula':formula,'normalized_clauses':normalized,'n':n,'m':m,'M':M,'P':P,'k':k,'p':frac(p),'C':frac(C),'rho':frac(rho),'alpha':frac(alpha),'lambda_upper':frac(lam),'pi0':frac(pi0),'histories':hs})
  overall_max=-1
  for h in hs:
   counts['histories']+=1;locmax=-1
   for bits in product((0,1),repeat=n):
    mask=[i for i in range(n) if h[i]!=bits[i]]
    variants=[mask]
    if len(mask)<k:variants.append(mask+[n])
    for mi,edit in enumerate(variants):
     if mi:counts['dummy_extra_cases']+=1
     z=list(h)
     for i in edit:z[i]^=1
     assert tuple(z[:n])==bits and len(edit)<=k and z[-2:]==h[-2:]
     rows=[];banks=[];Ls=[];statuses=[]
     for cl in normalized:
      taut=cl is None;s=[0 if taut else int(i+1 in cl)-int(-(i+1) in cl) for i in range(M)];negative=1 if taut else sum(v<0 for v in cl)
      row=[]
      for i in range(M):
       x=z[i];a=max(0,s[i]+x-1);b=max(0,-s[i]+x-1);v=a-b;assert v==s[i]*x;row.append([s[i],x,a,b,v])
      bank=sum(a[4] for a in row);L=negative+M*Fraction(bank,M);assert L.denominator==1
      rows.append(row);banks.append(bank);Ls.append(int(L));statuses.append(int(L>0))
     orig=[int(any(lit(v,z) for v in cl)) for cl in formula];assert statuses==orig
     S=sum(statuses);q=p+Fraction(S,M*P);tv=abs(q-p)
     assert tv==Fraction(S,M*P) and p<=q<=p+Fraction(1,M) and len(formula)==len(statuses)
     locmax=max(locmax,S);overall_max=max(overall_max,S);counts['assignment_cases']+=1
     emit({'kind':'case','name':name,'raw_formula':formula,'normalized_clauses':normalized,'n':n,'m':m,'M':M,'P':P,'k':k,'h':h,'assignment':bits,'mask':edit,'z':z,'position_relu':rows,'banks':banks,'literal_counts':Ls,'clause_satisfaction':statuses,'S':S,'p':frac(p),'q':frac(q),'tv':frac(tv),'C':frac(C),'alpha':frac(alpha),'rho':frac(rho)})
   emit({'kind':'history_summary','name':name,'h':h,'max_satisfied_by_assignments':locmax,'model_pointwise_optimum':frac(Fraction(locmax,M*P))})
   if name=='sat':assert locmax==m
   if name=='unsat_eight':assert Fraction(locmax,m)==Fraction(7,8)<alpha
  emit({'kind':'formula_summary','name':name,'m':m,'max_satisfied':overall_max,'exact_expected_optimum_by_identity':frac(Fraction(overall_max,M*P)),'yes_bound':frac(C),'no_bound':frac(alpha*C)})
  counts['formulas']+=1
print(json.dumps(counts,sort_keys=True),'PASS')
