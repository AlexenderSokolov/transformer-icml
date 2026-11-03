import unittest
import numpy as np
import calibration as c

class Tests(unittest.TestCase):
    def test_literal_collision_and_boundary(self):
        w=c.collision_words();s=c.literal_statistics(w)
        np.testing.assert_array_equal(s['H'][0].reshape(-1),[0,1,0,2,1,0,2,58]);np.testing.assert_array_equal(s['H'][0],s['H'][1])
        np.testing.assert_array_equal(s['H'][2],s['H'][3]);np.testing.assert_array_equal(s['J'],[1,1,1,1]);np.testing.assert_array_equal(s['C'],[0,0,1,1]);np.testing.assert_array_equal(s['D'],[1,0,1,0])
        np.testing.assert_array_equal(s['Q'],[.125,.875,.875,.125]);np.testing.assert_array_equal(w[:,-2:],[[1,0],[1,0],[0,1],[0,1]])
        s2=c.literal_statistics(c.collision_words(31,32));np.testing.assert_array_equal(s2['D'],[1,0,1,0]);np.testing.assert_array_equal(s2['Q'],s['Q'])

    def test_independent_feature_decoder(self):
        w=np.concatenate([c.collision_words(),c.collision_words(31,32),np.zeros((1,66),dtype=np.int8),np.ones((1,66),dtype=np.int8),np.tile([0,1],(1,33))])
        s=c.literal_statistics(w);x=c.features(w,'half_normalized')
        np.testing.assert_allclose(c.decode_features(x),s['Q'],atol=1e-14,rtol=0)
        np.testing.assert_allclose(c.pilot.statistics(w)['Q'],s['Q'],atol=1e-14,rtol=0)
        np.testing.assert_array_equal(x[:4,0:2],[[1/64,0],[1/64,0],[0,1/64],[0,1/64]])
        np.testing.assert_allclose(x[:4,2:4].sum(1),s['D'][:4]/32,atol=0,rtol=0)

    def test_matched_initialization_and_function_class(self):
        x=c.features(c.collision_words(),'half_normalized')
        for seed in [20261103201,20261103202,20261103203]:
            a=c.Readout(seed,'half_normalized');b=c.Readout(seed,'half_count_scaled')
            np.testing.assert_allclose(a.predict(x),b.predict(x),rtol=0,atol=1e-14)
            np.testing.assert_allclose(a.params['W'],b.effective_W(),rtol=0,atol=1e-14)
            self.assertEqual(sum(v.size for v in a.params.values()),353)
            # Any new W has the same exact linear reparameterization, not only initial W.
            a.params['W']*=2.3;b.params['W']=a.params['W']/b.scale[:,None]
            np.testing.assert_allclose(a.predict(x),b.predict(x),rtol=0,atol=1e-14)

    def test_all_readout_gradients(self):
        w=np.concatenate([c.collision_words(),np.zeros((1,66),dtype=np.int8),np.ones((1,66),dtype=np.int8),np.tile([0,1],(1,33))]);target=c.literal_statistics(w)['Q'];largest=0
        for condition in ['half_normalized','half_count_scaled','uniform_control']:
            x=c.features(w,condition);model=c.Readout(20261103201,condition);loss,grad,_=model.loss_grad(x,target)
            for name,param in model.params.items():
                for idx in np.ndindex(param.shape):
                    old=param[idx];eps=1e-6;param[idx]=old+eps;plus=c.pilot.cross_entropy(target,model.predict(x)).mean();param[idx]=old-eps;minus=c.pilot.cross_entropy(target,model.predict(x)).mean();param[idx]=old
                    numeric=(plus-minus)/(2*eps);error=abs(numeric-grad[name][idx]);largest=max(largest,error)
                    self.assertLess(error,2e-7,(condition,name,idx,error))
        print('all_readout_gradient_max_absolute_error',largest)

    def test_uniform_collision_information_floor(self):
        w=c.collision_words();q=c.literal_statistics(w)['Q'];x=c.features(w,'uniform_control');np.testing.assert_array_equal(x[0],x[1]);np.testing.assert_array_equal(x[2],x[3])
        for a in [.001,.1,.5,.9,.999]:
            for b in [.001,.1,.5,.9,.999]:
                pred=np.array([a,a,b,b]);self.assertGreaterEqual(c.kl(q,pred).mean()+1e-14,c.collision_floor())
        self.assertAlmostEqual(c.kl(q,np.full(4,.5)).mean(),c.collision_floor(),places=14)
        for seed in [20261103201,20261103202,20261103203]:self.assertGreaterEqual(c.kl(q,c.Readout(seed,'uniform_control').predict(x)).mean()+1e-14,c.collision_floor())

    def test_no_pooling_update_and_adam_not_invariant(self):
        x=c.features(c.collision_words(),'half_normalized');q=c.literal_statistics(c.collision_words())['Q']
        a=c.Readout(20261103201,'half_normalized');b=c.Readout(20261103201,'half_count_scaled');oa=c.pilot.Adam(a.params);ob=c.pilot.Adam(b.params)
        _,ga,_=a.loss_grad(x,q);_,gb,_=b.loss_grad(x,q);oa.step(a.params,ga);ob.step(b.params,gb)
        self.assertEqual(set(a.params),{'W','b','v','c'});self.assertEqual(set(b.params),{'W','b','v','c'})
        self.assertGreater(np.max(abs(a.predict(x)-b.predict(x))),1e-8)

if __name__=='__main__':unittest.main(verbosity=2)
