# Independent analytical review: statistical alphabet bounds

**Disposition.** No mathematical defect found in the claimed lower bounds, stationary add-one upper or bounded-reverse-mixing upper, under the explicitly stated classes and inherited standard inequalities. The reverse excursion/optional-stopping step is valid but benefits from the explicit mark-law and stopping-time justification below. This is not a formal proof-assistant verification, exhaustive prior-art survey, or architectural lower bound.

## Bindings and method

- Reviewed note `statistical_alphabet_bounds_v1.html`: SHA-256 `87b8129d99c89f8909a77fa9d711df70dfbe8a64bd107ccda1dc7fb90e8cb788`.
- Earlier alphabet candidate `../fixed_alphabet_causal_extension_20261103_1653/alphabet_extension_candidate_v1.html`: SHA-256 `f0a9621a62655aaa41cf4c45fcfcf183580511ed52465be1bf11b988e45e24ff`.
- R011 inherited theorem `../../cloud_work/conditions-20261028/research/resume_20261030/R011_global_rates_and_constant_adaptation_v1.md`: SHA-256 `aaafd3823ab11e20ffdeff2164115c6c91db5efea6e2dffd9c3c78da0b7fbbbf`.
- Han–Jana–Wu primary paper, Theorems 5 and 22 and equation (95): https://arxiv.org/html/2106.13947v2#S5 .

This review uses analytical derivations and source/hash reads only. It performs no enumeration, tests, simulations, scientific-code execution or source overwrite.

## 1. Binary two-point and quantifiers

For p±=1/2±δ, δ=1/(8sqrt N), the stated χ²-type KL bound gives per-symbol KL≤(2δ)²/(15/64), hence joint KL≤4/15 and Pinsker TV≤sqrt(2/15). A binary testing reduction for the absolute error in q(1) gives the advertised (1−sqrt(2/15))/(8sqrt N) lower bound on the worst of the two risks. Embedding these iid laws in an A-symbol alphabet is legitimate for the general stationary/arbitrary-initial classes, although that particular binary family has no full support for A>2. The next family supplies the stronger full-support assertion. Every bound is an infimum over a single history-based estimator followed by a source supremum, not a lower bound for each source separately.

## 2. Paired signs, stationary law and reverse KL

For every row, the perturbations of paired successors cancel; for fixed b,c, paired predecessor perturbations cancel. Thus the uniform law π(a,b)=1/A² is stationary for every sign vector, including odd A where unpaired coordinates use 1/A. Entries are at least (1−η)/A>0. A two-step pair transition is the product of two such entries, so P²(x,y)≥(1−η)²/A²≥π(y)/4. Since π is uniform, the stationary reversal is P transpose and satisfies the same two-step minorization. This gives d_t=(3/4)^floor(t/2), with sum from t=0 equal to 8.

Flipping one σ_hbr changes only reverse rows (b,2r−1),(b,2r), with two altered predecessor probabilities per row. Their one-step KL is (2η/A)log((1+η)/(1−η))≤8η²/A. Given terminal S_N=s, the reversed trajectory has M=N−2 transitions and starts from s. Its probability of the two-row set at reverse time t is at most 2/A²+d_t, so expected visits are ≤2N/A²+8. Conditional path KL is therefore ≤16η²N/A³+64η²/A≤3/16. Pinsker yields TV≤sqrt(3/32)<1/2, so each conditional equal-prior sign test has average error at least 1/4. All terminal states have the same π under all sign vectors, hence conditioning on s does not tilt the sign prior. A randomized estimator is handled by adjoining its independent seed.

For paired first symbol a, a wrong sign for successor pair r forces at least η/A TV loss on that disjoint output pair; the m pair costs add. Averaging the paired-terminal chance 2m/A and the sign-test errors yields ηm²/(2A²). Since floor(A/2)≥A/3 for A≥2 and η=(1/16)min{1,sqrt(A³/N)}, the bound is at least (1/288)min{1,sqrt(A³/N)}. The estimator may depend on the actual terminal state and the entire word; the conditional test is performed after fixing that terminal, then averaged with its common law.

Index check: observing X_1,...,X_N provides the pair path Y_0,...,Y_M where M=N−2. Its M departures have successors X_3,...,X_N, and its target is the row at Y_M=(X_(N−1),X_N). At N=2, M=0; the reverse-path KL is zero and the lower bound remains meaningful. No future symbol is exposed.

