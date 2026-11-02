# SB001 handoff

2026-11-02. Author candidate frozen for root review; NOT root-accepted.

## Results

- Complete query-independent K³ triple bank plus exact-pair weight amplification κ gives deterministic error relative to original add-one <=K/(J+K)+min(1,K(K+1)M/[κQ(J+K)])+(2K-1)/Q.
- Universal terminal occupation yields numerical Ψ(K^5/(M+1))+Ψ(K^5(K+1)/(κQ))+(2K-1)/Q.
- Entirely integer κ=bitlength(M+1), Q=2^ceil(bitlength(M+1)/2) (h>=4) attains O_K(M^-1/2) for arbitrary starts, uniformly all β. Effective natural-logit range is O(loglog M), improving GW001's sufficient O(log M).
- BA001's explicit finite constants give A<=C_(D,r)κ^(D+1); at Q≈sqrt M and β=0 any fixed risk multiplier requires lnκ>=lnln M/(D+1)-O(1). Matching ORDER only, for fixed local single-block family, K>=3 lower, K>=2 upper.
- AU001 mixture generalizes the upper to [1+ln(1+κQ/(Mβ₀))]/(κQ). With β-promise-selected κ≈f=1+ln(1+Q/(Mβ₀)), the matching score-budget order is 1+lnκ≈1+ln f. External β-dependent budget selection is explicitly separate from the paid integer-input program.

Full all-token finite costs include local feature gates, both singleton heads, dense K^6 projections, entire K³ bank, selection/normalization/rounding, masks/controllers/cache, exact full-width products, offline/program storage, peak sums, tape evaluator and separate PURE alternatives.

## Evidence

`check_sb001.py` ran successfully after final naming: 2,096 enumerated histories, 33,536 exact rational map cases, 7,938 nonempty selected blocks whose Q-floors all vanish. Integer schedule, Psi envelope and BA constant checks passed. This is mathematical-map testing, NOT emitted-network execution.

`SB001_algebra_audit_v1.md` records independent LLM reviewer inspection of proof, constants, inclusion and ledger. Two minor wording recommendations were resolved (literal constant-2 schedule requires κ>=f; sufficiency is for sufficiently large fixed risk multiplier). Root independent acceptance remains pending.

## Identifier reconciliation

The provisional NEW manuscript name SP001 collided with an older accepted stationary_precision/SP001 theorem. Before freezing, all NEW score_precision filenames, theorem labels and references were renamed SB001. The unrelated old SP001 was not edited. This was identifier hygiene, not mathematical failure.

## Files

- `SB001_loglog_effective_score_budget_v1.md`: complete theorem/construction/proofs/ledger.
- `SB001_source_bindings_v1.json`: SHA-256 of four directly read sources.
- `SB001_algebra_audit_v1.md`: scoped independent LLM reviewer audit.
- `check_sb001.py`, `SB001_diagnostics_v1.json`: reproducible finite checks/results.
- `SB001_freeze_manifest_v1.json`: hashes of the above and this handoff.

No publication or contact occurred. No external literature-priority investigation, full compiler implementation, formal proof verification or physical-noise analysis was performed.
