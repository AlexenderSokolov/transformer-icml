# Scoped PreLN components checkpoint

12 November 2026. Incremental research evidence, not a completed predictor, novelty certificate, formal proof artifact, or submission-ready result.

This directory contains a genuine paired-lane residual PreLN amplifier, its fixed-number persistent signed-lane extension, and a two-block endpoint gadget WITH mandatory final full LayerNorm. The endpoint gadget assumes a supplied estimator-logit/padding representation; construction of that representation is not free. The amplifier assumes externally supplied bounded predecessor-indicator score biases, not a proven fixed-width positional dot-product implementation.

Run `python check_endpoint.py` here. `endpoint_results.json` records 360 clean and 1440 noisy floating-point cases, independently rerun with identical output. The test covers the endpoint component only, not upstream estimation or a trained/end-to-end system.

Read REVIEW.md and RESOURCE_SCOPE.md before combining these components. Superseded no-final-LN drafts are deliberately not published here. Some source documents mention separate earlier work which is not a claimed dependency closure in this checkpoint.

This branch extends the fixed-c checkpoint without moving main or the previous research branches. Existing inventory rows are preserved and only new files appended. The known 293-file undeclared historical inventory gap is not repaired. No CI or repository-wide integrity success is claimed.
