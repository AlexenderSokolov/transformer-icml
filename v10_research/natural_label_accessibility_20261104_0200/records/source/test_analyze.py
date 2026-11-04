import importlib.util, unittest
import numpy as np
class AnalysisTests(unittest.TestCase):
    def test_paired_independent_replicate_screen(self):
        self.assertIsNotNone(importlib.util.find_spec('analyze'),'analysis implementation absent')
        from analyze import screening
        a=screening([.01,.02,.03,.01],[.005,.015,.02,.009],.02,.01)
        self.assertEqual(a['replicates_at_or_below_threshold'],3)
        self.assertTrue(a['passes_descriptive_screen'])
        self.assertAlmostEqual(a['median_paired_natural_minus_teacher'],.005)
if __name__=='__main__':unittest.main(verbosity=2)
