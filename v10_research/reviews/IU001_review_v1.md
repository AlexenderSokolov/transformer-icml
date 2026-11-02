# IU001 independent mathematical and resource review v1

2026-11-02. **Independent assigned LLM review, not formal validation, external peer review, cross-model replication, novelty certification, or emitted-network verification.** The review examined a completed candidate proof in the supplied research context. No author or accepted source file was edited. No LLM reviewers or external publication/contact actions were used.

## Result first — ACCEPT within the stated scope

The frozen IU001 proof supports its beta-sensitive upper bound for **exactly the unchanged accepted NB002 finite predictor**, for every integer K>=2, M>=1, h>=4 and every beta in (0,1], uniformly on the full all-state D2(beta) class with arbitrary initial pair law and actual-terminal expected-TV loss:

    risk <= min(1, 2^16 L
                   +(K^3/Q)[8360+456 ln(1+(480/76)Q/(beta K M))]
                   +9K/Q+4 epsilon_beta(M)).

The 8363 absorption and the simpler 2^14 version are valid. With the exact public SM001 half-log schedule, the claimed O_(K,c)(L) guarantee is uniform over beta sqrt(M+1)>=c, for every fixed K and c>0. The old all-beta Psi upper, including beta=0, and the SM001 reciprocal upper remain separately available.

No mathematical, source-access, permission, or resource blocker was found. No correction to the frozen candidate is required. Acceptance is **upper-only**: it does not establish a matched intermediate-beta frontier, globally adaptive precision-budget selection, sharper joint-K optimality, lower total arithmetic word/storage cost, or training/fault guarantees.

## 1. Exact object and inherited interfaces actually inspected

Frozen candidate:

`v10_research/intermediate_upper/IU001_beta_sensitive_precision_upper_v1.md`

SHA-256: `4c0adb15aadfb574e156c5ce5f4f4da1ec8447ed515417a71d400c5a52c7b317`.

The following load-bearing source bodies were read, not merely their verdict labels:

| Source | Actual SHA-256 | Use |
|---|---|---|
| NB002 conservative guard proof | `dcf815879aebe23d189403efb5c26e53f64ca8718ffc101b517097a3a32251d3` | Actual finite predictor, pathwise error/safety bounds, all five statistical cases, guard and full ledger |
| SM001 strong-mixing proof | `3d4bdb15966a79cb67766e91babee3b81017376a79f42c8c4141bfd85a7aa78d` | Explicit pre-integration reduction, complete-suffix transfer, exact public schedule |
| R011 all-parameter proof | `1b7133c69131b84c6e7e235338797e683eaa2c0e73b9c83a26612e344f78039d` | Exact source experiment, all-state minorization, actual terminal query, scale L and minimax lower |
| NB002 independent review | `3c605fddbf1be89781fd03bc8d83d72cab02d752cfae5c98d6c9169a46e49dd1` | Accepted source/interface scope and known statistical hazards |
| SM001 independent review | `a4939edd70d14a228f85b3b5ab87020561c03e9c00b17bd0c0130d28dea27388` | Accepted pre-integration and resource scope |

The exact finite weights, ordered normalizers, integer Z guard, pooling ties and output mux are unchanged. The inherited reduction is genuinely available **before** numerical occupancy integration:

    risk <= min(1,2^16 L+3 E_mu min(1,E/(J+K))
                         +P_mu(J+K<4E)+9K/Q), E=76KM/Q.

This is not inferred by inverting NB002's Psi bound or by treating scalar ALG risk as a count-radius estimate. In the radius-safe branches, NB002 actually bounds E(e+2rho) by 2^16 L using the proper count-radius certificates. Near IID, rejection-set containment gives pooled loss plus CT and the active-GT tail, bounded by 8000L, with extra error <=v+8K/Q. That is dominated by the common surcharge above. The finite exceptional cases have 2^16 L>=1 and are legitimately handled by the loss cap. The false unconditional NEXT statement is not used.

I did not reopen every transitive historical predecessor or re-prove the accepted neural prefix. Their unchanged scope is inherited through NB002/SM001, rather than presented as newly verified from scratch. The companion binding file distinguishes these inherited/hash-checked sources from sources read for the present new proof.

## 2. Actual-terminal reversal and first returns

