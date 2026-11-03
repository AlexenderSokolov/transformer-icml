import importlib.util,json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'program.py'
spec=importlib.util.spec_from_file_location('batch_review',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
original=m.readout
cases=0
for z in ((0,0,0),(1,0,1,1),(0,1,1,0,0,1,0)):
 for replacement in (None,(0,)*12,(4,)*12):
    seen=[]
    def traced(cut,r):
        seen.append(dict(cut))
        return original(cut,r)
    m.readout=traced
    actual=m.evaluate(z,2,3,replacement)
    assert len(seen)==len(z)+1
    assert all(s=={'bank':(0,)*12,'endpoint':(0,0),'h':2} for s in seen[:-1])
    cut=m.prefix(z,2)
    if replacement is not None: cut=m.replace_bank(cut,replacement)
    assert actual==original(cut,3) and seen[-1]==cut
    assert set(cut)=={'bank','endpoint','h'}
    cases+=1
print(json.dumps({'full_batch_cases':cases,'status':'PASS'},sort_keys=True,indent=2))
