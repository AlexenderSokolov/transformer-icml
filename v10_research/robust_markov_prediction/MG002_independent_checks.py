from pathlib import Path
import hashlib,json
D=Path(__file__).parent
counts={'capacity_admissible':0,'scalar':0,'snake':0}
for R in range(2,7):
 for c in [0,1,3]:
  B0=4*R*(c+2) # exact executable upper bound for 4 sqrt(R)(c+2)
  Ccap=(2*B0)**(R-1)
  for h in range(1,25):
   Q=2**h
   for exponent in range(6,65):
    for offset in [-1,0,1,17]:
     M=2**exponent+offset
     if M<64 or Q**(2*R)<Ccap**2*M:continue
     counts['capacity_admissible']+=1
     if Q*Q>=M:
      counts['scalar']+=1
      assert Q*Q>=M
     else:
      counts['snake']+=1;k=1
      while Q*Q*2**(2*k*(R-1))<M:k+=1
      N=2**k
      assert N>=2 and N*B0<=Q
      assert Q*Q*N**(2*(R-1))>=M
      assert Q*Q*(N//2)**(2*(R-1))<M
      # Table size scale N^(R-1)<2^(R-1)sqrt(M)/Q.
      assert Q*Q*N**(2*(R-1))<2**(2*(R-1))*M
assert counts['snake']>0
out={'status':'PASS','scope':'Exact integer squared capacity/selection inequalities; executable constants conservatively upper-bound radicals. Not full evaluator audit.',**counts,'MG002_theorem_sha256':hashlib.sha256((D/'MG002_partial_capacity_extension.md').read_bytes()).hexdigest()}
(D/'MG002_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
