import sys,json,numpy as np
sys.path.insert(0,'v10_research/learned_position_pilot_20261103');import pilot
rng=np.random.default_rng(318038)
for m in [6,8,10,16,32,64,128]:
 n=100000;w=rng.integers(0,2,(n,m+2),dtype=np.int8);model=pilot.Model(0,mode='half');q,cache=model.forward(w,cache=True);x=cache['x'];e=pilot.local_selected(w)
 j=e.sum((1,2));c=e[:,:,1].sum(1);d=e[:,:m//2,:].sum((1,2));v=e[:,:m//2,1].sum(1)
 seen={}
 for i in range(n):
  key=(int(w[i,-2]),int(w[i,-1]),int(j[i]),int(c[i]),int(d[i]),int(v[i]));old=seen.get(key)
  if old is None:seen[key]=i
  elif not np.array_equal(x[i],x[old]):
   print(json.dumps({'M':m,'bank_endpoint':key,'word1':''.join(map(str,w[old])),'word2':''.join(map(str,w[i])),'x1':x[old].tolist(),'x2':x[i].tolist(),'q1':float(q[old]),'q2':float(q[i]),'batch_size':n,'seed':318038,'index1':old,'index2':i}));sys.exit(0)
 print('M',m,'no mismatch',flush=True)
print('No mismatch observed; not proof of bitwise equivalence.')
