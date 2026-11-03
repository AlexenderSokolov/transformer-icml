# Additive reconciliation: BCJ001 already established the finite-bank precision phenomenon

2026-11-03 UTC. This is an explicit retrospective clarification of internal antecedents. It preserves the original proofs, their acceptance chronology and the external-literature audit. It is not a new acceptance, a retraction of valid interface statements, or a novelty certification. No external writes were performed by this audit.

## Finding

**BCJ001, accepted on 2026-11-02, already proves the central approximate-half-gate and twelve-coordinate finite-bank precision/noise/source-edit result.** The newer ACG001/FPA001/PBP001 sequence must not be described as an independent new precision phenomenon or first connection between approximate positional statistics and budget-blind robust prediction.

The external-literature report did not inspect BCJ001 in its initial scope. Its statement that no inspected external source subsumed the exact new observation remains a narrowly scoped literature finding, but cannot support internal novelty. This omission materially changes contribution framing. The useful newer work is interface-specific rederivation/verification, an alternative lower-bound argument for a changed quantizer/bank, and an explicit local attention/Boolean-ReLU realization with separately stated hybrid shape.

## Exact antecedent and acceptance

Read in full: recovered `balanced_joint_finite_cut/BCJ001_theorem.md`, `BCJ001_independent_full_review.md`, and `intake/BCJ001_root_acceptance.json`, together with accepted bindings. Re-read the new FPA acceptance and review and compared current ACG/PBP/FPA statements. The recovered base is `resumption_20261103/remote_recovery/files/v10_research/`.

BCJ theorem SHA256 is `95d5aac1ee2504955e55c1e82241c8a07d219661e2620c6e083acf5c8701554d`, exactly matching the acceptance receipt and accepted bindings. Receipt SHA256 is `27c1aa7efdc86752c63fd0b1f41b9c303a2aedff965ce81721f3abca7c54699f`, also matching accepted bindings. It records `ROOT_ACCEPTED_AFTER_INDEPENDENT_LLM_REVIEW` at `2026-11-02T14:31:28.560722+00:00`. The theorem's older candidate header is historical, not its current admission status.

**Verified original/export mapping, not an unexplained discrepancy.** The recovered review is the published export with SHA256 `1e74c502da8fcda31603fc7fc2fa1229747521c3774da55aaf21c8a29a14f64b`, explicitly mapped from historical review `9cce8092070916078baa9b1cb82dcc9a9d6872b0013568996e4310a9f4c413ef`. The recovered handoff is `863ee4947f74bcbdb7dc725cd8fddab7c3e3643f992dace21d1d565b7daed2d1`, explicitly mapped from `8b3d2724fcb1cbc93c2833d3de8c222ff3dbec82cde218df26a3a8facde855e0`. The accepted-bindings export itself is `7cb57c460d7398364c5c85152e2ae5dda199db18c0d3a0a45c871eaed76ecf6b`, mapped from `034a36cd1d9895bcf411fc7036493546d1eec469970c586f4d56871e6b81bbe9`.

These exact path/hash pairs were independently checked against recovered `provenance/increment3/BINDING_RECONCILIATION.json` (SHA256 `2b8556353c52bfe82697aeeb4b636f79bb103406b54d9dc95ced91dea90918c4`) and the relevant entries and replacement-line records in `SOURCE_MAP.json` (SHA256 `2a4c4ab88fc0a4bde28b85b3e947a722f1d288dea8d8f2d1a5737f32b1943082`). The map declares administrative/publication-report edits and reviewer-attribution normalization, not theorem changes. All eight other artifact references in the accepted bindings, including the theorem and root receipt, match their original hashes directly. Thus we verified the published export pairs, **not restoration of the original review/handoff bytes**, and did not alter any historical expected hash.

## What BCJ001 already contains

- **§1:** Same homogeneous binary order-two actual-terminal next-symbol TV setting, protected terminal pair, source-independent bounded edits, one budget-blind decoder. It gives stationary and arbitrary-start upper bounds and matching fixed-prefix rates on every fixed band `beta >= c/M`, including the newer critical `beta=1/M` case. Its decoder ignores k, delta and beta.
- **§2:** Twelve paid coordinates: eight full triple frequencies and four first-half row subfrequencies, all normalized by M. Public half-position flags, zero-score uniform attention, endpoint acquisition, masks and access isolation are explicitly present.
- **§3:** Real-valued approximate pseudo-count gate with threshold 512, clean balance thresholds 256/1024, the large/small denominator split, false acceptance implying `J<1026d`, false rejection implying `J<513d`, and no exact gate-bit recovery or cross-bank realizability requirement.
- **§4:** Fractional thresholds are already handled using integer ceilings. The coefficient `8*130944 + 16*1539 = 1072176` is exactly the later ACG coefficient. BCJ pays a looser additive ceiling remainder, not an invalid integer-only shortcut.
- **§§5–6:** Complete-bank IID Bernoulli precision floor of order `1/Q`, statistical `M^-1/2` floor, a source-independent port-coarsening noise lower, and a full-history source-edit lower. The total fixed-prefix rate is `Theta_c(min(1,max(M^-1/2,k/M,delta,1/Q)))`. It expressly excludes optimized encoders.
- **§7:** A full finite sequential evaluator, all-token costs, masks/positions/input/working-word accounting, precise cut isolation and optional PURE unrolling. Fractional bank precision is already distinguished from full arithmetic word width. Optional final probability rounding is explicitly contemplated.

Therefore `h ≈ (log2 M)/2` to balance normalized quantization and statistical error is already an immediate consequence of accepted BCJ at the critical certificate. Noise robustness and unknown-budget adaptation were also already established there, in its own declared port model.

