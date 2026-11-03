# Reproduce the bounded empirical stage

These are exploratory finite experiments, not universal robustness tests. The reports and additive review clarifications govern interpretation.

## Prepare an isolated copy

First run `python tools/public_verify.py` from the published repository. Then run:

    python provenance/empirical_position_20261103/prepare_public_replay.py /tmp/empirical-position-replay

Choose a nonexistent destination outside the repository. Optimized Python (-O or PYTHONOPTIMIZE) is explicitly rejected before filesystem changes, so integrity checks cannot silently be disabled. The helper verifies all 141 selected public files against their exact source map and active inventory, copies them, and preserves the original pilot seal as `PRE_RUN_HASHES.historical.json`. It replaces only the working seal's `PLAN.md` hash with its explicitly declared public-export hash. This is necessary because two non-scientific process sentences were normalized in the public plan. No code, protocol, seeds, optimizer, data or scientific constraints change. Every other original sealed hash must still match. The preparation receipt names the exact substitution; it is not a new preregistration or trusted timestamp. The repository and original frozen files are never modified.

## Run the sealed author experiments

In the isolated copy:

    cd v10_research/learned_position_pilot_20261103
    OPENBLAS_NUM_THREADS=1 python test_pilot.py
    python run.py run --output independent_replay

For calibration, from the isolated copy's root:

    cd v10_research/readout_conditioning_calibration_20261103
    OPENBLAS_NUM_THREADS=1 python test_calibration.py
    python run.py run --output independent_replay

Both runners refuse an existing output directory. Do not run `seal` or alter any other input. The source seeds and sampling order reproduce complete runs; timing and environment metadata need not match. Final saved models contain weights, not full Adam state, so arbitrary mid-step continuation requires rebuilding optimizer history. Successful preparation alone is not a scientific rerun.

## Inspect retained failures and original review programs

The public pilot retains all synthetic evaluation paths, per-trajectory metrics/proposal choices and five final models. The calibration retains all frozen words/targets/minibatches, all final predictions and nine final models. These support inspection of individual failures, overlap and final forward predictions, rather than only favorable averages.

All original pilot and calibration records are now included: 25 pilot and 36 calibration checkpoints, full aggregate and per-condition/per-fit update CSVs, every original artifact-manifest entry, numerical datasets and individual predictions. Only duplicate independent/root replay outputs and caches are omitted; their exact identities and reproduction boundaries are in `OMISSIONS_AND_REPLAY.json`.

The unchanged pilot independent checker loads `independent_replay` at startup. Reproduce that run as above before invoking its checker; original final models and trajectory arrays are present. The unchanged calibration checker has all 36 original checkpoints and all 53 original output-hash entries and can audit those original numerical outputs directly in the isolated copy. Its optional independent-run comparison specifically expects `review_independent/replay`, not the author command’s `independent_replay` directory; it is skipped unless the expected directory and final predictions exist. Populate that exact location only with a separately regenerated run whose provenance is recorded if that comparison is desired.

When auditing newly regenerated outputs rather than the retained original outputs, distinguish their newly generated manifest from the original historical manifest. Preserve and report environment/timing or other metadata differences instead of modifying original historical evidence. The bounded public integrity check verifies current exported identities and does not substitute for a rerun of the scientific review.
