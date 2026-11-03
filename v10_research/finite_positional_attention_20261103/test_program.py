"""Independent exact oracles; tests written before program implementation."""
import importlib.util
import itertools
import random
import unittest
from fractions import Fraction
from pathlib import Path

P = Path(__file__).with_name('program.py')

class Contract(unittest.TestCase):
    def setUp(self):
        self.assertTrue(P.exists(), 'finite attention evaluator has not been implemented')
        spec = importlib.util.spec_from_file_location('finite_program', P)
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)

    def test_scalar_grid_bit_extraction(self):
        self.assertTrue(hasattr(self.m, 'scalar_grid_bits'), 'paid scalar extraction missing')
        for h in range(10):
            Q=1<<h
            for numerator in range(Q+1):
                rails=self.m.scalar_grid_bits(Fraction(numerator,Q),h)
                self.assertEqual(rails,tuple((numerator>>i)&1 for i in range(h+1)))
                self.assertTrue(all(x in (0,1) for x in rails))

    def test_full_batch_suffix(self):
        self.assertTrue(hasattr(self.m, 'evaluate'), 'full batch suffix missing')
        for z in ((0,0,0),(1,0,1,1),(0,1)*34):
            cut=self.m.prefix(z,4)
            self.assertEqual(self.m.evaluate(z,4,6),self.m.readout(cut,6))
            changed=(0,)*12
            self.assertEqual(self.m.evaluate(z,4,6,changed),self.m.readout(self.m.replace_bank(cut,changed),6))

    def test_bit_arithmetic(self):
        for w in range(1, 7):
            b = self.m.Bits(w)
            for x in range(1 << w):
                for y in range(1 << w):
                    X,Y=b.enc(x),b.enc(y)
                    self.assertEqual(b.val(b.add(X,Y)), (x+y) % (1<<w))
                    self.assertEqual(b.ge(X,Y), int(x>=y))
                    if y:
                        q,r=b.div(X,Y)
                        self.assertEqual((b.val(q),b.val(r)), divmod(x,y))

    def test_all_small_words_all_banks(self):
        for M in range(1, 8):
            for z in itertools.product((0,1), repeat=M+2):
                counts=[]
                for a,b in itertools.product((0,1),repeat=2):
                    loc=[i for i in range(M) if z[i:i+2]==(a,b)]
                    counts += [len(loc),sum(z[i+2]==1-a for i in loc),sum(i<M//2 for i in loc)]
                for h in (0,1,3,7):
                    cut=self.m.prefix(z,h)
                    self.assertEqual(set(cut), {'bank','endpoint','h'})
                    self.assertEqual(cut['endpoint'], z[-2:])
                    Q=1<<h
                    expected=[(2*Q*c+M)//(2*M) for c in counts]
                    self.assertEqual(cut['bank'],tuple(expected))
                    for got,c in zip(cut['bank'],counts):
                        self.assertLessEqual(abs(Fraction(got,Q)-Fraction(c,M)),Fraction(1,2*Q))
                    for r in (0,3):
                        result=self.m.readout(cut,r)
                        j,c,d=expected[3*(2*z[-2]+z[-1]):][:3]
                        c,d=min(c,j),min(d,j)
                        exact=Fraction(c,j) if j and 512*d>=j else Fraction(0)
                        predicted=Fraction(result[1-z[-2]],1<<r)
                        self.assertLessEqual(abs(predicted-exact),Fraction(1,1<<r))
                        self.assertEqual(sum(result),1<<r)

    def test_masks_exact_legal_keys(self):
        for M in (1,2,3,64,65):
            masks,flags=self.m.metadata(M)
            n=M+3
            self.assertEqual(masks[2][-1],tuple(range(2,M+2)))
            for mask in masks:
                for t,keys in enumerate(mask):
                    self.assertTrue(keys)
                    self.assertTrue(all(0<=j<=t for j in keys))
            self.assertEqual(sum(flags),M//2)
            self.assertEqual(flags[-1],0)

    def test_boundary_and_fault_readout(self):
        h=10; Q=1<<h
        for j,c,d,accept in [(0,0,0,False),(512,123,1,True),(513,123,1,False),(511,123,1,True),(1,1,0,False),(1,1,1,True),(4,9,8,True)]:
            bank=(j,c,d)+(0,)*9
            cut={'bank':bank,'endpoint':(0,0),'h':h}
            out=self.m.readout(cut,10)
            self.assertEqual(out[1],(Q*min(c,j))//j if accept else 0)
        rng=random.Random(1729)
        for M in (64,65,127,512,1027):
            z=tuple(rng.randrange(2) for _ in range(M+2))
            cut=self.m.prefix(z,5)
            bank=tuple(max(0,min(32,x+rng.randrange(-2,3))) for x in cut['bank'])
            changed=self.m.replace_bank(cut,bank)
            self.assertEqual(changed['bank'],bank)
            self.assertEqual(changed['endpoint'],cut['endpoint'])
            out=self.m.readout(changed,9)
            self.assertEqual(sum(out),512)
            self.assertTrue(all(x>=0 for x in out))

if __name__=='__main__': unittest.main()
