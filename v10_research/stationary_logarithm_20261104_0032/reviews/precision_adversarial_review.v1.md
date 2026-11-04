# Adversarial analytical review of the constructive precision budget

Date: 2026-11-03 UTC.

Reviewed source: `precision_budget_constructive_candidate.v1.md`.

Exact SHA-256: `e555323ee18b39b0003863e9d41084d6f2222a575c340b0a9bb8c87213d01a16`.

## Verdict

**PASS within the explicitly specified integer/dyadic, arbitrary-precision evaluation model.** I found no counterexample or mathematical defect requiring a source revision. In particular, the claimed fractional budget `b=32 ceil(log2(AL))` is sufficient with the signed magnitude, accumulation, and constant-factor product widths already required by the source. It is not sufficient to reinterpret b as the entire signed machine-word width; the source does not make that claim.

This is a second independent analytical audit of the written algorithm, including adversarial checks of rounding, early positions, zero weights, endpoints, and the narrow-score dependence. No numerical mathematical experiment, simulation, sample enumeration, implementation execution, training, external upload, or repository mutation was performed. Source hashing is only an integrity check. This report binds the Markdown source, not any generated HTML or software implementation.

## 1. Exponential primitive: scaling, truncation, and denominator

The units in the repeated-squaring construction are correct. For d=X/H and F=H^2, `Z_0=F-X` represents `1-d/H`, not `1-d`. Exactly b squarings raise the unrounded value to `2^b=H`. On the retained interval d<=b, H>=2b gives the needed `d/H<=1/2`. The logarithmic sandwich then bounds the discrepancy from exp(-d) by d^2/H.

At each floor step both approximate and reference normalized values remain in [0,1]. The derivative bound for squaring is therefore two, so the accumulated F-grid error is below `(2^b-1)/F<1/H`. The final conversion costs less than 1/H. Together these give `(b^2+2)/H`. At d>b, the discarded weight is below exp(-b)<2^(-b). The strict-versus-nonstrict cutoff boundary d=b is handled by the retained branch.

At d=0, every integer step is exact and the returned weight is exactly one. Thus max shifting protects every attention or vocabulary row from an all-zero denominator, even if other weights are deliberately truncated to zero. This is not an underflow assumption or an unshifted evaluation of a huge positive exponential.

## 2. Mass-preserving rounding: the adversarial residual case

Let S be the positive integer weight sum and `a_j=floor(H Z_j/S)`. The residual `R=H-sum a_j` equals the integer sum of fractional remainders, so `0<=R<m`. Adding a unit to any R distinct coordinates is legitimate without sorting. Even if a selected coordinate had zero fractional remainder, its error is exactly 1/H, not larger. Hence the source's non-strict coordinate bound is the correct one; a strict bound would fail in that case.

The resulting entries are nonnegative and sum exactly to H. An entry cannot become larger than H, since that would contradict the nonnegative total-H invariant. Normalization of the approximate unnormalized weights costs at most m epsilon_w in TV, using the exact weight sum of at least one. The residual redistribution adds at most m/(2H), giving the stated epsilon_g bound. The analysis pays m<=L for an attention row and m=A for the final output.

Onehot-valued aggregation therefore produces an exact grid simplex, rather than separately rounded coordinates whose total mass is uncontrolled. This is essential for the later normalization and KL argument and is explicitly implemented.

## 3. Logarithms: no hidden exact-rational denominator or missing rounding term

The integer range reduction and atanh series are valid at r=0 and at the log-2 endpoint r=1/3. The finite Horner reference values are at most 9/8. Since the rounded r and q do not exceed their references, `q_tilde<=1/9` and `|q_tilde-r^2|<2/F`. The coefficient floor, product floor, and q perturbation give the displayed recurrence

    e_t <= (17/4)/F + e_{t+1}/9,

whose geometric sum is strictly below 5/F.

The final product constant was a specific adversarial check. Before multiplication by two, its error is bounded by

    (9/8)/F + (1/3)(5/F) + 1/F.

After multiplication by two this is less than 8/F. Thus that constant has not silently omitted the approximation to r, the accumulated Horner error, or the final product floor. The series tail is below `3^(-2b)<H^(-3)`, giving less than 9/F overall.

Multiplication by k and addition of the mantissa logarithm cost at most `9(s+1)/H^2`. Nearest H-grid rounding, not floor rounding, contributes at most 1/(2H). The stated `H>=18(s+1)` therefore proves the 1/H log-position error. The j=1 output is exactly zero. All recurrence denominators are handled by bounded integer division on the F grid; no exact-rational Taylor denominator growth is hidden in the work bound.

## 4. Gate snapping, zero counts, and earlier rows

Every needed data lag is at i>=A+2>=4. The exact copy wrong mass is below 1/16, and the allowed numerical error of 1/32 still leaves a strict gap to both snapping thresholds. Numerical attention is a simplex, so every copy coordinate remains in [0,1] even at early invalid positions. The two-hinge map also remains in that interval. Consequently the validity flag forces invalid context gates to zero exactly, while all valid context gates and the terminal query are exact onehots.

The candidate does not need an unproved simplex invariant for every earlier selected p vector. A crude all-position bound suffices: each row-head coordinate and query-gate coordinate lies in [0,1], so the selected coordinate is at most A^2. At the actual terminal, exact onehot selection gives the required exact numerical simplex. Later keys and values read their designated raw position/log coordinates, not an earlier selected probability. Thus a nonterminal selected vector cannot contaminate terminal counting or readout through an unmentioned dependency.

The first-BOS marker and all A smoothing tokens remain present. A uniform row has all returned exponential weights equal to one, and its mass-preserving grid rule approximates each 1/i weight within 1/H. Zero selected-row counts and the shortest N=2 word are included; the statistical V expression is not evaluated at n=0.

