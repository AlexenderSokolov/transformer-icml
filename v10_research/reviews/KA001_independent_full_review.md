# KA001 — fresh independent full mathematical review

**Verdict: no substantive mathematical defect found in the frozen candidate.** The weak-certificate positive band, the strictly intermediate-curve negative band, and the strong-certificate positive band follow with the stated quantifiers and constants. This is a **partial** classification only. In particular it does not settle unrestricted full-history adaptation at beta of order 1/M or throughout the remaining range up to order M^-1/2. Root acceptance is a separate decision.

This is independent LLM mathematical corroboration, not formal verification, external peer review, or an external novelty assessment. No author proof, accepted dependency, or public repository was changed by this reviewer.

Reviewed candidate:

- `binary_certificate_adaptation_phase/KA001_certificate_phase_partial.md`
- SHA256 `5cf1f9ba5dca0e5cb7dd2a703bca163f87e46f5eb16ddf5563837d873e9072e7`

Date: 2026-11-02. The author confirmed these bytes were frozen. The reviewer independently saved `reviews/KA001_audit_snapshots/KA001_received.md`; it is byte-identical to the candidate and the author's initial snapshot. The accompanying manifest binds all actual source, receipt, review, snapshot, checker and result files used in this audit. Later changed bytes are not covered by this verdict.

## 1. Inputs read and exact inherited scope

I read the complete KA001 candidate and complete accepted BK002, AB003, SC003, BT002 main proof, BT002 scalar completion, and SC002 proof. I also read BK002's full independent review, its fixed-positive-beta provenance clarification, SC002's independent review, and the complete IU001/AU001 proofs to inspect the stationary occupation and arbitrary-start suffix interfaces. I checked the current acceptance receipts and the proof hashes they identify, including BT002's component proofs. Receipt-specified review hashes were checked where present.

The experiment inherited here has binary symbols, M>=64, beta in [0,1], integer 0<=k<=M, homogeneous second-order sources, and an all-pair-state certificate P²>=beta Pi for a hidden qualifying stationary law. The entire corrupted word is visible. A corruption kernel is offline, source-independent, and obeys a strict Hamming budget on the first M positions while preserving the final two symbols. Loss is unconditional TV at the original, preserved terminal pair. All clean and corrupted guarantees refer to this actual endpoint, not an independent query or a conditioned row sample.

SC003 supplies the binary known-k upper and BT002 supplies the matching lower; together they justify using the capped profile H_2 as the known-k benchmark. SC003's old candidate-era caveat about the missing logarithmic lower is superseded only by the separately accepted BT002 result. Its k-aware estimator is **not** used as evidence for k-blind positive results in KA001. AB003 provides consistent background on small-budget adaptation, but neither positive band is obtained by extending AB003 beyond its proved budget envelope.

The two ordinary-add-one positive results are uniform for arbitrary initial laws, hence also for stationary starts. The negative result uses stationary witnesses, hence rules out the larger arbitrary-start problem as well. These directions are not interchangeable and are correctly used.

## 2. Ordinary add-one and the weak band

Preservation of the terminal pair makes the clean and corrupted selected rows identical as row labels, though their counts can differ. Each symbol edit changes at most three triples; each triple replacement changes the complete count histogram by l1 at most two. Therefore the selected-row l1 perturbation is at most 6k. Add-one gives positive clean row mass J+2, and the elementary normalized-vector bound yields

    TV(addone_corrupted,addone_clean)<=min(1,6k/(J+2)).

This is pathwise, so it includes arbitrary history-adaptive attacks and their randomness. No IID-after-selection assertion is involved. SC003 §3 records the inherited ORIGINAL clean comparator as 8192 sqrt(32)/sqrt(M+1), which is below 2^16/sqrt(M).

The four-state universal occupation inequality and its strict-integer-threshold layer-cake consequence give

    E min(1,6k/(J+2))<=Psi(96k/(M+1)).

This works for every homogeneous pair chain and every initial law, including beta=0, unsupported starts and J=0. The scalar step to 96F_0 is valid: for z=M/k<96 the proposed right side already exceeds one; for z>=96 use monotonicity of Psi and log(z/96)<=log(1+z). Thus (2.3) follows without a mixing assumption. At k=0 the perturbation vanishes and the logarithm is correctly omitted.

