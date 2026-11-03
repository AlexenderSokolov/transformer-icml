# Independent v2 addendum: arbitrary fixed-length erasure encodings

**PASS, conditional concrete conclusion.** This is a separate review of the newly appended section, not a retroactive extension of the previous source-bound reports.

## Bound source and actual change

Source: `../VISIBLE_ERASURE_COMPARISON_v2.md`, SHA-256 `103b7060910c0bb93f11873b1c2bb686d50666fa649ff843e650ac2580d417ee`.

The full original erasure file is an exact byte prefix of v2. Its actual before-image `../revisions/VISIBLE_ERASURE_COMPARISON.before_anycode_7c5770e9.md` is byte-identical to the original, hash `7c5770e908f31ba90cbab9eef0f5e7eec4d285151879d0f97ea6c36691e690f6`. The supplied `../revisions/VISIBLE_ERASURE_COMPARISON.anycode_v2.diff` was read; the only addition is the fixed-length arbitrary-encoding section. The prior source-bound reviews remain unchanged.

## Independent argument and quantifiers

Fix one admissible encoder and joint estimator before choosing k,theta,K. Its complete noisy message is the constant all-erased string with probability q=epsilon^R independently of every risk-relevant pre-channel variable. On that event a baseline-only rule can simulate the receiver by supplying that constant string, including the receiver's private randomization. Thus each instance's risk is at least q times the induced baseline rule's risk. Taking the common instance supremum, then the infimum over all encoder/receiver pairs, yields Gamma_any,R>=q Gamma_0. The same Gamma_0 applies because the instance/attack family is not changed when an encoder is selected. For zero q and potentially infinite baseline value, interpret this as nonnegativity, consistently with the endpoint convention already stated in the source; do not form 0 times infinity.

The extra lower bound Gamma_any,R>=1/96 requires the independently established full-history clean IID floor, not the historical single-bit exact-gate minimax risk. At k=0 a full-history estimator can simulate any **law/parameter-independent** randomized encoding, independent erasure mask and receiver rule, all from its observed word plus fresh private coins. Under matching target, normalizer and clean subfamily this transfers the assumed full-history lower bound uniformly to every composite procedure; taking the infimum over encoders preserves it. The source explicitly imposes these conditions and correctly does not claim Gamma_any,R>=Gamma_exact for the particular historical gate.

For R>=1 the admissible class contains the encoder repeating the historical exact gate R times. That supplies the already proved upper bound (1-q)(1024+2^20)+q 2^17 ell_M. Together with max{1/96,2^(-33)q ell_M}, this establishes conditional Gamma_any,R=Theta(1+q ell_M), uniformly in epsilon,R,M>=64. For R=0 the experiment is baseline and the relaxed bound is still valid. The epsilon=0 and epsilon=1 endpoints are also consistent: the former has a uniform floor and constant upper bound for R>=1, while the latter is exactly baseline. No assertion that a general clean R-bit message equals the single exact gate is required.

For fixed 0<epsilon<1, a fixed feasible target above the historical exact-gate upper constant is achievable using O(log ell_M) bits; any bounded target requires Omega(log ell_M) bits from q Gamma_0. Since ell_M is comparable to log M, this is a sharp Theta(log log M) order **among all admissible fixed-length encoders**, not merely among repetition encoders. The assumption that repetition is feasible and the constant-risk target qualification are both present in the source.

## Limits of this acceptance

This confirms the appended mathematics and its explicit conditional implication. It does not establish the historical full-history floor, the logarithmic baseline bounds, the exact gate's bound or admissibility, or the restored Markov dependency chain. The separate common-law/parameter-independence restrictions must remain part of the concrete model. Adaptive/variable-length encoders, feedback, correlated erasures, noise-aware attacks and extra parameter oracles are excluded as stated. The argument does not resolve the silent-BSC reliability gap. No external publication was performed.
