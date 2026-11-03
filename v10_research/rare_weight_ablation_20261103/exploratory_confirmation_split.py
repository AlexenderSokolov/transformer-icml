import numpy as np,sys,json,hashlib
sys.path.insert(0,'v10_research/rare_weight_ablation_20261103');import experiment as e
orig=np.load('v10_research/readout_conditioning_calibration_20261103/calibration_v1/frozen_data.npz');new=np.load('v10_research/rare_weight_ablation_20261103/ablation_v1/frozen_data.npz'); rows=json.load(open('v10_research/rare_state_enumeration_20261103/rare_states.json'))['rows'];
w=np.concatenate([orig[k+'_words'] for k in ['train','validation','collision','boundary']]+[new[k+'_words'] for k in ['train','natural','rare_heldout','collision','structural_heldout']]);k=set(map(tuple,e.group_stats(w)[0]));coll=e.collision_keys();salt='v10-rare-split-confirm-20261103';out=[]
for r in rows:
 key=(r['J'],r['C'],r['D'],r['U']);v=int.from_bytes(hashlib.sha256((salt+':'+','.join(map(str,key))).encode()).digest(),'big')%5==0
 if key not in coll and v and key not in k:out.append(key)
print('novel vectors',len(out),'groups',len(set(out)),'groups',set(out))
