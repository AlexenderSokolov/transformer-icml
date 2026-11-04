# Independent analytical review of the constructive fixed-point backend

3 November 2026. **PASS for the exact source identified below, within its stated specialized arbitrary-precision scope.** No numerical tests, simulations, sample enumeration, fitting, training, repository mutation, external upload, or browser rendering were performed. File hashing is an integrity check, not mathematical numerical evidence.

## Exact reviewed source

File: `precision_budget_constructive_candidate.v1.md`.

SHA-256: `e555323ee18b39b0003863e9d41084d6f2222a575c340b0a9bb8c87213d01a16`.

The entire candidate was read. The reference exact-real finite-A theorem and its first-three-block construction were previously independently reviewed; the relevant interfaces, Gaussian constants, resource accounting, and all-zero-count boundary cases were rechecked for compatibility. The earlier three-block integer backend was also inspected as context, not treated as proving the new two-block evaluator.

## 1. Verified conclusion and interpretation

For all finite A>=2 and N>=2, L=N+A, the candidate supplies an explicit integer/dyadic evaluation scheme at fractional precision

    s=ceil(log2(AL)), b=32s, H=2^b, F=H^2.

The output is an exact nonnegative H-grid simplex and satisfies the claimed terminal guarantees

    TV(Q,B)<=min{1,(46A+2)/L},
    Q_b>=1/(4AL),
    D(theta||Q)<=2D(theta||B)+8A(46A+2)^2/L.

The expected-risk corollary follows from the unchanged exact add-one statistical theorem, with n=0 separately assigned its elementary log A comparator bound. The deterministic log(4AL) risk cap follows directly from the output floor.

These are guarantees for a specified numerical evaluator, not a claim about generic IEEE inference. The number b is fractional precision, not total signed word width. The statement explicitly adds magnitude, summation, and constant-factor product bits. Learned parameters and architecture remain fixed across length for each chosen A; the arithmetic precision and positional generation are length-dependent numerical resources.

## 2. Conditional-port proof

The softmax perturbation inequality is valid: differentiating along a score interpolation gives an L1 derivative at most twice the score sup-norm, and division by two yields the claimed TV bound. Expectations of interval-bounded values then cost that interval's length. Rowwise shift invariance is used only in a way consistent with recomputing the score-difference norm.

The copy-head gate margin is sufficient. At every required lag, i>=4, the wrong mass is less than 2/(e^4-1)<1/16. Adding the permitted 1/32 numerical coordinate error still leaves the exact two-hinge thresholds safely separated. At invalid candidates the validity gate is zero and copied/snapped coordinates remain in [0,1], so all invalid context indicators remain exactly zero. N=2 requires only the legal terminal previous-symbol copy; the algorithm does not create an unobserved transition.

The block-4 score difference is correctly bounded by

    j|delta p|+|j-j^2||delta z|+additional score error
       <=3/(64L).

The expected position then changes by at most 3/64; adding its evaluation error gives 1/16. The clipping FFN is 2-Lipschitz and projects onto [0,L], so the inherited 20-error becomes at most 20+1/8<21.

The subsequent comparison is deliberately to the exact narrow Gaussian at the **computed clipped center**. That center is in [0,L], so the uniform geometric-mean lemma applies without propagating its center error through the narrow attention's large scores. This is a valid comparison within the proof, not a change to the implemented architecture. It avoids an unnecessary additional factor of L while preserving the claimed approximation to B.

The narrow-logit error is at most eta=3/(64L). Comparing score distributions first using the exact log values, and then adding log-value and mean-evaluation errors, correctly avoids assuming an unperturbed value range for the supplied approximate logarithms. Exponentiating the logits costs at most 2L eta<1. Thus every numerical geometric mean is within 46 of Lp_b, and the normalization identity gives TV(R_star,p)<=46A/L without requiring their centers or geometric means to have total L.

The same logit comparison gives R_star_b>=1/(2AL). Coordinate error at most 1/(8AL) in the final rounded simplex leaves Q_b>=3/(8AL), which is stronger than the claimed 1/(4AL). The final rounding TV cost is at most 1/(16L). Adding the retained matching error below 1/L proves the stated (46A+2)/L envelope. The forward-KL transfer then uses the proven support, not an invalid inference from small TV alone.

## 3. Integer exponential and denominator protection

For an exact shifted H-grid gap d=X/H<=b, Z_0=F-X represents 1-d/H on the F grid. The inequality

    -u-u^2<=log(1-u)<=-u, 0<=u<=1/2,

is correct, and H>=2b makes it applicable. After b exact squarings the unrounded reference is (1-d/H)^H. Its difference from e^-d is at most d^2/H. Each square-and-floor step adds less than 1/F, with error amplification at most two, so the accumulated floor error is less than 1/H. The last conversion adds less than 1/H. This proves the stated (b^2+2)/H error.

For d>b, setting the weight to zero has error below e^-b<2^-b=1/H. This is an explicitly controlled truncation, not an assumption about machine underflow. At d=0 every recurrence remains exact and the final weight equals one. Consequently every row retains a weight-one maximizer, its denominator cannot vanish, and no positive exponential of an O(L^2) or O(L^3) raw score is ever formed.

The mass-preserving normalization rule is valid. The integer residual R=H-sum floor(H Z_j/S) is nonnegative and smaller than the number m of keys. Adding one to any deterministic R distinct coordinates keeps every coordinate within **at most** 1/H of the exact normalization and gives total mass exactly one. It need not be largest-remainder rounding. This includes the possibility of adding a unit to a zero fractional remainder, so a strict less-than assertion would have been inappropriate; the artifact correctly uses a non-strict error bound.

