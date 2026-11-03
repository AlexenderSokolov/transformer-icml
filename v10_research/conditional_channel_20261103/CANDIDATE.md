# CCH001 — conditional fidelity, not memorylessness, preserves the sharp channel frontiers

2026-11-03. New local author candidate. Independent review and root acceptance pending. No accepted file is changed, and no publication is made. Historical pending headers in dependencies are superseded by their explicit root acceptance receipts, not by this candidate.

## 1. Result

Fix a known finite nonempty output alphabet and nominal binary-input rows P0,P1. Let d=TV(P0,P1)>0. For each M a known radius α may be any number in [0,d/2), including an arbitrary M-dependent choice. Put

    γ=d/2−α, L=1+ln((M+2)/2),
    T=ln M/[1+ln(1/α)] for α>0; T=0 for α=0.

Set H=1+T for disjoint nominal supports; H=ln L+T for unequal overlapping supports; H=ln M for equal, distinct nominal supports. In the precise conditional-channel model below, the minimum fixed binary-input length for the feasible target G_j+2 satisfies

    supplemental: R* = Θ_(P0,P1,j)(H/γ²),
    whole-message: R* = Θ_(P0,P1,j)(ln M/γ²), j∈{F,O2}.

One threshold M0 and comparison constants work for ALL α∈[0,d/2); they are independent of its schedule. The necessary orders apply to every fixed positive finite target; sufficiency is asserted at the stated feasible targets or larger ones. Constants may depend on the fixed nominal channel and target. No uniformity in d→0 or optimal leading coefficient is asserted.

Thus the accepted CMF001 sharp orders extend to channels with arbitrary history dependence and state-dependent drift, provided their per-use conditional distributions obey the row-TV constraint. UMC001's fixed-radius and CAF001's fixed-gap conclusions follow as special cases. UWC001's finite bound R≤240 ceil(4/γ²)B and maximal payload error ≤2^(−6B) also extend without changing constants.

At α≥d/2 (or d=0 at any α≥0), supplemental robust minimax equals the baseline-only minimax for every finite length; whole-message worst clean risk is at least 1/8 for every finite length. These conclusions concern the robust supremum, not every individual state-dependent channel.

Mere per-coordinate marginal fidelity does NOT suffice: for nominal binary identity and any 0<α≤1/2, a globally shared replacement event yields marginal BSC(α) at every coordinate but a whole-transcript common component of mass 2α. Every fixed-length code for N equiprobable messages has average error at least 2α(1−1/N), even with independent shared/private coins. Whole-message clean prediction risk is at least α, uniformly over length; supplemental normalized factor is at least 2α Γ0,j(M). This is an all-code obstruction, not a repetition counterexample.

## 2. Statistical experiment and nonanticipating channel model

The raw binary word is X0,...,X_(M+1). A single source-independent offline attack kernel, defined on all words, changes at most k positions among 0,...,M−1 on EVERY outcome and preserves both final symbols. k∈{0,...,M} is hidden. This kernel does not see encoder/decoder coins or channel randomness. The encoder scans the entire corrupted word Z. Loss is expected unsquared TV at the actual protected next-symbol target, normalized by

    g_M(k)=max{M^(−1/2),k/M}.

F consists of arbitrary homogeneous binary first-order transition tables with arbitrary initial PAIR law; the initial edge need not follow the table. The accepted repaired suffix gate discards X0. O2 consists of homogeneous binary order-two tables θ_ab(c), with stationary pair law Π and supplied certificate P²(u,v)≥Π(v)/M for EVERY pair u,v, including unsupported rows, and every initial pair law. Its target is the next-SYMBOL law θ_(X_M,X_(M+1)). Use the original O2 half gate, not F's suffix gate. No unrestricted O2 result is asserted.

In the supplemental model the receiver freely sees exact eight triple counts of Z and its actual protected final pair. Counts are noiseless messages about the corrupted word. The initial pair is reconstructible by flow imbalance; no other raw window is free. In the whole-message model NO sample-dependent information is free, including counts, endpoints, query or encoder state. Public experiment parameters and independent public seeds are free in both models.

