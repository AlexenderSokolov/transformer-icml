# TR001 — Full one-block weight-range/grid frontier

2026-11-02. Author candidate v1; fresh independent review pending; NOT root accepted. This standalone synthesis preserves all prior files and imports their accepted proofs within their exact domains.

## 1. Exact family, experiment, and statement

Fix integers K>=3, D>=K³, r>=3, M>=64, a public integer weight envelope κ>=1, and dyadic Q=2^h with integer h>=4. K,D,r are fixed architectural constants, independent of M,β,κ,Q. Observe X_1,...,X_n, n=M+2, from an unknown homogeneous second-order source θ. Its pair kernel P has a hidden stationary probability Π satisfying P²(s,t)>=βΠ(t) for EVERY pair s,t, including unsupported states; 0<=β<=1. In the stationary experiment the initial pair has law Π. In the arbitrary-start experiment its law is arbitrary and unknown. If certificates are nonunique, the experiment includes the choice of certificate. Loss is unconditional expected TV from θ at the actual final pair (X_(n-1),X_n), not an independently sampled query.

The admissible encoder/decoder family is BA001/SH001's exact one-block family, with at most D retained scalar coordinates. Let L_i be the trailing r-symbol window ending at i, i=3,...,n, padded publicly before position 1; shorter windows and functions of those windows are allowed. Let S consist of the first and last min(r,n) observed symbols, with consistent overlap. For every coordinate d and position i, source-independent real tables may depend on L_i, public parameters (including β), and a query q(S) computed only from S. They satisfy actual weights 1<=w_di<=κ and actual values |v_di|<=1. Exactly the following bank is retained:

    B_d = [sum_(i=3)^n w_di(L_i,q(S)) v_di(L_i,q(S))]
                         / [sum_(i=3)^n w_di(L_i,q(S))],
    Z_d = floor(Q B_d)/Q.

The decoder sees only this at-most-D bank, S, public parameters and source-independent randomness, and may return an arbitrary real simplex vector. Arbitrary positional tables, coordinate-dependent weights and query-dependent values are allowed. All M keys enter every ratio with positive weight. No interior exact side field, historical reread, source-dependent table, hard selected-key mask, nonlocal interior feature or recursively global block is allowed. Independent or shared source-independent seeds are allowed, with the bounds holding for every seed. Mathematical zero-padding to D coordinates is only a lower-bound inclusion, not a physical implementation claim. The family permits real weights within the integer envelope; the matching upper uses only {1,κ}.

Let R_stat and R_all be the infimum over admissible encoders and decoders of the worst-case expected loss over the respective source/initialization classes. Define

    β0=max(β,1/M), t=Mβ0, z=κQ, s=M^(-1/2),
    W(z,t)=[1+ln(1+z/t)]/z,
    F=max{s, 1/Q, W(z,t)}.

There are explicit positive constants c=c(D,r), C=C(K), independent of β,M,κ,Q, such that throughout this domain

    c F <= R_stat <= R_all <= risk_all(T_SB001) <= min{1,C F}.  (TR1)

Thus BOTH minimax risks are Θ_(K,D,r)(F), uniformly across ALL permitted joint weight/grid regimes. In particular larger κ cannot remove the 1/Q floor. No unit-risk branch is missing: t>=1,z>=Q>=16 and monotonicity give W<=W(16,1)=(1+ln17)/16<1/4, while s<=1/8 and 1/Q<=1/16.

For constants take c_I from UI001's displayed constructive constants, c_H=1/(8192A0) from SH001 §1, and

    c_S=1/256,
    c=min{c_S/5, c_I/2, c_H/48},
    C_K=48K³(K+1)+10K^5(K+1),
    C=(2^13+2)K^(5/2)+C_K+(2K-1).

These inefficient constants are intentionally retained to expose uniformity. No lower constant depends on κ.

## 2. Imported lower bounds and the statistical floor

UI001, accepted after its independent audit, proves R_stat>=c_I/Q for EVERY finite real κ>=1,Q>=1 and every β in [0,1]. It uses stationary binary IID sources satisfying P²(s,t)=Π(t) on every state; its uniformity in κ is indispensable here. BA001's older κ-dependent IID constant would NOT prove TR1.

SH001 §1 proves, only when β<=1/16 and z<=M/4,

    R_stat >= c_H L,
    L=z^(-1) ln(1+min{z/t,M/z}/8).                          (2.1)

We never extrapolate (2.1) outside this stated domain.

