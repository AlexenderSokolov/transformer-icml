from fractions import Fraction
from itertools import combinations
import gzip,json,sys
F=[(1,((1,),(-1,))),(2,((1,2),(-1,-2))),(3,((1,2,-3),(-1,2,3),(1,-2,3))),(2,((1,),(-1,),(2,)))]
def fr(a):return [a.numerator,a.denominator]
counts={'formulas':0,'masks':0,'satisfiable':0,'unsatisfiable':0}
with open(sys.argv[1],'xb') as raw,gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0) as out:
 def emit(r):out.write((json.dumps(r,separators=(',',':'))+'\n').encode())
 for n,clauses in F:
  m=len(clauses);M=1<<(max(n*n,m*m,4)-1).bit_length();P=1<<(m-1).bit_length();k=n;T=M+2
  p=Fraction(1,M*M);Q=Fraction(3,2*M);threshold=Q-p;t=Fraction(1,M+2);gap=Fraction(1,2*M*P)
  prob=Fraction(M*M-1,M*M)**T; low=1-Fraction(T,M*M)
  assert prob>=low>0 and n*n<=M and m*m<=M
  incidence=[[int(i+1 in cl)-int(-(i+1) in cl) for i in range(M)] for cl in clauses]
  neg=[sum(a<0 for a in cl) for cl in clauses]
  header={'kind':'formula','n':n,'clauses':clauses,'M':M,'P':P,'k':k,'h':[0]*T,'target_surrogate':fr(t),'source_p':fr(p),'zero_history_probability':fr(prob),'zero_history_lower_bound':fr(low),'threshold':fr(threshold),'gap':fr(gap),'position_coefficients':incidence,'negative_counts':neg}
  emit(header);best=None; witness=None; sat_count=0; tested=0
  for size in range(k+1):
   for mask in combinations(range(M),size):
    z=[0]*T
    for i in mask:z[i]=1
    assert z[-2:]==[0,0] and sum(z[:M])<=k
    local=[];banks=[];Ls=[];vs=[]
    for j in range(m):
     row=[]
     for i in range(M):
      s=incidence[j][i];x=z[i];plus=max(0,s+x-1);minus=max(0,-s+x-1);v=plus-minus
      assert v==s*x;row.append([s,x,plus,minus,v])
     bank=sum(item[4] for item in row);pooled=Fraction(bank,M);L=neg[j]+M*pooled
     direct=sum(z[abs(a)-1] if a>0 else 1-z[abs(a)-1] for a in clauses[j])
     assert L==direct and L.denominator==1 and 0<=L<=3
     local.append(row);banks.append(bank);Ls.append(int(L));vs.append(max(0,1-int(L)))
    V=sum(vs);q=Q-Fraction(V,2*M*P);tv=abs(q-p);signed=q-p
    sat=all(v==0 for v in vs)
    assert Fraction(1,M)<=q<=Q and q>max(p,t) and tv==signed and (tv==threshold)==sat
    if V:assert threshold-tv>=gap
    if best is None or tv>best:best=tv;witness=mask
    sat_count+=int(sat);tested+=1;counts['masks']+=1
    emit({'kind':'mask','n':n,'clauses':clauses,'M':M,'P':P,'k':k,'mask':mask,'word':z,'local_relu':[local[j] for j in range(m)],'banks':banks,'literal_counts':Ls,'violations':vs,'V':V,'q':fr(q),'p':fr(p),'tv':fr(tv),'threshold':fr(threshold),'gap':fr(gap),'surrogate_t':fr(t),'satisfies':sat})
  is_sat=sat_count>0
  assert (best==threshold)==is_sat
  counts['satisfiable' if is_sat else 'unsatisfiable']+=1;counts['formulas']+=1
  emit({'kind':'summary','n':n,'clauses':clauses,'M':M,'P':P,'k':k,'masks_checked':tested,'satisfying_masks':sat_count,'max_tv':fr(best),'threshold':fr(threshold),'best_witness':witness,'satisfiable':is_sat})
print(json.dumps(counts,sort_keys=True),'PASS')
