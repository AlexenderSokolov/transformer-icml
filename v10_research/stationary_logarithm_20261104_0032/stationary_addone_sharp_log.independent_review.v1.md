# Independent adversarial review: stationary full-history add-one bound

Review date: 4 November 2026 (UTC).

**Verdict: the mathematical proof in Sections 1–6 passes this independent analytical review.** No mathematical defect was found. The stationary upper bound proved by the reviewed file is

    E D_KL(p_{Y_n} || B_{Y_n})
      <= min{log(n+A),
             14000 A^3/(n+1) [1+log_+((n+1)/A^3)]}.

This verdict concerns the exact source bytes below. It is not a literature-priority claim. The source's comparison with the external HJW lower theorem remains subject to the separately recorded primary-source audit; this review did not independently re-read that paper.

## Exact source binding

- Source: `stationary_addone_sharp_log.candidate.v1.md`, in this directory.
- SHA-256: `90e949efc52cd8f3d57108ca334f9083a9858950183dd8e6f60d6664d92c6195`.
- The hash was independently checked before this review was written.
- Method: direct symbolic and probabilistic audit. No numerical experiment, simulation, training, external upload, or repository mutation was performed.

## 1. Stationarity, terminal selection, and the two initial-density bounds

The observation convention is internally consistent: the n observed pair-chain transitions have departure indices 0 through n−1, whereas Y_n is the actual terminal context. No departure from Y_n is included. The likelihood uses exactly those n observed transitions, so terminal selection does not require an additional likelihood factor.

The fixed-target occupation bound is valid. Restricting a length-n terminal event to its length-l suffix and using stationarity gives b_l >= b_n. A fixed path has at most w times that are among its first w visits to s, so summing b_l gives (n+1)b_n <= w. Consequently both P(E_{s,m}) <= 2m/(n+1) and P(E_{s,m}) <= pi(s) hold before any tilt.

The excursion comparison is also valid, including reducible and periodic chains. A state with pi(s)>0 belongs to a finite closed irreducible class. The row tilt preserves its transition support. Expected excursion visits away from s are linear in the first-departure probabilities because the two kernels agree until the next hit of s. Visits to s within an excursion equal one. Thus

    r_min v_P <= v_Q <= r_max v_P,
    r_min <= L_Q/L_P <= r_max.

Keeping stationary class weights unchanged gives two distinct, valid inequalities:

    pi(z)/nu(z) <= r_max/r_min = exp(|lambda|),
    pi(z)/nu(z) <= [pi(s)/nu(s)]/r_min.

On unaffected classes the ratio is one, and the second right side is at least one. States of zero stationary mass do not occur in the sampled path.

It is important to use these as two separate comparisons. Applying only the second inequality to the occupation bound under Q would leave an uncontrolled factor pi(s)/nu(s). The reviewed proof correctly avoids that mistake: the first comparison produces the 2m/(n+1) bound and the second produces the pi(s) bound.

For q>p, k >= jq+1 implies −(k−jq)lambda <= −|lambda|. For q<p, k <= jq−1 gives the same conclusion. Since log(1/r_min) <= |lambda|, the one-count shift cancels the initial-density cost in both comparisons. Taking the minimum of the two separately established probability bounds is legitimate and yields

    P(E_{s,m}, shifted one-sided event)
      <= min{2m/(n+1), pi(s)} exp[−m d(q||p)].

There is no conditional-binomial assertion or independent-test-context substitution.

## 2. Bernstein conversion and scalar KL integration

The Bernstein variational calculation is valid for either sign. Substituting a=delta/(p+delta/3) into the displayed moment-generating-function bound gives delta squared divided by 2(p+delta/3). The proposed delta makes that quantity at least t/m.

The event with threshold sqrt(4jpt)+4t/3+1 is contained in the shifted one-sided events because j delta <= sqrt(4jpt)+4t/3. When p plus or minus delta leaves (0,1), the corresponding strict deviation event is impossible; no invalid endpoint tilt is needed. The cases p=0 and p=1 have deterministic counts.

