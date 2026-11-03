from fractions import Fraction
import json,importlib.util,hashlib,ast
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("scalar_review",ROOT/"program.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
old=ast.parse((ROOT/"revision_scalar_extraction/program.py").read_text()); new=ast.parse((ROOT/"program.py").read_text())
olddefs={x.name:ast.dump(x) for x in old.body if isinstance(x,(ast.FunctionDef,ast.ClassDef))}
newdefs={x.name:ast.dump(x) for x in new.body if isinstance(x,(ast.FunctionDef,ast.ClassDef))}
assert all(newdefs[name]==body for name,body in olddefs.items())
# Independent literal ReLU recurrence on exact rational scalar-grid inputs.
def extract(H,h):
    A=(1<<h)*H; result=[]
    for j in range(h,-1,-1):
        b=max(A-((1<<j)-1),0)-max(A-(1<<j),0)
        assert b in (0,1)
        A=A-(1<<j)*b
        assert 0<=A<(1<<j)
        result.append(int(b))
    assert A==0
    return tuple(reversed(result))
cases=0
for h in range(13):
    for B in range((1<<h)+1):
        bits=extract(Fraction(B,1<<h),h)
        assert m.scalar_grid_bits(Fraction(B,1<<h),h)==bits
        assert len(bits)==h+1 and sum(v<<i for i,v in enumerate(bits))==B
        cases+=1
# This bridge intentionally is NOT extraction on arbitrary off-grid scalars.
A=Fraction(1,2)
b=max(A,0)-max(A-1,0)
assert b==Fraction(1,2)
print(json.dumps({'status':'PASS','program_sha256':hashlib.sha256((ROOT/'program.py').read_bytes()).hexdigest(),'prior_datapath_AST_unchanged':True,'canonical_grid_cases':cases,'h_range':[0,12],'H=0_H=1_h=0_included':True,'off_grid_not_a_bit_confirmed':True},sort_keys=True,indent=2))