For a fixed finite C>=0, D=max(1,sqrt(C)) is at least one. The band promise beta<=C/M² implies e_beta<=D/M, so

    F_2 >= (k/M)[1+log(1+z/D)].

The elementary inequality 1+z<=D(1+z/D), followed by the nonnegativity of both logarithms, gives

    1+log(1+z)
       <=1+log D+log(1+z/D)
       <=(1+log D)[1+log(1+z/D)].

Consequently F_0<=(1+log D)F_2. The final cap is legitimate: for a,b>=0 with a+b>=1, min(1,as+bF)<= (a+b)min(1,max(s,F)). This proves the displayed weak-band constant.

There is one estimator, not an estimator selected using C or beta. Only the bound's constant depends on the fixed band width C. C=0 and C<=1 are covered by D=1. A prescribed O(M^-2) curve whose band bound holds only eventually has finitely many earlier integer horizons. Those can be absorbed because risk<=1 and H_2>=M^-1/2 for M>=64. The constant can then depend on that fixed curve's finite exceptional part; the algorithm does not change.

## 3. Finite intermediate band, two different deltas, and floors

To avoid conflating the advertised certificate with the witness parameters, write

    delta_sup=sqrt(beta), k=floor(1/delta_sup),
    delta_wit=1/k.

They need not be equal. KA001 correctly retains b=delta_wit and e=1-delta_wit in the BK002 source, while evaluating the desired profile and supplied metadata at the actual beta=delta_sup².

The finite interval is nonempty exactly when M>=4096, since

    256/M²<=1/(16M) iff M>=4096.

For every beta in that interval,

    16/M<=delta_sup<=1/(4sqrt(M))<=1/4,
    k delta_sup<=1,
    k delta_sup>=1-delta_sup>=3/4.

The floor relation actually gives a strict lower bound except at harmless limiting comparisons; the stated weak inequality is safe. Also k<=M/16 and k>=4sqrt(M)-1>=2sqrt(M), so k²>=4M and k<=floor(M/8). The latter follows from the integer nature of k and k<=M/16<=M/8; no replacement of floor(M/8) by M/8 is illicit. Thus every such pair meets BK002's exact finite domain, including the smallest horizon and floor-sensitive values immediately above it.

Since k<=1/delta_sup,

    beta<=1/k².

All BK002 alternatives therefore belong to D_2(beta), because their all-state certificate 1/k² is stronger than the actual advertised one. The null's valid certificate is 1/M, also stronger than beta. Neither source needs to have its **maximal** minorization coefficient equal to the supplied number. Class membership requires a valid lower certificate, not a maximality assertion.

The source family is exactly the accepted BK002 family with a in [k/(32T),1/16], b=1/k, e=1-1/k, t=1/(4M), and its displayed stationary law. In particular it is a single stationary family over the common a parameter, not a different clean source chosen independently for each suffix length. BK002's all-sixteen-entry certificate and common-parameter integration remain applicable unchanged.

## 4. Actual public metadata and the universal-map application

The most important logical step is valid. Fix the actual supplied beta and the actual map

    A=A_(M,beta).

BK002's finite constrained-risk inequality is universal over the estimator map on complete corrupted words; its proof does not inspect the spelling of that map's public certificate label. Thus it can be applied to this fixed map. The clean risks defining S and the attacked null risk both evaluate **this same map**, supplied the same actual beta.

One may formally name it as a map at the witness's certificate for purposes of invoking the universal statement, but this does not assert an adaptation guarantee at that alternative public input. The guarantee used to bound S is solely the assumed k=0 guarantee at actual beta, licensed by D_2(1/k²) being a subclass of D_2(beta). The manuscript explains this distinction explicitly. There is no exchange of two metadata values inside a single guarantee and no forced identification beta=1/k².

