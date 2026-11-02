# SB001: targeted comparison for the log-log effective-score budget

Checked 2026-11-02. **Decision:** no same-setting theorem was located in this bounded search. The amplified histogram architecture has a particularly close, explicit predecessor; the statistical score/grid frontier is not stated in the inspected sources. This is neither novelty certification nor a proof audit.

## 1. Scope and immediate positioning

Compared `score_precision/SB001_loglog_effective_score_budget_v2.md` (SHA-256 `d10086be4d358e322872daffad4dd10572588d6dcffaecbffefc409df6a217b7`), after reading `bounded_attention_family_comparison.md` and `precision_frontier_followup.md`. The candidate changes the finite evaluator: actual cached weights are `{1,kappa}`, not rounded evaluations of an old exponential routine. It retains a complete bounded K³-coordinate triple bank, rounds each coordinate before unrestricted decoding, and measures expected TV for an unknown second-order source at its actual terminal context. At Q comparable to sqrt(M), it asserts necessary and sufficient **order** log log M for effective range log(kappa), in a fixed-dimensional, fixed-locality one-global-summary family. Its optional beta refinement concerns the same restricted family and a specified statistical target multiplier.

Do not position the result as inventing one-hot histograms, conditional empirical counts, two-level attention, normalization inversion, or logarithmic precision requirements. The plausible contribution to retain, subject to independent proof acceptance, is their finite-grid, same-trajectory statistical combination, including a growing-range family lower with explicit dependence on the weight ratio.

## 2. Closest explicit construction: inventory counting with two weight levels

