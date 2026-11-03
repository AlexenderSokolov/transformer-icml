# Retained numeric records: archival consistency scope

Date: 2026-11-03. This is a read-only audit of saved records and source text, not a research replay, independent theorem proof, external peer review, novelty certification, or numerical implementation certification. No archived script was executed or imported. No new scientific cases, words, chains, models, samples, or outputs were generated. All three numeric source files are preserved byte for byte. The accompanying safety tests operate only on new temporary copies and deterministic corruptions.

## Exact retained evidence

Paths below are relative to the public repository root.

- `v10_research/route_a_sensitivity_bottleneck_20261103_1341/population_cases.jsonl`: 90 rows, 11,178 bytes, SHA-256 `6a89efdd610420214e3c6de2ae692f082adf2f39f9ebcaee8c6d3d9fcd1f7f9f`.
- `v10_research/route_a_sensitivity_bottleneck_20261103_1341/reverse_moment_cases.jsonl`: 8 rows, 67,949 bytes, SHA-256 `b64dddf28c60588694bb7e3523873954ec04eaf19edd7bca55e6460bd8d4090a`.
- `v10_research/route_a_bos_causal_compile_20261103_1411/exhaustive_cases_v1.jsonl`: 1,008 rows, 420,366 bytes, SHA-256 `c19d158dcc74d415dca0a08606fcf570fb539fd2a63bf8b0e18ecfa508da1f1a`.

The 1,106 rows occupy 499,493 bytes. Counts, input domains, and fields agree with the retained scripts and logs under static inspection. That is not a claim that this audit reran or witnessed those historical executions.

### Population file

The saved input grid is u in {1/16, 1/8, 3/16}, gamma in {0, 1/2, 1, 3, 9}, and Lq in {0, 1/2, 1, 2, 5, 20}. Every row contains exactly `u, gamma, Lq, lambda, loss_minus, loss_plus, population_opt`, all canonical rational strings. The archived script evaluates an ideal clipped population comparator at two endpoints, not a random finite-prefix experiment or a finite network implementation.

The new checker validates the saved lambda relation, the saved positive-part population formula, equal saved endpoint losses, and their ranges. It does not regenerate the comparator's predictions. The exact-real division and clipping in the source do not establish a practical finite-word implementation or a finite-ReLU/depth theorem. These 90 cases do not prove the source's general sensitivity, stochastic moment, or architecture claims.

### Reverse-moment file

The saved input grid is m in {512, 768}, u in {1/8, 3/16}, and t in {1/4, 3/4}. Fields are exactly `m, u, t, mean_r, var_r, mean_J, var_J, all_bounds`. The last field is a JSON boolean and m is an integer. All other values are canonical rational strings. The longest rational string has 3,561 characters.

The archived program describes exact-Fraction reverse-chain dynamic programming from terminal 00, with r counting reverse states Y0 through Y(m-1), and J counting Y1 through Ym. The saved file contains final scalar moments only, not its transition matrix or intermediate P/M/V arrays.

The new checker checks only the saved parameter domains, canonical values, nonnegative variances, mean ranges, and these saved-field inequalities: v=mu >=60; |mean_r-2(1-u)/3| <=16/m; var_r <=61/m; |mean_J-v| <=15; var_J <=61(v+15). It also requires the saved all_bounds flag to be true. It does not advance or reconstruct a chain, recompute moments, or establish that the saved moments arose from the claimed process. Full-byte identity is the separate authenticity boundary.

### No-BOS file

Saved keys cover N=3,...,8, eta in {1/4,1/32}, and every binary input word in the corresponding historical finite domain. The existing 1,008 saved keys are read and their ordered digest checked; the new checker does not enumerate a word space.

Every row has exactly these 16 fields: `schema, N, bits, eta, b, c, terminal, J, C, copy_max_error, gates_exact, head_output, add_one, absolute_error, contamination_bound, passed`. Rational values use canonical integer numerator/positive-denominator objects. The source schema identifier is `no_bos_all_words_v1`.

The saved integer b and c are score-budget exponents. They are not arrays of actual per-position or per-edge logits. The file stores a maximum copy error, one aggregate gate flag, one final head output, one comparator, an error and a bound. It does **not** contain full internal execution traces: no per-position Q/K/V vectors, raw or centered logits, attention weights, individual gate preactivations or hinges, tokenwise gate arrays, or per-head port-output arrays are retained.

The original verification addendum's wording about full cases and logits must be read with this distinction. The separate `trace_preservation_and_r011_addendum_v1.html` (SHA-256 `8939b513ddc373ab810ebc20ba6e63f45998da76e452ad161d116abc38030538`) explicitly preserves this limitation. Deterministic code and inputs might support a separately authorized new run, but such a run would not recover a historical execution trace. No such run occurred in this audit; the clarification requires independent pre-run schema review before a further run.

The new checker verifies N/word length and terminal suffix, bounded integer counts and score budgets, canonical rationals, saved add-one/count equality, saved final-output/error equality, saved contamination formula, and the stored error/budget inequalities. It requires true gate and pass flags. It deliberately does not recompute J/C from words, lag-copy attention, gate computations, head outputs, or any internal trace. Passing therefore checks consistency of what was retained, not correctness of an execution that was not logged in full.

## Arithmetic and mathematical boundaries

Static inspection of `exhaustive_no_bos_v1.py` shows exact rational powers-of-two weights and normalization. The source's specialized backend maps a finite logit category set to stored powers of two. It is not exact exponentiation of its dyadic approximation to ln(2), not a generic exponential implementation, and not ordinary floating-point softmax. The JSONL does not store a dyadic s parameter, its preprocessing, p or p_out, or output-rounding traces. The deterministic cases consequently do not validate the analytical dyadic-real-softmax perturbation argument, preprocessing cost, balanced rational-circuit depth, bit-operation ledger, or practical fixed-word behavior.

