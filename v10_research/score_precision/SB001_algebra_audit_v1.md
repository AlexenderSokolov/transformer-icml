# SB001 independent LLM reviewer algebra and ledger inspection

2026-11-02. Scope: mathematical and written finite-ledger inspection of `SB001_loglog_effective_score_budget_v1.md`, with direct checks against BA001 v1 and AU001 v1. This is not execution of the emitted program, formal verification, external peer review, or root acceptance. Manuscript remains an author candidate pending root independent acceptance.

## Result

**No substantive mathematical or ledger obstruction found. Two wording corrections recommended below.**

1. The selected block is exactly `r C/J`; nonmatching triples reside in disjoint coordinates. For surviving floor mass `s=r-e`, the identity `y/r=(s/r)(floor/s)+(e/r)(discarded/e)` proves TV at most `e/r`. If the floor block is zero, `r<K/Q` covers the uniform fallback. The deterministic bound, including J=0, and its two UC/Psi integrations are valid.
2. The wholly integer bitlength schedule gives the stated precision bounds and `Psi(D_K/(LQ))<=3D_K/Q`; hence the claimed arbitrary-start statistical risk and sufficient log-log effective range follow.
3. BA001 applies separately for every finite M at a=1,b=kappa. Its explicit constants give `A<=H(2+4r)(8r sqrt(40DH)+6)^D kappa^(D+1)`. Retaining this deterioration yields the claimed log-log necessary range. Complete K^3 coordinates, local length-three features, and exact terminal-pair side data fit the stronger BA001 interface. The stationary lower transfers to the larger arbitrary-start source experiment. The K>=3 lower restriction is preserved.
4. Section 7's stationary coefficient `48K^3(K+1)` is conservative: `17+ln(1+(480/[K(K+1)])x)<=24[1+ln(1+x)]`. The residual coefficient `10D_K` follows AU001's scalar envelope with its precision variable replaced by positive real `z=kappa Q`. The beta<1/M branch is independently covered by UC. BA1 plus BA2 yields the stated mixing-dependent lower order.
5. The ledger retains every K^3 coordinate and all-token outputs, pays both singleton heads and feature gates, charges dense zero entries through K^6 map sizes, and includes selection, normalization, safe fallback denominators, cache, mask/controller/address handling, full product widths, program storage and offline generation. The conservative bounds absorb these operations. The tape evaluator and PURE alternatives are kept separate. No free count port or query-dependent value feature is used. This inspection does not certify an implemented compiler or execution trace.

## Minor recommended precision corrections

- Section 7 permits kappa in `[f,f+1]` **or within a fixed factor** and immediately asserts `(f+ln kappa)/kappa<=2`. The literal constant 2 is proved when kappa>=f. If the factor convention permits kappa<f, replace 2 by a factor-dependent O(1), or delete that extension. This does not affect the budget order.
- Qualify the final “least feasible” fixed-risk-multiplier statement: necessity holds for every fixed multiplier C, while sufficiency supplies an explicit sufficiently large K-dependent multiplier. Feasibility need not hold for an arbitrarily small prescribed C because of the full-history statistical floor.

No source or accepted manuscript was changed by this audit.

## Resolution checked

The author renamed this NEW manuscript from the provisional SP001 identifier to **SB001** to avoid collision with an older accepted artifact; this audit follows the new identifier. After the above inspection, the updated SB001 manuscript was reread at both relevant passages: Section 7 now restricts the displayed constant-2 derivation to `kappa in [f,f+1]`, and explicitly limits the feasibility statement to a sufficiently large fixed target multiplier while retaining necessity for every fixed C. Both recommendations are resolved. Final inspection verdict: **passes within the stated mathematical/ledger scope**, pending root independent acceptance.
