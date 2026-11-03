from fractions import Fraction as F
from itertools import product
import gzip,json,sys

def cv(v):
 if isinstance(v,F):return [v.numerator,v.denominator]
 if isinstance(v,(tuple,list)):return [cv(x) for x in v]
 if isinstance(v,dict):return {k:cv(x) for k,x in v.items()}
 return v

def lit(l,z):return z[abs(l)-1] if l>0 else 1-z[abs(l)-1]
def norm(c):
 s=set(c)
 return None if any(-x in s for x in s) else tuple(sorted(s))
forms=[((1,2,3),(-1,2,3)),tuple(tuple(-(i+1) if b else i+1 for i,b in enumerate(bits)) for bits in product((0,1),repeat=3)),((1,1,2),(1,-1,2),(-2,-2,-2),(1,1,2))]
alpha=F(15,16);eps=F(1,128);counts={'normalization_assignment_cases':0,'formulas':0,'histories':0,'assignment_mask_cases':0}
with open(sys.argv[1],'xb') as raw,gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0) as out:
 def emit(r):out.write((json.dumps(cv(r),separators=(',',':'))+'\n').encode())
 for clause in product((-3,-2,-1,1,2,3),repeat=3):
  nc=norm(clause)
  for bits in product((0,1),repeat=3):
   a=[lit(x,bits) for x in clause];b=[] if nc is None else [lit(x,bits) for x in nc];rt=any(a);nt=True if nc is None else any(b);assert rt==nt
   emit({'kind':'normalization','raw':clause,'normalized':nc,'bits':bits,'raw_values':a,'normalized_values':b,'raw_truth':rt,'normalized_truth':nt});counts['normalization_assignment_cases']+=1
 for fid,formula in enumerate(forms):
  n=3;m=len(formula);M=1<<(max(n*n,m*m,128)-1).bit_length();P=1<<(m-1).bit_length();k=n;p=F(1,M*M);C=F(m,2*P);gap=(1-alpha)*C;tau=(1+alpha)*C/2;lam=F(M+2,M*M);truepi=(1-p)**(M+2);policy_lower=1-eps/C-lam
  assert M>=128 and n*n<=M and m<=P<2*m and C>F(1,4) and gap>F(1,64) and C/32>eps and lam<=F(2,M)<=F(1,64) and truepi>=1-lam and policy_lower>F(61,64)>alpha
  states=list(product((0,1),repeat=2)); ps=(1-p,p); mat=[[ps[y[1]] if x[1]==y[0] else F(0) for y in states] for x in states];sq=[[sum(mat[i][l]*mat[l][j] for l in range(4)) for j in range(4)] for i in range(4)];stationary=[ps[a]*ps[b] for a,b in states];assert all(row==stationary for row in sq)
  normalized=[norm(c) for c in formula];negative=[1 if c is None else sum(l<0 for l in c) for c in normalized];incs=[[0 if c is None else int(i+1 in c)-int(-(i+1) in c) for i in range(M)] for c in normalized]
  histories=[tuple(0 for _ in range(M+2)),tuple(1 for _ in range(M+2)),tuple(i%2 for i in range(M+2)),tuple((i//3)%2 for i in range(M+2))]
  emit({'kind':'formula','id':fid,'raw_formula':formula,'normalized':normalized,'n':n,'m':m,'M':M,'P':P,'k':k,'p':p,'C':C,'alpha':alpha,'epsilon':eps,'yes_no_gap':gap,'midpoint':tau,'midpoint_margin':C/32,'lambda_bound':lam,'zero_probability':truepi,'policy_satisfaction_lower':policy_lower,'transition':mat,'square':sq,'stationary':stationary,'negative_counts':negative,'incidence':incs,'histories':histories})
  maxima=[]
  for h in histories:
   counts['histories']+=1; satisfaction=[]
   for bits in product((0,1),repeat=n):
    base=tuple(i for i in range(n) if bits[i]!=h[i]);masks=[base]+([base+(n,)] if len(base)<k else [])
    for mask in masks:
     z=tuple(bit^(i in mask) if i<M else bit for i,bit in enumerate(h));assert z[:n]==bits and len(mask)<=k and z[-2:]==h[-2:]
     allrows=[];banks=[];truth=[]
     for j in range(m):
      row=[]
      for i in range(M):
       s=incs[j][i];x=z[i];a=s+x-1;b=-s+x-1;u=max(0,a);v=max(0,b);y=u-v;assert y==s*x
       row.append({'s':s,'x':x,'pre_plus':a,'pre_minus':b,'relu_plus':u,'relu_minus':v,'v':y})
      bank=sum(x['v'] for x in row);pooled=F(bank,M);L=negative[j]+M*pooled;rawvals=[lit(x,z) for x in formula[j]];ok=any(rawvals);assert (L>0)==ok
      allrows.append(row);banks.append({'bank':bank,'pooled':pooled,'L':L,'raw_values':rawvals,'truth':ok});truth.append(ok)
     S=sum(truth);q=p+F(S,2*P);tv=abs(q-p);assert p<=q<=p+F(1,2)<=F(9,16) and tv==F(S,2*P)
     emit({'kind':'case','id':fid,'h':h,'bits':bits,'mask':mask,'z':z,'rows':allrows,'banks':banks,'truth':truth,'S':S,'p':p,'q':q,'tv':tv,'C':C,'alpha_C':alpha*C,'midpoint':tau,'error_bound':eps,'zero_TV_baseline':abs(p-p)})
     satisfaction.append(S);counts['assignment_mask_cases']+=1
   mx=max(satisfaction);maxima.append(mx);emit({'kind':'history_summary','id':fid,'h':h,'satisfaction_counts':satisfaction,'max_S':mx,'pointwise_optimum':F(mx,2*P)})
  assert len(set(maxima))==1
  if fid==0:assert maxima[0]==m and C-eps>tau
  if fid==1:assert F(maxima[0],m)==F(7,8)<alpha and F(maxima[0],2*P)+eps<tau
  emit({'kind':'formula_summary','id':fid,'maxima':maxima,'expected_optimum_any_initial_law':F(maxima[0],2*P),'yes_value':C,'no_upper':alpha*C,'midpoint':tau,'policy_lower':policy_lower})
  counts['formulas']+=1
print(json.dumps(counts,sort_keys=True),'PASS')
