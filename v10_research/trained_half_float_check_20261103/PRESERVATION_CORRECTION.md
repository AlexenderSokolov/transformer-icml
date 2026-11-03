# Preservation correction: trained-checkpoint audit

3 November 2026. This note supplements the existing report and manifest without changing them. It records an overwritten intermediate run; it does not supply or recreate an original artifact.

## What was overwritten

The first `check_trained.py` was written and run. Its standard output was redirected to `check_trained.log`, and the script wrote `trained_results.json`. The first run printed all six batch summaries (AB, BA, AA, BB, A, B) and an independent-forward-match line. It also wrote the complete first-run JSON. The reviewer observed the first script and log at 6,227 and 1,911 bytes, respectively.

After the initial run, the script was edited in place to add calls that print NumPy build configuration and runtime/BLAS information. It was then rerun using the same fixed words, checkpoint, thread settings and numerical calculation. Shell redirection with `>` replaced the original log, and the script's `write_text` replaced the original JSON. The edited script likewise replaced its predecessor. The currently retained script and log are 6,336 and 5,096 bytes; the current JSON is 37,390 bytes. No separate first-run copies or first-run artifact SHA-256 values were recorded in this folder before replacement. The later original-stage `SHA256SUMS` binds only the retained, second version and output, not the first run.

The complete first-run JSON, its original self-reported script hash, and the byte-for-byte first versions of the three files cannot be verified from the retained folder. The full first script was present as the shell tool-call input, and the first run's printed log was returned in the tool output, but these conversation records are not separate contemporaneous artifact files and are not a substitute for a preserved original JSON or verified artifact hashes. The first JSON was not printed in full. No claim is made about whether independent copies exist elsewhere. Reconstructing a file from later information would not make it an original.

## Conclusions and remaining evidence

The initial six-batch printed numerical summaries were recorded in the contemporaneous transcript before the script edit and rerun, including the equal trained-checkpoint A/B q and CE, the one-ULP rail difference, and the 18-ULP change in logit between the tested singleton and two-row layouts. The retained rerun's printed summaries agree with those originally displayed for these quantities and all six batch lines. This comparison does not prove that every unprinted field of the overwritten first JSON is bitwise identical to the later JSON. Whether the coordinating agent relayed the first summary to the user should be checked in its conversation; this worker sent no direct message to the user.

The retained second-run script, log, JSON and report are bound by the existing `SHA256SUMS`, which was created after the rerun. Its numerical findings remain observations of that retained run, not evidence that the initial JSON was preserved. Neither run involved random sampling, random model initialization, or training. No prior frozen-stage artifact was altered.

A separate `PRESERVATION_BINDINGS.sha256` binds this correction together with the unchanged report, existing manifest, retained script, log and JSON. It does not replace the existing manifest.
