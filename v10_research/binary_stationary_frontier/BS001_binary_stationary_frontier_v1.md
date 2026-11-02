# BS001 — Exact stationary binary one-block two-resource frontier

2026-11-02. Author candidate v1; fresh independent review pending; NOT root accepted. This standalone synthesis preserves all prior files and imports their accepted proofs within their exact domains.

## 1. Exact family, experiment, and statement

Fix K=2 and integers D>=8, r>=3, M>=64, a public integer weight envelope κ>=1, and dyadic Q=2^h with integer h>=4. K,D,r are fixed architectural constants, independent of M,β,κ,Q. Observe X_1,...,X_n, n=M+2, from an unknown homogeneous second-order source θ. Its pair kernel P has a hidden stationary probability Π satisfying P²(s,t)>=βΠ(t) for EVERY pair s,t, including unsupported states; 0<=β<=1. In the stationary experiment the initial pair has law Π. No arbitrary-start theorem is asserted here. If certificates are nonunique, the experiment includes the choice of certificate. Loss is unconditional expected TV from θ at the actual final pair (X_(n-1),X_n), not an independently sampled query.

The admissible encoder/decoder family is BA001/SH001's exact one-block family, with at most D retained scalar coordinates. Let L_i be the trailing r-symbol window ending at i, i=3,...,n, padded publicly before position 1; shorter windows and functions of those windows are allowed. Let S consist of the first and last min(r,n) observed symbols, with consistent overlap. For every coordinate d and position i, source-independent real tables may depend on L_i, public parameters (including β), and a query q(S) computed only from S. They satisfy actual weights 1<=w_di<=κ and actual values |v_di|<=1. Exactly the following bank is retained:

    B_d = [sum_(i=3)^n w_di(L_i,q(S)) v_di(L_i,q(S))]
                         / [sum_(i=3)^n w_di(L_i,q(S))],
    Z_d = floor(Q B_d)/Q.

The decoder sees only this at-most-D bank, S, public parameters and source-independent randomness, and may return an arbitrary real simplex vector. Arbitrary positional tables, coordinate-dependent weights and query-dependent values are allowed. All M keys enter every ratio with positive weight. No interior exact side field, historical reread, source-dependent table, hard selected-key mask, nonlocal interior feature or recursively global block is allowed. Independent or shared source-independent seeds are allowed, with the bounds holding for every seed. Mathematical zero-padding to D coordinates is only a lower-bound inclusion, not a physical implementation claim. The family permits real weights within the integer envelope; the matching upper uses only {1,κ}.

Let R_stat be the infimum over admissible encoders and decoders of the worst-case expected loss over this stationary source class. Define

    e0=max(sqrt(β),1/M), t=M e0, z=κQ, s=M^(-1/2),
    W(z,t)=[1+ln(1+z/t)]/z,
    F=max{s, 1/Q, W(z,t)}.

There are explicit positive constants c=c(D,r), C absolute, independent of β,M,κ,Q, such that throughout this domain

    c F <= R_stat <= risk_stat(T_SB001) <= min{1,C F}.       (BS1)

Thus the stationary minimax risk is Θ_(D,r)(F), uniformly across ALL permitted joint weight/grid regimes. In particular larger κ cannot remove the 1/Q floor. No unit-risk branch is missing: t>=1,z>=Q>=16 and monotonicity give W<=W(16,1)=(1+ln17)/16<1/4, while s<=1/8 and 1/Q<=1/16.

All constants are explicit. UI001's constant c_I is given by

    H_I=3^(2r), F_I=D H_I, q=4^(-r), L_I=r F_I+2r,
    J_I=(2r L_I+1)/q, V_I=4r² J_I/q,
    C_I=ceil(max{1,400 F_I(2r-1)/q²,3200 F_I V_I}),
    P_I=128 sqrt(L_I(C_I+1)), R_I=(2+48r)9^D,
    c_I=min{1/(128sqrt(C_I+3)),1/(32 R_I P_I)}.

BI001's constant c_B is

    H_B=2^(2r), T_B=34r sqrt(64 D H_B),
    N_B=ceil(2T_B+4)+1, A_B=H_B(2+68r)N_B^D,
    c_B=1/(524288 A_B).

Take c_S=1/256 and

    c=min{c_S/5,c_I/2,c_B/48},
    C=2^17+3+544=131619.

These deliberately inefficient constants are independent of β,M,κ,Q. In particular the lower constant does not deteriorate with weight range.