Choose the nonfeedback encoder and decoder and a deterministic integer R before observing the sample. Encoder private coins, decoder private coins and shared coins are independent of the source and attack and may be presampled. Let S denote the COMPLETE pre-channel statistical state: hidden source parameters, source word, attacked word and attack outcome, every protocol coin, and every sample-dependent quantity fixing targets, baselines and exact/baseline predictions. Conditioning on S is for analysis, not a disclosure to either party. H^R=h(S) is fixed before any channel output. Decoder coins are included so that potential exact and baseline losses are S-measurable.

For each i use a stochastic kernel K_i(·|s,y_<i,b), defined for b=0,1, satisfying

    TV(K_i(·|s,y_<i,b), P_b)≤α.                       (C)

The actual law is generated sequentially as

    Pr(Y_i∈· | S,Y_<i)=K_i(·|S,Y_<i,H_i).

The requirement may hold almost surely on reachable histories; specifying it on all states/histories is an equivalent convenient stronger formulation for constructions, with arbitrary admissible extensions off support. Kernels may depend on time, the complete pre-channel state, and past outputs. They do not access future channel random innovations. There is no encoder feedback, stopping, adaptive length, timing, calibration sample or revealed channel seed. A physical latent-memory mechanism is allowed only when its resulting conditional kernels after integrating unobserved channel randomness satisfy (C). A persistent hidden random mode does NOT automatically qualify simply because its unconditional marginals do.

S does not include random innovations belonging to the channel itself: otherwise even ordinary noisy channels would become deterministic after conditioning on their full future noise seed. S does include all pre-channel statistical/protocol information. Including decoder coins is intentional; a weaker assumption that omits them would not justify the loss-weighted conditioning argument in §5. Kernels are allowed to inspect S in this conservative upper model; this is a larger channel class than one observing only transmitted inputs. Neither the statistical attack nor the encoder gains this access. Lower bounds use fixed state-independent memoryless kernels, so potential leakage by some other channel cannot defeat robust lower bounds.

Define the robust factor by infimizing over one protocol AFTER taking the joint supremum over statistical instances and all such kernel strategies. A strategy is specified as a function on all states/histories, not chosen retroactively after outputs. Fixed memoryless W∈Uα is a subclass. Independent free coins remain independent of the source; arbitrary path-dependent free seeds are excluded. No assertion is made for feedback encoders, even though some upper estimates would tolerate them.

## 3. Exact imported interfaces and lower inheritance

The following accepted interfaces are imported, not rederived statistical theorems:

* BCC001/FOT002, WMC001, O2T001: for M≥64, exact-gate/exact-payload risk ≤G_j g_M(k), baseline factor c_j L≤Γ0,j(M)≤C_j L, with

      G_F=1024+2^20, c_F=2^−33, C_F=2^17;
      G_O2=2^17+2^23, c_O2=2^−30, C_O2=2^20.

  Stronger exact risks are 1024/√M+2^20 k/M and 2^17/√M+2^23 k/M. The accepted full-history normalized floor is 1/96. For whole-message transmission each exact predictor has a paid payload B=2ceil(log2(M+1))+2, described in §7.
* CAF001 §§3 and 7: finite memoryless arbitrary-code supplemental lower bounds imply, uniformly on each fixed α≤αmax<d/2, the necessary orders 1+T, ln L+T, ln M in the respective support classes. Its positive-radius witness gives, with s=|Y| and A_s=max{1,ln(2s)},

      R>ln M/[8 A_s(1+ln(1/α))]

  whenever M+1≥2^160 and 2^−32 ln(M+1)>B_target. Additional nominal common-component or equal-support likelihood lower bounds supply the respective baseline terms. This use imports its finite source-mixture proof through BSC001; it does not reapply a product-channel argument to an adaptive channel.
* CMF001 §§5,8: in d/4≤α<d/2 a feasible supplemental target B_target requires

      R>d² ln(M+1)/(256γ²)

  once M+1≥2^160 and 2^−33 ln(M+1)>B_target. Its whole-message grid/capacity lower gives Ω(ln M/γ²), uniformly over all α<d/2. Together with CAF001 the accepted CMF001 theorem gives the complete necessary H/γ² and ln M/γ² orders with a uniform threshold. Its chi-square/finite-mixture and capacity arguments are used ONLY at its admissible memoryless witness, not asserted for arbitrary kernels.
