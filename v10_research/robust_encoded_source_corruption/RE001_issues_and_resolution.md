# RE001 issues and resolution

## 1. Reviewer finding: full target-scale description omitted from automatic setup ledger

The first complete candidate permitted any public rational t0 in the finite-scale schedule but the resource ledger explicitly included only b_rho. A rational t0 can have an arbitrarily long full numerator/denominator while selecting a tiny N or scalar fallback. Thus the risk and schedule algebra were correct, but the claimed finite setup cost did not yet cover all permitted t0 inputs.

Resolution: define b_t0 as the FULL numerator/denominator description length, charge target acquisition and exact scale-selection comparisons, and add b_t0 to Bp and decoder guarded lengths. For direct externally specified N without executing the target-selection rule, b_t0=0. The statistical t0 has O(log M) bits but arbitrary t0 is not assumed short. No rate or cut interface changed. The independent reviewer requested this correction before PASS; final review binds corrected bytes.

## 2. Auxiliary diagnostic scope clarification

The separately authored binary lemma diagnostic uses exact rational confidence/envelope arithmetic but includes floating radical comparisons and floating ratio summaries. It is supporting finite evidence, not a wholly exact test. The main RE001 diagnostics check corresponding radical inequalities by exact squared rational comparison. Both files are retained; no failure or mixed-arithmetic distinction is suppressed.
