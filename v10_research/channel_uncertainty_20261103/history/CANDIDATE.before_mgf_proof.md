# UMC001 — fixed nominal-channel uncertainty collapses the supplemental support classes

2026-11-03. Local author candidate, not independently reviewed or root accepted. This is a new research unit outside the frozen publication stage. No released artifact is changed. Historical pending language in imported candidates is superseded only by their explicit root acceptance receipts.

## 1. Finding and its exact interpretation

Let a known binary-input channel W0=(P0,P1) have a fixed nonempty finite output alphabet Y, and let d=TV(P0,P1). For a fixed known radius α≥0, the true channel is hidden and lies in

    Uα={W=(Q0,Q1): TV(Qb,Pb)≤α for b=0,1}.

The same encoder/decoder must work for every W in Uα, every source, every attack budget and every legal attack kernel. Both alphabet and nominal rows, and α, are fixed independently of sample size M. Physical binary channel-input length is fixed in advance.

For d>0 the supplemental constant-adaptation length orders are:

* α=0: the accepted BCC001 four-way classification, unchanged.
* 0<α<d/2: Θ_(W0,α)(log M), irrespective of nominal supports.
* α≥d/2: impossible at every finite length schedule; the robust minimax factor equals the no-message baseline factor exactly.

If d=0, the last conclusion holds for every α≥0. Thus an arbitrarily small **fixed positive** TV model-error ball removes the one-use and log-log advantages of exact support zeros. This is a robustness theorem under an added uniformity requirement, not a correction to the fixed-known-channel theorem. Constants are not uniform as α decreases to zero or approaches d/2. No sharp leading coefficient is claimed.

“Length order for constant adaptation” means existence of some finite M-independent achievable factor, and a necessary order for any sequence with uniformly bounded factors. It does not promise every requested constant below an intrinsic statistical floor.

## 2. Statistical models and quantifiers

Two separately specified source classes are covered; no first-order upper is exported to general order two.

**F: unrestricted binary first order.** Raw word X_0,...,X_(M+1), arbitrary initial PAIR law, hidden first-order transition table. The encoder sees the entire corrupted word. The free receiver baseline is its exact eight triple counts and actual protected final pair. The first pair is reconstructible by flow imbalance and need not be supplied. No other raw window or path-dependent datum is free. The accepted first-order gate is the repaired suffix gate from FOT002, not a homogeneous-first-edge assumption. Upper results cover all first-order tables; lower witnesses already obey the all-state pair certificate 1/M, so the same theorem also holds if this certificate restricts the class.

**O2: critical-certificate binary order two.** Hidden homogeneous θ_ab(c), stationary Π with P²(u,v)≥Π(v)/M for EVERY pair u,v, including unsupported rows. Every initial pair law is allowed, including starts outside stationary support. The target is the next-SYMBOL law θ_(Y_M), Y_M=(X_M,X_(M+1)). The exact one-bit interface is the original order-two half gate from accepted O2T001, not the first-order suffix gate. No unrestricted/no-mixing order-two or all-β assertion is made.

In both classes the attack is one source-independent offline Markov kernel on all words, changing at most k positions among 0,...,M−1 on every outcome, with k=0,...,M; both terminal symbols are protected. Counts are exact *as receiver messages*, but are computed on the corrupted word, not the clean word. The kernel cannot inspect predictor random seeds or subsequent channel noise. The hidden true W is fixed during an experiment; conditional on the complete pre-channel experiment and all independent shared seeds, channel noise is fresh memoryless W^R. Independent private encoder/decoder coins and independent free public coins are allowed. Feedback, channel calibration observations, variable/adaptive length, timing, noise-seed revelation and path-dependent shared seeds are absent. W is not revealed to either party. The rule may use M,W0,α and the specified source-class convention, but not the hidden source/table/start/k/kernel/W.

