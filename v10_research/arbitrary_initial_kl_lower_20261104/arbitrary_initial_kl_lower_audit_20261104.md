> Public-export notice: this is a privacy-screened derivative of the dated analytical preparation. Its historical no-upload/no-mutation statements describe preparation, not this later publication. Mathematical claims and original scientific hashes are preserved. See [public export](../../provenance/arbitrary_initial_kl_lower_20261104/PUBLIC_EXPORT.md) and [public source map](../../provenance/arbitrary_initial_kl_lower_20261104/PUBLIC_SOURCE_MAP.json) for current public identities.

# Audit: MM5 implies an arbitrary-initialization A^5 terminal-KL lower bound

Date: 4 November 2026, UTC. Analytical source audit only. No numerical tests, simulations, uploads, or repository mutations were performed.

## Finding

The implication is valid, with an explicit universal constant. Let A>=2 and n>=1 be integers, observe X_1,...,X_{n+2} from a homogeneous second-order source, and evaluate the next-symbol prediction at the actual terminal pair Y_n=(X_{n+1},X_{n+2}). All transition rows and all initial pair distributions are allowed. Define

    R_KL^all(A,n) = inf_Q sup_(theta,mu) E D_KL(theta_{Y_n} || Q(X_1^{n+2})).

The infimum is over common measurable probability-vector predictors, including source-independent randomization. Natural logarithms are used. Then the inherited MM5 theorem implies

    R_KL^all(A,n) >= 2^(-31) min{1, A^5/(n+1)}.       (KL-MM5)

This supplies the polynomial A^5 lower factor missing from the recent synthesis. It matches the reviewed arbitrary-start add-one upper bound in its polynomial alphabet dependence, up to a logarithmic factor. It does not determine the sharp logarithmic factor or the full joint-(A,n) minimax rate.

## 1. Exact conversion, including quantifiers

For any distributions p,q, Pinsker with half-L1 TV and natural logarithms gives

    D_KL(p||q) >= 2 TV(p,q)^2.

If q vanishes where p is positive, the left side is infinite and the inequality remains true. No positivity restriction on predictions is needed for the lower bound. For every fixed predictor Q and every fixed source lambda=(theta,mu), expectation over both history and its independent random seed, followed by Jensen, gives

    R_KL(Q,lambda) >= 2 E[TV(Q,theta_{Y_n})^2]
                       >= 2 R_TV(Q,lambda)^2.

Consequently

    sup_lambda R_KL(Q,lambda)
      >= 2 [sup_lambda R_TV(Q,lambda)]^2.

Taking the infimum over the same predictor class preserves this direction. The square is increasing and continuous on nonnegative reals, so

    R_KL^all(A,n) >= 2 [R_TV^all(A,n)]^2.

MM5 gives R_TV^all(A,n)>=2^(-16)min{1,sqrt(A^5/(n+1))}; squaring yields (KL-MM5). Alternatively, fix an arbitrary Q, use MM5's finite-family witness for that Q, apply the first displayed expectation inequality there, and only then take the predictor infimum. This avoids any assumption that the full source supremum is attained.

There is no exchange of infimum and supremum. The hard source may depend on A,n and Q; a single source is not claimed to defeat every predictor. This is a lower-bound implication from TV to KL, not the invalid reverse-Pinsker upper-bound inference. Restricting Q to strictly positive outputs or any specified algorithm subclass cannot evade this minimax lower bound.

The observation set is finite for each A,n. Deterministic history-to-simplex functions are measurable, and the stated common randomized probability kernels give measurable coordinate-order tests and loss expectations. No computational or network-realizability assumption enters.

## 2. MM5 original-proof audit

The complete readable MM5 proof was read, including Sections 1-9. Its exact source variables are K=A, M=n, N=M+2=n+2. Its denominator M+1 is therefore n+1, not n+2. The domain is every integer K>=2, M>=1; there is no large-sample, divisibility, or even-alphabet restriction.

For K>=12, m=floor(K/4)>=3, L=m^2, and b=floor(m/2). Four disjoint m-symbol sets C,U,V,W fit within the original K-symbol alphabet. A finite Euler cycle on C lists all m^2 ordered C-pairs, including loops. The substitutions into that cycle define a complete homogeneous second-order table and obey the pair shift (a,b)->(b,c). Unused rows and leftover alphabet symbols are also assigned valid distributions. There is no external clock or uncharged hidden state.

One period has length L and only one U x V departure with an unknown W-valued label. Each unknown row has b disjoint perturbed coordinate pairs. If m is odd, the remaining W-coordinate has probability 1/m and carries no hidden bit. Hence b/m>=1/3 for every m>=3, including m=3.

