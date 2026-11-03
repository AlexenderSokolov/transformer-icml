# Sticky transient followed by a three-cycle: exact gate diagnosis

Local supplementary calculation, 2026-11-03. This is a counterexample to one half-prefix gate, **not** an all-predictor lower bound. The latter already follows from prior AB001 as explained in RESULT.md.

Take M>=64, a=1/M, initial pair Y_0=11, and transitions

- 11→11 with probability1-a and 11→10 with probability a;
- 10→00→01→10 deterministically.

Equivalently theta11(0)=a, theta10(0)=theta00(1)=theta01(0)=1. Let tau be the first index with Y_tau=10. Then P(tau=t)=a(1-a)^(t-1), t>=1. Set H=floor(M/2), and let D count departures i=0,...,H-1 in the actual terminal row, J count departures i=0,...,M-1 in that row.

If H<=t<=M-3 and M-t modulo3 is0 or1, the terminal row is respectively10 or00, its first-half count is D=0, its full count J is positive, and its true designated probability q=theta_(ab)(1-a_first) is1. Therefore the half gate `J>0 and 512D>=J` rejects and incurs unit next-symbol TV. Its expected clean risk is at least the exact finite sum

`L_M = (1/M) sum_{t=H}^{M-3} (1-1/M)^(t-1) 1{(M-t) mod3 in {0,1}}`.        (G1)

The range M-3 deliberately removes the two unvisited-terminal-row cases. It is not legitimate to use J>0 automatically when entry is at the very last departures.

There are at least M/4 admissible t for M>=64: the interval length is M-H-2, every complete block of three contributes two, and the crude lower bound is M/3-10/3>=M/4 for M>=40. Every summand before multiplication by1/M is at least `(1-1/M)^(M-1)>=exp(-1)`. Hence

`L_M >=1/(4e)>0.09` for every M>=64.                            (G2)

For M=6n, writing b=1-1/M, the sum has the closed form

`L_(6n) = (a/(1-b^3)) [b^(3n-1)(1-b^(3n)) + b^(3n+1)(1-b^(3n-3))]`.

Thus along these horizons its limit is `(2/3)(exp(-1/2)-exp(-1))`, approximately0.1591008. The same limit holds over all horizons by residue-block Riemann sums, though the uniform finite bound G2 is enough.

## Stationary and all-state status

For a>0 there is a unique stationary pair law, uniform on {00,01,10}, with zero mass at11. The specified initial pair11 is transient and nonstationary. The closed class has period three. From any of its states P² is a point mass, so there are supported target states v with P²(u,v)=0<Pi(v). Consequently **no positive all-state certificate** P²>=beta Pi holds. This is not merely a failure of beta=1/M. Stationary initialization would exclude the delayed departure from11; this particular constant clean-risk mechanism uses the allowed arbitrary initial pair.

## Ordinary empirical prediction succeeds cleanly here

Use the same designated orientation and empirical ratio C/J, with zero when J=0. After entry, every visited cycle row is deterministic and learned exactly. The only nonzero errors are: no exit through M, with loss a; exit at M, whose unvisited terminal row10 has q=1; and exit at M-1, whose unvisited terminal row00 has q=1. Thus for M>=3 its exact expected loss is

`a b^M + a b^(M-1) + a b^(M-2) <=3/M`.

This verifies directly that the gate failure is not a clean-data information obstruction.

## Why the naive cycle-based attack does not prove impossibility

Comparing a late constant-zero suffix to a deterministic period-three suffix requires a number of edits proportional to the suffix length. A strict-k replacement therefore reaches only suffix lengths O(k). With exit hazard of order1/M, that late-entry window has probability O(k/M), giving only the benchmark-scale lower, not a divergent factor. Full-word ordering cannot be discarded by transplanting a count-preserving canonicalization lower. AB001 instead uses many suffix lengths, parameter-scaled sparse random continuations, and a common integration argument; that already accepted full-word construction is what establishes the all-estimator obstruction.
