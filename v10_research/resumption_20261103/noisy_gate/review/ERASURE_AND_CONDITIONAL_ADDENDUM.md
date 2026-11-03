# Independent addendum: visible erasure and conditional v10 specialization

Status: **PASS for the abstract erasure claims and the conditional algebra. NOT a verification of the v10 premises.** Reviewed independently after the original BSC report; no automatic extension of that earlier report is assumed.

## Source binding

- `../VISIBLE_ERASURE_COMPARISON.md`, SHA-256 `7c5770e908f31ba90cbab9eef0f5e7eec4d285151879d0f97ea6c36691e690f6`.
- `../CONDITIONAL_V10_INSTANTIATION.md`, SHA-256 `7b1b826f26377fb4e5f45dfd9ab0a39ec97b8ab2674dcc7c8544fe992f68fed4`.
- Original BSC source remains SHA-256 `b94a940fb5a83c93057c19ac8b2b661c0a42105c410f679c6d4bc27ec34c4db7`. Its separate complete review is `INDEPENDENT_FULL_REVIEW.md`, and the exact reviewed source is preserved in `NOISY_MESSAGE_REDUCTION.reviewed_b94a940f.md`.

Both new source files were read in full. No substantive mathematical defect was found. The following records the independent reasoning and precise limitations.

## 1. Visible-erasure sandwich: quantifiers checked

Write E=Gamma_exact and B=Gamma_0. Fix erasure probability q independent of all pre-channel data, target, attack and estimator randomness. The exact experiment can simulate the erasure experiment, so E<=Gamma_erase. Its universal output-bottom component has mass q, so qB<=Gamma_erase by the original reduction. For the upper bound, choose one delta-optimal exact rule and one delta-optimal baseline rule. The visible flag allows a single admissible rule to select the former on success and the latter on erasure. For every instance, its normalized risk is the weighted sum of the two component normalized risks. Taking the supremum bounds it by (1-q)(E+delta)+q(B+delta). Infimum over all erasure rules and delta down to zero give

max(E,qB) <= Gamma_erase <= (1-q)E+qB.

All estimators are fixed across k,theta,K. No supremum is interchanged with an infimum. Nonnegative loss suffices; bounded loss is not required. The source correctly handles nonattainment, finite-component assumptions, and endpoint identities instead of 0 times infinity. The lower information-ordering statement assumes the same attack/instance classes and baseline data in all experiments.

## 2. Repeated erasure equivalence, not merely decoding

With R independent repetitions of the same clean bit, the all-erased probability is q=epsilon^R; for R=0 this is defined as 1. The transcript maps deterministically to the bit if any coordinate succeeds, or bottom otherwise. Conversely, given a successful bit from this effective channel, sample a mask from the independent iid-erasure mask distribution conditioned on at least one success and fill successful entries with that bit. Given bottom, emit the all-erased transcript. The mask distribution depends only on epsilon,R, not on Z, the bit, the target, or the attack. Therefore this is an exact Markov-kernel simulation preserving the joint law with Z and every risk-relevant pre-channel variable. The source handles the null-success branch and epsilon=0 endpoints correctly. Hence both experiments have identical minimax values, including when arbitrary joint estimation with Z is allowed.

At epsilon=1 or R=0, the experiment is baseline-only. At epsilon=0 and R>=1 it is the exact-bit experiment. Fresh mask independence is essential; noise-aware changes to Z could invalidate this equivalence and the sandwich.

## 3. Rate and necessary positive floor

The source explicitly assumes c_e<=E<=C_e and c_0 L<=B<=C_0 L with positive uniform constants. Its conclusion Gamma_erase,R=Theta(1+epsilon^R L) follows from the sandwich, with constants uniform over epsilon and R. The positive exact-risk floor is indispensable for the added 1: if E=0, noiseless transmission has zero risk. A valid more general comparison for finite E,B is

(1/2)(E+epsilon^R B) <= Gamma_erase,R <= E+epsilon^R B.

