# Exact statement — A-consistency-002/prover v1

Obligation: 67e1a38828e2a7b8f27f8a7d3d20e32b91c3c4f0e8e728035d85ad282ee1ff7d

## Original obligation, unchanged

On the exact smoothed reference and the explicitly compiled theta-independent family of the Route A actual-circuit prerequisite, prove for each fixed D1 theta that max_s TV(Pi_N(H;s),p_theta(.|s))->0 almost surely, hence actual terminal-query TV converges almost surely and in expectation despite query/history dependence. State any claim for conditional terminal-query risk separately and justify it. Determine the population limit of the specified direct matched outcome readout q_s, give necessary and sufficient equality-to-target conditions for a fixed context and all contexts, and exhibit a stationary strictly positive stochastic second-order counterexample to unqualified direct-readout consistency. Keep this theorem conditional on an admitted or self-contained actual implementation result; statistical formulas alone do not discharge the implementation prerequisite.

## Explicit theorem proved

For every fixed K>=2 and beta>0, use exactly the theta-independent finite circuit family admitted in Fact 3a69c2fa3d459b1d, with J_N=max(4,N-1), the charged rational/common-denominator probability readout and all its original resources. For every fixed D1 table theta, on one infinite trajectory started from the stationary pair law:

1. max_s TV(Pi_N(X_1:N;s),p_theta(.|s)) -> 0 almost surely and in L1.
2. Actual terminal-query TV tends to zero almost surely and in expectation. For each fixed s, its conditional expectation given s_N=s tends to zero, bounded by E[D_N]/pi_s.
3. The specified nominal A matched head q_N(s), and its vanishing-error finite implementation within the admitted family, converge simultaneously over s to (r_theta+gamma pi_s p_s)/(1+gamma pi_s), gamma=exp(beta)-1. Equality to p_s holds exactly when p_s=r_theta. Equality for every context holds exactly when every transition row is the same; under stationary D1 this is equivalent to iid symbols.
4. If b_s=TV(r_theta,p_s)/(1+gamma pi_s), then the direct head's conditional terminal risk tends to b_s, and its actual terminal expected risk tends to sum_s pi_s b_s. Its actual pathwise risk has liminf min_s b_s and limsup max_s b_s. These statements avoid assuming query/history independence.
5. For K=2, symbols +/-1, p(+1|a,b)=1/2+vartheta ab with 0<|vartheta|<1/2 and stationary pair law 1/4, the direct-head limiting TV bias is 4|vartheta|/(4+gamma)>0 in every context, including the actual terminal query. At vartheta=1/4 and beta=log(3) it is 1/6.

The finite implementation schedule and resources do not depend on theta. Mixing/frequency constants used in the proof are pointwise in theta. This theorem is for nominal finite-history inputs and TV risk; it makes no claim about arbitrary real perturbations fitting the same finite hardware, expected KL, a uniform rare-family rate, prototype B, C2/C3 completion, or root closure.

## Admitted dependency

Fact ID: 3a69c2fa3d459b1d.
Evidence ID: 83da5d4be4352713fb2833e7c7fa65a03a12797544dfce4961c393ac244bbcb9.
Fact file SHA-256: 899e13e3de35de82397926f56e26587a062e7789c726ea676465f2a1151b8132.
Original frozen implementation proof SHA-256: dc43a371ce803fdc519d8a2d662861439bd1d7b4338803fe14f777188a4a4fbf.

VERSION.json hashes this statement and exact-proof.md. Historical A-interface timeout records are not changed or resubmitted.
