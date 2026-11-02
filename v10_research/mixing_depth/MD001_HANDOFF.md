# MD001 author handoff

2026-11-02. POST-stage6 candidate; no root acceptance is implied.

Read in order:
1. `MD001_theorem.md`: exact fixed-capacity uniform-FA comparison and sharp fixed-Q-band depth theorem, both starts, both alphabet cutoffs.
2. `MD001_upper.md`: NEW binary compander purity/clipping, all-zero control, all-support arbitrary-start transfer; larger-alphabet AU transfer; paid schedule.
3. `MD001_binary_lower.md`: NEW depth-rescaled nonlinear active-Markov tube and full fixed-band inversion.

Key distinction: γ=2^L is compander gain, κ=1 is actual attention weight ratio (all logits zero), Γ_d<=C^d is lower-bound sensitivity envelope. They are three different quantities. The theorem minimizes 1+actual bounded-primitive depth; no hidden per-stage DAG, unbounded coefficient, global exact side port, or growing-width history rail is free. Explicit capacity must admit GD's K³ histogram/compander; D>=K³,r>=3 alone is insufficient.

Novel binary positive-bank bound is |v-p|<=32p via u=min(γx,sqrt(x)), u<=g<=1.5u, largest surviving coordinate x0<16y0. Zero bank separately implies J/M<6/(γQ)+18/Q². BIF full-support actual exit weights and BAI003 singleton weighted occupation close all initializations; weak β uses universal occupation. No stationary-only BU substitution is made.

The lower counts depth-independent good-message boxes only after rescaling z=Γ_dQ and shrinking the late-suffix window. No uniform growing-depth 1/Q floor is used or claimed. Both lower witnesses are stationary and thereby obstruct all-start guarantees.

Evidence: `MD001_diagnostics.py/json` PASS 90,018 scalar checks; `MD001_receipt_verification.json` confirms all exact receipt hashes, including all three GD components. `MD001_source_bindings.json` records imported exact files. These are finite corroboration, not formal verification or full network execution.

Fresh reviewer: `independent LLM reviewer`; initial review found no math blocker and requested two paid/expository clarifications, both applied. Independent final review is now PASS in `MD001_independent_review.md`, with 31,383 independent diagnostic checks passing and exact final proof hashes bound in `MD001_review_source_bindings.json`; explicit root acceptance is still required. Do not put this unit in stage6 freeze or earlier manuscripts/deliveries.

No all-Q depth frontier, sharp leading constant, optimal total storage/bitwork, shallow fixed-width PURE theorem, unconstrained rounded-network lower, external novelty, publication, upload or user contact has been performed or claimed.
