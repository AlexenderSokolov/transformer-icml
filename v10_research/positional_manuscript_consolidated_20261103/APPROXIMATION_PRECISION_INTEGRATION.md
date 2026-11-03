# Approximation and fixed-bank precision appendix integration

3 November 2026 UTC. Local proof translation and exposition only. No new scientific result, source alteration, publication, commit, or external write was performed. The translation changed neither the main narrative nor the bibliography.

## Deliverables and integration

- `sections/proofs_approximate.tex`: Section `sec:approximate-proofs`, theorem `thm:approximate-gate`, clipping lemma `lem:a-clipping`, and the nearest-rounded risk bound `eq:a-rounded-risk`.
- `sections/proofs_precision.tex`: Section `sec:precision-proofs`, theorem `thm:bank-precision`, complete bounded-differences lemma `lem:p-bounded-differences`, and complete finite-law Pinsker lemma `lem:p-pinsker`.
- Include approximation after the inherited positive proofs; include precision after approximation. Both openings use the bibliography key `BCJ001` once, without the unit identifier in prose.
- The source theorem labels occur in these appendices. Main-text summaries should refer to them rather than duplicate the labels.

## Claims-to-source mapping

| New section or label | Exact accepted source portion | Content retained |
|---|---|---|
| Approximation statement and equations `eq:a-stat-error` through `eq:a-risk-critical` | ACG001 §§1 and 5 | Every M>=64, budget 0<=k<=M, all-state positive certificate, arbitrary initialization, protected endpoint, real simultaneous pathwise error e, independent coins, decoder not knowing k/beta/e, optional legal probability error xi; constants 65536, 131072, 1072176, 6433056 |
| `lem:a-clipping` | ACG001 §3 | Sequential clipping against already clipped J; noninteger and zero endpoints; no error amplification |
| `eq:a-clean-errors` through `eq:a-pathwise` | ACG001 §§3–4 | Six-per-edit coarse union bound, real Delta, thresholds 512/256/1024, ratio cases including 0<Delta<1, false-gate thresholds 1026/513, integer ceilings with max(1,ceil), J=0 coverage |
| Approximation theorem proof | ACG001 §§2 and 5; inherited positive proofs | Exact reference-only imports of `lem:occupation`, `lem:empirical`, `lem:imbalance`, and `eq:p-half-inverse` inside `prop:finite-upper`; no duplicate stochastic proofs |
| `eq:a-rounded-risk` and representation discussion | ACG001 §§5–6 | Nearest rounding gives e<=M/(2Q); constant 536088; half-log sufficient bank precision; 12(h+1) representation bits plus exact endpoint; no streaming, architecture, total precision, or learning inference |
| Fixed observation and `thm:bank-precision` | PBP001 §1 | Only separately nearest-rounded normalized J/C/D and exact endpoint; h>=0; arbitrary real probability output and independent seeds; lower 1/1600000 and upper 667160 |
| `lem:p-bounded-differences`, `lem:p-pinsker` | PBP001 §8 | Full conditional martingale/mgf proof, variance bound, log-sum proof with zero masses, binary divergence second derivative, and product KL additivity |
| Mean curves and common cell | PBP001 §§2–3 | Exact twelve means, half count normalized by M, t>=1/3, derivative minimum 1/12, at most 12Q roots, cell width 1/(104Q), gap 1/(312Q), margin 1/(3744Q), h=0 and boundary-cell cases |
| Actual bank concentration and endpoint coupling | PBP001 §§4–5 | Per-bit sensitivity 3/M, sum<=10/M, 24 exp[-M/(5*3744²Q²)], crossover 500000000, same-endpoint coupling rather than bank-endpoint independence, TV<=5/24 |
| Randomized testing and full-history floor | PBP001 §§5–6 | Common subprobability measure with arbitrary seed space, 1/(1248Q) large regime, p0=1/8, delta=1/(16sqrt(M+2)), KL<=1/28, Pinsker TV<1/4, 1/(64sqrt M) floor, all-state IID qualification |
| Regime combination and precision scope | PBP001 §§6–7 | Small regime via statistical floor, lower components need not use same pair, exact upper imported from approximation, necessary half-log precision only for the fixed bank; no noise/k lower or all-encoder inference |
| Antecedent framing in both openings | BCJ001 §§3–5 and reconciliation | Real-error gate and twelve-port precision/noise/edit phenomenon already existed; changed direct-count/clipping/nearest-rounded interface and alternative lower proof are the present scope |

