from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import json,sys
root=Path(__file__).parent
inp=root/'exact_cases.jsonl'; outp=Path(sys.argv[1]) if len(sys.argv)>1 else root/'positionwise_cases.jsonl'
def counts(word):
 return Counter((word[i-2:i],int(word[i])) for i in range(2,len(word)))
with inp.open() as src,outp.open('x',encoding='utf8') as out:
 ct=0
 for line in src:
  x=json.loads(line);a,b=counts(x['word_a']),counts(x['word_b']);n,k,d=x['n'],x['k'],x['d']
  rows=['00','01','10','11'];ja={s:sum(a[s,z] for z in (0,1)) for s in rows};jb={s:sum(b[s,z] for z in (0,1)) for s in rows}
  assert ja==jb=={'00':2*n+1,'01':2*n+k+1,'10':2*n+k+1,'11':0}
  assert b['00',1]-a['00',1]==d and b['10',1]-a['10',1]==-d and b['01',1]-a['01',1]==0
  ratio=1+F(x['gamma']);score={'00':ratio**2,'01':ratio,'10':ratio,'11':F(1)}
  W=sum(score[s]*ja[s] for s in rows)
  qa=sum(score[s]*a[s,1] for s in rows)/W;qb=sum(score[s]*b[s,1] for s in rows)/W
  threshold=F(d,2)*(ratio**2-ratio)/W
  assert qb-qa==2*threshold
  y={'n':n,'k':k,'d':d,'e_beta':str(ratio),'row_occupancies':ja,'word_a':x['word_a'],'word_b':x['word_b'],'W':str(W),'q_a':str(qa),'q_b':str(qb),'midpoint':str((qa+qb)/2),'required_q_error':str(threshold),'fidelity_lower_bound':x['fidelity_lower_bound'],'passed':True}
  out.write(json.dumps(y,sort_keys=True,separators=(',',':'))+'\n');ct+=1
print('Positionwise-weight rational cases:',ct,'all passed; output:',outp)
