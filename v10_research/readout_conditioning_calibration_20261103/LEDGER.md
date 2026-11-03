# Bounded calibration implementation ledger

- Root approved the design exactly: three initializations, fixed data/target, three parameterizations and 2,000 steps. No scientific expansion was taken.
- Tests first failed because calibration.py did not exist. This red run drew no data.
- Implemented code/config were sealed before unit-test initialization draws and calibration data sampling.
- Six tests passed; independent literal teacher/feature decoder and matched initial predictions were verified before all nine fits.
- All nine fits completed and stopped. No positive criterion was adjusted after inspecting results.
- Saved 18,000 step diagnostics, 36 checkpoints and complete final predictions/targets.
- Root-requested post-hoc tail inspection found errors above 0.4 despite small mean KL. This uses retained predictions only, does not change fitted models or selection, and is explicit in REPORT.md.
- Author final checks verified all sealed/upstream files, output hashes and recomputed metrics. Original smoke delivery hashes remain unchanged.
- Root owns independent replay and scientific acceptance; no publication or external write occurred.
