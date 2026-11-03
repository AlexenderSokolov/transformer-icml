"""Static pre-sampling correctness checks for split, objective and gradients."""
import unittest, hashlib
import numpy as np
import experiment as e
class Tests(unittest.TestCase):
 def test_forced_collision_and_hash_split(self):
  keys,_=e.group_stats(e.c.collision_words());self.assertFalse(e.holdout(keys).any());self.assertEqual(len(set(map(tuple,keys))),4)
  examples=[(2,1,1,2),(3,1,1,2),(6,1,0,3),(6,2,3,0)]
  for key in examples:
   expected=key not in e.collision_keys() and int.from_bytes(hashlib.sha256(('v10-rare-split-20261103:'+','.join(map(str,key))).encode('ascii')).digest(),'big')%5==0
   self.assertEqual(e.original_split_key(key),expected)
 def test_reserved_structural_groups_are_previous_input_disjoint(self):
  words,groups=e.unseen_structural();keys,_=e.group_stats(words)
  self.assertEqual(len(words),20);self.assertEqual(len(groups),18)
  self.assertTrue(all(k[0]<=3 for k in groups));self.assertTrue(e.holdout(keys).all())
  self.assertFalse(groups & e.prior_input_groups());self.assertFalse(groups & e.collision_keys())
 def test_exact_reweight_identity(self):
  # Arbitrary synthetic finite per-word losses establish the deterministic empirical identity.
  r=np.array([.1,.5]);n=np.array([.2,.3,.4,.8,.9]);p=len(r)/(len(r)+len(n))
  self.assertAlmostEqual(p*r.mean()+(1-p)*n.mean(),np.r_[r,n].mean(),places=15)
  self.assertAlmostEqual(.5*(2*p*r.mean()+2*(1-p)*n.mean()),np.r_[r,n].mean(),places=15)
 def test_weighted_gradient(self):
  w=e.c.collision_words();extra=np.concatenate([np.zeros((1,66),dtype=np.int8),np.ones((1,66),dtype=np.int8),np.tile(np.array([0,1],dtype=np.int8),(1,33))]);allw=np.concatenate([w,extra]);x=e.c.features(allw,'half_normalized');y=e.c.literal_statistics(allw)['Q'];xs=[x[:2],x[2:4],x[4:]];ys=[y[:2],y[2:4],y[4:]];weights=np.array([.17,.33,.5]);m=e.c.Readout(20261103201,'half_count_scaled');loss,g=e.weighted_loss_grad(m,xs,ys,weights);maximum=0.
  for name,v in m.params.items():
   for idx in np.ndindex(v.shape):
    old=v[idx];v[idx]=old+1e-6;plus=e.weighted_loss_grad(m,xs,ys,weights)[0];v[idx]=old-1e-6;minus=e.weighted_loss_grad(m,xs,ys,weights)[0];v[idx]=old
    maximum=max(maximum,abs((plus-minus)/2e-6-g[name][idx]))
  self.assertLess(maximum,2e-7);print('weighted_gradient_max_absolute_error',maximum)
 def test_inputs_exact(self):
  w=np.concatenate([e.c.collision_words(),np.zeros((1,66),np.int8),np.ones((1,66),np.int8)]);x=e.c.features(w,'half_normalized');s=e.c.literal_statistics(w)
  np.testing.assert_allclose(e.c.decode_features(x),s['Q'],atol=0,rtol=0)