* UWC001 §§4–5: a deterministic greedy inner code of ell=12k_c bits, size 2^k_c, minimum distance ≥3k_c exists; an explicit Reed–Solomon evaluation code over F_(2^k_c) of length 4K and dimension K with its fully defined Welch–Berlekamp/fallback decoder corrects every pattern of ≤K inner-symbol errors. Construction correctness, field existence and bit-cost ledger are imported deterministic algebraic facts. Below all channel-error estimates formerly using independence are reproved.

Why the lower inheritance is valid: fix any protocol for the larger conditional class. Its worst risk is at least its worst risk on the original memoryless subclass. Accepted lower statements apply to EVERY such fixed-length nonfeedback protocol and its independent coins, not merely to an optimizer or repeated-gate code. Infimizing preserves them. There is no minimax interchange. The full-history floor similarly holds for robust risk by restricting to the nominal memoryless channel; it need not hold for every S-dependent channel separately.

At α≥d/2 choose the memoryless identical-row midpoint μ=(P0+P1)/2. It satisfies (C), and its transcript can be simulated by a baseline-only decoder. This gives robust supplemental factor ≥Γ0,j; ignoring the channel gives the reverse inequality, including nonattained infima by approximation. In the whole-message model the same witness makes the receiver independent of clean IID p∈[1/4,3/4], whose uniform-prior absolute-loss minimum is 1/8. All these IID sources satisfy the O2 all-state certificate. This proves the impossibility claims.

## 4. Conditional concentration and subset products

Write F_i=σ(S,Y_1,...,Y_i). All statements also hold conditional on an arbitrary deterministic block-start F_a. No independence is required.

**Lemma 1 (conditional Hoeffding).** If Z_i∈{0,1} is F_i-measurable and E[Z_i|F_(i−1)]≤u, then for ε>0

    Pr(Σ_(i=1)^n Z_i≥n(u+ε) | F_0)≤exp(−2nε²).

If conditional means are ≥u, the corresponding lower-tail bound at n(u−ε) holds. Bounds remain valid when a threshold is outside [0,n], by triviality.

Proof. For a Bernoulli variable of mean m, the centered log mgf has value and derivative zero at zero and second derivative equal to a tilted Bernoulli variance ≤1/4. Integrating twice gives log E exp(t(Z−m))≤t²/8 for every real t. Conditionally, for t≥0 and m_i≤u,

    E[exp(t(Z_i−u))|F_(i−1)]≤exp(t²/8).

Iterate the tower property, obtaining E[exp(tΣ(Z_i−u))|F_0]≤exp(nt²/8). Markov and t=4ε give the upper bound. For means ≥u use t≤0 and t=−4ε. This proof covers adapted, nonidentically distributed indicators and closed tail events.

**Lemma 2 (subset errors).** If E_i∈{0,1} is adapted and Pr(E_i=1|F_(i−1))≤q, then for any deterministic index subset J,

    Pr(E_i=1 for every i∈J | F_0)≤q^|J|.

Proof: integrate the largest index in J; all earlier factors are measurable at its previous filtration. Iterate, including gaps. Thus Pr(Σ E_i≥r | F_0)≤binom(n,r)q^r for integer 1≤r≤n. The same result holds for deterministic consecutive blocks when each block's conditional error given its start is ≤q: use the block-end filtration.

**Lemma 3 (conditional Chernoff count).** Under the same hypothesis, for t≥0,

    E exp(tΣE_i)|F_0 ≤(1+q(e^t−1))^n
                          ≤exp[nq(e^t−1)].

This follows by iterated conditional mgfs. For real r>q>0,

    Pr(ΣE_i≥rn|F_0)≤(eq/r)^(rn).

Use t=ln(r/q); discarding the negative −nq term only weakens the bound. The real threshold is legitimate even when rn is not an integer.

**Nominal event primitive.** Set A={y:P1(y)>P0(y)}, p_b=P_b(A), τ=(p0+p1)/2. Then p1−p0=d. Under (C), at every history and for b=0,1,

    K_i(A|S,Y_<i,0)≤τ−γ,
    K_i(A|S,Y_<i,1)≥τ+γ.

Repeat a fixed bit b for m slots and decide 1 iff its event count ≥mτ. Lemma 1 at block start gives each conditional bit error ≤exp(−2mγ²). Ties belong to the bit-0 upper-tail event; bit-1 error is contained in the closed lower tail. This remains valid after conditioning on S and ALL earlier blocks.

