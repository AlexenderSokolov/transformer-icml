"""Independent reverse recurrence plus literal-oracle verification, no fitting."""
import hashlib
import json
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT/'v10_research/readout_conditioning_calibration_20261103'))
import numpy as np
import calibration


def reverse_states(m=64, cap=3):
    # Work backward from the required terminal pair; no witness reuse.
    result = set()
    for terminal in range(4):
        frontier = {(terminal, (0, 0, 0, 0))}
        for i in range(m-1, -1, -1):
            prior = set()
            for current, counts in frontier:
                appended = current & 1
                for leading in (0, 1):
                    predecessor = 2*leading + (current >> 1)
                    c = list(counts)
                    if predecessor == terminal:
                        c[(0 if i < m//2 else 2)+appended] += 1
                    if sum(c) <= cap:
                        prior.add((predecessor, tuple(c)))
            frontier = prior
        result |= {(*counts, terminal) for _, counts in frontier}
    return result


def main():
    path = HERE/'rare_states.json'
    payload = json.loads(path.read_text())
    rows = payload['rows']
    assert payload['M'] == 64 and payload['max_J'] == 3
    expected = reverse_states()
    actual = {(r['a0'],r['a1'],r['b0'],r['b1'],r['U']) for r in rows}
    assert len(actual) == len(rows) and expected == actual
    assert len(actual) == 128
    words = np.array([[int(c) for c in r['word']] for r in rows], dtype=np.int8)
    assert words.shape == (128, 66)
    independent = calibration.literal_statistics(words)
    x = calibration.features(words, 'half_count_scaled') * calibration.SCALE
    groups = {'train':set(), 'holdout':set()}
    collisions = set()
    for s in map(calibration.literal_statistics, [calibration.collision_words()]):
        for j,c,d,q,w in zip(s['J'],s['C'],s['D'],s['Q'],calibration.collision_words()):
            collisions.add((int(j),int(c),int(d),int(2*w[-2]+w[-1])))
    assert collisions == {tuple(g) for g in payload['collision_groups']}
    for i, r in enumerate(rows):
        j,c,d,u = r['J'],r['C'],r['D'],r['U']
        assert (j,c,d) == tuple(int(independent[k][i]) for k in ('J','C','D'))
        assert u == int(2*words[i,-2]+words[i,-1])
        a0,a1,b0,b1 = (r[k] for k in ('a0','a1','b0','b1'))
        assert np.array_equal(x[i,:8], [a0+b0,a1+b1,a0,a1,b0,b1,u//2,u%2])
        q = Fraction(r['Q_numerator'],r['Q_denominator'])
        assert abs(float(q)-independent['Q'][i]) < 1e-15
        data = f'v10-rare-split-20261103:{j},{c},{d},{u}'.encode('ascii')
        h = int.from_bytes(hashlib.sha256(data).digest(),'big')
        split = 'holdout' if h % 5 == 0 and (j,c,d,u) not in collisions else 'train'
        assert r['split'] == split
        groups[split].add((j,c,d,u))
    assert not (groups['train'] & groups['holdout'])
    assert collisions <= groups['train']
    assert path.read_bytes() == subprocess.check_output([sys.executable,str(HERE/'enumerate_rare.py')])
    result = {'reverse_dp_exact_set_match':True,'literal_calibration_oracle_witnesses':len(rows),
              'replay_byte_identical':True, 'feature_vectors':len(actual),
              'groups':{k:len(v) for k,v in groups.items()},
              'feature_split':dict(Counter(r['split'] for r in rows)),
              'holdout_by_J_Dzero':dict(sorted(Counter(f"J={r['J']}, D={'0' if r['D']==0 else '>0'}" for r in rows if r['split']=='holdout').items())),
              'collision_groups':sorted(map(list,collisions)),
              'json_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
