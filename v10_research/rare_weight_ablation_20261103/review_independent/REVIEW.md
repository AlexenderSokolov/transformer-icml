# Independent audit: rare-weight ablation

3 November 2026. Scope: sealed pre-run report and protocol, implementation, retained data and all checkpoints, update logs and reported metrics. No new model fitting or modification of author artifacts was performed. The run is useful as an exploratory diagnostic, but a serious pre-run data-preservation commitment was breached. It must not be represented as a clean, fully retained prospective confirmation.

## Critical finding: promised generated data were discarded

PRE_RUN_REPORT.md required that **all raw generated data** be preserved. In sealed experiment.py, `prior_draw` (line 34) immediately returns only words and discards each draw's latent four-row transition table. `rejection_draw` (lines 35–42) retains only the first requested accepted words and discards rejected words and accepted overflow. The uniform transition draws are not preserved either. This affects natural evaluation as well as both rejection sets.

The recorded and independently regenerated accounting is:

- Training: 8,192 generated; 6,559 passed train-group filtering; 2,048 retained. Thus 1,633 rejected and 4,511 accepted overflow words were discarded.
- Rare heldout: 122,880 generated; 1,097 passed rare-and-heldout filtering; 1,024 retained. Thus 121,783 rejected and 73 accepted overflow words were discarded.
- Natural evaluation: all 8,192 words retained, but their latent tables and transition uniforms discarded.
- Total: 128,000 generated rejection-set words not retained, including 123,416 rejected words and 4,584 accepted overflow. Latent tables for all 139,264 generated trajectories were discarded.

The saved NPZ contains accepted train, natural, rare-heldout, collision and structural words and Q labels; group arrays; and the full proposed minibatch index streams. It does not contain latent source tables, discarded trajectories, or the underlying transition uniforms. Six fits finished and checkpoint metrics and final results were exposed before this breach was identified. The code and tests had no raw-preservation assertion, so their success does not establish compliance with the promised data contract. The stopping clause addresses failed checks; there is no evidence a runtime check actually detected this breach before completion. Do not falsely describe a failed check as having fired or describe the original raw data as retained.

Independent regeneration from the sealed seeds, code and current NumPy environment reproduces all retained generated words, proposal indices and recorded selection counts. That is useful retrospective reconstruction and consistency evidence, not contemporaneous preservation, independent attestation, or proof of what happened on an unobserved original execution. Missing latents do not enter the word-based Q targets or this run's loss or metrics, so the omission alone does not show numerical bias in the observed comparisons; it does limit source-level audits and prevents a complete archival account of generated data.

## Scope and conditional laws

The forced-collision group exceptions are correctly applied. Training words are sampled from the prior **conditional on the hash group being assigned to training**, and the 1,024 rare heldout words from the prior **conditional on rare and heldout group**. First-accepted rejection sampling implements those conditional laws under independent PRNG draws. The natural 8,192-word sample follows a separate unconditioned prior draw and is not group- or word-disjoint from training. Rare-heldout groups are nonuniform and repeated; they do not represent a uniform average over rare groups. The structural test uses exactly eight finite novel feature vectors in seven heldout groups, each feature weighted equally; it is not a population-probability estimate. These three evaluation laws cannot be interchanged.

The independently recomputed group sets verify zero overlap between training/collision and rare-heldout groups, zero overlap between training/collision and the 11 structural heldout groups, and zero overlap of the eight novel structural groups with the earlier calibration groups. There are 124 represented rare-heldout groups. The train and rare heldout samples are group-disjoint, not independent latent-source experiments or uniform coverage of every possible rare group. The split and novel construction were devised after earlier exploratory results and are not historically blinded.

## Objective, checkpoint and numerical audit

The empirical rare fraction is p=133/2048=0.06494140625. Each update uses 32 rare, 32 nonrare and 64 collision indices with replacement. The corrected gradient weights are (p/2,(1−p)/2,1/2) for stratum means; their expected value is the half-collision, half-empirical-training-prior gradient. It is **not** an unbiased unconditioned-prior gradient, because training itself is hash-conditioned. The rare-boost weights are (1/4,1/4,1/2), a different objective; matching the index stream does not match gradient variance or isolate the objective landscape from optimizer dynamics.

For all six fits, paired initial weights match exactly. Independent first-step CE and gradient-norm calculations agree with logs to at most 1.12e-16 and 8.89e-16 respectively. Literal independent reconstruction of features and Q has zero target discrepancy. All 24 checkpoint rows and retained final predictions reconstruct within 1.95e-16; the 12,000 update records, 24 checkpoint files, six final rows, saved index streams, and source/output manifests are present. All 15 sealed-input and 32 output-manifest hashes match. This audit did not rerun the full optimizer trajectory or prove the implementation correct on unobserved inputs.

On the retained data, all three seeds satisfy the stipulated computational composite screen: boosted/corrected structural-novel mean-absolute-error ratios are 0.3171, 0.4586 and 0.4480; natural mean-KL differences are −0.000241, −0.000436 and −0.000571; and boosted in-sample collision maxima are 0.00369, 0.00451 and 0.00221. These thresholds were sealed before the generated data and observed fits, as recorded by local timestamps and hashes, but the preservation breach remains and the eight-vector test was not historically blinded.

The secondary metrics prevent saying that boosted performance simply improved everywhere. Natural-prior mean absolute error increases by 0.00640, 0.00340 and 0.00246 respectively, although mean KL decreases. Rare-conditional mean absolute error decreases from 0.05760, 0.04728, 0.05650 to 0.02900, 0.02971, 0.03196 on the saved holdout. On the full 11-feature structural slice the boosted maximum errors remain 0.3852, 0.3305 and 0.3600. These are exploratory conditional and finite-panel observations, not a uniform fit, source-risk or robustness guarantee.

For context only, paired pointwise Monte Carlo SEs for the natural-prior KL differences, using the 8,192 shared evaluation words and conditioning on each fitted pair, are approximately 0.000149, 0.000134 and 0.000149. They are not simultaneous confidence bounds, account for neither initialization nor data-selection uncertainty, and do not create three independent data replications: the seeds share all train and evaluation samples and index streams. No significance test was declared.

## Prospective confirmation after exposure

A new protocol can be prospectively frozen **after** these outcomes are disclosed, then use fresh independent training/evaluation RNG streams and preserve every generated draw, latent table, acceptance decision, and index before training. Such fresh draws can provide new statistical evidence conditional on that later fixed design, but cannot restore the first run's original preservation or historical blinding. Reusing the same eight now-exposed structural feature vectors is a replication on known vectors, not a fresh independent structural holdout. Any post-result changes to splits, features, objectives or thresholds must be transparently designated as informed by the exploratory results, and no new run should be silently presented as the original pre-specified confirmation.

Supporting files in this review directory independently regenerate the draws in memory for comparison, reconstruct features, metrics and initial gradients, and retain only the audit code and textual output. They do not purport to be original raw artifacts.
