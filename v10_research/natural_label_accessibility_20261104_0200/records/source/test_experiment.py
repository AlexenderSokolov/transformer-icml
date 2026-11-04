import importlib.util, tempfile, unittest
from pathlib import Path
import numpy as np

class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(importlib.util.find_spec('experiment'),'runner implementation absent')
        import experiment
        self.e=experiment
    def test_table_pooling_and_unseen_default(self):
        J=np.array([1,1,2,1]);C=np.array([0,0,1,1]);y=np.array([0,1,1,1])
        table=self.e.fit_table([(J,C,y)])
        q=self.e.table_predict(table,np.array([1,1,2,3]),np.array([0,1,1,0]))
        np.testing.assert_allclose(q,[.5,2/3,2/3,.5])
    def test_metrics_and_overlaps(self):
        x=np.array([.2,.6]);s=self.e.summarize(x)
        self.assertAlmostEqual(s['mean'],.4);self.assertAlmostEqual(s['mc_se'],.2)
        a=np.array([[0,1,0],[1,0,1]],np.int8);b=np.array([[0,1,0],[0,1,0],[0,0,1]],np.int8)
        self.assertEqual(self.e.word_overlap([a],b),2)
    def test_natural_loader_excludes_teacher_and_latents(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'train.npz';np.savez(p,H=np.ones((1,8)),U=np.array([0]),J=np.array([2]),C=np.array([1]),y=np.array([0]),B=np.array([.5]),p=np.ones((1,4)))
            a=self.e.load_training(p,'y');self.assertEqual(set(a),{'H','U','J','C','target'});self.assertEqual(a['target'][0],0)
            a=self.e.load_training(p,'B');self.assertEqual(a['target'][0],.5)
    def test_source_gate_refuses_before_data_generation(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises((FileNotFoundError,ValueError)):
                self.e.check_sources(Path(d)/'missing_receipt.json')

if __name__=='__main__':unittest.main(verbosity=2)