The loss is unconditional expected unsquared TV at the actual protected terminal target. Put

    g_M(k)=max{M^(-1/2),k/M}, ell_M=1+ln((M+2)/2),
    Γrob,j(M,R)=inf_(one E,D) sup_(W∈Uα, admissible source,start,k,kernel)
                  risk_W(E,D)/g_M(k), j∈{F,O2}.

The infimum is after the joint supremum. No optimal rule or minimax interchange is assumed. Let Γ0,j denote the corresponding baseline-only minimax factor. For M≥64 the accepted interfaces are

    c_j ell_M ≤ Γ0,j(M) ≤ C_j ell_M;
    exact-gate risk ≤ G_j g_M(k);
    every randomized full-history rule has normalized minimax factor ≥1/96.

Constants are

    F:  c_F=2^(-33), C_F=2^17, G_F=1024+2^20;
    O2: c_O2=2^(-30), C_O2=2^20, G_O2=2^17+2^23=8519680.

The actual stronger exact-gate risks are 1024/√M+2^20 k/M and 2^17/√M+2^23 k/M, respectively. These are imported accepted statistical theorems, not reproved here.

## 3. Identifiability boundary, including equality

For any Q0,Q1 in the class, the triangle inequality gives

    TV(Q0,Q1)≥d−2α.

If α≥d/2, set Q=(P0+P1)/2. Then TV(Q,Pb)=d/2 for both inputs, so the identical-row channel Wmid=(Q,Q) belongs to Uα. This also works for d=0 and every α≥0. Conversely an identical-row channel in Uα forces d≤2α, establishing the exact intersection boundary.

Under Wmid the full channel output can be independently generated by a baseline-only randomized decoder. For any proposed robust rule, simulate Q^R and run its decoder; the resulting baseline-only rule has exactly its risk at Wmid on every source/attack instance. Thus each robust rule's worst-case factor is at least Γ0,j(M), and taking an infimum preserves this. Conversely baseline-only rules can ignore the channel and work uniformly over W. Approximating the baseline infimum if necessary proves

    Γrob,j(M,R)=Γ0,j(M)  whenever α≥d/2.             (1)

This holds for every finite R, including any M-dependent finite schedule, and proves impossibility of uniformly bounded adaptation. For the separate whole-message model with NO free sample-dependent receiver information, Wmid instead makes the output independent of a clean IID Bernoulli p∈[1/4,3/4]. The uniform-prior absolute-loss minimum is 1/8, so worst-case risk≥1/8 and normalized factor≥√M/8. This is only an impossibility observation for that other model, not a whole-message upper theorem here.

## 4. Robust O(log M) upper without learning W

Assume 0≤α<d/2, hence d>0. Define the NOMINAL event and threshold

    A={y∈Y:P1(y)>P0(y)},
    p_b=P_b(A),  p1−p0=d,
    τ=(p0+p1)/2,  γ=d/2−α>0.

The event identity p1−p0=d follows by summing the positive part of P1−P0. By the variational characterization of TV, every admissible true W has

    q0=Q0(A)≤p0+α=τ−γ,
    q1=Q1(A)≥p1−α=τ+γ.                            (2)

Compute the source-class-appropriate exact gate G from the corrupted word and send that same bit R times. From the channel outputs form T=R^(-1)Σ_i 1{V_i∈A}; decode gate 1 when T≥τ, otherwise gate 0. R≥1 here; unused inputs, if any, may be ignored.

Conditional on every complete pre-channel state with gate b, the indicators are independent Bernoulli(q_b). Hoeffding's bounded-variable bound and (2) therefore give separately

    Pr(error | any pre-channel state,G=b,W)≤exp(−2Rγ²), b=0,1.   (3)

Ties assigned to 1 are covered: gate-0 error is the closed upper-tail event; gate-1 error is contained in the closed lower-tail event. For completeness, the concentration bound follows from E exp(t(Z−EZ))≤exp(t²/8) for a [0,1]-valued Z, multiplication for independent variables and exponential Markov with t=4γ; the negative tail uses −t. No Bayes-average to maximal-error conversion is needed.