Writing M=qL+d, 0<=d<L, the proof explicitly chooses a legal initial pair law for each of the six possible phase classes so that the actual terminal pair is a U x V context. This initial law depends on the public K,M but is common to all hidden sign vectors. The source table is fixed within every experiment. This is allowed by the per-horizon supremum over initial distributions; it would not justify a lower bound for each prescribed initial law.

The observed unknown-row departures occur exactly q=floor(M/L) times. The terminal context is the next context, whose outgoing label is not observed. The complete observed history is in a source-independent bijection with q training triples D_i=(U_i,V_i,W_i) and the actual terminal pair T. Its exact path probability is

    m^[-2(q+1)] product_(i=1)^q q_sigma(W_i | U_i,V_i).

Thus the training triples are iid in this particular hard family, and the actual terminal pair is uniform and independent of them. T is not an extra independent test point substituted for the terminal context. The bijection accounts for all clock symbols and initial coordinates, including phases 1-4 and q=0; no potentially informative observations have been dropped.

For one flipped row-coordinate-pair bit, the full-history KL, also conditional on any actual T=s, equals

    (2q alpha/m^3) log[(1+alpha)/(1-alpha)].

With alpha=min{1/2, sqrt[m^3/(q+1)]/8}, both branches bound this by 1/8. The testing argument handles randomization and ties, uses one common finite prior over all bits, and yields risk >=3 alpha b/(8m)>=alpha/8. Consequently

    R_TV >= (1/64) min{1,sqrt[m^3/(q+1)]}.

For q>=1, q+1<=2M/m^2 and m>=K/8 give

    m^3/(q+1) >= K^5/[256^2(M+1)].

For q=0 the proof uses a separate constant lower bound. The large-K argument therefore actually has slack relative to the declared global constant 2^(-16).

For 2<=K<=11, the predecessor's Section 13.3 was read directly. It uses iid Bernoulli rows p_+=1/2+1/(8sqrt N), p_-=1/2-1/(8sqrt N), with iid initial pairs and zero embedding in the remaining symbols. The N-symbol history laws have TV<1/2; triangle inequality over their common part gives worst expected terminal TV >=1/(16sqrt N). This holds for every common randomized full-history predictor without the implementation interface I. The explicit comparison in MM5 covers every small K and M, including saturation. This resolves MM5's sole inherited small-alphabet interface.

## 3. Correction and source provenance

Public immutable snapshot: 0d678eefb558d5108dd5ef893b033c6f58077d81 in AlexenderSokolov/transformer-icml.

