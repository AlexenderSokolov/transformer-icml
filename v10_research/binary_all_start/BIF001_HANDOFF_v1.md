# BIF001 handoff

New standalone post-freeze research. Author candidate, not root accepted.

Main proof: `BIF001_binary_all_initializations_frontier_v1.md`.
Proof SHA-256: `35c6cb3b5c882c9e70dad68dbc8492c08e65ba49f532da84597e5e1e303467f0`.

## Result

For binary all-state D2(beta) sources, arbitrary initial pair laws, M>=64, integer kappa>=1, dyadic Q>=16, the unchanged SB001 predictor satisfies

`risk <= min(1, 2^17/sqrt(M) + 3/Q + 2^17 [1+ln(1+kappa Q/(M max(sqrt(beta),1/M)))]/(kappa Q))`.

The same stationary lower yields the exact one-block frontier for BOTH initializations, with common upper constant 262147. BC001's exact historywise uniform-histogram labels transfer the kappa=1 upper to its distinct bounded fixed-depth causal finite-evaluator family, also for both initializations. Joint product/grid thresholds and the beta=1/M binary versus K>=3 contrast upgrade to both initializations. This is analysis of existing paid programs, not a new implementation or runtime port.

## Essential proof safeguards

- Use true row exits q=(a,b,e,t), not BU001's stationary unit crossing caps. Reprove the deterministic floor step for these exits.
- Accepted diagonal components sum to 8336 A/M G. Crossing reduction doubles this to 16672 A/M G, with failure <=3/sqrt(M); common envelope uses 4/sqrt(M).
- Short suffixes may fail beta*n^2>=1: BAI004's max(sqrt(beta),1/n) only improves its logarithm; BOD001 imposes no strong-beta horizon restriction.
- Positive-beta support is either full or singleton absorbing. BAI003 covers the latter from arbitrary unsupported starts. Weak beta, including zero, uses SB001 directly.
- Causal upper transfer relies on EXACT bank equality, not an approximation bound. Its FA encoder and SB decoder suffix have separate summed costs; singleton heads are not smuggled into the causal family.

## Evidence

- Author deterministic boundary diagnostics: 14,640 checks PASS.
- Fresh reviewer diagnostics: 163,846 checks PASS, independently rerun by author; scalar lower domains and cutoff/constant checks, exact rational floor inequalities, exact integer common-weight/nested-floor labels, and finite all-start count DP.
- `BIF001_source_bindings_v1.json` verifies all eight direct imported proof hashes against their root receipts.
- Fresh full-manuscript independent review PASS: `BIF001_independent_review_v1.md`, with exact proof/source/test hashes in `BIF001_review_source_bindings_v1.json`. Author read the entire review. Root disposition remains separate.

No accepted source, frozen bundle, paper_v3, or stage-5 file was edited. No external publication, upload or contact occurred.
