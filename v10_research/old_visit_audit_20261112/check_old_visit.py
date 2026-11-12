#!/usr/bin/env python3
"""Exact finite diagnostics, not a proof or a manuscript-wide validation.

Run from any directory with Python 3; standard library only. No files written.
The transition law is propagated directly over (state, departures, old visits).
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json
import sys

if not __debug__:
    raise RuntimeError("Assertions must be enabled; do not use python -O")

MATRICES = [
    [[F(1), F(0)], [F(0), F(1)]],
    [[F(0), F(1)], [F(1), F(0)]],
    [[F(1), F(0)], [F(1, 3), F(2, 3)]],
    [[F(3, 4), F(1, 4)], [F(2, 3), F(1, 3)]],
    [[F(1, 2), F(1, 2), F(0)],
     [F(0), F(1, 3), F(2, 3)],
     [F(1, 4), F(0), F(3, 4)]],
]


def law(P, start, target, horizon, suffix):
    dist = {(start, 0, 0): F(1)}
    for i in range(horizon):
        nxt = defaultdict(F)
        for (state, count, old), mass in dist.items():
            for successor, probability in enumerate(P[state]):
                if probability:
                    key = (successor, count + (state == target),
                           old + (state == target and i < horizon - suffix))
                    nxt[key] += mass * probability
        dist = nxt
    assert sum(dist.values()) == 1
    return dist


def endpoint_inverse(dist, target, require_old=False):
    return sum((p / F(j + 1) for (state, j, old), p in dist.items()
                if state == target and (not require_old or old >= 1)), F(0))


def first_hits(P, start, target, horizon):
    live = {start: F(1)}
    hits = {}
    for t in range(1, horizon + 1):
        nxt = defaultdict(F)
        for state, mass in live.items():
            for successor, probability in enumerate(P[state]):
                nxt[successor] += mass * probability
        hits[t] = nxt.pop(target, F(0))
        live = nxt
    return hits


def main():
    gates = convolutions = 0
    for P in MATRICES:
        d = len(P)
        assert all(sum(row) == 1 for row in P)
        for M in range(2, 11):
            for m in range(M // 2 + 1):
                for u, v in product(range(d), repeat=2):
                    dist = law(P, v, u, M, m)
                    old = endpoint_inverse(dist, u, True)
                    if v == u:
                        assert old == endpoint_inverse(dist, u)
                    else:
                        hits = first_hits(P, v, u, M)
                        rhs = sum((hits[t] * endpoint_inverse(
                            law(P, u, u, M - t, 0), u)
                            for t in range(1, M - m)), F(0))
                        assert old == rhs, (P, M, m, u, v, old, rhs)
                    convolutions += 1
                    bound = F(3 * d, M) + F(2 * d * d, M) * sum(
                        (F(1, s) for s in range(m + 1, (M - 1) // 2 + 1)), F(0))
                    for c in [F(1, 1024), F(1, 2), F(1), F(2)]:
                        value = sum((p / F(j + 1) for (state, j, old), p in dist.items()
                                     if state == u and old >= c * j), F(0))
                        assert value <= bound, (P, M, m, u, v, c, value, bound)
                        gates += 1
    print(json.dumps({"status": "PASS", "matrices": len(MATRICES),
                      "horizons": [2, 10], "gate_checks": gates,
                      "convolution_or_start_at_target_checks": convolutions,
                      "arithmetic": "fractions.Fraction; exact rational",
                      "scope": "Finite diagnostics only; not a universal proof"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
