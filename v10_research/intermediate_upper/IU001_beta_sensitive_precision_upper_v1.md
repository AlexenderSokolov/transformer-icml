# IU001 — A beta-sensitive logarithmic precision surcharge for the unchanged NB002 predictor

2026-11-02. **New author candidate; independent review required.** The root supplied the candidate occupancy route. This author checked and completed its return-time, nonreversible operator, terminal-conditioning, and integer-threshold arguments. One genuine seed bookkeeping error is recorded: the proposed coefficient 8360 did not include the inherited `+9K/Q`. The explicit theorem retains that term; a relaxed 8363 coefficient or the simpler `2^14` form absorbs it. No accepted source is modified, and no external novelty claim is made.

## 0. Result first and exact scope

Let K>=2, M>=1 and h>=4 be integers, Q=2^h, and B_(K,M,h) be **exactly the accepted NB002 finite predictor** used in SM001: the same finite six-head frequency prefix, complete statistical master cut and exact side inputs, positive approximate count weights, ordered Q-grid normalizations, conservative integer guard, and output mux. There is no changed encoder, suffix, port, randomization, or runtime beta input.

Put

    E=76KM/Q,
    epsilon_beta(M)=1                         if floor(M/4)=0,
                    (1-beta)^floor(M/4)       otherwise.

Thus epsilon_1(M) is zero for M>=4 and one for M<4; no value of 0^0 is used. For every 0<beta<=1, uniformly over the full all-state D2(beta) source class with arbitrary initial pair law, the actual-terminal expected-TV risk obeys

    risk(B;beta)
      <= min(1, 2^16 L
                 +(K^3/Q)[8360+456 ln(1+(480/76)Q/(beta K M))]
                 +9K/Q+4 epsilon_beta(M)).                    (IU1)

Here L is exactly the accepted R011 scale, defined in Section 1. Since K>=2, replacing `8360` by `8363` and deleting the separate `9K/Q` weakens (IU1) validly. A simpler consequence is

    risk(B;beta)
      <= min(1, 2^16 L
                 +2^14 (K^3/Q)[1+ln(1+Q/(beta K M))]
                 +4 epsilon_beta(M)).                         (IU2)

The new logarithm depends on **beta E**, not merely log Q. The unchanged all-beta bound remains separately available, including beta=0:

    risk(B;beta)<=min(1,2^16 L+7 Psi(76K^5/Q)+9K/Q),             (IU3)

where Psi(x)=x(1+ln(1/x)) for 0<x<1, Psi(0)=0 and Psi(x)=1 for x>=1. One may take the minimum of these valid bounds. The accepted SM001 reciprocal bound can also be retained where numerically better; none is silently replaced.

An explicit upper-only consequence is: **for fixed K and every c>0**, the same public SM001 schedule Q=Theta_K(sqrt(M+1)) has risk O_(K,c)(L), uniformly over all M and beta satisfying

    beta sqrt(M+1)>=c.                                        (IU4)

This includes vanishing beta. It is not a matched intermediate-beta phase diagram, a lower bound, or global beta-adaptive budget selection. The predictor family is beta-blind at fixed public h. Choosing h using a class promise is a separate configuration decision and must not be called unqualified unknown-beta budget adaptation.

## 1. Inherited source experiment and pre-integration reduction

For alphabet {0,...,K-1}, a homogeneous second-order source has pair kernel

    P((a,b),(b,c))=theta_ab(c).

There exists a stationary probability pi on the K^2 pair states with

    pi P=pi,  P^2(s,t)>=beta pi(t) for every pair s,t,

including starting states outside supp(pi). The initial pair law mu is arbitrary. Observe X_1,...,X_(M+2), let Y_j=(X_(j+1),X_(j+2)) for 0<=j<=M, and query the true law theta_(Y_M). The original complete-history prior-visit count is

    J=sum_(j=0)^(M-1) 1{Y_j=Y_M}.

Set n=M+1, delta=1-beta and

    i=min(1,sqrt(K/n)), a=min(1,sqrt(K^3/n)),
    g=min(1,sqrt(K^5/n)), hstar=min(1,sqrt(K^4/n)),
    F=max(i,min(delta,a)), D=delta^n g,
    T=delta^(M/2) hstar, L=max(F,D,T).