## 2. Imported lower bounds and the statistical floor

UI001, accepted after its independent audit, proves R_stat>=c_I/Q for EVERY finite real κ>=1,Q>=1 and every β in [0,1]. It uses stationary binary IID sources satisfying P²(s,t)=Π(t) on every state; its uniformity in κ is indispensable here. BA001's older κ-dependent IID constant would NOT prove BS1.

BI001 v2 proves, only when β<=1/256 and z<=M/4,

    R_stat >= c_B L,
    L=z^(-1) ln(1+min{z/t,M/z}/8).                          (2.1)

We never extrapolate (2.1) outside this stated domain.

Also R_stat>=c_S s. To see this directly, use IID Bernoulli sources on two symbols with p±=1/2±1/(16sqrt(n)). Define every second-order row, even unsupported rows, to emit the common Bernoulli law. They have the all-state certificate for every β. Grant the full observed history and any independent encoder seed. For δ=1/(16sqrt(n)), the one-observation KL is

    2δ ln[(1+2δ)/(1-2δ)] <= 16δ²,

using ln[(1+x)/(1-x)]<=2x/(1-x) and x=2δ<=1/2. Hence history KL<=1/16, in particular <=1/8, and Pinsker gives history TV<=1/4. Testing these two points gives absolute-estimation Bayes loss at least (2δ)(1-TV)/4>=1/(128sqrt(n)). TV prediction loss dominates the C1 mass error. Because n=M+2<=4M, this is >=s/256. Source-independent randomization cannot improve the testing bound. Granting full history only strengthens the experiment.

These are three uniform minimax lower bounds, potentially with different witnesses. We take their maximum, not their sum or a falsely common witness.

## 3. All-regime lower completion

First, W(z,t) is decreasing in z>0: its derivative numerator is z/(t+z)-1-ln(1+z/t)<0. Also t>=1 and z>=Q.

**A. β>1/256.** Then e0>1/16. The inequality ln(1+u)<=u gives

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

**D. The remaining case:** β<=1/256 and z<=min{M/4,M^(3/4)}. Put x=z/t and y=M/z. Then x<=z<=y³ and y>=4. If x<=y, concavity of log gives ln(1+x)<=8ln(1+x/8). If x>y, the inequality 1+y³<=(1+y)³ gives

    ln(1+x)<=3ln(1+y)<=24ln(1+y/8).

Thus in both cases

    ln(1+x)<=24ln(1+min{x,y}/8),
    W<=1/z+24L<=1/Q+24L.

Using UI001 and BI001, R_stat>=min{c_I/2,c_B/48}W. Combining all cases with the separate s and 1/Q floors proves R_stat>=cF for the displayed c. This is an exhaustive finite-domain argument; no asymptotic or large-M exception is omitted.

## 4. Matching stationary upper and unchanged full implementation costs

BU001 v2, root accepted after independent review, proves for the SAME paid SB001 program and every legal budget

    risk_stat(T)<=min{1,2^17/sqrt(M)+3/Q+544 W(z,t)}.     (4.1)

Thus (4.1)<=min{1,CF}. Its binary structural step weights diagonal return errors by actual exit probabilities, uses the supported binary pair-chain reversal and weighted hitting bound H_s<=5/[sqrt(β)Π_s q_s], and integrates the weighted reciprocal count. The β>=M^-2 proof yields the sqrt(β) cutoff; for β<M^-2 the inherited β-free occupation estimate yields t=1. Zero-q states are omitted before division, and the all-zero quantized block is separately charged. This accepted lemma is stationary only; the general arbitrary-start TR001 theorem cannot replace sqrt(β) by β in this binary conclusion or transfer the improved cutoff to nonstationary starts.

For completeness, the program uses two paid singleton-copy heads and paid local pair/triple features (r=3). Its complete eight-coordinate value bank is the one-hot triple bank. A key receives weight κ when its preceding pair matches the terminal pair, and weight 1 otherwise. All M keys remain present. Each coordinate is downward-Q-quantized, then retained. The decoder chooses the two entries of the terminal pair's block ONLY AFTER this quantization; if their sum is positive it normalizes them, and otherwise uses the uniform distribution. Final ordered binary simplex output rounding is paid. Exact counts, denominators and unquantized row mass do not cross the cut. This program is admissible for D>=8,r>=3; the query pair belongs to S. Local-copy preprocessing does not add a global summary block. Mathematical padding to D is only an inclusion proof, not an implementation claim.

