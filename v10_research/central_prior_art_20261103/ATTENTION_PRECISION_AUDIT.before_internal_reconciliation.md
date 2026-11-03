# Attention, finite precision, and fixed-bank antecedent audit

Audit date: 2026-11-03 UTC. Targeted primary-source read, not an exhaustive literature review or a novelty certification. No external writes, contacts, or exported paper PDFs. Source reading is section-specific, recorded separately in `ATTENTION_READ_SCOPE.json`.

## Findings first

1. **The mechanism is standard/direct.** Uniform averaging of tokenwise indicators, positional selection/copying, local Boolean features, and finite arithmetic compilation are established tools. FPA001 should not claim invention of empirical-statistic attention, lag copying, or low-depth Markov prediction. Its paid zero-score masks make the realization particularly direct.
2. **The exact composite theorem was not found in the inspected original statements.** The closest Markov-attention papers represent conditional empirical distributions, with separate learning analyses or experiments. They do not state the same twelve individually rounded J/C/D coordinates plus exact endpoint, unknown bounded edits, all-state certificate, actual-terminal unsquared TV, canonical numeric replacement port, and matching fixed-bank precision lower bound.
3. **This non-match is not evidence of major novelty.** ACG001 is an extension of the project's existing half-gate proof; FPA001 composes its interface with conventional aggregation and arithmetic; PBP001 uses elementary cell counting, concentration, coupling and two-point testing. The scientifically meaningful question is whether the particular positional-information/robust-risk connection is new, not whether attention can count.
4. **Do not advertise half-log precision for a whole Transformer.** The h threshold is fractional precision of a specified normalized statistic bank. FPA001 still pays logarithmic accumulator/address information and a Boolean/ReLU computation with growing depth. Precision bounds on rounded attention weights or all floating-point operations are different statements.

## Internal statement binding

The following current local documents were read, together with ACG/PBP root acceptance receipts. Candidate headers retain historical status wording; receipts are the current admission evidence.

- FPA001 `finite_positional_attention_20261103/CANDIDATE.md`, SHA256 `a4194b8e44eff0302d0678df0ed4cc9650a683164950f9fd87acf7e62bf1c6f9`.
- ACG001 `approximate_gate_statistics_20261103/CANDIDATE.md`, SHA256 `66ca3f2c092eeceb78cdafab97854580df329b28dd5b4d3bb34c28bb5a44d4ed`; root accepted.
- PBP001 `positional_bank_precision_lower_20261103/CANDIDATE.md`, SHA256 `0a74d5e9eab9b276bc3cebe656815483d1dc22d49f138c48f310456003bcdbde`; root accepted.
- `research_direction_review_20261103/ASSESSMENT.md`.

This is an antecedent audit, not a replay or new proof certification of these units.

The comparison target is: binary order-two homogeneous sources, arbitrary initial pair law, all-state `P²(u,v) >= Pi(v)/M`, protected terminal two symbols, at most k edits in earlier symbols, one k-blind predictor, expected unsquared next-symbol TV at the actual terminal pair. FPA's only post-cut numeric observation is twelve nearest-rounded normalized row/full/half counts and the exact endpoint. Its fault changes canonical bank integers within delta, leaving arithmetic/endpoint exact. ACG gives `O(M^-1/2+k/M+2^-h+delta+2^-r)`; PBP gives clean fixed-bank minimax `Theta(max(M^-1/2,2^-h))`, not an all-encoder claim.

## Primary-source comparisons

### S1. Weiss, Goldberg and Yahav, *Thinking Like Transformers* (ICML 2021)