The sensitivity lower is confined to a common q/r/h-only decoder under stated coordinate sensitivity and seed assumptions. It is not a lower bound for unrestricted Transformers, residual bypasses, other heads, or direct raw-history counting. A seed independent of the entire path under each source and with the same law, or identical conditional seed laws after terminal conditioning, is required; common marginal seed laws alone are insufficient. Exact-real two-endpoint upper comparators do not establish a complete-t-interval or finite-precision matching upper.

The no-BOS construction still uses public position features and a designated first position. Its resource ledger is a deliberately loose mathematical upper estimate, not measured memory or runtime. The source explicitly includes the classical streaming add-one comparator and does not claim an efficiency improvement. The retained primary-source audits report antecedents rather than strict novelty. This audit did not reopen the cited external papers.

## Source and review chronology

- The family-aware single-head candidate and zero-history wording correction are bound by `independent_single_head_review_20261103_131631_2/REVIEW.txt`. Its separate terminal-only addendum review also binds the terminal-pair-only baseline clarification. These are scoped analytic reviews; no numerical Route B records are present in this selection.
- `independent_sensitivity_review_v1.html` binds `report_source.txt` and identifies the seed-conditioning gap. The original report and initial randomized clarification must not be read without `seed_independence_correction_v1.html` or corrected v2. The separate v2 verification binds both text versions, rendered v2, and the seed correction, and describes a change/rendering check rather than a full new proof review.
- The three-port upper review checks the finite-sample endpoint upper under the v2 hypotheses. The same-port addenda review binds the rare-boundary addendum and same-port upper. Older phrases saying review was pending are preserved historical text, not grounds to erase the later scoped review. None supplies a finite-network implementation or external novelty clearance.
- BOS v1's insufficient dyadic copy-margin choice is explicitly corrected in BOS v2. No-BOS v3 removes the added BOS token and separately charges rounding. No-BOS v4 adds preprocessing accounting and source qualifications. The independent no-BOS review primarily binds v3 (SHA-256 `2f22e818205b8f80f13794feedc6bc8ea3dcd782cc2541968f9038acc3e19592`); its explicit section 6 additionally gives a focused v4 preprocessing/source-caveat check (v4 SHA-256 `79e81b718fbb89990d4a679fbd6fd5f1aec30a65e29ac8ddb9fb43cca5afec3a`). This is not a blanket independent implementation replay of v4.
- The trace/R011 clarification identifies the same-path estimator by relabeling R011 indices, and distinguishes unconditional actual-terminal average risk from conditional-00 risk. It does not establish a new unconditional add-one rate or re-audit all inherited R011 dependencies.

All reviewed-artifact hashes whose targets are present in this frozen selection match their original frozen pre-export bytes. These are not necessarily the hashes of normalized public copies. `SOURCE_EXPORT_MAP.json` in the enclosing provenance stage maps original identities to public-export identities; historical review hashes remain bound to the originals. In particular, rendered sensitivity v2 is `c887f7e0aae192a3705c450fa7ef69811c600d9d6dda886109bca3084efd6e06`, same-port upper is `dca483b9dcba84d415b9b4ad23229d8082348154a07022a4c14d92363729a0a5`, and the seed correction is `494b8765739c72f8e6200bf3f0f3eb59c1b14932453135a96c2957d261afff7a`. No source/review mismatch was found among these selected targets.

References to earlier research are not made self-contained by these 46 selected files. The no-BOS review cites `route_a_terminal_report_v3.html` with SHA-256 `2f6030e99b4bc0ae4c6f3c20958a0d690d03c860653236aa898b86a2cc0dad17`; that file is outside this selection. The later clarification cites `R011_global_rates_and_constant_adaptation_v1.md` with SHA-256 `aaafd3823ab11e20ffdeff2164115c6c91db5efea6e2dffd9c3c78da0b7fbbbf`, also outside this selection. Route B additionally references earlier FOT003, BCJ001, and source audits outside the selection. These references are dependency boundaries, not discovered hash mismatches. This audit neither reconstructs their missing histories nor claims completeness of the historical research record. An enclosing archive may separately bind inherited public files.

## New verifier and tests

`verify_records(root)` is stdlib-only and reads only the three fixed public-relative paths. POSIX descriptor-relative opens reject symlinks in every root/path component and reject non-regular inputs. Files are bounded at 512 KiB; JSONL lines at 16 KiB; per-file rows at 1,100; rational integer strings at 2,048 digits. Duplicate JSON keys, floats/nonfinite numbers, malformed UTF-8/JSON, unexpected fields, noncanonical rationals, unsafe paths, oversized inputs and changed-during-read files are rejected. Explicit checks remain active under `-O`; scientific assertions do not rely on Python `assert`.

Ordered-key hashes bind saved-key coverage and order. They do not authenticate unchanged numeric results. The returned observed content SHA-256 values must be matched by the enclosing archive's independently pinned byte manifest. The parent archive verifier, not this numeric module, owns source maps and full-file identity checks.

Fresh normal and optimized runs each accepted the same 90+8+1,008 rows and emitted identical validation reports. The 34 safety tests passed under both `python -I -B` and `python -I -B -O`. Tests cover omitted/duplicate/reordered keys; corrupted saved equalities/bounds/status; type and schema errors; noncanonical/oversized rationals; duplicate keys, nonfinite/floating values, malformed/deep JSON and UTF-8; blank/truncated lines; oversized files; missing files; root/directory/file symlinks; unsafe relative paths; and a FIFO without blocking. The accepted baseline test also verifies all copied source bytes are unchanged after checking. These are verifier safety tests, not new scientific experiments.
