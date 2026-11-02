# Precision-frontier followup: exact-interface claims versus existing quantization theory

Checked **2026-11-02**. This is a **second-stage, targeted primary-source check**, not a broad survey, proof validation, or novelty certificate. Keep it outside the first frozen guide/package. The material correction concerning Han–Jana–Wu was separately sent to root for the guide's literature paragraph; this does not promote the rest of this note into the first-stage deliverable.

## 1. Finding first

I did **not verify a prior theorem with the same complete fixed-summary interface, same actual-terminal expected-TV loss, same source classes and initialization, and the exact `log(1+Q)/Q` versus `1/Q` comparison**. That is a bounded statement about the sources checked, not evidence that no such result exists.

The broad mechanisms are nevertheless substantially established:

- A nuisance waiting state, one common prior, and harmonic averaging over effective sample sizes already produce a logarithmic Markov-prediction penalty; mixing-dependent removal of a prediction logarithm also predates this work. See A.
- Scalar finite-message absolute-error lower bounds, quantizing a Bernoulli sample mean, and the half-logarithmic bit threshold for the parametric sampling rate are already available. See B.
- Uniform quantization suffering an additional logarithm because of small probability coordinates, and nonuniform companding removing that penalty, are also known in another loss/experiment. See C.
- Finite-memory estimation and distributed quantization have different budgets and quantifiers. They cannot be substituted for this interface, even when formulas look similar. See D–F.

**Conservative contribution statement:** the candidate value is an exact, complete-interface specialization of established statistical and quantization ideas, with a matched finite upper bound and a dependence-safe terminal-count analysis. In particular, the lower bounds account for all surviving masters and exact side information, not merely one damaged normalized coordinate. This is not a first rare-context amplification mechanism, first quantization lower bound, first half-log precision threshold, or an architecture-wide optimum.

## 2. Local comparison target and status

Read locally: `prior_art/comparison.md`; PL001 proof and independent review; SM001 and SM002 proofs; their reviews and root acceptance records. Author headers were frozen before acceptance and remain unchanged. By the last local check all three had root acceptance records:

| Unit | Root acceptance time (UTC) | Bound and relevant scope |
|---|---|---|
| PL001 | 2026-11-02 02:25:44 | `R_master >= ln(1+8Q)/(1024Q)` for `K>=5,M>=6,Q=2^h,h>=4`; arbitrary initialization, beta zero; separate explicit vanishing-positive-beta transfer |
| SM001 | 2026-11-02 02:31:14 | Same NB002 predictor; `risk <= min(1,(2^16+8)L+2^13 K^3/Q)` uniformly for `beta>=1/2`; each fixed positive beta also covered with nonuniform constants |
| SM002 | 2026-11-02 02:36:39 | `R_master >= 2^-226/Q` for all `K>=2,M>=1,h>=4,beta`; stationary binary IID witness; arbitrary real randomized decoder |

Acceptance here means independent same-model LLM review followed by root adoption—not external peer review, formal verification, original-emitter testing, or novelty review.

The fixed interface retains all `9K+1` Q-grid masters, the declared exact endpoint/query/flag information, and public metadata. It does **not** retain a history reread, clean head numerators/denominators, evaluator working words, or another clean statistic. Source tables are homogeneous unknown order-two tables; the target is the next-symbol law at the actual terminal pair of the same trajectory. The two-step condition is `P^2(s,t)>=beta*pi(t)` for every pair state, including off-support starts, for an existential stationary `pi`; reversibility is not assumed.

At fixed K, the accepted synthesis is:

```
beta=0, K>=5:       R_master = Theta_K(max(M^-1/2, log(1+Q)/Q));
beta>=1/2, K>=2:    R_master = Theta_K(max((M+1)^-1/2, 1/Q)).
```

These statements compare the **same fixed encoder**, not the best possible encoder under a generic bit budget. The computational word precision remains a separate quantity containing `log M`. Nothing here establishes a total-memory/time advantage or trained attainability.

## 3. Primary sources and precise differences