Both exponents in D,T are positive. R011 gives L>=i>=1/sqrt(n) and its full-history minimax risk R>=2^-17 L.

Write

    v=min(1,E/(J+K)), Cbad={J+K<4E}, E=76KM/Q.

Accepted NB002 Sections 3–6, explicitly assembled before integration in accepted SM001 Section 2, give

    risk(B;beta)
      <=min(1,2^16 L+3 E_mu[v]+P_mu(Cbad)+9K/Q).                (1.1)

This is an inherited **pre-integration** reduction, not an inversion of NB002's final Psi bound. Outside the near-IID branch it uses actual count-radius certificates for E(e+2rho); in the near-IID branch it uses monotone rejection, the pooled estimate and the actual CT/active-GT tails. The false unconditional NEXT statement is not used. The finite exceptional cases are covered by the loss cap because 2^16 L>=1 there.

Only the integration of v and Cbad is changed below. All burns, stationary comparators, reverse paths, spectral tilts and return times are analysis objects, never extra predictor inputs or computations.

## 2. Reverse paths and a self-contained conditional return bound

We first work with any finite stationary Markov chain P satisfying the same two-step minorization, without requiring the pair structure. Let S=supp(pi), d=|S|. Stationarity and nonnegativity imply P(s,t)=0 whenever s in S and t outside S; S is closed. On S the reversed kernel

    P*(s,t)=pi(t)P(t,s)/pi(s)

is stochastic and has stationary law pi. Telescoping the stationary path probabilities proves that, conditional on the actual endpoint Y_M=s, the reversed states Z_j=Y_(M-j), 0<=j<=M, form a P* chain started at s. Moreover

    (P*)^2(s,t)=pi(t)P^2(t,s)/pi(s)>=beta pi(t).                 (2.1)

Every division is on positive stationary support. No reverse kernel outside S is needed, and no IID claim about observed row successors or the terminal query is made.

### Lemma 2.1: return expectations and integer tails

For the P* chain started at s in S, put p=pi(s)>0 and let tau_k be its kth positive return time to s. Then

    E_s tau_k=k/p,
    P_s(J_M<k)=P_s(tau_k>M)<=k/(M p),                         (2.2)

for every integer k>=1, where J_M=sum_(j=1)^M 1{Z_j=s}.

**Proof, including Kac rather than invoking it.** The two-step skeleton has conditional chance at least beta p to hit s at each next skeleton step. Iterating the conditional failure bound shows that its first hit is dominated by a geometric variable of parameter beta p. Consequently the first positive return tau_1 of the full chain has E_s tau_1<=2/(beta p)<infinity.

Define the finite nonnegative row vector

    u(t)=E_s sum_(j=0)^(tau_1-1) 1{Z_j=t}.

By Tonelli and the one-step Markov property (the event j<tau_1 is measurable before step j+1),

    (u P*)(t)=E_s sum_(j=0)^(tau_1-1) 1{Z_(j+1)=t}=u(t).

The last equality holds because the initial and final states of this stopped path are both s. Also u(s)=1 and sum_t u(t)=E_s tau_1. The normalized vector u/E_s tau_1 is therefore stationary.

To verify uniqueness on S directly, for beta<1 write (P*)^2=beta Pi+(1-beta)R, with Pi the constant-row pi kernel and R stochastic and pi-invariant. Two-step iteration contracts TV to pi by at most (1-beta)^r. Hence any stationary probability on S equals pi. At beta=1 the two-step kernel equals Pi, so uniqueness is immediate. Thus u/E_s tau_1=pi, and u(s)=1 gives E_s tau_1=1/p.

The discrete strong Markov property at each finite tau_j follows by summing the ordinary Markov property over its possible integer values. The subsequent return increments have the same expectation 1/p, so E_s tau_k=k/p. The event equality in (2.2) follows from counting positive returns through time M; Markov's inequality proves its bound. This is a return-time calculation, not a conditional IID calculation. ∎

## 3. A stationary lower-tail certificate without an imported concentration theorem

The needed exponential estimate is proved by a finite-dimensional operator calculation, including for nonreversible chains.

### Lemma 3.1: stationary skeleton count

