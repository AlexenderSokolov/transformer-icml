# AB003 — Independent full mathematical review

2026-11-02. **Verdict: PASS, including the sharp range-envelope corollary in §8. No mathematical revision required.** This is a fresh independent LLM review and exact finite diagnostics, not formal verification, external peer review, or a novelty claim.

## 1. Version and dependency binding

Reviewed complete author file: `AB003_small_budget_hard_threshold.md`, SHA256
`fe3260f31f76a99576897d931e23ab939e0ebf8eb04e8cf31591b2b908d392e8`.

I read §§1–7, independently rederived the new perturbation and threshold steps, then read and audited the subsequently appended §8. The final checks bind the complete version above. I also read the relevant SC003 interfaces, the complete BIF001 and BAI003 v2 files, their matching acceptance receipts, and the accepted AB001 theorem/receipt used in §8.

Exact inherited files:

- `binary_source_corruption/SC003_theorem.md`: `4235fc6b9de9d04368354d22f15774d66965ca572f21f197e456537e9bcba837`.
- `binary_all_start/BIF001_binary_all_initializations_frontier_v1.md`: `35c6cb3b5c882c9e70dad68dbc8492c08e65ba49f532da84597e5e1e303467f0`.
- `binary_arbitrary/BAI003_uniform_absorbing_binary_upper_v2.md`: `99d209c423664c3fe74d1b32fd68fb89ed31218c58fa2f11c343c3e6a54bd0e4`.
- `binary_budget_adaptation/AB001_joint_blindness_obstruction.md`: `865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d`.

This review audits the new composition and the exact domains of the imported inequalities. It does not claim to newly formally certify every predecessor theorem in the inherited dependency chain.

## 2. Accepted result and limits

For M>=64 and every integer k<=floor(sqrt(M)), the hard-threshold count estimator with B=12ceil(sqrt(M)) is independent of both k and beta and satisfies (AB3), uniformly over all beta and every initial pair law. It therefore attains the accepted known-k minimax order simultaneously over that entire budget range, under both initialization conventions.

The sharp corollary is also valid: for a fixed public budget envelope b_M, uniform joint-blind adaptation over all 0<=k<=b_M exists if and only if b_M=O(sqrt(M)); the universal-in-M,beta,k risk constant may depend on that fixed envelope bound. This is not a pointwise impossibility at every larger budget, and it does not resolve supplied-beta unknown-k adaptation for all budgets.

## 3. Estimator and pathwise perturbation

The orientation is exactly the accepted designated exit, the complement of the first context bit. It does not require identifying a source-dependent minority. The active branch has C'>B and J'>=C'>0, so its ratio is defined; the inactive branch is a legal binary probability vector. Only corrupted counts, the protected terminal pair, and M are used.

The whole-histogram l1 perturbation <=6k implies both scalar count bounds used in the proof. The budget range gives d=6k<=B/2. On the active branch this forces C>B-d>=B/2>=d and hence J>0.

