# UI001 independent hostile mathematical review v1

Date: 2026-11-02. Reviewer: `independent LLM reviewer`.

## Verdict

**PASS — no mathematical blocker found for UI1 in the stated one-block local dense positive-weight ratio model.** Reviewed manuscript SHA256: `c4bd8a5d7324ed1cf03c1d746a253b592fbe9a63e9e6020be95e657c13307dde`.

This is an independent LLM mathematical audit with independently written exact-rational diagnostics, not formal verification, literature priority checking, or original-network execution. No source manuscript was edited. Root acceptance remains a separate decision. The supported conclusion is a positive `c(D,r)/Q` minimax floor uniform over all finite κ≥1, all real Q≥1, and every β∈[0,1]. It does not itself prove a matching two-resource frontier or any upper construction.

## Dependencies and model boundary

Read the complete UI001 manuscript, its source bindings and diagnostic script, complete BA001 and SH001 manuscripts, and both acceptance records. BA001 supplies the exact model and the elementary full-history two-point calculation; SH001 supplies its normalized [1,κ] restatement. No κ-dependent constant from BA001 is silently promoted to uniformity here. The new heavy-window/posterior argument is checked directly below.

The model uses fixed finite D and integer r, all M keys, actual positive weights, normalized local values, source-independent positional tables, and only boundary-derived exact query information. Random seeds are source-independent. Any extra interior exact information, recursive global feature, source-dependent table selection, variable interior-selected domain, or growing number of coordinates is outside this verdict. K does not affect the witness: fix two designated symbols, and define even unsupported pair rows to emit their common Bernoulli law.

## Adversarial checks

### 1. Source, all-state certificate, and target

The IID product pair law is stationary. From every pair state, including unsupported symbols, two common-law transitions produce exactly the product pair law. Thus P²(s,t)=Π(t), not merely an on-support statement; every β≤1 is allowed. The actual next C1 mass is p at every terminal context. TV dominates the C1 mass error even when a decoder assigns mass to other symbols. An arbitrary real scalar estimate would not weaken the scalar lower argument.

### 2. Small-history branch, real Q, and oversized locality

With m=ceil(CQ²), integer M<m gives n=M+2≤m+1≤(C+3)Q². The manuscript's looser chain through m+2 is valid too. The two fixed points p±=1/2±1/(16√n) give KL≤1/8, history TV≤1/4, and risk≥1/(128√n). The experiment can grant full history and independent encoder seed; neither adds source information beyond that history. The prior is independent of the encoder seed.

The displayed C is ≥r (indeed enormously larger). Consequently r≥n=M+2 forces M<m at every Q≥1, so the conditional reveal argument is not being applied where boundary windows alone cover a large history without sufficient m. All inequalities remain meaningful for nonintegral Q and equality M=m belongs to the large-history branch.

### 3. Query freezing and public reveal

There are ≤2^(2r)≤H possible binary boundary strings; overlap consistency only reduces this count. For each such s the proof freezes q(s) before sampling. The maxima a_dsi, tie-broken top-m indices, and union U are public source-independent objects, conditional on a fixed encoder seed. Taking a union across all branches does not condition on S, even when S includes the final observed symbol. No next unseen symbol is granted or used. Once B=X_U is observed it fixes S, which is an original permitted side field.

The selected underlying trailing windows contain their endpoints, so m≤N. A table which ignores its endpoint or is constant still has the canonical window envelope from the exact model; its bits may conservatively be revealed. This does not require actual functional dependence on every revealed bit. Public padding is not counted as a sampled bit. The other bound N≤rFm+2r≤Lm uses m≥1. U itself has no source-dependent information: it is fixed before the sample, not chosen by the realized large weights.

### 4. Heavy patterns, overlap, ties, and event measurability