## Notation and editorial decisions

- `D` is the first-half count, `Q=2^h` is the bank grid, and `b` is optional output precision. Raw-window width `r` is not reused.
- The common rounded mean bank is bold b-star, avoiding an additional Euler-font dependency.
- Rounded coordinates are described as separately rounded, not probabilistically independent.
- The concentration success event is **strictly** within rho, so a coordinate exactly at its threshold margin is not incorrectly guaranteed to retain its rounded label.
- Accepted source headers still use historical candidate wording. Their exact root acceptance receipts, not rewritten source headers, establish current accepted status.
- Diagnostic/status sections of the source candidates are represented here as verification provenance rather than article proof text. The complete mathematical proofs and scope statements are translated.

## Verification

An isolated temporary copy was built with the same preamble and all presently available inherited proof files. Missing implementation input was omitted only in that temporary copy. The new appendices compiled successfully, with no overfull boxes, duplicate labels, undefined citations, or unresolved references belonging to either new appendix. The only remaining references in that isolated build were the two main-text references to the omitted implementation appendix. The PDF author field is blank. The check used local TeX format/font caches and did not edit any source outside the two assigned appendix files and these notes.

The final whole-manuscript build, full pagination review, and implementation appendix integration are recorded separately. This preliminary translation check is not manuscript acceptance.

## Exact source hashes

- **ACG001 statement and complete perturbation proof**: `v10_research/approximate_gate_statistics_20261103/CANDIDATE.md`
  SHA256 `66ca3f2c092eeceb78cdafab97854580df329b28dd5b4d3bb34c28bb5a44d4ed`.
- **ACG001 current acceptance**: `v10_research/approximate_gate_statistics_20261103/ROOT_ACCEPTANCE.json`
  SHA256 `b6a2e5bb2438987a0d3b47f59cde37e8870254d27d74cc052c010a9f130c34c8`.
- **PBP001 statement and complete lower proof**: `v10_research/positional_bank_precision_lower_20261103/CANDIDATE.md`
  SHA256 `0a74d5e9eab9b276bc3cebe656815483d1dc22d49f138c48f310456003bcdbde`.
- **PBP001 current acceptance**: `v10_research/positional_bank_precision_lower_20261103/ROOT_ACCEPTANCE.json`
  SHA256 `7af436918247872a8e26372503005fd873b2e50171557002e8a0dde8fa3de4a1`.
- **Inherited stochastic proofs**: `v10_research/positional_manuscript_consolidated_20261103/sections/proofs_positive.tex`
  SHA256 `a629caebe01e614a71738f2036bd9016708f35871a15b6902dd98be967f69e88`.
- **Earlier real-error gate and twelve-port result**: `resumption_20261103/remote_recovery/files/v10_research/balanced_joint_finite_cut/BCJ001_theorem.md`
  SHA256 `95d5aac1ee2504955e55c1e82241c8a07d219661e2620c6e083acf5c8701554d`.
- **Internal antecedent reconciliation**: `v10_research/central_prior_art_20261103/INTERNAL_ANTECEDENT_RECONCILIATION.md`
  SHA256 `764c7364a5b7e03cae6afa6898a68c75e84eb9603fdabe0d1bde8904f7341a9f`.

## Generated appendix hashes

- `sections/proofs_approximate.tex`: SHA256 `20f22d9257acfbaa8298f549abb15fc46bb10f0a7497800009337352c3e1f860`.
- `sections/proofs_precision.tex`: SHA256 `8a92a6595e178dba09fa88801afc395b8cd3c5ee461487c26ed286685e93f95b`.
