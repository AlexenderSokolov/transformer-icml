import itertools,json,math
from fractions import Fraction as F
from pathlib import Path

out=Path(__file__).with_name('exhaustive_cases_v1.jsonl')
def qrepr(x):
 return {'numerator':x.numerator,'denominator':x.denominator}
def gate(A,v):
 a=2*A+2*v-F(9,2); b=2*A+2*v-F(11,2)
 return max(F(0),a)-max(F(0),b)
count=0
with out.open('x') as f:
 for N in range(3,9):
  for ed in (4,32):
   eta=F(1,ed); b=math.ceil(math.log2(N*ed)); c=math.ceil(math.log2(32*(N+1)))
   for bits in itertools.product((0,1),repeat=N):
    history=[]; max_error=F(0); all_gates=True
    for i in range(1,N+1):
     copies=[]
     for lag in (1,2):
      weights=[2**c if j==i-lag else 1 for j in range(1,i+1)]
      copy=F(sum(w*bits[j-1] for j,w in enumerate(weights,1)),sum(weights)); copies.append(copy)
      if i>=3: max_error=max(max_error,abs(copy-bits[i-lag-1]))
     v=int(i>=3)
     hist=[gate((copies[1] if a else 1-copies[1])+(copies[0] if z else 1-copies[0]),v) for a,z in itertools.product((0,1),repeat=2)]
     query=[gate((copies[0] if a else 1-copies[0])+(F(bits[i-1]) if z else 1-F(bits[i-1])),v) for a,z in itertools.product((0,1),repeat=2)]
     if i>=3:
      hs=2*bits[i-3]+bits[i-2]; qs=2*bits[i-2]+bits[i-1]
      all_gates &= hist==[F(int(x==hs)) for x in range(4)] and query==[F(int(x==qs)) for x in range(4)]
     else: all_gates &= all(x==0 for x in hist+query)
     history.append((hist,query))
    q=history[-1][1]; term=(bits[-2],bits[-1]); J=C=0
    numerator=F(0); denominator=0
    for j in range(1,N+1):
     flag=int(j==1); key=history[j-1][0]
     match=sum(a*z for a,z in zip(q,key)); assert match in (0,1)
     weight=2**(b+1) if flag else 2**b if match else 1
     y=F(1,2) if flag else F(bits[j-1]); numerator+=weight*y; denominator+=weight
     if j>=3 and (bits[j-3],bits[j-2])==term: J+=1; C+=bits[j-1]
    p=numerator/denominator; B=F(C+1,J+2); err=abs(p-B)
    bound=F(N-1-J,2**b*(J+2)+N-1-J)
    passed=all_gates and max_error<=F(1,32) and err<=bound<=F(N,2**(b+1))<=eta/2
    row={'schema':'no_bos_all_words_v1','N':N,'bits':''.join(map(str,bits)),'eta':qrepr(eta),'b':b,'c':c,'terminal':list(term),'J':J,'C':C,'copy_max_error':qrepr(max_error),'gates_exact':bool(all_gates),'head_output':qrepr(p),'add_one':qrepr(B),'absolute_error':qrepr(err),'contamination_bound':qrepr(bound),'passed':bool(passed)}
    f.write(json.dumps(row,separators=(',',':'))+'\n'); count+=1
    assert passed,row
print(f'PASS {count} full deterministic cases; every record retained; N=3..8 eta=1/4,1/32; no RNG')
