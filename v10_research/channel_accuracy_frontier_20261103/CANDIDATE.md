# CAF001 — shrinking channel-uncertainty radius: a uniform supplemental length frontier

2026-11-03. New local author candidate, not independently reviewed or root accepted. Separate from released commit 612b76d and all earlier candidates. No publication, repository write, or novelty claim. Historical pending headers in dependencies are superseded only by their explicit root acceptance receipts.

## 1. Statement, with joint quantifiers

Fix a binary-input channel W0=(P0,P1) on a fixed finite nonempty alphabet Y, with d=TV(P0,P1)>0. Fix 0≤αmax<d/2. The known radius α can be ANY number in [0,αmax], including a function of the sample size M. The actual hidden channel W=(Q0,Q1) belongs to

    Uα={W: TV(Qb,Pb)≤α, b=0,1}.

W is fixed within an experiment and fresh memoryless conditional on its entire pre-channel state. Define

    L=L_M=1+ln((M+2)/2),
    Dα=1+ln(1/α) for α>0,
    t(M,α)=ln M/Dα for α>0, and t(M,0)=0.

Let S_b={y:P_b(y)>0}. At the fixed feasible target B_j=G_j+2, in the supplemental observation models j=F,O2 specified below, the minimum fixed physical binary-input length satisfies, uniformly for 0≤α≤αmax and M≥M0,

    disjoint supports:             R*_j(M,α)=Θ(1+t(M,α));
    unequal overlapping supports:  R*_j(M,α)=Θ(ln L+t(M,α));
    equal supports, distinct rows: R*_j(M,α)=Θ(ln M).

All implicit positive constants and M0 may depend on W0, αmax and the fixed target/source interface, but NOT on α or its schedule. In particular the same M0 works even if α is exponentially or super-exponentially small. This is sharp order, not sharp leading constants or an exact risk curve. The upper holds for B_j=G_j+2 (also any larger target); the necessity holds for every fixed finite target B. Nothing promises an arbitrary target below the statistical floor.

Here R* is the minimum integer R admitting one encoder/decoder whose factor is ≤B_j over the entire joint supremum of W, source, start, budget and attack. This definition needs no minimax optimizer: the explicit upper provides a feasible integer, and the lower excludes all smaller integers. The same lower conclusions also hold when phrased using an infimum of factors.

## 2. Experiment and accepted statistical interfaces

Raw word X_0,...,X_(M+1); actual final pair is protected. An offline source-independent kernel on ALL words changes at most k of positions 0,...,M−1 on EVERY outcome, for k=0,...,M. It cannot inspect predictor random seeds or future channel noise. The encoder scans the full corrupted word. The receiver freely observes its exact eight triple counts and protected terminal pair. Counts are exact as communicated messages but count the corrupted word. Flow imbalance reconstructs the initial pair; it is not extra information. No other raw windows are free.

**F:** arbitrary binary first-order transition table and arbitrary initial PAIR law. Use the accepted FOT002 repaired suffix gate, which discards X0 rather than assuming the first edge is homogeneous. Lower witnesses also satisfy the all-state pair certificate 1/M, so the conclusion remains true if that certificate restricts F.

**O2:** arbitrary homogeneous binary order-two table θ_ab(c) having a stationary Π and supplied all-state certificate P²(u,v)≥Π(v)/M for EVERY pair u,v, including unsupported rows; allow every initial pair law. Target is the next-SYMBOL law θ_(X_M,X_(M+1)). Use the original accepted O2 half gate on M pair departures, NOT the first-order suffix gate. No unrestricted/no-mixing O2 statement is made.

At fixed (M,W0,α,j), one procedure works for every hidden table, initial law, k, kernel and W. R is fixed before observing data. Conditional on the complete pre-channel experiment and independent shared seeds, noise has law W^R. Private encoder/decoder coins and independent free public coins are allowed. No path-dependent shared seed, revealed mask or noise seed, feedback, variable/adaptive length, timing channel, calibration samples, or hidden free channel observations. Channel outputs and their membership in specified nominal events are observed exactly.

Loss is unconditional expected unsquared TV at the actual terminal target, normalized by

    g_M(k)=max{M^(-1/2),k/M}.

The accepted source interfaces, for M≥64, are baseline factor between c_j L and C_j L, an explicit exact-gate estimator with risk ≤G_j g_M(k), and full-history normalized minimax floor 1/96, where

    F:  c_F=2^(-33), C_F=2^17, G_F=1024+2^20;
    O2: c_O2=2^(-30), C_O2=2^20, G_O2=2^17+2^23.

