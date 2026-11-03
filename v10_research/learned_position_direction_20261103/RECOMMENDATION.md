# Learn the positional statistic, then try to falsify its protection

3 November 2026. Research recommendation only. No model was implemented or trained, no theorem is claimed, no frozen unit was changed, and no external write was performed.

## Recommendation

Run **one controlled feature-learning experiment**, not another bias/threshold theorem:

> Under the same binary order-two clean prior, can joint optimization of temporal pooling and prediction learn a position-dependent statistic that improves protected-terminal prediction against previously unseen legal source-edit attacks, compared with both count-only learning and frozen positional features?

This is a useful next *screening question*, not yet an ICML-level contribution. A positive result must survive causal feature ablation and difficult source panels. A negative result must distinguish absent training signal, insufficient readout, and attack overfitting. Neither outcome proves a general learning impossibility or a minimax guarantee.

## What is already closed, and what is not new

The accepted CTO001/PGT001/PBF001 chain already establishes the clean-prior Bayes rule, its logarithmic unknown-budget obstruction, a supplied-gate descent mechanism, and the sharp bias cap in that supplied-feature family. It does not learn a temporal statistic. The 55-page manuscript and BCJ001 already establish the half-gate, its approximate-statistic stability, and finite-bank precision phenomena. Those are baselines and interfaces, not new discoveries here.

