# Execution plan

Implement in a new self-contained directory; do not edit archived sources.

1. Write deterministic tests before implementation: literal triple counts and future-label exclusion; source simulation from supplied nonrandom uniforms; exact finite-prior mass/posterior identity for tiny horizons; pool/token equivalence; initial matching; finite-difference gradients; one-step Adam arithmetic; clipping/KL boundaries; receipt mismatch refusal.
2. Implement core.py (data, statistics, forward/backward and optimizer), experiment.py (one replicate preparation, one fit, final evaluation), capture.py (immutable manifests, ZIPs, roundtrip receipts), and analyze.py (all predeclared summaries). Do not run experimental data generation or training.
3. Independently inspect code/protocol and run deterministic tests, archive the actual red/green test logs. Freeze the final bytes, upload source ZIP to Space and independently compare the downloaded bytes. This is the only current deliverable.
4. After the technical capture check passes, use fixed commands from README.md. Generate and immediately preserve one input bundle; verify roundtrip; fit one condition; immediately preserve outputs; verify roundtrip before the next fit. Continue the frozen 4×4 plan with no human approval interposed.
5. Run final analysis after all 16 result captures are verified. Report all outcomes and limitations. Preserve analysis sources and outputs immediately. Stop; any broader experiment is a separately versioned design.

Review focus: label leakage; same-source/fresh-source confusion; shared data versus independent replicates; teacher-target masquerading as natural training; incorrect model/softmax derivative; mismatch between frozen manifests and receipt; falsely successful capture after interrupted writes; missing original random draws; overwriting outputs; selecting successful checkpoints or seeds.
