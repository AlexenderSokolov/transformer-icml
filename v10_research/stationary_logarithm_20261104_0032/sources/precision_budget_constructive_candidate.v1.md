# Constructive finite-bit evaluation of the fixed-A five-block readout

Analytical candidate, 3 November 2026. This note derives explicit sufficient error ports and then constructs a specialized integer/dyadic evaluator that meets them. It is not an IEEE guarantee, a constant-word-length claim, an optimal precision threshold, an independently reviewed result, or an empirical finding. No experiment, training, external upload, or source-file modification was performed.

Reference: `../fixed_alphabet_kl_upgrade_20261103_2300/fixed_alphabet_terminal_kl.v1.md`, especially Sections 5–9. Its exact-real Gaussian and statistical lemmas are retained. The present note does not change its fixed learned parameters or its five-block architecture.

## 1. Setting and conclusion

Let A>=2, N=n+2>=2, and L=N+A>=4. Let B be the actual terminal full-history add-one distribution and let p be the exact-real block-3 selected simplex. The reference proves

    TV(p,B) <= N exp(-N)/A < 1/L.

The conditional ports below imply that the numerical output Q is an exact dyadic simplex and, for every word, including n=0,

    TV(Q,B) <= min{1, (46A+2)/L},
    Q_b >= 1/(4AL),                                  (P1)
    D(theta||Q) <= 2D(theta||B) + 8A(46A+2)^2/L.       (P2)

Consequently, for n>=1 the reference's statistical bound V gives

    E D(theta||Q) <= min{log(4AL), 2V + 8A(46A+2)^2/L}.

For n=0 use the elementary E D(theta||B)<=log A rather than the n>=1 definition of V. Constants and alphabet dependence are deliberately conservative.

A complete arithmetic algorithm meeting the ports is given in Sections 4–6. Its common fractional precision is

    s = ceil(log2(AL)),  b = 32s,  H = 2^b,  F = H^2. (P3)

All working integer lengths are O(b+log A+log L)=O(log(AL)), with constant-factor wider products. This is sufficient, not a claim that the coefficient 32 is necessary.

## 2. Softmax perturbation and gate ports

For any two score vectors u,v on the same finite support,

    TV(softmax(u),softmax(v)) <= ||u-v||_infinity.      (P4)

The same statement holds after subtracting arbitrary rowwise constants. To prove it, interpolate u+t(v-u). The derivative of coordinate alpha_j is alpha_j(r_j-E_alpha r), whose total absolute sum is at most 2||r||_infinity. Integrate and divide by two. Therefore the expectations of any value in an interval of length R differ by at most R||u-v||_infinity. This bound is independent of key count; numerical approximation of each unnormalized weight must separately pay that count.

Require exact integer positions and squares, exact full causal supports j<=i, exact token onehots, and exact dyadic ReLU/linear operations. Copy-head outputs must lie in [0,1] coordinatewise and approximate their exact outputs within 1/32 per coordinate. At every valid data lag used for candidate or terminal gates, i>=A+2>=4. The wrong copy mass is less than

    2/(exp(4)-1) < 1/16.

The inequality exp(4)>33 follows already from the first five terms of its positive series. Thus every incorrect copy coordinate stays below 1/4 and the correct coordinate stays above 3/4. The exact two-hinge map snaps the needed copies to exact onehots. At invalid candidates, v=0 and the snapped coordinates remain in [0,1], so their g gates are exactly zero. Integer flags, all candidate-context indicators, and the terminal query are exact. For N=2 only the first lag is needed by the terminal query; no nonexistent data transition is introduced. The first-BOS marker and all A smoothing tokens remain present.

## 3. Conditional numerical ports

Quantities in this section are terminal quantities unless explicitly stated otherwise. These are sufficient conditions, not automatic properties of an unspecified floating-point implementation.

1. The block-3 selected output p_tilde is a simplex satisfying

       ||p_tilde-p||_infinity <= 1/(64L^2),
       |z_tilde-1/L| <= 1/(64L^3).

2. Block 4 evaluates its displayed scores from p_tilde,z_tilde, with additional absolute score error at most 1/(64L). Its numerical attention mean has additional error at most 1/64 relative to exact softmax of those evaluated scores. Its FFN computes the displayed clipping operation exactly, so 0<=x_tilde_b<=L.

3. Block 5 evaluates its displayed scores from x_tilde_b with additional absolute score error at most 1/[64L(1+log L)]. Its supplied log-position values have error at most 1/(64L). Its numerical weighted mean has additional error at most 1/(64L) relative to exact softmax of those evaluated scores and the supplied log values.