Learning positional structure in Markov prediction itself is established. [Edelman et al., NeurIPS 2024](https://papers.neurips.cc/paper_files/paper/2024/file/75b0edb869e2cd509d64d0e8ff446bc1-Paper-Conference.pdf) study learned induction heads and a reduced optimization model; their arXiv v1 §3.2 also uses a deliberately changed hard-example curriculum. [Nichani, Damian and Lee, ICML 2024](https://proceedings.mlr.press/v235/nichani24a.html), §§2–4, learn causal structure in a reduced transformer, with explicit prior assumptions and a separately sampled uniform terminal query in their main single-parent task. [Ekbote et al., NeurIPS 2025](https://arxiv.org/html/2508.07208), §5 and Appendices C–D, train positional scalars and a matching scalar in stages while fixing substantial components. Thus “position is learned by gradient descent” is not a novelty claim. [Wei et al., ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/file/934ebba637be11105cff78e86a99eb08-Paper-Conference.pdf), pp.1–3, further study inference of random dependency structure from multiple demonstrations sharing a graph. That is not the single edited trajectory considered here.

The narrower potentially useful contribution is learning **which temporal evidence to retain for unknown-edit protection at the actual terminal state**, under a source-independent word-edit experiment. The scoped reads above do not certify external novelty.

## Precisely specified small model

At horizon M, input is only the observed word z of length M+2. Form ordinary local triple indicators e_i in R^8, i=0,...,M−1. This fixed local tokenizer is disclosed; learning lag copying or context matching is not part of this pilot. Let U=(z_M,z_(M+1)), t_i=(i+1/2)/M.

Use one fixed uniform pooling head and two learned heads:

- f_0 = M^(-1) sum_i e_i.
- phi(t) consists of the eight continuous piecewise-linear cardinal basis functions at knots 0,1/7,...,1. There is no first-half indicator or privileged half-time knot.
- For h=1,2, a_h is an eight-vector, s_hi=a_h·phi(t_i), alpha_hi=exp(s_hi)/sum_j exp(s_hj), and f_h=sum_i alpha_hi e_i.
- Select the two successor coordinates for U from each f_h. Concatenate these six numbers, the two terminal bits, and 1/M to obtain x in R^9.
- q_psi(z)=epsilon_M+(1−2 epsilon_M) sigmoid(v·tanh(Wx+b)+c), with hidden width 32 and epsilon_M=(M+2)^(-2).

All pooling coefficients and readout weights are jointly optimized. There are 369 scalar parameters, including 16 pooling coefficients. Initialize pooling coefficients independently with small centered Gaussian values, readout weights by a declared symmetric random initialization, and biases at zero. Record all seeds. Do not initialize a half-window or a robust predictor.

No B, D, G, acceptance threshold, empirical ratio, or fallback prediction is passed to the predictor. The uniform head deliberately supplies the strong count baseline. This is a small attention-pooling model with a fixed tokenizer, **not an end-to-end raw-token Transformer**. A classical weighted-counter program implements the same features at the same information level.

## Objective and legal training attack

Keep CTO001's prior: four independent Uniform(0,1) row probabilities and an independent uniform initial pair. Use fresh training words at M in {64,128}, equally weighted. Let B(w) be CTO001's add-one posterior computed from the clean training word. It is a training target and attacker reference only, never a model input.

For each k, C_k(w) contains the identity and nine transformations: overwrite with 0, overwrite with 1, or flip the length-k interval beginning at 0, floor((M−k)/2), or M−k. The interval is contained in positions 0,...,M−1. Every proposal changes at most k symbols and protects both endpoint bits, on every word. Ties use a fixed lexicographic rule.

Compare two fully specified objectives:

- Clean: E CE(B(W),q_psi(W)).
- Edit: (1/2) E CE(B(W),q_psi(W)) + (1/2) E_(W,K) max_(z in C_K(W)) CE(B(W),q_psi(z)), where K is uniform over {1, floor(sqrt(M)), floor(M/8)}.

The inner maximum over this finite proposal set is exact; it is **not** the maximum over the Hamming ball. At a unique maximum its gradient is the gradient of the selected proposal; at a tie choose a declared active branch. This is genuine joint numerical optimization of a finite structured-edit objective.

Why this respects the threat model: the attacker sees w, the frozen model, M and k, and computes B(w), all fixed functions of the observed history. It never sees the hidden table or realized future label. For every frozen legal A(W),

E[CE(V,q(A(W))) | W] = CE(B(W),q(A(W))).

Thus the soft target removes label noise under this exact prior; it is not secretly a true-source oracle target. If the prior or initial-law sampling changes, this identity with the same B must be reconsidered. In particular, do not add a sticky-source training curriculum and continue calling B its conditional label mean.

## Controls and evaluation that can refute the idea

Use the same initialization seeds, data, optimizer and training budget for: learned pooling/clean; learned pooling/edit; uniform-frozen pooling/edit (count-only); random-frozen pooling/edit. Add a fixed half/suffix-pooling readout control to check whether the readout can use known useful information; failure of that control blocks conclusions about feature discovery. Compare all with exact B, the accepted half-gate A for TV, and its explicitly smoothed Q for cross-entropy. Do not silently clip A to report its logloss.

Predeclare an initial pilot of three seeds, 1,000 updates per condition, batch size 64, float64 Adam with learning rates 0.003 for the readout and 0.01 for the pooling coefficients, beta=(0.9,0.999), epsilon=1e−8, no hidden weight decay or early stopping. These are screening choices, not optimized scientific constants. An unsuccessful calibration may justify one separately versioned optimization investigation, not endless tuning until a favorable robustness plot appears.

Freeze models before testing M in {64,128,256}. Report cells separately by source, initial pair, budget and attack. Include:

1. Fresh clean-prior average loss, distinguished from certificate-qualified testing.
2. IID sources, all four initial pairs, including probabilities near 0 and 1.
3. The manuscript's non-IID family p=(a,1/2,1/2,1−t), with t in {2/M,8/M}, a in {t,1/4}, and its bit complements. All have a,t<=1/4 and a>=t; the displayed P_a^2 formula gives every entry >=t/2>=1/M, so the all-state certificate holds. Use stationary starts as a separate panel, not a substitute for the four fixed starts. These are finite stress sources, not an empirical realization of the manuscript's asymptotic lower-bound parameter domain.
4. Budgets {0,1,floor(sqrt(M)),floor(M/8),floor(M/4)}, with the same fixed predictor for every k.
5. Held-out block locations and sparse-flip proposals. On a smaller declared panel, run greedy single-bit attacks that maximize CE(B(w),q(z)) with B(w) held fixed, considering all still-unedited editable positions and allowing no improving flip. Greedy is a legal attack, not a certified global maximum. Attack-selection code must have no theta or future-label argument.

Score the true terminal-row probability **after** choosing the attack. For each cell report E|q(A(W))−theta_U(1)| divided by g_M(k)=max(M^(−1/2),k/M), with Monte Carlo uncertainty and paired comparisons. Never choose a different attack for each trajectory by consulting theta. A finite maximum over these tested cells is a finite-panel lower witness for worst-case risk, not an upper bound on Gamma. Sample maxima and their confidence corrections must be labelled separately. For C predeclared bounded-loss cell means with N independent paths, the elementary simultaneous Hoeffding half-width sqrt(log(2C/delta)/(2N)) applies before normalization; if it is too loose, report that rather than declaring worst-case superiority.

Mechanistic evidence requires interventions: replace learned profiles by uniform profiles, freeze random profiles, and test count-preserving history rearrangements/collisions. An attention heatmap alone is insufficient. Changing only profiles after training can create feature distribution shift, so the independently retrained frozen-profile controls remain necessary.

## Feasibility, success criteria, and stopping rule

The available environment has NumPy/SciPy and no Torch/JAX/TensorFlow. No new framework is needed. Existing experiment.py supplies a checked source simulator/count oracle but does not retain words; a new word-returning simulator must be independently checked, not patched into frozen code.

The exact analytic pooling derivative is

partial f_h / partial a_hj = sum_i alpha_hi phi_j(t_i)(e_i−f_h).

A symbol flip changes at most three local triple indicators. This permits constant-size feature updates per candidate; an implementation should verify those updates against full rescans. Forward/backward cost is linear in M for the fixed-width model, plus the small finite proposal count and 32-unit readout. A 64×130 word batch is tiny; the risk is repeated attack search, not memory. Benchmark a fixed small number of batches before committing to the pilot and report measured operation/time cost. Do not promise a wall-clock runtime from the architecture alone.

A useful positive screen requires all of: successful clean/readout calibration; an edit-trained learned model beating the edit-trained count-only and random-frozen controls on predeclared held-out attack/source cells; replication across seeds; position ablation materially removing the gain; and no unexplained collapse at M=256. A concrete screening default is 2,048 independent test paths per predeclared source/start cell, shared across models and attacks, with a separate 8,192-path confirmation set for the worst cells selected in the screen. Require clean excess <=0.02 nats, at least 20% reduction of the finite-panel maximum normalized TV against both trained controls at M=64 and M=128 in the median seed, the same improvement direction in at least two of three seeds, at least half the improvement removed by uniform-profile ablation, and a positive improvement at M=256. Report uncertainty alongside each criterion; an uncertainty interval spanning zero is inconclusive, not a positive result. Freeze the selected confirmation cells and their number before drawing confirmation paths. These are declared screening thresholds, not statistical constants or asymptotic claims. Root may change this proposed budget before running, but not to fit observed outcomes. Success means an empirical mechanism worth studying further, not constant-factor minimax adaptation.

Stop this pilot when the fixed run and independent audit establish that conjunction or a concrete failure. If only in-distribution average loss improves, or gains disappear under unseen attacks or frozen-feature controls, retain the negative finding and do not expand the sweep. If the fixed-half control fails, identify the readout/optimization obstruction before interpreting positional failure.

The theoretical route should follow the mechanism, not precede it with another supplied-answer construction. A general-source guarantee would require a uniform learned-statistic/readout certificate (for example an all-word approximation interface to the accepted gate) plus an actual finite-sample optimization argument. Finite panel tests provide neither. The existing perturbation theorem can transfer a **proved** interface, but cannot certify a learned MLP by average error. Pursue that bridge only if the learned profiles expose a tractable mechanism; otherwise this controlled experiment has served its falsification purpose.