For supplemental repetition, coupling exact and decoded predictors gives

    Γ≤G_j+√M exp(−2Rγ²).

Thus R=ceil(ln M/(4γ²)) attains G_j+1 for M≥64.

## 5. CAF support-aware upper without independence or slot symmetry

Fix αmax<d/2 and use γ0=d/2−αmax for a fallback length R_H=max{1,ceil(ln M/(4γ0²))}. The primitive of §4 applies uniformly to α≤αmax.

### 5.1 Disjoint nominal supports

Decode a single output as 1 on S1=supp(P1), and as 0 otherwise. Every tentative bit has conditional error ≤α for either input. This includes outputs nominally null under both rows. For α=0 one use is exact. For 0<α≤1/16 majority error over R repeated bits requires ≥ceil(R/2) errors; Lemma 2 gives

    Pr(error|S)≤2^R α^(R/2)≤α^(R/4).

With R=max{1,ceil(2ln M/ln(1/α))}, this is ≤M^−1/2, giving factor G_j+1 and length O(1+T). Above 1/16 use R_H; there 1+ln(1/α)≤1+ln16, so R_H=O(T). Empty branches require no action.

### 5.2 Unequal overlapping supports: adaptive two-slot probabilities

After swapping physical input labels if necessary, let E=S1\S0 be nonempty and p=P1(E)∈(0,1). Set a_P=(p/24)^2. For α≤a_P each physical input-0 slot has conditional E probability ≤α, and each input-1 slot has conditional E probability ≥p−α.

Encode semantic gate 0 by physical (0,1), and semantic gate 1 by (1,0). Exactly one E hit decodes according to the designated input-1 slot; neither OR both hits erase. In each two-slot block let C,W,N denote correct, wrong, nonerased indicators. Condition on S and all outputs before the block, denoted B.

Call the event at the input-1 slot V, and the event at the input-0 slot U. Towering the one-use inequalities, regardless of which slot comes first, gives

    Pr(V|B)≥p−α, Pr(U|B)≤α.

Correct is V∩U^c, wrong is U∩V^c, hence

    Pr(C=1|B)≥p−2α≥p/2,
    Pr(W=1|B)≤α,
    Pr(N=1|B)≥p/2.                                 (2S)

Here a_P≤p/4. These are conditional inequalities only. We do NOT assert identical ternary laws for the two gate values, independence of slots, independence of successive blocks, or the memoryless formulas q1(1−q0),q0(1−q1). An adaptive second slot can break all these equalities; (2S) survives.

Send n such blocks, with fixed length 2n. Let H be total nonerased blocks. If H<pn/4, abstain and use the accepted baseline predictor. Otherwise majority-decode the H tentative gates and use the exact-gate rule with that gate; ties have any fixed semantic convention. Noninteger thresholds are literal.

Lemma 1 for N at the BLOCK filtration yields, conditional on S,

    Pr(abstain|S)≤exp(−np²/8).                      (A)

On a wrong nonabstained decision the total wrong blocks Z satisfies Z≥H/2≥pn/8. Lemma 3 with r=p/8 and q=α yields for 0<α≤a_P<r,

    Pr(wrong and nonabstained|S)
      ≤(8eα/p)^(pn/8)≤α^(pn/16),                  (W)

because e<3 and α≤(p/24)^2 imply 8eα/p≤√α. At α=0 every wrong-block event has probability zero, hence (W)'s event has probability zero; no logarithm at zero is used.

Let ell_exact and ell_base be the potential TV losses, fixed by S. Pathwise

    ell_actual≤ell_exact+1_abstain ell_base
                              +1_wrong,nonabstained.

Taking conditional expectations using (A),(W), then averaging over S, gives

    risk≤risk_exact+exp(−np²/8) risk_base+α^(pn/16),
    Γ≤G_j+C_j L exp(−np²/8)+√M α^(pn/16).           (R)

Omit the last term at α=0. No independence between abstention and source loss is assumed: the UNIFORM conditional bound is what permits the baseline-loss factor.

Choose

    n=max{1,ceil((8/p²)ln(C_j L)),
                  ceil((8/p)ln M/ln(1/α))},         (N)

