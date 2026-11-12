# Independent fixed-D realized-QK mean-field bridge review

2026-11-12. Reviewed THEOREM.md. No mathematical gap found under the complete-score, homogeneous raw-map, common-domain and no-bypass hypotheses. This is an analytical review, not a new numerical experiment or novelty certification.

## Recursion and score gauge

The comparison order is valid and important: actual scores -> uniform actual values -> uniform reference values -> fair-token reference mean. Because the first replacement is pathwise on each actual execution, no state-Lipschitz bound on Q or K is needed. The full realized key-prefix Frobenius bound must hold at every row and stage. It is not replaceable by a learned projection norm.

The softmax estimate remains valid when the bounded score representative is specified only up to a row offset: along the interpolation, softmax and its Jacobian annihilate the constant offset, while the unshifted factorized vector has norm <=Q Fkey. Thus the same e^(2S)QFkey bound applies even if the chosen bounded representative is not literally Kq. An uncontrolled non-row-constant additive bias would break this argument and is explicitly excluded.

The value replacement contributes L Lo Lv times the prefix average of earlier state errors. Residual error contributes L e_i. Combining with the raw covariance/score forcing and prefix inequality gives exactly

    B_l=L_l(1+2Lo_l Lv_l),
    u_l=L_l Lo_l V_l[e^(2S_l)Q_l Fkey_l+kappa_c].

The convolution formula for E_D and its geometric upper bound are correct. Projection is legitimate because it fixes every actual state and all comparison domains/Lipschitz bounds explicitly include projected references.

## Terminal pair and risk

Causality keeps the raw reference branches independent of the terminal pair. They are also position-identical because the embedding, value and local residual maps are homogeneous across raw rows. The terminal reference can depend on the free pair but not theta.

The terminal reference self value cancels identically in the empirical-to-mean step. The remaining discrepancy is an unconditional raw sum, with norm concentration uniform over the tag. Thus no conditioning penalty or factor four is missing. This does NOT follow merely from terminal-pair uniformity; it relies on the displayed cancellation and raw-reference independence from the pair.

For the +/-h prior, the pair has the same uniform distribution at both parameters, and targets differ by h at each pair. A common pair-dependent template therefore has averaged absolute risk at least h/2. Subtracting Lout E_D/sqrt(n) is valid. The public-sentinel and raw-last-row observations are consistent with the uniform stationary pair, subject to their corresponding input contracts.

The count-retaining variant correctly omits only the FINAL covariance term. Earlier source fluctuations persist through E_(D-1), even when every score is zero. Its G must cover the whole final decoder as a function of both read and prior terminal state; no extra history read is allowed. D=1 and D=2 specialize correctly.

## Difference from the older general mean-field theorem

The old construction retained a possibly position-specific reference attention bank and charged state-dependent score sensitivity. This theorem instead pays a fresh score-to-uniform error at every actual stage. Its forcing depends on global realized key-prefix Frobenius budgets, and its simplified recurrence has no score-state sensitivity term. Identical raw maps make the reference shared across positions and permit the terminal cancellation directly.

These are substantial restrictions, not a stronger theorem for every old architecture. In particular:

- ordinary per-row key bounds can make Fkey=Theta(sqrt(N)), rendering this theorem vacuous;
- positional value or residual features destroy the homogeneous reference and the count-retaining reduction;
- externally supplied predecessor score matrices are not controlled by setting learned Q,K to zero;
- all gain and domain dependence on N and D remains charged;
- the result supplies only the familiar logarithmic-depth scale under uniform budgets, not an improved frontier or a matching upper bound.

The draft correctly labels its earlier numerical constants as vacuous and does not treat the two-read diagnostic as certification of the induction.
