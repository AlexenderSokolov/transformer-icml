# FG001 handoff

2026-11-02. Independent review PASS; no substantive blocker. No frozen preexisting source or delivery file edited. No external publication/upload.

## Established

For binary common-row IID sources, arbitrary initialization, exactly J>=2 bounded Q-grid scalar coordinates plus H-valued history-derived boundary state, arbitrary real decoder output:

- Every encoder, regardless of depth: risk >= max{3/(64 sqrt(M)), 1/[16H(Q+1)^J]}.
- Explicit finite causal folded-mean encoder: risk <=1/(2 sqrt(M))+2/Q^J.
- Width O(J), coefficients <=4, actual primitive depth O(1+(J-1)h), h=log2 Q.
- Finite precision P>=Jh (or the stated larger generic-FA prescription), with log M guards and all resource costs paid. Uniform pre-cut E/Q certificate E=1 follows directly.
- Hence IID-only capacity frontier Theta_(J,H)(max{M^-1/2,Q^-J}) when this depth/capacity is allowed.

This disproves a depth-uniform 1/Q obstruction for all fixed-dimensional bounded-coordinate encoders; it does not change any fixed-depth/prefix theorem. No general-Markov optimality or depth necessity is asserted. Raw labels include Q, so fixed-length label storage is J(h+1), not Jh exactly.

## Evidence

`FG001_theorem.md`: self-contained interval geometry, endpoint-Q handling, exact finite schedule, IID risk, alphabet/statistical lower, paid existence ledger, scope.

`check_fg001.py` / `FG001_diagnostic.json`: 156,118 exact cases, including 5,298 label-Q cases; maximal tested error 197/99 times Q^-J, below 2.

`FG001_independent_review.md` and independent Python/JSON: fresh review; 149,860 rational geometry points, 7,176 finite count/precision cases, 53,820 exact integer fold steps. Diagnostics supplement mathematical proof, not an emitted-network audit.

`FG001_source_bindings.json`: immutable-source hashes and primary Telgarsky triangle-fold attribution. Generic public searches only; no private proof text sent externally.

## Next research boundary

A plausible separate extension is folding each coordinate of the causal triple-histogram bank, allocating J rails per scalar and testing the resulting Q^-J reconstruction error through the accepted ratio/occupation upper. It requires its own complete bank accounting and decoder/output-format check, and is not proved here. The current theorem alone closes the assigned IID counterboundary. Depth necessity remains open and must not be inferred from fixed-depth constants without a uniform-depth argument.
