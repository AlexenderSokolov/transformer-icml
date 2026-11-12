# Independent single-read near-uniform risk-bridge review

2026-11-12. Reviewed qk-risk-bridge/BRIDGE.md. No gap found under its stated single-retrieval, position-independent raw-value, no-bypass contract. This is not a general Transformer risk lower bound.

## Main proof and constants

For a(t)=softmax(ts), differentiating a_j gives a_j(s_j-E_a s). The displayed L1 bound 2e^(2S)||s||_2/sqrt(n) is valid, as is the value-weighted attention bound and Euclidean concatenation over heads. Query dependence on the word does not invalidate this pathwise bound, provided the query reaches the output only through this read and satisfies the bound for every word. The terminal residual and postprocessor's other inputs must remain public/free-pair only, as explicitly required.

A slightly stronger optional constant follows from the softmax Jacobian J=diag(a)-aa^T: ||J||op<=max_j a_j<=e^(2S)/n. Thus ||softmax(s)-1/n||_2<=e^(2S)||s||_2/n. Since the value matrix has Frobenius at most V sqrt(n), the attention difference is <=V e^(2S)QF/sqrt(n), removing the factor two. The existing conservative constant is correct and need not be changed.

The global F bound is on the realized entire key array. A bounded projection matrix and bounded individual hidden rows generally give only F=O(sqrt(n)); substituting them as a constant would invalidate the asymptotic claim. This distinction is explicit in the draft.

## Summary sufficiency and risk

The uniform attention reference is a function of (total spin count, terminal pair) because each raw value is the SAME token-only map. The reference remains summary-measurable after the decoder only because all other decoder/residual inputs are also summary-measurable and parameters are source-independent. A history-dependent query cannot be separately exposed to the decoder. This restriction is necessary, not cosmetic.

With equal prior over +/-h, conditional absolute-loss Bayes prediction chooses one of the two target probabilities according to posterior majority. Their distance is h for each fixed terminal pair. Integrating the smaller joint mass gives exactly B_N=(h/2)(1-TV). The pathwise probability comparison then subtracts GC/sqrt(n) without any endpoint-conditioning factor: the proof uses joint laws including the endpoint. Consequently no missing factor four is present.

I independently recomputed the N=10, h=1/2 count/endpoint law with exact Fraction recursion: TV=2845/8192 and B_10=5347/32768, matching the draft.

## Critical scope boundaries

1. Position-dependent values may encode much more than the total count. They are excluded unless their reference summary is separately analyzed.
2. Evolved/contextual values can contain innovations: with K=0 and v_i=X_(i-2)X_(i-1)X_i, a uniform read estimates theta at root-N rate. Thus global key Frobenius alone provides no multi-layer lower bound.
3. G is the full post-read input-to-probability Lipschitz gain, including output projection, every continued block, final normalization and softmax. Bounded individual matrices do not imply bounded G across depth.
4. Multiple heads can be included with the displayed concatenation norm, but the number and all budgets are charged. Multiple interleaved retrieval stages are not covered.
5. Public additive score biases outside the realized Kq representation are not covered by F without a separate norm bound on the complete scores. Free arbitrary pairwise biases can destroy near-uniformity.
6. The logarithmic post-read depth consequence is a necessary condition under G<=G0 Lambda^D; it is not a sufficient architecture construction or a sharper general frontier.

Conclusion: the risk transfer is sound and more restrictive than a generic low-rank positional theorem. Preserve every stated value-access, key-array and no-bypass quantifier.
