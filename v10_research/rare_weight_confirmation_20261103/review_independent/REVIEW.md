# Independent audit: rare-weight follow-up

3 November 2026. Scope: the reviewed/sealed design, committed candidates, split and minibatches, all update-journal records, checkpoints and optimizer states, retained metrics and console. No author artifact was modified and no new model was fitted. No new preservation defect was found in this completed run. The previous ablation's missing raw data remain missing; this run does not repair that earlier record.

## Provenance and committed raw data

The approval marker and pre-run seal contain identical bindings for 18 inputs, and all 18 hashes match. The independent review and its input manifest match the hashes named by the approval marker. Local timestamps place review first, approval and seal at approximately 06:55:18 UTC, and the first candidate intent thereafter. These local files and timestamps are reproducibility and order evidence, not an independent timestamp or a cryptographic proof of all human decisions.

Independently regenerated every candidate directly from the declared seed and draw order, without calling the author's simulator. All 14 candidate batches (114,688 candidates: 8,192 training, 8,192 natural and 98,304 rare-heldout), and all corresponding 14 pre-draw intents, have matching PRNG before/after states, latent transition tables, starts, 64 transition-uniform vectors, derived words, eligibility and selected flags. The selected arrays match frozen_data.npz exactly. Every committed batch, including rejected and accepted overflow examples, is retained in the output manifest. The minibatch PRNG states and all 2,000 proposed index triples also reproduce exactly. All 61 output-manifest hashes match.

The completed files support preservation of this run's actual committed data. As the amendment correctly explains, a pre-draw intent alone would not preserve random values from a generated-but-uncommitted batch, and durability depends on the storage system honoring the requested fsync semantics. There were no unmatched candidate intents in the completed output. The prior run remains a separately disclosed, noncompliant exploratory record.

## Split, teacher and sampling

Independent literal recounts of all saved words match their Q labels exactly. Training and collision groups have zero overlap with the rare-heldout groups and with the reserved structural groups. The saved reserve contains 20 distinct feasible J≤3 feature vectors in 18 groups, exactly the groups absent from every prior calibration and ablation input/evaluation word array, and those groups are excluded from current training. Old enumerated identities and targets were already available. The assertion that no earlier predictions on these vectors were inspected is a provenance statement, not something the saved word arrays alone can prove.

The primary sample consists of 1,024 fresh accepted words from the prior conditional on rarity and the amended holdout group split. Repeated groups follow their conditional prior frequencies; they are not a uniform rare-group sample. The 20-vector structural diagnostic is an equally weighted deterministic finite panel, not a source-frequency sample. Natural evaluation is a separate unconditioned prior-word sample, permitted to overlap training in groups or exact words. These different distributions should not be conflated. The labels in all cases are supervised Q(word), not future-token labels or a true-source risk score.

## Full update and result reconciliation

Independently parsed and checksum-verified all 12,000 journal records, checked the six expected ordered 2,000-step sequences against the update CSV, and recomputed **every** recorded minibatch weighted CE and all 353 gradients from the frozen examples, index stream and pre-update parameters. Maximum gradient discrepancy was 4.45e-16 and maximum loss discrepancy 2.23e-16. Independently reconstructed Adam first/second moments and each proposed parameter state, reconciling all 24 checkpoints including step, moments and hyperparameters: maximum proposed-parameter discrepancy 2.23e-16, moment discrepancy 6.94e-18, and checkpoint-parameter discrepancy zero. CSV gradient/weight norms agree to 5.56e-17. All paired initial parameter arrays match each other and the declared seed initialization.

The write-ahead journal alone records prepared updates, but here its entire sequence agrees with subsequent CSV rows, all later model and optimizer checkpoints, and final outputs. Independently recomputed every checkpoint metric and final prediction within 1.67e-16. Six final CSV rows equal both final checkpoint rows and result JSON; 24 console checkpoint records equal their CSV counterparts, and its terminal screen equals results.json. The external console log's audit-time SHA-256 is 76c053e0e64b91a6b70eb027f444d1474b458cbfb93a838f08a89d73c44b39cc; it sits outside the output manifest, so this audit hash is a current binding, not an earlier externally attested hash.

## Findings and tradeoffs

The predeclared computational screen passes in all three initializations. Boosted/corrected primary rare-heldout mean absolute-error ratios are 0.7267, 0.6617 and 0.6756. Corrected means 0.07179–0.07695 decrease to boosted means 0.05091–0.05217. Natural mean KL changes by +0.000245, −0.000227 and +0.000409, all within the 0.002 ceiling; collision maximum errors are 0.00304, 0.00620 and 0.00756 on the four trained collision words.

The tradeoffs matter:

- Natural-prior mean absolute error **increases** in all seeds by 0.00626, 0.00621 and 0.00818, from corrected 0.00790–0.00859 to boosted 0.01410–0.01664. The natural-KL outcome is mixed, not an unqualified natural-performance improvement.
- Boosted rare-heldout maximum absolute errors remain 0.6985, 0.6035 and 0.7376. The screen measures a conditional sample mean and supplies no uniform-accuracy bound.
- On the reserved 20-vector secondary panel, mean error decreases in each seed, from 0.1615–0.1788 to 0.1242–0.1284, while maximum error rises in seeds 601 and 603. Boosted maxima are 0.3898, 0.3802 and 0.4029. These vectors are a finite, non-historically-blind diagnostic, not an all-word or source-risk certificate.

For context, paired pointwise Monte Carlo SEs for boosted-minus-corrected rare-heldout mean absolute error are approximately 0.00130, 0.00144 and 0.00165, conditional on the fitted model pairs and amended sampling distribution. They are not simultaneous confidence bounds or a predeclared significance test. All three initializations share one training dataset, one heldout dataset, one natural dataset and one minibatch stream; they are not three independent data replications. Natural-prior paired mean-error SEs are approximately 0.000174, 0.000170 and 0.000189 under the same conditional interpretation.

## Appropriate conclusion

This is a reproducible **non-blind fresh-data follow-up** supporting the specified rare-weight intervention for the stated conditional supervised-Q mean endpoint, with material ordinary-prior mean-absolute-error tradeoffs and large individual failures. It does not establish uniform approximation, robustness to source edits, natural next-token/source risk, minimax guarantees, width-32 representability or impossibility, or a general optimizer theorem. The selection and design were informed by previously exposed exploratory results, and the preserved new run cannot retroactively make the earlier run complete or blinded.

The independent audit scripts and their outputs are retained in this review directory. They reconstruct saved state for verification and do not create new fitted models or modify the author run.
