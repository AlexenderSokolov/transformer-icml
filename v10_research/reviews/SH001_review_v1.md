# SH001 v1 — independent hostile mathematical review

Date: 2026-11-02. Reviewer: independent LLM reviewer.

## Verdict and immutable target

**PASS within the exact stated model and accepted-dependency contract. No blocking defect found.** The new rescaled-tube lower has a genuinely κ-independent constant, and together with accepted SB001 v2 it establishes the stated sharp **weight-ratio** order κ_min=Θ(f), not merely the order of lnκ.

Target: `score_precision/SH001_sharp_weight_ratio_threshold_v1.md`.
SHA256: `fa8e326047f2df8f01dd7b3112da655937ad7be1a3508ad00b80ccd51b64fd50`.

This is an independent LLM mathematical review with independently authored finite diagnostics, not formal verification, external peer review, a novelty determination, or execution of an emitted network. Root acceptance is a separate decision. No source manuscript or frozen stage3 artifact was edited.

## Evidence and dependency scope

I read the full target, the actual BA001 manuscript (including exact model, witness and tube proof), the actual SB001 v2 construction/upper and §7 operating-point bound, the acceptance records, and the corresponding prior review records. Hashes of accepted dependency manuscripts were checked against the acceptance JSON. The new lower is checked from its displayed argument, not inferred by treating BA001's old constant as uniform. The upper is explicitly inherited from accepted SB001 v2; this review does not independently re-prove all of its upstream statistical results or implementation ledger.

The family has at most D scalar coordinates, bounded trailing-r local features, dense M-key positive-weight ratio outputs, downward Q-grid quantization, and only boundary side information. Uniformity in K for the lower is possible because the witness uses three symbols and has at most 3^(2r) boundary values. Matching feasibility requires K>=3, D>=K³ and r>=3. The at-most-D convention uses informational zero-padding only. Hard masks, global features, growing dimensions and arbitrary deep families remain excluded.

## 1. Source, common prior, and new cutoff

The stationary witness is valid at β=0, β=1/M and β=1/16, including unused starting symbols. With β0=max(β,1/M), α=1/(2M), η=β0-α, the proposed π is stationary and all rows satisfy T(x,y)>=β0π(y). The second-order embedding gives the all-state two-step inequality, not only a supported-state inequality. Π(W,W) is p-independent and at least 1/4.

For z=κQ<=M/4, both terms defining U are at least four. Thus J=floor(U)>=4 and J>=U/2, including the boundary U=4. Since β0>=1/M, J<=M/4; since J<=1/(4β0), β0J<=1/4. The new, essential bound is z sqrt(J)/M<=1/2. There is no hidden assumption that κ or Q is integral.

For E_j the number M-j of pre-entry WW transitions is correct. Its probability is independent of p after summing active letters, and its conditional active suffix is IID Bernoulli(p) before conditioning on boundary data. The lower e_j>=1/(32M) is conservative: Π(WW)>=1/4, waiting survival >=1/2, and no-exit survival >=3/4 yield 3/(64M). Events are disjoint, and the same uniform p prior is used for all j. The future exit mass η is correctly retained in the prediction target.

## 2. Why the κ exponent disappears legitimately

Freezing each possible boundary s before applying bounded differences is necessary and correctly done. If one varied the actual boundary-dependent query together with a suffix coin, every summand could change; the proof does not make that invalid move. It instead proves bounds simultaneously for every frozen s and later selects the actual one.

Changing one coin alters at most r trailing windows. Each weighted value is in [-κ,κ], so 2κr bounds its numerator change; it also bounds the denominator change. Efron–Stein therefore gives variance <=2κ²r²j for each sum. The Chebyshev union over 2DH sums with T0=r sqrt(40DH) has total failure at most 1/10. Random and mean denominators are at least M. The exact ratio identity yields deviation <=2κT0 sqrt(j)/M; no equality between E[A/D] and EA/ED is assumed.

The Bernoulli differentiation identity bounds both expectation derivatives by 2κrj. Quotient differentiation then bounds each comparison-curve derivative by 4κrj/M. This remains true for arbitrary source-independent real positional tables.

Multiplication of the deviation bound by Q, followed by the NEW cutoff, gives at most T0, independent of κ. Simultaneously the scaled mean-curve speed is at most 4r z j/M. The economical mesh has at most ceil(2r z j/M)+1 points, and the bound (2+4r)(1+zj/M) is valid even when the required mesh contains only endpoints. Its approximation radius is one grid unit. Downward rounding adds less than one for every real Q, including negative summary coordinates. Hence radius C0+2 is conservative, and N0^D bounds the integer banks in each mesh box without coordinate independence. Counting s in the message gives exactly the κ-independent prefactor A0 claimed in (3.3).

This is a genuine change in the proof's allocation: κ now shortens the suffix cutoff while entering the mesh length through z. It is not an omitted κ^D factor or a covert change in the quantization grid. Constants depend only on fixed D,r.

## 3. Bayes lemma, harmonic sum, cap and randomization