Choose one maximizing binary local pattern at each selected position, with deterministic tie-breaking. Its probability is ≥4^(-r)=q for all p∈I; fixed padding or fewer variable bits only improves this. Each trailing envelope overlaps at most 2r−2 other selected envelopes. For the indicator sum, Var≤(2r−1)m follows by bounding diagonal terms and ordered overlapping covariance terms by one; disjoint indicators are independent. Chebyshev at qm/2 gives failure ≤4(2r−1)/(q²m), and union over F gives ≤.01 by C.

All maximizing-pattern indicators depend only on B, hence E is B-measurable. For every selected maximum, a_i≥a_* irrespective of ties. Each realized maximizing selected pattern contributes its a_i, so W≥(qm/2)a_*. No independence of coordinates, branches, or S is asserted. Perfectly correlated heads therefore cause no issue.

### 5. Partial reveals and the κ-free denominator charge

This is the crucial nontrivial step. A residual window intersecting U need not retain positive conditional probability for its unconditional maximizing pattern. UI001 does **not** incorrectly lower-bound that window's expected weight by q a_i. Instead there are at most rN such windows and their total maxima are at most rN a_*≤rLm a_*≤(2rL/q)μ on E.

Every disjoint residual window retains its entire IID pattern conditional on B at fixed p, so its expected weight is ≥q a_i. Summing yields their total maxima ≤μ/q. Therefore sum_unselected a_i≤Jμ with exactly J=(2rL+1)/q. Reusing μ in both charges is conservative and legitimate. Very large positional weights are either among the public heavy windows, or bounded by the selected-window mass on E; there is no hidden κ term.

### 6. Conditional Efron–Stein and ratio subtraction

At fixed p and B, unrevealed bits remain independent Bernoulli(p). Selected terms are constants. Replacing a free bit changes either sum by at most 2 times the sum of affected residual maxima. At most r summands are affected. Cauchy–Schwarz and the half-factor in Efron–Stein give 2r times the incidence sum of a_i², and each window has at most r incidences, giving 2r²∑a_i². Combining ∑a_i²≤a_*∑a_i, the preceding charge, and a_*≤2μ/(qm) proves Var≤4r²J μ²/(qm)=Vμ²/m.

For a_*=0 all keys are selected and both variances vanish; no division by zero is required. At M=m all keys are selected per coordinate and U contains all M endpoints, so this case is genuinely covered.

Two Chebyshev bounds per frozen coordinate at μ/(4Q) give 32FVQ²/m≤.01. On the resulting event Dn≥3μ/4 and the exact ratio identity gives ≤2/(3Q)<1/Q. This is a ratio of conditional means, never an expectation-of-ratio substitution. Goodness may depend on p. A union bound needs no head independence.

### 7. Derivative bound

Conditional on B at fixed p, each local remaining-bit pattern has ≤r free bits and logarithmic derivative in absolute value ≤4r on I. Summing positive weighted probabilities gives |μ'|≤4rμ; |v|≤1 similarly gives |μ_A'|≤4rμ. Deterministic terms have derivative zero, and the denominator μ is positive. The quotient derivative is bounded by 8r. This calculation concerns the conditional sampling law at fixed p, not differentiation of the Bayesian posterior. Overlapping windows need not be independent for this termwise derivative calculation.

### 8. Posterior and truncation boundaries

The posterior after B is proportional to p^t(1−p)^(N−t), because U is a deterministic N-position subset for the fixed seed. It is not uniform, and the manuscript correctly accounts for this. Conditional on p, t is Binomial(N,p). Hoeffding gives joint failure ≤2e^(−18); Markov at .01 gives P(B∉T)≤200e^(−18). Union with E gives >.98, without any false independence claim.

For B∈T, I_B is nonempty and dist(y,I)≤3/√N. The clamped mode p0 maximizes the log density, including t=0,N. Since p(1−p)≥3/16 on I, |ℓ'(p0)|≤16√N. Also |ℓ''|≤16N. At least one direction from p0 admits length 1/4 inside I. The chosen δ=1/(64√N) fits there; Taylor loss is at most 1/4+1/512=129/512<log 2. Integrating that short interval proves the 128√N density bound, including a boundary mode with nonzero first derivative. This is the precise place where simply citing a centered normal approximation would fail; UI001 does not do that.

