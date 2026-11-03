import numpy as np,sys
sys.path.insert(0,'v10_research/readout_conditioning_calibration_20261103');import calibration as c
P='v10_research/readout_conditioning_calibration_20261103/calibration_v1/'
f=np.load(P+'frozen_data.npz');p=np.load(P+'final_predictions.npz');s=c.literal_statistics(f['train_words']);v=c.literal_statistics(f['validation_words']);
for seed in [20261103201,20261103202,20261103203]:
 pred=p[f'half_count_scaled_{seed}_validation']; tr=p[f'half_count_scaled_{seed}_train'];err=np.abs(pred-v['Q']);te=np.abs(tr-s['Q']);kl=c.kl(v['Q'],pred);i=1242; tail=err>.1
 print(seed,'tail prior kl sum',kl[tail].sum(),'all',kl.sum(),'single',kl[i], 'tail mean',kl[tail].sum()/2048,'train failures',sum(te>.1),'train max',max(te));
 print('target nearby', [(int(j),round(float(s['Q'][j]),5),round(float(tr[j]),5)) for j in [797,1885,177,376,464,1764]])
 print('shared feature tail',[(int(j),int(v['J'][j]),int(v['C'][j]),int(v['D'][j])) for j in np.where(tail)[0] if any(np.all(c.features(f['train_words'],'half_normalized')==x,axis=1)) for x in []])
