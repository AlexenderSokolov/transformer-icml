# Return to the Transformer question: direction assessment

2026-11-03. Scientific assessment and proposed next theorem, not a new acceptance or novelty certification. No external writes. Source statements with historical candidate wording are read together with the current FACT_INDEX admissions and root receipts.

## Decision

After closing the already-running conditional-channel extension, stop extending the channel taxonomy and prove **an architecture-specific approximate-count half-gate theorem**. The question is whether a paid finite causal attention prefix can achieve unknown-edit-budget risk `O(M^(-1/2)+k/M+eta)` when its positional statistics have adversarial normalized error `eta`, without recovering exact integer counts or an exact gate bit.

This is one focused bridge: statistical robustness → actual attention-derived statistic ports → finite readout and full resource accounting. It can give a useful positive theorem even if no Transformer advantage survives the strong baseline. It does not promise training or architecture-wide optimality.

## Evidence-linked gap map

- The research goal is to determine when finite historical evidence remains usable in a real network, including depth, precision, and perturbations. Document counts do not establish this, and fixed-port necessity must not be extended to all networks.
- [SRC-Pi, S1–S5](../../v10_intake/source/sources/euler-stage6/facts/fef8372728290b45.md) already supplies bounded-score finite attention, a particular `9K+1` master bank, an all-path add-one approximation, and paid Boolean/ReLU readout. Its depth/width are `O(Kp²)/O(Kp)` in its batch-hybrid model, with full-token work and quadratic attention separately charged. It has neither a half-time statistic nor the new budget-blind gate. Its generic PURE simulation is available but explicitly more expensive; merely applying that universal simulation again would add little science.
- [Anchored direct construction](../../v10_intake/source/sources/euler-stage6/facts/8a4d1b9aef15dae8.md) already recovers exact counts using an anchor and sufficient internal precision. [Anchor precision threshold](../../v10_intake/source/sources/euler-stage6/facts/911384a1c6a812b0.md) concerns that fixed procedure, not all attention. A new exact-count gate circuit alone would mostly combine existing constructions.
- [034](../../v10_intake/source/sources/euler-stage6/facts/d3e63f7b5e389adf.md) and [035](../../v10_intake/source/sources/euler-stage6/facts/ed3adf29f858da12.md) close necessity at fixed SRC V/master cuts. They prohibit re-reading history and new statistics. A new positional statistic prefix changes the experiment and cannot be inserted into their lower bounds.
- The [finite positional manuscript](../resumption_20261103/recovered_science/positional_manuscript_finite_20261102/main.tex) proves a real information separation: counts plus short boundary windows have logarithmic budget-adaptation cost, whereas a computed positional gate removes it. This concerns allowed observations, not neural depth. The [first-order addendum](../resumption_20261103/recovered_science/richer_count_consolidation_20261102/main.tex) removes mixing only for first-order sources; it does not do so for general order two.
- [O2T001](../resumption_20261103/order_two_transfer/CANDIDATE.md) returns to binary order two under `P²(u,v) >= Pi(v)/M`, arbitrary initial pair law, protected endpoint, and actual-terminal next-symbol TV. Its encoder is an unrestricted scanner. Counts and endpoint are free in the supplemental model and paid through a message in the whole-message model. These are not the original neural ports.
- [Current channel synthesis](../channel_uncertainty_stage_20261103/RESEARCH_SUMMARY.zh.md) characterizes reliability/model-accuracy cost after that scanner. This genuinely answers when a computed informative statistic survives transmission. But neither channel uses nor codeword length is Transformer depth, and its finite-code algorithms are not attention implementations. Conditional-noise extension tests a meaningful assumption; further support/exponent refinements now have diminishing relevance to the mother question.
- [Streaming capped-table fact](../../v10_intake/source/sources/euler-stage6/facts/5110203ec700e7e1.md) is a strong clean-data resource baseline. It is not automatically robust to edits. For the present binary attacked task, O2T001's ordinary exact full/half counter scan is already a simpler robust baseline: `O(log M)` auxiliary bits and `O(M log M)` conservative bitwork. Do not advertise a quadratic batch-attention implementation as a computational improvement over it.

## Exact proposed experiment and interfaces

Retain the accepted binary order-two experiment: `M>=64`, clean `X_0,...,X_(M+1)`, `M` departures, unknown fixed homogeneous table, arbitrary initial pair law, all-state certificate `P²>=Pi/M`. A source-independent offline attack changes at most `k` of positions `0,...,M-1` pathwise and preserves the last two symbols. One predictor at each M serves every k. Target is `theta_(Y_M)` on the same trajectory, next **symbol**, unsquared expected TV.