4. Let R_star be exact vocabulary softmax of the numerical block-5 logits ell_tilde. The final evaluated output Q is a simplex with

       |Q_b-R_star_b| <= 1/(8AL)  for every b.

Proof of (P1). Relative to the exact broad-Gaussian head at p,z=1/L, each block-4 score changes by at most

    L/(64L^2) + L^2/(64L^3) + 1/(64L) = 3/(64L).

By (P4), its exact mean changes by at most 3/64. Adding its mean-evaluation error gives 1/16. The FFN clipping map is 2-Lipschitz in the mean, so the reference's |x-Lp|<=20 becomes

    |x_tilde_b-Lp_b| <= 20+1/8 < 21.                 (P5)

Now compare block 5 with the exact narrow Gaussian centered at x_tilde_b. That center is in [0,L], so its exact log mean ell_b^0 obeys

    1 <= exp(ell_b^0) <= L,
    |exp(ell_b^0)-x_tilde_b| <= 24.

Using (P4), the perturbed log-value expectation changes by at most

    (log L)/(64L(1+log L)) + 1/(64L) + 1/(64L)
      <= eta := 3/(64L).

One may first compare the score distributions with the exact log values, then add the value perturbation; no enlarged range is required. Since eta<1/2 and exp(eta)-1<=2eta,

    |exp(ell_tilde_b)-exp(ell_b^0)| <= 2L eta < 1.

It follows that |exp(ell_tilde_b)-Lp_b|<=46. Normalization, using only sum p=1, yields

    TV(R_star,p) <= 46A/L.

Also exp(ell_tilde_b) lies in [exp(-eta), L exp(eta)], whence

    R_star_b >= exp(-2eta)/[1+(A-1)L] >= 1/(2AL).

The last elementary bound uses 2eta<1/2 and exp(1/2)<2. Final coordinate rounding costs TV at most 1/(16L), and leaves Q_b>=3/(8AL)>=1/(4AL). Add TV(p,B)<1/L to obtain (P1). The KL transfer from the reference gives

    D(theta||Q) <= 2D(theta||B) + sum_b (B_b-Q_b)^2/Q_b
                 <= 2D(theta||B) + 8AL TV(B,Q)^2,

which proves (P2). In particular, a TV guarantee without the rounding/support port would not prove a finite forward-KL bound.

## 4. Explicit max-shifted integer exponential

All scores used below are exact H-grid dyadics. For each row, compute its maximum exactly on its actual causal support. A nonnegative shifted gap is d=X/H with integer X>=0. The following deterministic integer routine approximates exp(-d):

- If X>bH, return 0.
- Otherwise set Z_0=F-X. For r=0,...,b-1 set Z_{r+1}=floor(Z_r^2/F).
- Return w_tilde=floor(Z_b/H)/H.

The zero-gap output is exactly one. All outputs lie in [0,1]. Since H>=2b, the retained case has d/H<=1/2. The elementary inequality

    -u-u^2 <= log(1-u) <= -u,  0<=u<=1/2,

shows that the difference between exp(-d) and (1-d/H)^H is at most d^2/H<=b^2/H. Each square-and-floor contributes at most 1/F absolute error, and x->x^2 is 2-Lipschitz on [0,1]. After b steps the total such error is less than 2^b/F=1/H. The final conversion adds less than 1/H. In the truncated case, exp(-d)<exp(-b)<2^(-b)=1/H. Hence uniformly

    |w_tilde-exp(-d)| <= epsilon_w := (b^2+2)/H.      (P6)

No exponential of a positive O(L^2) or O(L^3) argument is formed. A row always has a retained, exact weight-one maximizer, so its numerical denominator is at least one.

For m supported keys, let the returned weights be Z_j/H, and S=sum_j Z_j. Compute a_j=floor(H Z_j/S), R=H-sum_j a_j, and add one to any deterministically chosen R distinct coordinates, for example the first R supported keys. Here 0<=R<m. Dividing the resulting integers by H produces an exact nonnegative simplex alpha_tilde, each coordinate within 1/H of the exact normalization of the numerical weights. Largest-remainder sorting is unnecessary for this error bound. Normalization of the weight errors costs TV at most m epsilon_w; this follows from the exact weight sum being at least one and the standard two-term normalization identity. Thus

    TV(alpha_tilde, softmax(scores))
       <= m epsilon_w + m/(2H)
       <= m epsilon_g,
    epsilon_g := (b^2+3)/H.                           (P7)

