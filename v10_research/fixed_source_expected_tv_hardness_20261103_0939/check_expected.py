from fractions import Fraction
from itertools import product,combinations
import gzip,json,sys
F=[(1,((1,),(-1,))),(2,((1,2),(-1,-2))),(2,((1,),(-1,)))]
def fr(x):return [x.numerator,x.denominator]
def truth(phi,x):return all(any((x[abs(l)-1] if l>0 else 1-x[abs(l)-1]) for l in clause) for clause in phi)
def model(phi,n,M,P,z):
 m=len(phi);rows=[];banks=[];literal=[];viol=[]
 for clause in phi:
  row=[]
  for i in range(M):
   s=int(i+1 in clause)-int(-(i+1) in clause);x=z[i];u=max(0,s+x-1);v=max(0,-s+x-1);w=u-v
   assert w==s*x;row.append([s,x,u,v,w])
  bank=sum(x[4] for x in row);C=sum(l<0 for l in clause);L=C+Fraction(bank,M)*M
  direct=sum(z[abs(l)-1] if l>0 else 1-z[abs(l)-1] for l in clause)
  assert L==direct and L.denominator==1
  rows.append(row);banks.append(bank);literal.append(int(L));viol.append(max(0,1-int(L)))
 V=sum(viol);Q=Fraction(3,2*M);q=Q-Fraction(V,2*M*P)
 return rows,banks,literal,viol,V,q
counts={'formulas':0,'histories':0,'masks':0,'satisfiable':0,'unsatisfiable':0}
with open(sys.argv[1],'xb') as raw,gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0) as out:
 def emit(x):out.write((json.dumps(x,separators=(',',':'))+'\n').encode())
 for n,phi in F:
  m=len(phi);M=1<<(max(n*n,m*m,4)-1).bit_length();P=1<<(m-1).bit_length();k=n;T=M+2;p=Fraction(1,M*M);Q=Fraction(3,2*M);D=Fraction(1,2*M*P);tau=Q-p-D/2
  xs=[x for x in product((0,1),repeat=n) if truth(phi,x)];sat=bool(xs); xstar=xs[0] if sat else None
  pi0=(1-p)**T;assert pi0>=1-Fraction(T,M*M)>=Fraction(5,8)
  emit({'kind':'formula','n':n,'phi':phi,'M':M,'P':P,'k':k,'p':fr(p),'Q':fr(Q),'Delta':fr(D),'tau':fr(tau),'xstar':xstar,'pi0':fr(pi0)})
  mass=Fraction(0);risk=Fraction(0);identity=Fraction(0);fixed=Fraction(0);nh=0;nm=0
  for h in product((0,1),repeat=T):
   prob=p**sum(h)*(1-p)**(T-sum(h));mass+=prob;nh+=1;counts['histories']+=1
   best=None;bestmask=None;idtv=None
   for j in range(k+1):
    for mask in combinations(range(M),j):
     z=list(h)
     for i in mask:z[i]^=1
     assert z[-2:]==list(h[-2:]) and len(mask)<=k
     rows,banks,L,viol,V,q=model(phi,n,M,P,z);tv=abs(q-p)
     assert Fraction(1,M)<=q<=Q and q>p and tv==q-p
     if not sat:assert V>=1 and tv<=Q-p-D
     if best is None or tv>best:best=tv;bestmask=mask
     if not mask:idtv=tv
     emit({'kind':'mask','n':n,'phi':phi,'M':M,'P':P,'k':k,'h':h,'source_probability':fr(prob),'p':fr(p),'mask':mask,'z':z,'local_relu':rows,'banks':banks,'literal_counts':L,'violations':viol,'V':V,'q':fr(q),'tv':fr(tv),'Q':fr(Q),'Delta':fr(D),'tau':fr(tau)})
     nm+=1;counts['masks']+=1
   risk+=prob*best;identity+=prob*idtv
   az=None;atv=None;acost=None
   if sat:
    az=list(h);az[:n]=xstar;acost=sum(a!=b for a,b in zip(az[:M],h[:M]));assert acost<=k and az[-2:]==list(h[-2:])
    _,_,_,_,v,q=model(phi,n,M,P,az);assert v==0 and q==Q;atv=q-p;fixed+=prob*atv
   emit({'kind':'history_summary','n':n,'phi':phi,'h':h,'source_probability':fr(prob),'best_mask':bestmask,'best_tv':fr(best),'identity_tv':fr(idtv),'fixed_assignment_map_word':az,'fixed_assignment_map_cost':acost,'fixed_assignment_map_tv':None if atv is None else fr(atv)})
  assert mass==1 and identity/risk>=Fraction(3,5)
  if sat:assert risk==fixed==Q-p and risk>tau
  else:assert risk<=Q-p-D and risk<tau
  emit({'kind':'formula_summary','n':n,'phi':phi,'histories':nh,'masks':nm,'mass':fr(mass),'expected_optimum':fr(risk),'identity_expected_tv':fr(identity),'fixed_map_expected_tv':fr(fixed) if sat else None,'tau':fr(tau),'satisfiable':sat})
  counts['formulas']+=1;counts['satisfiable' if sat else 'unsatisfiable']+=1
print(json.dumps(counts,sort_keys=True),'PASS')