No β, Π, exit probability, return time or empirical count is supplied to the runtime decoder. These are analysis objects. For fixed supplied κ,Q the program is β-blind. Choosing budgets from the public β promise is separate setup, not online estimation or a free transcendental primitive.

Here is the unchanged SB001 v2 §6 ledger, reproduced to avoid confusing precision range with total cost. Set n_prog=M+3, ell=ceil(log2(n_prog+K+2)), k=bitlength(κ), and b=64(h+ell+k+1), with K=2. Persistent words have b bits, products retain all 2b bits and guarded temporaries at most 4b+4. The program pays all three n_prog-by-n_prog public masks; input and synthetic row; dense maps including zero entries; pair/triple AND features; all n_prog² edge scans in each head; integer cache generation; complete all-token eight-coordinate storage; divisions, block selection, fallback, rounding, explicit copies/clears; counters, addresses and serialization. No numerical n_prog² weight matrix is retained. With K kept visible for comparison, its bounds are

    T0=O(n_prog² K^6 b²),
    S=O(n_prog²+n_prog K³ b+K^6 b+b²).

For the addressed sequential alternative it pays instruction/opcode/address storage O(T0 b), and

    forward bitwork O(T0 S b), forward peak O(T0 b+S),
    offline bitwork O((T0+S)b²), offline peak O(T0 b+S+b²).

