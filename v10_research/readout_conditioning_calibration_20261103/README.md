# Fixed-half readout calibration

Read REPORT.md first. This is a bounded Q-supervised calibration at M=64, not natural robust feature learning. Count-scaled inputs pass its declared average/four-point screen, but saved models still have large held-out errors, so no uniform approximation is claimed.

The approved proposal is ../readout_conditioning_calibration_design_20261103/PROPOSAL.md. Original smoke data and reports remain unchanged.

Run `OPENBLAS_NUM_THREADS=1 python test_calibration.py` for checks and `python run.py run --output independent_replay` for a sealed replay into a new directory. Do not reseal or overwrite the original calibration_v1 run.
