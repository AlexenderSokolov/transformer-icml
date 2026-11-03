import importlib.util,itertools,random,json,hashlib
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reviewed',ROOT/'program.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
rng=random.Random(3112026)
checks={'words':0,'replacements':0,'arithmetic':0,'metadata':0}
# Independent recurrence oracle does not reuse author tests or feature construction.
def oracle(z,h):
    M=len(z)-2; a=[0]*12
    for i in range(M):
        row=2*z[i]+z[i+1]; a[3*row]+=1
        a[3*row+1]+=int(z[i+2]!=z[i])
        a[3*row+2]+=int(2*i<M-(M%2))
    return tuple((2*(1<<h)*x+M)//(2*M) for x in a),a
for M in range(1,7):
    for z in itertools.product(range(2),repeat=M+2):
        for h in (0,2,5):
            cut=mod.prefix(z,h); expect,counts=oracle(z,h)
            assert cut=={'bank':expect,'endpoint':z[-2:],'h':h}
            assert all(abs(Fraction(v,1<<h)-Fraction(c,M))<=Fraction(1,2<<h) for v,c in zip(expect,counts))
            checks['words']+=1
for M in (7,8,63,64,65,127,128,129,512,513,1024):
    masks,half=mod.metadata(M); n=M+3
    assert masks[0][-1]==(M+1,) and masks[1][-1]==(M,)
    assert masks[2][-1]==tuple(range(2,M+2))
    assert tuple(i-2 for i,x in enumerate(half) if x)==tuple(range(M//2))
    assert all(all(k<=t for k in keys) for mask in masks for t,keys in enumerate(mask))
    checks['metadata']+=1
    for z in ((0,)*(M+2),(1,)*(M+2),tuple(i%2 for i in range(M+2)),tuple(rng.randrange(2) for _ in range(M+2))):
        for h in (0,1,6):
            cut=mod.prefix(z,h); assert cut['bank']==oracle(z,h)[0]; checks['words']+=1
for _ in range(2200):
    h=rng.randrange(0,14); r=rng.randrange(0,14); Q=1<<h
    bank=tuple(rng.randrange(Q+1) for _ in range(12)); u=(rng.randrange(2),rng.randrange(2))
    j,c,d=bank[3*(2*u[0]+u[1]):3*(2*u[0]+u[1])+3]; c=min(c,j); d=min(d,j)
    expected=((1<<r)*c)//j if j>0 and 512*d>=j else 0
    output=mod.readout({'bank':bank,'endpoint':u,'h':h},r)
    assert output[1-u[0]]==expected and sum(output)==1<<r and min(output)>=0
    checks['replacements']+=1
# Inputs include full word values with no assumed spare bit.
for w in range(1,15):
    bit=mod.Bits(w); N=1<<w
    for _ in range(120):
        x=rng.randrange(N); y=rng.randrange(1,N)
        q,rem=bit.div(bit.enc(x),bit.enc(y)); assert (bit.val(q),bit.val(rem))==divmod(x,y)
        assert bit.ge(bit.enc(x),bit.enc(y))==int(x>=y)
        checks['arithmetic']+=1
# Regression at exact gate equality and both adjacent integers.
for h in (9,10,14):
    for d in range(1,min(20,(1<<h)//512)):
        for j in (512*d-1,512*d,512*d+1):
            for endpoint in itertools.product(range(2),repeat=2):
                bank=[0]*12; start=3*(2*endpoint[0]+endpoint[1]); bank[start:start+3]=[j,j,d]
                result=mod.readout({'bank':tuple(bank),'endpoint':endpoint,'h':h},7)
                assert result[1-endpoint[0]]==(128 if j<=512*d else 0)
                checks['replacements']+=1
checks['program_sha256']=hashlib.sha256((ROOT/'program.py').read_bytes()).hexdigest()
print(json.dumps(checks,indent=2,sort_keys=True))
