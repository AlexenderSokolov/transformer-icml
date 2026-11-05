# Independent review: finite overlap under minority erasure

Review time: 2026-11-05 13:15:17 UTC.

Disposition: **PASS for the stated overlap-weighted finite-alternative comparison.** The result is not a one-sided true-output risk bound, does not justify output-dependent fitting, and does not establish a minimax estimator.

## Exact binding

The complete frozen candidate was independently read:

- `KNOWN_CHANNEL_minority_erasure_finite_overlap.candidate.v1.md`
- SHA-256: `6e3665f563a7fb0f0f1c7033d9024fae4a240621875c805e348a5aed90e0004d`

No amendment was required. Approval binds these current bytes, not other revisions or an inferred historical state. The reviewer did not edit the candidate.

The derivative dependency is `KNOWN_CHANNEL_one_edit_minority_erasure_score.candidate.v1.md`, SHA-256 `b165999503367d3c46f9dfdb6ab6d4c140f19b923dd87ec72aec94c5bcdd5ae8`, with independent review SHA-256 `f7c71ec716a1bdc56bc76a5cac48052f0ef1c9a79dad705de17626c124679921`.

Throughout this review, pair-chain transition kernels and stationary full raw-word laws are distinguished by context, as in the candidate. The squared row Hellinger quantity is unnormalized: sum_c(sqrt(p_c)-sqrt(q_c))^2, without a factor one half.

## 1. Quantifiers and fixed orientation

The assumptions are two positive stationary binary order-two sources, a fixed finite bound B on their transition-entry log ratios, and a base source theta_0 with D2(beta) and pi_0(1)<=1/2. The proof does not need theta_1 itself to satisfy the original beta certificate or the minority-label condition; it supplies a weaker common certificate along the entire path.

The common channel has one base state, the separately charged actual one-edit counter, fixed public time hazards, and no nonterminal 0-to-1 edits. Its behavior is independent of the unknown source. The two endpoint positions may flip either bit within the strict budget. No source-dependent relabeling, hidden mode, or source-specific channel is used.

B bounds relative entry changes rather than absolute probabilities. The theorem permits probabilities tending to zero with the horizon, provided the same beta and B bounds continue to apply. The constant is allowed to deteriorate with B. For B=0 the alternatives and their posterior targets coincide, and the asserted inequality is trivial.

## 2. Stationary path and tree comparison

For each row, the normalized geometric interpolation has positive entries, and Holder gives Z_u(t)<=1. The relative-entry assumption gives Z_u(t)>=exp(-tB). Consequently the candidate's deliberately loose entry ratios exp(-2B)<=theta_t/theta_0<=exp(2B) are valid uniformly in t.

All pair kernels have the same legal graph. Every positive spanning in-tree on the four pair states has exactly three transition factors. If all legal edge ratios lie in [exp(-D),exp(D)], each tree weight and each sum of tree weights lie within factors exp(+-3D) of the reference. Normalizing the root weights costs another factor exp(+-3D). Thus every stationary coordinate ratio lies in [exp(-6D),exp(6D)]. Structural zero edges and excluded cyclic/self-loop tree configurations are common to every parameter and cause no issue.

Applying D=2B along the path and D=B at the endpoint gives exactly the stationary ratios in (F5): 12B and 6B, respectively. Positivity of the legal binary transitions makes the pair chain irreducible; the stationary law is differentiable along the path.

For this pair chain, a two-step transition from (a,b) to (c,d) is theta_ab(c)theta_bc(d). The two transition factors therefore give the exp(-4B) comparison to the base two-step kernel. The stationary comparison Pi_0>=exp(-12B)Pi_t then yields

    P_t^2 >= beta exp(-16B) Pi_t.

The supplied path certificate beta_*=beta exp(-16B) is correct and horizon-independent. No assertion that the original D2(beta) class is geodesically convex is needed.

## 3. The erased symbol need not remain a minority

When pi_t(1)<=1/2, the reviewed minority-erasure derivative theorem applies directly with beta_*.

When pi_t(1)>1/2, the stationary coordinate comparison gives pi_t(0)>=exp(-12B)pi_0(0)>=exp(-12B)/2. The other marginal exceeds one half, so both are at least exp(-12B)/2. Therefore every stationary triple probability is at least

    beta_*^2 [exp(-12B)/2]^3 = beta^2 exp(-68B)/8.

For any strict-one-edit channel and any future-row probability g in [0,1], the independent-posterior-copy count argument gives E|Cov(g,T_abc|Z)|<=6 E g<=6. The last positive lower bound therefore converts this to a common C_(beta,B)sqrt(p_abc) bound for all eight counts on this portion of the path.

The transition-score combination, the separately controlled stationary initial-pair score, and the direct row derivative then apply with uniform constants. They require neither minority status of label 1 on this balanced portion nor a channel relabeling. Taking the larger constant for the two portions gives the stated uniform source-wise derivative estimate (F9). The proof does not assume that stationary marginals interpolate monotonically.

## 4. Raw geometric domination pays no length factor

The stationary ratios imply

    Pi_t >= exp(-12B)Pi_0,
    Pi_0^(1-t)Pi_1^t <= exp(6B)Pi_0.

