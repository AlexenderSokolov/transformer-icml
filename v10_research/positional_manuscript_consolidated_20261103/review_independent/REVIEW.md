# Independent scientific and integration review

Date: 3 November 2026. Review type: a separate LLM scientific/editorial audit, not formal verification, external peer review, or priority certification.

## Decision and binding

The complete manuscript and all six proof appendices have been read. No unresolved mathematical or scope blocker was found. The central result is coherently stated as an observation-dependent, same-map budget-adaptation theorem. The finite implementation and fixed-bank precision results are correctly subordinate calibrations, not architecture-wide claims.

This decision applies only to the exact final scientific source hashes in `FINAL_BINDINGS.json`. It also depends on the fresh verification outputs `checks.json` and `build_check.json`; their source lists must match those bindings. The rendered PDF's identity is recorded there, but page-image inspection is separately owned by the author's separate visual review. This reviewer independently rebuilt the complete source in a clean temporary directory and checked the final compiler log.

The only integration defect found by this review was an appendix label mismatch: the main implementation section referred to `sec:implementation-proof`, while the appendix initially used `sec:implementation`. The author corrected it. The final reference check must have no unresolved or duplicate labels. Two additional editorial clarifications were checked: `separately round` rather than `independently round`, and removal of the duplicate November date in the BCJ bibliography entry. None changes a theorem.

No author or historical mathematical source was edited by this reviewer. Only files in this review directory were created or changed.

The three inherited core proof files are byte-identical to their original source copies, with these SHA256 hashes:

- `proofs_positive.tex`: `a629caebe01e614a71738f2036bd9016708f35871a15b6902dd98be967f69e88`.
- `proofs_negative.tex`: `c33000a5e7b98eb395d8ccae7c104b60d4cf7d30900607d64f4102c9bf9302c7`.
- `proofs_finite_horizon.tex`: `5ce65ec56017f2581e06681bb90848afc0a8987c44022663b4866667f84e3639`.

## Complete reading scope

Read in full: the original finite manuscript's model and main statements, its positive, negative, and finite-horizon appendices; the consolidated `main.tex`, `implementation_main.tex`, and all six consolidated proof appendices; the ACG001, PBP001, and FPA001 candidate statements and proofs; the current finite implementation program and test program; the claim ledger and source-binding records; the central statistical/attention prior-art reports and read-scope records; the internal-antecedent reconciliation; and the research-direction reassessment.

The recovered BCJ001 theorem, AB001 joint-blindness obstruction, and AF001 full-history domain classification were also read in full. Exact original/public pairs were checked against both recovery maps, rather than treating matching filenames as proof of identity. Primary external sources were read only to the scopes recorded in `CITATION_AUDIT.md`; this review does not imply that every external proof was independently checked.

## 1. Central model and finite-window theorem

### Quantifiers and experiment

The model fixes binary order-two homogeneous sources, with the induced four-state pair kernel. The supplied certificate is exactly `1/M`, not necessarily the largest coefficient for that source. The minorization is all-state, including rows outside stationary support. Source parameters and the initial law are hidden. Upper guarantees allow arbitrary initial laws; lower witnesses may be stationary. This distinction is retained throughout the main statement and proofs.

The kernel is a single source-independent map on full words, with at most `k` changes on every input/output in its support. It protects both terminal symbols, does not receive the hidden source or predictor seed, and can use a predeclared public auxiliary family. The lower kernel is explicitly defined beyond its favorable event, so legality is not only in expectation or on the null source. The target remains the actual protected terminal pair. Neither an independent query nor conditioning the departures on the observed row is substituted.

The observation is exact triple counts plus specified raw prefix/suffix windows. Overlap is allowed. The upper uses only the suffix. At width `r`, the exposed departure count is `r-2`, capped at half the trajectory, not `r-1`. A full-word scan and a computed message are separately defined, and are not granted to the restricted-window estimator.

The finite competitive factor takes one map at a fixed `(M,r)` and compares it across all budgets. The sequence criterion permits the map family to depend on the prescribed width sequence, but not on the budget. The known-budget minimax scale is justified for the same information and for full history. The paper correctly does not turn a clean/attacked same-map tradeoff into a logarithmic lower bound at each fixed budget. No attainment of an infimum is assumed.

