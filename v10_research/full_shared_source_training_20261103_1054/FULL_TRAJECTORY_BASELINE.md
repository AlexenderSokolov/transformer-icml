# Shared-source prediction from full clean trajectories

2026-11-03. Author-side proof; independent review required. This is a classical pooled-counter comparator and a finite-sample rate calculation, not a claim of a new Transformer or Markov-estimation principle. No random sampling, numerical diagnostic, model initialization, or public write was performed. All probabilities below define mathematical experiments.

## Setup and result

Let N,M≥1. Fix one unknown homogeneous binary order-two source θ and one of its stationary pair distributions π. The pair chain P on 00,01,10,11 obeys P²(u,v)≥βπ(v) for every u,v, where β≥b>0 and b≤1. Draw N independent clean training trajectories from that *same* θ, each with stationary initial pair π, and an independent stationary test trajectory from the same θ and π. Each training word is X^i_0,...,X^i_{M+1}, hence has exactly M valid departures j=0,...,M−1, and N(M+2) input symbols in total. The test word has M+2 symbols. No future test label X_{M+2} is observed by the predictor or the attacker.

An offline attacker may change at most k of the first M test symbols on every output, but must protect the original terminal pair U=(X_M,X_{M+1}). It may be randomized, adaptive, see the training data, know θ and k, and be source-dependent; the upper bound remains true under this stronger attack because the estimator ignores all attacked coordinates. The predicted target is θ_U(1), with binary total variation loss |q_U−θ_U(1)|. Neither k nor the actual β is supplied to the predictor. The known lower bound b can be chosen as 1/M throughout the original critical class.

For every row u collect pooled counts

  J_u=Σ_(i=1)^N Σ_(j=0)^(M−1) 1{(X^i_j,X^i_{j+1})=u},
  C_u=Σ_(i=1)^N Σ_(j=0)^(M−1) 1{(X^i_j,X^i_{j+1})=u, X^i_{j+2}=1},
  q^all_u=(C_u+1)/(J_u+2).

The predictor returns q^all_U. Then uniformly over all such θ, π, N, M, and attacks,

 R(q^all) ≤ min{1, 2/sqrt(NM)+8/(NM)+64/(NMβ)}
          ≤ min{1, 2/sqrt(NM)+8/(NM)+64/(NM b)}.       (1)

At b=1/M, the last term is 64/N. Separately, on the identical words, take only the *last valid departure* of each training episode: row (X^i_{M−1},X^i_M) and successor X^i_{M+1}. These N row/successor pairs are independent across episodes and have row distribution π. The four-row add-one estimator q^end based on them satisfies

 R(q^end) ≤ min{1,3/sqrt(N+1)}.                                (2)

No extra training label is acquired. Choose before reading the data whichever of (1)'s b-based bound and (2) is smaller, breaking ties deterministically; this choice depends only on public N,M,b and not on θ, π, k, actual β, data, or the test word. The resulting single predictor obeys

 R ≤ min{1, 3/sqrt(N+1), 2/sqrt(NM)+8/(NM)+64/(NM b)}.     (3)

This does not mean (1) is informative at every N: for small N or weak b it may exceed 1, in which case the cap and endpoint branch remain valid. Nor is the 64/(NMβ) term claimed necessary. At b=1/M and N=M the pooled bound is ≤66/M+8/M²; for N≥M it is O((NM)^−1/2).

## Proof of (1): occupancy, martingale, protected endpoint

Write T=NM and p_u=θ_u(1). Rows with π_u=0 are almost surely neither visited in any stationary training trajectory nor selected as stationary test endpoint. They contribute zero to risk, so all divisions by π_u below are restricted to π_u>0.

The minorization yields P²=β 1π+(1−β)R for a stochastic R, with the obvious β=1 limit. Since πP²=π, πR=π if β<1. Therefore, for h≥0,

  sup_x ||P^h(x,·)−π||_TV ≤ (1−β)^floor(h/2).

For one stationary trajectory, the covariance of row-u indicators at lag h≥1 has absolute value at most π_u(1−β)^floor(h/2). Because

  Σ_(h≥1) (1−β)^floor(h/2) = 1+2Σ_(j≥1)(1−β)^j = 2/β−1,

its M-step occupation count has variance at most

  Mπ_u[1+2(2/β−1)] ≤ 4Mπ_u/β.

The N trajectories are independent, so E J_u=Tπ_u and Var(J_u)≤4Tπ_u/β. Chebyshev gives

  P(J_u<Tπ_u/2) ≤ 16/(Tπ_uβ).                               (4)

For the numerator set S_u=C_u−p_u J_u. Reveal the N initial pairs and following symbols in episode order, revealing each trajectory's initial pair at its own start. At each departure, 1{Y_j=u}(X_{j+2}−p_u) has zero conditional expectation given all previously revealed data. Thus these are martingale differences even though within-word transitions and row visits are dependent. The cross terms vanish and

 E S_u² = E Σ_(i,j) 1{Y^i_j=u} p_u(1−p_u) ≤ Tπ_u/4.        (5)

No conditioning on the selected row count, nor independence of its selected successor bits, is asserted. Since

 |q^all_u−p_u|≤(|S_u|+1)/(J_u+2),

on H_u={J_u≥Tπ_u/2}, Cauchy–Schwarz and (5) give

 E[1_(H_u)|q^all_u−p_u|]
   ≤ 2(E|S_u|+1)/(Tπ_u)
   ≤ 1/sqrt(Tπ_u)+2/(Tπ_u).

