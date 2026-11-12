# Scalar-position single-public-source alignment

This is the corrected paired-state version reviewed in REVIEW.md. The sqrt2 conversion from two register errors to full paired-state error is charged, with gate contraction budget 2*q1^L. Earlier uncorrected snapshots must not be used.

The actual width14 full-PreLN/ReLU module aligns one publicly configured source index j to its causal future, using one uniform read and O(log N+log(1/eta)) depth. It does not simultaneously recover every predecessor, aggregate transition statistics, or solve next-token prediction. N and j may configure bounded coefficients; scalar positions and O(log N)-bit coefficient descriptions are part of the contract.

Two independent diagnostic replays matched every non-timing field: 105 configurations, 27540 gate/alignment assertions plus intermediate norm assertions. The elapsed_seconds field is excluded. Run `python check.py`; it writes results and a receipt beside the script. Binary64 tests are not adversarial-noise certificates. Precision sufficiency is an analytical tube argument; rounding the initial positional thresholds must be charged separately. Layerwise bounded norms are not a depth-independent total energy bound.

No CI or full-repository verifier was run. Historical inventory entries and 293 undeclared inherited files remain unchanged. The original author receipt is preserved separately from the publication receipt.
