# Clean episodes: shared-source baseline and fresh-source corollary

2026-11-03. Author-side analysis for independent review. These are elementary baselines and a direct re-expression of accepted proof B.3, not a new learning algorithm, independent scientific mechanism, architecture separation or external priority claim. No random samples, model initializations, numerical checks, or external writes were made. Probabilistic distributions and a randomized adversarial kernel below define mathematical experiments only.

## A. Baseline: repeated episodes from ONE unknown source

Fix M≥1 and N≥0. A fixed but unknown homogeneous binary order-two kernel θ and a fixed but unknown initial pair law μ generate N+1 independent trajectories. Each trajectory restarts from μ and has at least M+3 symbols. Episode i≤N supplies the complete clean history X^i_0,...,X^i_{M+1} and its subsequent label V_i=X^i_{M+2}; U_i=(X^i_M,X^i_{M+1}). Training is complete before the independent test episode, whose protected endpoint is U=(X_M,X_{M+1}). μ may be a stationary initial law of θ, as in the stated same-source comparison, but the proof works for any common μ. Test loss is absolute error in the probability of 1, equivalently binary TV, against θ_U(1). The future test label X_{M+2} is neither input nor available to the attack.

For each u∈{00,01,10,11}, retain only n_u=Σ_i 1{U_i=u} and c_u=Σ_i 1{U_i=u,V_i=1}, and set

  q_u=(c_u+1)/(n_u+2),     q(Z)=q_(Z_M,Z_{M+1}).

The estimator receives neither k nor β. At test time an arbitrary strict-k editing kernel changes at most k of the earlier M positions on every input and protects the terminal pair. It may be source-aware, adaptive, randomized and depend on the training data and predictor state; it cannot expose the test future label to the predictor. Since U is unchanged, q(Z)=q_U pointwise.

Let ν(u)=P_θ,μ(U=u), the same in every independent training and test trajectory. Conditional on n_u, the c_u observed outcomes are Bin(n_u,p_u), p_u=θ_u(1). This statement uses independence across episodes; it does not assert that selected transitions within a single trajectory are conditionally independent. For n=n_u,

 E[|q_u−p_u| | n] ≤ [sqrt(n)/2+1]/(n+2) ≤ 3/(2 sqrt(n+1)),

including n=0, where q_u=1/2. Indeed Var(c_u|n)=n p_u(1−p_u)≤n/4 and |1−2p_u|≤1. For ν(u)>0, n_u is Bin(N,ν(u)) and

 E[1/(n_u+1)] = [1−(1−ν(u))^(N+1)]/[(N+1)ν(u)] ≤ 1/[(N+1)ν(u)].

Test U is independent of training. Cauchy–Schwarz, Jensen, and Σ_u sqrt(ν(u))≤2 give uniformly over θ, μ, all budgets, and such attacks,

  R(θ,μ,k;q) = Σ_u ν(u) E|q_u−p_u| ≤ 3/sqrt(N+1).       (A.1)

Rows with ν(u)=0 contribute zero; no reciprocal is evaluated for them. The clean train and test trajectory symbols are not assumed iid within a trajectory. In particular N≥9M−1 gives risk ≤1/sqrt(M) even at k=0 and therefore at every k, including budgets unknown to the predictor. N=Θ(M) gives the same order with a different constant.

**Restricted-interface lower.** The O(N^-1/2) order is tight if the learner observes only the N pairs (U_i,V_i) and the protected test pair U, with no other trajectory symbols. Consider iid Bernoulli θ_±=1/2±d, d=1/[16 sqrt(3N+2)]. This is a legitimate order-two iid source with common stationary start and all-state certificate β=1, hence lies in the project's critical class. The permitted information consists of 3N+2 iid Bernoulli symbols. The product KL from θ_- to θ_+ is at most 32(3N+2)d²=1/8, using KL(Ber(p)||Ber(q))≤(p−q)²/[q(1−q)] and q(1−q)≥1/8. Pinsker gives total variation ≤1/4. Thresholding any estimate at 1/2 yields an induced test, so the usual two-point argument implies

  max_± E_±|q−θ_±| ≥ (d/2)(1−1/4)
                         =3/[128 sqrt(3N+2)].                 (A.2)

