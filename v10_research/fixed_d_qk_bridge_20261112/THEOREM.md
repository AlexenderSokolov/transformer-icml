# Explicit D-stage source-average risk bridge under realized global QK budgets

2026-11-12. Continuation of the independently reviewed two-read bridge. This is an explicit induction under layerwise homogeneous raw maps and complete-score budgets, not a theorem for arbitrary positional-value Transformers. No novelty claim is made; the ingredients are established source covariance, softmax sensitivity and mean-field comparison.

## 1. Source and complete computational contract

Let N>=2, n=N+1, c in (0,1/2) fixed. Use P_theta(z|xy)=(1+theta xyz)/2, |theta|<=1-2c, with uniform initial pair. Every raw marginal is fair and the final pair tau is uniform on four values. A terminal row initialized from public N and optionally the actual free endpoint pair is appended; every read is full self-inclusive causal attention. Thus raw rows never see the terminal initialization.

All raw embeddings are the SAME token-only map h0(X_i). At each stage ell=0,...,D-1, every raw row undergoes

    h_i^(ell+1)=F_ell(h_i^ell+O_ell A_i^ell).

F_ell is identical across raw positions and L_ell-Lipschitz on the reached comparison domain; ||O_ell||op<=Lo_ell. The value map v_ell is identical across raw positions, bounded by V_ell and Lv_ell-Lipschitz on a common radius-H state domain. Actual full positive-epsilon PreLN and FFNs are included in these constants. A separately specified terminal map/value depending on public/free tag is permitted only with the SAME uniform bounds, or enlarged bounds that are charged.

COMPLETE scores are q_i^ell dot k_j^ell, up to a row-constant offset that cancels in softmax. Any other additive positional bias must be included in the controlled factorization or separately bounded and charged. In particular, Q=K=0 does NOT control an independently supplied predecessor-indicator bias. At every stage and EVERY row, the actual realized query norm is <=Q_ell, the realized key PREFIX has Frobenius norm <=Fkey_ell, and a representative complete score vector after the permitted row shift lies in [-S_ell,S_ell]. A whole realized key-array bound implies the prefix bound. These are not merely learned-projection or per-key norm bounds.

Queries/keys can evolve and depend on actual contextual states. No Lipschitz constant for their state dependence is needed by this proof, because it compares actual scores directly with zero scores using their realized budgets. Positional information can enter only this charged score mechanism; it cannot bypass the homogeneous raw embedding, value or residual maps. Raw states must not receive the free terminal pair or any uncharged global statistic. Parameters and computational rules are theta-independent.

True states stay in the common state domain. Reference states may be projected onto its radius-H ball, fixing true states nonexpansively. Value bounds/Lipschitz constants and local-map domains must include these reference comparisons. A final scalar probability readout is Lout-Lipschitz on the common domain, uniformly in public/free tags. There is no additional historical-row read after the D stages in the first version below. All gains may depend on the declared architectural resources; their N or depth dependence must remain explicit.

## 2. Explicit reference and recursion

Let kappa_c=sqrt(4+8/c²). Define two deterministic raw branches bar_h_ell(+),bar_h_ell(-), shared across all raw positions, and one reference terminal bar_hT_ell(tau). Initialize them with the actual embeddings. Put

    mu_ell=[v_ell(bar_h_ell(+))+v_ell(bar_h_ell(-))]/2,
    bar_h_(ell+1)(s)=Pi_H F_ell(bar_h_ell(s)+O_ell mu_ell).

For the terminal use its actual public/free-tag local maps and the reference uniform average

    [N mu_ell+vT_ell(bar_hT_ell(tau),tau)]/n.

This produces bar_hT_(ell+1)(tau). All references are theta-independent. Causality ensures raw references need not acquire tau dependence.

Define E_0=0 and

    C_ell=V_ell exp(2S_ell)Q_ell Fkey_ell,
    u_ell=L_ell Lo_ell [C_ell+kappa_c V_ell],
    B_ell=L_ell(1+2Lo_ell Lv_ell),
    E_(ell+1)=B_ell E_ell+u_ell.                         (1)

Then for every admissible theta,

    E_theta||h_i^ell-bar_h_ell(X_i)||<=E_ell/sqrt(i), i<=N,
    E_theta||h_T^ell-bar_hT_ell(tau)||<=E_ell/sqrt(n).     (2)

The exact accumulated constant is

    E_D=sum_{ell=0}^{D-1} u_ell product_{r=ell+1}^{D-1} B_r.

If B_ell<=B>1 and u_ell<=U, E_D<=U(B^D-1)/(B-1); for B=1, E_D<=UD. These expressions expose rather than suppress the price of repeated layers.

## 3. Proof of the recursion

For a fixed stage and query, first replace the ACTUAL attention weights by uniform weights while retaining the actual evolved values. The softmax Jacobian estimate gives the deterministic read error <=C_ell/sqrt(i). This step is pathwise and does not require the query to be independent of the source or close to its reference query. The COMPLETE-score restriction is essential here.

