"""Independent deterministic pipeline fixtures, never experimental data or training.
Synthetic local roundtrips below test gates only; they are not Space evidence.
"""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import analyze
import capture
import experiment

BINDING = 'b' * 64
CONDITIONS = ['uniform_y', 'uniform_B', 'learned_y', 'learned_B']
CFG = {'replicates': 4, 'conditions': CONDITIONS, 'steps': 1500,
       'train_horizons': [32, 64], 'test_horizons': [32, 64, 128],
       'rare_J_max': 3, 'primary_threshold_nats': .02,
       'natural_minus_teacher_median_threshold_nats': .01}


def seal_fixture(d):
    archive = capture.make_archive(d, sorted(p.name for p in d.iterdir()), d / 'output.zip', 'output', BINDING)
    copy = d / 'synthetic_local_roundtrip.zip'
    copy.write_bytes(archive.read_bytes())
    receipt = capture.make_receipt(archive, copy, 'libfile_synthetic_unit_test_not_service_evidence')
    capture.dump(d / 'receipt.json', receipt)


def complete_fixture(root, rep, condition, metadata=None, alter_targets=False):
    d = root / 'runs' / f'rep{rep}' / condition
    d.mkdir(parents=True)
    started = {'status': 'INCOMPLETE_UNLESS_COMPLETED_FILE_EXISTS', 'replicate': rep, 'condition': condition,
               'source_manifest_sha256': BINDING, 'input_archive_sha256': f'{rep+1:064x}'}
    started.update(metadata or {})
    capture.dump(d / 'STARTED.json', started)
    J, C = np.array([2, 4, 8, 0]), np.array([0, 2, 6, 0])
    B = (C + 1) / (J + 2)
    pt, y = np.array([.2, .5, .8, .6]), np.array([0, 1, 1, 0])
    if alter_targets:
        y[0] = 1
    summary = {}
    for M in CFG['test_horizons']:
        q = B + (CONDITIONS.index(condition) + 1) * .005 + rep * .001 + M * .00001
        payload = {'J': J, 'C': C, 'B': B, 'p_terminal': pt, 'y': y}
        cell = {}
        for name in ['model', 'Bayes', 'KT', 'unigram', 'half', 'empirical_JC']:
            pred = q if name == 'model' else B
            payload[name + '_q'] = pred
            cell[name] = {}
            for metric, values in experiment.metrics(pt, B, y, pred).items():
                payload[name + '_' + metric] = values
                cell[name][metric] = {'all': experiment.summarize(values), 'rare_J_le_3': experiment.summarize(values[J <= 3])}
        experiment.save_npz(d / f'evaluation_M{M}.npz', **payload)
        summary[str(M)] = cell
    capture.dump(d / 'summary.json', summary)
    capture.dump(d / 'COMPLETED.json', {'status': 'COMPLETE', 'steps': CFG['steps']})
    seal_fixture(d)
    return d


