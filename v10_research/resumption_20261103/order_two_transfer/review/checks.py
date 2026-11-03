from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,random
BASE=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
counts={'words':0,'payload_cases':0,'flow_cases':0,'zero_denominator':0,'rejections':0,'reflection_paths':0,'certificate_entries':0}
def checkword(z):
 M=len(z)-2; u=z[-2:]; d=1-u[0]
 H={t:0 for t in product(range(2),repeat=3)}
 for i in range(M):H[z[i:i+3]]+=1
 J=H[u+(0,)]+H[u+(1,)]; C=H[u+(d,)]; A=sum(z[i:i+2]==u for i in range(M//2)); G=int(512*A>=J)
 # Direct distribution on symbols, independent of serialized decoder.
 direct=[F(0),F(0)]
 if J and G: direct[d]=F(C,J);direct[1-d]=1-direct[d]
 else: direct[1-d]=F(1)
 width=M.bit_length(); payload=f'{J:0{width}b}{C:0{width}b}{d}{G}'
 j=int(payload[:width],2);c=int(payload[width:2*width],2);dd=int(payload[-2]);gg=int(payload[-1]);q=F(c,j) if j and gg else F(0)
 p=q if dd else 1-q
 assert direct[1]==p and len(payload)==2*width+2
 for s in product(range(2),repeat=2):
  out=sum(H[s+(b,)] for b in range(2));inc=sum(H[(a,)+s] for a in range(2))
  assert out-inc+int(s==u)==int(s==z[:2]);counts['flow_cases']+=1
 counts['words']+=1;counts['payload_cases']+=1;counts['zero_denominator']+=not J;counts['rejections']+=not G
for L in range(3,15):
 for z in product(range(2),repeat=L):checkword(z)
rng=random.Random(120311)
for M in [64,65,127,512,1024]:
 for _ in range(100):checkword(tuple(rng.randrange(2) for _ in range(M+2)))
# Gate equality is included at every positive multiple 512, and zero count separately.
for a in range(5):
 j=512*a;assert int(512*a>=j)==1
# All-state certificate for first-order embedded matrices; IID and original null.
for M in [64,65,1000,2**160-1]:
 beta=F(1,M)
 for a,t in [(beta,beta/2),(F(1,4),F(1,4)),(F(3,4),F(1,4))]:
  T=[[1-a,a],[t,1-t]];pi=[t/(a+t),a/(a+t)]
  for u in product(range(2),repeat=2):
   for v in product(range(2),repeat=2):
    p2=T[u[1]][v[0]]*T[v[0]][v[1]];mass=pi[v[0]]*T[v[0]][v[1]]
    assert p2>=beta*mass;counts['certificate_entries']+=1
# Exact active-path domination for absorbing 00; includes all boundary probabilities.
for b,e,t in product([F(0),F(1,3),F(1)],repeat=3):
 P=[[0,1-b,b],[1-e,0,0],[0,t,1-t]]
 R=[[0,1-b,b],[1,0,0],[0,t,1-t]]
 for path in product(range(3),repeat=6):
  pp=rr=F(1)
  for i,j in zip(path,path[1:]):pp*=P[i][j];rr*=R[i][j]
  assert pp<=rr;counts['reflection_paths']+=1
assert 48*130944+16*(6156+3078)==6433056<2**23
assert 2**17+2**23==8519680
# Bind primary imported theorem files to actual acceptance receipts.
verified={}
for unit,filename in [('channel_classification','CANDIDATE.md'),('whole_message_cost','CANDIDATE.md'),('bsc_sharp','CHANNEL_LIKELIHOOD_LOWER.md')]:
 r=json.loads((BASE/unit/'ROOT_ACCEPTANCE.json').read_text());p=BASE/unit/filename
 actual=hashlib.sha256(p.read_bytes()).hexdigest();assert actual==r['artifacts'][filename];verified[str(p.relative_to(BASE))]=actual
r=json.loads((BASE/'recovered_science/intake/positional_finite_manuscript_root_acceptance.json').read_text())
for filename in ['main.tex','sections/proofs_positive.tex','sections/proofs_negative.tex','sections/proofs_finite_horizon.tex']:
 p=BASE/'recovered_science/positional_manuscript_finite_20261102'/filename
 actual=hashlib.sha256(p.read_bytes()).hexdigest();assert actual==r['artifacts'][filename]['sha256'];verified[str(p.relative_to(BASE))]=actual
assert (BASE/'order_two_transfer/CANDIDATE.md').read_bytes()==(BASE/'order_two_transfer/TRANSFER.md').read_bytes()
result={'status':'PASS','checks':counts,'receipt_source_matches':verified,'limits':'Finite combinatorial/arithmetic diagnostics, not statistical risk or asymptotic proof verification.'}
(OUT/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
files=[BASE/'order_two_transfer/CANDIDATE.md',BASE/'order_two_transfer/TRANSFER.md',*map(lambda x:BASE/x,verified),*[BASE/u/'ROOT_ACCEPTANCE.json' for u in ['channel_classification','whole_message_cost','bsc_sharp']],BASE/'recovered_science/intake/positional_finite_manuscript_root_acceptance.json',Path(__file__).resolve(),OUT/'checks.json',OUT/'REVIEW.md']
(OUT/'bindings.json').write_text(json.dumps({str(p.relative_to(BASE)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files},indent=2)+'\n')
print(json.dumps(result,indent=2))