Couple the decoded-gate receiver with the exact-gate receiver using identical receiver coins. Their predictions coincide whenever the gate is correct; TV loss lies in [0,1]. Hence for every instance and every W∈Uα,

    risk_noisy≤risk_exact+exp(−2Rγ²),
    Γrob,j(M,R)≤G_j+√M exp(−2Rγ²).                  (4)

In particular

    R≥ceil(ln M/(4γ²))                             (5)

attains factor G_j+1 for M≥64, uniformly over hidden W. Only W0 and α determine the decoder, and there are no training/calibration samples. Conditional independence of (3) is essential; independence of the error event from the path is NOT asserted or needed. The ordinary baseline rule also yields Γrob,j≤C_j ell_M for all R.

## 5. Arbitrary-code Ω(log M) lower for every positive radius

Assume 0<α<d/2. Let s=|Y| and U be uniform on the ENTIRE stipulated output alphabet, including any symbols null under both nominal rows. Choose

    δ=α/2 ∈(0,1/4),   Q_b*=(1−δ)P_b+δU.

(The upper bound is strict since α<d/2≤1/2.) Then

    TV(Q_b*,P_b)=δ TV(U,P_b)≤δ≤α;
    Q_b*(y)≥δ/s>0;
    Q1*−Q0*=(1−δ)(P1−P0)≠0.

Thus one fixed W*∈Uα has equal full supports and distinct rows. It is fixed independently of M and is a legal adversarial choice for the robust supremum. Let

    κ*=max_y max{Q0*(y)/Q1*(y), Q1*(y)/Q0*(y)}∈(1,∞).

In fact κ*≤s/δ. For every two binary codewords h,h' and output v, the product likelihood satisfies W*^R(v|h)≤(κ*)^R W*^R(v|h'). Integrating any two encoder input distributions preserves this pointwise domination, including after conditioning on any independent public seed. It applies to arbitrary full-word randomized encoders, not only repeated gates.

The accepted BSC001 finite likelihood transport, with its explicitly accepted BCC001 finite-output substitution and O2T001 witness embedding, gives for either source class j:

    M+1≥2^160 and (κ*)^R≤(M+1)^(1/8)
       ⇒ Γrob,j(M,R)≥2^(-32) ln(M+1).               (6)

Here is the exact logical use of that dependency. For any robust E,D, freeze W=W*. Its rule is an admissible fixed-channel rule, even though it was not designed knowing W*. The fixed-channel theorem is valid for EVERY such rule, so bounds its worst-case source/attack factor. Taking the larger robust supremum and then the infimum preserves the same numerical lower. Extra knowledge of W* in the comparison theorem can only enlarge the design class and cannot invalidate a lower bound. No estimate of unknown W is inserted.

The inherited transport compares equal-baseline clean y and relocated w at terminal pair 00. Pointwise target triangle inequality and likelihood domination give

    attacked_null_loss(w)≥a−β−(κ*)^R clean_actual_terminal_loss(y).

Only the nonnegative clean-loss penalty is multiplied; target separation is not. The legal predeclared FOT001 mixture attack transports nonnegative actual null losses before inserting this signed inequality. These are the load-bearing conditions behind (6); no new attack depending on W outputs, predictor seeds or source table is introduced. O2 lower witnesses are the same admissible stationary first-order tables embedded by θ_ab(c)=T(b,c), with all-state certificate 1/M.

Consequently if Γrob,j(M,R(M))≤B for all sufficiently large M, (6) forces eventually

    R(M)>ln(M+1)/(8 ln κ*).                         (7)

Equations (5) and (7) prove Θ_(W0,α)(log M). One can weaken (6) and (7) by replacing κ* with the explicit bound s/δ, if a closed numerical constant is preferred. This is a necessity for arbitrary codes and independent coins. Full-history floor 1/96 remains valid by composition and is not obtained by asserting that an arbitrary message is less informative than a chosen gate.

## 6. Zero-radius case, computation and scope

