import os,sys,json,math,collections,hashlib,itertools
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent.parent; D=R/'exact_dp_pilot_20261103'
sys.path.insert(0,str(R/'learned_position_pilot_20261103'));import pilot
records=[json.loads(x) for f in ('results.jsonl','followup_results.jsonl') for x in (D/f).read_text().splitlines()]
data=json.loads((D/'data.json').read_text()); raw=json.loads((D/'randomness_replayed.json').read_text());
def st(w):
 m=len(w)-2; u=w[m:]; triples=[(i,int(w[i+2])) for i in range(m) if w[i:i+2]==u]; j=len(triples);c=sum(b for _,b in triples);d=sum(i<m//2 for i,_ in triples); e=1/math.sqrt(m); q=(1-2*e)*(c/j if j and 512*d>=j else int(u[0]))+e; return j,c,d,q
def score(p,q):return -p*math.log(q)-(1-p)*math.log1p(-q)
def legal(h,z,k):return len(z)==len(h) and z[-2:]==h[-2:] and sum(a!=b for a,b in zip(h[:-2],z[:-2]))<=k
def dp(h,k):
 # Independent rolling dictionary mapping (last two bits,J,C,D) to min cost.
 m=len(h)-2;u=h[-2:];S={}
 for a,b in itertools.product('01',repeat=2):
  cost=(a!=h[0])+(b!=h[1]);
  if cost<=k:S[(a+b,0,0,0)]=cost
 for t in range(2,m+2):
  T={}
  for (pair,j,c,d),cost in S.items():
   for b in ('01' if t<m else h[t]):
    co=cost+(t<m and b!=h[t]); match=pair==u; key=(pair[1]+b,j+match,c+(int(b) if match else 0),d+(match and t-2<m//2))
    if co<=k and co<T.get(key,999): T[key]=co
  S=T
 e=1/math.sqrt(m); jc=st(h);p=(jc[1]+1)/(jc[0]+2)
 return max(score(p,(1-2*e)*(c/j if j and 512*d>=j else int(u[0]))+e) for pair,j,c,d in S)
for a,b in zip(data,raw):
 assert all(a[k]==b[k] for k in ('M','source_index','start_pair','table','word'))
 z=[b['start_pair']//2,b['start_pair']%2]
 for r in b['uniforms']:z.append(int(r<b['table'][2*z[-2]+z[-1]]))
 assert ''.join(map(str,z))==a['word']
assert len(records)==45
cnt=collections.Counter();gaps=[]; independent=0
for r in records:
 h=r['h'];k=r['k'];m=r['M']; row=r['source_index']; assert h==next(x['word'] for x in data if x['M']==m and x['source_index']==row)
 j,c,d,q=st(h);p=(c+1)/(j+2);assert abs(p-r['clean_b'])<1e-14
 assert abs(q-float(pilot.statistics(np.array([[int(x) for x in h]],dtype=np.int8))['Q'][0]))<1e-14
 P=r['proposal']; expected=[];w=np.array([[int(x) for x in h]],dtype=np.int8)
 for fam in ('training','heldout'):
  for i,z in enumerate(pilot.proposals(w,k,fam)[:,0,:]):expected.append((fam,i,''.join(map(str,z))))
 assert len(expected)==len(P['candidates'])
 for (fam,i,z),candidate in zip(expected,P['candidates']):
  assert (fam,i,z)==(candidate['family'],candidate['index'],candidate['word']) and legal(h,z,k)
  assert abs(candidate['objective']-score(p,st(z)[3]))<1e-12
 assert P['word']==P['candidates'][P['selected']]['word'] and abs(P['objective']-max(c['objective'] for c in P['candidates']))<1e-12
 E=r['exact_dp'];cnt[E['status']]+=1
 if E['status']=='ok':
  z=E['word'];assert legal(h,z,k);j,c,d,q=st(z);assert (j,c,d)==(E['j'],E['c'],E['d']); assert abs(E['objective']-score(p,q))<1e-12
  assert E['objective']+1e-12>=P['objective'];gap=E['objective']-P['objective'];assert abs(gap-E['advantage_over_proposals'])<1e-12;gaps.append(gap)
  assert abs(r['exact_abs_error']-abs(q-r['post_selection_true_q']))<1e-12
  if True:
   assert abs(dp(h,k)-E['objective'])<1e-12;independent+=1
 assert abs(r['clean_abs_error']-abs(st(h)[3]-r['post_selection_true_q']))<1e-12
 assert abs(r['proposal_abs_error']-abs(st(P['word'])[3]-r['post_selection_true_q']))<1e-12
 assert r['post_selection_true_q']==next(x['table'][int(h[-2:],2)] for x in data if x['M']==m and x['source_index']==row)
print('records',len(records),'statuses',cnt,'independent DP optima',independent)
print('gap positive',sum(x>1e-12 for x in gaps),'tied',sum(abs(x)<=1e-12 for x in gaps),'range',min(gaps),max(gaps))
for subset in (records[:36],records[36:]):
 print('subset',len(subset),'positive',sum(r['exact_dp'].get('advantage_over_proposals',0)>1e-12 for r in subset),'max gap',max(r['exact_dp'].get('advantage_over_proposals',0) for r in subset),'error exact>proposal',sum(r.get('exact_abs_error',0)>r['proposal_abs_error']+1e-12 for r in subset),'error exact<proposal',sum(r.get('exact_abs_error',0)+1e-12<r['proposal_abs_error'] for r in subset))
print('PASS all candidate lists regenerated, candidate and witness legality, scores, objectives, saved randomness replay, diagnostics')
