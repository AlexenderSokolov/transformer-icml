"""Exact rational verification of saved bound outputs; no random values."""
from fractions import Fraction as F
from decimal import Decimal,localcontext,ROUND_CEILING
from pathlib import Path
import hashlib,json,sys,numpy as np
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'v10_research/float_readout_bound_20261103'; out=json.load(open(B/'bounds.json'));U=F(1,2**53)
def gam(n):return n*U/(1-n*U)
def frac(x):return F.from_float(float(x))
def dec_up(x):
 with localcontext() as ctx:ctx.prec=14;ctx.rounding=ROUND_CEILING;return str(Decimal(x.numerator)/Decimal(x.denominator))
num=0;vals={}
for rec in out['checkpoints']:
 path=ROOT/rec['path'];assert hashlib.sha256(path.read_bytes()).hexdigest()==rec['sha256'];z=np.load(path);assert str(z['mode'])=='half';W=[[frac(v) for v in row] for row in z['W']];V=[frac(v) for v in z['v']];b=[frac(v) for v in z['b']];c=frac(z['c'][0]);vsum=sum(abs(v) for v in V);S=[sum(abs(V[j]*W[i][j]) for j in range(32)) for i in range(9)]
 for r in rec['results']:
  M=r['M'];lens=[M,M,M//2,M//2,M-M//2,M-M//2];d=[U+(1+U)*gam(n-1) for n in lens]+[F(0),F(0),U/M];A=[sum((1+d[i])*abs(W[i][j]) for i in range(9)) for j in range(32)];H=[gam(9)*x+U*((1+gam(9))*x+abs(b[j])) for j,x in enumerate(A)];rail=sum(S[i]*d[i] for i in range(9));aff=sum(abs(V[j])*H[j] for j in range(32));output=gam(32)*vsum+U*((1+gam(32))*vsum+abs(c));tau=(1+gam(32))*(1+U)*vsum
  expected={'delta_full':d[0],'delta_first':d[2],'delta_second':d[4],'six_rail_lipschitz':sum(S[:6]),'ninth_rail_lipschitz':S[8],'v_l1':vsum,'rail_logit_error':rail,'affine_logit_error':aff,'output_dot_logit_error_at_tau_zero':output,'logit_error_at_tau_zero':rail+aff+output,'tanh_abs_error_coefficient':tau}
  for key,value in expected.items():
   assert r[key]==dec_up(value),(path,M,key,r[key],dec_up(value));assert F(Decimal(r[key]))>=value
  num+=1
  if '/smoke_v1/' in rec['path'] and rec['path'].endswith('_200.npz'):vals[M]=r
for path,digest in out['input_hashes'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
print('all checkpoint hashes',len(out['checkpoints']),'all horizon bound rows',num,'exact rational and upward rounded fields',num*11,'input hashes',len(out['input_hashes']),'PASS')
for m in [64,128,256,1025]:print('step200',m,'S6',vals[m]['six_rail_lipschitz'],'V',vals[m]['v_l1'],'logit R tau=0',vals[m]['logit_error_at_tau_zero'],'tanh coefficient',vals[m]['tanh_abs_error_coefficient'])