Predictor randomness is included in the Markov kernel and does not improve testing affinity. (A.2) is NOT a lower bound when the entire clean training trajectories are available: their other symbols contain additional information. It also does not lower-bound a source-aware predictor, which could know θ.

**Accounting.** Read all N training trajectories and their labels as provided: N(M+3) symbol inputs, Θ(NM) for M≥1. Maintaining four n_u and four c_u uses O(log(N+1)) bits for a fixed four-row alphabet, plus O(log M) bits for a position index if endpoints are not explicitly delimited; no full trajectories or hidden source parameters are stored. The stored trained state is these eight exact counts, not a free trained model. Four counter updates per episode cost O(N log(N+1)) bit operations under a simple bit model; total full-stream acquisition plus updates costs O(NM+N log(N+1)) elementary bit operations. Computing a rational q_u to additive output accuracy η incurs output/working precision O(log(N+1)+log(1/η)) and charged division; a straightforward schoolbook implementation uses polynomial time in that precision. The test scans M+2 input symbols if the interface delivers the whole word sequentially; accessing only the protected pair costs two symbols only under a separately charged indexed-access interface. If episodes are supplied with only their last three symbols, input acquisition is 3N symbols, a different interface. At N=Θ(M), full-history acquisition costs Θ(M²) tokens, not O(M). A Transformer and the classical four-row counter must receive the same clean episodes and pay comparable storage, preprocessing, address, output and arithmetic costs.

## B. Prior-matched fresh-source episodic interpretation of B.3

This part is a direct integration of the accepted B.3 proof, not an additional lower mechanism. The source drawn for each training episode and the fresh test source are independent; this is different from A. Let M,k meet all of B.3's finite domain with r=2:

  M≥64, 2≤k/128, k≤M/8, ck≥1024,
  c=2^-16, A=2^12, t=ck/M, At<1/4,
  M/k²≤A c²/2^20, L=log(1/(4At)), u0=floor(ck/4).

Use the exact stationary critical-class sources Q_a, a∈[At,1/4], and Q_* defined in B.3; every source meets the all-state β=1/M certificate. Define the proper source prior

  μ_(M,k) = (1/2) Q_* + (1/2L) ∫_(At)^(1/4) Q_a da/a.          (B.1)

This notation means a mixture of *source/trajectory experiments*, not interpolation of transition matrices. Each clean training or test episode samples a fresh source from the same prior and restarts from that source's stationary pair law. The output label is the next symbol after the history; it is excluded from predictor input and all attacks. The prior visibly depends on M and the selected evaluation k; its disclosure can reveal k, and no lower bound on inferring k is claimed. The same learned predictor is evaluated both with identity corruption and with the fixed-k corruption. It is not given a per-test switch selecting clean versus attacked mode.

Let D be any random trained state formed from N independent prior episodes, plus any training randomness, and independent of the freshly drawn test source/path and the attack's auxiliary randomness. Conditional on each realization D=d, let q_d be a fixed probability predictor depending on a test word only through its eight exact triple counts and its actual first and last two bits; internal predictor randomness is included in the trained-state/independent seed convention. D may encode the prior, k, arbitrary computation, learned weights and unlimited clean training samples. Define its expected clean *source-TV* mixture risk

  ε = E_D E_(source,W∼μ) |q_D(W)−θ_U(1)|.

From the explicit nonnegative-loss step in B.3, not only its final supremum statement, there is one common source-independent protected strict-k word kernel K=K_(M,k,2) such that for any fixed q_d with this observation restriction,

  R_*(q_d,K) ≥ ρ [ tL/16 − ∫_(At)^(1/4) R_a(q_d,id) da/a ],
  ρ=u0/(8 M t) ≥1/64.                                         (B.2)

The kernel uses the proof's predeclared auxiliary mixture, strict actual Hamming check and identity rejection; it is fixed independently of the unknown true source, the training data D and predictor randomness. It preserves the final pair on every input/output and never sees the test future label. Its definition does depend on the public experimental M and k, which is allowed for the adversary; no efficient attack sampler or finite-precision implementation is claimed.

Average (B.2) over D. The nonnegative null and alternative clean losses in (B.1) imply

  E_D [L^-1 ∫ R_a(q_D,id) da/a] ≤ 2ε.

