# Four-counter DP and fixed-gate pilot: archive and safe verification

This release retains all 54 extant noncache files, including the original C++ executable, source/settings, every saved case/proposal/witness/timing, retrospective RNG/oracle archives, original reports, additive corrections and both review sets. Three regenerable Python bytecode caches are excluded. **This is not a complete contemporaneous raw-sampling archive. Missing historical draws and DP states remain missing.** Read the [additional preservation audit](../../v10_research/exact_dp_pilot_20261103/review_independent/ADDITIONAL_PRESERVATION_AUDIT.md) before interpreting earlier reports.

## Safe default: no random generation or model initialization

From a trusted pinned checkout, with ordinary Python 3 and its standard library:

    python3 provenance/four_counter_and_gate_pilot_20261103/verify_public_archive.py

This new public verifier validates all selected bytes, original/public maps, all 65 historical binding occurrences and the exact existing pilot.py dependency. It then reads already-retained values and enumerates deterministic masks. It does not run the native executable, import the pilot or NumPy, instantiate any model, regenerate a seed, invoke a historical sampler, access the network, or overwrite the checkout. Optimized Python is refused because scientific assertions must remain enabled. Imported PRNG/model/process modules are blocked during its checks. Symlinked or altered sources/inventory paths are rejected. Identity checks assume a trusted pinned checkout, not a coordinated malicious rewrite of the entire checkout and inventory.

Checks performed:

- All 45 saved evaluations, all 900 saved proposal entries, protected-endpoint/edit-budget legality, gate/CE arithmetic, selections and post-selection source errors.
- All 448 retained small-test records and every one of the 5,976 retrospective oracle entries against deterministic mask enumeration.
- The 720 values already stored in randomness_replayed.json reconstruct the 12 saved words when interpreted using their stored tables and starts. No new PRNG values are drawn. This does not prove those values were the original draws, nor validate RNG-state evolution.
- The 32 retrospective test-state records are checked against saved words/budget blocks. Their PRNG evolution is not regenerated.
- The original sampling-free four_counter.py is used to compare all 3,056 reachable bank/minimum-cost maps and 27,576 witnesses through M=6 against literal enumeration. This is a new deterministic recheck, not a replay of the earlier randomly initialized Model comparisons.
- The float/Fraction counterexample is reproduced and its output matched to the archived log. The historical Model.forward feature-tolerance checks and 700,000-word bitwise probe are not rerun.

The helper does not recompute all 45 large-case optimal objectives, rerun native timing, or certify exact-real CE optima. Historical independent reviews that performed these checks remain intact with their original logs. Floating comparisons are still environment-dependent numerical evidence.

## Historical scripts are preserved, not an automatic replay queue

[REPLAY_SAFETY.json](REPLAY_SAFETY.json) classifies every original program. In particular:

- four_counter_dp/verify.py and its independent check_theorem.py instantiate seeded models even though their word/mask loops are exhaustive.
- bitwise_probe.py generates 700,000 random words and seven seeded models.
- run.py, test_dp.py, archive_randomness.py, archive_test_oracles.py and review_independent/check_records.py generate or regenerate random values when their relevant entry paths run. A fixed seed does not make this contemporaneous capture or a no-sampling check.
- review.py/review_all.py are statically read-only, deterministic paths using saved data plus NumPy/pilot statistics/proposals. They were not executed during this publication check; third-party runtime internals were not audited as a sampling-free dependency closure.
- followup.py reuses saved words, but reruns the executable and overwrites results. It was not executed. The preserved compiled binary is platform-specific, and no binary rebuild or execution is claimed here.

Do not run historical scripts in place: several overwrite archival output files. Running them yourself can generate random data or new timings. A future sampling run requires a separately reviewed capture guard that records actual draws, PRNG states and required candidates before analysis. This release does not provide such a guard or repair missing records.

## Explicit missing records and reconstructed artifacts

- Original benchmark: 12 words/tables/starts are retained, but the original 720 uniforms and their PRNG snapshots were not captured. randomness_replayed.json is a post-result reconstruction, not original capture.
- Original small tests: 32 seeded histories (272 returned binary values) are retained in test rows; their contemporaneous generator states and underlying bits were not saved. test_random_states.json and the compressed candidate archive were created retrospectively.
- DP runs: all 20 proposal entries per evaluation and the final chosen DP witness are retained. Full intermediate/terminal DP state sets and their scores were not saved. Aggregate states/nodes and executable inputs are not a replacement for the missing trace.
- Bitwise diagnostic: 700,000 words containing 27,800,000 binary symbol values, original PRNG snapshots and a probe-specific environment receipt were not retained. Its script/seed/aggregate seven-batch log are retained; no absence-of-mismatch proof follows.
- Model diagnostics: 5,712 normal-valued parameter entries were generated across repeated seeded initializations without saved arrays/states. This includes repetitions, not 5,712 distinct configurations: seven seed-0 models contribute 2,352 entries, five seed-123 and five seed-203 models contribute 1,680 each.
- The historical record checker made three replays of the same 12 starts and 720-uniform sequence before the stop; its transient draws/states were not separately saved. They are not three independent datasets.

## Numerical and timing boundaries

The exact four-integer recurrence has O(M^5) transition and O(M^4) rolling-state upper bounds. The rational feature identity does not make the supplied float-converting model_inputs/maximize a generic exact-rational oracle or a bitwise-exact pilot optimizer. The additive correction and concrete Fraction counterexample control that interpretation.

The 36 initial and nine outcome-informed follow-up cases attack a fixed smoothed gate Q using clean B and float64 CE, not a trained neural readout. They reuse 12 histories from three fixed source tables. Thirty-six numerical CE gaps are positive and nine tie; in four initial cases the higher CE witness has smaller true-source error. The follow-up is not independent confirmation. Source parameters are used only in generation and scoring after selection.

Internal C++ time excludes launch. entire_case_wall_s includes proposals, launch/wait, parsing and validation; isolated child-process elapsed time was not measured. Caps are checked in expansion, not a hard end-to-end deadline. No controlled throughput ratio, general practical efficiency, exact-real argmax, learned robustness or novelty claim follows.

## Identity reconciliation

All mathematical statements, programs, binary/compressed records and original seal files are unchanged. Four nonmathematical public edits remove a container hostname and private publication/coordinator routing from environment/protocol/report/review text. [The source map](SOURCE_EXPORT_MAP.json) and [reconciliation](PUBLIC_EXPORT_RECONCILIATION.json) record original/export identities without exposing removed values. Original checksums remain historical: five of 65 binding occurrences reference normalized prose and must resolve through the explicit pairs, not a falsely passing naive original-hash check. Earlier project-wide original/public maps and missing-history limits remain unchanged. The reviews are source-bound LLM audits, not external peer review or formal verification.
