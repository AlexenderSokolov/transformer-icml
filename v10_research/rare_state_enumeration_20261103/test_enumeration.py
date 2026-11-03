import itertools
import unittest
try:
    import enumerate_rare as e
except ModuleNotFoundError:
    e = None

class EnumerationTest(unittest.TestCase):
    def test_module_exists(self):
        self.assertIsNotNone(e, 'enumerator must exist')

    def test_small_horizons_match_brute_force(self):
        for m in (2, 4, 6, 8):
            expected = set()
            for bits in itertools.product((0, 1), repeat=m + 2):
                row = e.literal(bits)
                if row['J'] <= 3:
                    expected.add(tuple(row[k] for k in ('a0', 'a1', 'b0', 'b1', 'U')))
            self.assertEqual(expected, set(e.enumerate_states(m, 3)))

    def test_witnesses_literal_match_and_split(self):
        rows = e.build_rows()
        self.assertEqual(len(rows), 128)
        for row in rows:
            observed = e.literal(tuple(map(int, row['word'])))
            for k in ('a0', 'a1', 'b0', 'b1', 'J', 'C', 'D', 'U'):
                self.assertEqual(row[k], observed[k])
            self.assertEqual(row['split'], e.split(row['J'], row['C'], row['D'], row['U']))
        self.assertEqual(len({(r['J'],r['C'],r['D'],r['U']) for r in rows}),108)

if __name__ == '__main__':
    unittest.main()
