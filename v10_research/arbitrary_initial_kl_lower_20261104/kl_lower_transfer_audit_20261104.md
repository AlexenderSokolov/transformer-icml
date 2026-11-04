> Public-export notice: this is a privacy-screened derivative of the dated analytical preparation. Its historical no-upload/no-mutation statements describe preparation, not this later publication. Mathematical claims and original scientific hashes are preserved. See [public export](../../provenance/arbitrary_initial_kl_lower_20261104/PUBLIC_EXPORT.md) and [public source map](../../provenance/arbitrary_initial_kl_lower_20261104/PUBLIC_SOURCE_MAP.json) for current public identities.

# Independent analytical audit: MM5 to terminal forward KL

Date: 4 November 2026 (UTC).

## Finding

The transfer is valid. For every integer A >= 2 and n >= 1, in the full class of homogeneous second-order A-symbol sources with arbitrary initial-pair distributions,

    R_KL(A,n) >= 2 R_TV(A,n)^2
               >= 2^(-31) min{1, A^5/(n+1)}.

Both risks use the same full observed history X_1,...,X_(n+2), the same actual terminal pair Y_n=(X_(n+1),X_(n+2)), and an infimum over all common, possibly randomized, probability-vector predictors. KL uses natural logarithms and has true-row-to-prediction orientation. The equality sign between the intermediate risk expression and the explicit constant would be incorrect: the second relation is another lower bound.

This is a lower bound for a supremum over initial laws and kernels. It does not give a lower bound for each prescribed initial law, every fixed deterministic initial pair, every fixed source, or one source simultaneously for all n and all predictors.

The current direct MM5 source supports its explicit constant, including odd alphabet group sizes and all finite n. Its sole inherited small-alphabet interface can be replaced by the elementary argument below. The old review's different proof hash remains unresolved and must not be represented as a byte-level review of the currently readable source.

## 1. Scope and materials directly inspected

This audit read the full current MM5 proof and independently checked the construction, indexing, full-history law, testing argument, constants, and KL transfer. It read the existing direct-source review and its separate odd-group correction, but does not use those reviews in place of the proof. It compared the statement of the new add-one upper bound and checked the relevant primary HJW theorem statements. It did not reprove the entire add-one upper-bound argument or every HJW proof step.

No mathematical numerical test, simulation, enumeration, training, external upload, or repository mutation was performed. Reading files and computing their cryptographic identity are not mathematical numerical experiments. This is a separate-context LLM analytical review, not formal verification, external human peer review, cross-model certification, or novelty clearance.

Directly inspected original MM5 source:

    MM5-proof.md [original preparation locator omitted; public scientific-copy link is listed below]
    SHA-256: 19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3

Compared upper-bound source:

    v10_research/fixed_alphabet_kl_sharpening_20261103_2346/tilted_occupation_terminal_kl.candidate.v1.md
    SHA-256: c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281

Public provenance was read at repository commit 0d678eefb558d5108dd5ef893b033c6f58077d81:

- [Alphabet-stage index](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/provenance/t1t2_alphabet_limits_20261103/INDEX.html).
- [Original/export map](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/provenance/t1t2_alphabet_limits_20261103/SOURCE_EXPORT_MAP.json).
- [Current-source analytical trace](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/v10_research/minimax_alphabet_bounds_20261103_1706/r011_mm5_trace_independent_review_20261103_1721.md).
- [Odd-group correction](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/v10_research/minimax_alphabet_bounds_20261103_1706/r011_mm5_odd_alphabet_correction_20261103_1732.html).

## 2. Exact observation experiment and minimax quantifiers

Write Theta_A for all stochastic A^2-by-A second-order transition tables, including zero entries, deterministic rows, reducibility, and periodicity. Let mu range over all initial-pair distributions. The table remains fixed during an experiment. A predictor Q maps the entire observed history H=X_1^(n+2) into a probability distribution on the A-symbol simplex; the conditional output kernel must be common to all hidden (theta,mu). It may depend on the public A,n and use source-independent randomness.

For L equal to TV or forward KL, define

    R_L(A,n) = inf_Q sup_(theta,mu)
        E_(theta,mu,Q) L(theta_(Y_n), Q(H)).

TV is half the L1 distance. The source can vary with the public horizon in the supremum and can be selected adversely to the predictor. The experiment does not supply the unobserved X_(n+3), an independent query, stationary initialization, or the hidden source parameters to Q.

The MM5 source uses K=A and M=n. Its auxiliary training-block count is floor(n/m^2), not the global observed-transition count n. Keeping these two indices separate prevents an off-by-one or effective-sample-size error.

## 3. Independent check of the large-alphabet MM5 construction