These come from accepted BCC001/FOT002 and O2T001. In particular baseline and exact-gate rules are source-independent and work for every k with the same rule. Their precise stronger risk bounds are 1024/√M+2^20 k/M and 2^17/√M+2^23 k/M. We import the accepted statistical theorems rather than claim a fresh proof of them.

## 3. Uniform finite lower bounds for arbitrary randomized codes

### 3.1 Nominal witnesses and no-message obstruction

W0 belongs to every Uα, so every robust procedure has at least the nominal-channel lower bounds. At R=0 the factor is at least c_j L. If λ0=Σ_y min{P0(y),P1(y)}>0, accepted common-component domination gives, for every R,

    Γrob,j(M,R,α)≥c_j L λ0^R.                       (1)

Indeed every codeword product law dominates the common submeasure ∏min(P0,P1), of mass λ0^R, and this persists under arbitrary private encoding mixtures and conditional on free shared seeds. A baseline-only receiver can sample its normalized common component. Nonnegative loss yields (1), with no ordering assumption between arbitrary messages and the historical gate.

For unequal overlapping supports 0<λ0<1. Any factor ≤B therefore requires

    R≥ln(c_j L/B)/ln(1/λ0)                          (2)

when the numerator is positive. If L≥(B/c_j)^2 and B/c_j≥1, this is at least (ln L)/(2 ln(1/λ0)). Enlarging M0 also covers B/c_j<1. In all cases R≥1 once c_j L>B.

For equal supports and distinct rows, ignoring common null symbols, let

    κ0=max_y max{P0(y)/P1(y),P1(y)/P0(y)}∈(1,∞).

The accepted BSC001 finite likelihood theorem and BCC001 finite-output substitution state

    M+1≥2^160 and κ0^R≤(M+1)^(1/8)
      ⇒ Γrob,j(M,R,α)≥2^(-32) ln(M+1).             (3)

O2T001 embeds the identical stationary first-order witnesses into the critical-certificate O2 class. Thus, once 2^(-32)ln(M+1)>B, every feasible length obeys R>ln(M+1)/(8ln κ0), uniformly in α.

### 3.2 Positive-radius full-support witness with explicit α dependence

For α>0, let s=|Y|, U the uniform law on the ENTIRE stipulated alphabet (including symbols null under both nominal rows), and set

    δ=α/2,   Q_b*=(1−δ)P_b+δU.

Since α≤αmax<d/2≤1/2, 0<δ<1/4. Row TV distance to P_b is at most δ≤α; all probabilities are at least α/(2s); and Q1*−Q0*=(1−δ)(P1−P0) is nonzero. Hence W* is admissible, full-support and informative, and its maximum row likelihood ratio satisfies

    1<κ*≤2s/α.

This W* MAY depend on M through α. We use the accepted FINITE implication, not a fixed-channel asymptotic result with an untracked constant. For every M and α satisfying its displayed hypotheses,

    M+1≥2^160 and (2s/α)^R≤(M+1)^(1/8)
      ⇒ Γrob,j(M,R,α)≥2^(-32)ln(M+1).              (4)

For clarity, product likelihood domination holds for all input codewords and therefore all unrelated randomized encoder mixtures, conditional on each free shared seed. The accepted transport compares equal-baseline clean y and relocated w at terminal 00 and bounds attacked loss below by a−β−(κ*)^R times the nonnegative ACTUAL-TERMINAL clean loss. Only that loss penalty pays the ratio. The source-independent predeclared attack transports actual nonnegative null loss before inserting the signed triangle inequality. The finite theorem has no residual dependence on channel parameters. Freezing this admissible W* is legitimate even though a robust rule does not know it: a lower valid for every fixed-channel rule is valid for this smaller design class.

If 2^(-32)ln(M+1)>B, (4) forces

    R>ln(M+1)/(8ln(2s/α))
     ≥ln M/(8 A_s Dα),   A_s=max{1,ln(2s)}.        (5)

The last inequality follows from ln(2s/α)≤A_s[1+ln(1/α)]. M0 here depends on B but not α. At α=0 we assert only t(M,0)=0 and do not divide by an infinite likelihood ratio or invoke W*.