class IndependentPipelineReviewTests(unittest.TestCase):
    def test_nonfinite_candidate_is_saved_before_abort(self):
        # Exercise only failure capture. Both model-gradient and update functions
        # are injected fixed values; no statistical model is trained here.
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inputs = root / 'runs' / 'rep0' / 'inputs'
            inputs.mkdir(parents=True)
            experiment.save_npz(inputs / 'train_M32.npz', H=np.zeros((1, 8)), U=np.array([0]),
                                J=np.array([0]), C=np.array([0]), y=np.array([0]))
            initial = np.zeros(experiment.PARAM_COUNT)
            experiment.save_npz(inputs / 'optimization.npz', initial_parameters=initial,
                                batches=np.zeros((1, 1), dtype=int), horizons=np.array([32]))
            capture.dump(inputs / 'STARTED.json', {'status': 'INCOMPLETE_UNLESS_COMPLETED_FILE_EXISTS',
                                                 'replicate': 0, 'source_manifest_sha256': BINDING})
            capture.dump(inputs / 'COMPLETED.json', {'status': 'COMPLETE'})
            archive = capture.make_archive(inputs, sorted(p.name for p in inputs.iterdir()), inputs / 'input.zip', 'input', BINDING)
            copy = inputs / 'synthetic_local_roundtrip.zip'
            copy.write_bytes(archive.read_bytes())
            capture.dump(inputs / 'receipt.json', capture.make_receipt(archive, copy, 'libfile_synthetic_unit_test_not_service_evidence'))
            bad = np.full_like(initial, np.nan)
            cfg = dict(CFG, steps=1, train_horizons=[32], test_horizons=[])
            cfg['optimizer'] = {'lr': .003, 'beta1': .9, 'beta2': .999, 'epsilon': 1e-8}
            with patch.object(experiment, 'ROOT', root), patch.object(experiment, 'check_sources', return_value=(cfg, BINDING)), patch.object(experiment, 'resources'), patch.object(experiment, 'prior_outputs'), patch.object(experiment, 'loss_grad', return_value=(float('nan'), bad)), patch.object(experiment, 'adam_step', return_value=(bad, bad, bad)), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(FloatingPointError):
                    experiment.fit(0, 'uniform_y')
            output = root / 'runs' / 'rep0' / 'uniform_y'
            self.assertFalse((output / 'COMPLETED.json').exists())
            self.assertTrue((output / 'FAILURE.txt').exists())
            self.assertTrue((output / 'FAILED_STEP.npz').exists())
            with np.load(output / 'FAILED_STEP.npz') as failed:
                self.assertEqual(int(failed['step']), 1)
                np.testing.assert_array_equal(failed['previous_parameters'], initial)
                for key in ['candidate_parameters', 'gradient', 'first_moments', 'second_moments']:
                    self.assertTrue(np.isnan(failed[key]).all(), key)
                self.assertTrue(np.isnan(failed['loss']))
            manifest = capture.verify_archive(output / 'output.zip')
            self.assertIn('FAILED_STEP.npz', [item['path'] for item in manifest['files']])

    def test_prior_capture_is_not_enough_when_fit_is_incomplete(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            d = root / 'runs' / 'rep0' / CONDITIONS[0]
            d.mkdir(parents=True)
            capture.dump(d / 'STARTED.json', {'status': 'INCOMPLETE_UNLESS_COMPLETED_FILE_EXISTS'})
            seal_fixture(d)
            with patch.object(experiment, 'ROOT', root):
                with self.assertRaises((ValueError, FileNotFoundError)):
                    experiment.prior_outputs(CFG, BINDING, 0, 1)

    def test_valid_capture_with_wrong_condition_identity_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            complete_fixture(root, 0, 'uniform_y', metadata={'condition': 'uniform_B'})
            with patch.object(experiment, 'ROOT', root):
                with self.assertRaises(ValueError):
                    experiment.prior_outputs(CFG, BINDING, 0, 1)
            with patch.object(analyze, 'ROOT', root), patch.object(analyze, 'check_sources', return_value=(CFG, BINDING)), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(ValueError):
                    analyze.main()

    def test_analysis_rejects_different_input_hashes_within_replica(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for rep in range(4):
                for condition in CONDITIONS:
                    overrides = {'input_archive_sha256': 'f' * 64} if rep == 0 and condition == 'learned_y' else None
                    complete_fixture(root, rep, condition, metadata=overrides)
            with patch.object(analyze, 'ROOT', root), patch.object(analyze, 'check_sources', return_value=(CFG, BINDING)), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(ValueError):
                    analyze.main()

    def test_analysis_rejects_nonmatching_paired_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for rep in range(4):
                for condition in CONDITIONS:
                    complete_fixture(root, rep, condition, alter_targets=(rep == 0 and condition == 'learned_y'))
            with patch.object(analyze, 'ROOT', root), patch.object(analyze, 'check_sources', return_value=(CFG, BINDING)), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(ValueError):
                    analyze.main()

    def test_analysis_rejects_unsealed_local_payload_mutation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for rep in range(4):
                for condition in CONDITIONS:
                    complete_fixture(root, rep, condition)
            d = root / 'runs' / 'rep0' / CONDITIONS[0]
            summary = json.loads((d / 'summary.json').read_text())
            summary['32']['model']['kl_B']['all']['mean'] = 123.
            (d / 'summary.json').write_text(json.dumps(summary))
            with patch.object(analyze, 'ROOT', root), patch.object(analyze, 'check_sources', return_value=(CFG, BINDING)), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(ValueError):
                    analyze.main()

    def test_preflight_failure_leaves_analysis_retry_possible(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(analyze, 'ROOT', root), patch.object(analyze, 'check_sources', return_value=(CFG, BINDING)):
                with self.assertRaises(FileNotFoundError):
                    analyze.main()
            self.assertFalse((root / 'analysis').exists())

    def test_all_fixed_cells_and_paired_metrics_are_retained(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for rep in range(4):
                for condition in CONDITIONS:
                    complete_fixture(root, rep, condition)
            with patch.object(analyze, 'ROOT', root), patch.object(analyze, 'check_sources', return_value=(CFG, BINDING)), contextlib.redirect_stdout(io.StringIO()):
                analyze.main()
            results = json.loads((root / 'analysis' / 'all_results.json').read_text())
            self.assertEqual(len(results['cells']), 16)
            self.assertEqual(len(results['paired_per_example']), 48)
            self.assertEqual(len(results['output_capture_receipts']), 16)
            self.assertEqual(len(results['baselines']), 12)
            with np.load(root / 'runs' / 'rep0' / 'learned_y' / 'evaluation_M32.npz') as a, np.load(root / 'runs' / 'rep0' / 'uniform_y' / 'evaluation_M32.npz') as b:
                expected = a['model_kl_B'] - b['model_kl_B']
                row = results['paired_per_example']['rep0_M32_learned_y_minus_uniform_y']['kl_B']
                self.assertAlmostEqual(row['all']['mean'], expected.mean(), places=15)
                self.assertAlmostEqual(row['all']['mc_se'], expected.std(ddof=1) / 2, places=15)
                self.assertEqual(row['rare_J_le_3']['n'], 2)
            for pool in ['uniform', 'learned']:
                n = np.array(results['primary_replicate_means'][pool + '_y'])
                t = np.array(results['primary_replicate_means'][pool + '_B'])
                self.assertAlmostEqual(results['screening'][pool]['median_paired_natural_minus_teacher'], np.median(n-t))
            capture.verify_archive(root / 'analysis' / 'analysis.zip')

    def test_screen_boundary_and_se_semantics(self):
        s = analyze.screening([.02, .02, .02, .03], [.01, .01, .01, .02], .02, .01000000001)
        self.assertTrue(s['passes_descriptive_screen'])
        s = analyze.screening([.02, .02, .03, .03], [.02]*4, .02, .01)
        self.assertFalse(s['passes_descriptive_screen'])
        self.assertEqual(experiment.summarize([]), {'n': 0, 'mean': None, 'mc_se': None})
        self.assertEqual(experiment.summarize([.5]), {'n': 1, 'mean': .5, 'mc_se': None})
        with self.assertRaises(ValueError):
            analyze.screening([.01]*3, [.01]*3, .02, .01)


if __name__ == '__main__':
    unittest.main(verbosity=2)