For the separate PURE alternative, T=T0+b, S'=S+b:

    depth O(T), width O(S'), sparse gate/hold records O(TS'),
    sparse wiring/coefficient bits O(bTS'),
    dense coefficient bits O(bT(S')²),
    dense forward/offline bitwork O(b²T(S')²),
    rolling two-layer numeric storage O(bS').

Sparse offline work is O(b²TS') if that representation is chosen. Each phase peak adds all simultaneous chosen parameters/program, inputs/public constants/masks when separately retained, outputs, rolling arrays and scratch; duplicate constant rails are charged twice. These alternatives cannot be combined by taking separate minima. The complete bank and all-token work remain paid even when only terminal output is exported. All of these costs are inherited, not improved by BS001. In particular reducing κ does not equate arithmetic word b, storage, offline work or compiled depth with grid bitlength h or effective logit range lnκ.

## 5. Exact statistical-order joint condition

Write a=sqrt(M), u=a/t=1/(sqrt(M)e0), f=1+ln(1+u), and

    Z_star=a f
      =sqrt(M)[1+ln(1+1/(sqrt(M)e0))].             (5.1)

This is the binary stationary PRODUCT threshold, not the grid threshold by itself:

    Q ≳ sqrt(M) AND κQ ≳ Z_star.                          (BS2)

The two conditions are simultaneous, and their meaning in target multipliers is as follows.

**Necessity for every target C0>0.** If an admissible procedure guarantees risk<=C0/a, even only on stationary sources, put B=max{1,C0/c}. BS1 implies Q>=a/B and W(z,t)<=B/a. With v=z/a, this last inequality is

    [1+ln(1+vu)]/v<=B.

If v>=1, its numerator is at least f, so v>=f/B>=f/B². If 0<v<1, concavity yields 1+ln(1+vu)>=v[1+ln(1+u)]=vf, so f<=B; the numerator is also >=1, so v>=1/B>=f/B². Therefore in EVERY case

    Q>=a/B,  κQ>=Z_star/B².                              (5.2)

This implication is meaningful without asserting that any arbitrarily small target C0 is achievable. It applies to infimum minimax risks too because the uniform lower persists under infima.

**Sufficiency for an explicit fixed multiplier.** If Q>=a and κQ>=Z_star, monotonicity of W and 1+fu<=f(1+u) give

    W(z,t)<=W(af,t)<=[f+ln f]/(af)<=2/a.

Thus risk_stat(T)<=2C/a (and <=1). More generally, for ANY fixed positive A,B0, if Q>=Aa and κQ>=B0 Z_star, then

    risk_stat(T)<= C max{1, A^(-1), 2 max{1,B0^(-1)}}/a.    (5.3)

For B0<1 use monotonicity of the numerator to get W(B0 Z_star,t)<=W(Z_star,t)/B0; for B0>=1 use decreasing W. This proves the usual order-equivalence of the joint conditions with constants independent of M,β.

There are always legal budgets: choose Q=2^max{4,ceil(log2 a)}, then a<=Q<=2a for M>=64, and κ=max{1,ceil(Z_star/Q)}. These satisfy the sufficient conditions, with κ<=1+Z_star/Q. Alternatively κ=1 and dyadic Q>=Z_star recover the larger original-interface-style grid schedule; many other allocations work. Budget selection using β is public promise-based selection, not learning β from data or a free transcendental runtime primitive. SB001's β-blind bitlength κ schedule remains available. This is not a theorem about fixed total precision or a universal optimum across multiple global blocks.

## 6. Least weight envelope in a square-root grid band

Fix positive c_-,c_+ and a legal Q with c_-sqrt(M)<=Q<=c_+sqrt(M). Define

    f_Q=1+ln(1+Q/(M e0)).

The least feasible INTEGER κ has order Θ_(D,r,c_-,c_+,C0)(f_Q) for each sufficiently large fixed target multiplier C0. The qualifier is essential: no feasibility at arbitrarily small prescribed risk multiplier is claimed.

Here is the direct lower, valid even for a hypothetical REAL budget κ>=1. The lower proof and UI001/BI001 apply to every finite real envelope. If risk<=C0/a, then W(κQ,t)<=C0/(c a). Since κ>=1, its numerator is at least f_Q. Therefore

    κ >= [c a/(C0 Q)] f_Q >= [c/(C0 c_+)] f_Q.          (6.1)

For the actual INTEGER upper choose κ=ceil(f_Q), so f_Q<=κ<=f_Q+1<=2f_Q. The inequality 1+κQ/t<=κ(1+Q/t) and lnκ<=κ give

    W(κQ,t)<= [f_Q+lnκ]/(κQ)<=2/Q.

The explicit BU2 bound is then at most

    [2^17+1091/c_-]/sqrt(M).                            (6.2)

Thus C0>=2^17+1091/c_- is one sufficient target. The nonempty feasible set of integers has a least element, bounded between the real-budget lower (6.1) and the integer construction ceil(f_Q). This is a weight-envelope order result, not a claim about fractional implementation weights or a fixed-total-bit optimum.

## 7. Sharp stationary alphabet contrast

Take β=1/M and legal Q≈sqrt(M). For K=2, e0=M^-1/2, so f_Q=1+ln(1+Q/sqrt(M)) is bounded above and below by positive band-dependent constants. Section 6 gives κ_min=Θ(1) for sufficiently large fixed target multiplier.

For every fixed K>=3, TR001 instead uses t=M max(β,1/M)=1. Its stationary lower gives κ_min=Ω(log M), and its unchanged paid upper gives κ_min=O(log M), again at a sufficiently large fixed target multiplier. In this comparison use the SAME all-state certificate P²>=βΠ, SAME stationary/actual-terminal loss and one-block local positive-weight interface, and fixed dimensions/locality admitting each upper. One can even fix a common D>=K³ and r>=3 for a chosen K>=3 and compare binary with that K under identical coordinate budgets. Constants remain architecture-dependent; there is no uniform-in-K,D,r claim. This is a genuine stationary alphabet-dependent threshold, not a change in initialization or a claim of universal neural-architecture optimality.

## 8. Provenance, diagnostics, scope and open successor

Direct source hashes and receipt hashes are in BS001_source_bindings_v1.json. BU001 v2 was accepted at 05:59:26 UTC, BI001 v2 at 05:52:32 UTC, with UI001 and TR001 separately accepted. Stale candidate-status headings in these source manuscripts do not override their version-specific acceptance receipts. The synthesis imports the exact UI/BI lower domains, the accepted statistical testing argument and BU2 stationary upper. The new work is the exhaustive completion, joint-product threshold and sharp alphabet comparison. No old source or delivery-stage-4 frozen file is modified.

Finite diagnostics test all four lower-completion branches, scalar logarithmic comparisons, threshold necessity/sufficiency and legal integer/dyadic allocations, including β=0,1,M^-2,1/256 and adjacent boundaries. They corroborate algebra, not the universal theorem. Fresh independent LLM review is separate from root acceptance and neither is formal verification or external peer review.

The improved arbitrary-start binary frontier remains OPEN. BU001 relies on stationarity, and this manuscript does not infer an arbitrary-start analogue from the older K>=3 TR001 theorem. The existing β-free arbitrary-start SB001 upper remains valid but does not establish this improved β-sensitive surface. Investigating whether a complete-suffix stationary mixture can preserve the weighted binary estimate without an excessive burn-in penalty is a natural successor, not an asserted result. No external contact, publication, upload, novelty priority, training attainability, original-network execution, deep/global-feature lower, sharp architectural-constant rate or total-resource optimality is claimed.
