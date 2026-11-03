# Fixed collision words on the retained trained half checkpoint

3 November 2026. This targeted, deterministic numerical check evaluates two fixed words, not a robustness sweep, global maximization, or production guarantee. It loads the original smoke run's `half_edit_200.npz` (SHA-256 `bc95b1e2f5dc4361224a4b52b740263bdda74242a81eaa52e49584020a22b848`), verifies it against `smoke_v1/ARTIFACT_HASHES.json`, and assigns the saved arrays directly to a `pilot.Model` allocated with `__new__`. Its random-initializing constructor is replaced by a function that raises. No random sampling, random initialization, training, or modification of prior stages was performed.

## Inputs and executable layout

At M=1025, both 1027-bit int8 words are all ones except A has zeros at zero-based indices {515,518}, and B at {519,522}. A direct literal-triple check verifies their same protected endpoint and four-counter bank (1021,1019,512,512), and four editable differences. These are the fixed words of the earlier float-bank audit, so that A and B are both legal from clean A at k=4. The clean target is the pilot's B(A), exactly 340/341 as a real rational and `0x1.fe7f9fe7f9fe8p-1` when computed in this floating run.

We evaluate AB, BA, AA and BB as two-row C-contiguous batches, and A and B as singleton C-contiguous batches. For the identical shapes tested here the independent implementation matches `pilot.Model.forward(...,cache=True)` **bitwise** for all six rails plus side inputs x, hidden tanh values, sigmoid values and final q. It constructs selected triples by a separate literal Python loop and computes the fixed half coefficients directly, but deliberately uses the same NumPy einsum, matrix multiply, tanh and exp primitives in the same order as the pilot to match its executable semantics. This is an independent reimplementation check, not an independent backend or formal certification. The constructed model is populated with the saved arrays, not newly generated weights.

## Observed results

In AB, uniform successor-1 rail for A is `0x1.fd00bfd00bfd6p-1`, and for B it is `0x1.fd00bfd00bfd7p-1`, one ULP apart. The split matches the original fixed-shape collision and follows the words in BA. **For this trained checkpoint and these two-row batches, the final logits, predictions and conditional CE happen to be bitwise equal between the two words:**

- Logit: `0x1.3a0db665792cbp+2` (approximately 4.907086943717057).
- Prediction q: `0x1.fc3dd84f48330p-1` (approximately 0.9926593395976848).
- CE against B(A): `0x1.647a2c4900137p-6` (approximately 0.021757643935417206).

AA and BB give the same readout values as AB and BA. In singleton calls, A and B each have logit `0x1.3a0db665792ddp+2`, 18 binary64 ULPs higher than the two-row logit, while their q and CE remain bitwise identical to the two-row values. Thus batch layout changes this observed logit even though the q/CE comparison for this checkpoint and these words does not change. The outputs cannot be generalized to other words, checkpoints, layouts, horizons, weights, or backends. M=1025 is the constructed collision horizon, not one of the pilot training horizons.

`trained_results.json` contains every input feature, preactivation and hidden value as binary64 hex, plus logits, q, target, CE, batch shapes/strides and errors. It also binds all source files by SHA-256. `check_trained.log` records full NumPy build and runtime/BLAS details, fixed thread settings and a concise output for each batch.

## Comparison with the conditional bound

The prior `float_readout_bound_20261103/REPORT.md` obtains, for this checkpoint and M=1025, a **conditional** logit bound R <= 1.1746381927788e-12 + 9.7440180599953 tau_h, where tau_h is a uniform tanh implementation error. That result requires the stated pooling/affine arithmetic model and other premises; tau_h and other implementation errors remain unverified. It is not a certified actual-backend bound.

As a diagnostic, the new script evaluates the common exact-rational bank inputs and exactly represented saved binary64 weights with mpmath at 100 decimal digits, treating tanh, sigmoid and logarithms as high-precision approximations to the ideal real functions. The approximate ideal logit is 4.907086943717055948674484312283..., and observed absolute logit differences from that high-precision value are about 1.0551e-15 (two-row) and 1.7043e-14 (singleton), smaller than the tau_h=0 diagnostic component. Agreement on these few computations does not prove that component is a valid bound for NumPy, establish any required uniform transcendental-error premises, certify an exact real value, or certify a global argmax. Target, q and CE approximations and their observed differences are included in the JSON.

## Reproduce

From repository root, run:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python v10_research/trained_half_float_check_20261103/check_trained.py`

Python 3.12.14, NumPy 2.3.5, mpmath 1.3.0 and scipy-OpenBLAS 0.3.30 were used; `MKL_NUM_THREADS` was unset. This script writes only its own directory's `trained_results.json`. Record byte-level hashes and repeat in a separate directory when preserving the original run. `SHA256SUMS` binds this report, script, retained output and log.
