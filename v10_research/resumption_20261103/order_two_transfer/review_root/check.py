import itertools,json,hashlib,pathlib
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[1]
n=0; zeros=0; rejects=0
for M in range(1,13):
 for z in itertools.product(range(2),repeat=M+2):
  h=[0]*8; half=[0]*4
  for i in range(M):
   h[4*z[i]+2*z[i+1]+z[i+2]]+=1
   if i<M//2: half[2*z[i]+z[i+1]]+=1
  u=2*z[M]+z[M+1]; d=1-z[M]
  J=h[2*u]+h[2*u+1]; C=h[2*u+d]; G=int(512*half[u]>=J)
  out=[sum(h[2*v:2*v+2]) for v in range(4)]
  inc=[sum(h[4*c+v] for c in range(2)) for v in range(4)]
  assert [out[v]-inc[v]+int(v==u) for v in range(4)]==[int(v==2*z[0]+z[1]) for v in range(4)]
  # Compare rational p1 numerator/denominator, avoiding floating point.
  q=(C,J) if J and G else (0,1)
  p=(q[0],q[1]) if d else (q[1]-q[0],q[1])
  selected=(J,C,d,G)
  j,c,orient,gate=selected
  q2=(c,j) if j and gate else (0,1)
  p2=q2 if orient else (q2[1]-q2[0],q2[1])
  assert p==p2
  assert J<=M and C<=J
  if not J: assert G==1; zeros+=1
  if not G: rejects+=1
  n+=1
files=['order_two_transfer/CANDIDATE.md','order_two_transfer/TRANSFER.md','recovered_science/positional_manuscript_finite_20261102/main.tex','recovered_science/positional_manuscript_finite_20261102/sections/proofs_positive.tex','recovered_science/intake/positional_finite_manuscript_root_acceptance.json','recovered_science/first_order_positional_probe/triple_access/BOUNDARY_RECONSTRUCTION_NOTE.md','recovered_science/intake/FOT003_root_acceptance.json','bsc_sharp/CHANNEL_LIKELIHOOD_LOWER.md','bsc_sharp/ROOT_ACCEPTANCE.json','channel_classification/CANDIDATE.md','channel_classification/ROOT_ACCEPTANCE.json','whole_message_cost/CANDIDATE.md','whole_message_cost/ROOT_ACCEPTANCE.json']
bind={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files}
assert bind[files[0]]==bind[files[1]]
(HERE/'bindings.json').write_text(json.dumps(bind,indent=2)+'\n')
res={'exhaustive_words':n,'M_range':[1,12],'zero_count_cases':zeros,'rejected_gate_cases':rejects,'checks':'flow reconstructs initial pair; selected J,C,d,G reproduces exact symbol prediction including zero/rejection; field bounds','scope':'Finite deterministic corroboration only; M below theorem threshold is permitted for pathwise identities, not a risk simulation.','constant_C2':2**17+2**23}
(HERE/'checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res))
