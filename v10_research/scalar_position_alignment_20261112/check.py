import math,random,json,hashlib,time
from pathlib import Path
if not __debug__:raise RuntimeError('Run without -O')
seed=1907;rng=random.Random(seed);eta=1e-5;gate_eta=.001
D1=math.sqrt(53/28);D2=math.sqrt(61/28);q1=1-(9/7)/D1**3;q2=1-1/D2**3

def ln(h):
 mu=sum(h)/14;d=math.sqrt(1+sum((x-mu)**2 for x in h)/14);return [(x-mu)/d for x in h]
def phi(t):return t-2*max(t-.1,0)+2*max(-t-.1,0)
def bump(x,c):return 10*(max(x-c+.24,0)-max(x-c+.14,0)-max(x-c-.14,0)+max(x-c-.24,0))
def count_steps(delta,dmax):return max(0,math.ceil(math.log(.1/delta)/math.log(1+1/dmax)))+2
checks=0;rows=[];maxnorm=0;maxgate=0;maxout=0;start=time.time()
for N in [2,3,8,32,128,512]:
 targets=sorted(set([1,max(1,N//2),N-1,N]))
 for j in targets:
  for mode in range(5):
   xs=([1]*N if mode==0 else [-1]*N if mode==1 else [rng.choice([-1,1]) for _ in range(N)])+[1]
   hs=[[s,-s,i/N,-i/N,1,-1,0,0,0,0,0,0,0,0] for i,s in enumerate(xs,1)]
   low=(j-.5)/N;high=(j+.5)/N
   for h in hs:
    z=ln(h);x=(z[2]-low*z[4])/4;y=(high*z[4]-z[2])/4
    h[6]+=x;h[7]-=x;h[8]+=y;h[9]-=y
   L0=count_steps(1/(8*N*math.sqrt(45/28)),D1);L1=math.ceil(math.log(gate_eta/2)/math.log(q1))
   for _ in range(L0+L1):
    for h in hs:
     z=ln(h)
     for idx in [6,8]:
      a=phi(z[idx]);h[idx]+=a;h[idx+1]-=a
   for i,h in enumerate(hs,1):
    z=ln(h);u=z[0]+10*z[6]+20*z[8];gate=bump(u,6+.83)-bump(u,6-.83)
    h[10]+=gate;h[11]-=gate;wanted=xs[i-1] if i==j else 0
    maxgate=max(maxgate,abs(gate-wanted));assert abs(gate-wanted)<1e-11;checks+=1
   vals=[ln(h)[10] for h in hs];acc=0
   for i,h in enumerate(hs,1):
    acc+=vals[i-1];v=acc/i;h[12]+=v;h[13]-=v
   B0=count_steps(1/((N+1)*math.sqrt(57/28)),D2);B1=math.ceil(math.log(eta/5)/math.log(q2))
   for _ in range(B0+B1):
    for h in hs:
     z=ln(h);a=phi(z[12]);h[12]+=a;h[13]-=a
     norm=math.sqrt(sum(x*x for x in h));maxnorm=max(maxnorm,norm);assert norm<=math.sqrt(16.5)+1e-10
   err=0
   for i,h in enumerate(hs,1):
    out=5*ln(h)[12];want=xs[j-1] if i>=j else 0
    err=max(err,abs(out-want));assert abs(out-want)<=eta+1e-8;checks+=1
   maxout=max(maxout,err)
   rows.append({'N':N,'j':j,'word_mode':mode,'blocks':L0+L1+B0+B1+3,'max_all_row_alignment_error':err})
p=Path(__file__).parent;r={'seed':seed,'eta':eta,'gate_eta':gate_eta,'cases':len(rows),'checks':checks,'max_gate_error':maxgate,'max_alignment_error':maxout,'max_observed_norm':maxnorm,'analytic_state_bound':math.sqrt(16.5),'q1':q1,'q2':q2,'cases_detail':rows,'elapsed_seconds':time.time()-start,'scope':'actual shared all-row full-LN/ReLU pipeline, one uniform attention; binary64 diagnostic not adversarial-noise certificate'}
(p/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='cases_detail'}))
(p/'RECEIPT.json').write_text(json.dumps({'sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in p.iterdir() if f.name!='RECEIPT.json' and f.is_file()}},indent=2)+'\n')