The normalization error is at most m epsilon_w in TV, and the grid adjustment adds at most m/(2H). Thus epsilon_g=(b^2+3)/H safely bounds the error per supported-key count. Attention pays m<=L; the final vocabulary softmax pays m=A.

## 4. Constructed logarithms

The range reduction j=2^k u and r=(j-2^k)/(j+2^k) keeps r in [0,1/3); log 2 uses the endpoint 1/3. The atanh identity and the b-term tail estimate are valid. This construction uses position integers only, not probabilities or counts.

The F-grid Horner proof checks. The exact finite Horner values are at most 9/8, q_tilde<=r^2<=1/9, and |q_tilde-r^2|<2/F. Coefficient flooring and multiplication flooring give

    e_t<=(17/4)/F+e_{t+1}/9,

so e_t<5/F. Including r approximation, the final product floor, and the factor two still costs less than 8/F. The omitted tail is smaller than 3^-2b<H^-3, giving the stated 9/F total bound.

Multiplication by k and addition of the mantissa logarithm cost at most 9(s+1)/H^2. The candidate then uses **nearest** H-grid rounding, costing at most 1/(2H). Therefore H>=18(s+1) genuinely proves the final 1/H error. A floor-only final conversion would not automatically justify this same constant; the candidate explicitly avoids that issue. At j=1 the result is exactly zero.

All Horner operations use bounded fixed-point integers. No rapidly growing exact-rational series denominator is hidden in the resource claim.

## 5. Constructed pipeline and precision budget

The displayed attention scaling constant kappa is an integer and cancels exactly. The score formulas therefore remain H-grid dyadics even though the standard attention divisor 1/kappa need not itself be a finite dyadic. Exact integer multiplication and division implement that cancellation; no rounded square root is used.

After copy gates, all block-3 candidate indicators are exact. Aggregating onehot values against an exact numerical attention simplex gives an exact H-grid categorical simplex. Terminal selection chooses precisely one such row, so the selected p_tilde preserves total mass. Independent coordinate truncations do not silently destroy it. The first-BOS marker attention gives an error at most 1/H in the reciprocal, and all smoothing tokens remain present.

Integer-position averages in block 4 are exact H-grid sums after attention-weight approximation. The clipping affine/ReLU expressions are exact on the grid because H is divisible by two and four. The narrow head's numerical-input scores are likewise exact. Its weighted approximate-log mean initially has H^2 scale and is explicitly rounded to the nearest H grid, accounting for the extra 1/(2H).

The elementary budget proof is sound. For s>=3, b^2+3<=2^(5s), so epsilon_g<=2^(-27s). Both epsilon_g and 1/H are at most 1/(256L^3). Substitution proves each conditional port, including the logarithmic mean port and final A epsilon_g<=1/(8AL), using A<=L. These inequalities cover the shortest legal word and every finite A; no asymptotic omission is used.

The method evaluates all attention supports causally. The global choice of numerical precision depends on the observed length, as disclosed, but no earlier row receives a future key or a source-dependent feature.

## 6. Bit resources and overflow/underflow claims

The raw-score range is not treated as constant: copy scores can grow as O(L^3), and narrow scores as O(L^2). Numerical row maxima and shifted differences are computed with exact signed integer/dyadic arithmetic before the exponential primitive. The broad O(L) score statement is specifically terminal; even crude early-row bounds involving A^2 remain polynomial in A,L and do not violate the asserted bit-length envelope.

Score numerators, row sums, products, and F-grid scratch require O(b+log A+log L) bits with fixed constant-factor widening. The largest F-grid products can need roughly 4b plus magnitude bits. Hence the theorem is about a growing-word arbitrary-precision evaluator, not a machine with only b total bits or a fixed exponent range.

The stated conservative work bound covers one b-squaring exponential evaluation per active causal score, log-position generation, normalization divisions, vector-valued aggregation, and dense projections/FFNs. Mass-preserving normalization may store a working row of weights or revisit it; either choice fits the displayed O(A^3Lb+b^2+A^6 log(A+2)) storage envelope. The residual allocation requires no sorting. The O(b^2) scratch term also covers stored Horner coefficients if used. No dense L-by-L attention matrix is necessary.

The operation and storage bounds are consistent with schoolbook integer multiplication/division. They are conservative mathematical bit-complexity bounds, not measured timings, an optimized implementation, or a practical hardware-performance claim.

## 7. Failure examples and remaining limitations

The failure examples are correctly scoped. Rounding an O_A(1/L) positive rare-coordinate prediction to zero can create infinite forward KL on a positive-probability constant-word event under an iid source with positive rare-symbol probability. Flooring the reciprocal to zero changes the broad heads into increasing exponential tilts, and for L>=10 the subsequent clipping sends all coordinate centers to L, producing uniform output. Unshifted exponentiation cannot supply an all-length fixed-exponent-range guarantee.

The lower statement b>=log2 L-O_A(1) is limited to a common positive dyadic output grid and the stipulated all-history O_A(1/L) approximation. It is not a lower bound for all floating/exponent, symbolic, or other numerical representations. The chosen precision coefficient and port exponents are only sufficient.

No defect requiring a mathematical revision was found. This verdict establishes the written constructive algorithm and its analytical guarantees. It does not assert that a software implementation was executed, that every possible implementation follows the specification, or that a generic floating-point backend is certified.

**Final verdict: PASS** for the exact source hash above, with the artifact's explicit arbitrary-precision, fixed-A architecture-family, and nonexperimental limitations retained.
