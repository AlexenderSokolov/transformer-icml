"""Independent literal oracle; changing count window/orientation/gate should fail."""
import itertools, math, unittest
from fractions import Fraction
import numpy as np
import experiment as e

def literal(w):
    M=len(w)-2; u=tuple(w[-2:]); d=1-u[0]
    h=[[0,0] for _ in range(4)]; D=0
    for i in range(M):
        h[2*w[i]+w[i+1]][w[i+2]]+=1
        if i<M//2 and tuple(w[i:i+2])==u:D+=1
    J=sum(h[2*u[0]+u[1]]); C=h[2*u[0]+u[1]][d]
    a=C/J if J and 512*D>=J else 0
    return np.array(h),J,C,D,(h[2*u[0]+u[1]][1]+1)/(J+2),a if d else 1-a

def mass(w):
    h=literal(w)[0]; z=Fraction(1,4)
    for x,y in h:z*=Fraction(math.factorial(int(x))*math.factorial(int(y)),math.factorial(int(x+y+1)))
    return z

class Tests(unittest.TestCase):
    def test_all_small_words(self):
        for M in range(11):
            w=np.array(list(itertools.product((0,1),repeat=M+2)),dtype=np.int64)
            z=e.from_words(w)
            total=Fraction(0)
            for i,ww in enumerate(w.tolist()):
                h,J,C,D,b,a=literal(ww)
                np.testing.assert_array_equal(z['H'][i],h)
                for k,v in [('J',J),('C',C),('D',D),('B',b),('A',a)]:self.assertEqual(z[k][i],v)
                pw=mass(ww);total+=pw
                self.assertEqual(mass(ww+[1])/pw,Fraction(int(h[2*ww[-2]+ww[-1],1])+1,J+2))
            self.assertEqual(total,1)
    def test_identical_uniforms(self):
        rng=np.random.Generator(np.random.PCG64(8675309))
        for M in [0,1,2,3,17,64]:
            p=rng.random((31,4));initial=rng.integers(0,4,size=31);v=rng.random((M,31))
            words=[]
            for i in range(31):
                w=[int(initial[i]//2),int(initial[i]%2)]
                for t in range(M):w.append(int(v[t,i]<p[i,2*w[-2]+w[-1]]))
                words.append(w)
            z=e.simulate(p,initial,M,uniforms=v); ref=e.from_words(np.array(words))
            for k in ref:np.testing.assert_array_equal(z[k],ref[k])
            np.testing.assert_array_equal(z['p'],p[np.arange(31),2*np.array(words)[:,-2]+np.array(words)[:,-1]])
    def test_gate_boundaries_orientation(self):
        J=np.array([0,0,512,513,512,513]);C=np.array([0,0,128,128,128,128]);D=np.array([0,0,1,1,1,1]);u=np.array([0,2,0,0,2,2])
        a,accepted=e.gate(J,C,D,u)
        np.testing.assert_array_equal(a,[0,1,.25,0,.75,1])
        np.testing.assert_array_equal(accepted,[False,False,True,False,True,False])
    def test_metrics(self):
        z=e.from_words(np.array([[0,0,0,0],[1,1,1,1],[0,1,0,1]]));z['p']=np.array([.1,.9,.4])
        out=e.metrics(z,64)
        b=z['B'];q=(1-2/8)*z['A']+1/8
        np.testing.assert_allclose(out['expected_logloss_Q'],-b*np.log(q)-(1-b)*np.log1p(-q),rtol=1e-14)
        self.assertTrue(np.all(out['excess_KL_B_Q']>=0))
        self.assertTrue(np.all(np.isfinite(out['expected_logloss_Q'])))
        for bad in [np.array([[-.1,.5,.5,.5]]),np.array([[np.nan,.5,.5,.5]])]:
            with self.assertRaises(ValueError):e.simulate(bad,np.array([0]),1,uniforms=np.array([[.2]]))
if __name__=='__main__':unittest.main(verbosity=2)