The attack is applied to the same source mixture; discard nonnegative alternative-source attacked losses. Since μ assigns Q_* mass 1/2,

  R_μ(q_D,K) ≥ (L/128) [t/16−2ε]_+.                            (B.3)

This is a **fixed pair of clean and attacked evaluations** under the same prior and same trained map; it is not a lower bound for arbitrary full-history learners, for all N, for training success, or for the shared-source experiment A. If D is correlated with the test source as in A, conditioning on D changes the source law and (B.2) cannot be averaged as above.

A concrete clean-loss witness exists without assuming training succeeds: clean add-one B has source-TV risk ≤560/sqrt(M) on every source, by CTO001. The exact population cross-entropy Bayes predictor m(W)=E[θ_U(1)|W] under (B.1) has prior-average source-TV risk ε≤1120/sqrt(M), since conditional Jensen and triangle give E|θ_U−m(W)|≤2 E|θ_U−B(W)|. Every source in (B.1) has strictly positive stationary mass and transition probabilities, so every finite word has positive prior probability and m(W)∈(0,1). Strict properness makes this the unique clean-population cross-entropy minimizer at every word. Source likelihoods factor into initial-pair probability and triple counts, so m depends only on those counts and the first/last pair and satisfies the observation restriction. This is a population Bayesian statement, not a theorem that an SGD procedure or a finite dataset reaches the minimizer. CTO001 already proves a related clean-objective separation under a different, nonstationary, non-critical-support prior; this is an application of B.3 to a narrower matched prior, not evidence of a new general principle.

For an exact asymptotic parameter sequence, choose M=2^(4n), k=2^(3n), r=2, integer n≥33. The B.3 domain holds, and 2ε≤2240·2^(-2n)≤(t/32)=2^(-21−n). Then L=(n+2)log 2 and (B.3) gives

  R_μ(m,K) ≥2^-28 L·k/M.                                      (B.4)

The source-independent full-history classical half-gate B_G, with identical count/endpoint inputs plus first-half row counts, has risk at most (2^17+16)M^-1/2+(2^23+192)k/M; smoothing changes it by at most M^-1/2. It ignores training episodes and does not know the actual budget. Supply the same test observations, precision and training resources to any neural comparator. The constants in (B.4) and the gate guarantee are so conservative that their asymptotic separation becomes numerically apparent only at fantastically large horizons; neither bound is a practical performance prediction.

## C. Source identity, antecedents, and failed route

The manuscript Q_a above is not AB001's different Q_a. The latter is only claimed in its β=0 class for the alternative family and underlies a separate joint-blindness obstruction. Source binding: `positional_manuscript_consolidated_20261103/sections/proofs_negative.tex` SHA-256 c33000a5e7b98eb395d8ccae7c104b60d4cf7d30900607d64f4102c9bf9302c7; `clean_training_objective_20261103/CANDIDATE.md` SHA-256 1405c661827773bba64c8d8ae91f8eb8a9b2bf17ffc6a66e3be69525f1674bb2; `positional_gate_training_20261103/CANDIDATE.md` SHA-256 91dcb755e6544fa04e728ab92bf48a7cb864e1e28fc9e4cbdbe0fc38257cb0be.

Earlier in this exploration, a proposed finite-episode certification gap trained on Q_a yet used the attacked risk witness Q_*. That is a cross-source design and was retracted as a same-source claim. The separate audited record `matched_slow_source_audit_20261103_1016/PAIRED_SOURCE_SCOPE_AUDIT.md` shows the G-rejection region has Q_* clean mass at least 1/128, so a constant-weight mixture exposes it in O(log(1/δ)) episodes. The prior-matched bound (B.3) instead uses B.3's full observation restriction and clean-risk tradeoff; it does not claim those two fixed gates remain hard to distinguish.

For multi-trajectory context, Leskelä and Dreveton, *Robust estimation of a Markov chain transition matrix from multiple sample paths*, https://arxiv.org/html/2506.20325v2, model and Theorems 3.1/3.5, already study transition estimation from independent trajectories, including corrupted whole trajectories. Their experiment, matrix loss and contamination differ; the elementary A bound is not claimed as novel. B and CTO provide the exact project-specific antecedents for part B. External comparisons are bounded, not a novelty certificate.