class PreservationTests(unittest.TestCase):
 def test_interrupted_batch_has_durable_intent_not_candidate_data(self):
  import tempfile,json
  from pathlib import Path
  from unittest.mock import patch
  def interrupted(n,M,rng):
   rng.random();raise RuntimeError('synthetic interruption')
  with tempfile.TemporaryDirectory() as d, patch.object(e,'candidate_batch',side_effect=interrupted):
   with self.assertRaisesRegex(RuntimeError,'synthetic interruption'):e.draw_set(3,31,'natural',d,batch_size=5,max_batches=1,M=5)
   base=Path(d)/'candidate_batches'/'natural';intent=json.loads((base/'batch_0000.intent.json').read_text())
   self.assertEqual((intent['set'],intent['batch_index'],intent['n'],intent['M']),('natural',0,5,5))
   self.assertEqual(intent['rng_before'],np.random.default_rng(31).bit_generator.state)
   self.assertFalse((base/'batch_0000.npz').exists())
 def test_journal_prefix_and_fixed_completion_modes(self):
  import validate_update_journal as validator
  self.assertEqual(validator.validate_records(iter(()))[0],0)
  with self.assertRaisesRegex(ValueError,'incomplete'):validator.validate_records(iter(()),complete=True)
  seeds=e.CFG['initialization_seeds']
  def records(steps=2000, omit=None):
   for seed in seeds:
    for arm in ('corrected','rare_boost'):
     for step in range(1,steps+1):
      if omit==(arm,seed,step):continue
      yield ({'arm':arm,'seed':seed,'step':step},None,None)
  self.assertEqual(validator.validate_records(records(),complete=True)[0],12000)
  self.assertEqual(validator.validate_records(records(steps=3))[0],18)
  with self.assertRaisesRegex(ValueError,'incomplete'):validator.validate_records(records(steps=3),complete=True)
  with self.assertRaisesRegex(ValueError,'nonconsecutive'):validator.validate_records(records(omit=('corrected',seeds[0],2)),complete=True)
 def test_original_draw_order_and_rng_state(self):
  # Small synthetic fixture, not an experiment sample or optimization run.
  seed=19;n=7;M=5
  original_rng=np.random.default_rng(seed);expected,expected_p=e.c.pilot.prior_batch(n,M,original_rng)
  reference=np.random.default_rng(seed);rp=reference.random((n,4));rs=reference.integers(0,4,n);ru=np.stack([reference.random(n) for _ in range(M)])
  rng=np.random.default_rng(seed);sample=e.candidate_batch(n,M,rng)
  np.testing.assert_array_equal(sample['probabilities'],rp);np.testing.assert_array_equal(sample['starts'],rs);np.testing.assert_array_equal(sample['uniforms'],ru)
  np.testing.assert_array_equal(sample['words'],expected)
  np.testing.assert_array_equal(sample['probabilities'],expected_p)
  self.assertEqual(str(sample['rng_after']),e.state_json(original_rng))
  replay=np.random.default_rng();replay.bit_generator.state=__import__('json').loads(str(sample['rng_before']))
  again=e.candidate_batch(n,M,replay)
  for k in ('words','probabilities','starts','uniforms','rng_after'):np.testing.assert_array_equal(sample[k],again[k])
  rebuilt=e.c.pilot.simulate_words(sample['probabilities'],sample['starts'],M,uniforms=sample['uniforms'])
  np.testing.assert_array_equal(rebuilt,expected)
  self.assertEqual(sample['uniforms'].shape,(M,n))
 def test_persisted_batches_and_truncation(self):
  import tempfile
  from pathlib import Path
  with tempfile.TemporaryDirectory() as d:
   selected,info=e.draw_set(7,23,'natural',d,batch_size=5,max_batches=2,M=5)
   self.assertEqual(info,{'drawn':10,'accepted_before_truncation':10,'saved':7})
   recovered=[];previous=None
   for index in range(2):
    with np.load(Path(d)/'candidate_batches'/'natural'/f'batch_{index:04d}.npz',allow_pickle=False) as z:
     self.assertEqual(int(z['global_candidate_start']),index*5)
     if previous is not None:self.assertEqual(str(z['rng_before']),previous)
     previous=str(z['rng_after']);self.assertTrue(z['eligible'].all())
     np.testing.assert_array_equal(e.c.pilot.simulate_words(z['probabilities'],z['starts'],5,uniforms=z['uniforms']),z['words'])
     self.assertEqual(int(z['selected'].sum()),5 if index==0 else 2)
     recovered.append(z['words'][z['selected']])
   np.testing.assert_array_equal(np.concatenate(recovered),selected)
 def test_rejected_candidates_and_selection_flags(self):
  import tempfile
  from pathlib import Path
  from unittest.mock import patch
  # Deterministic synthetic eligibility assigns alternating candidates to holdout.
  def groups(words):
   i=np.arange(len(words));return np.column_stack([i%2,i*0,i*0,i*0]),np.ones(len(words),bool)
  with tempfile.TemporaryDirectory() as d, patch.object(e,'group_stats',side_effect=groups), patch.object(e,'holdout',side_effect=lambda keys: keys[:,0].astype(bool)):
   selected,info=e.draw_set(1,29,'hold',d,batch_size=5,max_batches=1,M=5)
   self.assertEqual(info,{'drawn':5,'accepted_before_truncation':2,'saved':1})
   with np.load(Path(d)/'candidate_batches'/'hold'/'batch_0000.npz',allow_pickle=False) as z:
    np.testing.assert_array_equal(z['eligible'],[False,True,False,True,False])
    np.testing.assert_array_equal(z['selected'],[False,True,False,False,False])
    np.testing.assert_array_equal(selected,z['words'][z['selected']])
    self.assertEqual(len(z['words']),5)
 def test_full_update_journal_and_partial_detection(self):
  import tempfile,copy
  from pathlib import Path
  with tempfile.TemporaryDirectory() as d:
   m=e.c.Readout(11,'half_count_scaled');o=e.c.pilot.Adam(m.params)
   grad={k:np.full_like(v,(i+1)*.03125) for i,(k,v) in enumerate(sorted(m.params.items()))}
   original={k:v.copy() for k,v in m.params.items()};proposed={k:v.copy() for k,v in m.params.items()};next_o=copy.deepcopy(o);next_o.step(proposed,grad)
   path=Path(d)/'updates.bin';e.append_update_record(path,'synthetic',17,1,grad,proposed)
   # Simulate interruption immediately after durable prepare but before commit.
   records=list(e.read_update_records(path));self.assertEqual(len(records),1);self.assertEqual(o.t,0)
   for k in m.params:np.testing.assert_array_equal(m.params[k],original[k]);self.assertTrue(np.all(o.m[k]==0));self.assertTrue(np.all(o.v[k]==0))
   meta,g,p=records[0];self.assertEqual((meta['arm'],meta['seed'],meta['step'],meta['count']),('synthetic',17,1,353))
   self.assertEqual(meta['names'],sorted(m.params));self.assertEqual(meta['layout'],'all gradients then all post-update parameters')
   for k in m.params:np.testing.assert_array_equal(g[k],grad[k]);np.testing.assert_array_equal(p[k],proposed[k])
   o.step(m.params,grad)
   for k in m.params:np.testing.assert_array_equal(m.params[k],p[k]);np.testing.assert_array_equal(o.m[k],next_o.m[k]);np.testing.assert_array_equal(o.v[k],next_o.v[k])
   intact=path.read_bytes()
   for cut in (1,10):
    path.write_bytes(intact[:-cut])
    with self.assertRaisesRegex(ValueError,'truncated'):list(e.read_update_records(path))
   corrupt=bytearray(intact);corrupt[-1]^=1;path.write_bytes(corrupt)
   with self.assertRaisesRegex(ValueError,'checksum'):list(e.read_update_records(path))
 def test_exclusive_console_creation(self):
  import tempfile,os
  from pathlib import Path
  import launch_exclusive as launcher
  with tempfile.TemporaryDirectory() as d:
   path=Path(d)/'new.log';fd=launcher.open_new_log(path);os.write(fd,b'preserved');os.close(fd)
   with self.assertRaises(FileExistsError):launcher.open_new_log(path)
   self.assertEqual(path.read_bytes(),b'preserved')
 def test_immutable_atomic_npz_rejects_duplicate(self):
  import tempfile
  from pathlib import Path
  with tempfile.TemporaryDirectory() as d:
   path=Path(d)/'sample.npz';e.atomic_npz(path,value=np.array([1,2]))
   before=path.read_bytes()
   with self.assertRaises(FileExistsError):e.atomic_npz(path,value=np.array([9]))
   self.assertEqual(path.read_bytes(),before)
   with np.load(path,allow_pickle=False) as z:np.testing.assert_array_equal(z['value'],[1,2])
 def test_atomic_nested_output(self):
  import tempfile
  from pathlib import Path
  with tempfile.TemporaryDirectory() as d:
   path=Path(d)/'nested'/'data'/'status.json';e.dump(path,{'ok':True})
   self.assertEqual(__import__('json').loads(path.read_text()),{'ok':True})
 def test_incremental_updates_and_full_optimizer_roundtrip(self):
  import tempfile,csv
  from pathlib import Path
  with tempfile.TemporaryDirectory() as d:
   path=Path(d)/'updates.csv';e.append_csv(path,{'step':1,'loss':.25});e.append_csv(path,{'step':2,'loss':.125})
   with path.open(newline='') as f:self.assertEqual(list(csv.DictReader(f)),[{'step':'1','loss':'0.25'},{'step':'2','loss':'0.125'}])
   m=e.c.Readout(11,'half_count_scaled');o=e.c.pilot.Adam(m.params,readout_lr=.003,beta1=.9,beta2=.999,epsilon=1e-8)
   # A synthetic hand-written gradient tests state I/O; no fit or data draw.
   grad={k:np.full_like(v,.125) for k,v in m.params.items()};o.step(m.params,grad)
   e.checkpoint_state(Path(d)/'checkpoint.npz',m,o,1)
   m2=e.c.Readout(12,'half_count_scaled');o2=e.c.pilot.Adam(m2.params);e.restore_checkpoint(Path(d)/'checkpoint.npz',m2,o2)
   self.assertEqual(o2.t,o.t)
   for k in m.params:
    np.testing.assert_array_equal(m2.params[k],m.params[k]);np.testing.assert_array_equal(o2.m[k],o.m[k]);np.testing.assert_array_equal(o2.v[k],o.v[k])
   o.step(m.params,grad);o2.step(m2.params,grad)
   for k in m.params:np.testing.assert_array_equal(m2.params[k],m.params[k])

if __name__=='__main__':unittest.main(verbosity=2)