Also R_stat>=c_S s. To see this directly, use IID Bernoulli sources on two symbols with p±=1/2±1/(16sqrt(n)). Define every second-order row, even unsupported rows, to emit the common Bernoulli law. They have the all-state certificate for every β. Grant the full observed history and any independent encoder seed. For δ=1/(16sqrt(n)), the one-observation KL is

    2δ ln[(1+2δ)/(1-2δ)] <= 16δ²,

using ln[(1+x)/(1-x)]<=2x/(1-x) and x=2δ<=1/2. Hence history KL<=1/16, in particular <=1/8, and Pinsker gives history TV<=1/4. Testing these two points gives absolute-estimation Bayes loss at least (2δ)(1-TV)/4>=1/(128sqrt(n)). TV prediction loss dominates the C1 mass error. Because n=M+2<=4M, this is >=s/256. Source-independent randomization cannot improve the testing bound. Granting full history only strengthens the experiment.

These are three uniform minimax lower bounds, potentially with different witnesses. We take their maximum, not their sum or a falsely common witness.

## 3. All-regime lower completion

First, W(z,t) is decreasing in z>0: its derivative numerator is z/(t+z)-1-ln(1+z/t)<0. Also t>=1 and z>=Q.

**A. β>1/16.** The inequality ln(1+u)<=u gives

    W<=1/z+1/t<=1/Q+16/M<=1/Q+2s,

since M>=64. Consequently R_stat>=min{c_I/2,c_S/4}W.

**B. z>M/4.** Independently of β,

    W(z,t)<=W(M/4,1)
       =4[1+ln(1+M/4)]/M <=4(1+sqrt(M))/M <=(9/2)s<5s.

Here ln(1+u)<=2sqrt(u), proved by integrating 1/(1+u)<=1/sqrt(u), was used; and 1/sqrt(M)<=1/8. Thus R_stat>=c_S W/5.

**C. z>M^(3/4).** Again independently of β, sqrt(M)<=z^(2/3), and z>=1 gives

    W/s <=[1+ln(1+z)]/z^(1/3)
         <=1+ln2+3/e<3<5.

Indeed ln(1+z)<=ln2+ln z and max_(z>=1) (ln z)/z^(1/3)=3/e. Thus R_stat>=c_S W/5. Cases B and C may overlap, harmlessly.

**D. The remaining case:** β<=1/16 and z<=min{M/4,M^(3/4)}. Put x=z/t and y=M/z. Then x<=z<=y³ and y>=4. If x<=y, concavity of log gives ln(1+x)<=8ln(1+x/8). If x>y, the inequality 1+y³<=(1+y)³ gives

    ln(1+x)<=3ln(1+y)<=24ln(1+y/8).

Thus in both cases

    ln(1+x)<=24ln(1+min{x,y}/8),
    W<=1/z+24L<=1/Q+24L.

Using UI001 and SH001, R_stat>=min{c_I/2,c_H/48}W. Combining all cases with the separate s and 1/Q floors proves R_stat>=cF for the displayed c. This is an exhaustive finite-domain argument; no asymptotic or large-M exception is omitted.

## 4. Matching unchanged paid upper and initialization comparison

SB001 v2 §7, using AU001's stationary occupation and exact complete-suffix mixture lemmas, proves for its SAME paid program and every public integer κ>=1, dyadic Q>=16,

    risk_all(T)<=min{1,2^13 Hstat+Ψ(K^5/(M+1))
                         +C_K W(κQ,t)+(2K-1)/Q}.           (4.1)

Here Ψ(u)=u(1+ln(1/u)) for 0<u<1, Ψ(0)=0, Ψ(u)=1 for u>=1; Hstat is the inherited original R011 scale, with Hstat<=K^(5/2)/sqrt(M+1), and Ψ(u)<=2sqrt(u). Therefore (4.1)<=min{1,CF}.

For clarity the program's terminal encoder uses paid local pair/triple features (r=3), the complete K³-coordinate one-hot triple value bank, and weight κ on keys whose preceding pair matches the terminal pair, weight 1 otherwise. All M keys remain present. The decoder selects the K entries of the terminal-pair block ONLY AFTER quantization, normalizes their sum if positive, and otherwise uses the uniform fallback; then it performs ordered Q-simplex output rounding. Neither exact denominators nor counts cross the cut. SB001 §3 explicitly covers J=0 and positive J whose entire selected block floors to zero. This is within the present family because D>=K³ and r>=3, and the terminal query comes from S. Paid local-copy heads are not additional global summary blocks.

The algorithm uses neither β nor Π at runtime at supplied budgets. AU001's residual mixture is an analysis of the law of a whole suffix; it is not an observable regeneration event or an extra side port. Stationary sources form a subset of arbitrary-start sources for each fixed encoder/decoder; taking infima gives R_stat<=R_all. The explicit admissible program gives R_all<=risk_all(T), completing TR1.

