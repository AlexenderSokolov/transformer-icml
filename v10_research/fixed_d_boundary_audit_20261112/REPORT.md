# Which fixed-D hypotheses are essential? Precise counterexamples and non-counterexamples

2026-11-12. This report audits relaxations of ../fixed_d_qk_bridge_20261112/THEOREM.md. It separates failure of an exact summary/proof step from failure of the statistical conclusion. It does not overlap the centered-key norm refinement.

## 1. A global terminal bypass genuinely destroys the risk conclusion

Let theta_hat=clip((N-2)^(-1)sum_{i=1}^{N-2}X_i X_(i+1) X_(i+2),[-a,a]), a=1-2c. Give the terminal this statistic together with the actual endpoint parity tau at initialization. The computation is theta-independent and bounded, but it is a NONLOCAL INITIAL FEATURE, which the theorem excludes.

A broad Lipschitz probability readout Q=(1+theta_hat tau)/2 then has risk <=1/(2sqrt(N-2)) with zero retrieval stages, all QK arrays zero, and fixed bounded state/readout norms. The theorem's public/pair-only reference assumption would incorrectly predict a constant floor if this bypass were ignored.

This also admits an exact ordinary-final-LN softmax realization under the same explicitly enlarged bypass: externally supply l=log((1+theta_hat tau)/(1-theta_hat tau)) and r=sqrt(K²-l²), K>log((1-c)/c), as the terminal state (l,-l,r,-r). Its norm is sqrt(2)K and its mean is zero. With epsilon=1, final LN divides by fixed sigma=sqrt(1+K²/2), and logits (sigma LN_1,0) produce Q exactly. The architecture coefficients remain fixed; the unlicensed resource is computing that global initial encoding, not an unbounded head or a theta-dependent parameter. This is a counterexample only after dropping the initial-history restriction.

Likewise, supplying contextual values v_i=X_(i-2)X_(i-1)X_i directly makes a zero-score uniform read estimate theta. That violates TOKEN-LOCAL value access, not merely position-independence. It cannot be used as a counterexample under the original value contract.

## 2. Position-dependent token-local values break count sufficiency, not automatically shallow risk

Take N=6 and words +++--- versus ++-+--. Their count is zero and endpoint pair is (--), but X_3 differs. Use the bounded position-dependent local value v_i(X_i)=1{i=3} X_i and one uniform read. The output is X_3/6, so any strictly increasing bounded-gain final head separates these words. Thus the exact count-summary reduction is false once position-dependent values are permitted.

This is NOT a constant-risk counterexample. The difference is O(1/N) in its natural extension. More importantly, under the remaining bounded-score/gain/locality assumptions the FULLY mean-field theorem can be repaired with position-dependent references:

    bar_h_{ell,i}(s),
    mu_{ell,i}=i^-1 sum_{j<=i} [v_{ell,j}(bar_h_{ell,j}(+))
                              +v_{ell,j}(bar_h_{ell,j}(-))]/2.

Use the actual public position-specific local map at row i. All these references remain theta-independent. The covariance estimate already allows nonidentical deterministic token-local functions, so the same prefix error induction applies with uniform layer constants. Terminal self-value cancellation still holds. The final pair-only mean-field risk lower therefore survives; only the count-retaining variant loses its summary interpretation.

Consequently homogeneity is sufficient and convenient for the count version, but relaxing it to bounded public position dependence is not by itself evidence against the statistical fixed-D floor. A purported counterexample would need to violate another hypothesis or overcome the existing general mean-field argument.

## 3. Omitting additive position scores breaks the deterministic comparison even when they are bounded

Set learned Q=K=0, raw scalar values V_i=X_i, and let an external public bias be +1 on even keys and -1 on odd keys. At an even terminal index N reading N raw keys, choose the alternating word X_i=(-1)^i. The uniform average is zero, while the biased attention output is

    (e-e^-1)/(e+e^-1)=tanh(1).

All bias entries are bounded. Thus a claimed score-to-uniform error proportional only to ||Q|| ||K||F=0 is false if the external bias is omitted. This is a pathwise counterexample, not an average-risk lower or upper: the alternating word can be exponentially rare under a fixed-c source.

If the external score bound is a fixed constant and all other local gains remain fixed, the earlier general bounded-score mean-field theorem still applies. One cannot turn this pathwise discrepancy alone into a contradiction of its average-risk conclusion.

## 4. Unbounded uncharged local position scores can genuinely remove the shallow risk floor

Here is a counterexample in the broad Lipschitz-block model used to state the fixed-D theorem, not a claimed exact positive-epsilon PreLN compilation.

At every raw row i use two full-prefix heads. Give head k the public bias 4log N at j=i-k (where valid), zero elsewhere; learned Q,K can be zero. All scalar values are the raw signs. The target attention mass is at least 1-N^-3, so each predecessor read differs from its target sign by <=2N^-3.

A fixed-size bounded-slope piecewise-linear local map of (X_i,read1,read2) outputs their triple parity exactly for N>=3: use plateau interpolation at the four sums -3,-1,1,3, with plateau radius1/2. Total sum error is <=4N^-3<1/2. The first two rows can use arbitrary causal target choices. Thus the first stage creates the true innovations on all valid raw rows. A separate permitted terminal map preserves the free endpoint pair and ignores these first-stage read channels.

A second uniform read averages these innovation values, and a bounded Lipschitz probability head combines the clipped estimate with endpoint parity. Boundary/self contributions cost O(1/N); statistical risk is O(N^-1/2). Depth and nonattention local Lipschitz constants are fixed.

What failed is EXACTLY the complete-score budget: the external bias is 4log N, not a fixed S, and not represented in the alleged zero factor norm. If complete S is honestly charged, its exponential contribution makes the old bound vacuous rather than contradictory. The construction does not show a fixed-depth standard-PreLN upper bound, because the abstract parity/local/output maps would require their own actual physical compiler under that stricter class.

## 5. Practical reading of the theorem

- Dropping a terminal/global history restriction can destroy the actual risk lower immediately, even with bounded final full-LN softmax parameters.
- Dropping position homogeneity can destroy count sufficiency while leaving the more general source-average floor intact.
- Ignoring a bounded public score term can destroy the pathwise QK estimate without proving anything useful about typical source risk.
- Allowing an unbounded uncharged score term can support shallow local-statistic computation in the broad model; it must not be described as a bounded-score counterexample.
- None of these examples proves that a particular failed network establishes a lower bound for every network. Each is tied to the precise relaxed hypothesis above.
