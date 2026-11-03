from itertools import product
from fractions import Fraction
from pathlib import Path
import json

# Signed integer literals. Each individual record is an original clause;
# repeated literals and duplicate/tautological clauses are preserved.
cases = [
 ('single_repeated_literal', 3, [(1,1,1)]),
 ('two_distinct_repeated', 3, [(1,2,2)]),
 ('mixed_duplicate_and_tautology', 4, [(1,1,1), (1,2,2), (1,-1,3), (1,2,3), (1,2,3), (-1,-2,-3)]),
 ('all_eight', 3, list(product(*[(i,-i) for i in (1,2,3)]))),
 ('distinct_three_plus_tautology', 4, [(1,2,3),(-1,-2,4),(1,-1,2),(1,2,3)])
]
def sat(c, x):
 return any((x[abs(a)-1] == (a > 0)) for a in c)
def score(cs, x): return sum(sat(c,x) for c in cs)
def cond(cs, prefix, n):
 vals=[score(cs, prefix+rest) for rest in product((0,1),repeat=n-len(prefix))]
 return Fraction(sum(vals),len(vals))
def s(f): return f'{f.numerator}/{f.denominator}'
out=[]
for name,n,clauses in cases:
 pre=(); init=cond(clauses,pre,n); steps=[]
 for i in range(n):
  v0=cond(clauses,pre+(0,),n); v1=cond(clauses,pre+(1,),n)
  assert (v0+v1)/2 == cond(clauses,pre,n)
  bit=int(v1>v0); steps.append({'prefix_before':list(pre),'score_0':s(v0),'score_1':s(v1),'chosen_bit':bit}); pre+=(bit,)
 achieved=score(clauses,pre); opt=max(score(clauses,x) for x in product((0,1),repeat=n))
 assert Fraction(achieved)>=init and Fraction(achieved)>=Fraction(len(clauses),2)
 qualifies=all(any(-a in c for a in c) or len(set(map(abs,c)))==3 for c in clauses)
 if qualifies: assert 8*achieved>=7*len(clauses) and 8*achieved>=7*opt
 M=1
 while M<max(n*n,len(clauses)**2,128): M*=2
 P=1
 while P<len(clauses): P*=2
 hist=tuple([1 if i%2 else 0 for i in range(M+2)])
 edited=pre+hist[n:]
 flips=[i for i in range(M) if hist[i]!=edited[i]]
 assert len(flips)<=n and edited[-2:]==hist[-2:]
 out.append({'case':name,'n':n,'original_clauses':clauses,'initial_expectation':s(init),'steps':steps,'assignment':pre,'achieved':achieved,'opt':opt,'three_distinct_or_tautology':qualifies,'M':M,'P':P,'history':hist,'edited_history':edited,'flips':flips,'risk_vanishing':s(Fraction(achieved,M*P)),'opt_risk_vanishing':s(Fraction(opt,M*P)),'risk_constant':s(Fraction(achieved,2*P)),'opt_risk_constant':s(Fraction(opt,2*P))})
path=Path(__file__).with_name('conditional_cases.jsonl')
with path.open('x') as f:
 for row in out: f.write(json.dumps(row,separators=(',',':'))+'\n')
print('PASS:',len(out),'deterministic cases; full records:',path.name)