### Upper proof

The four-state occupation and empirical-row bounds are proved rather than supplied by an unjustified conditional-IID argument. The row-stack argument is compatible with the selected terminal row. The support classification, weighted hitting estimate, first-hit/return identity, endpoint-tail calculation, and imbalance bound cover initial states outside stationary support. The old-prefix reciprocal bound truncates a harmonic range after enlarging the balance event to an old visit. The enlarged event is used only analytically: the implemented gate still requires a positive fraction of older visits.

The strict edit bound changes a count by at most `6k`, including overlapping affected triples and a split crossing. Deterministic gate cases charge false status to small occupation, and empirical error, reciprocal occupation, and weighted imbalance are then averaged. The exact protected pair makes the selected row common to clean and corrupted histories. The known-budget count-only comparator is separated from the budget-blind gate.

### Lower proof and all-horizon closure

The marked-skeleton occupation mixture, exact relocation preserving triple counts and both windows, word-mass comparison, rejection kernel, and loss ordering were read in full. The transformation hardcodes a public comparison family and uses no oracle for the realized source. Matched observations are established before same-map risk transfer. The endpoint and final transition are retained rather than replaced by independent data.

The finite-horizon appendix explicitly handles small logarithmic factor by the oracle floor and large factor by a legal auxiliary budget, so the claim is for every `M >= 64`, not merely an asymptotic subsequence. The elementary parameter inequalities and constants were checked analytically, with additional exact/rational and high-precision finite diagnostics in `check.py`. The positive-liminf criterion permits nonmonotone widths and absorbs a finite prefix of horizons. The separate fixed-fraction proof retains its stated order of limits and stronger constant.

### One-bit distinction

The extra bit is produced by a whole-word scanner using exact positional counts and the protected query, not by a one-bit-memory raw streaming device. Its alphabet-size-two minimality is relative to the fault-free counts-plus-message interface. The manuscript explicitly separates message size from scan work, counters, and storage. The explicit pair of equal-histogram/equal-endpoint words was independently checked, including the differing half-gate bit.

## 2. Approximate direct-count interface

The approximate coordinates are direct `J,C,D` values, where the half count has denominator `M`. Sequential clipping of total, successor, and half coordinates preserves the coordinate-error bound, even if the upper endpoint changes or the total becomes zero. No assumption that the approximate or replaced bank is the count table of any word is used.

The real perturbation radius is `Delta = 6k + e`. The ratio step handles both `J >= 2 Delta` and smaller positive `J`, including noninteger arbitrarily small `Delta`. Equality accepts at the actual gate. The analytic thresholds `1/1024` and `1/256` are separated from the implemented `1/512` gate. False status entails the strict small-count thresholds `1026 Delta` and `513 Delta`; the integer occupation lemma is applied with `max(1, ceiling(...))`. This also covers `J=0` and `Delta=0` without evaluating a zero-denominator ratio.

The inherited stochastic lemmas are exactly referenced and suffice for arbitrary starts. The coefficient identity `8*130944 + 16*(1026+513) = 1072176`, the edit coefficient `6433056`, and the nearest-rounding coefficient `536088` check. Independent seeds and coordinate dependence are treated correctly: the accuracy premise is simultaneous pathwise and does not require independent coordinate errors. The decoder itself is blind to the bound `e`, the budget, and the certificate.

Nearest rounding has error `M/(2Q)`, unlike the older floored bank. The output error is separately `xi`; finite output precision `b`, bank precision `h`, and raw-window width `r` are not conflated. The error guarantee controls prediction risk, not exact recovery of a discontinuous gate bit.

## 3. Precision lower bound for the fixed bank

The observation contains exactly the twelve nearest-rounded direct coordinates, the exact endpoint, and source-independent metadata. The lower bound permits arbitrary computational power, real-valued probability outputs, and randomized decoders. It excludes hidden residuals, raw history, other token banks, and advice correlated with source or history. It is not an arbitrary-encoder bit lower bound.

