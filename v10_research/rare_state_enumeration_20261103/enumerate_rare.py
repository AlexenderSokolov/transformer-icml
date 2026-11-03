"""Enumerate all feasible J<=3 fixed-half feature vectors at M=64.

Output JSON to stdout.  No random sampling, fitting, or model inspection.
"""
import hashlib
import json
from fractions import Fraction

M = 64
CAP = 3
PREFIX = 'v10-rare-split-20261103:'


def literal(bits):
    m = len(bits)-2
    assert m % 2 == 0 and all(b in (0, 1) for b in bits)
    u = 2*bits[-2]+bits[-1]
    counts = [0, 0, 0, 0]
    for i in range(m):
        if 2*bits[i]+bits[i+1] == u:
            counts[2*(i >= m//2) + bits[i+2]] += 1
    a0, a1, b0, b1 = counts
    j, c, d = sum(counts), a1+b1, a0+a1
    A = Fraction(c, j) if j and 512*d >= j else Fraction(bits[-2], 1)
    q = Fraction(1, 8) + Fraction(3, 4)*A
    return dict(a0=a0, a1=a1, b0=b0, b1=b1, J=j, C=c, D=d, U=u,
                Q_numerator=q.numerator, Q_denominator=q.denominator)


def collision_groups():
    words = []
    for r in (8, 54):
        w = [0]+[1]*r+[0, 0]+[1]*(62-r)+[0]
        words.append(w)
    words += [[1-b for b in w] for w in words]
    return {(s['J'], s['C'], s['D'], s['U']) for s in map(literal, words)}


def split(j, c, d, u):
    group = (j, c, d, u)
    data = (PREFIX + ','.join(map(str, group))).encode('ascii')
    holdout = int.from_bytes(hashlib.sha256(data).digest(), 'big') % 5 == 0
    return 'holdout' if holdout and group not in collision_groups() else 'train'


def enumerate_states(m=M, cap=CAP):
    """Map (a0,a1,b0,b1,U) to a representative bit string."""
    assert m % 2 == 0 and m >= 2 and cap >= 0
    out = {}
    for u in range(4):
        # The path integer includes the first pair and every appended bit.
        states = {(pair, 0, 0, 0, 0): pair for pair in range(4)}
        for i in range(m):
            nxt = {}
            for (pair, a0, a1, b0, b1), path in states.items():
                for bit in (0, 1):
                    counts = [a0, a1, b0, b1]
                    if pair == u:
                        counts[2*(i >= m//2)+bit] += 1
                    if sum(counts) <= cap:
                        key = (2*(pair & 1)+bit, *counts)
                        nxt.setdefault(key, (path << 1) | bit)
            states = nxt
        for (pair, a0, a1, b0, b1), path in states.items():
            if pair == u:
                out[(a0, a1, b0, b1, u)] = format(path, f'0{m+2}b')
    return out


def build_rows():
    rows = []
    for (a0, a1, b0, b1, u), word in sorted(enumerate_states().items()):
        row = literal(tuple(map(int, word)))
        assert (row['a0'], row['a1'], row['b0'], row['b1'], row['U']) == (a0, a1, b0, b1, u)
        row['word'] = word
        row['split'] = split(row['J'], row['C'], row['D'], row['U'])
        rows.append(row)
    return rows


if __name__ == '__main__':
    print(json.dumps({'M': M, 'max_J': CAP, 'hash_input': PREFIX+'J,C,D,U',
                      'hash_rule': 'SHA256 integer big-endian mod 5 == 0, except collision groups are train',
                      'collision_groups': sorted(map(list, collision_groups())),
                      'rows': build_rows()}, indent=2, sort_keys=True))
