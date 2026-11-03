# Learned positional pooling: exploratory smoke result

3 November 2026. This is a completed author-run smoke pilot, **not independently accepted**, not preregistered research, and not a minimax experiment. The protocol and source/test hashes were fixed before the run. No expansion was performed.

## Result first

The model trains and its temporal pooling weights move, but this smoke **does not demonstrate useful learned positional protection**. Edit training does not clearly beat its count-only or frozen-random controls, and its finite-panel score is worse at the held-out length M=256. Replacing the learned edit-trained profiles with uniform pooling improves rather than destroys both clean loss and the descriptive stress-panel maximum. The supplied-half readout control also does not help. Readout/optimization calibration therefore remains unresolved; this is not a result that positional protection cannot be learned.

One initialization, five conditions, and 200 Adam updates per condition were run. Each condition saw the same 12,800 fresh training trajectories, alternating M=64 and 128. The training-data digest is identical for all five conditions. Evaluation used 2,048 independent clean-prior trajectories per length, plus 256 trajectories for each of three stress sources and starts 00/11 at each of M=64,128,256. Conditions shared evaluation paths. The stress source tables satisfy the declared critical all-state certificate; the training prior was not conditioned on that certificate.

## Observed clean excess cross-entropy

Values are nats relative to the exact CTO add-one posterior, averaged over the clean training prior. Parentheses are approximate pointwise Monte Carlo SE, not simultaneous intervals.

| Condition | M=64 | M=128 | M=256 |
|---|---:|---:|---:|
| Learned pooling, clean training | 0.018510 (0.000579) | 0.020801 (0.000719) | 0.023116 (0.000849) |
| Learned pooling, edit training | 0.022388 (0.000715) | 0.023419 (0.000821) | 0.025040 (0.000940) |
| Uniform frozen pooling, edit | 0.019163 (0.000624) | 0.021516 (0.000763) | 0.023973 (0.000894) |
| Random frozen pooling, edit | 0.019175 | 0.021532 | 0.023988 |
| Fixed half/suffix pooling, edit | 0.019202 (0.000627) | 0.021525 (0.000763) | 0.023972 (0.000895) |
| Edit-trained model, uniform-profile ablation | 0.019301 (0.000633) | 0.021734 (0.000774) | 0.024114 (0.000910) |

For scale, the explicit smoothed robust comparator Q has clean excess 0.017151, 0.010193, 0.006229 on these same paths. B has zero excess by definition. A is not silently clipped: its boundary predictions give infinite conditional CE on some clean paths, recorded in clean_evaluation.csv.

## Descriptive stress-panel maxima

Each entry is the largest estimated expected absolute probability error divided by max(M^(-1/2),k/M) among the finite source/start/budget/attack cells. The attack is selected using the clean-word reference B(w), never the hidden table or future label. All learned-model maxima below occur under the held-out proposal family on the symmetric sticky source a=t=2/M. These numbers are **not upper bounds on worst-case risk**. Their individual-cell MC SE values do not account for maximum selection.

| Condition | M=64 | M=128 | M=256 |
|---|---:|---:|---:|
| Learned pooling, clean training | 1.3269 | 1.3501 | 1.6595 |
| Learned pooling, edit training | 1.4378 | 1.5301 | 1.9876 |
| Uniform frozen pooling, edit | 1.4662 | 1.5318 | 1.9323 |
| Random frozen pooling, edit | 1.4685 | 1.5330 | 1.9342 |
| Fixed half/suffix pooling, edit | 1.4845 | 1.5418 | 1.9664 |
| Edit-trained model, uniform-profile ablation | 1.3799 | 1.4259 | 1.8275 |

For learned-edit, the selected cells have MC SE 0.0847, 0.1037, 0.1567. Small differences between the learned and frozen controls are not evidence of reliable improvement. All individual cells and trajectory-level errors are retained for paired inspection; no hypothesis test or confidence band was declared successful. Baseline B/A/Q results are also retained. Their finite-panel rankings cannot overturn their established asymptotic guarantees or obstructions.