Stationarity implies that S=supp(pi) is closed. On S, P*(s,t)=pi(t)P(t,s)/pi(s) is stochastic and pi-invariant. For each stationary path, the complete product identity

    pi(y_0) product_j P(y_j,y_(j+1))
      =pi(y_M) product_j P*(y_(j+1),y_j)

proves the full reversed path law conditional on the actual endpoint. It does not replace that endpoint by an independent pi draw. The original departure count becomes the number of positive-time visits Z_1,...,Z_M to Z_0=s. Multiplication of reverse transitions gives

    (P*)^2(s,t)=pi(t)P^2(t,s)/pi(s)>=beta pi(t).

Every division is on positive support; no reverse kernel off S is needed. This also covers nonreversible forward chains.

For a fixed s with p=pi(s)>0, each positive even skeleton step has conditional hit probability at least beta p. Thus the positive full-chain return time is at most twice a geometrically dominated skeleton hit time, proving E_s tau_1<infinity before the stopped occupation vector is introduced. This rules out a circular appeal to Kac.

For u(t)=E_s sum_(j<tau_1)1{Z_j=t}, Tonelli and the Markov property give uP*=u. The initial and final stopped states are both s, and u(s)=1. The normalized u is stationary. The two-step residual kernel contracts TV by 1-beta, so pi is the unique stationary probability on S. At beta=1, (P*)^2=Pi directly; no division by 1-beta occurs. Consequently E_s tau_1=1/p. Successive positive return times are finite, and the discrete strong Markov property gives E_s tau_k=k/p. Since {J_M<k}={tau_k>M}, the integer return tail k/(Mp) follows.

Singleton support is not an exception to this reasoning: the chain restricted to support stays at s, tau_k=k and J_M=M. Off-support forward starts are not used in this stationary return argument; they are handled later by the all-state forward transfer.

## 3. Nonselfadjoint tilted norm and complete spectral comparison

This is the principal new analytic step. It is valid for nonreversible kernels.

For beta<1, R=(H-beta Pi)/(1-beta) is stochastic and pi-invariant, hence an L2(pi) contraction by Jensen. Both constants and centered functions are invariant subspaces. Therefore for arbitrary f,g,

    |<f,Hg>| <= |pi(f) pi(g)|
                 +(1-beta)||f-pi(f)|| ||g-pi(g)||
              <= sqrt(<f,H0 f><g,H0 g>),
    H0=(1-beta)I+beta Pi.

For complex functions one inserts the usual conjugation; all operators here are real and the same norm bound follows. The last inequality is ordinary two-component Cauchy. At beta=1, H=Pi and the same comparison holds directly.

Applying this inequality to Df,Dg and taking the supremum over unit f,g proves the **singular operator norm** inequality ||DHD||<=||DH0D||. No eigenvalue or self-adjoint assumption about H is made. Equivalently, on constants plus centered functions H admits the contraction factorization H=H0^(1/2) C H0^(1/2); multiplying by D on both sides gives the same norm bound. Powers of the nonselfadjoint tilt are then controlled by submultiplicativity, not by an unjustified eigenvalue formula.

For 0<p<1, the displayed 2-by-2 matrix of I-DH0D has exactly

    determinant = a_lambda beta p,
    trace = beta+a_lambda(1-beta+beta p)<=beta+a_lambda.

Positive trace and determinant make both eigenvalues positive. The smaller is det/lambda_max>=det/trace. On the full orthogonal complement (zero at s, centered on its complement), the eigenvalue is beta; this is no smaller than a_lambda beta p/(beta+a_lambda). Thus the comparison does not silently omit a higher-dimensional mode. If support has two states the complementary subspace is zero-dimensional; if p=1 the only eigenvalue is a_lambda. If p=0, the lower-tail event is empty and the state is removed before any division.

With lambda=beta/8 and a_lambda=1-exp(-lambda),

    a_lambda>=15lambda/16, beta+a_lambda<=9beta/8,

so the gap is at least (5/6)lambda p. DH0D is positive self-adjoint, and its norm is its top eigenvalue, hence at most exp(-(5/6)lambda p).

The stationary mgf identity is correct with the paper's row-kernel/function-operator convention:

    E_pi exp(-lambda N_s)=<D1,(DHD)^(m-1)D1>.

This counts all m states, not m transitions. At m=1 the identity uses the identity operator and remains valid. The Chernoff exponent is exactly

    lambda mp/2-(5/6)lambda p(m-1)
      =-beta mp/24+5beta p/48.

