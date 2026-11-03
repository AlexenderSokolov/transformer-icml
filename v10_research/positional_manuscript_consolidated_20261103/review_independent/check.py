"""Independent integration diagnostics. No author or historical file is modified.

Run from any working directory. Diagnostics do not replace the all-horizon proofs.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D, getcontext
from itertools import product
from hashlib import sha256
import json, math, random, re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PAPER = HERE.parent
OLD = ROOT / 'v10_research/resumption_20261103/recovered_science/positional_manuscript_finite_20261102'
REC = ROOT / 'resumption_20261103/remote_recovery/files'
PROGRAM = ROOT / 'v10_research/finite_positional_attention_20261103/program.py'
getcontext().prec = 100

def digest(p):
    return {'sha256': sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size}

results = {}
scientific_files=[PAPER/'main.tex',PAPER/'references.bib',*sorted((PAPER/'sections').glob('*.tex'))]
initial_hashes={str(p.relative_to(PAPER)):digest(p)['sha256'] for p in scientific_files}
freeze=json.loads((PAPER/'verification/SCIENTIFIC_SOURCE_FREEZE.json').read_text())
assert initial_hashes==freeze['files'], 'Scientific source freeze differs from actual files'
source_bindings=json.loads((PAPER/'SOURCE_BINDINGS.json').read_text())
for rel,binding in source_bindings['files'].items():
    assert digest(ROOT/rel)=={'sha256':binding['sha256'],'bytes':binding['bytes']},rel
claims=json.loads((PAPER/'CLAIM_TO_SOURCE.json').read_text())['claims']
for claim in claims:
    assert digest(ROOT/claim['source'])['sha256']==claim['source_sha256']
results['source_bindings_verified']=len(source_bindings['files'])
results['claim_bindings_verified']=len(claims)
companion=json.loads((PAPER/'COMPANION_CONTEXT.json').read_text())
for rel,h in companion['source_sha256'].items():
    assert digest(REC/rel)['sha256']==h,rel
results['companion_source_bindings_verified']=len(companion['source_sha256'])
for name in ['proofs_positive.tex', 'proofs_negative.tex', 'proofs_finite_horizon.tex']:
    assert (PAPER/'sections'/name).read_bytes() == (OLD/'sections'/name).read_bytes()
    results['byte_identical:'+name] = digest(PAPER/'sections'/name)

texts = '\n'.join(p.read_text() for p in [PAPER/'main.tex', *sorted((PAPER/'sections').glob('*.tex'))])
labels = re.findall(r'\\label\{([^}]+)\}', texts)
refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', texts)
assert len(labels) == len(set(labels)), 'Duplicate LaTeX labels'
assert not (set(refs)-set(labels)), sorted(set(refs)-set(labels))
cites = set()
for block in re.findall(r'\\cite\w*(?:\[[^]]*\])?\{([^}]+)\}', texts):
    cites.update(k.strip() for k in block.split(','))
bibkeys = set(re.findall(r'@\w+\s*\{([^,]+),', (PAPER/'references.bib').read_text()))
assert cites <= bibkeys, cites-bibkeys
results['latex_reference_checks'] = {'unique_labels':len(labels),'references':len(refs),'cited_keys':len(cites)}

# Reconcile exact recorded original/public pairs, not just similar names.
recon = json.loads((REC/'provenance/increment3/BINDING_RECONCILIATION.json').read_text())
source = json.loads((REC/'provenance/increment3/SOURCE_MAP.json').read_text())
pathset = {
 'v10_research/balanced_joint_finite_cut/BCJ001_HANDOFF.md',
 'v10_research/balanced_joint_finite_cut/BCJ001_accepted_bindings.json',
 'v10_research/balanced_joint_finite_cut/BCJ001_independent_full_review.md',
 'v10_research/binary_full_history_domain/AF001_full_history_domain_classification.md',
}
verified = []
for entry in recon['new_pairs']:
    if entry['path'] not in pathset:
        continue
    same = next(x for x in source['files'] if x['path'] == entry['path'])
    assert entry['original_sha256'] == same['original_sha256']
    assert entry['public_export_sha256'] == same['public_export_sha256']
    assert digest(REC/entry['path'])['sha256'] == entry['public_export_sha256']
    verified.append(entry)
assert len(verified)==len(pathset)
results['verified_original_export_pairs'] = verified
for unit, rel in [('BCJ001','balanced_joint_finite_cut/BCJ001_theorem.md'),
                  ('AB001','binary_budget_adaptation/AB001_joint_blindness_obstruction.md')]:
    expected={'BCJ001':'95d5aac1ee2504955e55c1e82241c8a07d219661e2620c6e083acf5c8701554d',
              'AB001':'865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d'}[unit]
    assert digest(REC/'v10_research'/rel)['sha256']==expected
    results['exact_antecedent:'+unit]=expected

# Finite-window upper domain, including overlapping and full windows.
count = 0
for M in range(64,257):
    for r in range(2,M+3):
        m=min(r-2,M//2)
        assert F(M,m+1) <= max(F(2*M,r),2) <= F(2*(M+2),r)
        count+=1
results['finite_upper_pairs']=count

def ceilroot4(a):
    lo=0; hi=1<<((a.bit_length()+3)//4)
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**4<a:lo=mid
        else:hi=mid
    return hi

large=[]
for exponent in [92,128,256,512,1024]:
    for M in [2**exponent-1,2**exponent,2**exponent+1]:
        q=ceilroot4(M**3)
        boundary=int(D(M+2)/D(63).exp())
        for r in sorted({2,max(2,q//128-1),max(2,q//128+1),max(2,boundary-1)}):
            ell=1+(D(M+2)/D(r)).ln()
            if ell<64:continue
            k=max(128*r,q);c=F(1,2**16);t=c*k/M;u=(c*k)//4
            assert k<=F(M,8) and r<=F(k,128) and c*k>=1024
            assert F(M,k*k)<=F(1,2**40) and 2**12*t<F(1,4)
            assert F(u)/(8*M*t)>=F(1,64)
            assert ell/D(2**30)/D(M).sqrt()<D(t.numerator)/D(t.denominator)/32
            assert (4*D(M)/D(k)).ln()>=ell/8
            large.append({'exponent':exponent,'M':str(M),'r':str(r),'k':str(k)})
results['finite_lower_large_cases']=len(large)
assert F(1,64)*F(1,32)*F(1,8)*F(1,2**16)==F(1,2**30)

# Direct independent count and rational readout oracles.
ns={}
exec(compile(PROGRAM.read_text(),str(PROGRAM),'exec'),ns)
def counts(z):
    M=len(z)-2;out=[]
    for a,c in product((0,1),repeat=2):
        row=[i for i in range(M) if z[i]==a and z[i+1]==c]
        out.extend((len(row),sum(z[i+2]==1-a for i in row),sum(i<M//2 for i in row)))
    return out

def oracle(bank,endpoint,b):
    J,C,H=bank[3*(2*endpoint[0]+endpoint[1]):][:3]
    C=min(C,J);H=min(H,J)
    q=F(C,J) if J and 512*H>=J else F(0)
    v=(q.numerator*(1<<b))//q.denominator
    pair=(v,(1<<b)-v) if endpoint[0] else ((1<<b)-v,v)
    return pair,q

rng=random.Random(20261103)
words=[z for M in range(1,6) for z in product((0,1),repeat=M+2)]
for M in [64,65,127,128,129,256]:
    words += [(0,)*(M+2),(1,)*(M+2),tuple(i%2 for i in range(M+2)),
              tuple(rng.randrange(2) for _ in range(M+2))]
banktests=outtests=0
for z in words:
    M=len(z)-2;cs=counts(z)
    for h in (0,1,4):
        Q=1<<h;cut=ns['prefix'](z,h)
        exact=tuple((2*Q*c+M)//(2*M) for c in cs)
        assert set(cut)=={'bank','endpoint','h'} and cut['endpoint']==z[-2:]
        assert cut['bank']==exact
        assert all(abs(F(b,Q)-F(c,M))<=F(1,2*Q) for b,c in zip(exact,cs))
        banktests+=1
        for b in (0,2,7):
            want,q=oracle(exact,z[-2:],b)
            got=ns['readout'](cut,b)
            assert got==want and sum(got)==1<<b and min(got)>=0
            assert abs(F(got[1-z[-2]],1<<b)-q)<=F(1,1<<b)
            outtests+=1
results['direct_bank_cases']=banktests
results['exact_output_cases']=outtests

faults=0
for h in [0,1,5,10]:
    Q=1<<h
    banks=[tuple(rng.randrange(Q+1) for _ in range(12)) for _ in range(50)]
    if h==10:
        banks += [(j,c,d)+(0,)*9 for j,c,d in [(0,0,0),(511,123,1),(512,123,1),(513,123,1),(4,9,8)]]
    for bank in banks:
        for endpoint in product((0,1),repeat=2):
            for b in [0,3,10]:
                cut={'bank':bank,'endpoint':endpoint,'h':h}
                assert ns['readout'](cut,b)==oracle(bank,endpoint,b)[0]
                faults+=1
results['canonical_fault_readouts']=faults
extract=0
for h in range(11):
    for v in range((1<<h)+1):
        got=ns['scalar_grid_bits'](F(v,1<<h),h)
        assert got==tuple((v>>j)&1 for j in range(h+1))
        extract+=1
results['scalar_grid_extractions']=extract

batch=0
original=ns['readout']
for M in [1,2,5,64,65]:
    z=tuple(rng.randrange(2) for _ in range(M+2)); seen=[]
    def spy(cut,b):
        seen.append(cut.copy());return original(cut,b)
    ns['readout']=spy
    got=ns['evaluate'](z,4,7)
    assert len(seen)==M+3 and all(x['bank']==(0,)*12 for x in seen[:-1])
    assert got==oracle(seen[-1]['bank'],z[-2:],7)[0]
    batch+=1
ns['readout']=original
results['all_token_suffix_cases']=batch

# Real perturbation/clipping proof: rational cases close to gate boundaries.
clip=lambda x,a,b:min(b,max(a,x))
perturb=0
for J in [0,1,2,3,4,255,256,511,512,513,1024,4096]:
    M=max(64,J)
    for C in sorted({0,J//2,J}):
        for H in sorted({0,J//1024,J//512,J//256,J}):
            for e in [F(0),F(1,10000),F(1,2),F(1),F(7,2)]:
                for sj,sc,sd in product((-1,0,1),repeat=3):
                    jb=clip(F(J)+sj*e,0,M)
                    cb=clip(F(C)+sc*e,0,jb)
                    hb=clip(F(H)+sd*e,0,jb)
                    assert max(abs(jb-J),abs(cb-C),abs(hb-H))<=e
                    hat=F(cb)/F(jb) if jb>0 and 512*hb>=jb else F(0)
                    w1=max(1,math.ceil(1026*e));w2=max(1,math.ceil(513*e))
                    assert w1+w2<=1539*e+2
                    for q in [F(0),F(1,3),F(1)]:
                        rhs=(abs(F(C,J)-q) if J else F(0))
                        rhs+=8*e*int(1024*H>=J)/(J+1)
                        rhs+=q*int(J>0 and 256*H<J)+int(J<w1)+int(J<w2)
                        assert abs(hat-q)<=rhs
                    perturb+=1
results['real_radius_pathwise_cases']=perturb
assert 8*130944+16*(1026+513)==1072176
assert 1072176*6==6433056
assert 1072176//2==536088 and 131072+536088==667160
assert 500000000>30*3744**2
assert sum(F(6**i,math.factorial(i)) for i in range(11))>384
results['exact_constants']=True

# Explicit word collision in the main text.
z0=tuple(map(int,'0100'+'1'*62+'0')); z1=tuple(map(int,'0'+'1'*62+'0010'))
hist=lambda z:tuple(sum(z[i:i+3]==bits for i in range(len(z)-2)) for bits in product((0,1),repeat=3))
assert hist(z0)==hist(z1)==(0,1,1,1,1,0,1,60)
assert z0[:2]==z1[:2]==(0,1) and z0[-2:]==z1[-2:]==(1,0)
assert counts(z0)[6:9]==[1,1,1] and counts(z1)[6:9]==[1,1,0]
results['word_collision']=True
results['status']='PASS'
results['scope']='Finite diagnostics and exact integration checks, not formal verification or a substitute for full proofs.'
results['program']=digest(PROGRAM)
assert initial_hashes=={str(p.relative_to(PAPER)):digest(p)['sha256'] for p in scientific_files}, 'Source changed during checks'
results['checked_content']={str(p.relative_to(ROOT)):digest(p) for p in scientific_files}
(HERE/'checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({k:v for k,v in results.items() if not isinstance(v,(dict,list))},indent=2))