Let H be a finite Markov kernel with invariant pi and H>=beta Pi, 0<beta<=1. Fix a state s of mass p=pi(s), and let W_0,...,W_(m-1) be m>=1 stationary H samples. For N_s=sum_(j=0)^(m-1)1{W_j=s},

    P_pi(N_s<m p/2)<=2 exp(-beta m p/24).                      (3.1)

If p=0 the left side is zero. The p=1 case is deterministic and also satisfies the claim.

**Proof.** On L2(pi), a pi-invariant Markov operator R is a contraction: Jensen gives |Rf|^2<=R(|f|^2), and integration against pi proves ||Rf||_2<=||f||_2. It preserves both constants and centered functions.

For beta<1 set R=(H-beta Pi)/(1-beta). Then R is stochastic and pi-invariant. Decomposing f and g into mean and centered parts gives

    |<f,Hg>|<=|pi(f) pi(g)|+(1-beta)||f-pi(f)||_2||g-pi(g)||_2.

Applying Cauchy to these two nonnegative components shows that the right side is at most

    sqrt(<f,H0 f><g,H0 g>),  H0=(1-beta)I+beta Pi.              (3.2)

The same inequality holds directly for beta=1, when H=Pi. Thus it does not require dividing by 1-beta at that endpoint.

Let lambda=beta/8 and D be multiplication by exp(-lambda 1_s/2). Applying (3.2) to Df,Dg yields

    ||D H D||_(2->2)<=||D H0 D||_(2->2).                       (3.3)

This is a singular-operator-norm bound, not an assumption that H is self-adjoint. H0 is self-adjoint positive, so D H0 D is self-adjoint positive.

Put a_lambda=1-exp(-lambda). For 0<p<1, on the orthonormal span of the normalized indicator of s and the normalized indicator of its complement, the matrix of I-D H0 D is

    [ beta(1-p)+a_lambda(1-beta+beta p),
      -sqrt(1-a_lambda) beta sqrt(p(1-p));
      -sqrt(1-a_lambda) beta sqrt(p(1-p)), beta p ].

Its determinant is exactly a_lambda beta p and its trace is

    beta+a_lambda(1-beta+beta p)<=beta+a_lambda.

It is positive definite. Its smaller eigenvalue is the determinant divided by the larger eigenvalue, and hence is at least a_lambda beta p/(beta+a_lambda). On the remaining subspace (functions zero at s and centered on the complement) the eigenvalue of I-D H0 D is beta, no smaller than this bound. For p=1 the sole eigenvalue is a_lambda, also no smaller. The p=0 case has already been removed.

Since 0<lambda<=1/8,

    15lambda/16<=lambda-lambda^2/2<=a_lambda<=lambda=beta/8.

Consequently

    a_lambda beta p/(beta+a_lambda)>=(5/6)lambda p,
    ||D H D||<=1-(5/6)lambda p<=exp(-(5/6)lambda p).            (3.4)

The stationary moment generating function has the exact operator representation

    E_pi exp(-lambda N_s)
      =<D1,(D H D)^(m-1)D1>
      <=||D1||_2^2 ||D H D||^(m-1)
      <=exp(-(5/6)lambda p(m-1)).                             (3.5)

This covers m=1, when the operator power is the identity. Markov's inequality applied to exp(-lambda N_s) gives

    P_pi(N_s<m p/2)
      <=exp(lambda m p/2-(5/6)lambda p(m-1))
      <=exp(5beta p/48) exp(-beta m p/24)
      <=2 exp(-beta m p/24).

Here exp(5/48)<2, and p<=1. This proves (3.1). ∎

### Lemma 3.2: conditional terminal count

For the reversed chain started at its query s in S, every M>=1 satisfies

    P_s(J_M<M pi(s)/16)<=5 exp(-beta M pi(s)/96).               (3.6)

**Proof.** Set b=floor(M/2), L_suf=M-b=ceil(M/2), r=floor(b/2)=floor(M/4). The law of Z_b differs in TV from pi by at most epsilon_beta(M), by two-step contraction. Applying the same path-extension kernel bounds TV of the **whole** suffix Z_b,...,Z_M by the same quantity.

