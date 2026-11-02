# FN001 — first-orientation erasure in the specific FG001 encoder

2026-11-02. Candidate awaiting fresh independent review. This is a narrow IID robustness result, not a universal encoder lower bound, novelty claim, formal certification, or emitted-network audit. No frozen stage6/7 artifact is changed.

## Result and precise noise timing

Use exactly FG001's finite encoder: M=2^m generated IID Bernoulli(p) symbols, fixed common initial pair, Q=2^h (h>=1), J>=2, P>=max(m,Jh), D=2^P. Thus the finite mean U/D=floor(D A/M)/D is exactly x=A/M on every history. Let T(u)=2 min(u,1-u), F=T^h. The retained pre-cut rails are (x,F(x),...,F^(J-1)(x)). After the following ONE noise event, each is downward quantized at Q. Only these J labels, the specified exact side information below, and public source-independent metadata survive. Any estimator, including randomized estimators, is allowed after this cut.

The noise model is a common source-independent map on the FINITE PRE-QUANTIZATION rails, keeping them on G_P={0,1/D,...,1}, with coordinate l-infinity displacement <=delta on every input. It is not corruption of the already quantized G_h labels. Arithmetic before and after the one noise event is reliable. No history, count, unquantized rail, duplicate or timing side channel survives.

For 0<delta<=1/2 set epsilon=delta/2, p_±=1/2±epsilon. One legal common attack yields for every decoder

    max(risk(p_-),risk(p_+)) >= (delta/2) w_r [1-2 exp(-M delta²/2)]_+ .       (1)

Here the side-information contract is either:

* No history-dependent side label: r=0 and w_0=1.
* The actual terminal pair and any fixed-initial-pair flags: r=2 and w_2=p_+p_-=1/4-delta²/4, for M>=2. Public query/mode fields and deterministic functions of these retained bits may also survive.
* More generally, any functions of b fixed generated-symbol positions, plus fixed initial bits: choose an even r with b<=r<=M and pin r fixed positions to a balanced binary pattern; w_r=(p_+p_-)^(r/2). This extension requires enough positions and fixed-position side data, not an arbitrary finite-valued function of the whole history.

In particular, if M delta²>=2 log 4, the no-side lower is delta/4 and the terminal-pair lower is at least 3delta/64. The terminal target is p under each source regardless of endpoint; absolute error is Bernoulli TV error. The sources are admitted IID subfamily members under every beta of FG001's stationary-witness mixing class.

## Proof: exact rails, common attack, complete observations

Define a map a_delta on the first rail by a_delta(x)=1/2 if |x-1/2|<=delta, and a_delta(x)=x otherwise. Leave every other rail unchanged. This depends on x and public delta only, never on p or a future bit. It is legal globally, takes fine-grid values to fine-grid values because P>=1, and moves only one rail by at most delta. Even when delta is not dyadic the operation is a well-defined finite lookup; the explicitly executable dyadic examples below require only integer comparison. The adversary is not asserted to be a bounded-depth neural map.

First suppose r=0. Couple a history at p_+ with its generated-bit complement at p_- while holding the initial pair fixed. Then x'=1-x exactly. Since T(1-x)=T(x), F(1-x)=F(x), and every deeper retained rail agrees exactly. On E={|x-1/2|<=delta}, both first rails are replaced by 1/2. Consequently the complete quantized label vector is identical, including all possible endpoint labels. There is no orientation label hidden in the interface.

For the side extension, pin the r fixed generated positions to the SAME balanced pattern s under both sources; do not complement these positions. The probability of this event under each source is w_r. Complement all remaining M-r symbols. The pinned sum is r/2, so the two full counts sum to M and x'=1-x still holds. All retained side bits are identical. Initial bits are held fixed in both experiments and are not included in A. For the actual terminal pair take its common pattern to be 01. This restriction is a subprobability coupling in the unconditional risk experiment, NOT a claim about conditional-terminal risk.

Conditioned on the pinned pattern, A=r/2+B with B distributed Bin(M-r,p_+). Its mean divided by M is 1/2+epsilon(1-r/M), at distance at most epsilon from 1/2. For M>r, Hoeffding's inequality gives

    Pr(E^c | pinned) <= 2 exp[- M² delta²/(2(M-r))]
                      <= 2 exp[-M delta²/2].

