"""Fresh integration diagnostics. Scalar Decimal checks are not formal proofs."""
from pathlib import Path
from hashlib import sha256
import json,difflib
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
getcontext().prec=100
root=Path.cwd(); new=root/'v10_research/positional_manuscript_finite_20261102'; old=root/'v10_research/positional_manuscript_20261102'; out=new/'reviews/integration'
def digest(p): return {'sha256':sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
checks={}
for f in ['references.bib','sections/proofs_positive.tex','sections/proofs_negative.tex']:
 assert (old/f).read_bytes()==(new/f).read_bytes(); checks['byte_identical:'+f]=True
for f in ['SOURCE_BINDINGS.json','provenance/source_bindings.json']:
 for p,meta in json.loads((new/f).read_text()).items():
  assert digest(root/p)['sha256']==meta['sha256'],p
 checks['bindings:'+f]=True
receipt=json.loads((new/'provenance/positional_manuscript_root_acceptance.json').read_text())
for f,meta in receipt['artifacts'].items(): assert digest(old/f)['sha256']==meta['sha256'],f
for x in receipt['historical_bindings_verified']: assert digest(root/x['verified_at'])['sha256']==x['sha256']
checks['v1_receipt_all_current_and_historical']=True
fh=root/'v10_research/finite_horizon_window_adaptation'
receipt=json.loads((new/'provenance/FHW001_root_acceptance.json').read_text())
for f,meta in receipt['artifacts'].items(): assert digest(fh/f)['sha256']==meta['sha256'],f
checks['FHW001_receipt_all_artifacts']=True
for copy,original in [('FHW001_candidate.md',fh/'FHW001_candidate.md'),('REVIEW.md',fh/'review/REVIEW.md'),('source_bindings.json',fh/'review/source_bindings.json'),('FHW001_root_acceptance.json',root/'v10_research/intake/FHW001_root_acceptance.json'),('positional_manuscript_root_acceptance.json',root/'v10_research/intake/positional_manuscript_root_acceptance.json')]:
 assert (new/'provenance'/copy).read_bytes()==original.read_bytes(),copy
checks['all_provenance_copies_exact']=True
actual=''.join(difflib.unified_diff((old/'main.tex').read_text().splitlines(True),(new/'main.tex').read_text().splitlines(True),fromfile='positional_manuscript_20261102/main.tex',tofile='positional_manuscript_finite_20261102/main.tex'))
assert actual==(new/'v1_to_v2_main.diff').read_text()
checks['exact_v1_to_v2_diff']=True
for before,after,diff in [('main.before_root_wording.tex','main.tex','root_wording.diff'),('proofs_finite_horizon.before_heading_fix.tex','sections/proofs_finite_horizon.tex','proof_heading_fix.diff')]:
 actual=''.join(difflib.unified_diff((new/'revisions'/before).read_text().splitlines(True),(new/after).read_text().splitlines(True),fromfile=before,tofile=after))
 assert actual==(new/'revisions'/diff).read_text()
checks['both_editorial_diffs_exact']=True
before=(new/'revisions/proofs_finite_horizon.before_heading_fix.tex').read_text()
assert before.replace(r'\paragraph{',r'\noindent\textbf{')==(new/'sections/proofs_finite_horizon.tex').read_text()
checks['proof_change_headings_only']=True
count=0
for M in range(64,513):
 for r in range(2,M+3):
  m=min(r-2,M//2)
  assert F(M,m+1)<=max(F(2*M,r),2)<=F(2*(M+2),r)
  count+=1
checks['exact_upper_pairs']=count
# Exact ceiling fourth root: ceil(M**(3/4)) without floating point.
def ceilroot4(n):
 lo=0; hi=1<<((n.bit_length()+3)//4)
 while lo+1<hi:
  mid=(lo+hi)//2
  if mid**4<n: lo=mid
  else: hi=mid
 return hi
large=[]
for exponent in [92,100,128,256,512,1024,2048]:
 for M in [2**exponent-1,2**exponent,2**exponent+1]:
  q=ceilroot4(M**3)
  threshold=int(D(M+2)/D(63).exp())
  for r in sorted({2,max(2,q//128-1),max(2,q//128),max(2,q//128+1),max(2,threshold-1),max(2,threshold)}):
   ell=1+(D(M+2)/D(r)).ln()
   if ell<64: continue
   k=max(128*r,q); c=F(1,2**16); t=c*k/M; u=(c*k)//4
   assert k>=128*r and k**4>=M**3 and k<=F(M,8)
   assert c*k>=1024 and 2**12*t<F(1,4) and F(M,k*k)<=F(1,2**40)
   assert F(u,1)/(8*M*t)>=F(1,64)
   assert ell / D(2**30) / D(M).sqrt() < D(t.numerator)/D(t.denominator)/32
   lm=(4*D(M)/D(k)).ln(); assert lm>=ell/8
   assert k*k>=M
   assert F(1,64)*F(1,32)*F(1,8)*c==F(1,2**30)
   large.append({'M':str(M),'r':str(r),'k':str(k),'ell':str(ell),'log_ratio':str(lm/ell)})
checks['large_log_cases']=len(large)
checks['status']='PASS'
(out/'checks_results.json').write_text(json.dumps({'checks':checks,'large_cases':large},indent=2)+'\n')
paths=[new/f for f in ['main.tex','sections/proofs_finite_horizon.tex','sections/proofs_positive.tex','sections/proofs_negative.tex','references.bib','v1_to_v2_main.diff','SOURCE_BINDINGS.json']]+list((new/'provenance').glob('*'))+[old/'main.tex',out/'checks.py',out/'checks_results.json',out/'REVIEW.md']+list((new/'revisions').glob('*'))
(out/'source_bindings.json').write_text(json.dumps({str(p.relative_to(root)):digest(p) for p in paths},indent=2)+'\n')
print(json.dumps(checks,indent=2))