The learned-edit heads place first-half masses 0.4773 and 0.4784 at M=128, with last-quarter masses 0.1929 and 0.1890. Thus they learned nonuniform temporal weighting, but not an obvious half-prefix gate. The learned-clean heads have first-half masses 0.4843 and 0.4609. Heatmaps are not treated as proof of mechanism, and this smoke did not run the proposed count-preserving collision intervention or a greedy Hamming-ball attack.

## What ran and what was checked

- The predictor is the specified 369-parameter fixed-tokenizer NumPy pooling/readout model. It receives neither B nor the hard gate as an input.
- The edit objective exactly maximizes over identity plus nine finite proposals. This is not maximization over the full Hamming ball. Held-out proposals use different block locations and sparse deterministic positions.
- The attack API accepts only a prediction function, observed words, budget and family. The actual supplied predictors have no table/label access. All test output words were checked for protected endpoints and per-word edit budget.
- Nine unit tests pass: all 369 parameter gradients; exact small-word posterior and count/gate enumeration; literal simulator equivalence; independently formed full triple bank versus selected features; exhaustive small-word attack legality and tie behavior; finite-proposal maximization; frozen controls/count-only invariance; combined clean/edit gradient consistency; and stress-source certificates.
- Maximum absolute analytical-versus-central-difference gradient discrepancy was 1.44115e-10. Tests first failed because the implementation module was absent; the red log is retained.
- Author verification checked all 39 generated artifact hashes and five sealed source/config hashes. All 960 stress-row means and standard errors were recomputed from retained trajectory arrays, with zero discrepancy in the means. This is an author check, not independent review or formal verification.

## Actual cost and reproducibility

Total runtime was 15.49 seconds on the available CPU environment, including unit tests, training, evaluation and saving. Training seconds were 2.20 learned-clean, 2.45 learned-edit, 0.91 uniform, 0.88 random, and 0.96 half. Evaluation took 5.87 seconds. One BLAS thread was explicitly selected. The saved run occupies approximately 3.81 MB before filesystem overhead.

Candidate features were fully rescanned rather than using an incremental three-triple optimization. This is intentionally easier to audit and was fast enough for the smoke. No Torch/JAX installation, external service, GPU, or paid resource was used. Float64 uniforms approximate the continuous mathematical prior; there is no finite-bit sampling or training theorem.

From this directory:

    OPENBLAS_NUM_THREADS=1 python test_pilot.py
    python run.py run --output independent_replay

The runner verifies PRE_RUN_HASHES.json and refuses to overwrite an existing output directory. Do not rerun `seal` or edit sealed files to replay this experiment. Compare the numerical arrays and CSVs across runs; wall-clock times and environment metadata in results.json are expected to differ. Checkpoints contain weights, not a saved Adam state; complete runs are reproducible from seeds, while mid-step resumption would require rebuilding optimizer history.

Important artifacts:

- protocol.json, PRE_RUN_HASHES.json: fixed exploratory choices and pre-run input hashes.
- pilot.py, test_pilot.py, run.py: implementation, tests and sealed entrypoint.
- tests_red.log, tests_green.log, tests_preseal.log: observed test history.
- smoke_v1/checkpoints/: all declared initial and 50-step weight checkpoints.
- smoke_v1/training.csv: all 1,000 updates, including pooling-gradient norms and attack activity.
- smoke_v1/clean_evaluation.csv, stress_evaluation.csv, descriptive_panel_maxima.csv, profiles.csv.
- smoke_v1/evaluation_paths.npz: complete synthetic evaluation words and source tables.
- smoke_v1/trajectory_metrics.npz: per-trajectory losses and selected proposal indices.
- smoke_v1/results.json, ARTIFACT_HASHES.json; verification.json: result, output bindings and author recomputation.
- smoke_v1_console.log: complete run output.

## Decision and boundary

Stop here for root review, as requested. A larger seed/horizon sweep is not justified by this smoke alone. If research continues in this architecture, the next bounded question should be **whether the readout can learn the known useful fixed-half information at all under the chosen objective and optimization budget**, or whether the structured-edit objective encourages a different, unhelpful weighting. Any changed training budget/objective/model must receive a new version and fresh fixed protocol. Existing smoke failures should remain visible.

No frozen theorem/manuscript files, source antecedents, or remote repositories were altered.
