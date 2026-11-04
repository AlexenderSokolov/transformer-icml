# Natural-label accessibility: completed exploratory probe

**Mixed result: the combined prespecified descriptive hypothesis was not met.** Learned pooling passed its two screens; fixed-uniform pooling missed the paired-gap screen. The explicit KT counting baseline remained stronger. This is a supplied-feature, small neural readout experiment, not an end-to-end Transformer or a general learning theorem.

## Findings and scope

Four independent replicate bundles each ran uniform/learned pooling crossed with natural-next-token/Bayes-target supervision. All 16 fits completed 1,500 updates: **24,000 optimizer steps**, with full parameters, gradients, Adam moments, minibatches, inputs, random draws/states, and per-example predictions retained. No failed experimental fit, tuning, seed selection or checkpoint selection occurred. Red unit-test logs record development failures, not additional training trials.

- Learned-natural mean primary KL(B||q): 0.00919210 nats; four of four replicate means at or below 0.02. Median paired natural-minus-B-supervised gap: 0.00553699, below 0.01.
- Uniform-natural mean primary KL: 0.01889022; three of four at or below 0.02. Median paired gap: 0.01054882, above 0.01.
- KT mean primary KL: 0.00307995. Exact add-one Bayes has zero KL to B by definition. The neural model does not beat classical counting.
- Learned-natural heldout M=128 mean KL: 0.01320127. The rare-row J<=3 macro average over eight training-length/replicate cells is 0.03146868, not pooled risk.

These descriptive cutoffs are not powered hypothesis tests. The learned model has 64 additional trainable parameters; no equal-parameter comparison is claimed. Four replicates do not establish robustness, asymptotic rates, a raw-token mechanism, or novelty. Prior Markov in-context-learning work is cited in [SOURCES.json](records/source/SOURCES.json). See [interpretation](records/INTERPRETATION.md), [results](records/analysis/REPORT.md), [complete analysis](records/analysis/all_results.json), and [frozen design](records/source/DESIGN.md).

**This new 2026-11-04 experiment does not recover or authenticate the lost original 20:35 pilot.** Its independently reviewed frozen source has original manifest SHA-256 `79b7c4937ac91d48e5eea9a2f4fe6c1b13d6568a6d8ba4f5ca038bfe07d503b6`.

## Complete public scientific archive

[PUBLIC_ARCHIVE_INDEX.json](PUBLIC_ARCHIVE_INDEX.json) lists 22 original captures totaling 638,606,434 bytes, plus the recoverable earlier interrupted implementation snapshot. Every archive member is represented. Public ZIPs are losslessly split into parts no larger than 4 MiB. Numerical NPY/NPZ members and scientific Python source are byte-identical to the originals. Textual private storage IDs and host paths are removed, so public archive hashes differ; original and public identities are both recorded per archive and member. Repeated local/roundtrip copies are deduplicated, not treated as independent evidence.

[PUBLIC_TEXT_SOURCE_MAP.json](PUBLIC_TEXT_SOURCE_MAP.json) records the additional readable handoff, settings, audits, receipts, source and development logs with exact per-edit line ranges and original/public hashes. Private transport receipts are redacted historical records, not usable service authentication. Original SOURCE_MANIFEST, CAPTURE_MANIFEST, and SCIENTIFIC_REVIEW records retain their historical bindings; they must not be misrepresented as manifests or fresh reviews of edited public bytes. The public index is the current identity authority.

## Reproduce verification offline

Use Python 3.12 and NumPy 2.3.5 for the closest numerical environment (captured build details are retained). From this directory, with a **new empty/nonexistent destination outside the checkout**:

```
python3 restore_archives.py /chosen/new/restore-directory
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 public_replay.py /chosen/new/restore-directory --report /chosen/new/offline-audit.json
cd /chosen/new/restore-directory
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 -m unittest discover -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 -m unittest review_tests review_pipeline_tests -v
```

Restoration checks every chunk, full ZIP and member before extraction. Offline replay checks all 24,000 saved gradients and Adam transitions, data/label reconstruction, final predictions, metrics and summaries using the unchanged historical numerical audit. It replaces only the two private-storage/source-provenance gates with explicitly separate public hash checks. It makes no service write/readback claim and generates no new random draw or fitted trajectory. Exact floating-point comparisons may depend on the original BLAS/NumPy platform; a mismatch must be reported rather than silently loosened.

Fresh training is a **new experiment**, not this captured result. The original [runner](records/source/experiment.py), [protocol](records/source/protocol.json), [capture code](records/source/capture.py) and [execution instructions](records/source/README.md) are retained. The runner intentionally requires genuine source/input/output storage receipts. Public redacted receipts cannot satisfy those gates. A fresh run needs its own newly frozen source identity, independent review and genuine storage roundtrips; do not manufacture identities or reassign the historical PASS review. The public offline adapter is for validating retained numerical states, not bypassing a fresh-run gate.

## Audit limits

The historical audit reports checked all saved updates and final analysis with no discrepancies. Those were independent-context analytical/computational checks, not external peer review or formal verification. Repository integrity CI checks archive membership and bytes; it does not prove the scientific hypothesis. Public-upload and readback verification is recorded separately in publication provenance.
