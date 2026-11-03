# Learned positional pooling smoke

Read REPORT.md for actual results and limitations. This is a one-seed exploratory numerical pilot with no minimax or general learning guarantee and no independent acceptance yet.

Run `OPENBLAS_NUM_THREADS=1 python test_pilot.py` for the nine tests. Run `python run.py run --output independent_replay` for a full isolated replay; the output directory must not already exist. Sealed inputs are checked before every run. No external services or additional packages are required beyond NumPy.

The original run is smoke_v1/. Its full evaluation paths, trajectory metrics, checkpoints and hashes are retained. Do not overwrite the sealed protocol or original run.