Their combination is the exp(-18B) initial-pair comparison in (F10).

Every normalized path transition is at least its unnormalized geometric interpolant because its row normalizer Z_u(t) is at most one. Multiplying these inequalities over all M historical transitions introduces no penalty growing with M. Thus the stationary full raw-word law satisfies

    P_t(x)>=exp(-18B)P_0(x)^(1-t)P_1(x)^t.

This is the crucial reason there is no hidden exp(-cNB) factor. The initial stationary law has been paid for separately, rather than assumed fixed or itself equal to its geometric interpolant.

## 5. Fiber oscillation and exact output domination

For a common output z, every supported raw preimage is at Hamming distance at most one from z. Two such preimages therefore differ at at most two bits, affecting at most six historical triple positions. At each affected position the difference between the two transition log ratios is at most 2B, so the transition contribution to the oscillation is at most 12B.

The endpoint stationary-initial log ratio lies in [-6B,6B], so its difference between two initial contexts is at most 12B. Adding these gives exactly the 24B fiber oscillation in (F11). The absolute raw log ratio may grow with N; only its oscillation on one posterior fiber is bounded, and that is all the proof uses.

Since the raw sources are positive and C is common, their posterior supports on each reachable z coincide. Channel factors cancel from the posterior density ratio. Normalizing a function whose logarithmic oscillation is at most 24B puts that density ratio in [exp(-24B),exp(24B)]. Hence its t-power average under the first posterior is at least exp(-24B), proving (F12). Sums may be restricted to C(z|x)>0, so channel zero entries do not create undefined powers or likelihood ratios. Every reachable output is positive under all path sources.

Applying the channel to the raw geometric bound and factoring out the two output probabilities gives the posterior geometric-affinity factor exactly. Combining its lower bound with the initial 18B cost gives

    P_t^Z(z)>=exp(-42B)P_0^Z(z)^(1-t)P_1^Z(z)^t
             >=exp(-42B)min{P_0^Z(z),P_1^Z(z)}.

Thus the exponent 42B is correct. No unproved reversal of data processing, deletion of a channel normalizer, or replacement of a sum of minima by a minimum of sums occurs. This output domination itself uses only the common strict-one-edit fiber property; the one-sided S=1 restriction enters the derivative bound.

## 6. Integration and weighted Hellinger length

For each finite N, there are finitely many outputs. On every reachable output, the source-specific posterior next-1 probability is a differentiable function along the positive path. The channel is held fixed and future blind. Pointwise integration and the fixed overlap domination therefore give

    sum_z min(P_0^Z,P_1^Z)|p_1-p_0|
       <=exp(42B) integral_0^1 E_(P_t,C)|dot p_t(Z)| dt.

This is a legitimate conversion from changing source-wise observation measures to one fixed overlap measure. The direct future-row derivative and full stationary initial-law score are already included in the imported derivative bound.

Geometric row interpolation is linear in log odds, with derivative Delta ell_u. The stationary ratio contributes exp(12B), and the success/failure ratio bounds contribute exp(4B), giving

    I_step(t)<=exp(16B) sum_u Pi_0(u)q_0,u(1-q_0,u)(Delta ell_u)^2.

For r in [exp(-B),exp(B)], the mean-value bound for log on the square-root interval gives |log r|<=2exp(B/2)|sqrt(r)-1|. Squaring the difference of the success and failure log ratios costs a factor two. Multiplication by q_0(1-q_0) leaves

    8exp(B)[(1-q_0)(sqrt(q_1)-sqrt(q_0))^2
                  +q_0(sqrt(1-q_1)-sqrt(1-q_0))^2],

which is at most 8exp(B) times the declared row Hellinger square. Consequently (F16) and

    I_step(t)<=8exp(17B)d_H^2

hold with the written constants. Integrating its square root over the unit interval proves (F3). If D_(beta,B) denotes a valid uniform coefficient in (F9), an explicit sufficient final coefficient is exp(42B)sqrt(8exp(17B))D_(beta,B). It is finite for fixed beta,B and independent of N and the channel hazards.

## 7. Limits of the finite result

The proved loss is weighted by the actual output-law overlap min(P_0^Z,P_1^Z). It is not E_(P_0,C)|p_1-p_0|. A trivial conversion to that one-sided expectation adds an observation total-variation term, which need not vanish at the usual estimation scale.

The second source is fixed throughout the sum. Substituting theta_hat(z) would select a different alternative at each output and is not justified by this integrated inequality. Nor does add-one smoothing automatically give a uniformly bounded B when true rare transition probabilities are very small. Boundary sources are excluded from this positive-source path argument and require separate treatment in any estimator theorem.

No testing, aggregation, or fitted-model construction is supplied. The result therefore does not close the restricted fitted minimax problem or the unrestricted-position S=1 problem, and it makes no matching-lower or state-separation claim.

## Preservation and activity

All checks were mathematical reading and reasoning. File inspection and SHA-256 checks were used solely for document integrity. The candidate and earlier source notes were not edited by the reviewer. No scientific executable check, simulation, numerical diagnostic, model run, public write, or external disclosure occurred. No computational-efficiency, transformer, finite-precision, training, or novelty claim is approved.