Each entry identifies the inspected version and theorem/proof location. Rates use the source's own symbols.

### A. Han–Jana–Wu: the closest waiting/harmonic and mixing precedent

*Optimal Prediction of Markov Chains with and without Spectral Gap*, [arXiv v2, 3 May 2022](https://arxiv.org/html/2106.13947v2), §1 Eqs. (1),(8),(9), §3.1 Theorem 8, Theorem 3 and Corollary 4.

The experiment is stationary first-order Markov prediction from the full trajectory, with expected KL loss at its actual final state. Theorem 8 gives `Omega(log n/n)` for three states. Its symmetric, uniformly stationary witness has spectral gap `Theta(1/n)`; a nuisance waiting state yields roughly uniform effective sample sizes, and a common prior plus harmonic summation supplies the logarithm. Theorem 3 treats stationary irreducible reversible chains with absolute gap exceeding `gamma0`: add-one risk is `O(k^2/n)` if `gamma0 >= c(log k/k)^(1/4)`, also if `k >= c(log n)^6` and `gamma0 >= c log^2(n+k)/k`. Corollary 4 states that, for fixed `k>=2`, `O(1/n)` holds iff `gamma0=Omega(1)`.

**Difference:** this is a sample-size logarithm under unrestricted-data KL, not a precision-grid logarithm under a restricted encoder's TV loss. Its spectral/reversibility/stationary-start hypotheses are not v10's all-state two-step Doeblin condition and arbitrary-start setting. Nevertheless, the waiting/harmonic mechanism and broad mixing-removes-a-log narrative must be attributed, not claimed first.

### B. Xu–Raginsky: scalar `1/Q` and half-log bits are already explicit

*Information-Theoretic Lower Bounds on Bayes Risk in Decentralized Estimation*, [arXiv v1, 2 July 2016](https://arxiv.org/pdf/1607.00550v1), Theorem 3 Eq. (39), Example 6/Corollary 7, especially Case 1 Eqs. (100)–(103).

Theorem 3 gives, for scalar absolute loss, `R_B >= (1/(2e))*2^{h(W)-I(W;X)}` (unconditional specialization, bits). For a uniform prior of interval length `ell` and a D-valued observation, `h(W)=log2 ell` and `I<=log2 D`, hence `R_B>=ell/(2eD)`. This corollary is our direct substitution, not their printed constant `ell/(4D)` from PL001's separate elementary covering proof.

Example 6 estimates a uniform-prior Bernoulli bias after a processor quantizes its IID sample. In the noiseless case, the quantized sample mean has absolute error at most `1/sqrt(6n)+2^-b`; `b=(1/2)log2 n` matches their lower up to constants.

**Difference:** b is the **total** summary budget; the encoder is not v10's joint normalized bank. Its generic bound alone would count roughly `Q^(9K+1)` bank labels, not `O(Q)`. The essential SM002 obligation is its much sharper effective good-message count.

### C. Adler–Tang–Polyanskiy: logarithmic uniform-quantizer loss and companding

*Efficient Representation of Large-Alphabet Probability Distributions*, [arXiv v3, 26 October 2023](https://arxiv.org/html/2205.03752v3), §I, Remark 5/Eq. (29), Appendix F, Theorem 4.

Here the encoder observes the probability vector itself. Entries are scalar-quantized into N bins, then decoded by specified bin representatives and renormalized. Remark 5/Appendix F exhibit a prior with uniform-quantizer expected KL loss `Theta(K^2 N^-2 log N)` as N grows at fixed K; the proof explicitly sums inverse bin locations. Theorem 4 gives a nonasymptotic worst-vector KL bound `(1+err(K))N^-2 log^2 K` for their companders, for `K>4` and `N>=8 log(2sqrt(K log K)+1)`, with `err(K)<=18 log log K/log K<=7`.

**Difference:** known-vector coding, KL boundary sensitivity, and a specified reconstruction rule—not an arbitrary decoder estimating an unknown terminal transition law from a stochastic joint bank. No Markov mixing parameter appears. It is a genuine precedent for quantization logarithms and representation changes, but does not prove PL001. Applying companding to v10's *mixed statistics* is not automatically applying it to the desired row probabilities; cancellation and small denominators still need analysis.

### D. Berg–Ordentlich–Shayevitz: a tempting but different log/no-log comparison

*Deterministic Finite-Memory Bias Estimation*, [COLT 2021 published PDF](https://proceedings.mlr.press/v134/berg21a/berg21a.pdf), §1 Eqs. (1)–(5), Theorem 1/Corollary 2.

An S-state deterministic, time-invariant machine processes an indefinitely long IID Bernoulli sequence. Risk is the limiting time average of instantaneous **squared** estimation error. Theorem 1 proves `O(1/S)`; with the previously known lower, Corollary 2 gives `Theta(1/S)`. This disproves the older `Theta(log S/S)` conjecture, whose available construction incurred a derandomization overhead. The encoder/update rule is optimized, and storing a clock is not free.

**Difference:** S counts all streaming states, rather than Q levels per coordinate of a fixed batch summary; the loss, horizon and admissible updates also differ. Neither setting contains the other as stated. In particular, replace neither `S` by `Q` nor squared error by TV. This source prevents a generic claim that a log/no-log finite-memory distinction is new; it does not explain v10's mixing-dependent obstruction.

### E. Misra–Goyal–Varshney: functional quantization explains sensitivity, not this theorem

*Distributed Scalar Quantization for Computing: High-Resolution Analysis and Extensions*, [arXiv v3, 13 May 2011](https://arxiv.org/html/0811.3617v3), §IV-B assumptions MF1–MF4 and Theorem 9.

For scalar-quantized coordinates and a computed function g, Theorem 9 obtains the asymptotic optimal-decoder MSE

```
sum_j (1/(12 K_j^2)) E[(gamma_j(X_j)/lambda_j(X_j))^2],
gamma_j(x)^2 = E[|partial_j g(X)|^2 | X_j=x].
```

The stated assumptions include a Lipschitz g, an ambient continuous density on a compact cube, regular companding, and defined positive sensitivity integrals. The result permits correlated coordinates, so dependence alone is not an exclusion.

**Difference:** v10's frequency-to-row reconstruction can have sensitivity of order `M/(J+K)`; its empirical statistic law is discrete, and the IID comparison concentrates near curves rather than an ambient continuous density. The theorem is high-resolution MSE, not a finite-sample arbitrary-decoder TV lower. It motivates sensitivity-aware encoding but cannot be invoked across the rare-denominator regime without checking or replacing its hypotheses.

### F. Barnes–Han–Ozgur: per-observation communication is not a final-bank cut

*Lower Bounds for Learning Distributions under Communication Constraints via Fisher Information*, [JMLR 21 (2020) published PDF](https://jmlr.org/papers/volume21/19-737/19-737.pdf), §1 and Corollary 7.

Each of n distributed nodes holds one independent observation and writes at most k bits, under independent, sequential or blackboard protocols. For a distribution on `d+1` symbols, Corollary 7 gives squared-l2 risk at least `c max{d/(n 2^k),1/n}` when `n min{2^k,d}>=d^2`; its discussion identifies matching known schemes.

**Difference:** the total transcript can grow with n, and protocols/encoders are optimized. The precision cost is imposed **before aggregation**, not on one fixed normalized summary after observing the history. Thus this theorem neither proves an M-independent `1/Q` floor nor excludes one at v10's different information cut. It is a relevant baseline if a later branch changes the access model to distributed or streaming observations, not a license to equate these resource models.

### G. Kato–Kato: a recent finite-statistic prediction comparison, but no rare-context frontier

*Handover of In-Context Learning State Across Session Boundaries*, [arXiv v1, submitted 14 August 2026](https://arxiv.org/html/2608.14528v1), Theorem 5.3, Corollaries 5.4–5.6 and Appendix E.5–E.8. This is a preprint; no peer-review status is inferred.

For Bayesian Gaussian linear regression with known noise variance and positive-definite prior precision, Theorem 5.3 bounds posterior mean/covariance perturbations caused by quantizing Gram and cross-product statistics. Corollary 5.4 converts these to Gaussian predictive KL. For fixed sample count and other model parameters, Corollary 5.6 gives a finite-code upper `K*2^{-2(B-B0)/p}`, where `p=d(d+1)/2+d`; its constants are allowed to depend on the fixed sample count. The proof uses a resolvent identity and uniform lower eigenvalue bound.

**Difference:** a regularized Gaussian sufficient-statistic upper, not unknown Markov terminal TV, not sample-size-uniform rare-denominator stability, and not a matching lower for a prescribed scalar-quantized bank. It supports the need to distinguish finite-dimensional real sufficiency from actual finite coding, but does not settle the present comparison.

## 4. What follows from existing techniques, and what does not

This section is **our mathematical comparison**, not a quotation or a theorem attributed wholesale to any paper.

### 4.1 The lower-bound assembly is familiar once the complete message count is established

Suppose one scalar prior remains uniform on an interval of length ell conditional on events `E_j`, with `P(E_j)>=c/M`. Suppose the **entire permitted observation**, even after its allowed exact side information is retained, has at most

```
D_j <= C(1+Qj/M)
```

labels on each event. A scalar finite-message Bayes bound then yields

```
risk >= (c ell/(2e C M)) sum_{j=0}^{floor(c' M)} 1/(1+Qj/M).
```

For fixed positive c', the integral comparison gives order `log(1+Q)/Q`. The finite-message ingredient is covered by B, and the common-prior waiting/harmonic strategy is closely parallel to A. Thus the rate is **implied by existing elementary techniques plus the problem-specific message bound**; it would be misleading to present this final integration as a new statistical principle.

What A/B do **not** establish is PL001's exact `D_j` for the true `9K+1` bank, actual finite weights, retained boundary fields and homogeneous second-order witness. A lower bound for one coordinate or an idealized encoder would not establish it. The fixed-length cycles and joint monotone-cell count solve those particular information-leakage obligations.

### 4.2 The scalar IID floor is familiar; the effective bank dimension must be proved

A fixed-dimensional vector with Q levels in every coordinate can have order `Q^d` labels. One cannot claim a `1/Q` lower merely because it has finitely many coordinates.

SM002 instead bounds its complete unrounded bank, with uniformly positive finite head denominators, within `O(M^-1/2)` of finitely many Lipschitz one-parameter curves. In the range `Q<=sqrt M`, cover each curve by `O(Q)` boxes of diameter `O(1/Q)`. Each thickened box intersects only a constant number of grid cells at fixed active dimension; hence the **good-message** alphabet is `O(Q)`, not `O(Q^d)`. The good event has uniformly positive probability without conditioning IID observations on the terminal query. A covering Bayes argument then gives `Omega(1/Q)`; the complementary range uses the sampling lower bound.

This is a transparent metric-covering reduction, not evidence of a new general information-theoretic lower-bound method. Its content lies in verifying the regular finite-head maps, complete side-input accounting, uniform constants, and correct good-event handling for this encoder.

### 4.3 The logarithm is not automatic for every rare context

For nonnegative vectors u,v of positive masses s,t,

```
TV(u/s,v/t) <= ||u-v||_1/s.
```

This follows by adding and subtracting `v/s` and using `|s-t|<=||u-v||_1`. Thus absolute frequency error can be amplified by a small normalization mass. However, an amplification envelope alone is only an upper bound; it proves neither irrecoverable information loss nor the probability of encountering a difficult history.

PL001 supplies a legal stochastic family and exact joint-cell loss. SM001 controls a bounded reciprocal-count functional at the **same actual terminal context** by reversing a stationary suffix and using the inherited two-step minorization, then paying a whole-suffix TV transfer for arbitrary starts. A generic statement that mixing gives concentration, or a bound for an independent query, is insufficient. Conversely, the source comparisons above do not establish that this particular reciprocal lemma is unprecedented.

### 4.4 No transfer through an inappropriate loss or budget

- A KL lower bound is not a same-order TV lower bound. A KL upper can imply a TV upper with a square-root change; that does not preserve the relevant logarithm or precision threshold.
- `Q=2^h` levels per master is not h bits for the full bank, and not an S-state recurrent-memory budget.
- More computation after a fixed information cut cannot restore lost labels, but moving a normalization or a different encoder **before** that cut changes the experiment.
- Known-vector companding, protected counts, query-specific normalization and randomized encoders are meaningful comparison candidates only when their additional acquisition, arithmetic, range, storage and query access are charged.

## 5. Recommended positioning and next use

For the first guide, the correction from A is enough: acknowledge the waiting/harmonic precedent and distinguish unrestricted KL/spectral results from this finite-interface TV/Doeblin result. Root was sent the verified paragraph while work on this note continued. Do not add a claim of first mechanism or first mixing-sensitive precision law based on this search.

For a later paper, prioritize the following evidence rather than adding literature breadth:

1. State a general, inspectable class of normalized encoders for which the complete conditional label bound or the curve-tube argument holds. Prove every condition; do not encode the desired conclusion into an assumption.
2. Compare at least one genuinely changed, fully costed representation under the same access contract. B/C/E show that scalar quantization and sensitivity-aware encoders are established baselines, not new ideas by themselves.
3. Separate the theorem's actual contribution from the reusable proof tools: complete finite-interface identification; exact finite weights and side ports; same-trajectory risk; arbitrary-start transfer; matching order for that one encoder.
4. Keep open the stationary weak-mixing and horizon-dependent intermediate-beta regimes. The checked literature neither resolves those variants for this bank nor certifies their novelty.

**Suggested narrowly defensible wording:** “For a specified complete finite normalized-statistic interface, we identify the fixed-alphabet precision–prediction frontier and show how its quantization term changes between weak and uniformly strong mixing. The analysis combines established waiting-time and finite-message ideas with exact joint-message accounting for the evaluated interface. It does not optimize over encoders or establish a trained-network advantage.”

## 6. Search and evidence record

- Generic searches covered quantized Markov prediction; communication-constrained probability/distribution estimation; finite-memory Bernoulli estimation; conditional probability quantization; functional quantization; and quantized sufficient statistics. No private proof text, exact unpublished unique claim, witness table or source material was sent externally.
- The papers already mapped for shallow n-grams, CTW, coding and recurrent transformer comparisons were not resurveyed. A was revisited specifically for the new waiting/mixing issue rather than its already mapped higher-order rate.
- A–G were inspected in primary theorem statements and the cited proof/settings sections. Search snippets and third-party summaries were used only to locate primary sources, not as theorem evidence. The external proofs were not comprehensively independently re-proved.
- `https://arxiv.org/html/1607.00550v1` returned `Failed to fetch ... UnexpectedStatusCode`. Its public version-specific PDF was then retrieved successfully. This was a format/retrieval failure, not an access or safety denial; no denied route was bypassed. No contacts, installations, purchases or publication occurred.
- Keyword matches for quantizing observed Markov *states*, agent memory, unlearning and conditional clustering were not treated as matching transition-law precision theorems. The known-state source-coding literature is a different problem and was not exhaustively audited here.
- This note does not change frozen proof files, acceptance records or `comparison.md`. The latter remains the earlier bridge comparison, with its historical candidate-status language. Root separately owns any guide correction and delivery freeze.

### Local bindings used for status-sensitive claims

```
PL001 proof: d7cd0815fe506b5d25d3025abf80b64588728d0b3342241d38a3a13ccc4fac34
SM001 proof: 3d4bdb15966a79cb67766e91babee3b81017376a79f42c8c4141bfd85a7aa78d
SM002 proof: 170840c84e5633f5b131641aaef8ebaee9db69c5550e878db5002e5446cbb5cc
```

The source for these acceptance/status bindings is the corresponding JSON in `v10_research/intake/`, not stale author headers. This note's scope is complete after the focused source comparison and actionable positioning correction; a broader novelty search would be a separate research unit.