**Behrens, Biggio, Zdeborová, _Counting in Small Transformers: The Delicate Interplay between Attention and Feed-Forward Layers_.** Inspected [arXiv v3, 20 May 2025](https://arxiv.org/html/2407.11542v3), §2; §4.1.2; Appendix B.3.2–B.3.3, Proposition B.1, Eqs. (25)–(30). [Published ICML 2025 record](https://proceedings.mlr.press/v267/behrens25a.html).

Their orthogonal inventory construction uses equal-token logits 1 and unequal-token logits 0. Equation (26) therefore has unnormalized weights `{1,e}` and denominator `L+(e−1)k`. Equation (28) exposes selected mass `ek/[L+(e−1)k]` plus the residual; Eq. (30) inverts it. Proposition B.1 gives a histogram solution when embedding and hidden dimensions cover the alphabet. Section 2 explicitly assumes infinite-precision operations. Appendix C.3 separately increases inverse temperature to suppress interference for nonorthogonal embeddings.

**Comparison:** this directly precedes SB001's two-level weighted inventory and rational mass, rather than merely sharing the word attention. It does not impose SB001's post-summary grid, estimate conditional transition laws, integrate rare terminal-context occupation, or state a log-log score frontier. Their `p` denotes hidden width, not grid bits. The candidate's grouping by context and renormalizing a successor sub-block is an elementary extension of inventory representation, not by itself a new counting mechanism.

## 3. Other primary near-neighbors

### A. Histogram and count inversion are established primitives

**Yehudai et al., _When Can Transformers Count to n?_** [arXiv v3, 25 February 2026](https://arxiv.org/html/2407.15160v3), §§3.1–3.2, 4.1 Theorem 4.1, 4.2 Proposition 4.3/Lemma 4.4, Appendix B.

Theorem 4.1 presents a one-layer one-head histogram construction when dimension covers the vocabulary. Section 4.2 instead describes query-based attention followed by inversion of a normalized count statistic; its stated construction uses log(n)-scaled logits and an O(n)-width MLP. The task is exact query counting, not stochastic transition estimation. Section 3.1 declares finite-p-bit calculations but does not give SB001's per-coordinate-cut/statistical-risk tradeoff.

**Caution:** §4.1 describes uniform softmax aggregation as an unnormalized sum; ordinary softmax produces the average. Thus this passage is evidence of the histogram idea, not a directly reusable finite-arithmetic implementation certificate. No external theorem was independently validated here. Behrens's displayed normalized formulas above are the cleaner direct construction comparison.

### B. Conditional n-gram attention predates this candidate

**Rajaraman et al., _Transformers on Markov Data: Constant Depth Suffices_.** [arXiv v1, 25 July 2024](https://arxiv.org/html/2407.17686v1), Theorems 4.1/4.4/4.5, Remark 4.2; Appendix A.1 Eqs. (20)–(23); Remark 5.2.

Appendix A.1 concentrates attention on matching contexts by sending its scale parameter to infinity, then averages successor one-hots to obtain the conditional empirical law. Remark 4.2 states O(log T)-bit implementation with O(1/T) additive error for the attention-only constructions; Remark 5.2 does not bound finite-precision error for the layer-normalized construction.

**Comparison:** this establishes the conditional-count target and induction-head architecture, not a necessity for log-length effective range at statistical accuracy. Its scale symbol kappa is not SB001's actual integer weight ratio. Suppressing all nonmatches in successor-only coordinates and retaining all context–successor coordinates before decoding are different interfaces. The previous bounded-family note already covers their representation lower; it was not resurveyed here.

### C. A real log-log precision theorem, but not a score-range theorem

**Merrill–Sabharwal, _A Logic for Expressing Log-Precision Transformers_.** [arXiv v6, 6 November 2023](https://arxiv.org/html/2210.02671v6), §3 Proposition 1 and proof; §4 Theorem 2.

Proposition 1 bounds nonzero entries after nearest-p-bit-floating-point approximation of an attention probability vector by `2^(2^p)`. If `p<log log n`, uniform probabilities `1/n` all round to zero. The proof uses the smallest positive representable float. This is an exponent-range/underflow obstruction for storing individual normalized attention weights.

**Comparison:** a search hit saying log-log attention precision is not SB001. SB001 can use zero effective logit range for uniform attention while exact integer numerators/denominators still require growing arithmetic widths. Its final coordinate grid is another quantity. In particular, do not describe effective score range `ln kappa` as total floating precision or bits needed to represent logits. Proposition 1 neither supplies nor refutes the proposed statistical log-log range lower.

### D. Modern hardmax-to-softmax conversion still addresses a different accuracy target

**Brösamle–Eckstein, _The Expressive Power of Low Precision Softmax Transformers with (Summarized) Chain-of-Thought_.** [arXiv v1, 18 May 2026](https://arxiv.org/html/2605.18079v1), §4, Theorem 4.2, Appendix D Lemma D.3 and §D.5.1.

Section 4 gives softmax–hardmax l1 error at most `2n exp(−gap)`. Theorem 4.2 combines rounded softmax with added denoising MLPs, O(log log horizon) attention exponent bits, and query/key scaling; §D.5.1 takes `c²/sqrt(d_k)=log(96N)`. Depth and width grow logarithmically in the relevant horizon.

**Comparison:** exponent bits and projection scaling are not effective logit range. This is exact token simulation through hardmax approximation, not a fixed-dimensional one-block statistical summary. The standard bound explains log-length score separation for worst-case hard selection; it does not imply that the same separation is necessary for estimating a conditional law to its sampling-noise level.

### E. Recent counting norm/precision analysis: useful but not the desired frontier

**Shaffy et al., _Counting with Attention and LayerNorm: Norm Scaling and Representation Geometry_.** [arXiv v1, 12 October 2026](https://arxiv.org/html/2610.16653v1), §3; Appendix C.2 Proposition 2; Appendix G Propositions 8–10.

Their main minimal model has identity Q/K/V, no feed-forward layer, and linear regression readout; it counts one symbol with worst-input error. Proposition 2 bounds error by constant multiples of `L²/(L+gamma)`, where `gamma=exp(c_BOS−c_symbol)`. Exact counting after rounding consequently needs large saturation scale. Appendix G distinguishes shrinking representation gaps, classifier margins, perturbation bounds, and storage of parameters interpreted in exact arithmetic.

**Comparison:** a relevant score/readout/precision tradeoff, but not post-grid arbitrary decoding of conditional distributions. Values/readout norms can grow; counting every integer with error below 1/2 is not expected terminal TV at order M^(−1/2). Its classification alternative also shows why collapsing continuous margins alone do not prove information loss. This is a recent preprint, not treated as externally validated.

### F. Trigger-conditional averaging is not conditional probability estimation

**Ran-Milo, _Attention Sinks Are Provably Necessary in Softmax Transformers: Evidence from Trigger-Conditional Tasks_.** [arXiv v1, 12 March 2026](https://arxiv.org/html/2603.11487v1), §§3.2–3.5, Theorems 1–3.

The task returns a content average when a trigger appears and zero otherwise. Theorem 1 fixes length and dimension and proves concentration on BOS at nontrigger positions as task error becomes sufficiently small. Its model outputs projected attention averages, rather than an arbitrary decoder after a finite-grid summary.

**Comparison:** no Markov law, quantized statistical cut, or explicit horizon/score/precision frontier is supplied. The word conditional here refers to a trigger, not estimation of a conditional empirical distribution. This near-neighbor was checked and set aside.

## 4. Standard deductions versus load-bearing work

The following is our mathematical comparison of the local candidate, not a theorem attributed to any external paper.

1. **Standard representation move.** At kappa=1, SB001 is simply uniform attention over the complete triple histogram followed by conditional block normalization. Its occupation-based beta profile does not require a new counting mechanism; amplification changes the pre-grid rare-row mass. Treat a local tuple as a categorical feature, retain a complete orthogonal inventory, and use a query to select a block. Nonmatching categories then occupy other coordinates instead of contaminating the desired conditional composition. Multiplying every item in one block by the same positive factor preserves its normalized composition. No new statistical theorem is needed for that identity.
2. **Standard deterministic conditioning inequality.** If a nonnegative block has mass r and coordinatewise grid loss below 1/Q, renormalization error is bounded by a constant times `min(1,1/(Qr))` at fixed block size. The all-zero branch must be included. For the two-level bank, `r=kappa J/[M+(kappa−1)J]`; hence amplification reduces the small-denominator grid error. A rational mass of this form is explicitly present in the closest prior construction.
3. **Where statistical content enters.** Replacing a worst-history lower bound on r by integration over the occupation count J at the *actual terminal query* is essential. Obtaining a harmonic envelope, including arbitrary starts and optional mixing promises, cannot be inferred from a histogram or a hardmax-approximation theorem. The earlier precision note already identifies waiting/harmonic and quantization precedents; these are not first-of-their-kind tools.
4. **Why log-log arises once those bounds exist.** A grid term of order `log(kappa Q)/(kappa Q)` at `Q~sqrt(M)` is reduced to sampling order by `kappa~log(M)`; taking the logarithm of the weight ratio then gives log log M. Likewise, a family lower `log(M)/(kappa^(D+1)sqrt(M))` forces that effective-range order. These final substitutions are elementary, not independently new principles.
5. **The lower's remaining load-bearing obligation.** The complete allowed summary and side information must obey a suitable good-message bound, uniformly as kappa grows. Tracking a polynomial deterioration in kappa is essential; a fixed-range theorem with unspecified constants cannot be reused with a growing kappa. None of the inspected sources gives that complete-message result for this stochastic experiment.
6. **Mixing refinement.** No inspected theorem states the proposed `1+range ~ 1+ln(1+ln(1+Q/[M max(beta,1/M)]))` frontier. Its substantive burden is the occupation bound and the quantitative family lower. Inverting those expressions after they are established is routine. This pass does not establish novelty of the occupation lemmas or approve the candidate's proof.

## 5. Recommended wording and stopping boundary

“Using an established weighted-inventory representation, we analyze the effective-score range needed to preserve statistical prediction accuracy through a specified coordinate grid. For fixed alphabet, dimension and locality, at square-root grid resolution, the resulting one-summary-block comparison has matching log-log order in effective range. The construction and lower bound concern a declared finite information cut, not general transformer optimality or total arithmetic precision.”

The full triple bank has K³ coordinates, unlike the old SRC linear-in-K scalar bank. A fixed-K risk comparison does not show equal K-dependent feature, memory, parameter, or arithmetic costs.

Keep the optional beta result explicitly family-restricted and constant-qualified. Do not claim matching kappa, all-Q optimality, universal architectural lower bounds, a fixed-total-precision implementation, training success, or computational improvement.

**Search/evidence boundary:** focused generic searches covered softmax log-log precision, score range, conditional counts, histogram attention, and amplification. No private proof text, witness tables or unpublished exact formulas were sent to search; formulas in this local note come from already retrieved public sources or local analysis. Primary model/theorem/construction sections were inspected for A–F and Behrens. Existing Hahn/Chiang and statistical-quantization comparisons were reused rather than repeated. A search hit for an older Markov log-log risk result was not treated as a score theorem; its attempted arXiv HTML retrieval returned cache miss and was not used as new evidence. No access denial, contact, publication, account change, or external upload occurred.

The negative finding is bounded: these checked sources do not state the same result. Unsearched papers and alternate formulations may do so. The required decision is now supported: cite the weighted-inventory ancestor prominently; isolate finite-cut statistical stability and the uniform growing-range lower as the candidate's substantive steps; do not advertise a novel histogram mechanism. Broader novelty certification is outside this unit.
