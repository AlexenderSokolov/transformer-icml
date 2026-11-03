# Reproduce the finite program checks

Run from this directory or repository root:

    python v10_research/finite_positional_attention_20261103/test_program.py

Python standard library only. No external writes, network, randomness without fixed seed, or third-party dependencies. The production datapath uses bit ripple addition, subtraction/comparison, mux and restoring division. Tests use separate Python exact integer/Fraction oracles, never floating-point comparisons.

RED.log records four expected assertion failures before program.py existed. RED_batch.log records the expected missing full-batch suffix failure before evaluate() was added. These are implementation-missing failures, not import errors. GREEN.log is the final full test run. The first four-test run before adding batch suffix also passed (93.874 seconds); the final run supersedes it.

Checks include: all unsigned arithmetic inputs at word widths 1 through 6; every binary observed word for M=1,...,7 at h=0,1,3,7; all twelve master numerators against independent direct-count oracles; error <=1/(2Q); endpoint and exact mask legality; full decoder at r=0,3; zero count and 511/512/513 gate threshold examples; clipping inconsistent canonical values; seeded coarse-grid master replacements at M=64,65,127,512,1027; final simplex legality; full-batch suffix equivalence. The full word enumeration comprises 1016 words, 4064 bank settings, 8128 output settings. M<64 cases test deterministic construction only, not the statistical theorem's domain.

This evaluator is not an emitted neural coefficient file and its Python timings are not neural resource measurements. CANDIDATE.md proves the circuit realization and ledger by explicit bit-gadget recipes, fixed public schedules and lifetime accounting. Finite tests diagnose implementation/indexing mistakes; they do not prove the all-path theorem or source-probability lemmas. The tests run in about two minutes in the current workspace, but no timing guarantee is part of the theorem.

CANDIDATE.md is the full statement and proof. SOURCE_BINDINGS.json pins the original accepted model and new accepted statistical theorem. The final artifact manifest excludes review files produced independently; acceptance separately binds the actual reviewed hashes.

Repository-root `python -m unittest discover` was also attempted: it found zero tests (ROOT_DISCOVERY.log), so it gives no broader regression coverage. No root pyproject.toml, pytest.ini or package.json defining a repository-wide test command was found in the initial two-level inspection. Only the explicit five-test suite above is claimed as executed substantive verification.
