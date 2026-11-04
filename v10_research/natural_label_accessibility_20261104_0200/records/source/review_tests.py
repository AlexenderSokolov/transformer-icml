"""Independent review checks. Deterministic fixtures only; no sampling or fits."""
import hashlib
import itertools
import json
import math
from pathlib import Path
import tempfile
import unittest

import numpy as np
import core
import capture


class IndependentScientificReviewTests(unittest.TestCase):
    def test_posterior_by_independent_product_integrals(self):
        # An 8-node Gauss rule integrates degree <=15 exactly on [0,1].
        # This is independent of the factorial word-mass formula in test_core.
        x, weights = np.polynomial.legendre.leggauss(8)
        x = (x + 1.) / 2.
        weights = weights / 2.
        for length in (3, 4, 5, 6, 7):
            words = np.array(list(itertools.product((0, 1), repeat=length)), dtype=np.int8)
            H, U, J, C, B = core.statistics(words)
            total_mass = 0.
            for i, word in enumerate(words):
                counts = np.zeros((4, 2), dtype=int)
                for a, b, c in zip(word[:-2], word[1:-1], word[2:]):
                    counts[2 * int(a) + int(b), int(c)] += 1
                row_integrals = []
                for n0, n1 in counts:
                    row_integrals.append(np.dot(weights, x**n1 * (1-x)**n0))
                total_mass += math.prod(row_integrals) / 4.
                n0, n1 = counts[U[i]]
                posterior_mean = np.dot(weights, x**(n1+1) * (1-x)**n0) / row_integrals[U[i]]
                self.assertAlmostEqual(posterior_mean, B[i], places=13)
                # Conditional source-KL differences depend on E[p|W], not p=B.
                q, r = .17, .71
                integrand = x * np.log(r/q) + (1-x) * np.log((1-r)/(1-q))
                conditional_gap = np.dot(weights, integrand * x**n1 * (1-x)**n0) / row_integrals[U[i]]
                clean_gap = core.kl(np.array([B[i]]), np.array([q]))[0] - core.kl(np.array([B[i]]), np.array([r]))[0]
                self.assertAlmostEqual(conditional_gap, clean_gap, places=13)
            self.assertAlmostEqual(total_mass, 1., places=13)

    def test_gradient_all_queries_and_score_gauges(self):
        H = np.array([[4, 0, 1, 1, 1, 0, 0, 1], [0, 3, 0, 1, 1, 1, 2, 0],
                      [1, 1, 0, 0, 2, 2, 0, 2], [0, 0, 1, 1, 1, 2, 1, 2]], dtype=float)
        U = np.arange(4)
        target = np.array([.13, .29, .61, .83])
        p = .08 * np.cos(np.arange(core.PARAM_COUNT) * .17)
        _, g = core.loss_grad(p, H, U, 8, target, True)
        scores_grad = core.unpack(g)[0]
        np.testing.assert_allclose(scores_grad.sum(axis=2), 0., atol=1e-16)
        for j in range(64):
            up, down = p.copy(), p.copy()
            up[j] += 1e-6
            down[j] -= 1e-6
            fd = (core.loss_grad(up, H, U, 8, target, True)[0] - core.loss_grad(down, H, U, 8, target, True)[0]) / 2e-6
            self.assertLess(abs(fd - g[j]), 2e-8, j)
        shift = p.copy()
        core.unpack(shift)[0][:] += np.arange(8).reshape(2, 4, 1) - 4
        np.testing.assert_allclose(core.predict(p, H, U, 8, True), core.predict(shift, H, U, 8, True), atol=2e-16)
        # Aggregate every possible 4-label vector with its conditional mass.
        expected = np.zeros_like(g)
        for bits in itertools.product((0., 1.), repeat=4):
            y = np.array(bits)
            probability = np.prod(np.where(y, target, 1-target))
            expected += probability * core.loss_grad(p, H, U, 8, y, True)[1]
        np.testing.assert_allclose(g, expected, atol=1e-16)

    def test_input_labels_cannot_change_visible_words(self):
        sources = np.array([[.1, .3, .7, .9], [.7, .9, .1, .3]])
        starts = np.array([0, 3])
        draws = np.tile(np.array([.05, .45, .25, .75, .65]), (2, 1))
        a, b = draws.copy(), draws.copy()
        a[:, -1] = 0.
        b[:, -1] = np.nextafter(1., 0.)
        wa, ya = core.simulate_from_draws(sources, starts, a)
        wb, yb = core.simulate_from_draws(sources, starts, b)
        np.testing.assert_array_equal(wa, wb)
        np.testing.assert_array_equal(ya, np.ones(2))
        np.testing.assert_array_equal(yb, np.zeros(2))
        for aa, bb in zip(core.statistics(wa), core.statistics(wb)):
            np.testing.assert_array_equal(aa, bb)

    def test_extreme_absent_score_keeps_pool_defined(self):
        p = np.zeros(core.PARAM_COUNT)
        core.unpack(p)[0][:, :, 7] = 1000.
        H = np.array([[5, 1, 2, 0, 0, 0, 0, 0]])
        U = np.array([0])
        with np.errstate(all='ignore'):
            actual = core.pooling(p, H, U, True)
        np.testing.assert_allclose(actual[0, 0], H[0] / 8., atol=1e-15)
        np.testing.assert_allclose(actual[0, 1], H[0] / 8., atol=1e-15)


class IndependentCaptureReviewTests(unittest.TestCase):
    def test_correct_manifest_hash_does_not_allow_wrong_member_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'core.py').write_text('# deterministic fixture\n')
            manifest = {'files': [{'path': 'core.py', 'sha256': 'f' * 64}]}
            (root / 'SOURCE_MANIFEST.json').write_text(json.dumps(manifest) + '\n')
            binding = capture.sha(root / 'SOURCE_MANIFEST.json')
            (root / 'SCIENTIFIC_REVIEW.json').write_text(json.dumps({'status': 'PASS', 'source_manifest_sha256': binding}))
            with self.assertRaises(ValueError):
                capture.make_archive(root, ['core.py', 'SOURCE_MANIFEST.json', 'SCIENTIFIC_REVIEW.json'], root / 'source.zip', 'source', binding)

    def test_source_declared_hash_must_hash_source_manifest_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'core.py').write_text('# deterministic fixture\n')
            (root / 'SOURCE_MANIFEST.json').write_text(json.dumps({'files': []}) + '\n')
            wrong = 'a' * 64
            (root / 'SCIENTIFIC_REVIEW.json').write_text(json.dumps({'status': 'PASS', 'source_manifest_sha256': wrong}))
            with self.assertRaises(ValueError):
                capture.make_archive(root, ['core.py', 'SOURCE_MANIFEST.json', 'SCIENTIFIC_REVIEW.json'], root / 'source.zip', 'source', wrong)


if __name__ == '__main__':
    unittest.main(verbosity=2)
