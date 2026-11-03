# Independent analytic review: critical-scale risk and moving-target correction

Reviewed `critical_scale_markov_risk_v1.html`, SHA-256 `17e2400856f88047f3376aab80a2062ab13c7e9eb259e9f11db86f6f2a3d4797`, together with mandatory correction `moving_target_l1_clarification_v1.html`, SHA-256 `5894f3e194d1bce9c1b4115b7859d98f432108b20fc05b8554654da90bb798fb`. The review compares the exact-real graph and previously reviewed safe window and fixed-source perturbation; it is not a test, formal verification, generic Transformer claim, or IEEE inference result.

## Conclusion

The claimed actual-terminal expected TV limit 583/3072 and the two Θ(1/N)-scale sufficient/failing examples are supported by the displayed analytic argument, conditional on the previously reviewed architecture and Gaussian bound. Section 2's original phrase “same limit in L1” must be read with the correction: the moving comparator need not converge; the necessary statement is E|P_N−p_(X_(N−3),X_N)|→0. The correction preserves the risk limit and its quantifiers. The transition constants are not claimed optimal, monotone, sign-symmetric, or applicable to other perturbations.

## Score gap and indices

With L=N+2, D=L+2, r=i−1 and ζ=2r/D, the nearest integer to the center r−ζ changes at r=D/4 and 3D/4. Ties lie in the excluded H-neighborhoods. The winner is r−d, with d=0,1,2 over deterministic fractions 1/4,1/2,1/4. Since i≥H on retained rows, the winner is a data key for sufficiently large L. For i<D/8, ζ<1/4 and the gap is at least i/2≥H/2. For i≥D/8, the distance of r from each switching point exceeds H, so the adjacent-score gap is at least (1+2/L)i·4H/D≥H/2. If any row survives, H<D/4: otherwise the three excluded regions cover the possible range. Thus the artificial outer half-integer boundaries are not closer competitors; restricting to valid causal keys cannot decrease the gap. With at most L keys, wrong mass is at most Le^(-H/2)≤L^-49<1/4, and the snap is exact. Exceptional rows are O(log L), including integer/half-integer boundaries.

At data k=i−2, the snapped lag-one target is X_(k−1−d), whereas lag two is X_(k−2); the three anchor pairs in the draft follow. At terminal i=L, ζ=2−6/D, so the nearest integer is d=2 for L>10 and, for sufficiently large L, its score gap also passes the snap test. Thus terminal query is (X_(N−3),X_N), rather than an independent draw. The asymptotic argument does not require extending this terminal formula to the finitely many smaller N.

## Anchor and true-risk accounting

The ordered pair law is uniform. In the first and last bands each anchor has frequency 1/4, weighted by segment length 1/4. The middle band has only diagonal anchors, each with probability 1/2, weighted by segment length 1/2. Given (X_(k−3),X_(k−2))=(b,a), t_ba=(1−θ_ba)θ_a0+θ_baθ_a1, yielding t00=9/16, t10=11/16, t01=t11=3/8. The stated denominators and numerators follow. The four ratios simplify to 61/96, 19/32, 5/16, 19/48 in the 00,01,10,11 order.

Stationary ergodic prefix averages and differences of prefixes justify the three growing deterministic intervals. The O(log N) exceptional keys, BOS terms and nonmatch weights are negligible compared with Θ(N) good matching keys for each anchor. The four anchor outputs converge almost surely to constants. The corrected moving-target error is bounded and tends to zero almost surely, so its expectation tends to zero; the uniform 168/sqrt(N+2) fourth-block error also vanishes.

For a=X_(N−3), b=X_(N−1), c=X_N, summing over the intermediate bit gives P(a,b,c=0)=(7,10,9,6)/64 in 00,01,10,11 order. For c=1, P(a=0,c=1)=15/64 and P(a=1,c=1)=17/64, with target 1/2 for either b. The corresponding weighted absolute errors sum to (447+414+135+170)/6144=583/3072. Stationarity makes this comparator-risk expectation independent of N≥4; the reverse triangle inequality and the corrected L1 difference give the claimed limit.

The safe-window sufficient bound is |η|≤1/[8(N+2)] for either sign, while this particular positive η_N=2/(N+2) fails at the displayed fixed stationary source. The perturbation changes one Q scalar by 4η_N=8/(N+2), and the perturbed weights vary with N. None of this identifies a sharp numerical critical constant.
