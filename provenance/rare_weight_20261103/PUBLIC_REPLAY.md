# Rare-weight experiments: complete available records and lossless journal replay

This archive contains both fixed-feature, explicit-Q-supervised weighting experiments, their exact low-count enumeration dependency, all original retained data and updates, and both independent completion audit sets. The three paired initializations in each experiment share their datasets and minibatch stream. The second experiment is a fresh-data but nonblind follow-up, not a blind preregistration or a new general learning theorem. The historical `root` label denotes the coordinating scientific reviewer; the review gates and hashes are local scientific workflow records, not external peer review or trusted timestamps. All reviews here are independent LLM audits.

## What the first experiment did not preserve

The first ablation retained accepted words, minibatch indices, 12,000 summary updates, 24 model checkpoints, predictions, metrics, console, sources and settings. It did not contemporaneously save 128,000 rejected/truncated candidate words, their latent transition tables and uniforms, or the latent tables/uniforms for retained candidates. Retained initial pairs can be read from the first two bits of each retained word; discarded candidates' starts are unavailable. Its checkpoints have no Adam moment states, and its update CSV records gradient norms rather than full gradients.

A deterministic compatibility check from stored seeds is not recovery of those original uncaptured records. No missing first-run data are included or described as recovered. Read the [completed report](../../v10_research/rare_weight_ablation_20261103/COMPLETED_RUN_REPORT.md), [initial-pair correction](../../v10_research/rare_weight_ablation_20261103/COMPLETED_RUN_REPORT_CORRECTION.md) and [completion audit](../../v10_research/rare_weight_ablation_20261103/independent_audit_20261103/REVIEW.md) together. Earlier promises and pending-review status text remain historical, not silently rewritten.

## What the follow-up preserved

All 14 original committed candidate batches are present: 114,688 words, including rejects and overshoot, latent transition tables, starts, transition uniforms, selection flags and PRNG states, plus every corresponding pre-draw intent. The selected datasets and complete 2,000-step minibatch stream, all 12,000 summary updates, 12,000 full-gradient/proposed-parameter journal records, 24 model-and-Adam checkpoints, metrics, final predictions and captured console are retained. A write-ahead proposal alone does not establish application; the independent audits reconcile the full trajectory with the checkpoints, CSV and console. An uncommitted future intent would flag uncertainty, not preserve values held only in memory. No interrupted run is silently repaired or resumed.

## Journal storage and exact reconstruction

The original `confirmation_v1/full_updates.bin` has 71,171,358 bytes and SHA-256 `8869667903e50345fa375bd91b85dc9db0b8aef071b0f1cbdd27b9fa2f8ddf75`. It is represented by 17 uncompressed, contiguous raw byte chunks under `journal_chunks/`. [JOURNAL_CHUNKS.json](JOURNAL_CHUNKS.json) gives their order, offsets, sizes, SHA-256 and Git blob identities, plus the original file identity. There is no record selection, recompression or data omission. Concatenating the listed chunks reconstructs the exact original journal.

GitHub documents a 50 MiB warning and 100 MiB block for ordinary repository files. The source is below that block. The connector exposes no smaller numeric creation limit, so this is a conservative bounded-transport representation, not a claim the source was rejected. See [GitHub file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) and [the blob API](https://docs.github.com/en/rest/git/blobs).

To reconstruct only the journal at its original repository-relative path under a new directory outside this checkout:

```sh
python provenance/rare_weight_20261103/reconstruct_journal.py --output-root /tmp/rare-journal-copy
```

The program verifies the current inventory and chunk manifest, checks each chunk, checks the reconstructed size/SHA-256/Git identity, and exclusively creates the destination file. It refuses an existing destination, including a dangling symlink, and checks destination containment before creating directories. It never overwrites a retained journal or writes the reassembled file into the public checkout.

## Complete isolated audit copy

From the public repository root, choose a destination that does not exist and is outside the checkout:

```sh
PYTHONDONTWRITEBYTECODE=1 python provenance/rare_weight_20261103/prepare_public_replay.py --destination /tmp/rare-weight-public-replay
cd /tmp/rare-weight-public-replay
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python v10_research/rare_weight_ablation_20261103/independent_audit_20261103/audit.py
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python v10_research/rare_weight_confirmation_20261103/independent_completion_audit/audit_after_completion.py
```

The preparation program verifies every published input, copies the complete scientific selection and exact inherited inputs, then reconstructs the original journal path. Chunk storage files are not inserted into the experiment's output directory, so the original 61-entry artifact manifest retains its exact membership. The first output directory likewise retains all 32 manifest entries. Destination files are created exclusively. If materialization fails after copying some verified files, the incomplete directory is deliberately left for inspection, without a success receipt; do not treat it as a complete replay or silently resume it. No source, seal, review marker, mathematical expression, training configuration or checker predicate is changed. The program refuses optimized Python; scientific assertions must stay active. The full completion audit reconstructs saved random arrays and recomputes recorded losses/gradients/Adam steps for verification; it does not fit a new model or create a new experimental sample.

The only source-copy privacy edit removes a private absolute prefix from the enumeration's historical failed traceback. [The export map](SOURCE_EXPORT_MAP.json) and [reconciliation](PUBLIC_EXPORT_RECONCILIATION.json) distinguish its original and public hashes. The historical enumeration source binding still records the original log hash; do not call a naive comparison against that normalized log an exact original-hash pass. This log is not a sealed training input. All executable code and scientific seals remain exact, so no resealing or weakened validator is needed for the audits above.

Additional read-only author and independent checks can be run inside that copy: `self_verify.py`, `self_verify_supplement.py`, the two independent data/journal/summary checker sets, and `validate_update_journal.py confirmation_v1/full_updates.bin --complete` from the follow-up directory. Prefix-only journal validation is weaker than `--complete`, and neither alone replaces reconciliation with CSV/checkpoints/console. The enumeration's independent checker can also be run there. Do not redirect output to an existing historical log.

A new fit is not performed by archive preparation or audit. The original runners, full settings, seeds and scientific gates are included for an explicitly separate replay. Use a new output/log name if choosing to run them; their exclusive-create safeguards must remain in place. A fresh replay is not new historical evidence, and numerical/environment/timing bytes may differ across platforms. The first run's missing latent records and Adam state remain missing regardless of a fresh replay.