## 5. Broad-to-narrow propagation and support

At the terminal, the broad score is `(p_b+1/2+z)j-z j^2`. The p and z ports therefore give the stated sup-score cost, including the additional score port, of at most 3/(64L). Its effect on the position mean is at most 3/64. Adding mean evaluation and using the clipping map's two-Lipschitz bound yields the stated `20+1/8<21` center error.

The narrow-head proof correctly compares its numerical score distribution with the exact narrow Gaussian at the **computed clipped center**. It does not propagate the center discrepancy from the original exact network through an unnecessary L-sized narrow-score sensitivity. This comparison is legitimate because the inherited geometric-mean lemma holds uniformly at every center in [0,L]. The implemented score itself remains exactly the prescribed narrow-head score for its computed input.

Score perturbation is first compared using exact logarithmic values; only then are value and mean-evaluation errors added. Thus the unperturbed log L range is not illicitly applied to perturbed values. The resulting eta bound implies the less-than-one geometric-mean perturbation and the coordinate error at most 46 from Lp_b. The normalization argument uses only that terminal p sums to one, not that the clipped centers or geometric means sum to L.

The explicit logit bounds imply `R_star_b>=1/(2AL)`. The final coordinate port leaves at least `3/(8AL)`, which is stronger than the claimed `1/(4AL)`. The TV rounding contribution is at most 1/(16L). This proves the displayed TV envelope and, through the proven floor and zero-sum squared-error inequality, the forward-KL penalty. True probabilities may be zero. Positivity is not inferred merely from small TV or from exact-real exponentials.

## 6. The chosen budget and exact score grid

For s>=3, the elementary growth argument proves `b^2+3<=2^(5s)`, hence epsilon_g<=2^(-27s). Since L<=2^s, epsilon_g and 1/H are both at most `1/(256L^3)`. These bounds imply every stated port, including the extra H-grid rounding of the weighted logarithmic mean and the final A epsilon_g term. The latter also uses A<=L. No small-A, short-word, or zero-count exception was dropped.

The reference's kappa is an integer. Cancelling the query's factor kappa against the attention divisor is exact rational algebra; it does not require a dyadic representation of 1/kappa or a rounded square root. All remaining score operations use integer positions, dyadic activations, and fixed dyadic coefficients. H is divisible by the denominators in the snapping/clipping formulas. The broad means are exact H-grid sums after weight approximation. Weighted log means initially use the H^2 grid and are explicitly rounded back to H before final vocabulary softmax. These facts justify the claimed exact H-grid score inputs.

Precision chosen for the observed prefix is a length-dependent evaluation resource, not a changed learned coefficient. Full supports j<=i are retained; the evaluator does not supply an earlier row with future keys or source-specific statistics.

## 7. Signed range, guard bits, work, and storage

Raw signed score numerators must be stored before max shifting. Copy scores have O(L^3) magnitude, narrow scores O(L^2), and the quoted broad O(L) range is terminal only. The crude earlier-position p bound above permits larger polynomial broad scores, but still only O(log A+log L) magnitude bits. The clipping formula bounds every computed center in [0,i] independently of the earlier selected p magnitude. Signed differences and exact row maxima therefore fit the source's growing-integer model.

An F-grid product in repeated squaring may need approximately 4b bits before division. Other exact products, dense linear accumulations, and row sums add only O(log A+log L) magnitude/guard bits to the relevant scale. The common fractional precision b is therefore consistent with the stated `O(b+log A+log L)` working integer lengths and constant-factor wider temporaries. It would be incorrect to use only b total signed bits or a fixed exponent range; neither is certified by this note.

Schoolbook multiplication/division at these lengths has O(b^2) cost because b is proportional to log(AL). A shifted exponential uses b squarings, and a generated logarithm uses b Horner terms, giving the stated b^3 charges. The active-head count gives the claimed causal score-pair count. Vector aggregation and dense projection/FFN work fit the displayed `A^3 L^2+A^6 L` multiplier. Mass-preserving residual allocation is linear in row length and needs no sort. Its normalization divisions are included in the b^2 work allowance.

Streaming one row's attention weights fits within the `A^3 L b` activation allowance. Positional/log tables and the stored per-position activations are included. F-grid scratch or cached Horner coefficients fit the conservative b^2 term, and dense fixed parameters fit the stated `A^6 log(A+2)` term. A full L-by-L attention matrix is not needed. The bounds are conservative analytic bit-complexity statements, not runtime measurements.

## 8. Failure examples and limits

The final-zero example is a valid warning for coordinatewise nearest rounding on a fixed grid: an O_A(1/L) coordinate eventually rounds to zero while the constant-word event still has positive probability under an IID source with positive true probability for that symbol. The reciprocal-to-zero example also checks: the increasing exponential tilt has mean greater than L-2, and at L>=10 the clipping sends every center to L, producing uniform output. Max shifting is necessary to avoid assuming an unbounded hardware exponent range.

The dyadic-grid lower statement uses both the positive-support requirement and the all-history O_A(1/L) approximation. On the constant word, the positive output coordinate is simultaneously at least 2^(-b) and at most C_A/L, giving the stated logarithmic lower growth within that encoding class. It is not a lower bound for all representations or a necessity proof for the coefficient 32 or the chosen port exponents.

The exact source passes. This report does not certify generic IEEE execution, a fixed total word length, automatic mixed precision, every implementation of the algorithm, training attainability, or an optimal precision schedule. The existing exact-real source remains unchanged; incorporation of this separately reviewed upgrade should retain these numerical-model limitations.