## Exact changes, not merely renamed claims

### ACG001 versus BCJ §§3–4

ACG exposes a standalone interface for independently approximate direct J,C,D statistics and uses sequential clipping to keep `0<=C,D<=J<=M`. BCJ reconstructs J as the sum of two nonnegative successor rails, automatically obtaining `C<=J`, and does not need to clip its half count or total pseudo-count. ACG permits arbitrary real error radius e and explicitly allows separate final output error xi. BCJ's proof already works with real d and arbitrary dependence of errors, and its optional output rounding covers the basic output-error step.

The new clipping lemma and modular direct-count statement are legitimate changes. However, the main real-error gate proof, rare-row treatment, no-margin conclusion and rate order are rederivations of the accepted mechanism. The modest ceiling/constant refinements are not a new precision principle.

### PBP001 versus BCJ §5

PBP fixes nearest-rounded direct J/C/D rails with exact endpoint; BCJ fixes floored eight-triple/four-half rails. Before quantization the representations are linearly interconvertible: J is a sum of successor counts and the non-designated successor is J-C. **After separate rounding they are not automatically the same experiment**, so a lower cannot simply be transferred by counting twelve labels or asserting exact equivalence.

BCJ already proves a full twelve-port `1/Q` lower by concentration near a one-dimensional mean curve, an O(Q)-sized good-message set, and prior covering. PBP instead constructs a shared rounding cell on a monotone parameter interval, uses bounded differences and couples the exact endpoint, then applies two-point testing. This is a different elementary proof route for a changed bank, covering h>=0 instead of BCJ's Q>=16. PBP's clean theorem is narrower than BCJ's joint noise/edit theorem. The extension to small h and the changed cut justify verification; they do not constitute discovery of the statistical/quantization transition.

### FPA001 versus BCJ §§2 and 7

BCJ already has a paid radius-three feature table, uniform zero-score attention, positional half-bank, finite evaluator and isolated readout. Thus FPA does not add the first attention-derived noisy positional bank. Its specific incremental implementation is:

1. Two paid singleton-copy attention heads explicitly acquire the lagged raw bits and terminal pair; tokenwise Boolean/ReLU gadgets form direct J/C/D features instead of relying on the finite radius-three local table interface.
2. A zero-score head averages those features with exact integer accumulation followed by one nearest rounding, avoiding BCJ's general positive-Taylor finite evaluator and nested floors.
3. A canonical **post-rounding** bank replacement has normalized error `2^(-h-1)+delta`; BCJ permits a **pre-final-floor** additive analog attack after an internal P-grid floor, giving its different error accounting. Neither port theorem automatically includes the other, especially for lower-bound coarsening attacks.
4. Exact bit circuits, restoring division, scalar-grid-to-bit extraction and a separately charged dyadic output provide a concrete Boolean/ReLU suffix. FPA specifies two attention layers/three heads, max value width 12, shared pointwise depth O(p²) and width O(p), with p including address and output precision.

**Hybrid-shape assessment:** yes, the inspected FPA statement supplies a more explicit, small hybrid neural-shape construction than BCJ §7, which explicitly disclaims fixed neural depth and gives only a finite sequential schedule plus optional full unrolling. This is additional implementation detail at a different realization, not an architecture-wide separation. FPA's pointwise depth still grows with precision/horizon, and attention's integer evaluator work is charged outside the small hybrid depth. Its PURE form is still the much larger generic unrolling. Sparse active masks change the work profile relative to BCJ's dense causal-prefix execution; comparing their runtimes as an intrinsic Transformer speedup would conflate implementations and allowed masks. The ordinary same-information counter remains the stronger computational baseline.

## Required contribution framing

Safe: “Building on the accepted BCJ finite noisy positional-bank result, we rederive a direct J/C/D approximation interface, calibrate its nearest-rounded fixed bank using an alternative lower proof, and give an explicit paid singleton-mask attention/Boolean-ReLU realization.”

Unsafe: “We newly discover that approximate positional statistics suffice,” “the first twelve-coordinate finite-precision frontier,” “a new half-log Transformer precision law,” or “a new robust attention principle.” The old theorem already establishes the central phenomenon, while the new half-log statement concerns a fixed normalized bank, not total network precision.

This clarification is additive. No candidate theorem, root receipt, original review or publication chronology is silently rewritten. The four-unit stage was reported as already published at commit prefix `670b7fc`; this audit did not independently inspect that remote commit and makes no external repository change. The reconciliation should accompany later contribution summaries and any explicit published clarification.

## Current-unit bindings

- ACG candidate: `66ca3f2c092eeceb78cdafab97854580df329b28dd5b4d3bb34c28bb5a44d4ed`; root receipt: `b6a2e5bb2438987a0d3b47f59cde37e8870254d27d74cc052c010a9f130c34c8`.
- PBP candidate: `0a74d5e9eab9b276bc3cebe656815483d1dc22d49f138c48f310456003bcdbde`; root receipt: `7af436918247872a8e26372503005fd873b2e50171557002e8a0dde8fa3de4a1`.
- FPA candidate: `a4194b8e44eff0302d0678df0ed4cc9650a683164950f9fd87acf7e62bf1c6f9`; root receipt: `0d228c3fed6f2cd23c59270ba52731033467313ea03ea337785f395a01ae6773`.

All three candidate hashes were checked against their current root receipts. This reconciliation did not rerun historical diagnostic suites or independently verify all inherited statistical lemmas; its task is exact statement/proof-mechanism and acceptance-provenance comparison.