The kernel is the same accepted C_(M,k): its public parameters are M,k and its only other input is the observed word plus private randomness. Choosing k for a lower-bound construction as a function of the prescribed beta does not add a runtime source-parameter port to the kernel. It remains a source-independent map, has the same definition across the entire family, compares full ordered output words, preserves the actual endpoint, and enforces its budget on every outcome. The construction uses neither the estimator's random seed nor an unknown source table.

Therefore the imported finite inequality has exactly the constants stated in (1.3): 3/2048 for the positive term and 32 for the clean-risk penalty. Its positive part is justified by nonnegativity of risk. The clean S is the supremum over the explicitly displayed stationary subfamily, which is enough for the contradiction.

## 5. Benchmark comparison and the curve-wise contradiction

Because delta_sup>=16/M, the binary cutoff e_beta equals delta_sup. The lower rounding bound k delta_sup>=3/4 gives

    F_2 <= (k/M)[1+log(7/3)] <2k/M.

For example e>1+1+1/2=5/2>7/3 proves the last logarithmic comparison without numerical approximation. The finite-domain k>=2sqrt(M) gives s<=k/(2M), so H_2<=2k/M even after taking its cap. This is the actual-beta benchmark, not the benchmark at witness certificate 1/k².

On any prescribed curve with M beta_M->0 and M² beta_M->infinity, the finite band eventually holds. The same rounding yields

    k_M/sqrt(M)>=(3/4)/sqrt(M beta_M)->infinity,
    M/k_M>=M sqrt(beta_M)->infinity.

The clean k=0 guarantee for a hypothetical adaptive family gives S<=C_curve/sqrt(M) at the same public beta_M. Dividing the penalty by the positive term gives precisely the manuscript's upper bound

    (65536 C_curve/3)(sqrt(M)/k_M)
       log(2T/k_M)/log((T+1)/k_M).

The denominator logarithm diverges because T/M->1/8 and M/k_M->infinity. The difference of its numerator and denominator logarithms is log(2T/(T+1)), which is bounded. The logarithmic ratio therefore tends to one, and the displayed error ratio tends to zero. Eventually a fixed fraction of the positive term remains.

Moreover log((T+1)/k_M)=log(M/k_M)+O(1), so the risk is eventually bounded below by a fixed positive multiple of (k_M/M)log(M/k_M). Dividing by H_2<=2k_M/M makes the risk/benchmark ratio diverge. This contradicts any finite constant, including one depending on the whole prescribed curve, and allows the estimator family itself to know that curve. The same reasoning on a subsequence is sufficient to refute a guarantee required at every horizon.

The conclusion concerns simultaneous clean accuracy and robustness across all budgets. It does not imply failure at every individual positive k, and it is not a stronger fixed-known-k minimax lower. Stationary alternatives and null already suffice.

## 6. Generic upper at K=2 and strong-band uniformity

SC002's theorem statement imposes K>=3 for its matched nonbinary frontier. It would be incorrect simply to cite that entire theorem as a binary frontier. KA001 does not do so.

I checked the upper argument itself. Its ingredients are the normalized count perturbation, the ORIGINAL clean comparator, IU001 Lemma 4.1's stationary clipped reciprocal, the universal occupation inequality, and AU001's exact suffix-mixture argument. IU001 and AU001 explicitly permit K>=2; their relevant occupation statements are in fact finite-state-chain statements with d<=K². No step of this upper proof needs a third symbol.

In the arbitrary-start step, all-state minorization makes the residual two-step matrix stochastic even outside stationary support. Applying the ordinary P path-extension kernel to the mixture of suffix initial laws gives a mixture of **whole suffix trajectories**. The residual trajectory still uses P, not the residual matrix. Its terminal query is its actual endpoint, and its row count is bounded by universal occupation. The full count dominates the suffix count. Thus the transfer is valid for arbitrary starts without an additive burn error or an illegal conditional stationary argument. Beta=1 omits the residual; beta=0 uses the universal branch. K=2 causes no exception.

At K=2 the statistical constant 8192*2^(5/2) is below 2^16, and the corruption constant

    48(17+log80)+960

is below 2^12. Hence the exact upper interface (5.1) follows. The K>=3 restriction enters SC002's three-symbol matching lower only; that lower is not used here. BK002's provenance clarification is consistent with this independent inspection.

