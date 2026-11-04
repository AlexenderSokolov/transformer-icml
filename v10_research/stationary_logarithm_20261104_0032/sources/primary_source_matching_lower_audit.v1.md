# Primary-source audit: matching terminal-KL minimax lower bound

Date: 4 November 2026 (UTC).

Status: The matching-lower-bound implication is verified. This audit checks the primary theorem, model, loss, indexing, parameter regime, and reductions. It does not replace the separate analytical review of the candidate upper bound. No numerical experiment, simulation, training, external upload, or repository mutation was performed.

## 1. Finding

For every fixed alphabet size A >= 2, Han, Jana and Wu's original higher-order result supplies an Omega_A(log n/n) minimax lower bound for expected forward KL at the actual terminal pair of a stationary homogeneous second-order source. Binary second-order sources are expressly covered by their Theorem 24, not inferred from their first-order theorem.

Consequently, if the reviewed candidate upper bound is accepted, the usual full-history add-one predictor has worst-case risk Theta_A(log n/n), both over stationary sources and over the larger class with arbitrary initial-pair distributions. This is an asymptotic fixed-A minimax statement. It is not an assertion of optimal alphabet dependence, a lower bound at every individual source, or a lower bound for every prescribed initial distribution.

## 2. Materials and exact bindings

Candidate examined:

`tilted_occupation_terminal_kl.candidate.v1.md`

SHA-256:

`c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281`

Primary publication:

Yanjun Han, Soham Jana and Yihong Wu, "Optimal prediction of Markov chains with and without spectral gap," IEEE Transactions on Information Theory 69(6), 2023, pp. 3920-3959.

- Published DOI: https://doi.org/10.1109/TIT.2023.3239508
- Author preprint: https://arxiv.org/abs/2106.13947v2
- Author-preprint HTML: https://arxiv.org/html/2106.13947v2

The published PDF was read locally at:

`[preparation path omitted; see the DOI and source identity]`

Its SHA-256 is:

`375c730cb4c9f6dd2eaa4439e59800764faeddbebee73f220e22d6d2cf3116a3`

The online author-preprint theorem statements were cross-checked against the published PDF. Published theorem numbers 22 and 24 agree with the preprint, but some equation numbers differ.

## 3. Primary-source locations and hypotheses

### 3.1 Model and loss

Published Section V-A, pp. 3941-3942, defines a homogeneous order-m process by a fixed stochastic array with A^m rows and A columns. Its initial law is a distribution on the first m symbols. Stationarity is a condition on this initial law and the fixed transition array.

Published Eq. (103), p. 3942, defines the minimax risk using the forward KL loss at the actual terminal m-symbol context:

    R_{A,N,m}
      = inf_{Mhat} sup_M
          E[D_KL(M(. | X_{N-m+1},...,X_N)
                   || Mhat(. | X_{N-m+1},...,X_N))].

The observed trajectory has N symbols and is started from a stationary distribution. The estimator is a function of the complete observed trajectory, not merely its final context. Writing it as a collection of estimated rows does not restrict that dependence.

This is the desired terminal expected forward KL. It is neither cumulative prediction loss nor an average over an independently sampled test context. The preprint counterpart is Section 5.1, Eq. (95).

### 3.2 Higher-order theorem

Published Theorem 22, p. 3942, states: for each m >= 2, there exists C_m > 0 such that, for

    2 <= A <= N^(1/(m+1)) / C_m,

    A^(m+1)/(C_m N) * log(N/A^(m+1))
      <= R_{A,N,m}
      <= C_m A^(m+1)/N * log(N/A^(m+1)).

The lower bound continues to hold when the sources are required to be reversible. C_m depends only on m, not on A or N. Thus at m=2 the constant C_2 is absolute.

No positive lower bound on transition probabilities, stationary masses, or spectral gap is imposed for this theorem. Its domain is a restriction on the alphabet size relative to sample length. The reversibility here is reversibility of the symbol process; it should not be confused with ordinary reversibility of the overlapping-pair chain.

### 3.3 Explicit binary theorem

Published Section V-C1, pp. 3944-3945, Theorem 24 states

    R_{2,N,2} = Theta(log N/N).

The published proof uses a one-parameter binary second-order family, Eq. (111), with rows ordered 11,21,12,22:

    M_p(. | 11) = (1-1/N, 1/N),
    M_p(. | 21) = (1/N, 1-1/N),
    M_p(. | 12) = (1-p, p),
    M_p(. | 22) = (p, 1-p),
    0 <= p <= 1.

For each p, the stationary pair law is uniform on {11,12,21,22}. The proof places a uniform prior on p and extracts a harmonic-sum lower bound from selected trajectories; its terminal-risk conclusion is Eq. (117), p. 3945. Thus the binary result is established within the required structured second-order family and with a common stationary initial law.

The preprint counterpart is Section 5.3.1, Theorem 24. The general-alphabet construction in published Section V-C2 / Theorem 26 is explicitly the A >= 3 case and is not needed to justify A=2.

## 4. Exact indexing and fixed-A threshold

The candidate observes X_1,...,X_{n+2}, with n observed transitions and terminal pair

    Y_n = (X_{n+1},X_{n+2}).

