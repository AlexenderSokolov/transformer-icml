# EP001 — removing the exact-terminal-symbol exemption

2026-11-02. Post-stage-seven root-authored candidate, fresh independent review required. This is a different corruption experiment, not a revision of SC001–SC003 or a claim of novelty. Frozen files remain unchanged.

## Statement and changed experiment

Fix K>=2, M>=64, 0<=beta<=1 and integer0<=k<=M. Observe N=M+2 symbols from an unknown homogeneous second-order K-letter source in the all-pair-state class D2(beta), with hidden qualifying stationary pair law Pi. The source initial pair is either Pi or arbitrary. An offline randomized kernel may replace at most k of ALL N observed symbols, now INCLUDING the final two. It is a map on complete words without unknown source parameters as inputs. Prediction sees the complete corrupted word, no mask, no attack seed, no clean endpoint exemption, and targets the TRUE source next law at the TRUE original final pair. The risk is unconditional expected TV. In particular, the target is not changed to the transition row at the corrupted pair.

Write R_end,stat and R_end,all for the corresponding minimax risks, allowing arbitrary randomized computation and public K,M,beta,k. Let s=M^(-1/2), epsilon=k/M, delta=1-beta and

    H_end=min{1,max{s,epsilon,delta·1{k>=1}}}.

There is a constant C_K depending only on fixed K such that

    H_end/96 <= R_end,stat <= R_end,all <= C_K H_end.        (E1)

One possible C_K is max{2^13 K^(5/2),sqrt(K)/2+3}. For k=0 use the ordinary clean selected-row add-one rule. For k>=1 use the pooled empirical distribution of the corrupted symbols at positions3,...,N. This deterministic estimator does not need beta; it uses k only to select these two branches. The theorem is an information/statistical result, not a claim about a particular finite neural implementation or optimal machine cost.

Thus for a fixed beta<1, allowing even ONE edit at an unprotected final symbol prevents consistency for this true-terminal target. At beta=1 the target is IID, and this obstruction disappears. This does not contradict the protected-terminal frontiers: it identifies the role of that exemption.

## 1. Marginal implication of the all-state certificate

Let pi_c=sum_d Pi(c,d), the first-coordinate stationary marginal. For each pair state u, summing P²(u,(c,d))>=beta Pi(c,d) over d gives

    theta_u(c)>=beta pi_c.

Indeed after two pair transitions, the first coordinate is precisely the next symbol generated from u. For beta<1 write theta_u=beta pi+delta r_u for a probability vector r_u; for beta=1 equality holds. Hence, uniformly over all u, including states outside stationary support,

    TV(theta_u,pi)<=delta.                              (E2)

At beta=1 every row equals pi, so the process of generated symbols is IID even if the initial pair is arbitrary.

## 2. Pooled upper when k>=1

Let e_c be the c-th unit vector and define the clean generated-symbol mean

    pbar=(1/M)sum_{t=3}^N e_{X_t}.

With the natural history filtration, let m_t=theta_(X_(t-2),X_(t-1)) and D_t=e_{X_t}-m_t. These are vector martingale differences. Distinct-time inner products have zero expectation and

    E||M^(-1)sum D_t||_2²
      =M^(-2)sum E[1-||m_t||_2²] <=1/M.

Cauchy–Schwarz and Jensen therefore give expected TV seminorm at most sqrt(K)/(2sqrt(M)) for this martingale average. By convexity and (E2), the average of m_t differs from pi in TV by at most delta on every path; the TRUE terminal next law also differs from pi by at most delta. Thus

    E TV(pbar,theta_true_terminal) <=sqrt(K)/(2sqrt(M))+2delta.

The empirical distribution pbar' of corrupted positions3,...,N changes in TV from pbar by at most k/M on every history, regardless of whether edits hit the endpoint or initial symbols. Hence the pooled predictor has

    risk <=min{1,sqrt(K)s/2+2delta+epsilon}.             (E3)

No mixing-time concentration, stationary initialization, independent query, or clean endpoint reconstruction is used.

At k=0 the existing R011 ORIGINAL add-one upper is <=2^13 K^(5/2)s for every beta and initial law. This branch is necessary in the stated bound: the crude pooled bias2delta is not a clean-sample lower. The two upper branches imply C_K H_end by capping at one and bounding each term by max{s,epsilon,delta} when k>=1.