For k>=1, log(1+u)<=u gives

    F_gen<=(k/M)+1/[M max(beta,1/M)].

Under the fixed promise beta>=c/sqrt(M), its second term is at most s/c. The clean branch handles k=0 separately. Since F_2>=k/M, H_2 dominates the capped max(s,k/M); applying the cap as in the weak proof gives the stated constant 2^16+2^12+2^12/c.

The constant may depend on the fixed c>0 but not on M,beta,k within that band. It is one ordinary-add-one estimator, independent even of c. Large c simply makes some small-M parameter bands empty; there is no contradiction. The proof does not establish a uniform constant over c tending to zero with M, nor does it classify the gap merely because the generic upper becomes loose there.

## 7. Power laws and deliberately unresolved scope

For beta_M=M^-gamma, the table follows exactly:

- 0<=gamma<=1/2 is in the strong positive band;
- 1<gamma<2 satisfies both negative-curve limits;
- gamma>=2 is in the weak positive band;
- 1/2<gamma<=1 is not settled here.

Fixed positive multiplicative factors can be incorporated in fixed c or C at the positive endpoints; the two strict negative limits are unchanged in the open interval. As throughout the experiment, certificates must be in [0,1]; an inadmissible factor at gamma=0 is not a new source class.

The beta≈1/M full-history question remains open. BK001's obstruction is for histogram-plus-initial/final-pair information and is not promoted to a full-history lower. BK002's uniform-in-beta impossibility is not promoted to failure on every single prescribed curve. The result is nonmonotone in the certificate only relative to a known-k benchmark that itself changes: weak certificates make the benchmark larger. No claim of intrinsically easier estimation from less mixing follows.

No efficient or causal attack, visible mask or attack seed, editable endpoint, neural-resource, training, external novelty, formal-verification, or publication conclusion follows. These restrictions are correctly preserved.

## 8. Independent exact diagnostics and artifact status

The reviewer wrote `reviews/KA001_independent_exact_checks.py` independently, without reading or importing the author checker. The author later communicated aggregate diagnostic counts; those were not used as mathematical evidence or as code input. The reviewer checker constructs pair transition matrices from successor-bit probabilities rather than copying the displayed squared matrix.

The completed run produced `reviews/KA001_independent_exact_checks.json` and passed **413,327 assertions**. Every assertion uses exact integers or rational arithmetic. Logarithmic scalar assertions use rational upper/lower intervals from the positive atanh series after binary range reduction, with an explicit geometric remainder bound. Floating-point values occur only in illustrative curve output, not in pass/fail decisions.

The checks include:

- 49,194 distinct finite-band (M,beta,k) cases, including all integer horizons 4096 through 12288 at several rational beta locations, every intersecting inverse-square floor cell at selected horizons, and very large representative curve points;
- exact k=floor(beta^-1/2), k delta_sup>=3/4 (squared), k²>=4M, k<=floor(M/8), k<=M/16, class inclusion, cutoff selection and positive logarithm arguments;
- 411 stationary witness cases, including 366 where the actual beta is not 1/k²;
- 6,576 exact witness-certificate entries and another 6,576 exact actual-supplied-beta certificate entries;
- 1,644 stationarity equations and 2,192 null-certificate entries;
- clean/generic/constrained-risk constants, the weak-band logarithmic comparison, universal Psi comparison, and strong-band scalar absorption;
- exact accepted-proof/component/review hash checks where specified by the receipts, and unchanged candidate/snapshot checks at both ends of the run.

The representative curve outputs illustrate differing rates of approach; they are not substitutes for the universal limit argument in §5. All finite diagnostics corroborate only their tested instances. They do not formally verify the common-map quantifiers, asymptotic argument, or arbitrary-start analytic interfaces; those were separately reconstructed in this review.

No substantive revision is requested. The verdict applies only to the frozen hash above and only to the partial weak/intermediate/strong regime claims. Root should retain the unresolved critical range and the distinction between full-history and histogram-only obstructions in any acceptance or user-facing summary.
