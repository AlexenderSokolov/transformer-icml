# v10 central bridge: targeted primary-source comparison

**Checked 2026-11-02. Bottom line:** the defensible target is not that transformers count, reconstruct counts from normalized statistics, smooth, or select among statistical estimators. The candidate value is a *fully costed finite-computation bridge to the exact same terminal-prediction minimax experiment*, followed by a matched-resource statement explaining when changing the representation improves prediction. The present bridge, if its remaining implementation obligations pass, is a constructive upper bound—not a trained-learnability theorem or an attention computational advantage.

This is a targeted comparison, not an exhaustive survey or a certification of novelty. Statements below were checked in primary paper bodies/proofs, not inferred from abstracts or missing search hits. The papers' mathematical proofs were not independently re-proved here. Private v10 material was read locally; only generic literature queries and public paper URLs were sent externally.

## 1. Fixed comparison target

The inherited v10 experiment observes the full history, uses its first M observed departures, and predicts the next symbol at the actual terminal pair. The source is a fixed unknown homogeneous order-two table, with arbitrary initial pair law and possible zero transitions. Loss is unconditional same-trajectory expected TV. The inherited R011 selector is the same deterministic, mixing-parameter-blind algorithm for all classes D₂(β).

The new candidate would reconstruct only the queried row count vector C and pooled count vector H from declared finite attention ports, then implement R011's guard with exact integer comparisons and a probability-grid readout. Its statistics, precision, permitted local masks, input access, retained coordinates, FF circuitry, and output rounding must all be charged. This description is an **internal candidate**, not an accepted new theorem.

**Internal attribution matters too:** count snapping and exact-count margins are already in the inherited `sources/earlier/runtime/v10/stage2-flow-heads/evidence/root-proof-v1.md`, §6 (with its linked count-snap proofs). That section gives charged integer snapping and common-grid equality of D3-snap/B-C-snap/B-J-snap when their margins hold, including Q≥256M. Rediscovering this mechanism is source recovery, not a new local result. The current work must identify its genuinely additional bridge—especially the inherited R011 selector, pooled counts, and exact guard—rather than claim the snapping idea anew.

Notation below follows each paper: k is Markov order, S is vocabulary size, T is context length. These are not v10's K,M. An “order-k conditional k-gram” in these papers uses k predecessors; terminology differs from an n-gram counting both context and successor.

## 2. Nearest papers and actual scope

### A. Rajaraman et al., *Transformers on Markov Data: Constant Depth Suffices* (2024)