Next replace actual values by reference-bank values. Their mean expected error is at most

    (Lv_ell/i)sum_{j<=i} e_j^ell,

using the terminal reference at j=n if present. Last, replace the raw reference-bank empirical values by their fair-sign mean. The standard fixed-c dimension-free covariance estimate gives a read error at most kappa_c V_ell/sqrt(i). The reference raw map is token-local and identical across positions even though actual contextual states are not.

At the terminal, the self value cancels EXACTLY in this last empirical-to-mean comparison. The leftover random vector is n^-1 sum_{j<=N}(v_ell(bar_h_ell(X_j))-mu_ell). Its unconditional expected norm is <=kappa_c V_ell sqrt(N)/n<=kappa_c V_ell/sqrt(n). There is no conditional-independence claim, no conditioning on tau, and no factor-four loss. Uniform Lipschitz bounds in tau then transfer the comparison. Merely supplying tau does not make the raw reference branches tau-dependent because causal raw rows never read the terminal.

After the residual and local map,

    e_i^(ell+1) <=L_ell e_i^ell
      +L_ell Lo_ell Lv_ell i^-1 sum_{j<=i} e_j^ell
      +u_ell/sqrt(i).

Projection onto the common ball is nonexpansive and fixes the true state. Since i^-1 sum_{j<=i}j^-1/2<=2/sqrt(i), induction proves (1)-(2). This argument does not treat actual evolved means as public exact means; it constructs and charges a distinct reference.

## 4. Fully mean-field final readout

Let bar_Q(tau) be the actual final readout applied to bar_hT_D(tau). It is independent of theta, and

    E_theta|Q-bar_Q(tau)|<=Lout E_D/sqrt(n).              (3)

For the equal prior theta=+h,-h, fixed 0<h<=1-2c, the endpoint pair has the same uniform law and the two target probabilities at each pair differ by h. Thus every common template depending only on tau has equal-prior absolute risk >=h/2. Subtracting (3) gives

    R_equal_prior(Q)>=h/2-Lout E_D/sqrt(n),
    max(R_h,R_-h)>=max(0,h/2-Lout E_D/sqrt(n)).           (4)

The freely given pair eliminates an endpoint-retrieval obstruction but not this charged shallow parameter-estimation bound. This is an UNCONDITIONAL expected comparison and needs no factor four; the restricted complete-score/homogeneity structure is what permits it. For a public sentinel with no pair, the template is constant and the analogous fixed-theta risk lower is |theta|/2 minus the same error. For a raw-last-row readout, its reference depends only on X_N; the uniform stationary pair gives the same fixed-theta conclusion with denominator sqrt(N).

## 5. Variant retaining the last count summary

Sometimes it is preferable to retain the sharper observed last-stage statistic and import the previously established count Bayes risk B_N. Run recursion (1) for the first D-1 contextualization stages only. At the last terminal retrieval, replace actual scores by uniform weights, then actual evolved values by their reference values, but do NOT replace the final raw empirical value sum by its expectation.

The resulting last read is a function of (S_N,tau), because v_(D-1)(bar_h_(D-1)(s)) is identical at all raw positions. The previous terminal residual is a function of tau. If the entire final decoder is G-Lipschitz in the concatenation of the last head output and that residual, then

    E|Q-Q_countref| <=G[(1+2Lv_(D-1))E_(D-1)+C_(D-1)]/sqrt(n),
    R_equal_prior(Q)>=B_N
      -G[(1+2Lv_(D-1))E_(D-1)+C_(D-1)]/sqrt(n).          (5)

There is no extra last-stage covariance term in (5), since the empirical count summary is retained. For D=1 this is the original single-read bridge; D=2 recovers the new independently reviewed two-read extension. For D>=2 the earlier-stage covariance terms generally remain nonzero even when all QK arrays are zero. The explicit zero-score two-read counterexample proves that deleting those terms would be false.

## 6. Limits and relation to previous work

This is a fixed-D statement with explicit constants, and also a valid growing-D bound while those constants and domains remain as declared. Under uniform B,U it produces only the familiar logarithmic-depth necessary scale for fixed risk, not a super-logarithmic lower bound or sufficient construction. It does not settle fixed-inner-width optimality or vanishing-risk rates above that scale.

The earlier general mean-field argument allowed more positional heterogeneity and paid query-branch/endpoint comparisons differently. Here the complete-score Frobenius budgets permit a different comparison order, and homogeneous raw maps permit a shared token-only template; these restrictions explain the simplified constants, not a free strengthening for arbitrary architectures. Public additive biases, position-dependent raw values/residual channels, globally supplied context, additional decoder reads or uncharged growing gain invalidate the respective hypotheses. Standard projection bounds imply realized key-array Fkey=O(sqrt(N)) in general and need not give a useful conclusion.

No new numerical experiment is required for the mathematical induction. The two-read counterexample and its finite diagnostics remain at their original paths. Its conservative numerical bridge upper bounds all exceeded one and were quantitatively vacuous; the induction must not be advertised as empirically certified by those tests.
