# PGT001 local candidate

Read CANDIDATE.md for the theorem, full proof and limitations. SOURCE_BINDINGS.json pins inspected sources and local artifacts. checks.json contains reproducible diagnostic output.

Run from the workspace root:

    python v10_research/positional_gate_training_20261103/check.py

The checker uses standard-library exact fractions and installed mpmath at 80 decimal digits. It checks 2,044 small words and exact posterior masses, 21,844 word/edit-mask pairs, actual-word J=0 and 512D=J boundary cases at theorem horizons, integer layer-cake thresholds, exact derivative identities, high-precision derivatives and uniform bounds, and two short full-population runs at M=6. That M=6 run is explicitly outside the M>=64 theorem domain and only diagnoses scalar dynamics arithmetic. No Monte Carlo training, asymptotic rate fitting, neural experiment or worst-case test simulation is performed. The stochastic source bounds and minimax lower theorem are imported, not proved by these diagnostics.

Status: candidate pending independent review and root acceptance. No external writes and no frozen manuscript changes.
