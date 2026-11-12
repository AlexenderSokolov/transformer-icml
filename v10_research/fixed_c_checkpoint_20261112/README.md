# Fixed-c research checkpoint, 12 November 2026

This checkpoint records two scoped candidate results and independent internal mathematical reviews. It is not formal verification, external peer review, a novelty certificate, or a completed ICML submission.

* MEAN_FIELD_THEOREM.md: deterministic-reference approximation for bounded full-prefix causal attention with evolving keys and values on a specified stationary mixing source. It includes raw-last-row and freely disclosed terminal-pair variants, but yields only a constant-risk logarithmic-depth obstruction.
* COUNT_OBSTRUCTION.md: a depth-independent statistical obstruction for a much narrower single-read, position-free count-sufficient model. It does not cover a second evolving-bank read or arbitrary positional features.
* The two REVIEW files preserve assumptions and scope limitations.
* Run `python check_count.py` from this directory for the finite joint-count diagnostic. Exact small cases and floating larger cases are distinguished in the output. Finite diagnostics are not universal proofs.

The publication is isolated on a research branch; main is unchanged. The existing public inventory had 293 undeclared tracked files at the base commit. This checkpoint appends only its own entries and does not conceal or repair that historical mismatch. No repository-wide integrity pass, CI success, training experiment, or completed architecture upper bound is claimed.
