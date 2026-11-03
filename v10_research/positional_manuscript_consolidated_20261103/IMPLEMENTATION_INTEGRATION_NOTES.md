# Finite implementation appendix integration

## Deliverable

- File: `sections/proofs_implementation.tex`
- SHA256: `3e02a7f8b4f0169dff523b9f571701132a081e5bee453d64abffcfa3b603ee7a`
- Length: 759 lines, approximately 4,832 whitespace-delimited words.
- Main section label: `sec:implementation-proof`.
- Main theorem label: `thm:finite-realization`.
- Required external theorem labels: `thm:approximate-gate`, `thm:bank-precision`, and `thm:finite-window`.
- Bibliography keys: `BCJ001`, `WeissGoldbergYahav2021`, `MerrillSabharwal2023`, `EdelmanEtAl2024`, and `RajaramanEtAl2024`.
- No edits were made to `main.tex`, `references.bib`, or any source theorem/evaluator. No publishing or external repository writes were performed.

## Notation and scope

Output precision is `b`; `r` remains boundary-window width. The attention address width is `ell_a`, distinct from the finite-window theorem's logarithmic factor `ell`. The implementation uses `n=M+3`, `q=M+2`, `Q=2^h`, and `p=ell_a+b+h+32`. The theorem's deterministic domain is `M>=1`, `h,b>=0`; its statistical composition has `M>=64` and the supplied certificate `1/M`.

The manuscript does not include host paths, author/reviewer identities, acceptance bookkeeping, hidden notes, or internal execution details. It cites BCJ as an earlier technical construction, without claiming that the newer interface independently discovered its central precision phenomenon.

## Section and claim mapping

| Appendix part / label | Claims preserved or expanded | Bearing source |
|---|---|---|
| Opening and `sec:impl-statement` | Explicit finite hybrid semantics; theorem and exact risk constants; canonical replacement scope; old precision phenomenon acknowledged | FPA statement and sections 3, 5, 6; internal antecedent reconciliation |
| `sec:impl-prefix` | Exact causal singleton masks, synthetic token, lag identities, public half flag, twelve direct J/C/D rails, exact M-key query mask, all-word sums, nearest ties-up rounding | FPA section 1 and section 3; production `metadata` and `prefix` |
| `sec:impl-arithmetic` and `lem:impl-division` | Boolean/ReLU gates, mux, explicit full-adder recurrence, complemented subtraction, carry comparison, restoring-division invariant and no overflow | FPA section 2; production `Bits`; independent mathematical review |
| `sec:impl-extraction` and `lem:impl-extraction` | Distinct packed/scalar representations; paid scalar dyadic decode; exact grid-only ReLU extraction; retained-bit holds; h=0 and H=1 | FPA scalar-extraction amendment in section 2; production `scalar_grid_bits`; amendment review |
| `sec:impl-readout` | Four fixed row-select muxes, clipping, nine-place shift, exact gate equality, safe positive denominator, finite quotient, complementary probabilities, designated routing, b=0 and all-token execution | FPA section 2; production `readout` and `evaluate` |
| `sec:impl-cut` | Cut after rounding and before any readout fanout/extraction; cleared nonquery rails; no raw/feature/accumulator/clean-master port; logical access rather than hostile-host erasure | FPA sections 3 and 4; program return signatures; independent review |
| Theorem proof and `eq:impl-risk` | e=M eta is analysis-only scaling; direct application of approximate gate with xi=2^-b; exact endpoint selection; no count realizability assumption | FPA section 3; approximate-gate candidate statement and clipping lemma |
| `sec:impl-ledgers` | Hybrid shape distinct from evaluator work; all-token work; sparse vs dense programs and masks; actual key count; input, metadata, address, controller, holds, cleanup, output, peak and offline costs | FPA section 5 and independent resource review |
| `eq:impl-pure` | Separate fixed-schedule all-Boolean/ReLU expansion with complete state holds and T/S-dependent depth, width, parameter and runtime bounds | FPA section 5 PURE construction |
| `sec:impl-comparisons` | r=2 observation obstruction is across budgets for one map, not every-budget or architectural; stronger one-pass counter on matched input; exact-bank replication by rounding once | FPA section 6; existing finite-window theorem |
| Earlier-bank comparison | BCJ already has paid uniform positional bank and finite evaluator; direct/nearest/canonical changes matter after rounding; small explicit hybrid shape is additional implementation detail | Reconciliation sections “What BCJ001 already contains” and “FPA001 versus BCJ §§2 and 7”; attention audit |

