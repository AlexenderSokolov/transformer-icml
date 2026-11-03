# Safe isolated replay

The commands in `ANALYSIS.md` were written before this replay clarification. Running them directly would overwrite the historical `RESULTS.json`, `run.log`, and `verify.log` in this folder. **Do not run those commands in the original workspace.** Use the isolated procedure below instead.

From the workspace root, run:

    bash v10_research/fixed_half_tail_geometry_20261103/replay_verify.sh

The script copies only the analysis scripts, their imported calibration/pilot source, the two frozen arrays, and the twelve existing scaled checkpoints into a fresh temporary directory. It runs the original commands there with `OPENBLAS_NUM_THREADS=1`, compares each regenerated artifact byte for byte with the historical one, and deletes only its own temporary directory on exit. It never trains a model or writes to the original analysis or calibration directories. Output hashes and pass/fail messages go to standard output; to retain a separate log, redirect to a **new filename**, not any historical file. The previously recorded Python and NumPy versions are in `SOURCE_BINDINGS.json`; a different numerical environment may lead to differing bytes despite numerically equivalent results, so a failed byte comparison should be investigated rather than presumed to mean a scientific error.

`replay_verification.log` records this isolated replay on the original authoring environment. `REPLAY_BINDINGS.json` binds this clarification, script, verification log, and the original source bindings without changing the latter. The underlying analysis and historical results are unchanged.
