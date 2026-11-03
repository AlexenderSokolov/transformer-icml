"""Presealed matched rare-weight experiment; no artifact overwrite."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
from pathlib import Path
import sys, json, hashlib, csv, platform, traceback, argparse, time, tempfile, stat, struct, copy, io
from datetime import datetime,timezone
from functools import lru_cache
import numpy as np
P=Path(__file__).resolve().parent
CAL=P.parent/'readout_conditioning_calibration_20261103'
sys.path.insert(0,str(CAL));import calibration as c
CFG=json.loads((P/'protocol.json').read_text());SALT='v10-rare-split-20261103'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,o):atomic_bytes(p,(json.dumps(o,indent=2,sort_keys=True,allow_nan=False)+'\n').encode())
def group_stats(words):
 s=c.pilot.statistics(words)
 keys=np.column_stack([s['J'],s['C'],s['D'],s['U']]).astype(int)
 return keys,(s['J']<=6)|(s['D']==0)
def collision_keys():return set(map(tuple,group_stats(c.collision_words())[0]))
def original_split_key(key):
 key=tuple(int(x) for x in key)
 if key in collision_keys():return False
 return int.from_bytes(hashlib.sha256((SALT+':'+','.join(map(str,key))).encode('ascii')).digest(),'big')%5==0
@lru_cache(maxsize=1)
def prior_input_groups():
 # Membership only: never load or inspect any prior model predictions.
 paths=[CAL/'calibration_v1/frozen_data.npz',P.parent/'rare_weight_ablation_20261103/ablation_v1/frozen_data.npz']
 groups=set()
 for path in paths:
  with np.load(path,allow_pickle=False) as z:
   for name in z.files:
    if name.endswith('_words'):
     keys,_=group_stats(z[name]);groups.update(map(tuple,keys))
 return frozenset(groups)

@lru_cache(maxsize=1)
def unseen_structural():
 rows=json.loads((P.parent/'rare_state_enumeration_20261103'/'rare_states.json').read_text())['rows']
 words=np.array([[int(b) for b in row['word']] for row in rows],dtype=np.int8)
 keys,_=group_stats(words);prior=prior_input_groups()
 mask=np.array([tuple(key) not in prior for key in keys],dtype=bool)
 reserved=frozenset(map(tuple,keys[mask]))
 if len(words[mask])!=20 or len(reserved)!=18:raise AssertionError('unexpected predeclared structural slice')
 return words[mask],reserved

def split_key(key):
 key=tuple(int(x) for x in key)
 return original_split_key(key) or key in unseen_structural()[1]

def holdout(keys):
 unique,inverse=np.unique(keys,axis=0,return_inverse=True)
 return np.array([split_key(k) for k in unique],dtype=bool)[inverse]
def weighted_loss_grad(model,xs,ys,weights):
 grads=[];losses=[]
 for x,y in zip(xs,ys):
  loss,grad,_=model.loss_grad(x,y);losses.append(loss);grads.append(grad)
 g={k:sum(w*gg[k] for w,gg in zip(weights,grads)) for k in grads[0]}
 return float(np.dot(weights,losses)),g

def sync_directory(path):
 fd=os.open(str(path),os.O_RDONLY)
 try:os.fsync(fd)
 finally:os.close(fd)

def durable_mkdir(path):
 path=Path(path)
 if path.exists():
  if not path.is_dir():raise NotADirectoryError(path)
  return
 durable_mkdir(path.parent)
 path.mkdir();sync_directory(path.parent);sync_directory(path)

def atomic_bytes(path,data):
 path=Path(path);durable_mkdir(path.parent)
 fd,tmp=tempfile.mkstemp(prefix='.'+path.name+'.',dir=path.parent)
 try:
  with os.fdopen(fd,'wb') as f:f.write(data);f.flush();os.fsync(f.fileno())
  os.link(tmp,path);os.unlink(tmp);sync_directory(path.parent)
 except BaseException:
  if os.path.exists(tmp):os.unlink(tmp)
  raise

def atomic_npz(path, **arrays):
 path=Path(path);durable_mkdir(path.parent)
 fd,tmp=tempfile.mkstemp(prefix='.'+path.name+'.',dir=path.parent)
 try:
  with os.fdopen(fd,'wb') as f:
   np.savez_compressed(f,**arrays);f.flush();os.fsync(f.fileno())
  os.link(tmp,path);os.unlink(tmp);sync_directory(path.parent)
 except BaseException:
  if os.path.exists(tmp):os.unlink(tmp)
  raise

def append_csv(path,row):
 path=Path(path);exists=path.exists()
 with path.open('a',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(row));
  if not exists:w.writeheader()
  w.writerow(row);f.flush();os.fsync(f.fileno())
 if not exists:sync_directory(path.parent)

def console(row):
 print(json.dumps(row),flush=True);os.fsync(sys.stdout.fileno())

def require_external_console():
 # The approved launcher exclusively creates the new log before exec.
 out=os.fstat(1);err=os.fstat(2)
 if os.environ.get('CONFIRMATION_EXCLUSIVE_LOG')!='1' or not stat.S_ISREG(out.st_mode) or (out.st_dev,out.st_ino)!=(err.st_dev,err.st_ino) or out.st_size!=0:
  raise RuntimeError('stdout and stderr must both target the same NEW, empty, externally redirected regular log; use launch_exclusive.py')

def state_json(rng):return json.dumps(rng.bit_generator.state,sort_keys=True)

def candidate_batch(n,M,rng):
 # Exactly matches pilot.prior_batch: probabilities, integer starts, then M
 # successive vectors of n uniforms. All candidates, not just accepts, survive.
 before=state_json(rng);probabilities=rng.random((n,4));starts=rng.integers(0,4,n)
 uniforms=np.stack([rng.random(n) for _ in range(M)])
 words=c.pilot.simulate_words(probabilities,starts,M,uniforms=uniforms)
 return dict(words=words,probabilities=probabilities,starts=starts,uniforms=uniforms,
             rng_before=np.array(before),rng_after=np.array(state_json(rng)))

def draw_set(n,seed,want,out,batch_size=None,max_batches=None,M=64):
 rng=np.random.default_rng(seed);parts=[];total=0;drawn=0
 batch_size=batch_size or CFG['draw_batch_size'];max_batches=max_batches or CFG['maximum_draw_batches_per_rejection_set']
 directory=Path(out)/'candidate_batches'/want
 durable_mkdir(directory.parent);directory.mkdir(exist_ok=False);sync_directory(directory.parent);sync_directory(directory)
 for batch in range(max_batches):
  # Durable intent precedes any random draw. An intent without its batch
  # file denotes an uncertain, uncommitted batch, not preserved RAM values.
  before=state_json(rng)
  dump(directory/f'batch_{batch:04d}.intent.json',{'set':want,'batch_index':batch,'n':batch_size,'M':M,'rng_before':json.loads(before)})
  sample=candidate_batch(batch_size,M,rng);words=sample['words']
  if str(sample['rng_before'])!=before:raise AssertionError('intent and generator RNG states differ')
  if want=='natural':eligible=np.ones(len(words),dtype=bool)
  else:
   keys,rare=group_stats(words);isheld=holdout(keys)
   eligible=(~isheld) if want=='train' else (isheld&rare)
  selected=np.zeros(len(words),dtype=bool);eligible_idx=np.flatnonzero(eligible);selected[eligible_idx[:max(0,n-total)]]=True
  sample.update(eligible=eligible,selected=selected,global_candidate_start=np.array(drawn,dtype=np.int64))
  atomic_npz(directory/f'batch_{batch:04d}.npz',**sample)
  parts.append(words[selected]);total+=int(eligible.sum());drawn+=len(words)
  if total>=n:return np.concatenate(parts),{'drawn':drawn,'accepted_before_truncation':total,'saved':n}
 raise RuntimeError(f'{want} rejection draw cap reached after {drawn}; accepted {total} of {n}')

UPDATE_MAGIC=b'RWUPD01!'
UPDATE_HEADER=struct.Struct('<8sQ32s')

def append_update_record(path,arm,seed,step,grad,post_params):
 # One append-only, self-delimiting, SHA-256-protected write-ahead record.
 # Float values are IEEE 754 little-endian float64, flattened in C order.
 if set(grad)!=set(post_params):raise ValueError('gradient/parameter keys differ')
 names=sorted(post_params);shapes={k:list(post_params[k].shape) for k in names}
 if any(grad[k].shape!=post_params[k].shape for k in names):raise ValueError('gradient/parameter shapes differ')
 count=sum(post_params[k].size for k in names)
 if count!=353:raise ValueError('expected exactly 353 parameters')
 metadata={'version':1,'arm':arm,'seed':int(seed),'step':int(step),'names':names,'shapes':shapes,'count':count,'dtype':'<f8','order':'C','layout':'all gradients then all post-update parameters'}
 meta=json.dumps(metadata,sort_keys=True,separators=(',',':')).encode('utf-8')
 numbers=np.concatenate([np.asarray(d[k],dtype='<f8').ravel(order='C') for d in (grad,post_params) for k in names]).astype('<f8',copy=False)
 payload=struct.pack('<I',len(meta))+meta+numbers.tobytes(order='C')
 record=UPDATE_HEADER.pack(UPDATE_MAGIC,len(payload),hashlib.sha256(payload).digest())+payload
 path=Path(path);existed=path.exists()
 with path.open('ab',buffering=0) as f:
  view=memoryview(record)
  while view:
   written=f.write(view)
   if not written:raise OSError('short update journal write')
   view=view[written:]
  os.fsync(f.fileno())
 if not existed:sync_directory(path.parent)

def read_update_records(path):
 with Path(path).open('rb') as f:
  while True:
   offset=f.tell();header=f.read(UPDATE_HEADER.size)
   if not header:return
   if len(header)!=UPDATE_HEADER.size:raise ValueError(f'truncated update header at byte {offset}')
   magic,length,digest=UPDATE_HEADER.unpack(header)
   if magic!=UPDATE_MAGIC or length>10_000_000:raise ValueError(f'invalid update header at byte {offset}')
   payload=f.read(length)
   if len(payload)!=length:raise ValueError(f'truncated update payload at byte {offset}')
   if hashlib.sha256(payload).digest()!=digest:raise ValueError(f'update checksum mismatch at byte {offset}')
   if len(payload)<4:raise ValueError(f'invalid update payload at byte {offset}')
   ml=struct.unpack('<I',payload[:4])[0]
   if 4+ml>len(payload):raise ValueError(f'invalid update metadata length at byte {offset}')
   meta=json.loads(payload[4:4+ml]);raw=payload[4+ml:]
   if meta.get('version')!=1 or meta.get('count')!=353 or meta.get('dtype')!='<f8' or meta.get('order')!='C' or len(raw)!=2*353*8:raise ValueError(f'invalid update schema at byte {offset}')
   names=meta['names'];shapes=meta['shapes']
   if names!=sorted(shapes) or sum(int(np.prod(shapes[k])) for k in names)!=353:raise ValueError(f'invalid flatten metadata at byte {offset}')
   flat=np.frombuffer(raw,dtype='<f8');position=0;groups=[]
   for _ in range(2):
    group={}
    for k in names:
     size=int(np.prod(shapes[k]));group[k]=flat[position:position+size].reshape(shapes[k]).copy();position+=size
    groups.append(group)
   yield meta,groups[0],groups[1]

def checkpoint_state(path,model,opt,step):
 if opt.t!=step:raise ValueError('optimizer step differs from checkpoint step')
 payload={'condition':np.array(model.condition),'scale':model.scale,'optimizer_step':np.array(opt.t,dtype=np.int64),
          'readout_lr':np.array(opt.readout_lr),'pool_lr':np.array(opt.pool_lr),'beta1':np.array(opt.beta1),'beta2':np.array(opt.beta2),'epsilon':np.array(opt.epsilon)}
 for k,v in model.params.items():payload['param_'+k]=v;payload['adam_m_'+k]=opt.m[k];payload['adam_v_'+k]=opt.v[k]
 atomic_npz(path,**payload)

def restore_checkpoint(path,model,opt):
 with np.load(path,allow_pickle=False) as z:
  if str(z['condition'])!=model.condition or not np.array_equal(z['scale'],model.scale):raise ValueError('model configuration mismatch')
  for k in model.params:
   model.params[k][...]=z['param_'+k];opt.m[k][...]=z['adam_m_'+k];opt.v[k][...]=z['adam_v_'+k]
  opt.t=int(z['optimizer_step'])
  for k in ['readout_lr','pool_lr','beta1','beta2','epsilon']:setattr(opt,k,float(z[k]))

def review_inputs():
 root=P.parent.parent
 files=[P/'protocol.json',P/'PROTOCOL_AMENDMENT.md',P/'experiment.py',P/'test_experiment.py',P/'launch_exclusive.py',P/'validate_update_journal.py',P/'static_tests.log',CAL/'calibration.py',P.parent/'learned_position_pilot_20261103/pilot.py',P.parent/'rare_state_enumeration_20261103/rare_states.json',CAL/'calibration_v1/frozen_data.npz',P.parent/'rare_weight_ablation_20261103/ablation_v1/frozen_data.npz']
 files += [P.parent/'rare_state_enumeration_20261103'/name for name in ['REPORT.md','VERIFICATION.json','SOURCE_BINDINGS.json','enumerate_rare.py','verify_independent.py','test_enumeration.py']]
 return {str(f.relative_to(root)):sha(f) for f in files}

def require_review_approval():
 marker=P/'REVIEW_AND_RUN_APPROVAL.json'
 if not marker.exists():raise RuntimeError('UNSEALED: independent review and root permission are required; approval marker is absent')
 d=json.loads(marker.read_text());current=review_inputs()
 if d.get('independent_review')!='approved' or d.get('root_permission')!='approved' or d.get('files')!=current:
  raise RuntimeError('approval marker missing approvals or does not bind all current local and upstream inputs')
 return current

def metrics(y,p):
 e=np.abs(y-p);k=c.kl(y,p)
 return {'n':len(y),'mean_KL':float(k.mean()),'mean_abs_error':float(e.mean()),'q95_abs_error':float(np.quantile(e,.95)),'max_abs_error':float(e.max()),'count_over_0_1':int(np.sum(e>.1))}
def model_record(m,x,y):return metrics(y,m.predict(x))
def savecsv(path,rows):
 buffer=io.StringIO(newline='');w=csv.DictWriter(buffer,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 atomic_bytes(path,buffer.getvalue().encode())

def seal():
 files=require_review_approval();path=P/'PRE_RUN_HASHES.json'
 if path.exists():raise FileExistsError(path)
 dump(path,{'status':'SEALED_BEFORE_NEW_DATA_GENERATION_OR_FITTING','sealed_utc':datetime.now(timezone.utc).isoformat(),'files':files})
 print(path.read_text())

def verify_seal():
 data=json.loads((P/'PRE_RUN_HASHES.json').read_text())
 for p,h in data['files'].items():
  if sha(P.parent.parent/p)!=h:raise RuntimeError('sealed input changed: '+p)
 return data

def run(out):
 require_external_console();require_review_approval();sealdata=verify_seal();out=Path(out)
 if not out.is_absolute():out=P/out
 durable_mkdir(out.parent);out.mkdir(exist_ok=False);sync_directory(out.parent);sync_directory(out)
 durable_mkdir(out/'checkpoints')
 start=time.perf_counter()
 try:
  import unittest,test_experiment
  f=io.StringIO();result=unittest.TextTestRunner(stream=f,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(test_experiment))
  atomic_bytes(out/'tests.log',f.getvalue().encode())
  if not result.wasSuccessful():raise AssertionError('unit tests failed before sampling')
  train,tinfo=draw_set(CFG['training_prior_words'],CFG['data_seeds']['training'],'train',out)
  val,vinfo=draw_set(CFG['natural_prior_evaluation_words'],CFG['data_seeds']['natural_evaluation'],'natural',out)
  hold,hinfo=draw_set(CFG['rare_group_heldout_words'],CFG['data_seeds']['rare_group_heldout'],'hold',out)
  col=c.collision_words();struct=json.loads((P.parent/'rare_state_enumeration_20261103'/'rare_states.json').read_text());rows=struct['rows'];allstruct=np.array([[int(b) for b in row['word']] for row in rows],dtype=np.int8)
  sk,srare=group_stats(allstruct);sheld=np.array([original_split_key(k) for k in sk],bool)
  unseen,unseen_groups=unseen_structural()
  assert len(rows)==128 and all(len(row['word'])==66 for row in rows)
  for i,row in enumerate(rows):
   assert tuple(sk[i])==(row['J'],row['C'],row['D'],row['U'])
   assert sheld[i]==(row['split']=='holdout')
   assert c.literal_statistics(allstruct[i:i+1])['Q'][0]==row['Q_numerator']/row['Q_denominator']
   xx=c.features(allstruct[i:i+1],'half_count_scaled')[0]*c.SCALE
   assert np.array_equal(xx[2:6],[row['a0'],row['a1'],row['b0'],row['b1']])
  structure=allstruct[sheld];assert len(structure)==11
  previous=np.load(CAL/'calibration_v1/frozen_data.npz');prevwords=np.concatenate([previous[n+'_words'] for n in ['train','validation','collision','boundary']]);prevkeys,_=group_stats(prevwords);oldgroups=set(map(tuple,prevkeys));novelmask=np.array([tuple(k) not in oldgroups for k in sk[sheld]],bool);novelstructure=structure[novelmask]
  assert len(novelstructure)==8 and len(set(map(tuple,sk[sheld][novelmask])))==7
  tk,tr=group_stats(train);vk,vr=group_stats(val);hk,hr=group_stats(hold);ck,cr=group_stats(col);zk,zr=group_stats(structure)
  assert not holdout(tk).any() and not holdout(ck).any() and holdout(hk).all() and hr.all() and holdout(zk).all() and (zk[:,0]<=3).all()
  train_groups=set(map(tuple,np.r_[tk,ck]));held_groups=set(map(tuple,hk));struct_groups=set(map(tuple,zk))
  assert not (train_groups&held_groups) and not (train_groups&struct_groups) and not (train_groups&unseen_groups)
  assert len(unseen)==20 and len(unseen_groups)==18 and not (unseen_groups & prior_input_groups())
  assert len(structure)>0 and tr.any() and (~tr).any()
  y={name:c.literal_statistics(w)['Q'] for name,w in [('train',train),('natural',val),('rare_heldout',hold),('collision',col),('structural_heldout',structure),('structural_previous8',novelstructure),('structural_unseen20',unseen)]}
  words={'train':train,'natural':val,'rare_heldout':hold,'collision':col,'structural_heldout':structure,'structural_previous8':novelstructure,'structural_unseen20':unseen}
  x={name:c.features(w,'half_count_scaled') for name,w in words.items()}
  for name in words:
   assert np.max(abs(c.decode_features(x[name])-y[name]))<1e-14
   assert np.max(abs(c.pilot.statistics(words[name])['Q']-y[name]))<1e-14
  rareidx=np.where(tr)[0];commonidx=np.where(~tr)[0];p=len(rareidx)/len(train);steps=CFG['optimization']['steps'];rng=np.random.default_rng(CFG['data_seeds']['minibatches'])
  minibatch_rng_before=state_json(rng)
  ir=np.empty((steps,32),int);inn=np.empty((steps,32),int);ic=np.empty((steps,64),int)
  for i in range(steps):ir[i]=rng.choice(rareidx,32);inn[i]=rng.choice(commonidx,32);ic[i]=rng.integers(0,4,64)
  packed={name+'_words':v for name,v in words.items()};packed.update({name+'_Q':v for name,v in y.items()});packed.update(prior_rare_indices=ir,prior_nonrare_indices=inn,collision_indices=ic,train_groups=tk,natural_groups=vk,rare_heldout_groups=hk,structural_heldout_groups=zk,structural_unseen20_groups=group_stats(unseen)[0])
  packed.update(minibatch_rng_before=np.array(minibatch_rng_before),minibatch_rng_after=np.array(state_json(rng)))
  atomic_npz(out/'frozen_data.npz',**packed)
  wordset=lambda w:set(map(bytes,np.asarray(w,dtype=np.uint8)))
  checks={'train_sampling':tinfo,'natural_sampling':vinfo,'holdout_sampling':hinfo,'p_empirical_rare':p,'rare_count':len(rareidx),'nonrare_count':len(commonidx),'train_group_count':len(train_groups),'rare_heldout_group_count':len(held_groups),'structural_heldout_group_count':len(struct_groups),'structural_heldout_feature_count':len(structure),'structural_previous8_feature_count':len(novelstructure),'structural_previous8_group_count':7,'structural_unseen20_feature_count':20,'structural_unseen20_group_count':18,'train_intersection_structural_unseen20_groups':len(train_groups&unseen_groups),'train_intersection_rare_groups':len(train_groups&held_groups),'train_intersection_struct_groups':len(train_groups&struct_groups),'natural_train_distinct_word_overlap':len(wordset(val)&wordset(train)),'heldout_train_distinct_word_overlap':len(wordset(hold)&wordset(train)),'rare_factors_corrected':[2*p,2*(1-p)],'rare_factors_boost':[1,1],'frozen_data_sha256':sha(out/'frozen_data.npz')}
  dump(out/'pre_fit_checks.json',checks);console({'pre_fit_checks':checks})
  predictions={};checkpoint_rows=[];update_rows=[];final=[]
  for seed in CFG['initialization_seeds']:
   for arm in ['corrected','rare_boost']:
    model=c.Readout(seed,'half_count_scaled');opt=c.pilot.Adam(model.params,readout_lr=.003,beta1=.9,beta2=.999,epsilon=1e-8)
    weights=np.array([.5*p,.5*(1-p),.5]) if arm=='corrected' else np.array([.25,.25,.5])
    def checkpoint(step):
     checkpoint_state(out/'checkpoints'/f'{arm}_{seed}_step{step}.npz',model,opt,step);row={'arm':arm,'seed':seed,'step':step}
     for name in ['natural','rare_heldout','collision','structural_heldout','structural_previous8','structural_unseen20']:
      row.update({name+'_'+k:v for k,v in model_record(model,x[name],y[name]).items()})
     for label,mask in [('train_rare',tr),('train_nonrare',~tr)]:
      row.update({label+'_'+k:v for k,v in model_record(model,x['train'][mask],y['train'][mask]).items()})
     append_csv(out/'checkpoint_metrics.csv',row);checkpoint_rows.append(row);console(row);return row
    checkpoint(0)
    for j in range(steps):
     loss,grad=weighted_loss_grad(model,[x['train'][ir[j]],x['train'][inn[j]],x['collision'][ic[j]]],[y['train'][ir[j]],y['train'][inn[j]],y['collision'][ic[j]]],weights)
     if not np.isfinite(loss) or not all(np.isfinite(g).all() for g in grad.values()):raise FloatingPointError('nonfinite loss or gradient')
     # Write-ahead: calculate the next Adam state on copies, durably preserve
     # all gradients and resulting parameters, then commit the update in memory.
     next_params={k:v.copy() for k,v in model.params.items()};next_opt=copy.deepcopy(opt)
     next_opt.step(next_params,grad)
     if not all(np.isfinite(v).all() for v in next_params.values()):raise FloatingPointError('nonfinite parameter')
     append_update_record(out/'full_updates.bin',arm,seed,j+1,grad,next_params)
     model.params=next_params;opt=next_opt
     row={'arm':arm,'seed':seed,'step':j+1,'weighted_CE':loss,'gradient_l2':float(np.sqrt(sum(np.sum(g*g) for g in grad.values()))),'effective_W_l2':float(np.linalg.norm(model.effective_W())),'raw_W_l2':float(np.linalg.norm(model.params['W']))}
     row.update({f'W_gradient_row_{i}_l2':float(np.linalg.norm(grad['W'][i])) for i in range(9)});append_csv(out/'updates.csv',row)
     if j+1 in CFG['optimization']['checkpoints']:last=checkpoint(j+1)
    final.append(last)
    for name in words:predictions[f'{arm}_{seed}_{name}']=model.predict(x[name])
  savecsv(out/'final_metrics.csv',final);atomic_npz(out/'final_predictions.npz',**predictions)
  screens=[]
  for seed in CFG['initialization_seeds']:
   a=next(r for r in final if r['arm']=='corrected' and r['seed']==seed);b=next(r for r in final if r['arm']=='rare_boost' and r['seed']==seed)
   screens.append({'seed':seed,'rare_heldout_error_ratio':(b['rare_heldout_mean_abs_error']/a['rare_heldout_mean_abs_error'] if a['rare_heldout_mean_abs_error'] else None),'natural_KL_increase':b['natural_mean_KL']-a['natural_mean_KL'],'collision_max_error':b['collision_max_abs_error'],'pass':bool(b['rare_heldout_mean_abs_error']<=.8*a['rare_heldout_mean_abs_error'] and b['natural_mean_KL']-a['natural_mean_KL']<=.002 and b['collision_max_abs_error']<=.05)})
  dump(out/'results.json',{'status':'SIX_FITS_COMPLETE_NOT_INDEPENDENTLY_REVIEWED','sealed_inputs':sealdata,'environment':{'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),'blas_threads':1},'seconds':time.perf_counter()-start,'screen':screens,'screen_all_pass':all(x['pass'] for x in screens),'final_metrics':final})
  dump(out/'ARTIFACT_HASHES.json',{str(f.relative_to(out)):sha(f) for f in sorted(out.rglob('*')) if f.is_file()});console({'status':'done','screen':screens})
 except Exception as e:
  dump(out/'FAILURE.json',{'error':str(e),'type':type(e).__name__,'traceback':traceback.format_exc(),'elapsed_seconds':time.perf_counter()-start});raise
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('command',choices=['seal','run']);p.add_argument('--output',default='confirmation_v1');a=p.parse_args();seal() if a.command=='seal' else run(a.output)
