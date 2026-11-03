from itertools import product
from collections import Counter
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,difflib,math
base=Path(__file__).resolve().parent; root=base.parent
counts=Counter()
def pairs(w):return Counter(w[i:i+2] for i in range(len(w)-1))
for M in range(2,10):
 for z in product((0,1),repeat=M+2):
  H=Counter(z[i:i+3] for i in range(M))
  reconstructed=Counter()
  for a,b in product((0,1),repeat=2):
   reconstructed[a,b]=sum(H[a,b,c] for c in (0,1))+int(z[-2:]==(a,b))-int(z[:2]==(a,b))
  assert reconstructed==pairs(z[1:])
  # Includes every possible edited output and cancellation of a changed first symbol.
  flipped=(1-z[0],)+z[1:];Hf=Counter(flipped[i:i+3] for i in range(M))
  for a,b in product((0,1),repeat=2):
   assert sum(Hf[a,b,c] for c in (0,1))+int(flipped[-2:]==(a,b))-int(flipped[:2]==(a,b))==reconstructed[a,b]
  counts['reconstruction_and_first_edit_cancellation']+=1
  s=z[1:];selected=s[-1];J=sum(n for (a,b),n in reconstructed.items() if a==selected)
  Jhalf=sum(a==selected for a in s[:M//2])
  bit=int(512*Jhalf>=J)
  assert bit==int(512*sum(s[i]==selected for i in range(M//2))>=sum(s[i]==selected for i in range(M)))
  counts['exact_suffix_half_bit']+=1
  for r in range(2,M+3):
   rp=min(r,M+1)
   assert s[-rp:]==z[-rp:] and len(z[-r:])>=rp
   m=min(rp-1,M//2)
   observed_tail=z[-(m+1):]
   assert pairs(observed_tail)==pairs(s[-(m+1):])
   counts['suffix_window_access']+=1
for M in range(2,6):
 words=list(product((0,1),repeat=M+2))
 for w in words:
  for z in words:
   if w[-2:]!=z[-2:]:continue
   k=sum(a!=b for a,b in zip(w,z))
   assert k<=M and sum(a!=b for a,b in zip(w[1:],z[1:]))<=k
   assert w[1:][-1]==z[1:][-1]
   counts['induced_kernel_support_pairs']+=1
for M in range(64,513):
 for k in range(M+1):
  # Squared comparisons avoid floating-point square roots.
  gn2=max(Q(1,M+1),Q(k*k,(M+1)**2));gm2=max(Q(1,M),Q(k*k,M*M))
  assert gn2<=gm2<=Q((M+1)**2,M*M)*gn2
  if k:
   assert Q(1,32*(M//(k+1)+1))>=Q(k,96*M)
  counts['horizon_and_oracle_constants']+=1
 for r in range(2,M+3):
  rp=min(r,M+1)
  assert Q(M+1,rp)<=Q(M+2,r)
  counts['log_argument_order']+=1
# Exact retained-set channel identity, including bucket sizes for two protected labels.
from math import comb
for M in range(2,20):
 for k in range(1,M+1):
  for n in range(M+1):
   h=(k+1)*(n//(k+1))
   assert Q(comb(M-h,n-h),comb(M,n)*comb(n,h))==Q(1,comb(M,h))
   counts['iid_channel_identity']+=1
before=(root/'FOT002_before_initial_pair_repair.md').read_text().splitlines(keepends=True)
after=(root/'FOT002_before_message_scope_clarification.md').read_text().splitlines(keepends=True)
expected=''.join(difflib.unified_diff(before,after,fromfile='FOT002_before_initial_pair_repair.md',tofile='FOT002_matched_original_experiment.md'))
assert expected==(root/'FOT002_initial_pair_repair.diff').read_text()
final=(root/'FOT002_matched_original_experiment.md').read_text().splitlines(keepends=True)
second=''.join(difflib.unified_diff(after,final,fromfile='FOT002_before_message_scope_clarification.md',tofile='FOT002_matched_original_experiment.md'))
assert second==(root/'FOT002_message_scope_clarification.diff').read_text()
result={'status':'PASS','counts':dict(counts),'actual_repair_diff_verified':True,'actual_message_scope_diff_verified':True,'candidate_sha256':hashlib.sha256((root/'FOT002_matched_original_experiment.md').read_bytes()).hexdigest(),'scope':'Independent finite interface checks, not independent reproof of accepted generic FOU lemmas or root acceptance.'}
(base/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
