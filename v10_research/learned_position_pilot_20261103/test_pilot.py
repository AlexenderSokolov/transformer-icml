import inspect,itertools,math,unittest
from fractions import Fraction
import numpy as np
import pilot
SEED=20261103104

class Tests(unittest.TestCase):
    def test_counts_posterior_and_gate_exhaustive(self):
        for M in range(1,7):
            words=np.array(list(itertools.product([0,1],repeat=M+2)),dtype=np.int8)
            result=pilot.statistics(words)
            masses=Fraction()
            for r,w in enumerate(words.tolist()):
                H=np.zeros((4,2),dtype=int)
                for i in range(M):H[2*w[i]+w[i+1],w[i+2]]+=1
                u=2*w[-2]+w[-1];J=int(H[u].sum());C=int(H[u,1]);D=sum(2*w[i]+w[i+1]==u for i in range(M//2))
                B=Fraction(C+1,J+2)
                mass=Fraction(1,4)
                for row in H:mass*=Fraction(math.factorial(int(row[0]))*math.factorial(int(row[1])),math.factorial(int(row.sum())+1))
                masses+=mass
                self.assertEqual(result['J'][r],J);self.assertEqual(result['C'][r],C);self.assertEqual(result['D'][r],D)
                self.assertAlmostEqual(result['B'][r],float(B),places=15)
                A=C/J if J>0 and 512*D>=J else w[-2]
                self.assertEqual(result['A'][r],A)
                # Exact posterior predictive identity via one additional observed transition.
                Hp=H.copy();Hp[u,1]+=1
                extended=Fraction(1,4)
                for row in Hp:extended*=Fraction(math.factorial(int(row[0]))*math.factorial(int(row[1])),math.factorial(int(row.sum())+1))
                self.assertEqual(extended/mass,B)
            self.assertEqual(masses,1)

    def test_simulator_literal(self):
        rng=np.random.default_rng(SEED);p=rng.random((11,4));starts=rng.integers(0,4,11);uniforms=rng.random((17,11))
        words=pilot.simulate_words(p,starts,17,uniforms=uniforms)
        expected=[]
        for j in range(11):
            w=[int(starts[j]//2),int(starts[j]%2)]
            for t in range(17):w.append(int(uniforms[t,j]<p[j,2*w[-2]+w[-1]]))
            expected.append(w)
        np.testing.assert_array_equal(words,expected)
        with self.assertRaises(ValueError):pilot.simulate_words(np.ones((11,4))*2,starts,17,uniforms=uniforms)

    def test_feature_bank_against_literal(self):
        rng=np.random.default_rng(SEED);words=rng.integers(0,2,(9,13),dtype=np.int8)
        model=pilot.Model(SEED,'learned');q,cache=model.forward(words,cache=True)
        alpha=cache['alpha'];expected=[]
        for w in words:
            e=np.zeros((11,8))
            for i in range(11):e[i,4*w[i]+2*w[i+1]+w[i+2]]=1
            full=alpha@e;u=2*w[-2]+w[-1]
            selected=full[:,2*u:2*u+2].reshape(-1)
            expected.append(np.r_[selected,w[-2:],1/11])
        np.testing.assert_allclose(cache['x'],expected,atol=1e-15)
        self.assertEqual(sum(x.size for x in model.params.values()),369)
        self.assertTrue(np.all((q>0)&(q<1)))

    def test_all_parameter_gradients(self):
        rng=np.random.default_rng(SEED);words=rng.integers(0,2,(5,11),dtype=np.int8);target=np.array([.1,.25,.5,.7,.9])
        model=pilot.Model(SEED,'learned');loss,grad=model.loss_grad(words,target)
        largest=0
        for name,param in model.params.items():
            for index in np.ndindex(param.shape):
                old=param[index];eps=1e-6
                param[index]=old+eps;plus=pilot.cross_entropy(target,model.predict(words)).mean()
                param[index]=old-eps;minus=pilot.cross_entropy(target,model.predict(words)).mean()
                param[index]=old
                numeric=(plus-minus)/(2*eps);err=abs(numeric-grad[name][index]);largest=max(largest,err)
                self.assertLess(err,2e-8,(name,index,numeric,grad[name][index]))
        print('gradient_max_absolute_error',largest)

    def test_attack_contract_and_no_hidden_inputs(self):
        self.assertEqual(list(inspect.signature(pilot.attack).parameters),['predict','words','k','family'])
        for M in range(1,8):
            words=np.array(list(itertools.product([0,1],repeat=M+2)),dtype=np.int8)
            for k in range(M+1):
                for family in ['training','heldout']:
                    candidates=pilot.proposals(words,k,family)
                    self.assertTrue(np.all((candidates==0)|(candidates==1)))
                    self.assertTrue(np.all(np.sum(candidates!=words[None],axis=2)<=k))
                    np.testing.assert_array_equal(candidates[:,:,-2:],np.broadcast_to(words[None,:,-2:],candidates[:,:,-2:].shape))
                    attacked,info=pilot.attack(lambda z:np.full(len(z),.5),words,k,family)
                    np.testing.assert_array_equal(attacked,words);np.testing.assert_array_equal(info['selected'],0)
        with self.assertRaises(ValueError):pilot.proposals(words,-1,'training')
        with self.assertRaises(ValueError):pilot.proposals(words,M+1,'training')

    def test_attack_exact_finite_max(self):
        rng=np.random.default_rng(SEED);words=rng.integers(0,2,(8,18),dtype=np.int8);model=pilot.Model(SEED,'learned')
        candidates=pilot.proposals(words,4,'training');target=pilot.statistics(words)['B']
        loss=np.array([pilot.cross_entropy(target,model.predict(z)) for z in candidates])
        attacked,info=pilot.attack(model.predict,words,4,'training')
        np.testing.assert_allclose(pilot.cross_entropy(target,model.predict(attacked)),loss.max(axis=0),rtol=0,atol=1e-14)
        np.testing.assert_array_equal(info['selected'],loss.argmax(axis=0))

    def test_frozen_controls_and_uniform_invariance(self):
        rng=np.random.default_rng(SEED);words=rng.integers(0,2,(10,18),dtype=np.int8);target=pilot.statistics(words)['B']
        for mode in ['uniform','random','half']:
            model=pilot.Model(SEED,mode);old=model.params['a'].copy();optimizer=pilot.Adam(model.params)
            loss,grad=model.loss_grad(words,target);self.assertTrue(np.all(grad['a']==0));optimizer.step(model.params,grad)
            np.testing.assert_array_equal(old,model.params['a'])
            _,cache=model.forward(words,cache=True)
            if mode=='uniform':
                f=cache['x'][:,:6].reshape(-1,3,2)
                np.testing.assert_array_equal(f[:,0],f[:,1]);np.testing.assert_array_equal(f[:,0],f[:,2])
            if mode=='half':
                self.assertEqual(cache['alpha'][1,8:].sum(),0);self.assertEqual(cache['alpha'][2,:8].sum(),0)
        # Same-count words with different temporal ordering must be indistinguishable to uniform controls.
        allwords=np.array(list(itertools.product([0,1],repeat=10)),dtype=np.int8);s=pilot.statistics(allwords)
        groups={}
        for i,w in enumerate(allwords):
            key=(int(s['J'][i]),int(s['C'][i]),tuple(w[-2:]))
            if key in groups:
                model=pilot.Model(SEED,'uniform');np.testing.assert_allclose(np.ptp(model.predict(allwords[[groups[key],i]])),0,atol=1e-15)
                break
            groups[key]=i

    def test_weighted_edit_gradient_and_update(self):
        rng=np.random.default_rng(SEED);w=rng.integers(0,2,(7,15),dtype=np.int8);model=pilot.Model(SEED,'learned');target=pilot.statistics(w)['B']
        z,_=pilot.attack(model.predict,w,2,'training');both=np.concatenate([w,z]);labels=np.tile(target,2)
        combined,g=model.loss_grad(both,labels);l1,g1=model.loss_grad(w,target);l2,g2=model.loss_grad(z,target)
        self.assertAlmostEqual(combined,.5*(l1+l2))
        for name in g:np.testing.assert_allclose(g[name],.5*(g1[name]+g2[name]),atol=1e-15)
        before=combined
        for name in model.params:model.params[name]-=1e-4*g[name]
        after=pilot.cross_entropy(labels,model.predict(both)).mean();self.assertLess(after,before)

    def test_stress_certificates(self):
        for M in [64,128,256]:
            for name,p in pilot.stress_sources(M).items():
                P=np.zeros((4,4))
                for u in range(4):P[u,2*(u%2)]=1-p[u];P[u,2*(u%2)+1]=p[u]
                mat=P.T-np.eye(4);mat[-1]=1;rhs=np.array([0.,0.,0.,1.]);pi=np.linalg.solve(mat,rhs)
                self.assertTrue(np.all(P@P>=pi[None,:]/M-1e-14),(M,name))

if __name__=='__main__':unittest.main(verbosity=2)