- [Public scientific proof](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/inherited_statistics/DOT_conditions_stage02/inherited/MM5_statistical_proof.md), blob d8aef0a80a3dd33a01dba631a454d4fccf4ffda1. It retains the complete statistical argument, removing historical/process material. The public scientific copy has SHA-256 4d5e865ebe00846662cef1830be02bf52cc2b839eca8a0600f8baa501ada6078.
- [Full fact snapshot](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/v10_intake/source/sources/euler-stage6/facts/946d42d5bf502eb4.md) includes frozen statement, contract and proof. The historical heading calls the submitted statement a candidate; the later proof/review evidence must be distinguished from that frozen heading.
- [Direct trace review](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/v10_research/minimax_alphabet_bounds_20261103_1706/r011_mm5_trace_independent_review_20261103_1721.md) directly checks the readable original proof.
- [Odd-m correction](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/v10_research/minimax_alphabet_bounds_20261103_1706/r011_mm5_odd_alphabet_correction_20261103_1732.html) corrects the trace review's phrase "m/2 pairs" to floor(m/2). The original MM5 already used floor(m/2) and b/m>=1/3. Thus this correction does not change MM5's bound.
- [Small-K predecessor](https://github.com/AlexenderSokolov/transformer-icml/blob/0d678eefb558d5108dd5ef893b033c6f58077d81/v10_intake/source/sources/euler-stage6/facts/a12539a93d9f1ee3.md), Section 13.3.

The readable original source is MM5-proof.md [original preparation locator omitted; public scientific-copy link is listed below], SHA-256 19d2b5e4d5a5c7c5f152f14b287bd42a5f130de4428c82f82e1a5916fe9400f3, independently rehashed here. The old MM5-independent-report.json quotes an earlier proof hash 5fef4320..., not this hash. The public trace properly discloses that discrepancy. Do not claim that the old report directly certifies byte-identical review of the readable 19d2... version. This audit read the latter directly and checked the current correction.

## 4. Comparison with the reviewed arbitrary-start add-one upper

The reviewed source v10_research/fixed_alphabet_kl_sharpening_20261103_2346/tilted_occupation_terminal_kl.candidate.v1.md has SHA-256 c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281. Its exact-file independent review records PASS for Sections 1-7. The source and review were read here; the present audit is not represented as a new complete upper-proof certification.

For B_s(b)=(C_{s,b}+1)/(J_s+A) and K_n=1+floor(log_2 n), that theorem gives

    sup_(theta,mu) E D_KL(theta_{Y_n}||B_{Y_n})
      <= V(A,n)
      = min{log(n+A), A^4[log A+1536 A K_n]/(n+1)}.

Both bounds use the same source class, all n observed departures, the same complete history, the same actual terminal pair, and the same forward-KL loss. The upper estimator is common and requires no hidden parameters. Therefore

    2^(-31) min{1,A^5/(n+1)}
      <= R_KL^all(A,n)
      <= sup_(theta,mu) E D_KL(theta_{Y_n}||B_{Y_n})
      <= V(A,n).

Since log A<=A and K_n>=1, the second upper branch is at most 1537 A^5 K_n/(n+1), uniformly for all integer A>=2,n>=1. Thus no hidden A<=O(log n) restriction is needed for this newer row-tilted upper. That restriction concerned an earlier, different upper bound with a tuning parameter t>=A.

The minimax risk also has the separate uniform-predictor upper log A, so it is at most min{log A,V(A,n)}. This is a minimax bound using the better of two estimators, not an improved log-A cap for add-one itself.

Safe consequences:

- The A^5 polynomial factor is necessary for the unrestricted initialization class, up to logarithmic factors. Calling its A^5-versus-A^3 gap merely unproved is now inaccurate.
- If arbitrary-initialization minimax KL tends to zero along A=A_n, then A_n^5/(n+1) must tend to zero. The reviewed add-one theorem gives the sufficient condition A_n^5 log(n+2)/(n+1)->0. The logarithmic gap remains.
- For error epsilon<2^(-31), (KL-MM5) requires n+1>=2^(-31)A^5/epsilon. This is a statistical sample-necessity condition, not a precision or architecture lower bound.
- The lower saturates only at a universal constant, while forward KL can grow with A. It does not prove sharp saturation or a global Theta(min{1,A^5 log n/n}) formula.

## 5. Stationarity and literature boundary

HJW's stationary higher-order theorem remains a second, compatible lower bound: with N=n+2 and order two it gives A^3/[C_2 N] log(N/A^3) on 2<=A<=N^(1/3)/C_2. Theorem 22 and Section 6 were cross-checked directly in the [primary arXiv v2](https://arxiv.org/pdf/2106.13947v2); the publication is [Han, Jana and Wu, IEEE TIT 2023](https://doi.org/10.1109/TIT.2023.3239508). Their Section 6 explicitly distinguishes stationarity from nonstationary prediction. The higher-order stationary lower and (KL-MM5) can be combined by taking their maximum on the former's stated domain. Fixed A is still governed by the stationary Omega_A(log n/n) lower, not by claiming MM5 itself supplies a logarithm.

The MM5 hard initial law concentrates the terminal phase on an informative U x V row. Its initial law is not stationary. Under stationary clock-phase initialization the informative phase would have weight 1/L, so this proof cannot be transferred unchanged to stationary sources. The two source classes can genuinely differ: along n=A^5 and A->infinity, (KL-MM5) remains bounded below by a positive universal constant, whereas the known stationary achievable rate A^3/(n+2) log[(n+2)/A^3] tends to zero.

The A^5 TV theorem is inherited project mathematics already present in the public snapshot; the KL corollary is a standard Pinsker-and-Jensen consequence. This audit is not an exhaustive literature search, a novelty claim, external peer review, formal verification, or a result about trained networks, floating-point backends, or architectural resource optimality.

## Suggested replacement summary

For arbitrary initialization, the inherited all-finite-parameter MM5 TV lower bound yields the forward-KL minimax lower 2^(-31)min{1,A^5/(n+1)}. Combined with the reviewed ordinary full-history add-one upper O(A^5 log(n+2)/(n+1)), this matches the polynomial alphabet dependence up to logarithmic factors. The exact logarithm, saturation behavior, and complete joint-(A,n) minimax rate remain unresolved. The stationary A^3 theory is a separate smaller source class and must not be substituted for this arbitrary-initialization result.
