import json,math,itertools,hashlib,numpy as np
from pathlib import Path
P=Path(__file__).resolve().parents[1]; data=json.load(open(P/'data.json'));old=[json.loads(s) for s in open(P/'results.jsonl')];follow=[json.loads(s) for s in open(P/'followup_results.jsonl')];archive=json.load(open(P/'randomness_replayed.json'));assert (len(data),len(old),len(follow),len(archive))==(12,36,9,12)
def stats(w):
 M=len(w)-2;J=C=D=0
 for i in range(M):
  if w[i:i+2]==w[-2:]:J+=1;C+=int(w[i+2]);D+=int(i<M//2)
 a=C/J if J and 512*D>=J else int(w[-2]);s=1/math.sqrt(M);return J,C,D,(1-2*s)*a+s
def ce(p,q):return -p*math.log(q)-(1-p)*math.log1p(-q)
def propositions(w,k):
 m=len(w)-2;out=[]
 for family in ('training','heldout'):
  inds=[range(s,s+k) for s in [0,(m-k)//2,m-k]] if family=='training' else [range(s,s+k) for s in [(m-k)//4,3*(m-k)//4]]+[np.floor(np.linspace(0,m-1,k)).astype(int)]
  out.append((family,0,w));index=1
  for positions in inds:
   for op in range(3):
    z=list(w)
    for i in positions:z[i]=str(op) if op<2 else str(1-int(w[i]))
    out.append((family,index,''.join(z)));index+=1
 return out
r=np.random.default_rng(845120)
for d,a in zip(data,archive):
 M=d['M'];start=int(r.integers(0,4));u=r.random(M);z=[start//2,start%2]
 for v in u:z.append(int(v<d['table'][2*z[-2]+z[-1]]))
 assert ''.join(map(str,z))==d['word']==a['word'] and start==d['start_pair']==a['start_pair'] and list(u)==a['uniforms']
print('12 historical words/starts/tables/seeded draws independently reconstructed; RNG archive is retrospective')
maxerr=0.;positive=0;neg_tv=0;zero_gap=0; status={};counts={};wall=[];internal=[]
for row in old+follow:
 w=row['h'];m=row['M'];k=row['k'];J,C,D,Q=stats(w);p=(C+1)/(J+2); assert abs(p-row['clean_b'])<1e-14
 expected=propositions(w,k);actual=row['proposal']['candidates'];assert len(expected)==len(actual)==20
 for (fam,idx,z),c in zip(expected,actual):
  assert (fam,idx,z)==(c['family'],c['index'],c['word']);assert z[-2:]==w[-2:] and sum(x!=y for x,y in zip(z[:m],w[:m]))<=k;maxerr=max(maxerr,abs(ce(p,stats(z)[3])-c['objective']))
 sc=[ce(p,stats(z)[3]) for _,_,z in expected];chosen=max(range(len(sc)),key=lambda i:sc[i]);assert chosen==row['proposal']['selected'] and expected[chosen][2]==row['proposal']['word'];assert abs(sc[chosen]-row['proposal']['objective'])<1e-12
 dp=row['exact_dp'];status[dp['status']]=status.get(dp['status'],0)+1;counts[(m,k)]=counts.get((m,k),0)+1
 if dp['status']=='ok':
  z=dp['word'];assert len(z)==len(w) and z[-2:]==w[-2:] and sum(x!=y for x,y in zip(z[:m],w[:m]))<=k;j,c,d,q=stats(z);assert (j,c,d)==(dp['j'],dp['c'],dp['d']);obj=ce(p,q);maxerr=max(maxerr,abs(obj-dp['objective']));assert abs((obj-sc[chosen])-dp['advantage_over_proposals'])<1e-12 and obj>=sc[chosen]-1e-12;positive+=obj>sc[chosen]+1e-12;zero_gap+=abs(obj-sc[chosen])<=1e-12
  dat=next(t for t in data if t['M']==m and t['source_index']==row['source_index']);truth=dat['table'][int(w[-2:],2)];assert truth==row['post_selection_true_q'];assert abs(row['clean_abs_error']-abs(Q-truth))<1e-14 and abs(row['proposal_abs_error']-abs(stats(row['proposal']['word'])[3]-truth))<1e-14 and abs(row['exact_abs_error']-abs(q-truth))<1e-14;neg_tv+=row['exact_abs_error']<row['proposal_abs_error']-1e-12
  if 'entire_case_wall_s' in row:wall.append(row['entire_case_wall_s']);internal.append(dp['wall_s'])
print('records',len(old)+len(follow),'statuses',status,'positive CE gap',positive,'ties <=1e-12',zero_gap,'DP lower source-TV than proposal',neg_tv,'max objective discrepancy',maxerr)
print('followup total-case wall range',min(wall),max(wall),'internal C++ range',min(internal),max(internal),'isolated subprocess elapsed not saved')
for m in [16,32]:
 for d in [x for x in data if x['M']==m]:
  w=d['word'];J,C,_,_=stats(w);p=(C+1)/(J+2);best=-1
  for j in range(5):
   for idx in itertools.combinations(range(m),j):
    z=list(w)
    for i in idx:z[i]='1' if z[i]=='0' else '0'
    best=max(best,ce(p,stats(''.join(z))[3]))
  row=next(r for r in old if r['M']==m and r['source_index']==d['source_index'] and r['k']==4); assert abs(best-row['exact_dp']['objective'])<1e-12;print('independent all-mask numerical max agrees M',m,'source',d['source_index'],'k=4')
for file in ['PRE_RUN_SHA256.txt','FOLLOWUP_PRE_RUN_SHA256.txt']:
 bad=[];ls=(P/file).read_text().splitlines()
 for line in ls:
  digest,name=line.split(maxsplit=1);f=P/name.strip()
  if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=digest:bad.append(name)
 print(file,'count',len(ls),'bad',bad)
tests=[json.loads(x) for x in open(P/'test_cases.jsonl')];assert len(tests)==448
for rec in tests:
 w=rec['h'];m=len(w)-2;k=rec['k'];J,C,D,Q=stats(w);p=(C+1)/(J+2);best=-1.;near=[]
 for j in range(k+1):
  for ix in itertools.combinations(range(m),j):
   z=list(w)
   for i in ix:z[i]='1' if z[i]=='0' else '0'
   z=''.join(z);score=ce(p,stats(z)[3]);
   if score>best+1e-12:best=score;near=[z]
   elif abs(score-best)<=1e-12:near.append(z)
 z=rec['word'];assert z[-2:]==w[-2:] and sum(x!=y for x,y in zip(z[:m],w[:m]))<=k and abs(ce(p,stats(z)[3])-best)<1e-12 and abs(rec['objective']-best)<1e-12 and abs(rec['oracle_best']-best)<1e-12 and rec['oracle_maximizer_count']==len(near) and rec['status']=='pass'
print('all 448 retained test rows and masked oracles independently recomputed')
import gzip
archives=[]
with gzip.open(P/'test_oracle_candidates.jsonl.gz','rt') as f:
 for s in f:archives.append(json.loads(s))
expected=0
for index,t in enumerate(tests):
 w=t['h'];m=len(w)-2;J,C,_,_=stats(w);p=(C+1)/(J+2)
 for j in range(t['k']+1):
  for ix in itertools.combinations(range(m),j):
   a=archives[expected];z=list(w)
   for i in ix:z[i]='1' if z[i]=='0' else '0'
   z=''.join(z);jj,cc,dd,q=stats(z);assert (a['case'],a['flips'],a['word'],a['j'],a['c'],a['d'])==(index,list(ix),z,jj,cc,dd) and abs(a['q']-q)<1e-15 and abs(a['objective']-ce(p,q))<1e-15;expected+=1
assert len(archives)==expected;print('retrospective oracle-candidate archive checked',expected,'records')
