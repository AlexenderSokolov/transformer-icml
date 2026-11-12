# Independent key-energy examples review

2026-11-12. Reviewed RESULT.md analytically. Both examples pass. No independent diagnostic rerun claimed.

Example A: the initial squared norm is6 in width6, so epsilon1 LN divisor is sqrt2. The three stated sqrt2 projections recover constant query1, positional key p_i and value X_i. For even N the keys are centered, Frobenius sqrtN, and weights are (1+p_i tanh1)/N. The alternating word gives a constant attention discrepancy. The mean-square formula has the correct sign (-1)^j at lag3j, and its upper bound follows by absolute covariance summation. Consequently this example is a worst-word failure of near-uniformity, not a nonvanishing average-risk result. Supplied alternating position features remain an explicit input assumption.

Example B: raw squared norm4 gives LN divisor sqrt(5/3); terminal squared norm2 gives sqrt(4/3). The chosen Q,K,V recover the stated raw/terminal queries, keys and values. Allrow score and post-attention state norm bounds check out. The terminal read formula, centered array energy N-S_N²/(N+1), and final full-LN map Phi(x)=sigmoid(lambda sqrt3 x/sqrt(4+x²)) are exact.

At theta0 the source is iid fair, so m_N->0 and the actual read tends to tanh1 whereas the uniform reference tends to0. Bounded continuity yields the positive limiting risk and expected predictor discrepancy. This is a genuine failure of a UNIVERSAL parameter-bound-to-near-uniform transfer; it is not a lower bound for all architectures. The constant1/2 predictor has zero risk at theta0. The draft correctly states this distinction.

The squared matrix parameter total20/3, three LN gain-vector contributions18 and final-head lambda² are correct for the displayed one-block architecture. Embedding coefficients are separately fixed and bounded. The theorem's global centered key premise fails: its centered energy is order sqrtN, despite these ordinary parameter/per-row bounds.
