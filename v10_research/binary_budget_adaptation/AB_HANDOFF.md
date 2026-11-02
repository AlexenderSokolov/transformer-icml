# AB001–AB003 stable research handoff

2026-11-02. All three units are root accepted after fresh independent full LLM mathematical review; acceptance authority is the exact receipt in `../intake`, not the preserved candidate header. No external peer review, formal verification or novelty certification is claimed.

## Results

| Unit | Established result | Important boundary |
|---|---|---|
| AB001 | No single estimator blind to both k and beta attains the binary known-k profile for all budgets/classes, even stationary. Exact finite constrained-risk inequality. | Does not exclude unknown-k adaptation when beta is supplied. |
| AB002 | Ordinary selected-row add-one has a logarithmic excess at beta=1/M, even stationary, under an explicit strict-k source-independent kernel. | Refutes that estimator only. Includes the actual failed same-beta witness route. |
| AB003 | A hard designated-count threshold attains the profile, jointly blind, for k<=sqrt(M), all beta/all starts. Scaling by a fixed public envelope constant gives k=O(sqrt(M)). | With AB001, this is the sharp order boundary for uniform adaptation over 0<=k<=b_M. It is not a pointwise impossibility at every larger k. |

AB003's estimator uses B=12ceil(sqrt(M)): output C'/J' on the publicly oriented terminal row only when C'>B, otherwise designated probability zero. Its no-log threshold bias is proved by a separate fixed-q_u occupation bound for each of four states; no random-threshold substitution or terminal-conditioned IID assumption is used.

The unresolved full-history question is now precise: for supplied beta, can a single A_(M,beta) attain the profile for every k, uniformly in beta? `NEXT_PROBLEM.md` records the exact question and unproved directions. Continued work is isolated in the separate sibling directory `binary_beta_known_adaptation`; it is not part of these accepted units.

## Exact accepted versions

- AB001 proof SHA256 `865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d`; root receipt `intake/AB001_acceptance.json`, 2026-11-02 11:57:46 UTC.
- AB002 proof SHA256 `7848267fa73e33775ca2aa467230980ee5f89e1d5ae0ae140c0d7955909d219b`; root receipt `intake/AB002_acceptance.json`, same acceptance time.
- AB003 proof SHA256 `fe3260f31f76a99576897d931e23ab939e0ebf8eb04e8cf31591b2b908d392e8`; root receipt `intake/AB003_acceptance.json`, 2026-11-02 12:11:01 UTC.

The complete AB001/AB002 review is `review_joint_blindness_full.md`, hash `07050ce099a0e1770f0dd4b59c11911938e1bed798246c23256093d25f4629c5`. The complete AB003 review is `review_ab003_full.md`, hash `0d4ec9fb2f4672fc5b2c850b0e553caebd83871a8ec808931b75fa25193ada90`. Root independently read all three complete proofs and both complete reviews before accepting.

## Exact diagnostics

- Author AB001/AB002: 150 rational stationarity/certificate/acceptance cases and 74,640 full-word edit/count cases.
- Independent AB001/AB002: 270 rational alternative/weight cases, 270 exact acceptance DPs, 76,656 exact edited-word cases; minimum tested acceptance 9/16 versus proof's 1/4.
- Author AB003: 93,044 rational pathwise cases, 16,132 integer threshold checks, 4,033 exact squared finite-domain constant checks.
- Independent AB003: 26,292 relaxed count configurations, 88,156 critical-q checks, 61,864 floor checks, every M=64,...,100000 constant check, and scaled-envelope/§8 coefficient checks.

All are PASS on their stated instances. They corroborate, not replace, the universal proofs and dependency reviews. Scripts and JSON outputs are retained side by side.

## Provenance and preservation

`AB_SOURCE_BINDINGS.json` records exact imported sources, artifacts and root receipts. `build_bindings.py` rechecks proof/diagnostic/receipt bindings and rebuilds that inventory without manufacturing acceptance. Direct stochastic interfaces come from accepted SC003, BIF001 and BAI003 v2; BT002 supplies the known-k comparison lower. The original R011 chain remains explicitly transitive through the accepted SC003 interface.

The initial IDs BA001/BA002 collided with historical bounded-attention BA001. Root required renaming before acceptance. `draft_history` preserves the exact original drafts/diagnostics, and `DRAFT_RENAMING.md` records the ID-only change. The independent review checked that no mathematics changed. Accepted proof files were not rewritten after review or acceptance. The actual failed positive-beta construction, including the zero P²(01,10) obstruction and the repaired family's certificate limit, remains in AB002 §2.

No original manuscript, stage-eight freeze or older accepted result was overwritten.