Combine (5) with R≥1 for disjoint supports, with (2) for unequal overlapping supports, and with (3) for equal supports. For nonnegative u,v, max(u,v)≥(u+v)/2, so the stated SUM orders follow without claiming independent risks add. These lower bounds hold for arbitrary full-word codes, not just the constructions below. The full-history floor remains separately valid by composition.

## 4. A uniform robust fallback test for all radii

Let

    A={y:P1(y)>P0(y)}, p_b=P_b(A),
    τ=(p0+p1)/2, γ0=d/2−αmax>0.

Then p1−p0=d. Every true channel in every Uα with α≤αmax satisfies Q0(A)≤τ−γ0 and Q1(A)≥τ+γ0. Repeat the exact source-class gate R times, decode 1 when the empirical fraction of A is ≥τ, otherwise 0. Each of the TWO conditional bit errors, separately for every complete pre-channel state, is ≤exp(−2Rγ0²). This is not merely a Bayes-average error statement. Ties go to 1; the upper-tail bound covers equality and the other error is contained in its closed lower tail.

The concentration follows from the Bernoulli centered log-mgf f with f(0)=f'(0)=0 and f''≤1/4, hence f(t)≤t²/8 for either sign of t, followed by exponential Markov and minimization. Coupling decoded and exact estimators with identical receiver randomness gives

    risk≤risk_exact+exp(−2Rγ0²),
    Γrob,j≤G_j+√M exp(−2Rγ0²).                     (6)

Thus

    R_H=max{1,ceil(ln M/(4γ0²))}                    (7)

attains G_j+1. It does not require true W or calibration. This supplies the equal-support upper outright. In the next two cases it is used only when α exceeds a fixed small nominal threshold, where Dα is uniformly bounded and ln M=O(t(M,α)). If that interval is empty, no fallback case is necessary.

## 5. Disjoint nominal supports: uniform 1+t upper

When S0 and S1 are disjoint, decode one output as 1 on S1 and 0 elsewhere. For input 1, error probability is Q1(Y\S1)≤α. For input 0, error probability is Q0(S1)≤α. This handles symbols nominally null under both inputs without pretending they cannot occur under W. At α=0, one use is exact.

For 0<α≤a_D=1/16, repeat the gate R≥1 times and majority-decode these tentative bits, with either fixed tie convention. Error entails at least ceil(R/2) wrong tentative bits. Conditional on each full pre-channel state the bits are independent and each error probability is ≤α, so a union bound over subsets gives

    Pr(error | prestate)≤2^R α^(R/2)
                        ≤α^(R/4).                 (8)

The second inequality is precisely α≤1/16. Choose

    R_D=max{1,ceil(2ln M/ln(1/α))}.                 (9)

Then (8) is ≤M^(-1/2); coupling as in (6) yields factor ≤G_j+1. Since ln(1/α)≥ln16,

    Dα/ln(1/α)≤1+1/ln16,

and (9) is at most a fixed multiple of 1+t(M,α). If a_D<α≤αmax, use (7). There Dα≤1+ln16, so (7) again is O(1+t), with constants depending only on αmax and W0. At α=0 choose exactly R=1. This proves the upper with no α-dependent hidden constant.

## 6. Unequal overlapping supports: erasure/error separation with two slots

Choose a nonempty exclusive event after relabeling channel inputs if necessary:

    E=S1\S0, P0(E)=0, p=P1(E)∈(0,1).

If only the other support difference is nonempty, swap the physical channel labels throughout; the semantic gate and its estimator are unchanged. Overlap guarantees p<1. Define the fixed rational-form threshold

    a_P=(p/24)^2.

It satisfies a_P≤p/4 and a_P<1. First treat 0≤α≤a_P. For the true channel write q_b=Q_b(E). Then q0≤α, q1≥p−α. Encode semantic gate 0 as physical (0,1), gate 1 as physical (1,0). Inspect E-membership in each slot:

* exactly one E occurrence: decode the gate whose designated input-1 slot contains it;
* neither or BOTH slots report E: output an erasure.

Unlike exact-support decoding, BOTH is no longer null and must be explicitly erased. For either semantic gate, with the labels interpreted correctly, the block probabilities are exactly

    correct: c=q1(1−q0),
    wrong:   w=q0(1−q1),
    erased:  e=q0q1+(1−q0)(1−q1).