Let the attacked word be Z. Define all eight normalized triple counts `c'_(u,a)=C'_(u,a)/M` and four first-half normalized row counts `d'_u=D'_u/M`, with half departures `0,...,floor(M/2)-1`. The new attention bank approximates these quantities; endpoint acquisition is exact and paid. No counts, original symbols, hidden table, clean bank, evaluator scratch, or extra history enter the downstream readout.

Require a **pathwise derived**, not postulated neural result: bank-coordinate error is at most `eta` after quantization and allowed numeric-port perturbation. Errors may depend on the attacked word and be mutually correlated. This is a different fault port from SRC's old master bank and from post-encoder bit-channel noise. Prove the bridge between physical head rounding/perturbation and eta explicitly. Do not attach the channel frontier to these ports without an additional construction.

Select actual row u and designated successor `1-u_first`. If both successor count coordinates have error eta, their sum has error at most `2 eta`; use common count-error budget `e=2M eta` conservatively, or supply a separately paid row-count coordinate to obtain `e=M eta`. Clip reconstructed `Jtilde` into `[0,M]`, and `Ctilde,Dtilde` into `[0,Jtilde]`. Relative to legal attacked `(J',C',D')`, this clipping does not increase the common absolute error e. Output `Ctilde/Jtilde` if `Jtilde>0` and `512 Dtilde>=Jtilde`, otherwise zero; assign the complementary symbol its complement. Final probability rounding contributes a separately charged `rho_out`.

The theorem should first prove the bank-interface risk, then produce one explicit finite network realizing the interface. It should not assume exact gate recovery or a positive margin around `512D'=J'`.

## Why this is viable: a specific missing proposition

The accepted [positive proof, pathwise gate reduction and half-gate upper bound](../resumption_20261103/recovered_science/positional_manuscript_finite_20261102/sections/proofs_positive.tex), lines 503–629, already has threshold slack 256/512/1024. Its reduction uses only absolute errors and legal probabilities. It never needs the perturbed triple `(J',C',D')` to be integer counts of a common path after the perturbation step.

Here is the concrete proposed extension to verify independently. Put `Delta=6k+e`. The same case analysis gives

`R <= E[1{J>0}|C/J-q|] + 8 Delta E[1{D>=J/1024}/(J+1)] + E[q 1{J>0,D<J/256}] + P(J<w1)+P(J<w2)`, where `w1=max(1,ceil(1026 Delta))` and `w2=max(1,ceil(513 Delta))`.

Details needing checking, rather than hiding behind gate continuity:

1. On accepted gate and clean balanced event, if `J>=2 Delta`, denominator comparison bounds the ratio difference by `8 Delta/(J+1)`. If `0<J<2 Delta`, the unit loss bound suffices (J remains an integer even when Delta is real).
2. False acceptance outside `D>=J/1024` implies `J<1026 Delta`; false rejection outside `D<J/256` implies `J<513 Delta`, including `Jtilde=0`. Equality in the gate is accepted. These are deterministic implications, not an assumption that the gate bit is stable.
3. The accepted occupation lemma bounds rare actual-terminal rows. The accepted half-count reciprocal estimate is `130944/M`, valid for any start. Thus rare rows are charged in expectation, not discarded or assumed to have mass bounded away from zero.
4. The coefficient of `Delta/M` is `8*130944+16*(1026+513)=1,072,176`. The original proof already absorbs the remaining `32/(M+1)` into its statistical term. For the original certificate the proposed result is therefore

`R <= min(1, 2^17/sqrt(M) + 1,072,176*(6k+e)/M + rho_out)`.

The displayed integer thresholds cover J=0 and both strict false-gate bounds and satisfy `w1+w2 <=1539 Delta+2`, giving precisely the retained `32/(M+1)` remainder. Using `J<1026 Delta+1` and silently treating its threshold as an integer would be incorrect. Conservative `O(M^-1/2+k/M+eta+rho_out)` is the scientific target; constants are not another research branch.

This calculation is a source-supported proposed proof, not an accepted new result. In particular, it is **not** a proof about a smooth differentiable gate, training, or noisy comparisons. It supports an exact finite comparison of approximate bank values. Arithmetic or comparator faults must be included in a separately proved error interface or excluded explicitly.

## Paid neural realization to investigate

