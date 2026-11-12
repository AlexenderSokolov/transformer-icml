# Independent review: heterogeneous-position tag-aware L2 refinement

Date: 2026-11-12. Reviewed THEOREM.md analytically. Verdict PASS; no mandatory correction. No independent numerical rerun or formal verification. This reviews a refinement of the original bounded-score theorem, not the centered-key theorem.

## Reference independence and positional structure

The raw reference at row i is a deterministic two-branch function of X_i and public position information. It remains independent of theta and the terminal tag because causal raw rows never read the appended terminal. For each fixed terminal tag r, the receiving reference state and its self contribution are deterministic. Reference weighted numerator/denominator functions are token-local in each raw source sign, even though actual network states are fully contextual. Complete public positional biases count in S and cancel only in the state-difference comparison. The common-domain requirement explicitly covers inconsistent fixed-tag/query/reference-bank combinations, as needed.

## Fixed-tag L2 concentration and selection

The known vector covariance bound applies separately to each fixed query/tag branch under the UNCONDITIONAL source law. The terminal self contribution cancels for that fixed branch. Neither operation conditions the raw law on the observed endpoint. Denominators remain bounded below by exp(-S), so the quotient comparison is pathwise and uniform over all branches.

The exact pointwise identity ||Z_R||²=sum_r 1{R=r}||Z_r||²<=sum_r||Z_r||² is valid with arbitrary correlation. It gives sqrt2 for a raw sign query and2 for four terminal tags. Selecting the actual tag after fixed-tag concentration is therefore legitimate. No division by P(T=r) or conditional independence is hidden. The sharpness example proves only the generic selection lemma, as the draft states.

## Fully evolving-state recurrence

First compare the actual bank to the reference bank at the SAME realized signs and terminal tag, using the original bounded-score stability inequality. Then apply the fixed-tag fluctuation comparison. Minkowski's inequality gives the stated RMS recursion with a,b unchanged and forcing sqrt(m_i) f. The common envelope uses2f, which coincides with the old first-moment theorem's displayed forcing. Thus the improved free-pair bound does not silently assume smaller per-layer score amplification.

The separated raw/terminal recurrence is correct: multiplying the terminal prefix-error term by sqrt(n) yields b alpha_N R plus bT/n, with alpha_N=n^-1/2 sum_{j<=N}j^-1/2<2. Reference projection is nonexpansive and fixes true states. Values, local maps and final head must retain their common-domain bounds; they are explicitly required.

## Risk, tails and comparison with the old factor four

The new proof tracks the ACTUAL tagged execution directly in unconditional L2. It does not first bound a complete artificial-tag execution and later condition on endpoint agreement. Consequently the old factor4 conditioning loss is genuinely avoided by a new proof, not simply deleted.

Uniform per-theta RMS error delta implies the same bound under the equal +/-h prior. At each endpoint pair the two targets differ by h, so every common pair-template has averaged absolute risk at least h/2 and squared risk at least h²/4. L1 and L2 triangle inequalities give max(0,h/2-delta) and its square. For theta0 versus h the corresponding half-gap is h/4. The tail bound is ordinary Markov applied to squared error and is correct.

The update remains a logarithmic-depth-scale result with potentially exponential E_D. It does not establish a matching construction or an arbitrary-depth information contraction. Exact-real information retention in a shrinking output range is compatible with its RMS conclusion. No global key-energy budget is introduced, and no centered-key terminal-cancellation theorem is being silently substituted.

## Verification boundary

The draft's finite checks concern only selection bookkeeping and are not numerical certification of a nonvacuous network risk bound. This review is analytical. Any diagnostic replay should be credited separately to the worker that performs it.
