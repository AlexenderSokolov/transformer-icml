# Gauge-centered realized key budgets for the D-stage risk bridge

2026-11-12. Strict relaxation of the realized-global-key hypothesis in the reviewed fixed-D bridge. This note proves the centered-prefix replacement, its uniform and nonuniform recursions, and the limits of its N-dependence. It does not remove homogeneous-value/residual or decoder-bypass restrictions and is not a generic low-rank lower bound.

## 1. Exact gauge quotient and a sharper deterministic estimate

At a causal query with i keys, let K_i have rows k_j, q be its actual query, and P_i=I_i-11^T/i. Write bar_k_i=i^-1 sum_{j<=i}k_j. Then

    softmax(K_i q)=softmax(P_i K_i q).

The removed scalar q dot bar_k_i is the SAME for every source key in this row. The identity holds pathwise even when q, the key mean, or an added common key vector depends on the word, N, query position, or earlier contextual states. It does not assume their independence. The key mean must not be separately exposed as a historical decoder input; that would be an additional bypass, not an attention gauge.

Define the realized centered prefix norm

    Fc(i)=||P_i K_i||F=(sum_{j<=i}||k_j-bar_k_i||²)^(1/2).

For the COMPLETE score vector s, define its oscillation Omega=max_j s_j-min_j s_j. If s=K_i q plus a row constant, ||P_i s||2<=||q|| Fc(i). Along softmax(ts), t in [0,1], the Jacobian has operator norm at most the maximum probability, which is <=exp(Omega)/i. Since the Jacobian annihilates constants, integration gives

    ||softmax(s)-1/i||2 <=exp(Omega)||P_i s||2/i.

For values ||v_j||<=V, the value matrix Frobenius norm is <=V sqrt(i), so

    ||Attention(s,v)-Uniform(v)||
      <=V exp(Omega)||P_i s||2/sqrt(i)
      <=V exp(Omega)||q|| Fc(i)/sqrt(i).                 (1)

This is the old near-uniform read estimate with RAW key norm replaced by the EXACT softmax-gauge centered norm. It can be materially smaller. For i=1, P_i=0 and the read difference is exactly zero; no singular boundary convention is needed.

If complete scores also have a separately supplied additive positional vector b, then P_i s=P_i K_i q+P_i b. The valid upper bound is ||q|| Fc(i)+||P_i b||2. Only row-constant biases disappear. A predecessor-indicator bias is not free. An optional bound Omega<=sqrt2||P_i s||2 follows from differences of coordinate basis vectors, but substituting it can produce an exponentially bad N-dependent constant. Keeping a uniform score-oscillation bound is consequential.

## 2. Full centered array controls every centered prefix

Let n be the full raw-plus-terminal key-array length and bar_k_n its mean. Least-squares optimality of the prefix mean gives, for every realized array,

    sum_{j<=i}||k_j-bar_k_i||²
      <=sum_{j<=i}||k_j-bar_k_n||²
      <=sum_{j<=n}||k_j-bar_k_n||².

Therefore one uniform GLOBAL CENTERED array bound ||P_n K_n||F<=Fc controls all causal prefix-centered norms, even though the prefix means differ and the terminal row may depend on the free endpoint. This is a pathwise subset-sum statement, not a probabilistic assumption about initialization. The raw arrays themselves need not have bounded Frobenius norm.

The centered quantity is invariant under K -> K+1 b^T and equals min_b||K-1 b^T||F. The original raw budget always upper-bounds it, but the converse fails. For example, identical nonzero keys k_j=b have raw norm sqrt(n)||b|| and centered norm zero. Such a constant key can arise from an ordinary fixed nonzero affine key bias or LN shift. Its attention is EXACTLY uniform for any bounded query. More generally k_j=b+n^-1/2 z_j with bounded z_j has centered Frobenius O(1) but raw norm Theta(sqrt n). This is a strict enlargement of the hypothesis at the level of realized arrays, not merely a restatement of a raw norm bound.

## 3. Uniform D-stage recurrence

Retain ALL non-score hypotheses of ../../fixed_d_qk_bridge_20261112/THEOREM.md: stationary fixed-c spin source; identical token-only raw initialization; full causal prefixes; identical raw value and local residual maps at every position; a free-pair terminal visible only to itself; common bounded comparison domains and charged value/local/readout Lipschitz constants; no extra historical decoder inputs or later uncharged reads. Public position information may affect only the COMPLETE controlled score mechanism, not evade the homogeneous raw-value/residual contract.

At layer ell assume for every word, N, and row: ||q_i^ell||<=Q_ell, score oscillation <=Omega_ell, and the full realized centered array satisfies ||P_n K_n^ell||F<=Fc_ell. Constants may depend on layer/resources; any N-dependence must be retained. A prefixwise uniform bound is equally sufficient. Arbitrary uncharged additive biases are excluded; if present, a uniform centered bias norm bound Bc_ell can be added below.

