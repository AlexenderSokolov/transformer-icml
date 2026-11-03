from fractions import Fraction as F
from itertools import product,combinations
import gzip,json,sys

def enc(x):
 if isinstance(x,F):return [x.numerator,x.denominator]
 if isinstance(x,(tuple,list)):return [enc(a) for a in x]
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 return x
forms=[(1,((1,),(-1,))),(2,((1,2),(-1,-2))),(2,((1,),(2,)))]
with open(sys.argv[1],'xb') as raw,gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as out:
 def emit(r):out.write((json.dumps(enc(r),separators=(',',':'))+'\n').encode())
 N=HC=NC=0
 for fid,(n,phi) in enumerate(forms):
  m=len(phi);M=1<<(max(4,n*n,m*m)-1).bit_length();P=1<<(m-1).bit_length();k=n;p=F(1,M*M);Q=F(3,2*M);delta=F(1,2*M*P);threshold=Q-p-delta/2
  pr=[1-p,p];states=list(product((0,1),repeat=2));trans=[[pr[b[1]] if a[1]==b[0] else F(0) for b in states] for a in states];square=[[sum(trans[i][l]*trans[l][j] for l in range(4)) for j in range(4)] for i in range(4)];stat=[pr[a]*pr[b] for a,b in states];assert all(row==stat for row in square)
  mus=[stat,[F(1),F(0),F(0),F(0)],[F(0),F(1),F(0),F(0)]]
  assignments=[]
  for bits in product((0,1),repeat=n):
   literals=[[bits[abs(a)-1] if a>0 else 1-bits[abs(a)-1] for a in cl] for cl in phi]
   assignments.append({'bits':bits,'literals':literals,'satisfies':all(any(c) for c in literals)})
  winners=[a['bits'] for a in assignments if a['satisfies']];sat=bool(winners);xstar=winners[0] if sat else None
  incidence=[[int(i+1 in c)-int(-(i+1) in c) for i in range(M)] for c in phi];neg=[sum(a<0 for a in c) for c in phi]
  def model(z):
   rows=[]; banks=[]; vio=[]
   for j in range(m):
    row=[]
    for i in range(M):
     s=incidence[j][i];x=z[i];pa=s+x-1;pb=-s+x-1;ra=max(0,pa);rb=max(0,pb);r=ra-rb;assert r==s*x
     row.append({'s':s,'x':x,'pre_plus':pa,'pre_minus':pb,'relu_plus':ra,'relu_minus':rb,'v':r})
    bank=sum(r['v'] for r in row);avg=F(bank,M);L=neg[j]+M*avg;direct=sum(z[abs(t)-1] if t>0 else 1-z[abs(t)-1] for t in phi[j]);assert L==direct
    rows.append(row);banks.append({'bank':bank,'avg':avg,'negative_count':neg[j],'L':L,'direct':direct});vio.append(max(0,1-int(L)))
   V=sum(vio);q=Q-F(V,2*M*P);tv=abs(q-p);assert F(1,M)<=q<=Q and q>p and tv==q-p
   return {'rows':rows,'banks':banks,'violations':vio,'V':V,'q':q,'p':p,'signed_q_minus_p':q-p,'tv':tv}
  mass=[F(0)]*3;risk=[F(0)]*3;identity=[F(0)]*3;fixed=[F(0)]*3
  zero_prob=(1-p)**(M+2); lower=1-F(M+2,M*M);assert zero_prob>=lower>=F(5,8)
  emit({'kind':'formula','fid':fid,'n':n,'phi':phi,'m':m,'M':M,'P':P,'k':k,'p':p,'Q':Q,'delta':delta,'threshold':threshold,'transition':trans,'transition_squared':square,'stationary':stat,'initial_laws':mus,'assignments':assignments,'xstar':xstar,'zero_probability':zero_prob,'zero_lower_bound':lower,'incidence':incidence})
  for h in product((0,1),repeat=M+2):
   probs=[mu[states.index(h[:2])]*p**sum(h[2:])*(1-p)**(M-sum(h[2:])) for mu in mus]
   for j in range(3):mass[j]+=probs[j]
   candidates=[];winner=None;winner_result=None;identity_result=None
   for s in range(k+1):
    for mask in combinations(range(M),s):
     z=tuple(bit^(i in mask) if i<M else bit for i,bit in enumerate(h));res=model(z)
     assert z[-2:]==h[-2:] and sum(a!=b for a,b in zip(z[:M],h[:M]))<=k
     if not sat:assert res['V']>=1 and res['tv']<=Q-p-delta
     if winner_result is None or res['tv']>winner_result['tv']:winner=mask;winner_result=res
     if not mask:identity_result=res
     emit({'kind':'candidate','fid':fid,'h':h,'history_probability_by_initial_law':probs,'mask':mask,'z':z,'result':res,'threshold':threshold,'delta':delta})
     NC+=1
   for j in range(3):risk[j]+=probs[j]*winner_result['tv'];identity[j]+=probs[j]*identity_result['tv']
   fixed_word=fixed_result=None;fixed_cost=None
   if sat:
    fixed_word=tuple(xstar)+h[n:];fixed_cost=sum(a!=b for a,b in zip(fixed_word[:M],h[:M]));fixed_result=model(fixed_word)
    assert fixed_word[-2:]==h[-2:] and fixed_cost<=k and fixed_result['V']==0 and fixed_result['q']==Q
    for j in range(3):fixed[j]+=probs[j]*fixed_result['tv']
   emit({'kind':'history_summary','fid':fid,'h':h,'history_probability_by_initial_law':probs,'winner_mask':winner,'winner_result':winner_result,'identity_result':identity_result,'fixed_word':fixed_word,'fixed_cost':fixed_cost,'fixed_result':fixed_result,'mass_running':mass[:],'risk_running':risk[:],'identity_running':identity[:],'fixed_running':fixed[:]})
   HC+=1
  assert mass==[F(1)]*3
  for j in range(3):
   assert identity[j]/risk[j]>=F(3,5)
   if sat:assert risk[j]==fixed[j]==Q-p and risk[j]>threshold
   else:assert risk[j]<=Q-p-delta and risk[j]<threshold
  emit({'kind':'formula_summary','fid':fid,'mass':mass,'risk':risk,'identity':identity,'fixed':fixed if sat else None,'threshold':threshold,'sat':sat,'zero_probability':zero_prob,'zero_lower_bound':lower})
  N+=1
print(json.dumps({'formulas':N,'histories':HC,'masks':NC,'initial_laws_each':3},sort_keys=True),'PASS')
