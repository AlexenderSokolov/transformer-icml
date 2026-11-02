# SC003 author handoff

## Useful result

For binary full-history source corruption with final pair preserved, all M>=64, beta in[0,1], 0<=k<=M and arbitrary starts:

    max(M^-1/2,k/M)/96 <= R_stat <= R_all
      <= min(1,2^17 M^-1/2+2^19 F),
    F=(k/M)[1+ln(1+1/(k max(sqrt(beta),1/M)))], k>=1; F0=0.

Estimator is new, deterministic, beta-blind and k-aware. Fixed designated exits: 00/01→1 and10/11→0. For k>=1 use (C'_exit−6k)_+/(J'+6k+2), with complementary other bit; k0 ordinary clean add-one. No unknown probability input, quantized-bank cut, or imported zero-purity claim. Finite rational output and conservative linear-in-M/logarithmic-word count budget are in theorem §5.

## Proof mechanism and exact scope

Histogram discrepancy ≤6k makes estimator a lower envelope of clean exit empirical mass. The new pathwise loss reduction charges twice the clean empirical error plus min(q_true,(24k+2)/(J+2)). BIF001's ALL-start true-exit occupation handles full support at beta>=M^-2; BAI003 v2 handles both absorbing diagonal singleton-support cases; universal occupation handles beta<M^-2 without support assumptions. Support classification and symbol-exchange orientation are explicit.

Only stationary IID clean/corruption lower floors are proven. Matching logarithmic binary source-corruption lower remains OPEN. SC002's three-symbol rare IID suffix cannot be transplanted into a binary active Markov core. All precision lower theorems remain interface-specific. Fixed positive beta yields matching order with beta-dependent constants, but moving-beta regimes may have a logarithmic gap.

## Artifacts and review state

- SC003_theorem.md: complete author proof, frozen sources unchanged.
- SC003_diagnostics.py/json: PASS;20,184 exact path/edit cases,48 kernel/start/budget scenarios,180 scalar checks.
- SC003_algebra_independent_checks.py/json: separate subreview PASS;58,185 exact rational row cases and79,768 whole-word corruption cases.
- SC003_source_bindings.json: source/receipt hashes, all four accepted proof hashes checked against receipts.

The independent subreview checked algebra and all four orientations, not the complete composed theorem. Root requested to obtain fresh full-proof independent review before acceptance. No review PASS is a formal verification or external peer-review claim. No frozen file, publication, contact, purchase or environment restart was made.
