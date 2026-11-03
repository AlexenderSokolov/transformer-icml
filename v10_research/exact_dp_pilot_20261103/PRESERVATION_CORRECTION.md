# Preservation correction

This is an additive correction; the original initial and follow-up protocols, data, code, results, logs and preceding report remain unchanged.

The initial run contemporaneously retained its twelve generated words, source tables, initial pairs, seed and generator code, but did **not** save the raw random uniforms or each PRNG state at the time they were originally drawn. `randomness_replayed.json` was reconstructed after the initial results, by rerunning the saved seed and generator sequence, and its reconstructed outputs match all originally saved words and initial pairs. This is a deterministic replay artifact, not contemporaneous raw capture, and matching words does not independently establish that the original random uniforms were preserved.

Similarly, the exhaustive test uniform/PRNG and candidate archive was reconstructed after those tests from the saved seed, saved case words and test code. It is labeled as a replay, not a contemporaneous audit log. The DP experiment retained its selected final witness, per-case result and all 20 block/sparse proposal entries, not every DP terminal bank or all intermediate reachable states. Those missing contemporaneous records must not be described as captured or retroactively recovered. Deterministic replay can be attempted from saved code and inputs, subject to runtime and platform, but is not a substitute for the original trace.

Any future newly sampled work must save generator state and actual random draws and relevant candidate/state records before outcome analysis, retaining append-only originals and logging failures. This correction does not alter numerical outcomes, and no new sampling is authorized by this note.
