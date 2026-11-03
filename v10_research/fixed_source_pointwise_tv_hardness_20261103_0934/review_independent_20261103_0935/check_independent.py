from itertools import combinations,combinations_with_replacement
from fractions import Fraction as F
import gzip,json,sys

def v(x):
 if isinstance(x,F):return [x.numerator,x.denominator]
 if isinstance(x,list):return [v(q) for q in x]
 if isinstance(x,tuple):return [v(q) for q in x]
 if isinstance(x,dict):return {k:v(q) for k,q in x.items()}
 return x
clauses=[(1,),(-1,),(2,),(-2,),(1,2),(1,-2),(-1,2),(-1,-2)]
forms=[(2,f) for m in (1,2) for f in combinations_with_replacement(clauses,m)]
forms += [(1,((1,),(-1,))),(3,((1,2,-3),(-1,2,3),(1,-2,3))),(2,((1,),(-1,),(2,)))]
N=R=SAT=0
with open(sys.argv[1],'xb') as raw,gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0) as out:
 def emit(x):out.write((json.dumps(v(x),separators=(',',':'))+'\n').encode())
 for fid,(n,phi) in enumerate(forms):
  m=len(phi); M=1<<(max(n*n,m*m,4)-1).bit_length(); P=1<<(m-1).bit_length(); k=n; p=F(1,M*M);t=F(1,M+2);qmax=F(3,2*M);Delta=F(1,2*M*P);tau=qmax-p
  states=((0,0),(0,1),(1,0),(1,1)); probs=(1-p,p)
  transition=[[probs[c] if v==(u[1],c) else F(0) for v in states] for u in states for c in []] # constructed below
  transition=[[probs[y[1]] if x[1]==y[0] else F(0) for y in states] for x in states]
  square=[[sum(transition[i][w]*transition[w][j] for w in range(4)) for j in range(4)] for i in range(4)]
  stationary=[probs[a]*probs[b] for a,b in states]
  assert all(row==stationary for row in square)
  initials=[[F(1),F(0),F(0),F(0)],[F(0),F(1),F(0),F(0)],[F(1,4)]*4,stationary]
  initial_cases=[]
  for mu in initials:
   val=mu[0]*(1-p)**M
   initial_cases.append({'mu':mu,'history_probability':val,'positive':val>0,'formula_value':mu[0]*(1-p)**M})
  assert initial_cases[0]['positive'] and not initial_cases[1]['positive'] and initial_cases[3]['history_probability']==(1-p)**(M+2)
  lower=1-F(M+2,M*M);assert (1-p)**(M+2)>=lower>0
  incidence=[[int(i+1 in clause)-int(-(i+1) in clause) for i in range(M)] for clause in phi]
  nneg=[sum(l<0 for l in clause) for clause in phi]
  emit({'kind':'formula','id':fid,'n':n,'phi':phi,'m':m,'M':M,'P':P,'k':k,'p':p,'t':t,'Q':qmax,'threshold':tau,'Delta':Delta,'transition':transition,'transition_squared':square,'stationary':stationary,'initial_laws':initial_cases,'lower_zero_probability':lower,'incidence':incidence,'negative_literals':nneg})
  best=None;bestmask=None; anysat=False; records=0
  for j in range(k+1):
   for mask in combinations(range(M),j):
    word=[int(i in mask) for i in range(M)]+[0,0]; assert len(mask)<=k and word[-2:]==[0,0]
    stages=[]; literals=[];viol=[];bank=[]
    for l,cl in enumerate(phi):
     row=[]
     for i in range(M):
      s=incidence[l][i];x=word[i];a=s+x-1;b=-s+x-1;aa=max(a,0);bb=max(b,0); y=aa-bb
      assert y==s*x
      row.append({'i':i,'s':s,'x':x,'pre_plus':a,'pre_minus':b,'relu_plus':aa,'relu_minus':bb,'value':y})
     B=sum(e['value'] for e in row); pool=F(B,M);L=nneg[l]+M*pool;direct=sum(word[abs(a)-1] if a>0 else 1-word[abs(a)-1] for a in cl); assert L==direct
     stages.append(row);bank.append({'sum':B,'pool':pool,'L':L,'direct':direct});literals.append(int(L));viol.append(max(0,1-int(L)))
    V=sum(viol); q=qmax-F(V,2*M*P); signed=q-p;tv=abs(signed);deriv=(q-t)/(q*(1-q));sat=all(a>0 for a in literals)
    assert F(1,M)<=q<=qmax and q>t and q>p and tv==signed and (tv>=tau)==sat and deriv>0
    diff=tau-tv
    if not sat:assert diff>=Delta
    anysat|=sat
    if best is None or tv>best:best=tv;bestmask=mask
    emit({'kind':'mask','id':fid,'mask':mask,'word':word,'layers':stages,'bank_pool_literals':bank,'violations':viol,'V':V,'q':q,'p':p,'signed_difference':signed,'tv':tv,'surrogate':t,'ce_derivative':deriv,'threshold':tau,'threshold_minus_tv':diff,'Delta':Delta,'satisfies':sat,'crosses_threshold':tv>=tau})
    records+=1;R+=1
  assignments=[]
  for a in range(1<<n):
   bits=[(a>>i)&1 for i in range(n)]; truth=[any(bits[abs(l)-1] if l>0 else 1-bits[abs(l)-1] for l in cl) for cl in phi]
   assignments.append({'bits':bits,'clause_truth':truth,'satisfies':all(truth)})
  direct_sat=any(a['satisfies'] for a in assignments)
  assert direct_sat==anysat==(best==tau)
  emit({'kind':'summary','id':fid,'n':n,'phi':phi,'assignments':assignments,'mask_count':records,'best':best,'witness':bestmask,'threshold':tau,'satisfiable':anysat})
  N+=1;SAT+=int(anysat)
print(json.dumps({'formulae':N,'masks':R,'satisfiable':SAT,'unsatisfiable':N-SAT},sort_keys=True),'PASS')