The finite-message lemma remains valid when goodness depends on p. For each fixed independent decoder seed, at most R good-message estimates have neighborhoods occupying at most one quarter of the prior interval. Their complement intersects goodness with probability at least 0.65, enough for the claimed ell/(16R) lower. No uniform posterior after goodness is needed.

TV dominates the error in the C1 mass. Dividing that estimated mass by 1-η and losing at most a factor two produces the conditional 1/[64A0(1+zj/M)] lower. This covers arbitrary simplex output rules, including all-zero-bank fallbacks; the lower assumes no preserved positive bank mass.

Multiplication by event probabilities gives 1/(2048A0M) times the harmonic sum. For u=z/M<=1/4, shifting the index and integrating on [0,J-1] gives at least ln(1+uJ)/(4u). The floor bound yields uJ>=min(z/(Mβ0),M/z)/8. The coefficient c0=1/(8192A0) follows. The RHS is at most c0/(8Mβ0)<=c0/8, so the bounded risk range causes no contradiction.

The same source prior and constants work for every independent encoder/decoder seed; conditional meshes may depend on that seed. Averaging the resulting Bayes bound before taking the source supremum is legitimate. Uniformity in tables then permits optimization over encoders. There is no seed-dependent adversarial-source swap.

## 4. Uniform sharp-κ corollary

The case split is exhaustive and handles the domain where the new tube cannot be used.

* β>1/16 implies x<=16Q/M<=2c_+, hence bounded f and κ>=1 suffice.
* z>M/4 implies κ>sqrt(M)/(4c_+). Because f<=1+Q<=(1/8+c_+)sqrt(M), this already gives the displayed constant times f. SH1 is not extrapolated outside its domain.
* Inside the domain, bounded f and κ>=f are trivial branches. For f>F and κ<f, x=exp(f-1)-1. The first logarithm is at least f-1-ln8>=f/2. The second uses M/(κQ)>=x/(κc_+²)>x/(f c_+²), valid because x<=Q and Q²/M<=c_+². Condition (5.1) gives its lower f/2 as well. Choosing a finite F valid for all s>=F is justified by the ratio tending to infinity, not merely by a single numerical crossing.

Combining with risk <=C/sqrt(M) forces κ>=c0 f/(2Cc_+). Taking the minimum of the five constants gives a uniform positive c_* for all stated M and β. No separate IID c/Q floor is required because κ>=1 supplies the bounded-f baseline. The result concerns every fixed C>0 on the necessary side, not only the sufficiently large sufficient multiplier.

## 5. Matching upper and scope

The imported SB001 §7 upper has exactly the displayed C_K. Its capped Ψ term is bounded by 2K^(5/2)/sqrt(M+1), and κ=ceil(f) satisfies f<=κ<f+1<=2f and [1+ln(1+κx)]/κ<=2. The c_- dependence in C_suff correctly pays for 1/Q. The risk cap at one does not weaken this inequality. SB001's all-zero and J=0 branches remain part of the inherited theorem; no new encoder is introduced.

The lower permits real κ,Q; the paid upper uses integer κ and legal dyadic Q. The manuscript explicitly restricts upper comparison to legal Q in the band, notes vacuous empty-band instances, and does not claim implementing noninteger weights. An infimum of feasible budgets suffices; no attainment is presumed. Arbitrary-start upper feasibility is stronger than stationary feasibility, while the stationary obstruction also applies to any claimed arbitrary-start guarantee.

Thus for fixed target C>=C_suff, κ_min=Θ(f) is justified. At β<=1/M and Q comparable to sqrt(M), this gives κ_min=Θ(log M) and lnκ_min=lnln M+O(1). For bounded f the statement correctly includes one in the effective-range comparison. Known-β public budget specification does not assert a free transcendental runtime operation; SB001's input-bitlength selection caveat remains. No all-Q matching minimax law, exact threshold constant, original finite-exponential evaluator equivalence, or deep-network lower follows.

## Independent reproducible diagnostics

`reviews/SH001_independent_checks_v1.py` was authored independently of the author's diagnostic and run successfully. Results, bound to the candidate hash, are in `reviews/SH001_independent_checks_v1.json`:

* 1,120 finite cutoff/event/harmonic cases, including real nonintegral κ,Q and cutoff endpoints;
* 2,430 necessity-case checks across β boundaries, tiny/large c_+, and M up to 10^100;
* 468 exact-rational local-table moment/derivative cases with query dependence, positional variation, negative values, κ=1,3/2,4, and r=1,3,70 (including overlapping/full-history boundary windows);
* 19,968 exact bounded-influence checks;
* minimum observed event-probability ratio to the claimed bound: 4.84272793154957;
* minimum observed harmonic ratio to the claimed bound: 2.507541380592722.

Finite checks corroborate the analytic proof and cannot establish universal validity. No blocking correction or new authorization is required. Recommend root acceptance of SH1–SH2 and the specified fixed-band κ_min=Θ(f) consequence, with the dependency and evidence limitations above.