omitting the third entry at α=0. The last two contributions in (R) are each ≤1, so factor ≤G_j+2. This length is O(ln L+T), uniformly on [0,a_P]. On a_P<α≤αmax use R_H; the denominator of T is bounded above by 1+ln(1/a_P). Equal nominal supports use R_H directly. These are exactly the CAF orders with constants independent of α schedules. The concentration proof, rather than an equality of semantic ternary laws, is the new ingredient.

## 6. Uniform approach to the identifiability boundary

For α≤d/4 apply §5 with FIXED αmax=d/4. Since γ∈[d/4,d/2], multiplication by γ^−2 changes lengths only by fixed nominal constants. For d/4≤α<d/2 use §4 repetition with actual γ. In that range 1+ln(1/α) lies between the fixed positive constants 1+ln(2/d) and 1+ln(4/d), so H is uniformly comparable to ln M for M≥64. This supplies O(H/γ²). Imported CMF001 memoryless lower bounds from §3 give the reverse order with the SAME α-independent threshold convention. At α=0 all conditional kernels have nominal rows exactly, so the old support cases are recovered. No fixed-radius asymptotic is substituted for a uniform finite implication.

## 7. UWC concatenation with conditional subset bounds

Fix a B-bit payload, B≥1. Use the deterministic construction imported from UWC001 with

    m0=ceil(4/γ²), k_c=ceil(log2(8B)), q=2^k_c,
    K=ceil(B/k_c), n=4K, ell=12k_c.

Send each inner-code bit through m0 repeated physical slots. Section 4 gives hard-bit error ≤e^−8<2^−8=:p* conditional on S and the entire transcript BEFORE that hard-bit block. Thus the hard-bit errors need not be independent, but Lemma 2 applies to every deterministic subset of hard-bit blocks.

For an inner codeword c and competitor c' at distance s≥ell/4, nearest-Hamming decoding can prefer c' only if at least ceil(s/2) of their s disagreement coordinates are wrong. Agreeing coordinates cancel exactly in the distance comparison, including odd s and adverse ties. Conditional on the inner-block start, Lemma 2 gives probability ≤2^s(p*)^(s/2)=8^−s. A union bound over at most q competitors yields

    Pr(inner error | S, all prior physical outputs)≤q8^(−ell/4)
                                                        =2^(−8k_c)=:p.

This is uniform in every transmitted label and history. The transmitted inner codeword is fixed given S; it does not adapt to prior outputs. At the next layer use the filtration at inner-block ends. The deterministic outer decoder corrects ≤K errors, so Lemma 2 at this layer gives

    Pr(payload error|S)≤binom(4K,K+1)p^(K+1)
       ≤2^(4K−8k_c(K+1))≤2^(−6k_cK−8k_c)≤2^(−6B).

Here k_c≥3, 4K≤2k_cK, and k_cK≥B. Every step holds at B=1; fallback behavior and padding verification are those of the accepted fully defined deterministic decoder. No product law of hard decisions or inner errors is asserted.

The length is R=m0 n ell=48m0Kk_c≤240m0B, using Kk_c≤B+k_c and k_c≤4B. Codes, decoder and their algebraic correctness are unchanged; only the stochastic proof is replaced.

For prediction use B=2ceil(log2(M+1))+2. F's payload is (J,C_flip,t,G): departure/flip counts in the final-symbol row on suffix departures 1,...,M, final bit t=Z_(M+1), and repaired gate 1{512A_t≥J_t}. Decode flip probability C_flip/J when J>0 and gate accepts, else zero; rejection predicts t. O2's payload is (J,C,direction,G): selected terminal-pair departure count, directed transition count toward 1−Z_M, direction=1−Z_M, and original O2 half gate. Both protected symbols select that row at the encoder; the paid direction determines next-symbol output at the receiver even on rejection. No query bit is free. Each count uses ceil(log2(M+1)) bits. Validate 0≤C≤J≤M; invalid payloads receive a fixed distribution.

Successful payload decoding reproduces the respective accepted exact predictor, hence risk≤G_j g_M(k)+2^−6B≤(G_j+1)g_M(k). Since γ≤1/2, m0≤(4+1/4)/γ², so length is O(ln M/γ²) with no γ-dependent horizon threshold. Imported CMF lower completes the whole-message order.

