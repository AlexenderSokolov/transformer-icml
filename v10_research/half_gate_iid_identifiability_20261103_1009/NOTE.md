# Clean-episode identifiability of the fixed half gate: an iid dead end

2026-11-03. Author analysis, not independently reviewed. No sampling, model initialization, or external writes. Question: can a clean-training lower bound for the actual fixed J/C/D half-gate derive a meaningful corruption gap from insufficient coverage of rare feature groups, against an unknown-source classic sequence estimator? The broad iid comparison fails in a regime that includes all statistical-scale budgets.

## Model and statement

M≥8, 0≤k≤floor(M/1024). X_0,...,X_{M+1} iid Bernoulli(theta), with unknown theta in [1/4,3/4]. A source-independent offline attacker edits at most k of positions 0,...,M−1 and leaves terminal X_M,X_{M+1} fixed; Z is the resulting word. Future label X_{M+2} is excluded from Z and from attack observations. Let u=(Z_M,Z_{M+1}), J the number of indices i=0,...,M−1 with (Z_i,Z_{i+1})=u and D that same number for 0≤i<floor(M/2). Define G=1{J>0 and 512D≥J}. Then uniformly in theta and in every legal attack,

  P(G(Z)=0) ≤ exp(−M/1024).

Consequently for any measurable B(Z), F(Z) in [0,1], the fixed half-feature predictor H(Z)=G(Z) B(Z)+(1−G(Z)) F(Z) differs from B on at most that probability. In particular the absolute difference of their expected TV losses for the protected-row true probability theta, under the same attack, is at most exp(−M/1024). The conclusion also bounds the difference of the two separate suprema over the same allowed attack class. It does not bound models that differ when G=1, or gate approximations whose mistakes are outside the rejection region.

## Proof

Put n=floor(M/4). Conditional on u, the n disjoint pairs (X_0,X_1), (X_2,X_3),...,(X_{2n−2},X_{2n−1}) are independent and independent of the protected endpoint. Their match count S is Bin(n,p_u), where p_u=P((X_0,X_1)=u)≥1/16. Therefore mu=E[S|u]≥n/16≥M/128, using M≥8.

The edited first-half row count D includes every one of those disjoint starting pairs. A single editable symbol can change at most two first-half row indicators, and the terminal pair does not change the identity of u. Hence D≥S−2k. If G=0, then D<M/512: when J=0 this follows from D=0; otherwise 512D<J≤M. Therefore S<M/512+2k≤M/256≤mu/2. A multiplicative Chernoff bound yields P(S<mu/2|u)≤exp(−mu/8)≤exp(−M/1024). Average over u. These inequalities remain valid for fully adaptive randomized attacks because the implication is pathwise.

## Classical comparison and resource accounting

The simple estimator T=clip_{[1/4,3/4]}((1/M) sum_{i=0}^{M−1} Z_i) is independent of k and theta. Clipping cannot increase error against theta in the interval, and each edited bit changes the average at most 1/M. Thus for all k, E|T−theta|≤1/(2 sqrt M)+k/M: Jensen plus Bernoulli variance ≤1/4. T uses an M-symbol sequential scan, an exact integer accumulator needing ceil(log2(M+1)) bits, and paid division/output rounding if finite precision is required. This exploits the iid subclass and is not a robust estimator for the full unknown binary order-two family. It estimates from the test word, not from other training trajectories. The stationary iid source has P²(u,v)=Pi(v), so meets the project's all-state critical 1/M certificate.

The finite-episode question remains distinct: N is the number of independent *training trajectories*, each with one held-out next-token label, not the number M of symbols in one test word. Failure to see rejected rare groups does not itself imply a consequential test risk, because reachable rejection is exponentially unlikely on this source class at these budgets. Moreover an all-word identification requirement could demand certifying words outside high-probability attack images even when unneeded for expected risk.

## Genuine unresolved research choice

Study accepted stationary lower-witness sources and their allowed source-independent path transports. For a *specified trainable* fixed-feature model, define an influence-weighted gate approximation error E[sup_{legal K} |q_w(KX)−A(KX)|], or its supremum over those sources, and ask whether clean episodes identify the gate to o(max(M^−1/2,k/M)) at the witness budgets. Compare a constructive clean-episode training or verification procedure and a classic one-pass fixed-gate counter with the same source words, labels, arithmetic precision, space and total training/test work. A real lower must show two statistically indistinguishable proper source/training experiments or two objectively near-optimal predictors whose *reachable* gate disagreement carries enough unconditional source risk, with no future-label leakage. No such lower is established here. Exact accepted CTO001 already proves an asymptotic population logloss/robustness difference; BCJ001 already supplies the fixed positional bank and its precision mechanism. Do not repackage either as a new finite-episode theorem.

## Prior art and limits

Schmidt et al., *Adversarially Robust Generalization Requires More Data*, NeurIPS 2018, https://proceedings.neurips.cc/paper_files/paper/2018/file/f708f064faaf32a43e4d3c784e6af9ea-Paper.pdf, abstract and introduction, already establish a broad information-theoretic robustness sample-gap for other models. Attias, Kontorovich, Mansour, *Improved Generalization Bounds for Adversarially Robust Learning*, JMLR 2022, https://jmlr.org/papers/v23/20-1353.html, abstract, treats clean samples with access to corruptions, including real-valued prediction. Neither inspected abstract establishes or refutes the stated sequential fixed-gate bound. The present result is elementary, limited, and not claimed publishable or novel. The deterministic diagnostic in check.py checks finite binomial tails and numerical constants, not the infinite-domain proof.
