# CB004 — Stationary full-history adaptation on and above the critical certificate curve

2026-11-02. **New complete stationary theorem candidate; fresh independent FULL review pending.** This does NOT prove arbitrary-initialization adaptation. Accepted CB001–CB003 remain unchanged. The separate proof component `balance_probe/BP001_stationary_weighted_balance.md` is part of this candidate and must be reviewed in full with it.

## 1. Result and exact estimator

Use the accepted binary homogeneous second-order source-corruption experiment. A source has an existential stationary pair law Pi satisfying P^2(i,j)>=beta Pi(j) on ALL pair states, with beta>0. Here the clean source is initialized at Pi. A source-independent offline randomized kernel replaces at most k of the first M symbols of the M+2-symbol word and preserves the final pair. The predictor sees the entire corrupted word, not k, the clean interior, mask, seed or source table. Loss is unconditional TV at the actual protected terminal row.

There is one deterministic estimator A_bal, independent of BOTH k and beta, such that for every M>=64,0<=k<=M and beta>0,

 R_stat(A_bal) <= min{1, 2^16/sqrt(M)
                    +4096/(M sqrt(beta))+2^23 k/M}. (CB4)

In particular, at beta=1/M,

 R_stat(A_bal)<=min{1,2^17/sqrt(M)+2^23 k/M}.         (CB4-critical)

The same estimator attains the accepted known-k minimax order simultaneously over every budget on every band beta>=c/M with fixed c>0, with a constant allowed to depend on c. Its input need not include beta. This is a positive result for STATIONARY initialization; the corresponding arbitrary-start weighted bias is not proved here.

Here is the complete estimator. Let n=floor(M/2). From the corrupted word, count each pair row among departures0,...,n-1 and among all departures0,...,M-1. At the preserved terminal row u, let J1' and J' be these two counts, and let C' be the full designated-successor count, with the fixed public orientations

    d(00)=1, d(01)=1, d(10)=0, d(11)=0.

If J'>0 and512 J1'>=J', output designated probability C'/J'; otherwise output designated probability0. Output the complementary probability for the other symbol. This is a total finite-rational map; no model-dependent branch or unknown budget is used. It can be computed by one ordinary sequential scan. It only needs the full triple histogram, the four first-half row counts and the protected terminal pair; it does not rely on unrestricted order information after retaining those summaries. No neural/training/compiled-resource claim is made.

## 2. Generic balanced inverse-occupation bound

This step applies to every four-state homogeneous Markov chain and every initial law, with no certificate. Write J1_u for first-half row occupation, J2_u for the remainder, J_u=J1_u+J2_u, and m=M-n. Then

 E[(J_(Y_M)+1)^-1 1{J1_(Y_M)>=J_(Y_M)/1024}]
       <=130944/M.                                 (2.1)

To prove it, fix a state u and condition on the first-half history, whose endpoint is v and whose u-occupation is j. The balance event implies J2_u<=1023j. The accepted universal terminal-occupation inequality from SC003 applied to the m-step suffix gives

 P_v(Y_m=u,J2_u<=1023j)<=16(1023j+1)/(m+1).

On this event(J_u+1)^-1<=(j+1)^-1. Since(1023j+1)/(j+1)<=1023 even for j=0, summing the conditioned prefix distribution gives a bound16368/(m+1) for each u. Sum over four u and use m+1>=M/2 to obtain(2.1). This conditions on a deterministic-time prefix, not on an IID terminal-row sample. It does not divide by a future terminal probability. For M>=128 the suffix horizon is at least64; smaller M is handled trivially in the final assembly.

## 3. Deterministic protected-corruption reduction

Let J1,J,C be the corresponding ORIGINAL clean counts at the same preserved terminal row; q is its true designated probability. These are analysis variables, not predictor inputs. Put d=6k. The accepted pointwise Hamming-to-triple perturbation bound implies

    |J'-J|<=d, |J1'-J1|<=d, |C'-C|<=d.             (3.1)

The half-count bound remains valid for edits straddling the split: every changed symbol affects at most three of the selected departure triples. Simultaneous adjacent edits do not increase the sum bound.

Define

    G'={J'>0,J1'>=J'/512},
    H={J1>=J/1024},
    B={J>0,J1<J/256},
    E=1{J>0}|C/J-q|.

### Active gate on a truly balanced row

On G' intersect H with J>0, normalization gives

    |C'/J'-q|<=E+8d/(J+1).                         (3.2)

For d=0 it is exact equality with E. For d>0 and J>=2d, J'>=J/2 and the ratio perturbation is at most4d/J<=8d/(J+1). If J<2d, the two empirical probabilities differ by at most1<=8d/(J+1). J=0 will be paid separately by a terminal-occupation tail.

### An active gate cannot hide a large truly imbalanced row

On G' intersect H^c, J1<J/1024 while J1+d>=J1'>=J'/512>=(J-d)/512. Hence

    J<1026d=6156k.                                 (3.3)

### A false gate rejection also requires a small row

