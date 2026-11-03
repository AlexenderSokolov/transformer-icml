from fractions import Fraction as F
from itertools import product
import gzip,json,sys

def enc(x):
 if isinstance(x,F):return [x.numerator,x.denominator]
 if isinstance(x,(tuple,list)):return [enc(y) for y in x]
 if isinstance(x,dict):return {k:enc(y) for k,y in x.items()}
 return x

def sat_lit(l,b):return b[abs(l)-1] if l>0 else 1-b[abs(l)-1]
def norm(c):
 s=set(c)
 return None if any(-x in s for x in s) else tuple(sorted(s))

rho=F(1);alpha=F(15,16);gap=rho-alpha; assert alpha>F(7,8)
forms=[((1,2,3),(-1,2,3)),tuple(tuple(-(i+1) if b else i+1 for i,b in enumerate(bits)) for bits in product((0,1),repeat=3)),((1,1,2),(1,-1,2),(-2,-2,-2),(1,1,2))]
N=R=hist=0
with open(sys.argv[1],'xb') as raw,gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as out:
 def emit(x):out.write((json.dumps(enc(x),separators=(',',':'))+'\n').encode())
 for clause in product((-3,-2,-1,1,2,3),repeat=3):
  nc=norm(clause)
  for b in product((0,1),repeat=3):
   raw_values=[sat_lit(x,b) for x in clause]; norm_values=[] if nc is None else [sat_lit(x,b) for x in nc]
   a=any(raw_values);z=True if nc is None else any(norm_values);assert a==z
   emit({'kind':'normalization','raw_clause':clause,'normalized':nc,'bits':b,'raw_literal_values':raw_values,'normalized_literal_values':norm_values,'raw_truth':a,'normalized_truth':z});N+=1
 for fid,phi in enumerate(forms):
  n=3;m=len(phi); minM=max(n*n,m*m,4,(8*gap.denominator+gap.numerator-1)//gap.numerator);M=1<<(minM-1).bit_length();P=1<<(m-1).bit_length();k=n;p=F(1,M*M);C=F(m,M*P);lam=F(M+2,M*M);pi0=(1-p)**(M+2)
  assert M>=8/gap and lam<=F(2,M)<=gap/4 and pi0>=1-lam and M*M>=n*n
  states=list(product((0,1),repeat=2)); probs=(1-p,p);Pmat=[[probs[y[1]] if x[1]==y[0] else F(0) for y in states] for x in states];P2=[[sum(Pmat[i][j]*Pmat[j][k] for j in range(4)) for k in range(4)] for i in range(4)];stat=[probs[a]*probs[b] for a,b in states];assert all(row==stat for row in P2)
  normalized=[norm(cl) for cl in phi];nneg=[1 if c is None else sum(x<0 for x in c) for c in normalized]
  incidence=[[0 if c is None else int(i+1 in c)-int(-(i+1) in c) for i in range(M)] for c in normalized]
  histlist=[tuple(0 for i in range(M+2)),tuple(1 for i in range(M+2)),tuple(i%2 for i in range(M+2)),tuple((i//3)%2 for i in range(M+2))]
  emit({'kind':'formula','id':fid,'phi':phi,'normalized':normalized,'n':n,'m':m,'M':M,'P':P,'k':k,'p':p,'C':C,'alpha':alpha,'rho':rho,'lambda_upper':lam,'pi0':pi0,'source_transition':Pmat,'source_squared':P2,'stationary':stat,'incidence':incidence,'negative_counts':nneg,'histories':histlist})
  scores=[]
  for h in histlist:
   hist+=1;this=[]
   for bits in product((0,1),repeat=n):
    base=tuple(i for i in range(n) if bits[i]!=h[i]); masks=[base]+([base+(n,)] if len(base)<k else [])
    for mask in masks:
     z=tuple(x^(i in mask) if i<M else x for i,x in enumerate(h));assert z[:n]==bits and len(mask)<=k and z[-2:]==h[-2:]
     rows=[];bs=[];truth=[]
     for j in range(m):
      row=[]
      for i in range(M):
       s=incidence[j][i];x=z[i];a=s+x-1;b=-s+x-1;ra=max(0,a);rb=max(0,b);y=ra-rb;assert y==s*x
       row.append({'s':s,'x':x,'pre_plus':a,'pre_minus':b,'relu_plus':ra,'relu_minus':rb,'value':y})
      bank=sum(a['value'] for a in row);avg=F(bank,M);L=nneg[j]+M*avg;lit=[sat_lit(x,z) for x in phi[j]];literal_truth=any(lit);assert (L>0)==literal_truth
      rows.append(row);bs.append({'bank':bank,'avg':avg,'L':L,'raw_literal_values':lit,'truth':literal_truth});truth.append(literal_truth)
     S=sum(truth);q=p+F(S,M*P);tv=abs(q-p);assert p<=q<=p+F(1,M) and tv==F(S,M*P)
     emit({'kind':'case','id':fid,'h':h,'assignment':bits,'mask':mask,'z':z,'rows':rows,'banks':bs,'truth':truth,'S':S,'p':p,'q':q,'tv':tv,'C':C,'rho_lower':rho*C,'alpha_upper':alpha*C})
     R+=1;this.append(S)
   scores.append(max(this));emit({'kind':'history_summary','id':fid,'h':h,'all_satisfaction_counts':this,'max_satisfied':max(this),'pointwise_optimum':F(max(this),M*P)})
  assert len(set(scores))==1
  if fid==0:assert scores[0]==m
  if fid==1:assert F(scores[0],m)==F(7,8)<alpha
  emit({'kind':'formula_summary','id':fid,'scores_by_history':scores,'max_satisfied':scores[0],'expected_optimum_any_initial_law':F(scores[0],M*P),'yes_value':C,'no_upper':alpha*C})
print(json.dumps({'normalization_assignment_cases':N,'formulas':len(forms),'histories':hist,'assignment_mask_cases':R},sort_keys=True),'PASS')