Finally N≤Lm≤L(C+1)Q² gives density≤P0Q. Dependence of N on tables or the encoder seed is harmless because the same P0 bounds every case.

### 9. Good alphabet and arbitrary real quantization

I_B is an interval of length ≤6/√N. For any interval of length ℓ, endpoints plus a spacing-≤1/(8rQ) grid need at most ceil(8rQℓ)+1≤2+8rQℓ points. Since N≥m≥CQ²≥Q², this is ≤2+48r. The derivative bound gives a mesh error ≤1/Q; the random tube adds less than 1/Q. Multiplying by any real Q≥1 and flooring adds a displacement in (−1,0], including negative values. A radius-three integer box is already sufficient, so nine integers per coordinate is conservative. Correlated coordinates may reduce cardinality but cannot increase the product upper bound.

The mesh, its boxes, and all resulting candidate labels are fixed conditional on B and the encoder seed, not on p or the remaining sample. B fixes the actual S, so there is no missing boundary alphabet multiplier. It is permissible for the label set to differ across B because the subsequent Bayes argument is conditional on B.

### 10. Bayes floor, exceptional events, and seeds

For B∈E∩T, posterior mass of I_B is ≥.99, while the tube conditional failure averaged over the posterior is ≤.01. Their intersection therefore has joint conditional probability ≥.98; no assertion of a uniform posterior after goodness is used.

For a fixed decoder seed, at most R0 candidate labels produce at most R0 real outputs. Their ε-neighborhoods have posterior mass ≤2R0εP0Q=1/4. Even though labels are correlated with p, the event of being good and outside every output neighborhood has probability ≥.98−.25. Thus risk≥(.73)/(8R0P0Q)≥1/(16R0P0Q). Averaging over B loses less than a factor two. Randomized decoder seeds can be conditioned on and averaged; source-independent shared randomness is included in the granted encoder seed. The prior in the large-history branch is exactly the same uniform prior for every encoder seed. Therefore a common source supremum dominates the final seed-averaged Bayes risk. There is no illicit seed-dependent adversarial source selection.

## Independent exact diagnostics

Files: `UI001_independent_checks_v1.py` and `.json`, written independently for this review. Execution command:

`python v10_research/reviews/UI001_independent_checks_v1.py`

Observed exit status 0, PASS:

- 2,136 exact-rational conditional experiments; 510 satisfy the tiny-instance heavy event.
- Localities r=1,2,3; tie-broken equal weights; weights above 2^80; overlapping and partially revealed windows; perfectly correlated sign-reversed coordinates; all-selected M=m and zero remaining variance.
- Checked Efron–Stein bound, local derivative bounds, partial/disjoint maximum charges, and heavy-event normalized variance bounds with no floating-point tolerance.
- 226 exact truncated-beta posterior cases in T, of which 122 have a truncation-boundary mode; checked posterior density, mode derivative, and the specific short-interval normalizer lower bound by rational polynomial integration.
- Exact C/probability/ceiling arithmetic for multiple D,r including r=64, and rational noninteger Q values. Verified the r≥n branch implication and m ceiling inequalities.

These deliberately small conditional examples do not meet the theorem's huge C and do not empirically establish .99 event probability; they test the algebra when its required heavy event holds. The theorem's .99 statements were checked analytically above. The posterior finite grid does not replace the uniform proof. No diagnostic failure or discarded counterexample was encountered. A nonessential `git status` probe reported that the workspace is not a Git repository; this has no bearing on the mathematical audit or artifact creation.

## Residual limitations

No revision is required for the claimed theorem. Constants are extremely inefficient but positive and architecture-only. This audit does not authorize extending the result to adaptive source-dependent reveals as actual model features, κ=∞, unbounded values, nonlocal side channels, deep networks, or growing architectural dimensions. A full two-resource minimax result still needs its own independently checked combination with an admissible matching upper bound and all parameter regimes.