HJW use N for the number of observed symbols. The exact substitution is therefore

    N = n+2,  m = 2,  k = A.

Then their final context is the candidate's Y_n, and their next symbol is X_{n+3}. Hence, writing R_A^stat(n) for the candidate-indexed stationary minimax risk,

    R_A^stat(n)
      >= A^3/[C_2(n+2)] * log[(n+2)/A^3]

whenever

    n+2 >= (C_2 A)^3.

For every fixed A, this gives Omega_A(log n/n) as n tends to infinity. For an explicit sufficient large-n comparison, additionally require n+2 >= A^6. Then

    log[(n+2)/A^3] >= (1/2) log(n+2).

The absolute constant C_2 is not numerically specified by the theorem statement. No numerical value or all-n guarantee is invented here. The displayed logarithm and domain must be retained in any finite-sample or growing-alphabet restatement.

## 5. Why a terminal predictor is covered

An arbitrary prediction rule q(X_1,...,X_N) in the A-symbol probability simplex can be represented as a row-valued estimator: put q in the realized terminal row and assign arbitrary probability vectors to the other rows. HJW's infimum over row-valued estimators therefore covers every history-dependent probability-vector predictor used here.

If a predictor has internal randomness, conditional averaging of its output cannot increase forward KL, by convexity in the predicted distribution. Randomization therefore does not evade the minimax lower bound.

In particular, the lower bound applies to the full-history add-one output, and also to a normalized architecture output if a separately verified upper bound is available for that output.

## 6. Extension to arbitrary initial-pair distributions

Let R_A^all(n) be the minimax risk when both the kernel and the initial-pair distribution are arbitrary. The stationary parameter set is a subset of this larger parameter set. Thus

    R_A^all(n) >= R_A^stat(n).

Let B be the full-history add-one predictor. The candidate upper bound gives

    sup_{all initial laws and kernels} E D_KL(p_{Y_n} || B)
      <= U_{A,n},

where U_{A,n} = O_A(log(n+2)/(n+1)). Therefore

    R_A^stat(n)
      <= R_A^all(n)
      <= sup_all E D_KL(p_{Y_n} || B)
      <= U_{A,n}.

Furthermore,

    R_A^stat(n) <= sup_stationary E D_KL(p_{Y_n} || B).

Together these inequalities prove the claimed fixed-A minimax-rate match for both classes, conditional on the upper-bound theorem. The stationary lower bound is sufficient because a worst case in a smaller class is still a valid worst case in the larger class.

This does not imply a lower bound for every prescribed initial distribution, every deterministic starting pair, or every fixed transition kernel. The supremum is taken separately at each sample length, and the hard source may depend on that length, as the displayed binary construction does.

## 7. Correct direction of alphabet embedding

A lower bound over a larger alphabet does not imply a lower bound for the binary subclass. The valid monotonicity goes in the other direction.

Embed any stationary binary second-order source in [A] by setting probabilities of symbols 3,...,A to zero and supporting the initial pair on {1,2}^2. Define unused rows arbitrarily. This is allowed in the candidate class, which permits zero probabilities and reducibility.

For any A-symbol prediction q and binary-supported true row p, set

    z = q_1+q_2,
    q' = (q_1/z,q_2/z)  if z>0.

For z>0,

    D_KL(p || q) = D_KL(p || q') - log z
                >= D_KL(p || q').

If z=0, the A-symbol loss is infinite, so the inequality is harmless after choosing any binary q'. This pointwise reduction maps every A-symbol estimator to a binary estimator. Taking the supremum over binary sources and then the infimum over estimators yields

    R_{A,N,2} >= R_{2,N,2}.

Thus Theorem 24 alone gives a matching order in N for every fixed A>=2. This alternative argument does not recover the sharp A^3 factor of Theorem 22, but it is sufficient for fixed-A optimality in n.

An unrelated shortcut is also invalid: applying a lower bound for arbitrary ordinary A^2-state chains does not automatically lower-bound the structured pair chains coming from an A-symbol second-order source. HJW's actual higher-order theorems avoid that issue.

## 8. Exceptions and scope limits

1. Binary first-order sources have a different stationary minimax rate, Theta(log log N/N), recalled in published Eq. (2), p. 3921. This does not contradict the binary second-order theorem.
2. The conclusion is minimax optimality in sample length for fixed A. The candidate's leading upper-bound dependence is A^5, whereas the sharp stationary theorem has A^3. No growing-A optimality follows.
3. This audit verifies the lower theorem's applicability and the reductions above. It is not a claim of literature priority, a survey of subsequent work, or a new proof of every step in HJW.
4. The candidate's upper-bound acceptance must be determined by its independent exact-file analytical reviews. This audit supplies the matching lower half and does not silently promote an unreviewed upper theorem.

## 9. Safe summary sentence

For each fixed A>=2, the verified full-history add-one upper bound matches the stationary second-order minimax lower bound of Han, Jana and Wu in its dependence on sample length; since stationary sources form a subset of sources with arbitrary initial-pair laws, it also establishes minimax-rate optimality over that larger class. The result does not establish sharp alphabet dependence or a pointwise lower bound for every source or initial law.