On stationary IID Bernoulli parameters in `[1/8,1/4]`, all twelve mean curves are monotone and have derivative magnitude at least `1/12`, including the half-count normalization for odd `M`. At most `12Q` threshold crossings yield a common-cell interval of length at least `1/(104Q)`. The selected parameters are separated by at least `1/(312Q)` and have margin at least `1/(3744Q)` from every threshold. The endpoint-interval argument handles thresholds outside the curve's range without extrapolating derivative bounds. It includes `Q=1` and any fixed nearest-tie rule.

A raw bit changes a count by at most three, so bounded differences applies to the original independent symbols despite overlapping triples. The joint bank/endpoint law is compared to a constant bank retaining its actual endpoint, then endpoint laws are coupled. No independence of endpoint and bank is claimed. Decoder randomization cannot defeat the resulting total-variation two-point bound. The all-history two-point bound fills the complementary `M` versus `Q^2` regime. The in-appendix bounded-differences and Pinsker proofs were read and checked, not merely named.

Both explicit lower components and their conservative combined constant check. The upper constant `667160 = 131072 + 536088` follows from the approximate interface. The scale `h = (1/2) log_2 M + O(1)` concerns fractional grid bits in this prescribed bank. It says nothing about network-wide accumulator, address, weight, or score precision. The clean lower does not establish matching noise/edit lower terms for the new replacement port; the manuscript says so.

## 4. Finite implementation and resource accounting

The construction is defined on every binary word for `M >= 1`, while its statistical use requires `M >= 64` and the stated source experiment. Two zero-score singleton-mask heads acquire lag-one and lag-two bits. At token `i+2`, the local rails form the correct row, designated successor, and half-prefix indicators. A synthetic query at `M+2` averages exactly departure keys `2,...,M+1`; the same copy layer acquires the actual protected terminal pair.

The masks are structural causal exclusions, not finite large negative logits or a claim about unrestricted dense causal attention. Dense and sparse resource columns are complete alternative implementations of those masks; their best entries cannot be mixed. Uniform attention probabilities are not individually rounded before summation. Exact integer accumulation and one final nearest rounding implement `floor((2QS+L)/(2L))`, with sufficient word widths. This is why the aggregate construction is not contradicted by claims about individually rounded attention weights.

The numeric fault port jointly replaces the canonical master numerators only after rounding. Every downstream duplicate is made after replacement; other history, residuals, raw registers and nonquery banks are cleared from the cut. Endpoints, metadata, masks, addresses, comparators, and subsequent arithmetic remain exact. Off-grid analog noise, register corruption, and message-bit faults are distinct excluded experiments.

Finite comparison/clipping and restoring division produce a legal binary distribution. Empty rows, gate equality, numerator `Q`, exact ratio one, and `h=b=0` are explicitly treated. Scalar-to-bit extraction is paid and valid only on the canonical finite grid: multiplying by `Q` gives an integer, and the pair of ReLUs extracts each binary threshold bit exactly. It is not claimed valid for arbitrary real-valued noisy coordinates.

All-token suffix evaluation, live-wire holds, code storage, structural masks, addressing, input storage, zero coefficients in dense circuits, and cleanup are counted. The small two-layer/three-head description is a hybrid attention plus exact finite arithmetic description. The pure Boolean/ReLU unrolling is separately charged with larger depth and width; the two guarantees are not merged. The conservative scalar allocation is consistent with the peak-memory bounds. The classical one-pass positional counter is explicitly simpler and has the same statistical interface, with input storage and output division counted separately.

The actual `program.py` and its tests were read in full. Independent oracles recompute counts and finite readout outputs without calling the program's counting/decoder helpers. Further diagnostics cover arbitrary canonical faults, extraction, equality boundaries, and instrumented all-token execution. These tests support implementation consistency; they do not replace the all-word circuit proof or certify runtime asymptotics experimentally.

## 5. Antecedent chronology and claim discipline