All algebra in the scalar h lemma checks. In particular, its premise gives

    z <= 2k+10u/3,
    (k−z)^2 <= 8ku+128u^2/9,
    ((j+1)p−k−1)^2 <= 16ku+31u^2.

Splitting according to k+1 >= u or k+1 < u proves the stated 48u(1+log u) bound. The exact row identity is correct and avoids a nonzero first-order error after summing coordinates.

For t>=1 the extra unit in the deviation threshold is absorbed by using u=4t. The function f_m(t)=576t(1+log t)/m is a valid monotone upper threshold. Layer-cake integration with P(E)<=beta and the two-sided tail 2 beta exp(−t) gives

    E[1_E Z] <= [576+3456/e] beta/m < 2304 beta/m.

Thus the large-count full-row estimate 2304 A beta/m is established, with no hidden dependence on p, m, A, or the stationary mass.

## 3. Low-count loss estimate and endpoint cases

The exact alternative KL decomposition is correct. On a band, j+1<=2m because j is an integer and j<2m. If

    log_+((j+1)p/(k+1)) > log 4,

then j>=1 implies k+1 < (j+1)p/4 <= jp/2, hence k < j(p/2)−1. This is contained in the required shifted lower-tail event for q=p/2.

The binary-KL bound d(p/2||p)>=p/8 follows from the second derivative lower bound 1/[t(1−t)] >= 1/p on [p/2,p]. For 0<p<1 all tilted supports are preserved. For p=1 the relevant positive log is identically zero, and p=0 contributes zero after weighting. In particular, no unsupported p=1 tilt is used.

The deterministic positive-log cap log_+(2mp), combined with the tail exp(−mp/8), makes arbitrarily small positive probabilities harmless. The bound

    log 4 + log_+(2z) exp(−z/8) < 10

follows from log_+(2z)<=2z and sup_z 2z exp(−z/8)=16/e<8. Multiplication by p_b before summing coordinates is essential and is done correctly. The result is the full-row estimate

    beta [10+log(1+A/m)],

not an estimate with an extra alphabet factor.

## 4. Dyadic summation and all parameter regimes

The bound sum_s beta_{s,m} <= min{2A^2m/(n+1),1} follows directly from summing the two pointwise bounds. The partition into low bands m<A, middle bands A<=m<=T, and high bands m>=A with m>T is exhaustive and disjoint. Extending the finite collection m<=n to an infinite positive series is safe.

The low-band geometric sum is at most (20+6 log 2)M < 26A, giving 52H. The middle-band count is at most 1+log(T/A)/log 2 when T>=A. The high-band reciprocal sum is 2/m_0<2/T. These produce the constants 52H, 4608H plus its logarithmic term, and 9216H respectively.

When T<A, the middle range is empty; the displayed positive bound remains an upper bound, and the high-range estimate remains valid. When A>n, some formal bands are absent, which can only decrease the result. Thus no unmentioned assumption such as n>=A^3 is needed.

For J_{Y_n}=0, add-one is uniform and its risk is at most log A. The terminal occupation bound gives a contribution at most A^2 log A/(n+1) <= H. Combining all terms gives 13877H plus the stated logarithmic coefficient. The replacement by 14000H[1+log_+((n+1)/A^3)] follows from log 2>=1/2 and T/A=(n+1)/(2A^3).

Finally, B_s(b)>=1/(n+A) makes log(n+A) a valid pathwise cap. The separate n=0 statement is correct. All claimed constants are conservative rather than dependent on asymptotic notation.

## Scope of the accepted conclusion

The accepted conclusion is a stationary, actual-terminal, full-history add-one upper bound with the displayed growing-alphabet dependence. The proof does not establish the same result under arbitrary initialization and does not, by itself, establish literature novelty. The generalization to D contexts and A outcomes uses the same proof when the stated row tilt is a legal kernel and the observed likelihood has the asserted row-count form.
