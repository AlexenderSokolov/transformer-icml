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
   self.assertEqual(e.split_key(key),expected)
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
if __name__=='__main__':unittest.main(verbosity=2)