## 8. Why unconditional row marginals are insufficient

Take nominal identity P_b=δ_b and any fixed integer R≥1. For α∈[0,1/2], define one channel kernel on WHOLE input words h∈{0,1}^R:

    with probability 1−2α, output h exactly;
    with probability 2α, output V uniform on {0,1}^R,
                          independent of h and of all pre-channel variables.

The replacement decision is one shared Bernoulli variable. The uniform string uses independent fair coordinates. For every h, coordinate i has probability α of differing from h_i, so

    Law(Y_i|S)=BSC(α)(·|h_i(S)),
    TV(Law(Y_i|S),δ_(h_i))=α.

This is stronger than a row-marginal guarantee averaged over the source: it holds for every deterministic full input word and complete pre-channel state. It is a nonanticipating latent-mode mechanism with no encoder feedback. But it fails (C). For R≥2, after observing Y1≠h1 the replacement mode is certain; the next coordinate's conditional error is 1/2, larger than α when 0<α<1/2. That history has probability α. Thus conditioning on past outputs, in addition to S, is substantive.

### 8.1 Arbitrary message codes

Let message J be uniform on N≥2 possibilities, independent public seed U be allowed, and let an arbitrary nonfeedback randomized encoder choose H^R. Conditional on the replacement mode, the complete receiver transcript (U,Y^R,independent decoder coins) is independent of J. Therefore its probability of correct decoding in that mode is exactly 1/N for any decoder that always returns a message, and at most 1/N if abstention is allowed. Averaging gives

    Pr(decoding error)≥2α(1−1/N).

The same lower bounds maximum error by averaging. It holds for every R, every codebook, encoder randomization, interleaving, pilots and deterministic padded prefix. Public seeds are not allowed to depend on J. A zero-length protocol already has error ≥1−1/N, so the bound also holds there.

### 8.2 Whole-message prediction

Choose clean stationary IID Bernoulli sources p=0 and p=1 with equal prior. They lie in F. They also lie in O2: from every initial pair, an IID transition table reaches the deterministic stationary pair in two steps, so P²(u,v)=Π(v) for all u,v. Use their stationary starts and no source attack. Targets are constant 0 and 1. In the replacement mode the decoder's prediction a∈[0,1] is independent of which source was selected; average absolute loss is (|a|+|1−a|)/2=1/2. The ordinary mode has nonnegative loss. Thus prior average clean risk≥α, so for every protocol one of these two clean sources has risk≥α and

    Γ_marginal,total,j(M,R)≥α√M.

This rules out bounded adaptation at any fixed α>0, regardless of the length schedule. For α depending on M it proves the necessary condition α=O(M^−1/2), not sufficiency. A decoder may partly detect replacement from pilots; even revealing the replacement indicator does not reveal the erased message, so the bound persists.

### 8.3 Supplemental prediction

In the replacement mode the baseline remains visible. For each candidate protocol define a baseline-only decoder D0 that samples an independent uniform R-bit string and executes that protocol's decoder, using the same admissible public/private seed distributions. For EVERY source/attack instance i, nonnegative loss gives

    risk_i(protocol)≥2α risk_i(D0).

Divide by its own g_M(k_i), take the joint statistical supremum, then infimize over protocols:

    Γ_marginal,sup,j(M,R)≥2α Γ0,j(M)≥2α c_j L.

This is a factor bound over the original same-procedure source/attack supremum, not a clean-risk lower for supplemental prediction. The baseline can contain information about the target, so claiming clean risk≥α here would be unjustified. For fixed α>0 the factor still diverges for every length schedule.

### 8.4 Not the correctable global-flip example

A different correlated channel chooses one Bernoulli(α) bit F and outputs Y_i=H_i XOR F for every i. Its coordinate marginals are also BSC(α), but one known pilot input reveals F exactly and lets the receiver invert every remaining output. This cannot prove an all-code impossibility. In the replacement channel, the common transcript component is independent of the message even after arbitrary pilots; knowing the mode cannot reconstruct the erased payload. The two examples must not be conflated.

### 8.5 General nominal channel: no positive fixed marginal tolerance suffices

