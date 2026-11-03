# Targeted reliability prior-art audit

2026-11-03. Local research note; no publication, outreach, novelty certification, or new mathematical root acceptance. Read-scope limitations are in `READ_SCOPE.md`. Candidate-file “pending” labels are historical: the four accompanying ROOT_ACCEPTANCE.json receipts record BSC001, BCC001, WMC001 and PMC001 as accepted local mathematical results.

## Executive disposition

The strongest direct overlap is **not merely a thematic citation**: Duchi–Ruan's general constrained-risk theorem replaces the new channel comparison and preserves its order after the existing mixture attack, with changed numerical constants. The total-message lower/upper architecture has a particularly close predecessor in Xu–Raginsky's Bernoulli-bias-through-BSC example. The unequal-support mechanism is classical zero-undetected-error detection. Concatenation is a standard coding ingredient.

The potentially distinctive object remains the *specific* hidden-budget, protected-endpoint, first-order Markov experiment and its same-rule adaptation/positional-information theorem. This audit establishes neither that this object is new nor that an existing paper proves the entire object. “Search did not locate the exact theorem” is not evidence of priority.

## 1. Constrained risk: a direct substitution, not a new inequality

Primary source: John Duchi and Feng Ruan, **A constrained risk inequality for general losses**, AISTATS 2021, §2, Theorems 1–2, [full paper](https://proceedings.mlr.press/v130/duchi21a/duchi21a.pdf). Theorem 2 uses nonnegative loss, its loss distance `d_L(P0,P1)=inf_v[L(v,P0)+L(v,P1)]`, and chi-square affinity `rho(P1||P0)=E_0[(dP1/dP0)^2]`. If risk at P0 is at most δ, the lower bound at P1 is `(sqrt(d_L)-sqrt(rho δ))_+²`. It extends the Brown–Low constrained-risk framework beyond squared error.

**Audit derivation applying that theorem (not a claim made in the cited paper):** Fix clean proposal y and relocated w with the same baseline and terminal 00. Let P0 be the encoded-channel output law at y and P1 that at w; include independent decoder randomization in the observation. Assign targets a and β respectively (if P0=P1, use the direct integrated triangle inequality instead; no parameter functional on identical distributions is needed). Bernoulli unsquared-TV is absolute loss, hence `d_L=a−β=Δ`. Bounded channel likelihood implies `dP1/dP0≤κ_R` and therefore `rho≤κ_R` (not κ_R²). With `ell=E_y loss_a`, the cited theorem gives

```
b >= (sqrt(Δ)-sqrt(κ_R ell))_+² >= Δ/2 - κ_R ell.
```

The last inequality holds for all nonnegative arguments: when `κ_R ell≥Δ/2` its right side is nonpositive; otherwise use `2sqrt(Δ κ_R ell)≤Δ/2+2κ_R ell`. The local direct L-infinity proof gives the stronger `b≥Δ−κ_R ell`, but a new universal risk inequality is not needed.

Insert this replacement **after** restriction/transport of nonnegative actual null loss in the existing FOT001 mixture construction. It changes the transported positive term from `t/64` to `t/128`, keeps the clean penalty `κ_R S`, and preserves the `Ω(log M)` necessary-length order. The local finite constants should not be copied unchanged into this alternative proof. Independent public coins can be conditioned on and then averaged; no source-dependent seed is allowed.

Thus standard constrained-risk machinery directly subsumes the *new statistical comparison ingredient*, conditional on the bespoke legal mixture lemma. It does not construct that strict-budget kernel or establish its Markov/certificate/endpoint properties.

Historical reference: Brown and Low (1996), **A constrained risk inequality with applications to nonparametric functional estimation**, Ann. Statist. 24(6), 2524–2535, [author-hosted PDF](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Constrained-risk-inequality-with-applications.pdf), DOI 10.1214/aos/1032181166. Original theorem text was not successfully extracted in this pass; do not cite an unchecked theorem number or claim a literal unsquared-TV statement there. Duchi–Ruan is the verified direct theorem.

## 2. Noisy statistical communication: closest checked application

Primary source: Aolin Xu and Maxim Raginsky, **Information-Theoretic Lower Bounds on Bayes Risk in Decentralized Estimation**, [2016 full preprint](https://arxiv.org/pdf/1607.00550). Theorem 4 bounds single-processor information using quantization, capacity and SDPI. Example 6 / Corollary 7 / equations (96), (100)–(107) study IID Bernoulli bias under **absolute loss**: `b≈(1/2)log n` noiseless quantization, and BSC transmission of a logarithmic-size sufficient statistic, with risk bounded by estimation plus decoding error. Example 4 / Corollary 4 treat arbitrary-code single-bit BSC transmission.

**Audit implications:** WMC001's clean IID lower is standard scalar-quantization/remote-estimation territory, not a new information principle. Its restricted prior preserves the project certificate. Its robust Markov payload and uniform unknown-k guarantee require separate proof.

Supplemental BSC001 has free data-dependent counts/endpoints. Generic capacity bounds must account for that baseline; whole-transcript information cannot be charged solely to R. An arbitrary encoder need not encode the historical gate. Thus a single-bit reliability converse is insufficient without the actual mixture reduction.

Do not claim first noisy statistical communication bounds, first logarithmic communication for parametric accuracy, or a new coding-based separation principle. This predecessor does not itself establish the project's strict-budget Markov experiment.

## 3. Support partition: classical detection versus silent error

Primary source: Christoph Bunte, Amos Lapidoth and Alex Samorodnitsky, **The Zero-Undetected-Error Capacity Approaches the Sperner Capacity**, IEEE TIT 60(7), 2014, [full paper](https://www.isiweb.ee.ethz.ch/papers/docu/buch-alap-2014-1.pdf), §II, p.3827 and Proposition 1. The paper explicitly proves that an exclusive output permits reduction to a Z-channel and positive zero-undetected-error capacity; if all input rows have identical supports, every codeword remains possible and such a decoder must erase. Proposition 1 coalesces outputs with identical support patterns; for binary input it reduces this capacity computation to an asymmetric erasure channel.

**Application-specific inference:** BCC001's two-slot `01/10` code balances a one-sided exclusive event into an exact BEC with input-independent erasure probability. This is a particularly elementary realization of that standard support mechanism, not a newly discovered detection principle. Disjoint supports give exact one-use decoding; identical rows give no information; finite common support gives bounded likelihood ratios. Those elementary distinctions are not themselves novel.

The *orders* `log log M` versus `log M` additionally use this project's baseline factor `Θ(log M)` and clean-scale risk requirement. They are not a new zero-error-capacity classification. In particular an unequal-overlap channel can have zero ordinary zero-error capacity while positive zero-undetected-error capacity: erasures are allowed in the latter. Never conflate these quantities. Coarsening supplies a degradation to a BEC, not equivalence of the full raw output experiment.

## 4. Experiment comparison and robust adaptation boundaries

For Le Cam/Blackwell language, the relevant verified mathematics here is simple kernel composition: simulate the coarsened observation and then its decision rule; a uniform TV simulation error ε changes a [0,1]-loss risk by at most ε. This is an elementary derivation, not a checked quotation of a particular Le Cam theorem. It explains why “less informative” must mean a valid common parameter-independent randomization, not arbitrary comparisons of two different side-information channels. The original [Le Cam 1964 article](https://doi.org/10.1214/aoms/1177700372) was located but its core theorem was not readable in this pass; no theorem-level subsumption claim relies on it.

Primary robust source: Chen, Gao and Ren, **A General Decision Theory for Huber's ε-Contamination Model**, [full preprint](https://arxiv.org/pdf/1511.04144), Theorems 3.1–3.3. Its Scheffé-based estimator adapts to unknown contamination proportion in an IID Huber mixture model; TV estimation is controlled through metric entropy/local entropy and contamination. The modulus lower bound in Theorem 3.2 is a standard clean-complexity/contamination decomposition. These results prohibit framing unknown-contamination adaptation as generally new or generally impossible.

Primary contrasting source: Liu and Gao, **Density Estimation with Contaminated Data: Minimax Rates and Theory of Adaptation**, [full preprint](https://arxiv.org/pdf/1712.07801), §4, Theorems 4.2–4.3 and §6.7. Under arbitrary Huber contamination and pointwise squared density loss, knowledge of either smoothness or contamination enables adaptation with a logarithmic term; joint unknown smoothness/contamination has an impossibility result. The proof constructs an exactly identical mixture with different target densities.

**Non-subsumption conditions:** IID mixture contamination is not an almost-sure ≤k offline symbol-substitution kernel on a dependent trajectory. Pointwise density loss is not actual-terminal unsquared-TV prediction. Full sample access is not exact triple counts plus a paid positional message. An oracle supplying k, a clean sample, or source labels is not the law-independent gate computed from the corrupted trajectory. No located theorem here proves the protected-final-pair advice tradeoff; equally, this scoped pass is not an exhaustive audit of advice/side-information literature.

## 5. Coding implementation: standard method, careful accounting

Primary historical anchor: G. David Forney Jr., **Concatenated Codes**, MIT RLE Technical Report 440 (1965), [full report](https://ntrs.nasa.gov/api/citations/19660011586/downloads/19660011586.pdf?attachment=true), §§1.1–1.2 and 5.1. It develops inner/outer concatenation, Reed–Solomon outer coding, and reliability/computational-complexity tradeoffs. The scanned §5.1 includes a near-exponential-in-length bound for a multistage construction; do not relabel that particular displayed statement as PMC001's exact finite maximal-error lemma without checking its details.

PMC001's small exhaustive inner code, polynomial evaluation outer code, unique decoding, and union-bound reliability are standard ingredients. Its explicit rational arithmetic, uniform constructibility, maximal rather than average message error, and charged storage are useful implementation bookkeeping for this experiment, not a new code family or capacity theorem. An average-error existence theorem alone would need expurgation or a separate maximal-error proof for arbitrary attack-induced payloads. “Polylogarithmic resources” applies to coding/design/auxiliary storage, not the full input scan or a resident raw word.

## Recommended claim discipline

Safe: “For the specified first-order, hidden-budget experiment, we combine a positional adaptation construction with standard constrained-risk and coding methods to obtain a channel-dependent supplemental-information classification; when all prediction information is charged, standard scalar-information and coding arguments yield total logarithmic communication.”

Not established: priority, a general new channel lower-bound principle, a new support/detection classification, a new concatenated code, second-order transfer, unknown/infinite-output/M-dependent-channel extensions, optimal leading constants, practical coding efficiency, neural realizability, or learnability. The local root receipts certify none of those.
