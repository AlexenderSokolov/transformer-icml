# Reproduce the natural-label accessibility probe

This is a new bounded exploratory experiment, not recovery of the missing old pilot. Read DESIGN.md before interpreting any outcome. Pure Python 3 plus NumPy is required. No GPU or autodiff framework is used.

## Frozen execution order

1. Run deterministic tests: `python3 -m unittest discover -v && python3 -m unittest review_tests review_pipeline_tests -v`.
2. Freeze all production sources, tests, protocol, design, source map, plan and red/green review logs in SOURCE_MANIFEST.json. The independent reviewer records SCIENTIFIC_REVIEW.json bound to its SHA256. Construct source.zip containing those exact files, source manifest and review. Upload to Space. Materialize that actual saved item into a separate roundtrip directory. Independently compare bytes and members. Create source_receipt.json with `capture.py receipt` using the actual saved Library identity. These receipts record actual service writes/readbacks, not self-asserted approval.
3. For r=0,1,2,3, run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 experiment.py prepare --replicate r`. Upload runs/repr/inputs/input.zip immediately, materialize and verify readback, and save its receipt as runs/repr/inputs/receipt.json. Latent sources, initial pairs, all transition uniforms, words/labels, counts, B, initial parameters, minibatch indices and RNG states are saved. Initial pairs are integer random draws, not hidden discarded uniforms.
4. For each r, in order uniform_y, uniform_B, learned_y, learned_B, run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 experiment.py fit --replicate r --condition CONDITION`. Upload runs/repr/CONDITION/output.zip immediately, materialize and verify readback, and save runs/repr/CONDITION/receipt.json before the next fit. No concurrent fits, no resume, no overwritten directories.
5. `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 analyze.py`. Immediately archive analysis/analysis.zip and verify the readback. Send all summaries, failures, and raw archives to the user.

`repr` means `rep0` through `rep3`; commands use integer r substituted explicitly. Python's argparse command parameters are fixed by protocol; they do not expose hyperparameter overrides. Do not manufacture a capture receipt for convenience. A clean independent reproduction may use its own real storage identities and receipts with this same fixed protocol.

## Retention and failure handling

Every run directory begins with STARTED.json, whose status is INCOMPLETE unless COMPLETED.json exists. The full float64 parameter, gradient, Adam first-moment and second-moment trajectories are in .npy files; unfilled entries are NaN. For each successfully committed step, arrays are flushed before a fsynced JSONL record is added. Abrupt process death can leave a step beyond the last JSONL record partially written; such a step must not be treated as committed. Exceptions retain FAILURE.txt and the complete directory, including partial arrays. SIGKILL or machine loss cannot execute Python finally handlers; on recovery, inspect and archive all available bytes before any further run. No code here retries or resumes a fit. A missing or corrupt required archive/receipt blocks later work.

All final heldout predictions and five per-example metrics are saved for the learned model, exact add-one Bayes, KT, whole-word add-one unigram, half, and empirical (J,C) table. The empirical table pools training labels from both training lengths, smooths with add-one and returns one-half for unseen cells. No test labels enter training. No test checkpoint or seed selection occurs.

Full training source and every raw archive should be retained in Space. Public-repository publication is a separately coordinated parent operation after privacy inspection; this package has no GitHub credentials or write operations. It contains only synthetic data and scientific code.