On H_u^c, the loss is at most 1, and (4) applies. The test endpoint has law π and is independent of all clean training trajectories. Because edits do not change U, this remains true after any allowed attack, even one depending on the training data. Thus

 R ≤ Σ_(u:π_u>0) π_u[1/sqrt(Tπ_u)+2/(Tπ_u)+16/(Tπ_uβ)]
   ≤ 2/sqrt(T)+8/T+64/(Tβ),

where Σ_u sqrt(π_u)≤2. The loss cap gives (1).

## Proof of (2), with exactly the same training input

Let V_i=(X^i_{M−1},X^i_M) and B_i=X^i_{M+1}. Stationarity and independent restarts give iid V_i∼π and P(B_i=1|V_i=u)=p_u, independent across episodes. For row u let n_u and c_u be their occurrence and one counts. Conditional on n_u, c_u is Bin(n_u,p_u); when n_u=0, q^end_u=1/2. Therefore

 E[|q^end_u−p_u| | n_u]≤[sqrt(n_u)/2+1]/(n_u+2)
                            ≤3/[2 sqrt(n_u+1)].

For π_u>0, n_u∼Bin(N,π_u), and

 E[1/(n_u+1)] = [1−(1−π_u)^(N+1)]/[(N+1)π_u]
                 ≤1/[(N+1)π_u].

By Cauchy–Schwarz, weighting by the independent test endpoint π and summing over four rows gives 3/sqrt(N+1). No conditional iid claim is made about all transitions in a single trajectory.

## Rate check for the shared-source interface

The pooled upper is minimax-sharp in order when N≥M and b=1/M, even if a competing predictor is given the entire clean test word and no attack occurs. Restrict the unknown common source to iid Bernoulli θ_±=1/2±d, with d=1/[16 sqrt(m)], m=(N+1)(M+2). These sources are in the critical class because P²(x,·)=π. All N training words and the complete test word together are m iid Bernoulli symbols. Their product KL is at most 32m d²=1/8, since KL(Ber(p)||Ber(q))≤(p−q)²/[q(1−q)] and θ_+(1−θ_+)≥1/8. Pinsker gives total variation ≤1/4, and midpoint testing yields

  max_± E|q−θ_±| ≥ 3/[128 sqrt(m)].                           (5)

This includes any randomized or source-independent predictor, not merely counters, and even grants the full unedited test interior. An attacker can always choose identity, so (5) lower-bounds worst-attack minimax risk as well. For N,M≥1, m≤6NM; for N≥M the pooled upper is ≤74/sqrt(NM). Consequently the minimax rate in that regime is Θ((NM)^−1/2), with very loose upper/lower constants. This does not prove the extra 1/(NMβ) term in (1) is needed when N<M, and no matching claim is made for that regime.

## Why source reuse, starts and information matter

The same θ across training and test, stationary independent restarts, and independence of test from training conditional on θ are essential to the above proof. If θ is a random latent kernel but fixed once and reused for all episodes, all bounds apply conditionally and hence after averaging. If a fresh θ is drawn independently for each episode, pooling does not estimate the test kernel.

For a simple fresh-source counterexample to applying (3), draw each episode independently from iid Bernoulli θ∈{1/4,3/4} with equal probabilities and stationary starts. On a fresh test word, U=01 has probability 3/16 under either source, so even given U=01 and any amount of independent prior-episode data, the test source posterior remains equally weighted. Every predictor based only on training data and U has conditional expected error at least 1/4, hence risk at least 3/64. This remains true at k=0. A predictor allowed the rest of the *test* history gets additional information, so this is not an impossibility for full-word meta-learning.

If the test starts from an arbitrary initial law while training episodes start stationary, its endpoint law need not equal π. The π-weighted risk calculation above then does not apply. No arbitrary-start or source-resampling extension is claimed here. Similarly, a single recurrent source that evolves continuously across training episodes without independent restarts need not satisfy the variance decomposition used in (4).

## Resource and prior-art accounting

Full input acquisition is N(M+2) clean training symbols and M+2 test symbols if the test interface streams the whole word. Pooled J_u,C_u are eight exact counters, each ≤NM, so O(log(NM+1)) stored bits for the fixed four-row alphabet, plus O(log M) positional/index bits; this is paid trained state, not free weights. A simple conservative implementation uses O(NM log(NM+2)) bit operations for counting and O(p²) final long-division work for output precision p=O(log(NM+1)+log(1/η)), yielding additive output error η. The η term must be added to (1)–(3). The final test access can be only the endpoint if a separate indexed-access interface grants it, but reading the streamed word still costs M+2 input symbols. N=Θ(M) consumes Θ(M²) clean training symbols. The competing endpoint estimator uses the identical input set and can use O(log N) count bits; it may discard the rest only after paying acquisition or under an explicitly different last-triple access contract.

Leskelä and Dreveton, *Robust estimation of a Markov chain transition matrix from multiple sample paths*, https://arxiv.org/html/2506.20325v2, model and Theorems 3.1 and 3.5, provide substantial primary prior art on pooled transition estimation from independent Markov trajectories, including fully corrupted whole trajectories. Their matrix loss, spectral/mixing assumptions and corruption experiment differ; this note's elementary stationary endpoint-weighted bound is not a novelty claim. The project B.3 proof also uses stationary occupation variance plus mixing (source `positional_manuscript_consolidated_20261103/sections/proofs_negative.tex`, SHA-256 c33000a5e7b98eb395d8ccae7c104b60d4cf7d30900607d64f4102c9bf9302c7). The endpoint-only benchmark and its interface distinction are recorded in `shared_source_vs_fresh_prior_20261103_1031/BASELINE_AND_COROLLARY.md` and its review correction. This work changes the data available relative to the accepted one-test-word theorems; it neither refutes them nor assumes a free training set.
