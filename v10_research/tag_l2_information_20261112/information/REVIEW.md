# Independent review: full-PreLN exact information retention

Date: 2026-11-12. Reviewed CANDIDATE.md analytically. Verdict PASS; no mandatory correction. No independent diagnostic rerun, novelty certification or formal verification.

Raw and sentinel inputs both have mean zero and squared norm6. The raw key/padding pair contributes constant energy2, while the sentinel sqrt2 padding pair contributes4 and replaces the absent token/key energy correctly. Width12 epsilon1 LayerNorm therefore has the common divisor sqrt(3/2). The stated projections recover query1, raw keys k_j, raw values X_j and sentinel key/value0 exactly.

At the terminal the shared bounded output coefficients cancel the uniform part exactly, producing C_T=T^-1 sum 2^-j X_j. The same coefficients are used at every row; other rows need not realize a prefix code. Their attention averages remain in [-1,1], so the displayed all-row physical-state bound is valid. Matrix Frobenius squares, zero biases, the three LN gain-vector contributions36, and final head coefficient are correctly charged. Public logarithm/padding features and the exponentially resolved N-dependent coefficient are explicit representation assumptions, not manufactured for free from a scalar position.

The final terminal state has squared norm6+2C_T², so the final full-LN logit lambda C_T/sqrt(3/2+C_T²/6) and its derivative are exact. The actual probability is strictly increasing, with fixed positive derivative bounds on the stated compact interval.

Binary word codes form a uniform grid with exact spacing2^(1-N)/T. This proves injectivity without relying on floating-point collision checks. Probability spacings are of the same order by the derivative bounds. Worst-word recovery from adversarial scalar-output error therefore requires resolution of order2^-N/T; the stated p=N+log2T+O(1) is correctly restricted to that output-error model. Recovering opposite last bits requires gain at least T2^N in code coordinates. These do not automatically prove a coefficient-bit or per-residual execution lower bound.

The exact output map is independent of theta and injective on the finite word space, so KL and TV of source laws are preserved exactly. Independent triple innovations give the displayed (N-2) Bernoulli KL formula. For distinct fixed parameters, full-history testing yields TV tending to1; meanwhile all outputs lie in an O(1/N) interval, hence their Wasserstein-1 distance is O(1/N). There is no conflict between these metrics.

The actual bounded-gain prediction head stays O(1/N) from1/2, and its pathwise absolute-risk difference from |theta|/2 is at most that amount. Its L2 displacement from1/2 is also O(1/N), so the original and strengthened mean-field output-approximation results remain compatible. The model is not a successful predictor merely because an external discontinuous or exponentially steep inverse could recover the word.

The realized full key-array norm is bounded while the whole query array has norm sqrt(T); the single-terminal query norm remains1. This correctly matches the earlier global-key bridge's hypotheses and does not assert a globally bounded query array. This is an explicit ledger for a known exact-real information phenomenon, not a new injectivity principle or a low-precision algorithm.
