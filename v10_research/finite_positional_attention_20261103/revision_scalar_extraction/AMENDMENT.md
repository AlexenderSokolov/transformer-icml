# Paid scalar-grid extraction amendment

Root requested this clarification after reading the initial complete candidate. Original CANDIDATE.md, program.py, test_program.py and MANIFEST.json are preserved in this directory. CANDIDATE.diff contains the exact prose change; the original nine-artifact MANIFEST.json at the parent directory is historical and unchanged.

The initial implementation uses packed numerator-word heads, where wiring the stored bits is legitimate. The amendment explicitly distinguishes that model from scalar-grid head outputs and supplies a paid ReLU scalar-to-bit conversion for the latter. The all-path induction handles H=1 and h=0, retains finite-grid restrictions, and charges thresholds, active gates/depth, held bit rails and scalar head decode within the existing resource upper bounds. No statistical statement, mask, fault radius, gate rule or nominal packed evaluator output changes.

A new test was written and failed with the expected missing-function assertion before scalar_grid_bits() was added (RED_scalar.log). The new function evaluates the stated ReLU recurrence using exact rational scalars; it uses no floor, numerator inspection or host bit extraction. GREEN_scalar.log records the targeted passing test. It checks all 1,033 canonical scalar values across h=0,...,9 against independent numerator-bit oracles. GREEN_six_tests.log records the complete revised regression suite when finished. No neural coefficient emitter or timing claim is added.

Reproduce targeted check:

    python v10_research/finite_positional_attention_20261103/test_program.py Contract.test_scalar_grid_bit_extraction

Reproduce full revised suite:

    python v10_research/finite_positional_attention_20261103/test_program.py
