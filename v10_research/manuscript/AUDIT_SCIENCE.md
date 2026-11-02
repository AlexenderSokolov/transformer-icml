# Independent manuscript science audit

Audit date: 2026-11-02. Reviewer: independent LLM reviewer.
Scope: 04:45 UTC scientific freeze; manuscript synthesis, not external peer review or formal verification. No manuscript or proof-source edits were made by this reviewer. Exact reviewed file identities and evidence paths are in `AUDIT_SCIENCE_BINDINGS.json`.

## Decision and issues

**ACCEPTED after source-level correction and reread of S1, S2 and T1.** The mathematical synthesis is supportable with the now-explicit model hypotheses below. These are missing hypotheses in the initial manuscript, not requests for new research. The substantive statements, including the new uniform full-histogram corollary, otherwise pass this review. Final source status is recorded in the binding file and closure addendum below. No required scientific correction remains open.

1. **S1 — causal upper membership / density (required).** CF001 §1 requires that the architecture budget permit density constant `c<=1/3`. Its explicit four-head prototype uses keys `3,...,min(t,N)` and has density exactly 1/3 at row three. The initial manuscript declared only a fixed positive c, which does not guarantee inclusion of this proved upper witness. Required change: explicitly state that the density budget permits `c<=1/3`. The author has now inserted this condition. This does not broaden the proved family.
2. **S2 — local weights strictly positive and fixed (required).** BA001 and BF001 require `0<a<=b<infinity`, with a,b fixed independently of M,Q. The initial definition displayed only `a<=w<=b`, and the main theorem only `a<=1,b>=6`. Zero/negative lower bounds are not admissible; positive dense mass is load-bearing in concentration and ratio bounds. Required change: explicitly impose `0<a<=b<infinity` fixed independently of M,Q in the local-family definition, and use `0<a<=1` in the main theorem. The author has now inserted the strict-positive fixed bounds in both locations. Growing kappa in Section 8 is a separately quantified application of the finite constants, not an exception silently available in the bounded-family theorem.
3. **T1 — mathematical typography (required, resolved on reread).** Three literal `qquad` strings lacked backslashes in signed weighted sums and the recovered-frequency TV display. They would print as mathematical variables, corrupting the equations. A source search after author changes finds no remaining unescaped instances.
4. **B1 — optional bibliographic precision.** Hahn's author PDF is titled “Supplement: Theoretical Limitations of Self-Attention in Neural Sequence Models,” rather than the descriptive “Supplementary Material for ...” in the bibliography. URL, author, date and substantive correction are correct. The author has now normalized the exact title; this does not affect a claim.

## Method and evidence boundary

Read the entire manuscript text and bibliography, then compared theorem statements and relevant derivations in FR001 v1, BA001 v1, BF001 v3, CA001 v3 and its boundary-causality note, FA001 v3, CF001 v1, SB001 v2, GW001 v3, PF001 v1, AU001 v1, IU001 v1, NB002 v1, and the inherited R011 statement and G/U §11.1. In particular the check did not merely infer validity from acceptance JSON. R011's entire older statistical dependency chain was not re-proved; its use is explicitly inherited, as required by the manuscript's modular status. The current review checks the interface and stated premises, not a claim that the article alone proves that chain.

Literature prose was compared with all four version-specific primary-source notes in `prior_art/`. Fresh primary metadata checks covered all eight bibliography entries (publisher/arXiv/author pages); the substantive external theorem comparisons rely on those inspected-primary notes, not on abstracts. The external papers' proofs were not independently validated in this audit. No private proof formulas were sent to search; only already-public bibliographic URLs were opened.

## Statement-by-statement assessment

### Experiment and complete cut