For A >= 12, put m=floor(A/4), L=m^2, b=floor(m/2). Four disjoint m-symbol groups C,U,V,W fit inside the original alphabet. A directed Euler cycle on C supplies a cyclic word whose consecutive pairs enumerate C^2 exactly once. The clock uses these ordinary pair states, not an external hidden state or a time-varying transition rule.

Replacing five clock transitions by a U choice, a V choice, an unknown W-valued emission, and two deterministic return transitions preserves an exact cycle length L. The table assigns nonconflicting stochastic rows to the disjoint symbol-group pair types and defines all remaining rows. The known return path is independent of the unknown emitted symbol after its deterministic copies have been observed. Strict positivity within W gives a common support, including the odd-m leftover symbol.

For each global n, the six listed initialization cases align the terminal phase with U x V. This initialization depends only on A,n, not on hidden sign bits. If q=floor(n/L) and d=n mod L, the unknown departures occur at d,d+L,...,d+(q-1)L, while d+qL=n is the actual terminal pair and has not departed. This holds for n<L and the initial phases carrying fixed W symbols; those fixed symbols are not unknown-row samples.

There is a source-independent bijection between the entire observed history and q training triples D_1,...,D_q together with the actual terminal pair T. The full path law is

    m^(-2(q+1)) product_(i=1)^q q_sigma(Z_i | U_i,V_i).

Consequently, the training triples are iid, the actual T is uniform on U x V and independent of those triples, and the same law remains available after conditioning on T=s. This is an exact property of this hard family. It does not assert conditional iid sampling under arbitrary adaptive row visits in a general Markov source, nor does it discard informative parts of the history.

For a single hidden sign flip, the full-history KL and its T=s conditional version equal

    (2 q alpha / m^3) log((1+alpha)/(1-alpha)).

With alpha=min{1/2, sqrt(m^3/(q+1))/8}, both branches give KL <= 1/8 and hence adjacent-history TV <= 1/4. Every common randomized predictor induces a common randomized sign test. Pairing the same finite hypercube prior gives average bit error at least 3/8. One wrong bit incurs at least alpha/m in terminal TV. There are b disjoint successor pairs, so averaging over actual contexts gives

    average risk >= 3 alpha b/(8m) >= alpha/8,

because b/m >= 1/3 for every integer m >= 3. For odd m, the unmatched W symbol has mass 1/m and carries no bit. Thus the 1732 correction repairs the later review's phrase “m/2 pairs”; the original source and its constant are already correct.

The resulting bound is at least (1/64) min{1,sqrt(m^3/(q+1))}. If q=0 this is at least 1/64. If q>=1, then q+1<=2n/m^2 and m>=A/8, giving

    m^3/(q+1) >= A^5/[256^2(n+1)].

Thus the large-alphabet argument actually gives the conservative lower constant 2^(-14), which dominates the submitted 2^(-16) constant. No asymptotic approximation is needed.

## 4. Independent small-alphabet completion

The current MM5 source inherits an older iid interface for 2<=A<=11. To avoid depending on an unavailable earlier proof, let N=n+2 and delta=1/(8 sqrt N). Use two iid Bernoulli sources p_+=1/2+delta and p_-=1/2-delta, with their iid initial-pair laws, embedded in the A-symbol alphabet. All transition rows equal the corresponding Bernoulli law; unused alphabet coordinates have zero mass.

The Bernoulli KL is at most its chi-squared divergence. Therefore the KL of the full N-symbol history is at most

    N * 16 delta^2/(1-4 delta^2)
      = (1/4)/(1-1/(16N)) <= 4/15.

Its TV is at most sqrt(2/15)<1/2. On the common overlap of the two history laws, the triangle inequality for TV gives, for every possible predicted A-vector, a sum of the two losses at least TV(p_+,p_-)=2delta. Integrating the same output kernel on that overlap yields

    max{risk_+,risk_-} >= delta(1-TV(history_+,history_-))
                      >= 1/(16 sqrt N).

This argument directly handles arbitrary randomized predictions and does not require renormalizing their mass on the binary support. Since N<=4(n+1) and A^5<=11^5<2^18, it dominates 2^(-16) min{1,sqrt(A^5/(n+1))}. This closes every finite small-A case without claiming to recover the old iid Fact's original bytes or review history.

## 5. Transfer to expected forward KL

For all probability vectors p,q, with natural logs and extended-real KL,

    D_KL(p||q) >= 2 TV(p,q)^2.

If q_b=0<p_b for any b, the left side is infinite and the inequality is automatic. If p_b=q_b=0, the term is conventionally zero; if p_b=0<q_b it also contributes zero. In the remaining finite case, the usual log-sum reduction and binary convexity proof applies on the support and by boundary limits. No full-support restriction on the predictor is needed.