## 3. A single common endpoint erasure gives the delta floor

Suppose k>=1. Let alpha=min{delta/2,1/4} and consider the symmetric first-order binary source embedded in the K-letter second-order class:

    T(0,0)=T(1,1)=1/2+alpha,
    T(0,1)=T(1,0)=1/2-alpha.

Unused-symbol rows, if K>2, equal the binary uniform law. Initialize the pair at its stationary law Pi(u,v)=pi_u T(u,v), pi=(1/2,1/2), with zero mass on unused symbols. The symbol minorization T(y,c)>=(1-2alpha)pi_c holds for every starting symbol, including unused ones. Therefore

    P²((x,y),(u,v))=T(y,u)T(u,v)
                   >=(1-2alpha)Pi(u,v)>=beta Pi(u,v),

because 1-2alpha>=beta. This is a legitimate stationary witness for every beta.

Use the SAME deterministic attack that sets ONLY the last observed symbol to0 and leaves every other symbol unchanged. It makes at most one replacement on every input word. On this source the observation therefore contains the true prefix through X_(N-1), but no information about X_N beyond what that prefix predicts. Grant the decoder the entire source law and stationary initialization, which can only help it.

Conditioned on the clean prefix, the true last bit has probabilities1/2+alpha and1/2-alpha, in one order depending on X_(N-1). The two possible true next-symbol laws have probabilities of symbol1 equal to1/2-alpha and1/2+alpha. For any scalar prediction z, the minimum posterior expected absolute error is the smaller last-bit probability times their gap:

    (1/2-alpha)·2alpha=alpha-2alpha².

This elementary weighted-median formula follows by checking z below, between, or above the two target values; randomized predictions cannot improve it. For any K-vector prediction q, TV(q,theta)>=|q(1)-theta(1)|, so the same lower holds even with mass assigned to unused symbols. It holds after every prefix and hence unconditionally.

If delta<=1/2, alpha=delta/2 and alpha-2alpha²=delta(1-delta)/2>=delta/4. If delta>=1/2, the loss is1/8>=delta/8. Consequently

    R_end,stat >=delta/8, k>=1.                         (E4)

At delta=0 this is zero, as it should be. The attack reads no unknown parameter and is common across all sources; the stronger lower grants full knowledge of the particular witness law. Hidden edit masks are essential: a revealed replacement indicator for this specific map could reveal the original last bit.

## 4. Statistical and corruption floors

The stationary IID Bernoulli family, with every source row equal and all unused rows defined identically, has P²=1Pi and belongs to every D2(beta). Identity attack with parameters1/2±1/(16sqrt(M+2)) gives the previously verified full-data lower s/64 for M>=64.

For k>=1, the SC002/SC003 common count-erasure kernel on the first M IID symbols is still an allowed attack here, since this larger model permits but does not REQUIRE endpoint edits. If n of these M symbols are ones, retain r=(k+1)floor(n/(k+1)) uniformly chosen ones and set the rest to zero; preserve the final two. Its edit count is at most k. The entire output arrangement is parameter-independent conditional on r and the two preserved bits, leaving at most4(floor(M/(k+1))+1) messages. The uniform-prior finite-message lemma yields risk>=k/(96M). This is a lower even though the model allows stronger attacks.

The separate stationary witnesses may differ; take their maximum. For k>=1, (E4), s/64 and epsilon/96 imply max{s,epsilon,delta}/96, hence H_end/96. For k=0 only the statistical floor is needed. Stationary initialization is a restriction of arbitrary initialization, completing (E1).

## 5. Scope

This theorem changes precisely the endpoint exemption. It does not change the prediction target to the corrupted endpoint, reveal edit locations, allow attacks on future symbols, or assert a causal-online attack model. The lower endpoint erasure is causal at its last position, but no broader online minimax equivalence is claimed. Reliable computation is still allowed without a retained-bank restriction. Fixed-K constants, growing alphabets, training, internal noise, and attribution of novelty remain separate questions. The upper requires no knowledge of Pi or source parameters; pi is only an analysis device.

Dependencies actually used: R011 ORIGINAL clean add-one interface, and SC002/SC003 stationary IID statistical/common-count-erasure floors. The new all-state marginal consequence, pooled martingale upper and known-source terminal-erasure lower are proved fully above. The proof does not depend on the unclosed binary transport question.