All SB001 §6 costs remain unchanged: with n_prog=M+3, ell=ceil(log2(n_prog+K+2)), k=bitlength(κ), b=64(h+ell+k+1), it pays exact full-width arithmetic, two local singleton-copy heads, complete dense K³ bank, all-token storage/work, masks, controller/addresses, cache, offline generation, explicit copies and clears. Its T0=O(n_prog²K^6b²), S=O(n_prog²+n_prog K³b+K^6b+b²) feed its separately paid addressed-sequential or PURE alternatives. This theorem does not reduce full word b, total storage, forward/offline work, or compiled depth to the grid h or to lnκ.

## 5. Exact statistical-order joint condition

Write a=sqrt(M), u=a/t=1/(sqrt(M)β0), f=1+ln(1+u), and

    Z_star=a f
      =sqrt(M)[1+ln(1+1/(sqrt(M)max(β,1/M)))].             (5.1)

This is numerically the ORIGINAL Q_star from FR001/PF001. It is now a PRODUCT threshold, NOT the grid threshold by itself:

    Q ≳ sqrt(M) AND κQ ≳ Z_star.                          (TR2)

The two conditions are simultaneous, and their meaning in target multipliers is as follows.

**Necessity for every target C0>0.** If an admissible procedure guarantees risk<=C0/a, even only on stationary sources, put B=max{1,C0/c}. TR1 implies Q>=a/B and W(z,t)<=B/a. With v=z/a, this last inequality is

    [1+ln(1+vu)]/v<=B.

If v>=1, its numerator is at least f, so v>=f/B>=f/B². If 0<v<1, concavity yields 1+ln(1+vu)>=v[1+ln(1+u)]=vf, so f<=B; the numerator is also >=1, so v>=1/B>=f/B². Therefore in EVERY case

    Q>=a/B,  κQ>=Z_star/B².                              (5.2)

This implication is meaningful without asserting that any arbitrarily small target C0 is achievable. It applies to infimum minimax risks too because the uniform lower persists under infima.

**Sufficiency for an explicit fixed multiplier.** If Q>=a and κQ>=Z_star, monotonicity of W and 1+fu<=f(1+u) give

    W(z,t)<=W(af,t)<=[f+ln f]/(af)<=2/a.

Thus risk_all(T)<=2C/a (and <=1). More generally, for ANY fixed positive A,B0, if Q>=Aa and κQ>=B0 Z_star, then

    risk_all(T)<= C max{1, A^(-1), 2 max{1,B0^(-1)}}/a.    (5.3)

For B0<1 use monotonicity of the numerator to get W(B0 Z_star,t)<=W(Z_star,t)/B0; for B0>=1 use decreasing W. This proves the usual order-equivalence of the joint conditions with constants independent of M,β.

There are always legal budgets: choose Q=2^max{4,ceil(log2 a)}, then a<=Q<=2a for M>=64, and κ=max{1,ceil(Z_star/Q)}. These satisfy the sufficient conditions, with κ<=1+Z_star/Q. Alternatively κ=1 and dyadic Q>=Z_star recover the larger original-interface-style grid schedule; many other allocations work. Budget selection using β is public promise-based selection, not learning β from data or a free transcendental runtime primitive. SB001's β-blind bitlength κ schedule remains available. This is not a theorem about fixed total precision or a universal optimum across multiple global blocks.

## 6. Provenance, diagnostics and limitations

Direct bindings are in TR001_source_bindings_v1.json: UI001 proof/acceptance/review (uniform grid floor); SH001 proof/acceptance (rescaled log floor with its finite cutoffs); BA001 exact family; SB001 v2 proof/acceptance (unchanged paid all-β upper and ledger); AU001 proof/acceptance (suffix-mixture justification); FR001 proof/acceptance (original threshold definition). Each binding records SHA-256 of the bytes read. The stale author-review headings inside accepted dependency manuscripts do not override their separate root acceptance receipts.

The new ingredients here are the all-regime elementary completion and the full joint-budget formulation, not a new upper program. Finite diagnostics test scalar inequalities, branch boundaries, dyadic/integer allocation and threshold implications; they do not prove a universal theorem. Independent LLM review and root acceptance are separate and do not constitute formal verification or external peer review. No external novelty claim, original-network execution, training attainability, sharp joint-K/D/r order, K=2 logarithmic lower, or deep/growing-global-feature lower is asserted. The exact model exclusions are substantive.