Choose the same transparent model as SRC: finite causal attention plus shared tokenwise Boolean/ReLU circuits, explicit masks, full batch accounting, no oracle arithmetic. This is a concrete model version, not an off-the-shelf learned Transformer claim.

- Two paid local-copy heads obtain lagged symbols and preserve the endpoint at the synthetic query. The least-change version uses SRC's explicitly allowed singleton masks, whose generation and storage are charged. This is a structural mask permission, not content-based bounded-logit recovery. If one instead requires dense causal masks only, a new soft positional copying proof is needed; positional score magnitude/weights, precision, and saturation margins must be charged, and the resulting score cap need not remain bounded. Do not combine the cheap aspects of these two models.
- Shared local bit circuits form eight triple indicators and four row indicators multiplied by a public first-half position flag. This is fixed width for binary symbols; no query is broadcast to past tokens.
- One uniform attention head at the synthetic query averages these 12 feature rails over exactly the M legal departure keys. Its score is zero, so no large logits, anchor probability `1/M` inversion, or hard content matching is required. Other-token masks/fallbacks and all-token work must be specified.
- A finite exact accumulator followed by dyadic rounding yields bank error `2^-h`, then a declared numeric bank fault of size delta gives eta at most `2^-h+delta`. If full row counts are derived by summing two coordinates, keep the factor two noted above.
- Bit selection, clipping, rational division, comparison and final probability decode get an explicit finite circuit and resource ledger. The source-independent schedule, positions, masks, parameter bits, temporary registers, copying/holds/clearing, input storage, online/offline work and output are charged. Do not merely cite a sequential interpreter and report SRC's smaller hybrid depth.

This uniform-feature construction is a **strong direct baseline**, not a novel feature trick. Its value is to establish the new precision/robustness connection and expose whether the proposed mechanism adds anything beyond ordinary aggregation. A claimed bound such as `h >= 0.5 log2 M + O(1)` concerns **bank fractional precision** at statistical risk, not every arithmetic word: accumulators, indices and masks still require logarithmic horizon information. The original SRC's legal `h>=log M` is a different program domain and cannot simply be relaxed by substitution.

For a neural-only formulation, separately report literal finite arithmetic circuit costs, or the full conservative PURE expansion. Neither arbitrary encoder algorithms nor word-RAM counters imply efficient neural realizability; neither explicit neural construction implies gradient training will find it.

## Comparison, alternatives rejected, and stopping condition

Compare three transparent observations within the same attacked-source experiment:

1. Exact count-only/endpoint readout, even unlimited computation: the accepted logarithmic adaptation obstruction applies. Rounded count-only statistics cannot beat this stronger exact observation.
2. Paid count-plus-half-position attention bank: prove the proposed upper with finite precision and numeric port error. This is an observation/representation improvement, **not** an architecture-wide depth separation. A stronger comparator allowed the same positional features can match it.
3. Ordinary full/half streaming counter with the same input, endpoint and k-blindness: matches the statistical risk and has cheaper sequential work. Report that fact plainly. Match whether input is resident, read-once, or accessible by attention; do not compare auxiliary space to total batch memory.

Rejected as immediate next tasks: more channel constants (small mother-question gain), full-beta/all-K extension (important but does not repair the missing architecture connection), exact gate/whole-ECC generic compilation (largely standard composition), and an immediate training sweep (premature without a tested deterministic target and a precise failure mechanism). Generalized soft-gate trainability is a later question, not smuggled into this theorem.

Bounded work plan:

A. Prove/review the real-error gate reduction above, including zero visits, equality, clipping, fractional errors and actual-terminal occupation tails. If it fails, preserve the specific counterexample; do not rescue it by assuming a large gate margin.

B. Build and verify the uniform-feature attention program for all binary paths, using finite enumeration only to catch indexing/rounding bugs. Prove the all-path interface and complete resource bound; test synthetic examples with small visited-row counts and gate threshold crossings.

C. Integrate the established statistical theorem with the new program and the two strong baselines. Independent review should attack hidden count access, endpoint leakage, feature timing, whole-word costs, and distinction between bank and accumulator precision.

Stop this unit when the theorem plus explicit construction and honest comparison are established, or a concrete obstruction invalidates the proposed bank bound/realization. Do not manufacture a new tiny constants unit. Then decide whether empirical learning of this positional statistic is justified; if the result is only a standard composition, frame it as the necessary bridge and select the next genuinely unresolved architecture or learning question. Existing proofs alone do not establish priority or publishable novelty.
