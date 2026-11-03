"""Independent exact-rational enclosures: fixed M=2 demo; no RNG or model init."""
from fractions import Fraction as F
from math import factorial
from decimal import Decimal,localcontext
from pathlib import Path
import runpy,contextlib,io,json
P=Path(__file__).resolve().parents[1];N=60;Q=10**40
def lower(x):return F(x.numerator*Q//x.denominator,Q)
def upper(x):return -lower(-x)
def exp_positive(x):
 assert x>=0;k=0
 while x>F(1,2):x/=2;k+=1
 term=F(1);s=F(1)
 for j in range(1,N+1):term=term*x/j;s+=term
 first=term*x/(N+1)
 # Since all tail ratios <=1/2, upper tail <=2 times its first term.
 return lower(s**(2**k)),upper((s+2*first)**(2**k))
def exp_rational(x):
 if x>=0:return exp_positive(x)
 a,b=exp_positive(-x);return lower(1/b),upper(1/a)
def th(x):
 lo,hi=exp_rational(2*x);return lower((lo-1)/(lo+1)),upper((hi-1)/(hi+1))
def log1to2(x):
 z=(x-1)/(x+1);s=sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0));return lower(2*s),upper(2*s+2*z**(2*N+1)/(1-z*z))
def ln(x):
 assert x>0
 if x<1:
  l,h=ln(1/x);return -h,-l
 k=0
 while x>2:x/=2;k+=1
 a,b=log1to2(x);c,d=log1to2(F(2));return lower(a+k*c),upper(b+k*d)
def ideal_ce(x):
 lo,hi=th(x);ea,eb=exp_rational(-hi);ec,ed=exp_rational(-lo);ql=F(1,16)+F(7,8)/(1+eb);qh=F(1,16)+F(7,8)/(1+ec);assert 0<ql<=qh<1
 la,lb=ln(ql)[0],ln(qh)[1];lc,ld=ln(1-qh)[0],ln(1-ql)[1];return -F(1,4)*lb-F(3,4)*ld,-F(1,4)*la-F(3,4)*lc
# The author script is read-only and deterministic; capture its stdout in memory.
with contextlib.redirect_stdout(io.StringIO()) as buf:author=runpy.run_path(str(P/'certificate_demo_v2.py'))
assert buf.getvalue()==(P/'run_v2.log').read_text();records=author['records'];out=[]
for x,rec in zip([F(1),F(1,2),F(0)],records):
 word,bank,oldx,ol,oh=rec; a,b=ideal_ce(x);assert x==oldx and a<=oh and ol<=b and a<=b and b-a<F(1,10**25)
 with localcontext() as ctx:ctx.prec=25;mid=str(Decimal((a+b).numerator)/Decimal((a+b).denominator)/2)
 out.append({'word':''.join(map(str,word)),'bank':list(bank),'own_lower':str(a),'own_upper':str(b),'author_reconstructed_lower':str(ol),'author_reconstructed_upper':str(oh),'own_mid_decimal':mid})
print('all 3 independent rational intervals overlap author reconstructions, each width <1e-25; replay stdout byte-identical')
for r in out:print(r['word'],'bank',r['bank'],'own midpoint',r['own_mid_decimal'])
for i in (1,2):assert F(out[0]['own_lower'])-F(out[i]['own_upper'])>F(189,6400)
assert F(189,6400)-2*F(1,1000)==F(881,32000)
print('analytic gap 189/6400, post-error gap 881/32000; singleton winner checked')
print('all endpoint fractions below are reconstructed in this review, not original run_v2 raw output')
Path(__file__).with_name('reconstructed_intervals.json').write_text(json.dumps(out,indent=2)+'\n')