In arXiv v1, Theorem 4.4 represents the conditional k-gram using two attention-only layers, k heads, and dimension (k+2)S+k+1. Remark 4.2 asserts O(log T)-bit implementations with O(1/T) additive error for the attention-only constructions. Theorem 5.1 gives three layers, one head, dimension O(S), RPE and layer normalization; its proof concentrates attention by increasing logit scale. Crucially, Remark 5.2 says that this proof does **not** bound finite-precision error; it suggests sufficient precision of order log T+k (printed using Ω notation). Theorem 6.1 says a one-layer model computing conditional 3-grams on ternary strings within 1/(3T) must satisfy 2pH+dp+2≥T/3. This is a worst-input representation lower bound, not terminal expected-TV minimax. Training evidence is empirical, separate from these constructions. [Primary body, §§4–6 and appendices](https://arxiv.org/html/2407.17686v1)

**Implication:** neither shallow empirical Markov prediction nor logarithmic-precision representability is a new target by itself. A fully explicit arithmetic/error analysis can still strengthen the exact resource statement, but cannot be advertised as the first finite-precision Markov transformer.

### B. Ekbote et al., *What One Cannot, Two Can* (NeurIPS 2025; arXiv v2)

Theorem 3 gives two layers, one head each, dimension 6S+3, RPE, MLPs and layer normalization for conditional k-grams. Remark 2 reports 9(6S+3)²+(6S+3)(2T+2S+9) parameters and sufficient precision of order log T+k, with O(1/T) error (again printed Ω). The constructive proof uses a hard-attention/logit-scale limit; Appendix A.1 explicitly changes layer normalization to implement v/||v||₂.

Theorem 4 is genuinely a training theorem, but **only for a reduced first-order model**: train positional scalars then one second-layer attention scalar; assume the MLP already supplies its correct representation; omit/reintroduce normalization by stage; impose positive-transition, non-degeneracy and constant-mean prior assumptions. For T+1≥poly(γ⁻¹,S), it gives prior-averaged excess loss ≲log(T+1)/(T+1)^(cγ). It is not training the full higher-order construction from generic initialization. [Primary PDF, Theorems 3–4, pp. 7–10; Appendix A.1](https://arxiv.org/pdf/2508.07208v2)

**Implication:** v10 should not compete on minimum layer count. Its hand-written decoder does not inherit this optimization theorem.

### C. Zhou, Tian and Diggavi, *An Information-Theoretic Approach to Understanding Transformers' In-Context Learning of Variable-Order Markov Chains* (AISTATS 2026)

Theorems 3–5 construct D+2 layers for CTW on maximum-order-D context trees under the specified Bayesian tree/Dirichlet prior. Theorem 4 collects forward and backward normalized statistics. Appendix G.2.2, Eq. (38), already reconstructs a count through

    n[i,s_l](a) = i · g[i,s_l](a) · product_{j=0}^{l-1} g_backward[i-1,s_j](x[i-j]).

Theorem 5 computes Bayesian mixing weights and the next-token vector. The proof takes c→∞ for the attention selection and invokes a sufficiently wide FF approximator for count-dependent functions/readout. Thus the abstract's “exactly implement CTW” must not be read as an explicit bounded-score, every-operation-rounded, finite-cost theorem. Two-layer approximate blending and successful training are supported experimentally; the construction is not a gradient-learning theorem. [Published record](https://proceedings.mlr.press/v300/zhou26b.html), [primary v3, §4.4 and Appendix G](https://arxiv.org/html/2410.05493v3)

**Implication:** restoring evidence magnitude from normalized attention and then blending models is direct prior art. Distinction must reside in the exact finite implementation, source/loss quantifiers, and proven cost or stability consequences.

### D. D'Angelo et al., *Induction Heads Interpolate N-Grams* (ICML 2026)

Proposition 3.1 constructs a disentangled two-layer model, k first-layer heads and one second-layer head, with estimator

    [exp(κ)/S + sum_A exp(sum_{r in A} β_r) N_A(a)]
      / [exp(κ) + sum_A exp(sum_{r in A} β_r) N_A].

Here A is the exact match mask; exp(κ) is absent without BOS. Lemma 4.1/Corollary 4.2 rewrite it as data-dependent mixtures of partial-context estimators. Corollary 4.1 recovers add-α smoothing as β→∞ with κ=kβ+log(αS). Importantly, finite β concerns **global context matching**: §3.2.1 takes δ^(1)→∞ for exact local copying; §3.2.2 also sends early-position suppression to infinity. No all-operations finite-precision theorem follows. Appendix E proves label-symmetry preservation/constraints under gradient flow, not convergence to the desired estimator; trained agreement is empirical. [Primary PDF, Proposition 3.1, §§3.2–4, Appendix E](https://arxiv.org/pdf/2607.02800v1)

**Implication:** the direct soft-mixture identity, smoothing interpretation, and partial-context interpolation cannot carry novelty. Exact finite-score inversion can be a different computational mechanism, but its local binding and extra ports must be included.

### E. Chen, Sheen, Wang and Yang, *Unveiling Induction Heads* (2024)

Theorem 3.6 establishes three-stage **population gradient flow** in a specialized two-layer model: train polynomial FF feature coefficients, then first-layer RPE, then the second-layer attention scale. Assumptions 3.3/3.5 require a lag-aligned initialization gap, initial scale a=O(L^(-3/2)), uniformly positive kernel entries ≥γ, and a primitive lifted chain with uniform spectral bound below one. The informative subset has a positive modified-χ² information gap. With H≥M and sufficiently large L, staged dynamics select the subset and concentrate the copiers; Appendix C.5 bounds deviation from the generalized induction-head estimator by O(L^(-1/8)). The theorem does not cover arbitrary zeros/initializations, unrestricted full-network SGD, or v10's β-uniform minimax selector. [Primary body, §3.3 and Appendix C.5](https://arxiv.org/html/2409.10559)

**Implication:** “higher-order joint features are unlearnable” would be false as a blanket claim. A v10 training problem must instead specify its architecture, initialization, task prior/coverage, finite training sample, precision and evaluation risk.

## 3. Resource and statistical boundaries that must not be conflated

### F. Chakrabarti, Pitassi and Alman, *Every Bit Counts* (2026)

Theorem 2.4 proves a one-bit separation for a one-layer, one-head softmax transformer with value dimension one, on its specially padded representation T¹_m of promised equality inputs (m odd and y≤z). For m=2p−1 and n>4p, p bits suffice whereas p−1 do not. Appendix A.3–A.4 declares primitive arithmetic/rounding and accumulation rules. This is a fixed-point Boolean function/representation theorem, not a stochastic Markov prediction lower bound or a general multilayer impossibility. [Primary theorem and arithmetic model](https://arxiv.org/html/2602.02707v1)

### G. Bondaschi et al., *From Markov to Laplace: How Mamba In-Context Learns Markov Chains* (v2, 2026)

Theorem 1 constructs MambaZero with N=S,d=2S,e=1,w=2 that exactly represents first-order add-β prediction for every sequence, using an L1-normalized output. Theorem 2 considers any recurrent state H_t∈R^d with p-bit coordinates. Under binary order-k independent Dirichlet(1) rows, eventual almost-sure pointwise L∞ error ≤ε relative to Laplace prediction requires

    d p ≥ 2^k (1−3ε) log(1/ε).

The guarantee is much stronger than small average error on the actual terminal context, and forbids rereading discarded history through the recurrent interface. Theorems concern representation; training success is empirical. [Primary v2, Theorems 1–2, Appendix D](https://arxiv.org/html/2502.10178v2)

### H. Han, Jana and Wu, *Optimal Prediction of Markov Chains with and without Spectral Gap* (2022 version)

Theorem 22 considers **stationary** order-m chains, m≥2, under next-state KL risk. For 2≤k≤n^(1/(m+1))/C_m, its minimax rate is Θ_m((k^(m+1)/n)log(n/k^(m+1))); the lower bound survives reversibility. The upper-bound argument uses universal-compression machinery. It is not an arbitrary-initialization TV theorem. Neither its logarithm nor its stationary rate can be transferred to v10 merely by replacing KL with TV. [Primary §5, Eq. (95), Theorem 22](https://arxiv.org/html/2106.13947v2)

### I. Basu, Choraria and Varshney, *Transformers are Universal Predictors* (2023)

Theorem 3.1 assumes an entropy-sufficient state representation and a count-based estimator on binary stationary/ergodic train/test data; it gives conditional-entropy limits as training data n→∞, with an O(|S|/n) expected convergence statement. The analysis uses a fixed underlying source and an infinite-test limit. This is not a finite-bit construction or a training guarantee across previously unseen source tables; the theorem's stated sufficient-representation assumption is substantive. [Primary §3.2, Theorems 3.1–3.2](https://arxiv.org/html/2307.07843v1)

## 4. What the candidate can honestly claim, if proved

1. **A genuine bridge:** under precisely declared masks, ports, rounding rules and network/circuit cost, the finite evaluated model produces the inherited selector's distribution up to an explicit TV term. The statistical theorem is inherited; the computational theorem is new work only to the extent it has actually been established.
2. **No oracle-sized margin:** integerizing the guard resolves exact ties without assuming that TV(q,b) stays away from the selection threshold. This is an implementation point, not itself a learning theorem.
3. **A useful scope extension:** arbitrary initial pair law, zero transitions, actual-terminal unconditional risk, and the same β-blind algorithm must remain visible. Do not relabel prior-averaged log loss as a weaker version of the same theorem; it is a different experiment.
4. **No attention advantage yet:** root's full-history direct counting comparator already obtains C,H with O(K log(M+K)) counting bits and an explicit scan. Comparing only final neural width against a streaming model that cannot reread history would be unfair. History/KV storage and accesses belong in the budget.
5. **No global lower bound yet:** inherited 034/035 concern specified corrupted ports and side information, even with arbitrary decoder. They do not cover alternative encoders, protected statistics, more snapshots, or a modified prefix.

## 5. Strongest meaningful next question

**Recommendation: determine the prediction precision–representation frontier, rather than prove another exact-count realization.**

For a *fixed declared causal computational model*, how much precision/storage is necessary to retain a constant-factor version of R011's expected-TV risk uniformly over β, when the encoder may be changed? In particular, is exact count recovery substantially over-solving the prediction problem, and can a protected/query-specific statistic attain the same risk with fewer precision bits or channels than the present mixed-statistic port?

This is a proposed research question, not a claim that no paper has solved any version. It is stronger than changing a decoder behind a fixed damaged port, and it asks for a consequence in the project's actual prediction loss. It also tests whether the bounded-score inversion mechanism has explanatory value beyond recompiling a count algorithm.

### Minimum concrete theorem package

- **Freeze access first:** full-history query-known scan, causal attention with stored prefix, or late-query one-pass memory. Choose one; do not combine the lower bound from one with an upper bound from another.
- **Freeze a real budget:** total retained bits (including history/cache and protected channels), finite score range, dynamic range, local copying/masking, primitive precision, and all additional computation. A bounded global matching score is not bounded score everywhere.
- **Include elementary digital protection:** under exact gate evaluation, R(x)=2 ReLU(x−1/4)−2 ReLU(x−3/4) restores any b∈{0,1} whenever |x−b|≤1/4. This margin calculation is an elementary baseline, not a novelty claim or a theorem about fully noisy gates. If restoration itself is perturbed, prove the invariant at every operation and charge the extra bit channels. Robust bit encodings can invalidate an analog-port comparison that equates only coordinate counts.
- **Compare two allowed encoders:** original soft-mixture statistic versus one costed protected representation, both with arbitrary decoder and the same actual terminal risk. Include direct counting as a baseline when the access model permits it.
- **Prove a nontrivial separation or matching frontier:** an information collision must occur with sufficient probability under legal stochastic sources, not merely on two rare hand-picked strings. Conversely, a constructive improvement must control the same corruption/rounding model at every charged operation.
- **Stop honestly:** if the direct baseline dominates, or decoder-independent loss disappears after cheap representation changes, report that negative result and position the bridge as a finite realizability theorem rather than an architecture-optimal theory.

Training is an important subsequent branch, but it has an additional mismatch: a finite-task, prior-averaged loss guarantee does not automatically imply a worst-source guarantee over the entire D₂(β) family. A training theorem would first need a specified task coverage condition or a narrower distributional evaluation target. This is why the representation/precision frontier is the cleaner immediate continuation of the current accepted results.

## 6. Evidence and limitations

- Read locally: `v10_intake/source/RESEARCH_STATE.md`, the linked total research plan, and `v10_research/root/exact_selector_v1.md`.
- Subsequently checked the inherited earlier stage2 `root-proof-v1.md`, §6, after root identified the count-snapping attribution; this narrows the novelty of any new bridge further.
- Checked public primary HTML/PDF body, displayed theorems and relevant proof sections for A–I. Ekbote's PDF was used because the HTML rendering drops boxed theorem statements. D'Angelo's PDF was used to verify the hard-copy and early-position limits, not just the finite-matching headline.
- The PMLR PDF link returned an unsupported-content-type retrieval error; the matching public arXiv v3 was retrieved successfully and checked. No access denial was bypassed.
- This pass did not verify every citation in the old plan, audit all published proofs, or claim literature completeness. Version-specific URLs and theorem numbers are supplied for subsequent comparison.
