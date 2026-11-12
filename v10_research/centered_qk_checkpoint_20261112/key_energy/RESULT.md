# Bounded parameters do not bound centered key-array energy

2026-11-12. Two explicit fixed-width, fixed-parameter constructions. The second gives a direct task-risk failure of transferring a near-uniform-read estimate from global activation norms to ordinary parameter norms. This is not a claim that bounded-parameter models must have high risk.

## A. Pure positional example

For even N, let p_i=(-1)^i and h_i=(X_i,-X_i,p_i,-p_i,1,-1). Full LN with epsilon1 and unit gain divides by sqrt(2). Fixed scalar projections Q=sqrt(2)e_4, K=sqrt(2)e_2, V=sqrt(2)e_0 (zero-based coordinates) give q_i=1,k_i=p_i,v_i=X_i. All states have norm sqrt(6), each projection Frobenius norm is sqrt(2), and scores are bounded by1. The realized key array is centered and has Frobenius norm sqrt(N). Its rank-one score matrix has a terminal row with centered l2 norm sqrt(N).

At row N, softmax weights are (1+p_i tanh(1))/N. Therefore their l1 distance from uniform is tanh(1), their l2 distance is tanh(1)/sqrt(N), and

    H_N-U_N=(tanh(1)/N) sum_i p_i X_i.

The word X_i=p_i gives a constant difference tanh(1). This alone says nothing about its probability. Under the stationary fixed-c spin source, E(H_N-U_N)=0 and

    E(H_N-U_N)^2=(tanh(1)^2/N²)
      [N+2 sum_(j=1)^floor((N-1)/3)(N-3j)(-1)^j theta^(2j)]
      <=tanh(1)^2 [(1+theta²)/(1-theta²)]/N.

This uses Cov(X_i,X_(i+k))=0 unless k is a multiple of3, when it equals theta^(2k/3). Thus large centered key energy and worst-word read difference do NOT by themselves establish an average-risk obstruction. The alternating public positional feature is explicitly supplied; no claim is made that an arbitrary restricted position embedding generates it for free.

## B. Content-key counterexample with an actual final full-LN head

Use width6 raw rows h_i=(X_i,-X_i,1,-1,0,0) and public terminal h_T=(0,0,1,-1,0,0), T=N+1. The actual endpoint pair may be disclosed but is ignored. Full LN has epsilon1, gain1, shift0. Raw LN divisor is sqrt(5/3); terminal divisor is sqrt(4/3). Choose fixed scalar rows

    Q=sqrt(4/3)e_2, K=V=sqrt(5/3)e_0.

Then raw keys/values are X_i and terminal key/value zero. Terminal query is1, raw queries sqrt(4/5). All causal scores have magnitude<=1. These are CONTENT-DEPENDENT keys, not a pure positional predecessor-score construction. The score matrix is still rank one before the causal mask.

One full causal attention head executes on every row. O writes its scalar average A_i into coordinates4,5 as (A_i,-A_i); ||O||F=sqrt(2). The FFN is zero. All post-attention raw row norms are <=sqrt(6), terminal norm<=2. Projection norms are fixed: ||Q||F=sqrt(4/3), ||K||F=||V||F=sqrt(5/3). No weights depend on N or theta.

The terminal attention output is exactly

    H_N = [sum_i exp(X_i)X_i]/[sum_i exp(X_i)+1]
        = (m_N+t)/(1+t m_N+1/[N cosh(1)]),
    m_N=S_N/N, t=tanh(1).

The realized keys are (X_1,...,X_N,0). With centering across ALL T rows,

    ||K_centered||F²=N-S_N²/(N+1).

At theta0, E S_N²=N, so expected squared energy is N-N/(N+1), and K_centered/sqrt(N) tends to1 in probability. In fact the same conclusion holds uniformly in fixed c by the variance bound above. Global key energy is therefore order sqrt(N) even though all learned projection and physical row-state norms are bounded.

Terminal residual is (0,0,1,-1,H_N,-H_N). Apply mandatory full final LN with epsilon1, unit gain and affine two-class logits(lambda*LN(h_T)_4,0), lambda=1 for the diagnostic. The exact probability map is

    Phi(x)=sigmoid(lambda*sqrt(3)x/sqrt(4+x²)).

Replacing the attention scores by zero, without changing any other parameters or residual/head operation, gives U_N=S_N/(N+1) and prediction Phi(U_N). At theta=0, the source is iid fair, the true next-plus probability is1/2, and m_N converges to0. Bounded continuity gives

    actual expected TV risk -> Phi(tanh(1))-1/2 >0,
    uniform-reference expected TV risk ->0.

Hence the expected prediction difference also tends to the same positive constant. This is a direct failure of any universal O(N^-1/2) near-uniform-read/risk transfer derived solely from these parameter/state bounds. It does NOT contradict the earlier bridge, whose necessary global realized K-Frobenius premise fails here. It is also not a lower bound on optimal architectures: setting the head to predict1/2 solves theta=0 exactly. The purpose is to test a proposed universal parameter-to-summary reduction.

## Parameter ledger and scope

For example B, initial attention matrix squared norms total4/3+5/3+5/3+2=20/3. All biases and FFN parameters are zero. Counting both block LNs (including the unused zero-FFN pre-LN) plus final LN, unit gain vectors contribute18 to squared norm. The final affine matrix contributes lambda². Thus complete layer-occurrence matrix/gain squared norm is20/3+18+lambda², fixed because depth is one. Input token/anchor features are explicitly displayed; their bounded embedding coefficients are fixed as well. There are no public positional biases in example B.

The examples distinguish parameter norms, per-row activations, and whole-array centered activation energy. They establish neither a predecessor retrieval algorithm nor a general evolving-memory lower bound, and no execution-noise robustness is claimed.
