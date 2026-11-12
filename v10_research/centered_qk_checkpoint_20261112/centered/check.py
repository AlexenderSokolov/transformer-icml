import math,random,json,hashlib
from pathlib import Path
if not __debug__:raise RuntimeError('Run without -O')
rng=random.Random(811);checks=0
for n in [1,2,3,8,32]:
 for trial in range(20):
  d=3;K=[[rng.uniform(-1,1)/math.sqrt(n) for _ in range(d)] for j in range(n)];shift=[rng.uniform(-30,30) for _ in range(d)];Ks=[[x+s for x,s in zip(row,shift)] for row in K];q=[rng.uniform(-1,1) for _ in range(d)];vals=[rng.uniform(-1,1) for _ in range(n)]
  fullmean=[sum(row[k] for row in K)/n for k in range(d)];fullvar=sum(sum((x-m)**2 for x,m in zip(row,fullmean)) for row in K)
  for i in range(1,n+1):
   mean=[sum(row[k] for row in K[:i])/i for k in range(d)];center=[[x-m for x,m in zip(row,mean)] for row in K[:i]];F=math.sqrt(sum(x*x for row in center for x in row));scores=[sum(x*y for x,y in zip(row,q)) for row in K[:i]];score2=[sum(x*y for x,y in zip(row,q)) for row in Ks[:i]]
   def soft(s):
    e=[math.exp(x-max(s)) for x in s];return [x/sum(e) for x in e]
   aa,bb=soft(scores),soft(score2);assert max(abs(x-y) for x,y in zip(aa,bb))<1e-12;assert F*F<=fullvar+1e-12
   read=sum(x*y for x,y in zip(aa,vals[:i]));mu=sum(vals[:i])/i;omega=max(scores)-min(scores);bd=math.exp(omega)*math.sqrt(sum(x*x for x in q))*F/math.sqrt(i)
   assert abs(read-mu)<=bd+1e-12;checks+=3
p=Path(__file__).parent
r={'checks':checks,'seed':811,'configurations':100,'scope':'gauge invariance, prefix SSE and deterministic softmax norm bound; not statistical risk validation'}
(p/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
(p/'RECEIPT.json').write_text(json.dumps({'sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.name!='RECEIPT.json' and f.is_file()}},indent=2)+'\n')
