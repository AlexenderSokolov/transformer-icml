# Independent audit of the rare-weight follow-up

3 November 2026. The completed run's retained arrays, checkpoints, update journal, metrics, screen, console and hash bindings were checked independently. The audit performed no new experiment draws or fits. Its RNG check deterministically replays the saved pre-batch states solely to compare against already retained random arrays; its gradient and Adam calculations reconstruct the recorded trajectory without changing a model or using newly generated observations.

## Verdict

**PASS: no numerical, split, preservation or reporting discrepancy was found within the checks below.** All 18 reviewed sealed-input hashes, 61 run-output hashes, and the author's 74 separately bound result files match. The external console is bound separately, SHA-256 `76c053e0e64b91a6b70eb027f444d1474b458cbfb93a838f08a89d73c44b39cc`. The machine-readable output and independent script are retained alongside this report.

All 14 committed candidate batches were inspected, comprising 114,688 original candidates: 8,192 train, 8,192 natural and 98,304 holdout. Every pre-draw intent matched its batch's initial PRNG state; consecutive before/after states and the sealed initial seed agreed. Independently replayed states reconstructed every saved probability, initial pair and transition uniform exactly; a separate literal pair-transition implementation reconstructed all candidate words. Eligibility and first-N selection flags reproduced, including rejected and overshoot cases. The selected arrays reproduced the 2,048 training, 8,192 natural and 1,024 conditional heldout words. The complete 2,000-step frozen minibatch stream and final PRNG state also reproduced.

Independent literal counts and targets reproduced every frozen array. The sampled rare holdout and 20 reserved low-J feature vectors in 18 prior-input-absent groups have zero group intersection with fresh training or supplied collisions. The prior 11-feature and eight-feature diagnostic slices also match their stipulated definitions. The unconditioned natural sample shares 15 distinct words with training, as disclosed. The empirical rare fraction is 115/2,048.

Every one of the 12,000 journal records was checked for framing, checksum, identities, order and schema. Using frozen minibatches and the retained pre-update parameters, an independent implementation recomputed every weighted loss and all 353 gradient values, then reconstructed the Adam recurrence and proposed post-update parameters. These agree with the journal and each update-summary CSV row. All 24 checkpoints, including parameter arrays, Adam first and second moments, step and optimizer hyperparameters, agree with the reconstructed state. Maximum absolute discrepancies were 2.23×10⁻¹⁶ for losses, 3.54×10⁻¹⁶ for gradients and 3.34×10⁻¹⁶ for both parameter updates and checkpoint state.

All 24 checkpoint metric rows and all 42 saved final prediction arrays were independently reconstructed; maximum absolute differences were 3.34×10⁻¹⁶. The CSVs, results JSON, 24 checkpoint records in the console and final console screen reconcile. All three paired composite screens pass: boosted/corrected heldout MAE ratios are 0.72669, 0.66168 and 0.67561; changes in unconditioned natural-prior mean KL are +0.00024511, −0.00022730 and +0.00040887; boosted in-sample collision maximum errors are 0.003044, 0.006199 and 0.007559. The rounded numerical claims in the author report agree with reconstructed metrics.

## Interpretation and limits

On the 20 input-novel structural vectors, boosted mean errors are 0.12417–0.12836, while boosted worst errors remain 0.38016–0.40295. The mean improvements and finite composite pass do not establish uniformly small errors, an all-word approximation result, model-width necessity or a general-source guarantee. The unconditioned and conditional evaluation samples follow different distributions. Three paired initializations share one dataset and one index stream; they are not independent data replications. The follow-up and its structural identities are not historically blind.

A durable batch intent without a committed NPZ would flag uncertainty, not preserve values generated only in RAM; this completed run has a committed NPZ matching every intent. Journal entries are write-ahead proposals, not by themselves proof of commit: here their values reconcile with all 12,000 summary rows, final checkpoint states, metrics, and console completion. This audit does not prove future cross-platform bitwise replay or recover missing randomness from the preceding ablation. Root retains final scientific acceptance.

## Reproduction

From the workspace root, after the experiment has stopped:

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python -B v10_research/rare_weight_confirmation_20261103/independent_completion_audit/audit_after_completion.py

`AUDIT_RESULTS.json` preserves the full raw check output and `AUDIT_ERROR.log` is empty for the passing run. `SOURCE_BINDINGS.json` binds the audited input manifest, report and console as well as the independent script, check output and this report. The run's own manifest binds each original output.