For fixed 0<epsilon<1, an upper target C_e+a with a>0 is achieved by taking epsilon^R C_0 L<=a, requiring at most O(log L) repetitions. Any fixed positive upper target C requires epsilon^R c_0 L<=C, hence at least Omega(log L) repetitions. Thus Theta(log log M) is a genuine matching repetition-complexity order if L is comparable to log M and the chosen target is feasible as specified. It does not promise a risk level below E, does not cover epsilon=1, and is not a theorem about silent BSC errors.

## 4. Conditional v10 arithmetic

The following are only assumed inputs in the reviewed sources, not independently verified by this addendum:

- g_k=max(M^(-1/2),k/M), budgets including zero, so g_min=M^(-1/2).
- 2^(-33) ell_M<=Gamma_0<=2^17 ell_M, ell_M=1+ln((M+2)/2).
- Exact-rule risk <=1024 M^(-1/2)+2^20 k/M, yielding E<=1024+2^20 after division by g_k and a uniform supremum.
- Historical clean/exact floor E>=1/96 for the erasure specialization.
- Matching estimator randomization conventions, legal encoders, attack/kernel classes, protected unchanged baseline observations, and [0,1]-bounded loss for the BSC additive upper bounds.

Under precisely those inputs, all displayed numerical factors in CONDITIONAL_V10_INSTANTIATION.md check out: multiplying the baseline lower bound by 2eta gives 2^(-32)eta ell_M; the exact-rule additive term is eta sqrt(M) or e_R sqrt(M); the chosen ceiling R>=log(M)/(2[-log rho]) gives e_R sqrt(M)<=1/2; the arbitrary-message factor is 2^(-33)(2eta)^R ell_M. The 1024 contribution is correctly retained.

The erasure specialization likewise gives max{1/96,2^(-33)epsilon^R ell_M} below and (1024+2^20)+2^17 epsilon^R ell_M above. For M>=64, replacing ell_M by a comparable log M in asymptotic statements is legitimate. These formulas establish **conditional** consequences, not the truth or admissibility of any of their concrete premises.

## 5. Release boundary

The recovered WPC/FOU/FOT proof dependency chain, historical receipts, and the reported floor 1/96 were not audited in this addendum. Their restoration and verification remain an open parent task. In particular, no claimed v10 logarithmic baseline bound, exact-gate construction, or common-law-independent attack admissibility receives a new acceptance merely because the channel algebra is correct.

The sharp visible-erasure result cannot be used to close the BSC gap: the branch-dependent baseline/exact choice requires an observed failure flag absent from a BSC. The distinction is substantive, not a proof artifact. No adversarial-noise or damaged-public-count statement follows. No repository publication was performed.

## Revision history and final interface check

The conditional source was first read at `6c0c85a9b58b1c0ca2dca1e7911bb9fdd64f11b9e5633820d1079cbfe2dab23c`, then at `3ed7652df32b39aef3bcdb85be036bfbacfd575b61c40d532e5a9d43e52e82a2` (two historical link corrections), and finally reread in full at the bound `7b1b826f...` hash. The link-only original can be reconstructed exactly from the author's retained intermediate before-image, and its hash was verified. The original review did not validate the concrete model's historical indexing; root subsequently found the path-length mismatch and requested its correction. The final source now describes M+2 symbols, M consecutive triples, and protected final positions M,M+1. This is internally consistent; correspondence to the historical experiment remains the parent's provenance task.

The retained author diff in `../revisions/CONDITIONAL_V10_INSTANTIATION.interface_fix.diff` also adds the parameter-oracle prohibition and the clean-floor data-processing argument. These are sound conditional repairs: an estimator with the full observed word can simulate any parameter-independent randomized supplemental encoding of that word and the associated reduced observation. Thus a full-history clean lower bound transfers to the exact-message experiment at k=0, **provided** the historical lower bound uses the matching target, normalizer, and admissible clean subfamily. This review does not prove the numerical historical 1/96 bound. An abstract parameter-dependent encoder is allowed by the minorization theorem but cannot be used for this concrete data-processing floor. The final source correctly distinguishes these two claims.

No revised mathematical content has been accepted solely by inheriting an earlier hash review. The final source and actual revision diff were separately read; all release boundaries above remain in force.