Within this suffix choose times b+1,b+3,... up to M, giving m=ceil(L_suf/2)>=M/4 samples of H=(P*)^2. All are positive times and counted in J_M, including when b=0 or M=1. Under the stationary suffix comparator those samples are a stationary H chain. Since M pi(s)/16<=m pi(s)/2, Lemma 3.1 and bounded event transfer yield

    P_s(J_M<M pi(s)/16)
      <=2 exp(-beta m pi(s)/24)+epsilon_beta(M).

The first term is at most 2 exp(-beta M pi(s)/96). For all beta including beta=1, the explicit zero-exponent convention gives

    epsilon_beta(M)<=exp(-beta floor(M/4))
                    <=exp(beta) exp(-beta M/4)
                    <=3 exp(-beta M pi(s)/96).

The last comparison uses exp(beta)<=e<3 and pi(s)<=1. Thus (3.6) holds for all small horizons and both parities without an unmentioned burn-length condition. ∎

## 4. Clipped reciprocal integration: beta times the perturbation scale

### Lemma 4.1: stationary terminal-count functional

For any integer smoothing parameter kappa>=1 and real A>0, the stationary path of length M>=1 obeys

    E_pi min(1,A/(J_M+kappa))
       <=min(1,(dA/M)[17+ln(1+480/(beta A))]).                 (4.1)

Here J_M is the actual-terminal prior-visit count, not a count against an independent query.

**Proof.** Condition on the terminal state s in S, and write p=pi(s), mu_s=M p and a0=A/mu_s. If a0>=1/16, the unit cap is at most 16a0, hence at most the claimed conditional right side.

Otherwise 16a0<1. Layer cake and the trivial bound by one give a contribution at most 16a0 on 0<t<=16a0. For t>16a0,

    {min(1,A/(J_M+kappa))>t}={J_M<A/t-kappa}.

If the right threshold is nonpositive the event is empty. Otherwise let k=ceil(A/t-kappa)>=1. Because J_M is integer, the event is exactly {J_M<k}. The smoothing condition kappa>=1 ensures

    k<=A/t-kappa+1<=A/t<mu_s/16.

Thus both (2.2) and (3.6) apply, giving

    P_s(v>t)<=min(a0/t,q_s), q_s=5exp(-beta mu_s/96).

Define F(x)=x for 0<=x<=1 and F(x)=1+ln x for x>=1. Direct integration at t=a0/q_s gives

    integral_0^1 min(a0/t,q_s) dt=a0 F(q_s/a0)
                                      <=a0[1+ln_+(q_s/a0)].

Since x exp(-x)<=1 for x>=0,

    q_s/a0=5mu_s exp(-beta mu_s/96)/A<=480/(beta A).

It follows that

    E_s v<=a0[17+ln(1+480/(beta A))].                         (4.2)

There is no independence assumption between the count, query, or numerical perturbation. Multiplying (4.2) by pi(s), summing over S, and applying the separate unit cap proves (4.1). The factor pi(s) cancels against a0=A/(M pi(s)) only after conditioning and proving the statewise inequalities. ∎

The relevant scale in (4.1) is beta A. In the implementation A=E=76KM/Q, so the logarithm becomes ln(1+(480/76)Q/(beta K M)). Replacing this by a generic log Q earlier in the proof would lose the useful intermediate-beta information.

## 5. Arbitrary forward initialization and the bad event

Return to the actual forward source, with arbitrary initial law mu on all pair states. Set b=floor(M/2), L_suf=ceil(M/2), and

    J_suf=sum_(j=b)^(M-1)1{Y_j=Y_M}.

Pathwise J>=J_suf. All-state forward minorization bounds TV(mu P^b,pi) by epsilon_beta(M), also for off-support starts. The same path-extension kernel compares the **complete** suffix laws, including their terminal query, by that TV bound. The clipped reciprocal is bounded by one, so it must be transferred before any clip is discarded. Lemma 4.1 then gives, for every A>0 and integer kappa>=1,

    E_mu min(1,A/(J+kappa))
      <=(dA/L_suf)[17+ln(1+480/(beta A))]+epsilon_beta(M)
      <=(2dA/M)[17+ln(1+480/(beta A))]+epsilon_beta(M).          (5.1)