Since exp(5/48)<2, Lemma 3.1's constant and exponent follow.

## 4. Conditional tail, layer cake, and arbitrary starts

In the reverse chain started at s, b=floor(M/2) and r=floor(b/2)=floor(M/4). Two-step contraction compares Z_b to pi with error epsilon_beta(M). Applying the same path-extension kernel compares the **entire** suffix Z_b,...,Z_M with that error. The selected times b+1,b+3,... are all positive times, all counted in J_M, and number m=ceil(ceil(M/2)/2)>=M/4. Under the comparator they form a stationary (P*)^2 chain. The desired threshold M p/16 is no larger than m p/2.

Thus the conditional lower tail is at most 2 exp(-beta Mp/96)+epsilon. The bound epsilon<=exp(beta) exp(-beta M/4)<=3 exp(-beta Mp/96) includes M=1,2,3 and beta=1 under the explicit r=0 convention. Lemma 3.2 follows. There is no hidden burn-length restriction.

For the clipped reciprocal, condition on the actual stationary endpoint s and put a0=A/(Mp). If a0>=1/16, the unit cap is at most 16a0. Otherwise split the layer cake at 16a0. For t>16a0 the strict threshold is exactly

    {J_M<A/t-kappa}={J_M<ceil(A/t-kappa)}

whenever positive. With integer kappa>=1, this integer k satisfies k<=A/t<Mp/16. Both the return-Markov tail and Lemma 3.2 apply, giving min(a0/t,q_s), where q_s=5 exp(-beta Mp/96).

The integral over (0,1) is a0 F(q_s/a0), with F(x)=x below one and F(x)=1+ln x above one. Combining the initial 16a0 portion and x exp(-x)<=1 yields

    E_s min(1,A/(J_M+kappa))
      <= a0[17+ln(1+480/(beta A))].

This explains exactly why the logarithm contains beta A. Multiplication by pi(s) only occurs after the valid statewise estimate; it cancels the denominator p and leaves the support size d. It is not an independence argument. Taking the separate cap one is legitimate.

For arbitrary initial laws, J>=J_suf pathwise with the same actual query. All-state minorization, including off-support starts, bounds TV(mu P^b,pi). The same extension kernel bounds the complete forward suffix law, including its endpoint. The clipped reciprocal remains in [0,1] until after this comparison. Thus its transfer costs one epsilon, not an unbounded reciprocal times epsilon.

The bad-event indicator is transferred independently, also at cost one epsilon. If 4A<=kappa it is empty. Otherwise k=ceil(4A-kappa) is a positive integer with k<=4A, and the return-Markov bound at horizon L_suf gives 4dA/L_suf. Since L_suf>=M/2, the two functionals give exactly

    E v <=(2dA/M)[17+ln(1+480/(beta A))]+epsilon,
    P(Cbad)<=(8dA/M)+epsilon.

No endpoint independence, unconditional row-sample IID property, or unclipped TV transfer is used.

## 5. Constants, small cases, and the promised-class corollary

The coefficients compose as

    3*2*17+8=110, 3*2=6,
    76*110=8360, 76*6=456.

The inherited +9K/Q is still present. It cannot simply disappear from the seed's 8360 coefficient. In the frozen candidate it is retained, or absorbed using 9/K^2<=9/4<3. Also

    ln(1+(120/19)x)<=2+ln(1+x),
    8363+912<2^14, 456<2^14,

which proves IU2 with room to spare.

The exact integer schedule h=20+3 ceil(log2 K)+ceil(ceil(log2(M+1))/2) satisfies

    2^20 K^3 sqrt(n)<=Q<=2^24 K^3 sqrt(n), n=M+1.

The upper factor includes both dyadic ceiling effects; no real-log or square-root oracle is required by the configuration. Under beta sqrt(n)>=c and n/M<=2,

    Q/(beta K M)<=2^25 K^2/c.

Moreover epsilon<=e exp(-c sqrt(n)/8)<=8/(c sqrt(n)); the final inequality follows from max_(x>=0) x exp(-cx/8)=8/(ce). This handles small M as well as beta=1. Substitution gives precisely

    risk <= min(1,[2^16+32/c
                    +2^-6(1+ln(1+2^25 K^2/c))]L).