The probabilities are identical for the two semantic gate values because exchanging gate values exchanges slots; this remains true for asymmetric W. In particular

    c≥(p−α)(1−α)≥p/2,   w≤α.                      (10)

The first inequality can be weakened using α≤p/4, p≤1: (p−α)(1−α)≥(3p/4)(3/4)=9p/16≥p/2.

Send n independent two-slot blocks of the same gate. Let H be the number of nonerased blocks. If H<(p/4)n, ABSTAIN and use the accepted baseline estimator. Otherwise use the majority decoded gate among the H nonerased blocks and run the exact-gate estimator with that gate. Ties in this majority are resolved by a fixed semantic bit. These definitions apply to noninteger thresholds literally; H≥(p/4)n is equivalent to H≥ceil(pn/4). Physical length is exactly 2n, without feedback or stopping early.

### 6.1 Uniform abstention bound

By (10), the nonerasure probability c+w is ≥p/2. The n indicators are conditionally independent. The same bounded-variable lower-tail calculation as §4 yields

    Pr(abstain | complete prestate)≤exp(−np²/8).   (11)

The bound holds even after conditioning on the random coins that will produce the baseline and exact-gate predictions. Those coins can be sampled in advance independently of channel noise. Independence of a semantic decoding error from source data is not assumed; only the displayed uniform conditional bound is needed.

### 6.2 Uniform wrong-nonabstained bound

On a nonabstained wrong majority, the number Z of wrong blocks is at least H/2≥pn/8, including a wrong decision on a tie. Put r=p/8. For α>0 we have α≤a_P<r. Conditional on the complete prestate, Z is a sum of independent Bernoulli indicators with probability w≤α. Its mgf obeys

    E exp(tZ)≤exp[nα(e^t−1)].

Use t=ln(r/α)>0. Exponential Markov (valid for the real threshold rn, so no integer rounding gap) gives

    Pr(Z≥rn)≤exp[−rn ln(r/α)+n(r−α)]
             ≤(eα/r)^(rn)=(8eα/p)^(pn/8).

Since e<3 and α≤(p/24)^2, 8eα/p≤sqrt(α). Consequently

    Pr(wrong and not abstained | complete prestate)
        ≤α^(pn/16).                               (12)

At α=0 there are NO wrong blocks, so the probability is exactly zero; use this fact directly rather than a logarithm at zero. This is a maximal conditional guarantee for each gate, not average error under an assumed prior.

### 6.3 Correct risk accounting for a potentially data-dependent abstention

On the correct, nonabstained event the prediction equals the exact-gate prediction. On abstention it equals a coupled baseline prediction. On a wrong, nonabstained event its TV loss is at most 1. Pathwise, with losses ℓ_exact and ℓ_base fixed by the prestate and sampled receiver coins,

    ℓ_actual≤ℓ_exact+1_abstain ℓ_base
                       +1_wrong,nonabstained.

Apply (11) after conditioning on that complete prestate, and then average. For EVERY source/start/k/kernel and EVERY W∈Uα,

    risk_actual≤risk_exact+exp(−np²/8) risk_base
                              +α^(pn/16)          (13)

when α>0, and omit the final term when α=0. It is invalid to replace the second term by a small marginal abstention probability times baseline risk without this conditional argument. Here it is justified. The exact slot symmetry even gives constant conditional ternary probabilities for fixed W, but (13) needs only their uniform bounds.

Thus, for α>0,

    Γrob,j≤G_j+C_j L exp(−np²/8)+√M α^(pn/16).      (14)

Choose the integer

    n=max{1,
          ceil((8/p²) ln(C_j L)),
          ceil((8/p) ln M/ln(1/α))}.               (15)

At α=0 omit the third entry. The second contribution in (14) is at most 1; the third is at most 1. Therefore R=2n attains B_j=G_j+2, including α=0, where it actually attains G_j+1.

For M≥64, ln L is positive and bounded below by a fixed positive constant. Hence the first two entries in (15), including ceilings and the constant ln C_j, are O_j,p(ln L). On 0<α≤a_P,

    Dα/ln(1/α)≤1+1/ln(1/a_P),

so its third entry is O_p(t(M,α)), up to an additive 1 already absorbed by ln L. Consequently R=O(ln L+t). For a_P<α≤αmax use the robust fallback (7); Dα≤1+ln(1/a_P), so R_H=O(t), with constants independent of α. If αmax=0, only the α=0 construction is used. This proves the claimed uniform upper in every boundary case.

