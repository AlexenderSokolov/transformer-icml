#!/usr/bin/env python3
"""Reconstruct all original independent-test RNG states and enumerate oracle candidates."""
import gzip,itertools,json,pathlib,random
from test_dp import stats,target,ce
D=pathlib.Path(__file__).resolve().parent
cases=[json.loads(s) for s in (D/'test_cases.jsonl').read_text().splitlines()]
rng=random.Random(20261103);states=[];off=320
for m in range(5,9):
    for sample in range(8):
        st=rng.getstate();h=''.join(str(rng.randrange(2)) for _ in range(m+2));end=rng.getstate()
        for k in range(4):assert cases[off]['h']==h and cases[off]['k']==k;off+=1
        states.append(dict(M=m,sample=sample,h=h,before=st,after=end))
assert off==len(cases)
(D/'test_random_states.json').write_text(json.dumps(states)+'\n')
n=0
with (D/'test_oracle_candidates.jsonl.gz').open('wb') as raw:
    with gzip.GzipFile(fileobj=raw,mode='wb',mtime=0) as g:
        for ci,c in enumerate(cases):
            h=c['h'];m=len(h)-2;p=target(h)
            for j in range(c['k']+1):
                for flips in itertools.combinations(range(m),j):
                    z=list(h)
                    for i in flips:z[i]='1' if z[i]=='0' else '0'
                    z=''.join(z);J,C,Dd,q=stats(z)
                    rec=dict(case=ci,flips=flips,word=z,j=J,c=C,d=Dd,q=q,objective=ce(p,q))
                    g.write((json.dumps(rec,separators=(',',':'))+'\n').encode());n+=1
print(f'PASS: archived states for {len(states)} seeded test histories and {n} enumerated test candidates')
