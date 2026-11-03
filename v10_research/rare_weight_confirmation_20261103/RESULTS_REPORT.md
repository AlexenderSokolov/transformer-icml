# Rare-weight follow-up: completed, awaiting independent audit

3 November 2026. The six approved fits completed under the sealed protocol. This is a non-blind fresh-data follow-up of the first ablation, with three paired initializations sharing one training draw, one unconditioned validation sample, one conditional heldout sample, and one minibatch stream. It is explicitly Q-supervised fixed-feature calibration, not natural next-token learning, a source-risk result, a uniform approximation theorem, or a capacity/optimization impossibility statement.

## Main result and tradeoff

The predeclared composite screen passed in all three initializations. On the 1,024 sampled words conditional on rarity and the amended holdout group, final mean absolute errors for corrected versus rare-boost were:

| Initialization | Corrected | Rare boost | Boost/corrected |
|---|---:|---:|---:|
| 20261103601 | 0.071794 | 0.052172 | 0.727 |
| 20261103602 | 0.076946 | 0.050913 | 0.662 |
| 20261103603 | 0.076528 | 0.051703 | 0.676 |

The natural-prior mean KL changes, boost minus corrected, were +0.000245, −0.000227, and +0.000409, each within the predeclared +0.002 allowance. Boosted maximum errors on the four supplied, **in-sample** collision words were 0.00304, 0.00620 and 0.00756, each below 0.05. These are operational thresholds, not statistical significance tests.

A meaningful tradeoff is hidden by the KL screen: natural-prior **mean absolute** error rose from 0.00859, 0.00790, 0.00846 to 0.01485, 0.01410, 0.01664 across the same pairs. The rare-conditional sample's maximum errors after boosting were 0.699, 0.604 and 0.738, versus 0.695, 0.743 and 0.692 before; its mean improvement does not imply worst-case improvement. The natural sample is independent and unconditioned but has 15 distinct word strings also present in training; it is not word- or group-disjoint. The 1,024-word rare sample instead is conditional on the hash-and-reserve holdout rule and has 143 distinct `(J,C,D,U)` groups. Do not compare the two samples as if they estimated the same distribution.

## Input-novel structural test

The secondary structural test uses all 20 enumerated feasible M=64, J≤3 feature vectors in 18 statistic groups absent from every input/evaluation array in both earlier calibration and completed first ablation. All 18 groups were predeclared and removed from fresh training, rather than chosen by model performance. Their identities and Q targets were already available in the enumeration, and the follow-up was designed after prior results were exposed, so call them **input-novel but nonblind**, not a blind or independent scientific preregistration. They are weighted equally by feature, not by prior frequency.

Corrected versus boosted mean absolute error was 0.16152→0.12417, 0.17638→0.12836 and 0.17884→0.12683. Maximum error was 0.32587→0.38978, 0.39955→0.38016 and 0.40226→0.40295. Thus boost improves the mean in this finite slice for each pairing, but does not uniformly improve its maximum. The prior eight and eleven examined structural vectors are retained separately as known-vector diagnostics. No conclusions about unobserved words or all-state capacity follow.

Both arms use the same word/index streams and identical starting parameters in each pair. Corrected stratification reweights by the empirical 115/2048 rare share of the train-group sample; boost gives rare and nonrare half each of the prior objective mass, retaining half of the total loss on collision words. Because reweighting changes both the objective and stochastic-gradient variance, the experiment does not disentangle their mechanisms. The amended reserve changes the training-group distribution compared with the first ablation.

## Preservation and verification

The independently reviewed source hashes and root permission were checked before the seal at 06:55:18 UTC and before sampling. The exclusive-create launcher captured stdout and stderr in `confirmation_console.log`. The retained `confirmation_v1/` includes 14 committed candidate batches: 8,192 training candidates, 8,192 natural candidates and 98,304 rare-holdout candidates. Every batch includes original candidate words including rejects and overshoot, latent transition tables, starts, all transition uniforms, selection flags, before/after PRNG states, and a separately durable pre-draw intent. The selected arrays, all 2,000 minibatch index streams, 12,000 update-summary rows, 12,000 full 353-gradient/353-proposed-parameter write-ahead records, 24 checkpoints with model and Adam state, metrics, final predictions and hashes are retained. `ARTIFACT_HASHES.json` binds 61 output files.

Author-side checks in `self_verify.log` reconstructed the retained candidate arrays and selection flags, reconciled all 12,000 journal records exactly with the update-summary order and the Adam recurrence, and reconciled all 24 checkpoint parameters and Adam moments. The final saved predictions and checked final metrics matched exactly. `self_verify_supplement.log` reconciled 24 console checkpoint records with the CSV, recomputed all three screen rows, and verified the console's final done message. These are **author** checks; independent audit is pending. Exact cross-platform replay is not promised.

The batch intent does not preserve values held only in RAM if a batch is interrupted before its committed file; it flags uncertainty. A complete journal record is write-ahead and does not alone prove its update was applied or evaluated. This completed run was reconciled against CSV, checkpoints, results and console, but any future interrupted run must not be silently resumed, discarded or represented as complete. These limits do not repair the preceding run's unsaved rejected draws or latent inputs.