I independently obtained the normalization identity bound

    |C'/J'-C/J| <= (|C'-C|+p'|J'-J|)/J <=2d/J.

The two cases J>=2d and J<2d yield p'<=4p. Since both frequencies are nonnegative, |p'-p|<=max(p',p)<=4p. The Lipschitz step then gives

    |p'-q|<=5|p-q|+min(4q,2d/J),

and the final conversion to 4min(q,6d/(J+2)) is conservative and valid for every J>=1. At d=0 the same statement is immediate and no singular division is introduced.

On the inactive branch, C<=3B/2. If J>3B/q and q>0, p<q/2 and q<=2|p-q|. Otherwise the threshold-bias term pays the loss. J=0 and q=0 are explicitly treated and do not require an empirical frequency or a q-dependent division to be evaluated. These arguments establish (3.1) with all stated edge cases.

## 4. No-log hard-threshold accounting

The proof correctly does **not** substitute the random selected-row threshold into an unconditional tail inequality. For each fixed state u, q_u is a fixed source parameter and w_u=floor(3B/q_u)+1 is a fixed integer. The event with terminal row u is contained in {J_terminal<w_u}; hence its weighted probability is bounded by 16(3B+q_u)/(M+1). Summing four separate bounds yields 64(3B+1)/(M+1).

Zero-probability rows contribute zero and never need a threshold. The bound remains valid when an intermediate probability upper bound exceeds one. The calculation B<=27sqrt(M)/2 and 3B+1<=325sqrt(M)/8 for M>=64 is correct, giving 2600/sqrt(M). This is a genuinely no-log threshold-bias bound and uses no terminal-conditioned IID assertion.

A soft subtraction estimator would have a different residual bias; the manuscript correctly identifies that its new proof is specific to hard thresholding.

## 5. Imported occupation and clean-comparator domains

SC003 §3 supplies the clean empirical-row comparator after comparing it with original clean add-one. The undefined J=0 frequency is excluded by the indicator, and the universal reciprocal occupation estimate pays the smoothing difference. The coefficient (8192+1)sqrt(32) is the exact interface used here.

BIF001 §3 equation (3.4) is an occupation statement for arbitrary A0>0 and arbitrary initialization, not merely a quantized-encoder theorem. Its fixed weights are (a,b,e,t), precisely the present orientation. Its assumption beta M^2>=1 with full stationary support is exactly the strong case in AB003. Its diagonal-start and crossing-start composition also covers every suffix horizon involved; no global sqrt(beta) mixing assertion is imported.

For positive beta, the support classification is exhaustive: positive crossing mass forces all four stationary masses and all designated exits positive, whereas zero crossing mass leaves one absorbing diagonal. BAI003 v2 §6 then gives the displayed occupation bound for arbitrary remaining rows and arbitrary initial states, including transient or unsupported starts. Its symbol-exchanged version retains the same public orientation. The v2 horizon correction is irrelevant to the stated M>=64 domain but is present in the accepted dependency.

For beta<M^-2, the universal four-state layer-cake bound applies without any support assumptions. The equality beta=M^-2 is handled by one of the positive-beta support cases. A=36k is legal whenever k>=1; A=0 at k=0 is not inserted into a positive-A logarithmic interface.

The arithmetic is correct:

    16672*36=600192,
    256*36+16=9232,
    16*36=576.

Monotonicity of the logarithm when A>=k gives the claimed F_2 comparison. The weak-case scalar split at 576 is valid, including the capped branch. Thus the uniform bound (5.6) follows within the inherited hypotheses.

## 6. Assembly, endpoints, and computation

The statistical and corruption coefficients are below the claimed powers of two. In particular,

    5*8193*sqrt(32)+2616 <2^18,
    4*600192=2400768<2^22.

At k=0 the occupation term vanishes but the clean hard-threshold bias is still covered. Unit TV gives the cap. The accepted BT002 lower is a known-k lower; imposing joint blindness cannot invalidate it, and the same new estimator supplies the simultaneous upper.

Exact integer square-root computation and count scanning are sufficient. No approximate real computation is needed for the rational output. The conservative bit bounds are consistent with counting, input retention, threshold computation, and serialization; they are sequential full-history costs, not neural-depth claims.

## 7. Fresh audit of §8: sharp adaptive range envelope

### Sufficiency

For fixed integer L>=1, B_L=12Lceil(sqrt(M)) gives d<=B_L/2 whenever k<=Lsqrt(M). The pathwise argument and weighted-occupation terms are unchanged. The sole altered contribution is the threshold bias, bounded by 2600L/sqrt(M), since 3B_L+1<=L(3B+1). Absorbing the unchanged statistical constants into 2^18 L is valid. This proves the stated uniform-in-M,beta,k bound for every envelope bounded by Lsqrt(M).

The estimator may be designed using this fixed public envelope bound; it still receives neither the actual k nor beta. If the envelope is merely O(sqrt(M)) asymptotically, the finitely many remaining M values have finite ratios because b_M<=M, so the global supremum is finite as stated.

### Necessity

For an unbounded envelope ratio, choose M_n tending to infinity with b_(M_n)/sqrt(M_n) tending to infinity. Both terms in

    k_n=min{b_(M_n),floor(M_n^(3/4))}

have ratios to sqrt(M_n) tending to infinity. Also k_n<=floor(M_n/8) eventually and log(M_n/k_n)>=one-quarter log(M_n). Thus accepted AB001 applies on the same estimator map that must also meet the k=0,beta=0 clean guarantee.

Dividing its negative coefficient by its positive coefficient gives exactly

    (8192C/9)(sqrt(M_n)/k_n)
       log(2T_n/k_n)/log((T_n+1)/k_n).

The logarithm ratio tends to one: the numerator minus denominator is log(2T_n/(T_n+1)), a bounded quantity, while the denominator diverges. Therefore the clean penalty is negligible. The resulting risk is a positive fixed multiple of (k_n/M_n)log(M_n/k_n), whereas the beta=1/M_n profile is <=2k_n/M_n. This contradicts one finite uniform C.

AB001 uses stationary witnesses, so this necessity holds already under stationary initialization; the new sufficiency holds for arbitrary starts. The proof correctly avoids a false pointwise claim at k comparable with M, where the profile is already constant.

## 8. Independent finite diagnostics

I wrote and ran `review_ab003_checks.py`, producing `review_ab003_checks.json` with PASS, using exact integer and rational arithmetic throughout:

- 26,292 admissible relaxed count configurations, including 7,440 scaled-envelope configurations;
- 88,156 critical-probability checks of the new pathwise inequality, including threshold right limits;
- 3,472 active and 22,820 inactive configurations;
- 61,864 fixed-row threshold-floor inequalities;
- 99,937 finite-M constant checks, covering every integer M from 64 through 100000;
- exact assembly coefficients and the §8 penalty-ratio coefficient.

The count configurations obey weaker scalar perturbation constraints than actual edited words, so they check the stated deterministic reduction without assuming special word feasibility. The tested q values include all piecewise-linear breakpoints for each configuration and the only threshold right limit. The universal proof above remains necessary; finite diagnostics alone do not establish the infinite theorem. The JSON binds the current author proof and exact inherited source versions. Root acceptance remains separate.