The phenomenon is not specific to identity rows. For ANY nominal finite-output binary channel, choose a fixed output law ν independent of the input (for example uniform on the stipulated alphabet), set η=min{α,1}, and use one shared mode: with probability 1−η run the nominal memoryless channel on the entire word; with probability η output an IID ν string independent of the entire pre-channel state. Every coordinate, conditional on each complete pre-channel state and fixed input word, has row (1−η)P_b+ην, whose TV distance to P_b is η TV(ν,P_b)≤η≤α. Its full transcript has an input-independent component of mass η.

The identical arguments give average N-message error ≥η(1−1/N), supplemental robust factor ≥η Γ0,j(M), and whole-message clean worst risk ≥η/2 using IID p=0,1 (or ≥η/8 using the uniform prior on [1/4,3/4]). Thus ANY fixed positive marginal-only tolerance destroys bounded-factor adaptation in both receiver models, regardless of the nominal supports or length schedule. This is a robust impossibility for the enlarged marginal class, not an exact risk characterization or a claim about every marginally faithful channel. The identity example with mode mass 2α is the sharper illustrative specialization for α≤1/2; the general construction merely supplies η>0.

## 9. Resources, dependencies, and limits

All upper algorithms are exactly the accepted nonfeedback algorithms: one statistical scan, fixed repetitions/two-slot blocks, and for whole-message payloads the existing deterministic concatenated code. The adaptive channel strategy is an adversarial model, not a computation the encoder must simulate. Conditionality adds no endpoint computational work.

Statistical scans take O(M log M) conservative bit time and O(log M) auxiliary counters. Supplemental channel decoding uses O(log(R+1)) counters and O(R log(R+1)) naive bit operations, with nominal event membership charged. Whole-message coding retains UWC001's polynomial-in-B design, table, encoding/decoding and auxiliary space with universal polynomial powers; its inner table generation is O(B^13 log(B+1)), and m0-dependent physical reading/counting is additionally charged. Resident raw input adds M+2 bits. Uniform polylogarithmic resources as γ→0 are NOT claimed; R itself can grow arbitrarily fast. Reading arbitrarily long rational α descriptions has separate cost. Rational nominal rows/radius admit exact event/comparison arithmetic and conservative integer length choices; arbitrary real inputs require an appropriate representation for effective computation.

Method attribution: the existing stage literature note `../channel_uncertainty_stage_20261103/METHOD_ANTECEDENTS.md` records a direct reading of Saha and Ramdas, *Robust likelihood ratio tests for composite nulls and alternatives*, arXiv:2408.14015v1 (2024), §2.1/Theorem 2.1, for supermartingales under conditional TV-neighborhood uncertainty. That source note, not a new primary-source reading in this unit, is the provenance of this attribution. Conditional bounded-mgf concentration and chronological subset bounds are established elementary methods. This unit's contribution is their rigorously scoped composition with the accepted prediction interfaces, preserving these particular sharp frontiers, plus the all-code marginal-fidelity obstruction. No claim that conditional-TV testing or the underlying coding methods are new is made.

Direct accepted sources: CMF001, CAF001, UMC001, UWC001 with ROOT_ACCEPTANCE receipts; their original statistical interfaces were checked in O2T001, WMC001, BCC001 and BSC001 model sections and receipts. Their statistical/combinatorial proofs, including FOT002 and the positional-manuscript finite-upper theorem, remain explicitly imported, not independently rederived. SOURCE_BINDINGS.json verifies candidate hashes against receipts and records exact dependency files. This is proof composition plus new conditional-probability arguments, not formal verification, external peer review or novelty certification.

`checks.py` provides exact finite tree recursions for adaptive two-slot extremizers, adaptive subset-error bounds and global replacement marginals/common-component code errors, plus concatenation arithmetic and dependency hash checks. Finite checks corroborate but do not prove universal results. They do not implement the full concatenated encoder or benchmark it.

Excluded: feedback encoders, stopping/variable length, future-looking adversaries, marginal-only fidelity guarantees as a sufficient hypothesis, sample-dependent free side channels, calibration sample complexity, unknown nominal/alphabet, infinite alphabet, unrestricted/no-mixing O2 or all certificates/general source order, next-pair O2 targets, neural implementation/learning, optimal constants and new general coding theory. Review and root disposition remain required. No accepted files, external repositories, permissions, licenses or deployments were changed.
