# FOC001 repaired-interface review and final recommendation

2026-11-02. Same independent reviewer as `REVIEW.md`. **PASS for the corrected FOC001 common-experiment corollary**, subject to subsequent root acceptance. Candidate SHA256: `bf2e37f684a02e3e40b0d4674b0e10e472fee6d3d7a76fe494c5801de96a26fd`.

The original REVISION REQUIRED finding remains intact in `REVIEW.md`, bound to its original candidate. I read the complete repaired candidate and actual combined repair diff, then read the final one-line g-definition diff. I independently verified that the preserved original before-file is byte-identical to the initial bound candidate, that the combined diff is the actual original-to-final diff, and that all inherited source/review/receipt bytes remain unchanged. `verify_repair.py` and `repair_verification.json` record these checks.

## Resolved findings

1. The common experiment now explicitly allows arbitrary hidden initial pair laws. It does not silently narrow to ordinary first-order symbol starts.
2. The predictor discards X0 and applies FOU001 to N=M transitions of X1,...,X_(M+1). These are genuine homogeneous first-order transitions for every conditional initial X1 law.
3. For each fixed clean X0=b, the induced suffix kernel is a map on every suffix input, obtained by running the original kernel on (b,w) and projecting the output. It is source-independent, strict-k, and terminal-protected. Dependence of the original attack on X0 is thus permitted, not ignored. Conditional FOU bounds can be averaged because the actual suffix predictor is identical for both b values and never receives clean b.
4. The compressed sufficient observation is now explicitly the suffix pair counts and suffix exact half-gate bit, plus actual terminal symbol. No claim of reconstructing those counts from the unaugmented original histogram is made.
5. The final version restores the explicit definition `g_M(k)=max(M^(-1/2),k/M)`. The normalization comparison and constant remain correct: 1024+2^20<=2^21 and g_M<=H2 on 0<=k<=M.
6. The actual initial-pair counterexample and correction are preserved transparently in the candidate and before/diff history. No accepted theorem is edited or retroactively strengthened.

The other interfaces retain the findings in the initial review: exact symbol/pair target equality; no budget/certificate/table oracle input; first-order upper valid across reducible and periodic tables; AB001 negative in the same full-history protected-pair experiment with stationary witnesses; genuinely second-order clean alternatives and first-order null; correct same-map joint-blindness quantifiers; no beta-informed, unknown-order, exact-minimax, noisy-bit, neural, or novelty extension.

## Verification and scope

The supplemental finite checks were rerun successfully after the repair. Their output deliberately retains the historical label `WITH_INITIAL_INTERFACE_BLOCKER`, referring to the original counterexample rather than an outstanding corrected-candidate failure. The final repair verification passes. An initial run of the repair verifier used a too-specific textual spelling `M^-1/2`; the candidate correctly spells it `M^(-1/2)`. That local test assertion was corrected and rerun; it was not a mathematical failure or source change.

`final_bindings.json` binds final candidate, inherited dependencies, all repair-history files, and review/check artifacts. This is independent local LLM mathematical/interface review plus finite diagnostics, not formal verification, external peer review, scientific novelty certification, publication approval, or acceptance of FOT002/other candidates. No external writes were performed. Root acceptance remains a separate step.