## 7. Joint threshold and interpretation

For a fixed finite lower target B, choose M0≥64 so that M0+1≥2^160, 2^(-32)ln(M0+1)>B, c_j L_M0>B, and, when relevant, ln(c_j L_M/B)≥(ln L_M)/2 for all M≥M0. The latter follows by taking L_M0≥max{1,(B/c_j)^2}. All conditions are monotone in M, all involve only accepted fixed constants and B, and NONE involve α. Combine the explicit lower coefficients from §§3.1–3.2 with the uniform upper coefficients from §§4–6. This establishes one common threshold for the entire continuum [0,αmax]. It is not an exchange of limits M→∞ and α→0.

Examples of the order formula (not leading constants):

* If α=M^(−c) for fixed c>0, disjoint supports retain O(1) length, unequal overlapping supports retain Θ(ln ln M), and equal supports still require Θ(ln M).
* If α=(ln M)^(−c), the extra term is Θ(ln M/ln ln M), dominating the partial-support baseline term eventually.
* For fixed positive α≤αmax the first two orders become Θ(ln M), agreeing with accepted UMC001. At α=0 they recover BCC001/O2T001 exactly in order (and disjoint supports need exactly one use for sufficiently large M at this target).

These are consequences for a GIVEN certified uncertainty radius. No theorem here says any number of calibration samples, floating-point bits, training steps, or model-fitting effort produces that radius. In particular α is not an uncharged estimate of W. Distance to the nonidentifiability boundary is kept positive by fixed αmax<d/2; allowing αmax approach d/2 with M is a different frontier.

## 8. Computation, dependencies and limits

The encoding only computes the accepted source-specific exact gate. One pass uses O(log M) auxiliary statistics bits and O(M log M) conservative naive bit operations; raw resident input, if retained, costs M+2 bits and is not auxiliary space. Decoding needs event-membership tests and counters up to R or n, O(log(R+1)) counter bits and O(R log(R+1)) conservative counter bit operations. No exponential codebook, path-dependent mask, variable stopping rule or silent uncharged message is used. With fixed nominal data and αmax, every displayed construction has R=O(log M), uniformly in α.

For rational nominal rows and rational supplied α, the event E or A, and comparisons with p n/4 and τR, admit exact rational arithmetic. Logarithmic ceiling formulas specify theoretical sufficient integers; they can be conservatively implemented by dyadic upper/lower bounds rather than an exact transcendental comparison oracle. For example, floor(log2(1/α)) is positive in the small-radius branches and yields a constant-factor lower bound on ln(1/α); integer bit lengths give upper bounds on ln M and ln(C_j L). These replacements preserve orders and the sufficient inequalities. Reading/processing an arbitrarily long rational representation of α is an additional input cost, NOT claimed uniformly poly(log M). Arbitrary real parameters yield statistical existence unless a suitable representation/access model is supplied.

Read source dependencies: BCC001 `../resumption_20261103/channel_classification/CANDIDATE.md` and ROOT_ACCEPTANCE.json; BSC001 `../resumption_20261103/bsc_sharp/CHANNEL_LIKELIHOOD_LOWER.md` and ROOT_ACCEPTANCE.json; O2T001 `../resumption_20261103/order_two_transfer/CANDIDATE.md` (identical to TRANSFER.md) and ROOT_ACCEPTANCE.json; UMC001 `../channel_uncertainty_20261103/CANDIDATE.md` and ROOT_ACCEPTANCE.json. UMC001 was root accepted at 2026-11-03T02:25:41.835718+00:00. We use its model/robust event argument and explicit finite witness construction, not its fixed-α asymptotic statement as a uniform theorem. SOURCE_BINDINGS.json records source digests and verifies accepted candidate hashes. The accepted statistical proofs and mixture lemma remain imported dependencies; finite checking cannot replace their proof.

New derivation here: joint uniform α,M bounds, small-radius disjoint decoding, a two-slot error/erasure channel under support contamination, thresholded abstention plus conditional risk composition, and the explicitly uniform use of the finite likelihood theorem. No whole-message/no-free-count theorem, infinite alphabet, correlated/adversarial channel noise, variable/adaptive length, feedback, corrupted receiver count messages, unrestricted O2, general source order, calibration sample complexity, neural realization, learning guarantee, optimal leading constants, or novelty certification. Independent review and root disposition are still required; LLM review is not formal verification or external peer review.