Fix Q and a source s=(theta,mu). Pinsker followed by Jensen gives

    E_s D_KL >= 2 E_s TV^2 >= 2(E_s TV)^2.

This remains valid when the KL expectation is infinite. Let t_Q=sup_s E_s TV, which lies in [0,1]. Monotonicity and continuity of squaring imply

    sup_s E_s D_KL >= 2 sup_s(E_s TV)^2 = 2 t_Q^2.

Taking infimum over the same Q class gives

    R_KL >= 2 inf_Q t_Q^2 = 2(inf_Q t_Q)^2 = 2 R_TV^2.

There is no minimax interchange. The existence of an attaining source or an attaining optimal predictor is not needed. Applying the verified MM5 bound and squaring its nonnegative truncated expression gives exactly

    R_KL(A,n) >= 2^(-31) min{1,A^5/(n+1)}.

## 6. Comparison with the current add-one upper

The compared source states, for K_n=1+floor(log_2 n),

    sup_(theta,mu) E D_KL(theta_(Y_n)||B_(Y_n))
      <= min{log(n+A), W_(A,n)},

    W_(A,n) = A^4[log A + 1536 A K_n]/(n+1).

Conditional on the separately reviewed upper theorem, the minimax risk therefore satisfies

    2^(-31) min{1,A^5/(n+1)}
      <= R_KL(A,n)
      <= min{log A, W_(A,n)}.

The extra log A minimax cap comes from the always-uniform predictor. It must not be presented as an unproved log A cap on add-one itself. The A^5 power in the nontruncated lower term is unavoidable for the full arbitrary-initialization class. This sandwich leaves a logarithmic gap in general growing-alphabet regimes and does not prove a constant saturation value when A^5/n is large.

For a sequence of alphabets, KL consistency requires A_n^5/(n+1)->0. The displayed upper bound supplies the sufficient condition A_n^5 log(n+2)/(n+1)->0. These are different conditions. TV consistency and its exact threshold cannot be reversed through Pinsker to establish an exact KL consistency threshold.

## 7. Distinction from HJW

[Han–Jana–Wu, Theorem 22 and Section 5.1](https://arxiv.org/html/2106.13947v2) concern stationary higher-order sources and actual-terminal forward KL. With observed-symbol length N=n+2 and order m=2, their lower bound is A^3/[C_2(n+2)] times log((n+2)/A^3), in the regime A<=(n+2)^(1/3)/C_2. Theorem 24 explicitly covers binary second-order chains. Thus fixed-A logarithmic sample-length optimality is a separate existing result, while the MM5 transfer shows an arbitrary-initialization A^5 obstruction. Their stationary A^3 upper bound is not an arbitrary-initialization upper bound and creates no contradiction. The stationary lower can be combined with MM5 by taking the maximum in its valid regime; it does not supply a growing-A A^5 logarithmic lower factor. No priority claim follows from this comparison.

## 8. Provenance limitations that remain

The old MM5 report records proof hash 5fef432092c4d7394021f1651dbcd086b660028b2a62c1297342340892dd6d24, whereas the directly inspected original is 19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3. This audit does not resolve that discrepancy or claim it is mere wrapping. The old report is not used to establish that it reviewed the current bytes.

The 1721 direct-source review's original hash is c0f503d24a2fa1b590b85bf23ee3daf62d51d5d64bcdccfe7a57bc60769507fd; its public export is 6e12f01bf32241526e552f7a3621d1d34c7234274d2a0efd5969c4f9bbe9e425, with the difference documented in the export map. The separate 1732 correction is byte-identical in the public map, hash 281e8225a24fc29929f0f1df6bea1eeac88f8ebaad116452fb3e1a08f04175cb. Original and public-export identities must remain separate.

The public MM5 scientific copy has hash 4d5e865ebe00846662cef1830be02bf52cc2b839eca8a0600f8baa501ada6078 according to the stage index and earlier copy map; it is not the original 19d2 file. This audit's primary mathematical review used the latter original directly. A provenance map or hash check establishes identity, not mathematical truth. The direct analysis above supplies the new review, while the historical identity gap remains disclosed.

## Safe summary

The existing actual-terminal TV lower bound rigorously transfers to an all-finite-parameter expected forward-KL lower bound 2^(-31) min{1,A^5/(n+1)} for the same common randomized predictors and full arbitrary-initialization source class. Together with the separately reviewed add-one upper, it establishes an unavoidable A^5 obstruction but not the exact growing-alphabet logarithmic factor, saturation law, or KL consistency threshold.