At α=0 the class is exactly {W0}; accepted BCC001/O2T001 apply: identical rows impossible, disjoint supports minimum one input, unequal overlapping supports Θ(log log M), equal supports distinct rows Θ(log M). The positive-radius lower above deliberately does not apply at δ=0; its finite likelihood domination vanishes at nominal support zeros. There is no contradiction in the discontinuity of the fixed-parameter asymptotic orders.

For fixed rational nominal probabilities and rational α with α<d/2, A,τ,γ and (5) can be implemented with exact comparisons; compare the integer indicator count with Rτ using a fixed nominal denominator. A conservative integer R satisfying (5) suffices, so no exact transcendental ceiling oracle is necessary. Gate computation retains the accepted one-pass O(log M) auxiliary statistics space and O(M log M) naive bit-operation bound; channel decoding counts up to R in O(log R) bits. With fixed constants R=O(log M), this adds only O(log M) output operations and finite fixed-precision nominal constants. For arbitrary real nominal parameters this is a statistical existence theorem, not a claimed effective real-number implementation without a representation/access model.

The radius may exceed 1 without changing the impossibility conclusion (TV≤1); no small-radius convention is needed for (1). Output-alphabet finiteness and fixed known nominal rows are essential to the stated constants. No result is asserted here for α=α_M, unknown alphabet, infinite alphabet, simultaneous unknown source/channel calibration, nonmemoryless or adversarial channel noise, feedback, variable/adaptive length, corrupted free count messages, next-pair targets under O2, unrestricted order-two sources, higher source order, neural implementation, learning, sharp constants or novelty. A whole-message upper would require a separate robust coding argument; known-W ML decoding must not be imported for hidden W.

## 7. Failed or insufficient routes

1. Nominal exclusive-symbol decoding is not uniformly zero-error on any positive TV ball. Previously impossible outputs acquire positive mass, so its detectable-erasure branch cannot simply be retained.
2. Lower-bounding only by the smallest row separation d−2α proves identifiability, not the application-specific Ω(log M) communication lower. The fixed full-support witness plus accepted transport is needed.
3. A common-component minorizer attenuates the old log M penalty multiplicatively and gives only Ω(log log M), insufficient for the new sharp order.
4. Testing with the unknown W's likelihood is not an admissible robust upper. The fixed nominal event A and threshold τ avoid that mistake.
5. Small average gate error does not suffice uniformly over the unknown source/path. Equation (3) bounds both conditional gate classes separately.
6. Independence of noise given the pre-channel state does not imply gate-error independence from that state; coupling uses only the uniform conditional bound.
7. The midpoint obstruction includes α=d/2 exactly. A strictly positive robust row gap cannot be extended to that equality case.
8. The first-order statistical upper cannot be silently used for general order-two sources. Section 2 retains the separate accepted critical-certificate O2 gate.
9. A radius tending to zero with M cannot be classified by a fixed-positive-radius Θ statement; the lower witness's likelihood constant then also changes with M.

## 8. Dependencies and disposition

Read in full for this derivation: `../resumption_20261103/channel_classification/CANDIDATE.md`, `../resumption_20261103/bsc_sharp/CHANNEL_LIKELIHOOD_LOWER.md`, `../resumption_20261103/order_two_transfer/CANDIDATE.md`, and each unit's `ROOT_ACCEPTANCE.json`. BCC001 receipt accepts the complete four-class result and finite-output substitution; BSC001 accepts the clean-loss likelihood transport; O2T001 accepts the critical-certificate statistical interface, full witness inclusion and supplemental transfer. Underlying FOT002/FOT003/statistical manuscript proofs are explicit accepted dependencies imported through those interfaces, not claimed independently rederived here.

`SOURCE_BINDINGS.json` binds these six read artifacts and records checks against each root receipt's candidate hash. This candidate has no acceptance receipt of its own. Independent analytic review must check the quantifiers, sharp midpoint boundary, positive-radius full-support witness, uniform test tails, source-class separation and applicability of the accepted likelihood interface. No external writes, manuscript changes, commits, uploads, publication, formal verification or external peer review were performed.
