# Next-Symbol Prediction from Adversarially Corrupted Markov Trajectories

An English companion manuscript on **full corrupted-history statistical prediction**, separate from the immutable 70-page `manuscript_v5` on internal information cuts.

## Main conclusions

For fixed alphabet size, protected true terminal-pair risk is of order
`min(1,max(M^-1/2,(k/M)[1+log(1+1/(k e_K))]))`, with the corruption term zero at `k=0`. The cutoff is `e_2=max(sqrt(beta),1/M)` for binary sources and `e_K=max(beta,1/M)` for `K>=3`. Both stationary and arbitrary initialization are covered. The binary upper uses public `k` but not `beta`; the larger-alphabet add-one upper uses neither. Strict-budget common-kernel lower witnesses account for the whole word, with hidden seed and mask.

Allowing edits to the endpoint while retaining the **true original hidden terminal target** changes the rate to `min(1,max(M^-1/2,k/M,(1-beta)1{k>=1}))`. One endpoint edit can prevent consistency even for a known source.

A new elementary scalar corollary in the main text gives protected statistical-order tolerable budget of order `sqrt(M)/[1+log(1+1/(e_K sqrt(M)))]`, with separate sufficiency/necessity constants and explicit integer/zero-budget treatment.

## Scientific boundary

Scientific freeze: **2026-11-02 09:22:25.495805 UTC**, exact `delivery_stage8/SCIENTIFIC_FREEZE.json`. Adopted units: SC001 (main and stationary extension), SC002, SC003, BT001 (obstruction, witness and conditional reduction only), BT002 (main and exact scalar completion), EP001. Later explorations are excluded.

New arguments are embedded in the manuscript. R011 clean prediction and IU001, AU001, BIF001, BAI003-v2 occupation interfaces are explicitly identified with their domains; their full original proofs and reviews remain in the predecessor dossier. This is not a claim to rederive that entire foundational chain. BT001's stronger interior constant-step transport remains unproved and is not a premise of the proved rate. No efficient attack sampler, causal/visible-mask equivalence, neural depth, training result or certified novelty is claimed. Independent LLM reviews and finite diagnostics are not formal verification or external peer review.

## Files

- `corrupted_trajectories.tex`: main narrative, experiment, theorems, budget corollary and provenance.
- `nonbinary_endpoint.tex`: complete larger-alphabet and endpoint proofs.
- `binary.tex`: binary upper, obstruction/witness, entropy transport and complete lower.
- `references.bib`, `corrupted_trajectories.bbl`, `corrupted_trajectories.pdf`.
- `build.sh`: local pdfLaTeX/BibTeX build with writable format/font caches; `--render` renders all pages.
- `SOURCE_MANIFEST.json`: exact adopted sources, receipts and inherited interface bindings.
- `PRESERVATION_BINDINGS.json`: pre-authoring immutable predecessor and stage7 baseline.
- `make_manifest.py`: verifies all freeze and accepted-proof hashes, rebuilds source bindings.
- `check_tolerance.py/json`: finite corroboration of the new scalar corollary, not proof.
- `QA_VERIFICATION.json`: clean rebuild, reference/layout checks and preservation results (generated after verification).

Rebuild from this directory with `bash build.sh --render`. The three TeX source files and bibliography are the complete editable source set; external proof files are not needed to compile. The full predecessor dossier remains necessary to inspect the explicitly inherited proofs. Nothing has been uploaded, submitted or sent externally.