## Small explicit implementation clarifications

These do not change the accepted theorem or its asymptotic resources.

1. The full-adder equations are written explicitly rather than referring only to standard carries.
2. Scalar query-type clearing is implemented as `ReLU(H+U-1)` for canonical `H in [0,1]` and `U in {0,1}`. This clears nonquery scalar banks before the cut without extracting the query's bits before replacement. Packed rails use bit muxes. The scalar extraction and full suffix remain charged at every token.
3. Output payload is written as `O(b+1)` packed bits, and `O((b+1)p)` scalar allocation, so the displayed bound literally includes `b=0` and numerator `2^b`.
4. Sparse PURE record-description size is bounded explicitly by `O(p(T+p)(S+p))` bits; public schedule indices fit `O(p)` bits under the stated T/S choices. The main PURE dense bounds remain the accepted ones.
5. Classical finite-output division is separately charged by `O((log M+b+1)^2)` active bitwork and `O(log M+b+1)` live bits rather than being merged into the scan-only workspace statement.

## Source hashes

| Source | SHA256 |
|---|---|
| `../finite_positional_attention_20261103/CANDIDATE.md` | `a4194b8e44eff0302d0678df0ed4cc9650a683164950f9fd87acf7e62bf1c6f9` |
| `../finite_positional_attention_20261103/program.py` | `9892df19071f4c8573f59ad9ca9bdc6f681632f7b37b335df2f906e29d0e51eb` |
| `../central_prior_art_20261103/INTERNAL_ANTECEDENT_RECONCILIATION.md` | `764c7364a5b7e03cae6afa6898a68c75e84eb9603fdabe0d1bde8904f7341a9f` |
| `../central_prior_art_20261103/ATTENTION_PRECISION_AUDIT.md` | `84c1a5d4fcf9958331c257c0cf23a13c73c5627bb6fb4f1866bc10bf1ecb6bd9` |
| `../approximate_gate_statistics_20261103/CANDIDATE.md` | `66ca3f2c092eeceb78cdafab97854580df329b28dd5b4d3bb34c28bb5a44d4ed` |

The complete production evaluator, original independent review, and scalar-amendment review were also read. BCJ's bibliographic URL is maintained in the main bibliography, not embedded as a host-path reference in the appendix.

## Checks performed

- Checked the mathematical construction against all six FPA sections and the production arithmetic, mask, prefix, replacement, readout, all-token evaluation, and scalar-extraction functions.
- Checked the internal-prior reconciliation and external attention audit; kept both the standard-mechanism context and the changed-cut qualification.
- Verified 38 unique labels, with exactly the three external theorem labels listed above. Checked that output precision was not renamed to `r` and that no host paths or acceptance/process labels entered the manuscript.
- Independently compiled the appendix in a separate temporary harness using the manuscript preamble. Final compilation succeeded (11 appendix pages), with no overfull/underfull boxes, undefined control sequence, or LaTeX error. External theorem references and bibliographic completion are checked by the complete manuscript build; the standalone harness is not a deliverable.
- Inspected all eleven standalone appendix page images. After the scalar query-clearing clarification, recompiled and inspected the changed page. No layout defect was observed.
- Replayed the existing independent extraction checker against the unchanged production program: 8,204 canonical grid cases for h=0,...,12 passed, including H=0, H=1 and h=0. The checker also confirmed pre-existing datapath AST unchanged and off-grid exclusion.
- Checked the explicit scalar query-clearing identity on 1,040 exact rational cases over h=0,...,8, both public query flags, and every canonical numerator. All passed.
- These finite checks corroborate the translation and arithmetic interfaces. They do not substitute for the all-word proof, the inherited statistical theorem, or a full newly emitted neural coefficient file. The full production suite was not rerun as part of this translation.