BCJ001, accepted on 2 November 2026, already contains a real-error half-gate argument, a twelve-coordinate finite precision/noise/edit result, and paid sequential/PURE implementations. A stale candidate-style header does not undo its later acceptance receipt. The consolidated abstract, related work, and appendix openings do not claim that ACG/PBP discovered these phenomena.

The changed interface matters. BCJ uses eight floored successor coordinates plus four half counts, reconstructs row totals, and places analog perturbation before final floor/projection. The new interface directly nearest-rounds four triples `J,C,D` and FPA uses canonical post-rounding replacement. Unquantized linear equivalence does not identify separately quantized experiments. The rederivations and fresh lower proof are therefore appropriate, but are not a fresh general precision principle. FPA's additional deliverable is the explicit local lag-copy hybrid shape and complete ledger, not the first finite evaluator.

AB001 already closes the particular obstruction to simultaneous budget/certificate blindness. AF001 already classifies the supplied-certificate full-history domain. They are not silently converted into new open questions or into impossibility of prediction at zero certificate. They need not be inserted into the focused proof chain, but their companion provenance distinction must remain visible. The exact AF original/public pair is recorded in `checks.json`; the mathematical source is not silently rewritten.

Original and public-export bytes are not conflated. Three BCJ companion pairs and the AF source pair were verified independently against both `SOURCE_MAP.json` and `BINDING_RECONCILIATION.json`, including actual public-export file hashes. Recovered public review bytes are not described as restored original review bytes. The BCJ mathematical theorem itself matches its original receipt exactly.

## 6. Bibliography and editorial scope

All new bibliography records were checked against primary venue/arXiv records for exact author list, title, year, and cited version. The anonymous article has no invented author identity. The relevant citation sentences remain within the source-read scopes recorded separately. In particular, generic robust selection is not dismissed merely because the target depends on the observation; Markov prediction papers are distinguished by their precise experiment/loss/source class; and established shallow counting/induction constructions are acknowledged. The text contains no accusation that an external paper is incorrect and no claim of exhaustive novelty certification.

The public technical-note link is a fixed source revision, not a publication or peer-review credential. No external communications, public writes, or source-PDF redistribution were performed by this reviewer.

## 7. Verification artifacts and limits

`check.py` performs fresh exact source identity/reference checks and finite diagnostics. `checks.json` records counts and source hashes. `build_check.sh` makes a clean-directory build; `build_check.json` and the final compiler log record its outcome. `FINAL_BINDINGS.json` binds final scientific sources, comparison sources, final PDF, ledgers, freeze, and review evidence.

Publication scope: `build_check_transcript.txt` and `build_check_final.log` are local-only evidence and must be excluded from the public package. Although temporary-workspace paths were replaced, those logs retain machine-specific system-package paths. Their hashes are retained separately in the binding record; their contents are not public deliverables. The public `build_check.json` reports the successful final build and exact scientific input hashes without host paths. No scientific source, test, or build result changed in making this publication-scope distinction.

Finite diagnostics include all short words, specified larger horizons, arbitrary canonical readout banks, all grid numerators through `h=10`, gate boundary values, clipped real perturbations, the explicit word collision, all raw-window widths over a finite range, and very large integer-domain witnesses. They are falsification/consistency tests, not an exhaustive all-horizon proof, formal proof assistant output, or external peer review.

The recorded successful diagnostic counts are: 31,073 finite upper-domain pairs; 39 large-horizon lower-domain cases; 816 direct-bank cases; 2,448 exact readouts; 2,460 arbitrary canonical-fault readouts; 2,058 scalar-grid extractions; five instrumented all-token runs; and 13,635 rational perturbation configurations, each tested at three target probabilities. All 33 source-input bindings and 11 claim bindings are checked, as are the four AB/AF companion source/receipt bindings. The first draft of the reviewer-only perturbation diagnostic accidentally allowed Python integer division to become a floating-point value after clipping; it was corrected to exact rational division before reporting success. No manuscript defect was inferred from that test-code error.

The exact-source decision should be reopened if any mathematical source, observation definition, fault lifecycle, cost ledger, or substantive related-work sentence changes. Pure bibliography/layout edits may be rebound after reviewing their diff and repeating build/reference checks.
