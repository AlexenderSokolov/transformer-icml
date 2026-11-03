# Independent audit of retained rare-weight ablation

3 November 2026. This audit reads the completed original artifacts and recomputes features, targets, predictions, metrics, partitions and screen decisions from saved words and model parameters. It did not simulate words, resample indices, replay optimization, modify sealed inputs or train a model. The audit script is a separate implementation and does not import the calibration or experiment implementation.

## Findings

No numerical, prediction, grouped-split or screen discrepancy was found. All 32 files listed in the run's artifact-hash manifest and all 15 pre-run sealed inputs match their SHA-256 hashes; the run-output manifest accounts for every retained file in `ablation_v1` except itself. The six final checkpoints' predictions agree exactly with all 36 saved final prediction arrays. An independent direct Bernoulli-KL computation and half-count reconstruction reproduce 1,008 numerical fields for all 24 checkpoint rows to a maximum absolute difference of 1.12×10⁻¹⁶. All six final CSV rows agree with their checkpoint rows and `results.json`, and the original captured console's 24 checkpoint records and final screen agree with those outputs. Each pair of step-0 parameter sets is identical.

Independently reconstructed `(J,C,D,U)` groups confirm no overlap between training (including collisions) and either the sampled rare-group holdout or the 11-vector structural holdout. The eight-feature primary set is exactly the subset of the 11 held-out vectors whose groups do not occur in any of the old train, validation, collision or boundary words; it contains seven distinct groups. The new training set has 133 rare and 1,915 nonrare words, and all frozen rare, nonrare and collision minibatch indices have the declared dimensions and point into the correct strata. The natural-prior sample shares 14 distinct words with the training sample, as disclosed. The exact grouping and prior holdout are not a claim of unseen sources or all-word generalization.

The three paired screen ratios recompute as 0.3171342243, 0.4585647066, and 0.4479885741. The boosted-minus-corrected natural KL changes are −0.0002405593, −0.0004359052, and −0.0005707348. Boosted collision maximum errors are 0.0036909830, 0.0045123654, and 0.0022079164. Every pair meets all three fixed support-screen conditions. Other rounded numerical claims in the completed report agree with reconstructed final predictions and metrics. There are three paired decisions over six fits, not six independent evaluations; all three pairs share the same data and sampling stream.

## Disclosure correction and scope

The preservation limitation is real: the source discards rejected or truncated candidate words and does not retain latent transition tables or transition uniforms, and checkpoints do not contain Adam moment states. Counts in the retained sampling log imply 128,000 candidate words were discarded, as reported. The report's statement that generator starts for the retained samples were not stored needs one qualification: although no separate start array was retained, each saved word begins with its initial pair, so a retained word's initial pair is recoverable exactly from its first two bits. Initial pairs of discarded words cannot be recovered from the retained word arrays. This does not recover the missing generator tables, random uniforms, or rejected words.

The retained checkpoint and prediction results are now exposed; this is not a pristine confirmation set. Filesystem modification times are consistent with the reported order of seal, saved dataset and completion, but timestamps and this numerical audit do not establish the exact time at which human or root approval was given. The artifact set can establish consistency of retained predictions and reported metrics, not prove every gradient or Adam update was executed as intended: full gradient tensors and optimizer states were not saved, and optimization replay was explicitly outside this audit's scope. The theoretical interpretation remains a finite controlled weighting intervention, not proof of a uniform approximation, a width-32 capability limit, or general-source risk.

## Reproduction

From the workspace root:

    OPENBLAS_NUM_THREADS=1 python -B v10_research/rare_weight_ablation_20261103/independent_audit_20261103/audit.py

`AUDIT_RESULTS.json` retains the complete machine-readable output of that check, including six reconstructed final rows. `SOURCE_BINDINGS.json` records hashes of the audited manifest, report, console, and this review's script and results. The separate run manifest binds each completed-run output.