This explicitly charges m<=i<=L for attention and m=A for the final vocabulary softmax. It does not replace full causal support by a sparse or future-looking set.

## 5. Constructed log-position routine

Exact log i is not supplied to the numerical evaluator. Here is a source-independent integer construction. For j>=1 write j=2^k u, with integer k=floor(log2 j) and 1<=u<2; finding k uses the integer bit length. Put r=(j-2^k)/(j+2^k), so 0<=r<1/3. For log 2 use r=1/3. The identity

    log u = 2 sum_{t>=0} r^(2t+1)/(2t+1)

follows by integrating the geometric series for 2/(1-r^2). Use T=b terms, F-grid truncation r_tilde=floor(Fr)/F, and q_tilde=floor(F r_tilde^2)/F. Form c_t=floor(F/(2t+1))/F. Evaluate by Horner's rule from h_T=0:

    h_t = c_t + floor(F q_tilde h_{t+1})/F,
       t=T-1,...,0,
    ell_tilde(r) = 2 floor(F r_tilde h_0)/F.

All these expressions are integer products and divisions on F-grid representations. The exact finite Horner values are at most 9/8. We have |q_tilde-r^2|<2/F; the Horner error recurrence is bounded by

    e_t <= (17/4)/F + e_{t+1}/9,

so e_t<5/F. The final multiplication and factor two cost less than 8/F in total. The omitted tail is at most 3^(-2b)<H^(-3). Therefore

    |ell_tilde(r)-log u| < 8/F+H^(-3) < 9/F.

The same bound holds for log 2. Compute k ell_tilde(1/3)+ell_tilde(r), and round to the nearest H-grid point to obtain lambda_j. Since k<=s and H>=18(s+1),

    |lambda_j-log j| <= 9(s+1)/H^2 + 1/(2H) <= 1/H.  (P8)

At j=1 the routine returns zero exactly. The table is generated from positions alone and charged in time and memory. It is not a log of a probability or an externally supplied count statistic.

## 6. Satisfying every port

Use the integer exponential and mass-preserving weight rounding for all attention rows. Use exact integer i,i^2, exact fixed rational weights, and exact dyadic FFNs. The displayed kappa cancels exactly against attention's divisor; this is exact rational algebra, not a rounded approximation to sqrt(d_h). Every score is an H-grid number: the learned formulas only multiply dyadic activations by integer positions and fixed dyadic constants. In particular there are no uncontrolled state-by-state products in these scores.

- Copy heads: their onehot-valued aggregates are exact H-grid numbers in [0,1]. By (P7), each coordinate error is at most L epsilon_g. The margins in Section 2 therefore snap all needed gates exactly.
- Block-3 row heads: the aggregate of onehot values with an exact simplex of numerical weights is an exact H-grid simplex. Exact terminal selection yields p_tilde with coordinate error at most L epsilon_g. There is no independent rounding of A probabilities that loses their total mass.
- Uniform marker head: all numerical exponential weights equal one. The mass-preserving rule gives each attention weight within 1/H of 1/i, hence |z_tilde-1/L|<=1/H.
- Block 4: its numerical-input scores are evaluated exactly, so the additional score port is zero. Its integer-position weighted mean is an exact H-grid sum, with absolute error at most L^2 epsilon_g. The clipping FFN is exact.
- Block 5: its numerical-input scores are exact. Use lambda_j from (P8). Its dyadic weighted sum is initially on the H^2 grid and is rounded to the nearest H grid. Relative to exact attention on the supplied values, the resulting mean error is at most L(log L+2/H)epsilon_g+1/(2H). Its log-position error is at most 1/H.
- Vocabulary softmax: apply the same integer routine and mass-preserving rounding on exactly A logits. Its coordinate error is at most its TV error, hence at most A epsilon_g. The support proof is then quantitative, not an assumption that positive real exponentials remain nonzero after rounding.

For a simple analytic verification of the chosen budget, s>=3, A,L<=2^s and b=32s. For all integer s>=3,

    b^2+3 <= 2^(5s).

At s=3, 9219<32768, and the right side grows by 32 while the left side grows by less than (4/3)^2 from one s to the next. Thus

    epsilon_g <= 2^(-27s),   1/H=2^(-32s).

In particular,

    epsilon_g <= 1/(256L^3),  1/H <= 1/(256L^3).       (P9)

Indeed 2^(27s)>=256*2^(3s) for s>=3. These imply all Section 3 ports:

    L epsilon_g <= 1/(256L^2) <= 1/(64L^2),
    1/H <= 1/(64L^3),
    L^2 epsilon_g <= 1/(256L) <= 1/64,
    1/H <= 1/(64L),
    L(log L+2/H)epsilon_g+1/(2H) <= 1/(64L),
    A epsilon_g <= 1/(8AL).

