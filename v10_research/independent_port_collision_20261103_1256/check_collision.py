from fractions import Fraction as F
from pathlib import Path
import json,sys

def stats(word):
 pairs=[(word[i-2:i],int(word[i])) for i in range(2,len(word))]
 s=word[-2:]
 return len(pairs),sum(pair==s for pair,y in pairs),sum(y for pair,y in pairs),sum(y for pair,y in pairs if pair==s),s

def fstr(x):return str(x)
output=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('exact_cases.jsonl')
with output.open('x',encoding='utf8') as out:
 count=0
 for n in range(1,9):
  for k in range(9):
   for d in range(1,n+1):
    tail='10'+'10'*k+'0'
    a='00'+'010100'*n+tail
    b='00'+'100100'*d+'010100'*(n-d)+tail
    m,j,c_all,ca,query=stats(a);m2,j2,c_all2,cb,query2=stats(b)
    assert (m,j,c_all,ca,query)==(6*n+3+2*k,2*n+1,2*n+k+1,n+1,'00')
    assert (m2,j2,c_all2,cb,query2)==(m,j,c_all,n+d+1,'00')
    for gamma in (F(1,10),F(1,2),F(1),F(3),F(10)):
     r=F(c_all,m);h=F(j,m)
     qa=(c_all+gamma*ca)/(m+gamma*j);qb=(c_all+gamma*cb)/(m+gamma*j)
     mid=(qa+qb)/2;e=gamma*d/(2*(m+gamma*j));ba=F(ca+1,j+2);bb=F(cb+1,j+2);lb=F(d,2*(j+2))
     assert abs(qa-mid)==abs(qb-mid)==e and bb-ba==2*lb and 0<=mid<=1
     rec={'n':n,'k':k,'d':d,'word_a':a,'word_b':b,'m':m,'J':j,'C_all':c_all,'C_a':ca,'C_b':cb,'query':query,'gamma':fstr(gamma),'r':fstr(r),'h':fstr(h),'q_a':fstr(qa),'q_b':fstr(qb),'q_mid':fstr(mid),'max_port_error':fstr(e),'B_a':fstr(ba),'B_b':fstr(bb),'fidelity_lower_bound':fstr(lb),'passed':True}
     out.write(json.dumps(rec,sort_keys=True,separators=(',',':'))+'\n');count+=1
print('Exact collision cases:',count,'all passed; output:',output)
