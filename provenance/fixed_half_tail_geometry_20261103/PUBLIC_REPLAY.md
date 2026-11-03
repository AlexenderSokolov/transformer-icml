# Fixed-half geometry: public source identity and safe replay

This stage analyzes the frozen calibration examples and existing checkpoints. It does not train, select new examples, tune parameters, or introduce a new empirical sample. The original all-word feature argument and finite-set interpolation argument are in [ANALYSIS.md](../../v10_research/fixed_half_tail_geometry_20261103/ANALYSIS.md); the finite numerical checks do not replace those arguments.

From the repository root, use:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python provenance/fixed_half_tail_geometry_20261103/verify_public_replay.py
```

The program refuses optimized Python because the historical scientific checker uses assertions. It first verifies the current public inventory, this stage's exact source map and all 23 already-published dependencies. It copies the 20 stage files and those dependencies to a temporary directory, then runs the author's nested isolated replay, both independent numerical checks, and the retained failed probe there. It compares regenerated author results/logs and independent results/logs byte for byte. The failed probe must again raise its recorded `UnboundLocalError`; its temporary-directory traceback is not claimed byte-identical. Only the program's own temporary directories are removed. No model fitting occurs, and no historical repository file is overwritten. A different numerical environment can produce differing bytes; investigate a mismatch rather than silently updating the expected values. The recorded author environment is Python 3.12.14 and NumPy 2.3.5.

The source-bound independent LLM review is not external peer review, formal verification or a new confirmation sample. Its retained replay program has exactly four public-copy filesystem-location edits: the source directory and three output destinations now derive from the script location rather than a private host prefix. All computational statements are unchanged. A fifth line edit removes the same private prefix from the earlier failed probe's traceback. Exact original/export identities and changed regions are listed in [PUBLIC_EXPORT_RECONCILIATION.json](PUBLIC_EXPORT_RECONCILIATION.json), without disclosing removed private values.

`SOURCE_BINDINGS.json` and `REPLAY_BINDINGS.json` remain exact historical bytes. The former still binds the original failed traceback, so a naive original-hash check against that one normalized public log will not pass. The public source map supplies the explicit original/public pair; it does not claim that the two files have the same hash. The four old replay bindings and all 23 inherited dependencies still match exactly. No original seal is rewritten or weakened.

The commands printed in the historical analysis and the review replay program can overwrite their output artifacts if run directly. Prefer the verified isolated procedure above, or the narrower [author replay guide](../../v10_research/fixed_half_tail_geometry_20261103/README_REPLAY.md). All 20 stage files, including the failed diagnostic and the independent replay outputs, are retained; nothing scientific from this stage is omitted.

Notation clarification: the analysis writes terminal pairs `U=10` and `U=11` as binary strings; the JSON and independent numerical review encode the same pairs as integers `2F+G=2` and `3`. These are the same endpoints, not different cases.