For the bad event, transfer its bounded indicator separately. Under a stationary suffix, condition on terminal state s. If 4A<=kappa the event J_suf+kappa<4A is empty. Otherwise its exact integer threshold k=ceil(4A-kappa) satisfies 1<=k<=4A. Lemma 2.1, now at horizon L_suf, gives

    P_pi(J_suf+kappa<4A)<=sum_s pi(s)4A/(L_suf pi(s))
                       =4dA/L_suf<=8dA/M.

Therefore

    P_mu(J+kappa<4A)<=8dA/M+epsilon_beta(M).                   (5.2)

No logarithm is needed in (5.2). The strict threshold, noninteger A, and kappa>=1 are handled explicitly. There is one TV charge for each bounded functional, not a TV error multiplied by A/kappa or any unbounded reciprocal.

Combining (5.1)–(5.2),

    3 E_mu min(1,A/(J+kappa))+P_mu(J+kappa<4A)
       <=(dA/M)[110+6ln(1+480/(beta A))]
          +4epsilon_beta(M).                                  (5.3)

For the pair experiment take kappa=K, A=E=76KM/Q and d<=K^2. Substituting (5.3) into (1.1) gives exactly (IU1), including the inherited `+9K/Q`.

For (IU2), let x=Q/(beta K M). Since 480/76=120/19>1 and ln(120/19)<2,

    ln(1+(120/19)x)<=2+ln(1+x),
    8360+9/K^2<=8363,
    8363+912+456ln(1+x)<=2^14[1+ln(1+x)].

This proves the stated compact bound. No constant depends secretly on the unknown source or stationary masses.

## 6. A vanishing-beta half-log sufficiency corollary

Use precisely the public SM001 integer schedule

    u=ceil(log2(M+1)), vK=ceil(log2 K),
    h_strong=20+3vK+ceil(u/2), Q=2^h_strong.                    (6.1)

It satisfies

    2^20 K^3 sqrt(n)<=Q<=2^24 K^3 sqrt(n), n=M+1.              (6.2)

These bounds follow from dyadic ceiling factors; no real-log or square-root oracle is added to the actual integer configuration computation.

Fix K and c>0, and assume only beta sqrt(n)>=c. Since n/M<=2,

    Q/(beta K M)<=2^25 K^2/c.                                (6.3)

Also, uniformly including the beta=1 and M<4 conventions,

    epsilon_beta(M)<=exp(beta) exp(-beta M/4)
                    <=e exp(-c sqrt(n)/8)
                    <=8/(c sqrt(n)),                         (6.4)

where M>=n/2 and the last inequality follows from the maximum of x exp(-cx/8). Applying (IU2), (6.2)–(6.4), and 1/sqrt(n)<=L yields

    risk(B;beta)
      <=min(1,[2^16+32/c
                 +2^-6(1+ln(1+2^25 K^2/c))]L).               (6.5)

This proves (IU4). Its constant is uniform along every vanishing-beta sequence with beta sqrt(M+1) bounded below by the same c, but it depends on K,c. The full-history minimax lower R>=2^-17 L makes this constant-order minimax sufficiency on that promised class.

When Q is of order sqrt(M) at fixed K, the new logarithm has order `1+ln(1+1/(beta sqrt(M)))`; this describes the new **upper surcharge**, not a necessary precision frontier. When beta sqrt(M) is small, the burn term and the independent all-beta Psi bound must still be kept. No matched intermediate lower is established here, and no beta-dependent precision planning is advertised as global unknown-beta budget adaptation.

## 7. Same finite implementation and complete resource scope

No new arithmetic operation appears in B. Its exact finite definition, h>=4 legality, full product/guard widths, canonical grid totality, master-cut lifetime and absence of reread ports are inherited unchanged from accepted NB002 and its review. Let

    ell=ceil(log2(M+K+4)), p_word=4h+4ell+64,
    N=M+2, n_tok=M+3.

All the following NB002 charges remain; they are not replaced by the size of a reciprocal-count proof:

| Coordinate | Unchanged upper bound / property |
|---|---|
| Hybrid neural depth / width | O(K p_word^2) / O(K p_word) |
| Heads total / max per layer; max QK dimension; score cap | 6 / 4; 2K; 2 |
| Complete online arithmetic words, products and guards | <=128 p_word bits |
| Dense coefficient slots / bits, including zeros and biases | O(K^3 p_word^4) / O(K^3 p_word^5) |
| Active records / explicit holds | O(K p_word^2+K^2) / O(K^2 p_word^3) |
| Addressed sparse program, coefficients and holds | O(K^2 p_word^4) bits |
| Masks / positions | O(n_tok^2+n_tok log(n_tok+1)) bits |
| Observed one-hot input | O(NK) bits; acquisition/conversion separately charged |
| Rolling scalar-neural work excluding stored data | O(n_tok K p_word^2) bits |
| Uncached attention bitwork | O(n_tok^2(K+p_word)p_word^2) |
| Equally cached attention bitwork | O(n_tok^2 K p_word^2), plus actual cache creation/storage/selection |
| Dense all-token pointwise and QKV bitwork | O(n_tok K^3 p_word^6) |
| Rational logs: work / scratch | O(p_word^3 log^2(p_word+1)) / O(p_word log(p_word+1)) |
| Five full-score cache creation / evaluator code | O(p_word^3) plus logs / O(p_word^4) bits |

Offline generation still pays public configuration, layouts, masks, positions, constants, every gate/term/hold, addressing, sorting and actual selected-format writes. With R_rec actual records, conservative generation/sorting bitwork is O(R_rec p_word^2) and scratch O(R_rec p_word); dense files additionally pay their actual coefficient-bit writes, including zeros.

Peak is the maximum of **simultaneous phase sums** of program, parameters, input, metadata/masks, historical/QKV arrays, residual/master/weight/normalized/output banks, controller/address words and scratch. A safe dense forward sum is

    O(K^3 p_word^5+n_tok^2+n_tok log(n_tok+1)+NK+n_tok K p_word^2),

replacing only the stored-program term by O(K^2 p_word^4) in sparse format. Offline scratch coexists with retained generated data. Rolling work is not total peak, packed-bit storage and scalar-neural bit-channels remain distinct conventions, and all-token work is charged despite one requested output.

The separate PURE expansion still has depth O(T_bit+p_word), width O(S_bit+p_word), sparse gates/holds O((T_bit+p_word)(S_bit+p_word)), dense coefficient bits O(p_word(T_bit+p_word)(S_bit+p_word)^2), and generic dense bitwork O(p_word^2(T_bit+p_word)(S_bit+p_word)^2), with **all** online control/movement/copies/clears/attention included in T_bit and all simultaneously live data in S_bit. It is not assigned hybrid resources.

Reducing master/output h does not erase ell or total word p_word. This is not an emitted implementation measurement, training theorem, time/space advantage over paid direct counting, hardware fault theorem, or architecture-universal precision statement.

## 8. Genuine correction, hazards, and status

1. **Seed bookkeeping correction:** 76 times 110 is 8360, but (1.1) still contains +9K/Q. The seed's bare 8360 compact bound does not follow from those constants. (IU1) retains it; 8363 or the stated 2^14 bound absorbs it. No accepted theorem is implicated.
2. **Nonreversibility:** H is never made self-adjoint. The proof bounds its tilted singular operator norm by that of a positive self-adjoint comparison through the two-component Cauchy inequality (3.2).
3. **Kac and uniqueness:** finiteness is proved from two-step minorization, the stopped occupation vector is shown invariant, and uniqueness is proved by contraction. No unverified recurrence theorem is imported.
4. **Terminal dependence:** time reversal is conditional on the actual terminal state only under stationarity; the whole suffix law is transferred before applying the stationary argument. No original row-sample IID assertion is made.
5. **Integer thresholds and smoothing:** ceil(A/t-kappa)<=A/t uses kappa>=1. Real A and strict inequalities are handled exactly. This proof does not claim the same formula for smoothing below one.
6. **Endpoint cases:** positive support, singleton support, beta=1, m=1, M<4, both parities and off-support initial states are treated. Beta=0 uses (IU3), not a division by beta.
7. **Upper versus lower:** accepted SM002 supplies an independently witnessed 1/Q complete-master lower, not an intermediate logarithmic matching theorem. Its fixed-positive-beta synthesis does not settle vanishing-beta precision. Any combined intermediate phase needs a separate lower/upper audit.
8. **Evidence identity:** the attached finite diagnostics corroborate individual calculations and cases; they are not universal proofs, independent peer review, external novelty certification or emitted-neural-artifact validation. This author candidate requires independent review before acceptance.