For the penultimate line, use log L+2/H<=L and (P9), giving at most 1/(256L)+1/(512L^3). For the final line use A<=L. The copy bound is much smaller than 1/32. Every condition therefore holds uniformly, including L=A+2 and arbitrary histories.

The precision schedule is chosen for the prefix being evaluated. It is a numerical resource, not a learned length-dependent parameter or an extra token feature. Earlier rows are still evaluated using only their allowed keys and fixed formulas. This is a finite-precision evaluation of the exact model's ordinary softmax, not a claim that its dyadic result equals a transcendental exact-real softmax.

## 7. Bit complexity and limitations

Exact integer positions reach L and L^2. The largest raw copy scores are O(L^3), not merely O(L^2); narrow-head scores are O(L^2), broad-head terminal scores O(L), and final logits O(log L). The implementation does not assume these raw scores are bounded. Fixed coefficients can add O(log A) bits before exact cancellation. Scores and activation numerators, accumulated row sums, and constant-factor wider F-grid products all have O(b+log A+log L) bits. The logarithm construction uses bounded fixed-point Horner arithmetic, avoiding the growing denominators of an exact-rational Taylor sum.

With schoolbook integer arithmetic, a conservative complete causal evaluation cost is

    O(((A^2+2A+3)L^2+L)b^3
       +(A^3 L^2+A^6 L)b^2) bit operations.

The b^3 term pays for b squarings per shifted exponential and b-term log generation; the b^2 term pays for exact score arithmetic, vector aggregation and dense projections/FFNs. Row-streamed storage is conservatively

    O(A^3 L b + b^2 + A^6 log(A+2)) bits.

The first term includes positional/log tables and working row storage. Dense parameters have O(A^6) entries, with O(log(A+2))-bit fixed descriptions. A growing A changes architecture and vocabulary; this remains a fixed-A family, with A dependence shown. No fixed exponent range, GPU kernel, automatic mixed precision, training algorithm, latency guarantee, or optimal bit complexity is certified.

## 8. Exact failure modes that a generic finite-bit claim must exclude

1. **Final zero destroys forward KL.** For a constant-symbol word, a different symbol has B_b=1/(n+A), and the reference's exact readout gives R_b=O_A(1/L). Fixed-grid nearest rounding eventually makes that coordinate zero. Choose an iid source giving that symbol strictly positive true probability: the constant-word event still has positive probability, so conditional KL on that event and expected KL are infinite. Small TV error does not repair this.

2. **Coarse rounding of z can destroy even TV.** If a fixed fractional grid floors 1/L to zero, block 4 uses score (p_b+1/2)j. Its mean is at least L-1/(exp(1/2)-1)>L-2. For L>=10, the clipping FFN therefore sets every x_b=L, so all block-5 logits are equal and final softmax is uniform. Constant-symbol histories have B approaching a point mass, hence TV tends to 1-1/A rather than O_A(1/L). This failure occurs even with every remaining computation exact.

3. **Large raw logits cannot be ignored.** Unshifted exponentiation of raw copy and narrow-head logits encounters respectively O(L^3) and O(L^2) positive magnitudes. An unspecified finite exponent range cannot support an all-length theorem. Max shifting, an exact weight-one anchor, and explicit tail control avoid this; simply saying “softmax is stable” does not.

4. **The port exponents are sufficient, not sharp.** In particular p accuracy O(L^-2) and z accuracy O(L^-3) were chosen to make a global sup-score proof short. Local Gaussian sensitivity may permit weaker ports. This note proves an O(log(AL))-bit construction, not a matching necessity theorem for every numerical representation.

Under a common positive dyadic output grid 2^(-b), logarithmically growing fractional precision is necessary for the stated all-history O_A(1/L) approximation plus positive support: the constant-word rare coordinate must be at most C_A/L yet, if positive, is at least 2^(-b), forcing b>=log2 L-O_A(1). This is a statement about that encoding class, not every floating/exponent or symbolic encoding.

## 9. Review status

This is a constructed analytic candidate, not a port assumption disguised as a backend. The proof gives integer recurrences, denominator protection, precise rounding, paid log generation and all error bounds. It still requires independent analytic review before incorporation into a reviewed theorem or public research materials. The source note's disclaimer remains accurate for its own unchanged contents until such an upgrade is reviewed and explicitly adopted.
