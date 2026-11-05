# A finite-candidate prediction guarantee from the overlap bound

5 November 2026 UTC. Pure analytical addendum, pending independent review. No scientific execution or public write. This gives a statistical estimator only for a supplied finite source family, not for the full unknown-source class.

## 1. Experiment

Let N=M+2 with M>=2, as in the finite-overlap theorem. Let Theta={theta_1,...,theta_L}, L>=2, be a public finite family of positive stationary binary order-two sources. Every member belongs to D2(beta) and has pi_j(1)<=1/2. Assume every pair of transition tables has log-entry ratio bounded by the same finite B.

Use one fixed common disclosed S=1, strict-one-edit online channel C, with actual counter e in {0,1}, no nonterminal 0-to-1 edits, and arbitrary legal endpoint edits. The channel is independent of the unknown source index.

For each candidate j, its output likelihood P_j^Z(z) and its own next-symbol posterior p_j(z) are mathematically determined by the disclosed model and channel. This statement makes no resource-optimal implementation claim.

## 2. Maximum-likelihood source selection yields an actual predictor

Let

    j_hat(z) be a maximizer of P_j^Z(z),
    q_C(z)=p_(j_hat(z))(z),

using a fixed source-independent rule for ties. Every channel-reachable output has positive probability under every positive candidate; define q_C arbitrarily on outputs unreachable under all candidates. Under a true candidate j, on every event {j_hat=k},

    P_k^Z(z)>=P_j^Z(z).

Therefore

    Risk_j(q_C)
      =sum_(k!=j) sum_(z:j_hat(z)=k)
                    P_j^Z(z)|p_j(z)-p_k(z)|
      <=sum_(k!=j) sum_z min{P_j^Z(z),P_k^Z(z)}
                                      |p_j(z)-p_k(z)|.

Applying the finite overlap comparison gives

    max_j Risk_j(q_C)
       <= C_(beta,B) max_j sum_(k!=j) d_H(theta_j,theta_k),

up to the unit cap. Each d_H uses the stationary pair weights of its first argument, as in the finite-overlap note. The proof does not substitute a randomly fitted candidate into a theorem for fixed laws: it partitions the risk into finitely many fixed-candidate selection events, and likelihood dominance supplies the overlap weight on each event.

## 3. Precise local consequence and limitation

For L=2, the finite-family minimax prediction risk is at most

    C_(beta,B) max{d_H(theta_1,theta_2),d_H(theta_2,theta_1)}.

For fixed beta and B uniformly in M, a supplied two-source family with these distances O(M^(-1/2)) therefore has an actual root-M posterior-prediction upper, even when its transition probabilities vanish with M. More generally, with beta, B, and L fixed uniformly in M, a family of diameter O(M^(-1/2)) has the same order. A B_M that is finite at each horizon but grows with M does not by itself give a uniform root-M constant.

For a growing grid, this elementary bound pays the number of competing candidates. It does not establish that maximum likelihood over a grid or over the full continuous source class has a uniform root-M risk. A full-class proof still needs localization/testing or aggregation with controlled complexity, rare-row relative-ratio handling, and boundary sources. No such full-class theorem is asserted.

## Dependency

`KNOWN_CHANNEL_minority_erasure_finite_overlap.candidate.v1.md`, exact frozen SHA-256 `6e3665f563a7fb0f0f1c7033d9024fae4a240621875c805e348a5aed90e0004d`.