With kappa_c=sqrt(4+8/c²), define

    C_ell=V_ell exp(Omega_ell)(Q_ell Fc_ell+Bc_ell),
    u_ell=L_ell Lo_ell(C_ell+kappa_c V_ell),
    B_ell=L_ell(1+2Lo_ell Lv_ell),
    E_0=0, E_(ell+1)=B_ell E_ell+u_ell.                 (2)

Here Bc=0 unless the COMPLETE extra score term has been explicitly centered, bounded and charged. The same shared raw reference branches and terminal reference as in the reviewed fixed-D proof give

    E||h_i^ell-bar_h_ell(X_i)||<=E_ell/sqrt(i),
    E||h_T^ell-bar_hT_ell(tau)||<=E_ell/sqrt(n).

Proof change: replace exactly the deterministic first score-to-uniform comparison by (1). The subsequent actual-to-reference value comparison, fixed-c source covariance, terminal-self cancellation and prefix averaging are unchanged. No Q/K state Lipschitz assumption is introduced. The common key component is removed only from scores; actual value/residual functions still obey every original bound.

For a final Lout-Lipschitz terminal readout after D stages and equal prior theta=+h,-h, the free-pair reference depends only on tau, so

    R_equal_prior >=h/2-Lout E_D/sqrt(n),
    max(R_h,R_-h)>=max(0,h/2-Lout E_D/sqrt(n)).           (3)

If the final empirical count summary is retained rather than mean-averaged, use E_(D-1) in the earlier final-decoder variant:

    R_equal_prior>=B_N
      -G[(1+2Lv_(D-1))E_(D-1)+C_(D-1)]/sqrt(n).         (4)

No factor four is introduced because the terminal's own reference value cancels before applying the unconditional raw-source concentration inequality. These remain necessary lower bounds under their full contracts, not matching constructions.

## 4. Nonuniform prefix profiles and N-dependence

If centered budgets or queries vary with prefix length, define a deterministic envelope

    T_ell(i)>=sup_word exp(Omega_ell(i))
                   [||q_i^ell|| Fc_ell(i)+||P_i b_i^ell||2].

A uniform pointwise recursion, without forcing this into a constant, is

    e_i^(ell+1)<=L_ell e_i^ell
      +L_ell Lo_ell Lv_ell i^-1 sum_{j<=i}e_j^ell
      +L_ell Lo_ell V_ell [T_ell(i)+kappa_c]/sqrt(i).     (5)

The terminal is index n with its own reference and the same bound. This positive triangular recursion is the precise statement when a single uniform E_ell is unavailable.

For a useful special case, suppose T_ell(i)<=t_ell i^beta for every i, with fixed 0<=beta<1/2, and let alpha=1/2-beta. Since i^-1 sum_{j<=i}j^-alpha<=i^-alpha/(1-alpha), setting A_0=0 and

    A_(ell+1)=L_ell[1+Lo_ell Lv_ell/(1-alpha)]A_ell
               +L_ell Lo_ell V_ell(t_ell+kappa_c)

yields e_i^ell<=A_ell i^-alpha. This gives a decaying source-average approximation at fixed D. At beta=1/2 this argument no longer yields decay. If Omega itself grows with i, its exponential factor is part of T; it cannot be silently omitted.

Alternatively, if the centered GLOBAL norm bound is Fc_ell(N), simply keep it inside C_ell(N) and E_D(N). Nonvacuity requires Lout E_D(N)=o(sqrt N), or the desired explicit finite inequality. Fixed D and bounded other gains with Fc_ell(N)=O(N^beta), beta<1/2, give O(N^(beta-1/2)) approximation; this is not a claim with an N-independent E_D. If D grows, products of the B_ell must also be charged. Standard per-row key bounds permit centered norm Theta(sqrt N), which can still make the bridge vacuous.

## 5. Scope and diagnostic

Centering strictly removes a score gauge nuisance and may turn previously vacuous raw-key bounds into useful statements. It does not control arbitrary position-dependent values, an exposed key-mean bypass, hidden global initialization, uncharged gain, or an arbitrary multi-read architecture. It also does not claim that a learned parameter Frobenius budget automatically bounds the realized centered key array.

An in-memory standard-library diagnostic used seed811, n in {1,2,3,8,32}, 20 random configurations each, and every prefix. It passed 2,760 checks: invariance under a common key shift, prefix-centered SSE<=full-centered SSE, and bound (1) for bounded scalar values. Large common shifts were included. This supports the algebraic implementation but is not numerical evidence for a nonvacuous statistical risk lower bound. The proof above is analytical.