- Actual terminal pair is Y_M; departures end at M-1; successor counts use X_(j+3). No independent query or unobserved target symbol enters the predictor.
- The certificate is existential, stationary and all-state, including off-support starts. Zero transitions remain legal. Stationary initialization is at a qualifying hidden law, not a known law supplied to the encoder.
- Minimax choices are source-law independent; public class promise beta and source-independent seeds are allowed. Fixed uniform bounds apply seedwise, so the same priors and uniform per-seed lower arguments survive randomization.
- All D coordinates and finite exact boundary/flag metadata are retained in the count. No clean numerator, denominator, duplicate state, historical token output or history reread is introduced. The cut is correctly described as access control, not a free physical isolation device.
- Grid Q is absolute coordinate resolution. Closed [0,1] coordinates need h+1 bits; signed bounded ranges h+O(1); accumulation and products additionally pay log M and full widths. D, heads, ideal depth, unrolled depth and total bits are not identified.

### Theorem: bounded finite information cut

- Original-bank constants and domain match FR001: K>=3, M>=64, h>=4, beta in [0,1], lower 2^-336 H, and displayed C_K. The source inclusion direction is correct: stationary risk <= arbitrary-start risk.
- Local lower uses BA001 for the full bank, not the original-interface lower transplanted into a larger class. BF001 verifies the **actual** finite prefix weights in [1,6], local radius three, 9K+1 outputs, boundary inclusion, and deterministic-zero padding. Its matching upper needs the corrected S2 hypothesis.
- Causal family matches CF001/FA001: supplied finite dyadics, affine/ReLU blocks, bounded reachable states on formal histories, public branch-independent dense causal masks, fixed architecture, compiled precision h+3, final Q-floor. The capacity witness has width 12K+4 and D>=9K+1; S1 is needed for its mask inclusion.
- CF001's upper replaces the original statistical evaluator. Uniform error 1/(8Q), finite-log error 1/(8Q), and final floor <1/Q give <2/Q, with closed [0,1] range. This meets NB002's deterministic premises. Equality of labels and selector decisions is correctly disclaimed.
- Constants are fixed-alphabet/fixed-architecture constants, not uniform joint-K or growing-depth/dimension claims.

### Corollary: grid threshold

The displayed synthesis proof is valid. With s=sqrt(M), t=M beta0 and f=1+ln(1+s/t), Q=sf gives W<=2/s; W is decreasing. Conversely H<=A/s implies Q>=s/A, logarithmic concavity gives numerator >=f/A, hence Q>=sf/A². The risk lower constant must be incorporated into A, and the text explicitly does so. A sufficiently large attainable target multiplier is distinguished from necessity for every chosen multiplier. Known-beta budget choice is not asserted to learn beta.

### Lemma: good-message Bayes bound, and all-Q completion

- Stationary witness is legal, including unused-symbol rows and off-support starts. The common prior remains uniform conditional on E_j because event probability is p-independent.
- The next target retains exit probability eta. Its TV coordinate lower is valid for arbitrary simplex outputs, even if rescaled scalar decoder outputs leave the prior interval.
- Local numerator/denominator expectations, replacement bounds, variance, curve derivative, and tube count match BA001. The comparison curve is a ratio of means, not a mean ratio. Full boundary values are frozen before unconditional IID sampling; simultaneous estimates precede selection of the actual branch.
- The good event can vary with p, while the containing label set cannot. The covering argument uses only that fixed alphabet; 9/10 minus 1/4 times radius is stronger than ell/(16R).
- The rare-window cutoff retains both 1/beta0 and M²/Q². The logarithmic lower retains min{Q/(M beta0),M/Q}. IID c/Q and full-history statistical floors close the remaining domains, by maximum rather than by a fictional common-source sum.
- The elementary all-Q completion is valid: high beta bounds W by 1/Q+O(M^-1/2), high Q by 5M^-1/2, and in the remaining range x>y implies x<=y³. No thick-tube extrapolation is used.

### Proposition: triangular influence

The softmax differential correctly retains weight variation. Interpolation takes place in bounded logit space, not through unverified reachable hidden states. Dense masks supply C=e^(2B)/c. The recurrence and triangular-power expansion are valid; d_i is the dominating matrix entry, so its row-sum bound is not incorrectly applied to a larger envelope. The right-Riemann-sum square bound and late-suffix bound hold. Fixed local windows multiply sum/late constants by r and square constants by r².