## 3. Stationary harmonic bound and simultaneous stacks

For a two-sided stationary extension, J_t^(M)≥J_t^(t) for 0≤t≤M. Stationarity makes E[1/(J_t^(M)+1)] independent of t, while J_M^(M) has the actual terminal count J. Summing therefore gives (M+1)E[1/(J+1)]≤E sum_t 1/(J_t^(t)+1). Grouping the latter pathwise by each state's successive occurrence yields sum_s H_(n_s)≤A² H_(M+1). This is not a claim that the final position is a uniform rank in its own realized path, and it remains valid for reducible or nonmixing stationary chains.

Independent infinite successor stacks realize the original process unconditionally. For a fixed state and k-prefix, expected empirical TV≤(1/2)sqrt(A/k) by Cauchy–Schwarz, and changing one sample changes the TV by at most 1/k. One-sided bounded differences followed by a union bound over A²M fixed stacks/prefix lengths yields the stated simultaneous event. It is valid when later evaluated at the random terminal state and count because all fixed prefixes were controlled simultaneously; it does not assert iid samples after conditioning on either quantity. The add-one mixture plus the inequalities sqrt(k)/(k+A)≤1/sqrt(k+1) and A/(k+A)≤sqrt(A)/sqrt(k+1), with a separate k=0 check, yields the stated coefficient. Jensen and the harmonic result give the stated stationary upper; the δ failure event contributes ≤1/(M+1).

## 4. Reverse-occupation and excursion argument

Fix π_s>0 and condition on actual terminal s; the reverse pair chain starts at s. Put p_t=P_s(Y_t=s). Uniform reverse mixing gives |p_t−π_s|≤d_t, so |EK−λ|≤B. Moreover for u>t,

Cov(1{Y_t=s},1{Y_u=s}) = p_t(R^(u−t)(s,s)−p_u)
 ≤ p_t(d_(u−t)+d_u).

Summing the two lag bounds over u gives Var K≤(1+4B)(λ+B), and replacing B by B₀≥1 gives the note's formula. If λ≥4B₀, EK≥3λ/4; Chebyshev with a λ/4 deviation gives P(K<λ/2)≤20(1+4B₀)/λ.

For the mark step, work within the recurrent class containing s. Successive complete reverse excursions from s back to s are iid by the strong Markov property. The forward-successor mark associated with a completed reverse excursion is its final reverse state immediately before returning to s. Its law is the original forward transition row θ_s: the stationary cycle-flow identity gives expected arrivals from t per s-cycle as π_t R(t,s)/π_s=P(s,t). Marks can be dependent on their own excursion lengths, but whole excursions are independent. Extending the reverse chain past the horizon, T=K+1 is the index of the first return strictly after M and is a bounded stopping time for the full-excursion filtration (T≤M+1). The centered mark increments are martingale differences for that filtration. Optional isometry gives E||S_T||²₂≤E T≤1+λ+B₀, and removing the final increment costs at most sqrt 2. This does not condition marks on K.

For λ≥max{A,4B₀}, on K≥λ/2 the add-one numerator gives TV≤(sqrt(A)||S_K||₂+2A)/λ. The moment bound and exceptional-event bound imply a constant multiple of sqrt(A/λ); the stated (50+120B₀)sqrt[A/(1+λ)] is conservative. When λ is smaller, the same constant makes the displayed cap-one bound trivial. Averaging over π_s and using sum_s sqrt(π_s)≤A gives (50+120B₀)sqrt(A³/M). The Θ_B statement requires the subclass to contain the constructed uniformly mixing witness family, as the note says; it is not a claim for arbitrary initial laws or unbounded reverse mixing.

## 5. Primary-source comparison and scope

Han–Jana–Wu define risk at the actual last m-symbol state in their equation (95), under stationary initialization. Theorems 5 and 22 give the stated Θ_m((A^(m+1)/N)log(N/A^(m+1))) minimax KL rate for m≥2 and 2≤A≤N^(1/(m+1))/C_m. At m=2, Pinsker followed by Jensen converts a KL upper into an expected-TV upper of the stated order. This implication does not convert the KL lower into a TV lower. Their displayed add-one assignment is an ingredient of a redundancy/averaging construction; the theorem alone does not assert the same rate for the unaveraged full-history add-one estimator or arbitrary initialization. The lower and direct add-one arguments in the note remain separate mathematical claims.