On G'^c outside B with J>0, J1>=J/256. If J'=0, then J<=d. Otherwise J1'<J'/512 implies J/256-d<(J+d)/512, and hence

    J<513d=3078k.                                  (3.4)

If G' fails on B, the output is0 and the loss is q. At k=0, the two false-status cases with J>0 are impossible. Combining these cases, with harmless overlapping tail bounds that also pay J=0, gives

 R_stat(A_bal) <= E E
      +8d E[(J+1)^-1 1_H]
      +E[q 1_B]
      +P(J<6156k+1)+P(J<3078k+1).                  (3.5)

This deterministic/probabilistic reduction holds for arbitrary starts. Only the next bound on its clean weighted bias uses stationary initialization.

## 4. Stationary weighted imbalance and inherited clean comparison

The complete companion proof `balance_probe/BP001_stationary_weighted_balance.md`, fixed SHA256 `22b60eedf31f1e990e990a8b64ad733a1a3acc9723a421fdc6d677866c771271`, establishes

    E_Pi[q_(Y_M) 1_B]<=min{1,4096/(M sqrt(beta))}.    (4.1)

Its ingredients are: accepted BU001 v2 target-specific hitting bounds; an explicit positive/negative exponential return-time calculation; exact binary stationary reversal; and the exact shifted first/second-half windows. It uses the stationary Pi(s) multiplier and does not assert that row observations are IID after terminal conditioning. Full and singleton stationary supports are covered; no arbitrary-start extension or global sqrt(beta) mixing is claimed. This companion is a proof component of CB004, not a previously accepted theorem being assumed without review.

Accepted SC003's clean empirical comparator and universal terminal-occupation inequality supply, uniformly even over arbitrary starts,

    E E <=8193 sqrt(32)/sqrt(M+1),
    P(J<w)<=min{1,16w/(M+1)}, integer w>=1.         (4.2)

These are analysis interfaces, not access to the unobserved clean word by the estimator.

## 5. Assembly and all-budget profile comparison

Substitute(2.1),(4.1),(4.2) into(3.5). The corruption coefficient is

    48*130944+16*(6156+3078)=6433056<2^23.

The clean comparator coefficient plus32/(M+1) is at most2^16/sqrt(M) for M>=64. This proves(CB4) for M>=128. For64<=M<128, its displayed right side after the unit cap is1, so the bound is trivial. At beta=1/M,2^16+4096<2^17 gives(CB4-critical).

The accepted known-k profile is

 H_2(M,k,beta)=min{1,max{M^-1/2,F_2(M,k,beta)}},
 F_2=(k/M)[1+log(1+1/(k max(sqrt(beta),1/M)))], k>=1,
 F_2=0 for k=0.

Always H_2>=min{1,max(M^-1/2,k/M)}. For beta>=c/M, (CB4) is at most a constant depending only on c times this lower envelope, hence at most a constant times H_2. Conversely BT002's stationary known-k lower applies to each fixed k even when k is supplied; restricting the estimator to be k-blind cannot improve it. Thus A_bal achieves known-k minimax order simultaneously over all budgets on that band. At beta=1/M the profile is equivalent to min{1,max(M^-1/2,k/M)}; no moving-beta logarithm is being silently discarded below the critical band.

The algorithm is the SAME map across the band and all budgets, not a different k-aware invocation on clean and corrupted data. This does not contradict BK002 or the subcritical-band negative theorem: their stationary clean families share much weaker advertised beta, and(CB4)'s additional1/(M sqrt(beta)) term need not be statistical order there.

## 6. Exact scope and outstanding all-start problem

This resolves the prescribed critical-curve unknown-budget question only for stationary initialization, subject to fresh complete review and root acceptance. It is genuine full-corrupted-history adaptation with strict first-M Hamming edits, protected actual terminal pair, unknown homogeneous binary order2 source, and all-state certificate. The realized mask, seed and clean interior remain hidden.

The same algorithm's analysis for arbitrary initialization reduces to the weighted bias in(4.1), because sections2–3 and(4.2) are already all-start. That bias has NOT been established for arbitrary initial laws; stationary reversal cannot be used for them without additional work. The statement therefore does not include unsupported initial states outside stationary support. The certificate itself is still all-state, including unsupported states, exactly as required by the source model.

This result uses more than a global triple histogram: the first-half row occupations provide essential order information. It does not show that arbitrary word order is necessary, and it does not make a neural architecture, training, novelty, formal-verification or external-peer-review claim.

## 7. Provenance and current validation

Read complete accepted SC003, BT002 main/scalar proofs, AB003, BK001 and BK002 and their receipts in this research stage. Read BU001 v2's weighted-hitting/return sections for the companion premise; the companion author separately read complete BU001 v2 and its exact receipt. Read the complete BP001 companion proof before assembly. Accepted CB001–CB003 are context, not premises of this theorem. Fresh review must cover BOTH this file and BP001 and the exact inherited interfaces. No publication is performed here.