The A² example correctly disproves uniform O(1/T) influence for the earliest token; the proof instead uses logarithmically inflated early influence, square summability, and O(1/M) late influence. This is not a claim that Hahn's unrestricted dense argument immediately establishes the causal statement.

The formal frozen-boundary branch model can broadcast future information and is explicitly identified as stronger than true temporal causality. Historical tables/parameters and masks in the actual finite causal theorem are future independent; only the appended initial query reads the complete boundary. This matches the adopted causality note.

### Theorem: finite evaluator

Signed downward rounding, complete affine products/sums, shifted positive Taylor recurrence, and exact signed weighted division agree with FA001. T_0 makes every weight >=1 in real units, hence denominator >=m; no attention-weight underflow certificate is assumed. There is correctly no extra scale division in O=floor(N/Z). The error comparison is uniform in key count, and the bootstrap constants are computed on the rounded-state neighborhood before the induction closes it. P=4h+C_arch is fractional precision, not the full signed/accumulation word.

End-to-end error transfers the information lower by widening final tubes; discontinuity of intermediate rounding is not treated as Lipschitz. The full integer expansion is not called a fixed-depth scalar Transformer. Layer normalization and arbitrary unevaluated Lipschitz maps are excluded from this finite subclass.

### Upper proof: statistical inputs and occupation

- The exact ORIGINAL and common-selector scales match R011, including positive exponents at beta=1 and the same-history add-one and pooled definitions.
- NB002 recovery constants 76/Q and 6/Q, positive approximate counts, Aminus, radius inflation and monotone rejection containment match its Sections 2–6. The inherited event-radius/rejection estimates are explicitly needed; a final scalar statistical bound is not used backwards to manufacture them.
- G/U §11.1 is accurately reproduced: the maximum over starts is monotone by suffix domination; sum-of-maxima <= sum-over-starts gives d²w, not dw. Integer ceiling thresholds justify layer cake.
- IU001 reverses only on positive stationary support, proves return expectations before conditioning/integration, and uses a singular-operator comparison without assuming reversibility. The stationary clipped reciprocal matches its actual statement.
- AU001's residual kernel is stochastic on all states, exact suffix-law mixture uses the original P path extension, and full counts dominate suffix counts. The residual is not mistakenly evolved under R. Its precision-decaying cost removes an additive burn error for all Q; beta=0 and beta=1 endpoints are handled separately.
- The manuscript explicitly retains these as modular dependencies, not a new self-contained all-parameter statistical proof.

### Theorem: amplified triple bank, and effective-range comparison

- The changed evaluator uses actual integer weights {1,kappa}, not the old exp routine. Query/key dimension K², local triple features, all K³ output coordinates, two paid singleton acquisitions and all-token work are identified.
- The selected mass kappa J/[M+(kappa-1)J] and unchanged conditional composition C/J are correct. The zero-floor branch is included: if all coordinates vanish then r<K/Q. J=0 is covered by the unit first term.
- Deterministic error, occupation substitution, D_K=K^5(K+1), and bitlength-only schedule match SB001. With M>=64 the h>=4 clamp causes no inconsistency; sqrt(M+1)<=Q<=2sqrt(M+1). The bounds on Psi yield the displayed integer-point constant.
- The lower explicitly retains A_b<=C_BA kappa^(D+1). With Q in the fixed square-root band and beta=0, the rare-window logarithm has order ln M. Thus effective range ln kappa has required loglog order, not a sharp necessary kappa~log M.
- Comparison family has at most D coordinates. Zero padding for BA001 is conceptual only, not an uncharged physical extension. Sufficient dimensions D>=K³ are retained; no matching upper is asserted with too few coordinates.
- Necessity is only for fixed-dimensional, fixed-locality, one-global-summary family, not arbitrary deeper networks. The upper holds at K=2; three symbols are required for this logarithmic lower.
- Optional beta refinement uses SB001 §7 and states the c_- dependence of the sufficiently large target-risk multiplier. For bounded f it concerns 1+ln kappa, not a positive pointwise lower on ln kappa. Budget selection using beta is not beta estimation.