Since L>=1/sqrt(n) and the accepted full-history minimax lower is 2^-17 L, this is the stated constant-order sufficiency on each promised class. K,c dependence is explicit. The algorithm reads neither beta nor c: only the scope of the bound changes. Choosing a precision schedule using an external class promise must remain distinguished from global unknown-beta budget adaptation.

## 6. Full resource ledger and scientific interpretation

I compared IU001 Section 7 with NB002 Section 9 and SM001 Section 8. No operation or online input was added. In particular no reversed-chain simulation, stationary mass, burn, suffix count, spectral tilt, return time, or beta estimate appears in the program.

All previously charged coordinates remain: hybrid depth/width, six heads and QK/score limits, complete product/guard words, dense coefficient slots including zeros/biases, addressed sparse program and holds, masks and positions, observed input, all-token QKV and pointwise work, cached/uncached attention plus real cache creation, finite logarithm/evaluator work and scratch, full offline generation/sorting/selected-format writes, and simultaneous-phase peak sums. The separate PURE expansion is not assigned the smaller hybrid resources.

The word p_word=4h+4ell+64 still includes ell. A smaller master/output h does not remove accumulator bits, historical arrays, masks, offline costs or input conversion. The result is a sharper numerical upper analysis for an existing finite map, not a measured implementation speedup, total-memory separation, architecture-universal precision claim, training theorem or physical-fault guarantee.

The separate SM002 lower is not a premise of the new upper and is not newly re-reviewed here. Nothing in this review turns a valid 1/Q lower or a fixed-positive-beta synthesis into a matching vanishing-beta logarithmic lower.

## 7. Executed independent checks and actual issue disposition

The reviewer script `reviews/IU001_independent_checks_v1.py` passes in **exact Fraction/integer and symbolic rational algebra only**, without floating-point inequalities. It uses six independently specified kernels: nonuniform directed circulation with slow/medium/full refresh and two zero-mass transient states, an asymmetric binary pair chain, rare IID pair chain, and singleton-support pair chain. It checks:

- 156 all-state and 81 reversed-support minorization entries;
- 21 exact first-return means from killed-chain linear equations;
- 1,365 conditional count identities and 1,365 return-Markov thresholds;
- 6,804 complete conditional stationary path identities, not only marginal count laws;
- 84 exact tilted bilinear block-PSD certificates and 84 full-space comparison-gap PSD certificates, including singular beta=1 cases and complement modes;
- 5,760 bounded full/suffix functional cases, including strict bad-event boundaries and off-support starts;
- symbolic determinant and trace cancellations;
- strict integer thresholds, exact constants, and 436 integer public schedules through 4,096-bit horizons.

These finite tests corroborate the proof; they do not substitute for it. In particular the exact rational tilts test the comparison mechanism, while the universal exponential tilt and concentration bound are established by the analytic audit above.

The author's current diagnostic code was read and rerun from a copy under `/tmp`, without changing the author's files. The saved rerun is byte-for-byte identical to the frozen author diagnostic JSON. The author's numerical tail checks are still floating-point corroboration, even though their large-tail DP now rescales each step and compares log probabilities. A displayed exp(log_probability)=0 is not evidence that the probability is exactly zero.

Actual issues and resolutions:

1. **Reported seed missing term:** bare 8360 did not account for +9K/Q. Resolved in the frozen candidate by retaining it or using the legitimate 8363/2^14 relaxations. No remaining correction required.
2. **Reported earlier diagnostic underflow:** the current diagnostic preserves log probabilities; displayed exponentials may underflow. Resolved as an implementation/evidence-label issue, not a theorem proof and not a mathematical counterexample. No remaining theorem correction required.
3. **New mathematical failures found in this review:** none. The nonselfadjoint norm, complement subspace, support zeros, singleton/beta=1 cases, first-return finiteness and uniqueness, conditional full path law, integer thresholds, bounded transfer, and constant composition all survive the independent audit.

No inaccessible source, denied read/write, missing authorization, or bypass was encountered. No publication, upload, contact or purchase was attempted.

## 8. Binding and verdict

`reviews/IU001_review_bindings_v1.json` records the exact candidate, inspected source, inherited comparison/source, and diagnostic identities. The frozen candidate hash was checked before and after this review; all entries in the author's source manifest matched their actual files.

**Disposition: ACCEPT, with no unresolved mathematical or resource revision requirement, at the exact candidate hash above and within its explicit upper-only finite-model scope.** Later changes or stronger precision-frontier/algorithmic-adaptation claims require their own argument and review.
