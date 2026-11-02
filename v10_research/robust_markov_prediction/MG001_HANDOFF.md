# General-Markov robust packing handoff

## Result first
MG001 closes the general unknown homogeneous second-order, arbitrary-initialization, actual-terminal upper. For fixed K,R>=2, a K^3 triple bank, coordinate companding and R-coordinate robust scalar packing achieve O_(K,R,c)(M^-1/2) risk with a sufficient internal cut capacity Q^R >= constant sqrt(M), D=RK^3 exposed coordinates and finite exact rational post-cut probabilities. Complete finite approximation and a c/Q one-shot pre-cut fault are both covered. At the minimal sufficient dyadic Q, bounded-primitive depth is Theta(log M) in the explicitly common bounded-influence/dense-mask/local-table family.

The main new inequality is

risk <= 2^13 Hstat + 8K^(5/2) epsilon + Psi(K^5(4epsilon^2+2epsilon/chi)),

where epsilon is compander-space reconstruction error and chi≈log M. It is proved by a symmetric inverse estimate and reconstructed add-one normalization, then unconditional terminal occupation. It handles positive reconstructed mass at true zero coordinates. No IID upper is transplanted into the general class.

## Evidence and state
- MG001_theorem.md: full proof, exact interface, geometry dependency, composed finite certificate, resource ledger and necessary-bound gap.
- MG001_independent_review.md: independent PASS plus root-requested delta review; final theorem hash c4f114bb7510f3dd5ead7461d9ebead092e2abe103fc92f96e3af9fbd4ac6623.
- MG001_diagnostics.json: 49,565 exact author checks across symmetric inverse, robust packing, add-one rows, actual-terminal counts and deterministic occupation.
- MG001_independent_checks.json: 41,891 independent exact checks, including nontrivial stochastic arbitrary-start occupation up to M=64.
- MG001_issues_and_resolution.md and preclarification/: real ambiguity/accounting corrections preserved rather than overwritten without record.
- MG001_source_bindings.json: source hash bindings. Root acceptance is separate from independent review.

## Critical boundaries
Q is the internal cut resolution, NOT the final probability-grid resolution. Exact rational finite output is essential; forcing final output onto Q restores O(1/Q) loss. The chosen comparison-family front end is a paid finite local TABLE, not a sparse singleton attention layer. Full bank conversion between generic encoder word w and decoder word b is charged with both banks live. Exposed dimension is RK^3; the universal alphabet necessity has exponent RK^3, not the construction's scalar exponent R. No optimal K dependence, minimum P, efficient decoder, internal fault robustness, learning theorem or novelty certification.

## Next extension already executed
MG002_partial_capacity_extension.md uses accepted GN001's no-plateau scalar geometry, now separately reviewed, to reduce sufficient depth to O(loglog M+log_+(sqrt(M)/Q)) for all dyadic Q at a sufficiently large scalar capacity constant. MG001 is preserved unchanged as the simpler fully dyadic RG construction. Its general statistical transfer, not GN001's IID sampling argument, supplies the new upper. See MG002-specific review/diagnostics and root receipt for status.

## Useful next scientific choices
The dimensional capacity gap remains genuine: D=RK^3 is sufficient, while only Q^D≥constant sqrt(M) is universally necessary. A future upper using Markov-flow constraints or row-selective information must retain actual-terminal causality and paid exact-boundary restrictions; it cannot simply query counts after the cut. Another distinct question is optimal general-Markov depth at Q near/above sqrt(M), where the current upper retains a compander term and only scoped predecessor lower results are available. Neither gap is claimed solved here.