### Corollary: uniform full-histogram synthesis (new manuscript proof)

**Accepted as a correct short synthesis, not a separately frozen source theorem.** At kappa=1, SB001 §7 gives risk <=O_K(M^-1/2)+O_K(W)+(2K-1)/Q, and 1/Q<=W. The fixed full K³ bank has weights a=b=1 and radius three, hence BA001's lower applies to this specific encoder and unrestricted decoder; granting the stronger complete boundary can only make that lower harder to prove, so it is safe. BA001's own IID and rare-window lower bounds plus the displayed domain completion give Omega_K(H). Stationary inclusion and the arbitrary-start upper finish both risks.

Crucially this argument does **not** invoke BF001's matching-upper requirement D>=9K+1. At K=3 the histogram has 27 coordinates, less than 28, but BA001's lower permits every fixed D>=1. The manuscript uses the correct independent route. It also correctly distinguishes K³ versus 9K+1 resource dimensions despite equal fixed-K rates.

### Resource ledger and limitations

FA001 compact converted records use O(UP), separately from guarded numerical words and original descriptions UB_param; padding is correctly charged as a different format. The sequential schedule and bitwork are not free RAM claims. SB001 full products, guarded temporary widths, all-token banks/masks/code, separate addressed and PURE alternatives, offline generation, and phase sums are represented consistently. No best-of-both ledger is assembled. Weight bitlength O(loglog M), effective range ln kappa, cut h and full words O(log M) are distinguished. No runtime/memory optimality, practical constants, training convergence, emitted-network execution or attention-specific computational advantage is claimed.

## Literature assessment

- Behrens is prominently credited for the actual rational weighted-inventory ancestor, including weights e and 1, mass ek/[L+(e-1)k], and inversion. Infinite precision is retained. The article does not claim to invent grouped histograms or block normalization.
- Yehudai is cited for histograms and query-count inversion, not used as a finite-arithmetic certificate (the primary notes flag its sum/average normalization caveat).
- Rajaraman's attention-only precision statement is not silently transferred to its layer-normalized construction.
- Hahn is accompanied by the 2021 weight-change correction; Chiang–Cholak is used to distinguish shrinking sensitivity from finite-message loss and to identify normalization/logit escape routes.
- Han–Jana–Wu is credited for waiting/common-prior/harmonic and mixing precedents, while KL/full-history/stationary/spectral hypotheses are not equated to this TV finite-cut experiment.
- Xu–Raginsky is credited for finite-message and half-log communication primitives; the manuscript correctly explains that generic Q^D cardinality alone is insufficient.
- No novelty certification or broad negative literature assertion appears. Modular proofs and independent LLM audits are not called external peer review or formal verification.

Fresh metadata sources: [Behrens/PMLR](https://proceedings.mlr.press/v267/behrens25a.html), [Yehudai v3](https://arxiv.org/abs/2407.15160v3), [Rajaraman v1](https://arxiv.org/abs/2407.17686v1), [Hahn/TACL](https://aclanthology.org/2020.tacl-1.11/), [Hahn supplement](https://mhahn.info/files/transformers-proof.pdf), [Chiang–Cholak/ACL](https://aclanthology.org/2022.acl-long.527/), [Han–Jana–Wu v2](https://arxiv.org/abs/2106.13947v2), [Xu–Raginsky v1](https://arxiv.org/abs/1607.00550v1).

## Closure addendum

Final reread at approximately 05:00 UTC confirms S1 (density budget), S2 (strict-positive fixed local weights and theorem bounds), T1 (no malformed qquad), and B1 (exact supplement title) are all resolved. **Scientific manuscript synthesis accepted on the exact files in AUDIT_SCIENCE_BINDINGS.json.** PDF layout inspection belongs to separate visual QA, not this scientific acceptance. Any later source change requires an updated binding; scientific changes require rereview. This acceptance remains modular and does not certify the inherited full statistical chain anew.
