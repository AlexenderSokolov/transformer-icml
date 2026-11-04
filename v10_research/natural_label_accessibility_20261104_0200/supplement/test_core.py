"""Deterministic correctness tests only; no experimental RNG or fitting."""
import importlib.util, itertools, math, unittest
import numpy as np
from pathlib import Path

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(importlib.util.find_spec('core'), 'core implementation absent')
        import core
        self.c=core
    def test_counts_literal_and_label_exclusion(self):
        w=np.array(list(itertools.product([0,1],repeat=6)),dtype=np.int8)
        H,U,J,C,B=self.c.statistics(w)
        for i,x in enumerate(w):
            literal=[0]*8
            for j in range(len(x)-2): literal[4*int(x[j])+2*int(x[j+1])+int(x[j+2])]+=1
            self.assertEqual(H[i].tolist(),literal)
            self.assertEqual(U[i],2*x[-2]+x[-1]);self.assertEqual(J[i],sum(literal[2*U[i]:2*U[i]+2]))
            self.assertEqual(C[i],literal[2*U[i]+1]);self.assertAlmostEqual(B[i],(C[i]+1)/(J[i]+2))
        self.assertTrue(np.all(H.sum(1)==4))
    def test_deterministic_simulation_and_heldout_label(self):
        p=np.array([[0,1,0,1],[1,0,1,0]],float);starts=np.array([0,3]);draws=np.full((2,4),0.5)
        w,y=self.c.simulate_from_draws(p,starts,draws)
        self.assertEqual(w.tolist(),[[0,0,0,0,0],[1,1,0,1,0]])
        self.assertEqual(y.tolist(),[0,1]);self.assertEqual(self.c.statistics(w)[0].sum(1).tolist(),[3,3])
    def test_prior_word_mass_and_next_label_identity(self):
        def mass(w):
            H=self.c.statistics(np.array([w],np.int8))[0][0]
            ans=.25
            for u in range(4):
                a,b=map(int,H[2*u:2*u+2]);ans*=math.factorial(a)*math.factorial(b)/math.factorial(a+b+1)
            return ans
        words=list(itertools.product([0,1],repeat=5))
        self.assertAlmostEqual(sum(map(mass,words)),1,places=13)
        for w in words:
            b=self.c.statistics(np.array([w],np.int8))[-1][0]
            self.assertAlmostEqual(mass(w+(1,))/mass(w),b,places=13)
    def test_pool_token_equivalence_and_matched_initialization(self):
        w=np.array([[0,0,1,1,0,1],[1,1,1,0,0,1]],np.int8);H,U,*_=self.c.statistics(w)
        flat=np.sin(np.arange(self.c.PARAM_COUNT,dtype=float))*.03
        S,*_=self.c.unpack(flat);S[:]=0
        q0=self.c.predict(flat,H,U,4,False);q1=self.c.predict(flat,H,U,4,True)
        np.testing.assert_array_equal(q0,q1)
        S[:]=np.cos(np.arange(64)).reshape(2,4,8)*.2
        pool=self.c.pooling(flat,H,U,True)
        for n,x in enumerate(w):
            ts=4*x[:-2]+2*x[1:-1]+x[2:]
            for h in range(2):
                a=np.exp(S[h,U[n],ts]);a/=a.sum();literal=np.eye(8)[ts].T@a
                np.testing.assert_allclose(pool[n,h],literal,atol=1e-14)
    def test_full_gradient_finite_difference(self):
        H=np.array([[2,1,0,3,1,0,1,0],[0,2,1,0,0,2,1,2]],float);U=np.array([0,3]);t=np.array([.2,.8])
        p=np.sin(np.arange(self.c.PARAM_COUNT,dtype=float))*.05
        for learned in [False,True]:
            loss,g=self.c.loss_grad(p,H,U,8,t,learned)
            self.assertTrue(np.isfinite(loss))
            for i in range(len(p)):
                pp=p.copy();pm=p.copy();pp[i]+=1e-6;pm[i]-=1e-6
                numeric=(self.c.loss_grad(pp,H,U,8,t,learned)[0]-self.c.loss_grad(pm,H,U,8,t,learned)[0])/2e-6
                self.assertLess(abs(numeric-g[i]),2e-7,(learned,i,numeric,g[i]))
    def test_rao_blackwell_gradient_identity_at_fixed_input(self):
        H=np.array([[2,1,0,3,1,0,1,0]],float);U=np.array([0]);p=np.sin(np.arange(self.c.PARAM_COUNT))*.05;b=.4
        gb=self.c.loss_grad(p,H,U,8,np.array([b]),True)[1]
        g0=self.c.loss_grad(p,H,U,8,np.array([0.]),True)[1];g1=self.c.loss_grad(p,H,U,8,np.array([1.]),True)[1]
        np.testing.assert_allclose(gb,(1-b)*g0+b*g1,atol=1e-14)
    def test_adam_first_step_and_kl_edges(self):
        p=np.array([.2,-.3]);g=np.array([.1,-.2]);z=np.zeros(2)
        q,m,v=self.c.adam_step(p,g,z,z,1,{'lr':.003,'beta1':.9,'beta2':.999,'epsilon':1e-8})
        np.testing.assert_allclose(q,p-.003*g/(np.abs(g)+1e-8),atol=1e-14)
        np.testing.assert_allclose(self.c.kl(np.array([0.,1.,.5]),np.array([.25,.75,.5])),[-math.log(.75),-math.log(.75),0])
        self.assertTrue(np.all(self.c.kl(np.array([0.,1.]),np.array([1e-8,1-1e-8]))>=0))

if __name__=='__main__':unittest.main(verbosity=2)