[Original paper](https://proceedings.mlr.press/v139/weiss21a/weiss21a.pdf). Read §§2–3 selections and Figure 3's `frac_prevs` program, plus compilation discussion. Selected aggregation is explicitly averaging; the example averages a token indicator over preceding positions. Index selection also transfers values between positions. This is a direct antecedent to indicator-frequency aggregation and positional routing. FPA's exact masks and known denominator make these operations straightforward, while its finite arithmetic and cut accounting are extra implementation obligations. The source does not state the present adversarial Markov risk or rounded-bank minimax theorem. RASP abstraction alone is not a proof of the particular finite hybrid ledger.

### S2. Merrill and Sabharwal, *A Logic for Expressing Log-Precision Transformers* (NeurIPS 2023)

[Original paper](https://papers.neurips.cc/paper_files/paper/2023/file/a48e5877c7bf86a513950ab23b360498-Paper-Conference.pdf). Read Definitions 1–2, §3 Proposition 1 and proof, Theorem 2 and its one-sided caveat. Proposition 1 concerns nearest p-bit floating-point approximation of an attention probability vector: support is bounded by `2^(2^p)`, and uniform weights vanish when `p < log log n`. Constant keys/queries are explicitly identified as a uniform-attention implementation. Theorem 2 is a logical upper bound, not a converse representability theorem. FPA accumulates integer indicators and rounds the aggregate, rather than rounding every `1/M` weight onto the h-bit bank grid. Thus Proposition 1 neither refutes its declared evaluator nor certifies an ordinary h-bit softmax implementation. No fixed-bank statistical precision lower is supplied here.

### S3. Edelman et al., *The Evolution of Statistical Induction Heads: In-Context Learning Markov Chains* (NeurIPS 2024)

[Original paper](https://papers.neurips.cc/paper_files/paper/2024/file/75b0edb869e2cd509d64d0e8ff446bc1-Paper-Conference.pdf). Read §§2.1–2.2, Proposition 2.1, Proposition 3.1 and beginning of Appendix B.1. Proposition 2.1 constructs a single-head two-layer attention-only mechanism for bigram statistics: previous-token copying followed by context matching. The task draws Markov kernels from a prior; the nearby Bayesian estimator uses transition counts. The training proposition analyzes a specified simplified model and initialization, not arbitrary learning of the present gate. This is strong prior art against treating lag-copy plus empirical transitions as new. It does not give the half-position statistic, fixed-bank h threshold, protected-endpoint adversarial minimax TV statement, or FPA's numeric fault semantics.

### S4. Rajaraman et al., *Transformers on Markov Data: Constant Depth Suffices* (NeurIPS 2024)

[Original paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8a2070082ad05b4deeff4ffb4312a6f-Paper-Conference.pdf). Read §§4–5 theorem/remark passages, Theorem 4, and corresponding construction pointers. Theorems 1–3 construct conditional empirical k-gram representations; Remark 1 states O(log T)-bit implementation with O(1/T) additive error for those constructions. Theorem 4 uses three layers, one head per layer, relative positions and layer normalization. Remark 2 explicitly acknowledges that its proof does not bound finite-bit approximation error, then suggests sufficient precision scaling. These are architecture representation results, not the same bank-observation statistical experiment. FPA cannot claim a first shallow Markov empirical estimator; conversely this source's precision remarks do not establish the twelve-rail h≈(log M)/2 risk threshold. Singleton structural masks are not interchangeable with its attention/normalization construction.

### S5. Ekbote et al., *What One Cannot, Two Can* (NeurIPS 2025)

[Original paper](https://arxiv.org/pdf/2508.07208). Read Theorems 2–3, Remark 2, proof-sketch temperature limit, Appendix D setup/Theorems 9–10, and H.3–H.4. Theorem 3 gives two layers, one head each, MLP, relative positions and normalization for conditional k-grams. Remark 2 states sufficient per-parameter precision in `Omega(log T+k)` notation with O(1/T) approximation. The construction uses a large-logit limit for matching. Appendix D freezes most components and imposes substantial source/training assumptions. H.3's noise tests are stochastic token substitutions/dynamics perturbations measured by cross-entropy, not bounded adversarial edits; H.4 is a finite quantization experiment. These do not subsume ACG/FPA/PBP. Their representation/learning claims must nevertheless be discussed when motivating any further architecture or training question.

### S6. *Counting in Small Transformers: The Delicate Interplay between Attention and Feed-Forward Layers* (arXiv 2407.11542v2)

[Original text](https://arxiv.org/html/2407.11542v2). Read §4.1.2 Proposition 4.3 and Appendix A.3. Proposition 4.3 constructs histogram solutions for linear mixing with and without softmax when feature/embedding dimensions accommodate the alphabet. Its constant mixing weights give a position-independent average; residual/FFN processing extracts a selected count. This is a particularly close one-block aggregation/readout antecedent. FPA instead has a fixed binary local-feature alphabet and uses multiple precomputed indicator coordinates, but the averaging idea is the same basic mechanism. The source's exact histogram classification and dimension conditions are not a minimax prediction-accuracy theorem for a quantized positional bank.

### S7. Zhu and Lafferty, *Quantized Minimax Estimation over Sobolev Ellipsoids* (2017/2018)

[Original preprint](https://arxiv.org/pdf/1503.07368); [journal article](https://academic.oup.com/imaiai/article/7/1/31/3865490). Read the original abstract and indexed journal §2 Example 2.2 and §4 estimate-then-quantize comparison. The latter explicitly separates estimation risk from a covering/quantization error; its Gaussian sequence example has a statistical term plus an exponentially decaying bit-budget term. Thus balancing estimation and quantization errors is established methodology. Those results concern other experiments/losses and optimized encoded estimators, not the prescribed twelve-coordinate nearest-rounded observation with retained terminal bits. They cannot be cited as the exact PBP theorem or used to replace h by the total 12(h+1)-bit payload. Direct journal opening failed; scope does not include a complete theorem/proof audit of its general lower bound.

### S8. Kato and Kato, *Handover of In-Context Learning State Across Session Boundaries* (2026 preprint)

[Original text](https://arxiv.org/html/2608.14528v1). Read §5.2 quantized sufficient statistics, Theorem 5.3 and Corollary 5.4 heading/setup. Theorem 5.3 controls Gaussian-regression posterior mean/covariance perturbations from approximate Gram/vector statistics under positive prior precision. This is an explicit statistic-quantization stability antecedent, but in a different model with a nonsingular regularized inverse. It does not supply the rare-row occupation and discontinuous half-gate analysis needed here. No claim is made about its other handover results or full proofs.

### S9. Lepage, Mary and Picard, *Markov Chain Estimation with In-Context Learning* (GRETSI 2025)

[Primary proceedings paper](https://gretsi.fr/data/colloque/pdf/2025_lepage1593.pdf); [arXiv v1](https://arxiv.org/html/2508.03934v1), submitted 2025-08-05 (verified primary metadata). Read abstract, §§3–5 and evaluation equations (7)–(9). This is an empirical first-order Markov prediction study with Dirichlet-sampled transition matrices, unseen test matrices, and comparisons against the oracle and smoothed count estimator `(c_ij+alpha)/(N_i+k alpha)`. Evaluation uses cross-entropy over the final 20 steps. Its robustness studies vary state-space size and Dirichlet parameter between training and test. The inspected four-page paper contains no bearing finite-sample minimax or quantization theorem; searches for “Theorem” and “precision” found none in the original text. Thus its actual prediction task is relevant, but its observed model/data-size thresholds and distribution-shift results do not subsume the fixed-bank adversarial unsquared-TV precision theorem. Here k denotes number of states, not edit budget. Preserve it as empirical prediction/learning context, not a matching risk-bound antecedent.

## Ingredient-by-ingredient disposition

- **Two singleton lag heads:** direct copying once structural masks are allowed. Paying masks avoids a hidden resource, but does not create a novel attention algorithm. Dense causal bounded-logit copying remains a different theorem.
- **Twelve tokenwise Boolean indicator rails:** finite truth-table/local feature construction. AND/NOT/XOR as ReLU identities on bits is elementary; this does not assert floor or exact arbitrary-real bit extraction.
- **Zero-score uniform aggregation:** direct empirical average (S1, S2, S6). No query-conditioned values or training is needed. The denominator M is public from the mask, not learned or estimated.
- **Exact accumulation then nearest rounding:** elementary deterministic error `<=2^(-h-1)`. Streaming repeated rounding is not equivalent. The h+1 numerator representation must include 1.
- **Canonical numeric fault and triangle inequality:** direct error composition. The restriction to post-rounding bank replacements is substantive; no automatic claim covers noisy endpoint, comparator, parameters, addresses or accumulators.
- **Finite Boolean/ReLU readout and scalar-grid extraction:** direct constructive arithmetic/finite-grid identities. Their ledger can be useful and necessary even without novelty in the primitives. No general neural learning claim follows.
- **ACG gate robustness:** the only stochastic bridge is inherited occupation/empirical/imbalance/reciprocal bounds plus its real-error pathwise extension. Generic smooth estimator stability does not automatically handle threshold changes or small actual-terminal counts. Its proof contribution must be assessed against the project's earlier gate argument and the separate statistical prior-art review.
- **PBP collision interval:** its mean-curve partition and common-cell argument are elementary quantizer geometry. Bounded differences, endpoint-preserving coupling, Pinsker and two-point testing are standard. The actual-bank concentration and dependent endpoint treatment prevent invalid shortcuts, but do not by themselves establish publishable novelty.
- **Matching h threshold:** algebraically balances `2^-h` with `M^-1/2`. The model-specific content is proving the upper and lower for exactly this bank, not the act of balancing exponents.

## Subsumption test and safe framing

None of S1–S9, in the bearing statements inspected, has all of: (i) this order-two source class and actual-terminal target; (ii) unknown bounded adversarial edits with protected endpoint; (iii) the precise quantized J/C/D observation and no side port; (iv) the canonical numeric-fault upper; (v) the clean matching lower for arbitrary decoders of that fixed bank. This is a scoped negative finding only. A different paper, theorem, or proof may still subsume part or all of the result; the statistical-source search is especially important.

Suggested framing: **A fully accounted finite realization and fixed-observation precision calibration for a positional robust predictor.** State the classical full/half counter comparator immediately. Present the attention prefix as a direct implementation, ACG as the statistical composition lemma, and PBP as fixed-bank calibration. Do not claim computational superiority, architecture-wide optimality, a learned mechanism, exact-gate recovery, total-precision optimality, or priority for attention-derived frequencies.

A genuine later architecture question could require dense causal masks and bounded/paid logits throughout, or analyze learning of the half-position gate under a precisely matched training distribution. Those are open directions relative to the present proof, not established gaps in the whole literature.

## Access and attribution caveats

The initially requested arXiv `2210.02671v3` HTML displayed *Transformers Can Be Expressed In First-Order Logic with Majority*, not the intended log-precision title. It was not silently treated as the target paper; the verified NeurIPS 2023 PDF supplied S2. OpenReview URLs for S2/S5 returned verification pages; no CAPTCHA was attempted. S4 HTML returned 404; S5 HTML timed out, while original PDFs were readable through the web tool. Zhu/Lafferty journal direct opening returned an inaccessible redirect; only the explicit indexed sections and preprint opening above support S7. All passages retained here are short paraphrases; no full paper files are included.