For M=r the mean is 1/2 deterministically and Pr(E)=1. The looser displayed lower still holds.

The coupling therefore supplies identical FULL observations with mass at least w_r [1-2exp(-Mdelta²/2)]_+. At each matched observation use the same independent decoder seed. The triangle inequality gives |z-p_+|+|z-p_-|>=2epsilon. Integrating over this common subprobability mass and discarding nonnegative losses elsewhere gives sum of risks >=2epsilon times that mass, hence their maximum >=epsilon times that mass. This proves (1). Source-independent decoder randomness cannot restore the erased orientation.

For delta<=1/2, w_2>=3/16; the stated sample condition makes the bracket at least 1/2, giving 3delta/64. No assumption about the FG001 clean decoder is needed: this holds for the best decoder after the attacked specific encoder.

## Separation below half a coarse cell

Fix J>=2, choose Q=2^h tending to infinity, M=Q^4, P>=max(4h,Jh), and delta=1/(4Q). All values and the attack comparison are dyadic and exactly executable. Then delta<1/(2Q), yet Mdelta²=Q²/16 diverges. The terminal-side lower is Omega(Q^-1), whereas FG001's clean decoder upper is

    1/(2 sqrt(M))+2/Q^J <= (5/2) Q^-2.

Thus a perturbation smaller than half the coarse grid spacing can destroy the deeper clean packing gain in THIS pre-cut interface. The attack does not perturb later high-frequency rails at all: their exact reflection symmetry is the vulnerability.

No contradiction arises with PE1. PE1 corrupts a canonical G_h codeword AFTER encoding. At that interface, any delta<1/Q permits only the identity corruption; in particular the current delta=1/(4Q) cannot change a canonical coordinate. The present fine pre-cut state is G_P and is subsequently coarsened to G_h. Moving a fault boundary is a model change and must not be hidden.

## Failed hypotheses and limits preserved

1. Complementing every generated bit while retaining the exact terminal pair does NOT yield identical full observations. The balanced-pattern subprobability argument above is necessary; it costs w_2 and is explicitly included.
2. For arbitrary non-dyadic M or P<m, floor(D x)/D and floor(D(1-x))/D need not sum to 1. Exact folded equality cannot be asserted then. The theorem intentionally uses dyadic M and paid P>=m. No generic-rounding extension is claimed.
3. FG001 permits an arbitrary H-valued history-derived boundary label in its broad interface definition. Such a label can include an orientation bit, and is NOT covered merely because H is fixed. This theorem explicitly names its allowed side functions; it does not establish fragility for every boundary-label choice in FG001's interface class.
4. Finite post-coarse-grid corruption with delta<1/Q cannot realize this attack. A claim that this is the literal PE1 canonical channel would be false.
5. A clean first-rail orientation bit could defeat this particular reflection collision, but adding an exact bit changes the port. A protected or redesigned digital encoder may evade it. No theorem that bounded-depth guards fix all noise, no fixed-capacity impossibility, and no universal depth/robustness tradeoff is established.
6. This is a deterministic one-shot adversary, not random noise, training evidence, internal arithmetic noise, hardware robustness, or a full Markov minimax result.

## Source bounds and verification

Mathematical imports: accepted FG001 theorem Sections 1–5 and its independent review (specific encoder, finite exact tent implementation, clean risk); PE1 v3 Sections 2–3 and 8 (noise timing, canonical-grid model, exceptions). Proof of the new collision and bound is given in full here. Hoeffding is used only for independent bounded Bernoulli sums. No external source search or private-data upload is needed or performed. Source hashes are in FN001_source_bindings.json.

Finite exact diagnostics and independent adversarial review are separate evidence, not substitutes for the all-parameter proof. Resource statement is limited: the encoder is unchanged and its paid precision can grow to m; original FG001 ledger carries that P. The adversary is allowed an arbitrary common kernel, as in the declared fault model. No new implementation performance or minimum resource claim is made.

Attribution scope: the local prior-art audit `v10_research/prior_art/folded_capacity_comparison.md` records established geometric multi-coordinate scalar packing and Uss et al. (ICML 2025) Hilbert-curve constructions with their own noise assumptions. FN001 does not refute that different construction or its empirical results. No originality claim for packing, folding, or standard coupling/concentration techniques is made. That paper is not a mathematical dependency of FN001.
