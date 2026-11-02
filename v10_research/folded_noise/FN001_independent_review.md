# FN001 fresh independent adversarial review

2026-11-02. Reviewer is a separate same-model LLM reviewer, not the theorem author. This is separate execution with shared research context, not a blind review or an independent-model/formal certification. Reviewed the full FN001 statement/proof, FG001 encoder and exact evaluator Sections 1–5, and PE1 v3's canonical noise interface. No frozen artifact was changed, and no private source was sent externally.

## Verdict

**PASS for the specified FG001 finite encoder under the explicitly new fine-grid, pre-coarse-quantization fault model and named side-information contracts.** No mathematical blocker found. This is a research review, not formal verification, an emitted-network audit, or a universal robustness lower bound.

Reviewed theorem SHA256: `38d716cdd2703ac3f53338c71f77b86728bf39d25fdd389a81d06d7b975d8399`.

## Independent proof checks

1. **Exact finite symmetry:** M=2^m and P>=m imply D A/M is an integer. Thus the two finite initial means really sum to one, rather than merely approximating complementary ideal means. The fine tent update is integer-exact and satisfies T(D-U)=T(U). All later retained rails therefore coincide. P>=Jh retains FG001's evaluator requirements. Intermediate causal prefix means need not be dyadic-exact: only terminal symmetry is used; the architecture already independently pools at each row.
2. **Legal common fault:** The map resets the first fine rail to D/2 only within displacement delta, and is identity elsewhere. It is a single source-independent deterministic map, not a source-specific attack chosen after learning p. D/2 is on the declared fine grid, and every later rail is unchanged. Arbitrary real delta is harmless for the mathematical finite channel; the constructive separation uses explicit dyadic delta.
3. **Complete terminal side port:** Complementing all symbols would indeed change the terminal pair and fail. Instead the common event terminal pair 01 has probability p_+p_- under either law; complementing only the other M-2 generated bits keeps their conditional laws paired and makes total counts sum to M. Fixed initial bits/flags are identical. This is a valid common subprobability coupling of unconditional observations, not conditioning away a loss without paying its probability. For general even r the same reasoning yields weight (p_+p_-)^(r/2).
4. **Concentration:** Conditional on the balanced pinned event, E[x]=1/2+epsilon(1-r/M). Since its distance from 1/2 is at most delta/2, leaving the delta band requires a deviation at least delta/2 from that mean. Applying Hoeffding to M-r independent summands, scaled by M, gives 2 exp[-M² delta²/(2(M-r))], bounded above by 2 exp[-M delta²/2]. The M=r case is deterministic and separately covered.
5. **Risk conversion and constants:** Every matched full observation forces the two decoder losses to sum to at least p_+-p_-=delta. Integrating over common mass and dividing by two gives (delta/2) times the common mass. Sharing the decoder seed verifies randomized decoders too. At Mdelta²>=2log4 the concentration bracket is at least 1/2, and delta<=1/2 gives p_+p_->=3/16; hence terminal risk >=3delta/64. The source target remains p for every endpoint.
6. **Scale separation:** With M=Q^4, delta=1/(4Q), and fixed J>=2, the clean upper is <=(5/2)Q^-2 while attacked risk is Omega(Q^-1). Both the fine mean and gate are exact in the stated precision. This proves fragility of the specific encoder, not arbitrary encoders with the same output dimension.
7. **Channel distinction:** PE1's post-encoding G_h perturbation cannot change any coordinate when delta<1/Q. FN001 inserts the fault on G_P before the Q-grid quantizer. The theorem explicitly distinguishes the two and does not portray their difference as a contradiction. Likewise, arbitrary history-derived H-valued boundary labels are explicitly excluded; an exact orientation label could break this collision.

## Independent executable evidence

`FN001_independent_checks.py` independently constructs integer tent rails and exact rational observation laws, without importing author diagnostics or decoding code. Fresh run passed:

- 9,396 count/parameter collision and displacement cases, including endpoints and midpoint;
- 360 exact observation-law comparisons, with either no side label or ALL FOUR terminal-pair values retained in the observation alphabet;
- each exact full-law overlap dominates the proposed balanced-event coupled mass;
- supplemental numerical checks of the concentration inequality on this grid;
- preserved non-dyadic rounding failure M=3, P=2, A=1: complementary fine numerators are 1 and 2, not a pair summing to D=4.

Output is `FN001_independent_checks.json` and binds the theorem hash. These bounded computations corroborate but do not replace the symbolic argument.

## Scope cautions retained

No claim is made about arbitrary boundary functions, post-coarse-grid subcell perturbations, nondyadic sample-size exact symmetry, internal arithmetic faults, protected/redesigned encoders, depth necessity, or training/hardware behavior. Additional orientation guards might remove this particular collision but have not been proved sufficient against all legal attacks. No optional guard theorem should be inferred from this PASS.

Final delta check: the author added only an attribution-scope paragraph while review was running. It disclaims claims against a different Hilbert-curve construction and is not a mathematical dependency. The theorem was reread at that delta and independent diagnostics rerun against the final hash above; PASS is unchanged. No external bibliographic revalidation was performed by this reviewer.
