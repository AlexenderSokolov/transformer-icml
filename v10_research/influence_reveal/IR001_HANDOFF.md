# IR001 handoff

New files only in `v10_research/influence_reveal/`; earlier/frozen files unchanged.

## Deliverable

`IR001_theorem.md`: IID minimax floor `c(D,b,E)/(QB)` for any fixed-dimensional final Q-grid bank with deterministic branchwise summed single-bit replacement majorants at most B, a fixed finite boundary side label, common source-independent public randomness, and uniform ideal/actual precut discrepancy at most E/Q. Explicit constants and all small-history endpoints included. No local-ratio or denominator structure is required.

Key new step: reveal the union of each branch/coordinate's top `ceil(100 D 2^b Q²B²)` influence indices, together with boundary bits. All remaining majorants are at most B/m. Conditional Efron–Stein and the product derivative identity replace UI001's maximizing-pattern/denominator argument. The oracle's truncated Bernoulli posterior has width O(1/(QB)) and peak density O(QB), including boundary modes; the good final alphabet is O_(D,b,E)(1).

The causal-attention application uses the row sum of actual nonnegative matrix-entry majorants, not logarithmic envelopes or factorial square-sum constants. This includes early coins and yields B_l<=C_depth^l with fixed primitive constants. Thus at M comparable to Q^(2J), fixed J>=2 and fixed E, statistical-order IID risk requires depth Omega(log Q). FG001's separately reviewed candidate upper has depth O(log Q) on powers-of-two Q. This pairing is restricted to the shared fixed-primitive/interface scope; it is not an all-Q exponential-base risk equivalence or a Markov upper result.

## Evidence and limits

- `IR001_diagnostics.py/json`: finite nonlinear conditional-table, posterior boundary, row-sum, and floor-box checks. PASS. Not formal verification or emitted-network execution.
- `IR001_source_bindings.json`: SHA256 source bindings.
- Fresh independent mathematical/model review **PASS** from a separate agent; see `IR001_independent_review.md` and independent checks (608 exact conditional cases, 31,336 posterior segment cases, 936 exact row-sum/locality cases, 10,000 grid-tube cases). Reviewed theorem SHA256: `963e3f743c474f3f4c29fcb2f4aa9dfe1283ac82e0821b18df6a99223b09fffe`. The theorem's original pending-review header is historical; the separately bound report supplies the current review status without modifying the reviewed bytes.
- Root acceptance is a separate decision; author does not self-accept.
- No external publication/upload, novelty claim, or modification to accepted source artifacts.
