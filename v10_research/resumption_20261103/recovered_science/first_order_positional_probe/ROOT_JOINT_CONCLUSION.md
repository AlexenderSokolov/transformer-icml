# Natural first-order positional information: root consolidation

2 November 2026. FOU001 and FOL001 have each passed fresh independent proof review and root acceptance. The revised exact sources and review histories are bound in intake/FOU001_root_acceptance.json and intake/FOL001_root_acceptance.json. This is local scientific acceptance, not formal verification, external peer review, a novelty certificate or publication permission.

## Same experiment, matched bounds

For integer N>=64, 1<=r<=N+1, consider all binary homogeneous first-order transition tables, arbitrary starts for sufficiency and stationary starts for necessity. The word has N+1 symbols and N departures. The sole protected terminal symbol is the actual prediction query. A common offline source-independent kernel may edit at most k of the first N symbols on every outcome, integer0<=k<=N. The predictor sees four exact transition counts plus the first/last r symbols, but not k. Risk is unconditional expected unsquared TV.

Let g_N(k)=max(N^-1/2,k/N) and ell=1+ln((N+1)/r). For one map at fixed(N,r), take the supremum of R/g over all k and experiments; then infimize over maps. The reviewed lower and upper have this same definition and imply

2^-30 ell <= Gamma_stat(N,r) <= Gamma_all(N,r) <= 2^17 ell.

The upper ignores the raw prefix. No spectral gap or minorization assumption is needed. The same-information known-budget risk lies between g/96 and2^16g, so this is a genuine rate-oracle comparison. Exact oracle normalization changes numerical constants: the sufficient factor is at most96*2^17ell, not2^17ell. Conversely an exact-oracle-relative factor D implies a g-relative factor at most2^16D.

## Consequences with precise scope

- For prescribed widths, a uniform finite factor exists iff liminf r_N/N>0. Upper uses explicit suffix maps and finite early horizons; lower uses a subsequence where ell diverges. No infimum/limit interchange is needed.
- Counts plus the two endpoint symbols (r=1) require order logN competitive factor. This is not a risk lower at every individual budget.
- In the separate full-word-scan/exact-message model, the reviewed half-gate bit attains a constant factor. A singleton message alphabet leaves at most the r=1 baseline, ruled out by the lower. Thus the minimum fixed supplemental alphabet is two. This is a direct interface deduction; the bit is computed after all edits, not a raw coordinate or a noisy communication channel. Optional access to the initial symbol does not change this conclusion.
- The phenomenon therefore does not require second-order dynamics in the natural matching-order histogram experiment. However, it does NOT yet follow that the first-order subclass has the same lower when given the original eight triple counts and two protected symbols. That richer-access question is being studied separately and is not included in this acceptance.

## Why this matters for the existing manuscript

The two-state hitting scale is exactly max(1,a+t)<=2, removing the original certificate-dependent four-state calculation. The lower mixture becomes a one-state marked-run skeleton with an exact binomial sum. These simplify the mechanism, but the observation and protection conventions differ. The accepted31-page second-order manuscript remains unchanged. Do not replace it or assert the two experiments are equivalent.

A bounded primary-source screen found no inspected subsumption or contradiction, with explicit reading limits. In particular HJW's binary TV-rate question is in squared loss; this unsquared result does not resolve that question. Transition-matrix contamination and independent-trajectory robustness are different experiments. No first/novel claim is made.

Next check: whether adding all triple counts removes the first-order lower, under two protected terminal symbols and fully accounted horizon shifts. The unreviewed renewal observation in TRIPLE_ACCESS_NEXT_QUESTION.md is a lead, not an accepted theorem.
