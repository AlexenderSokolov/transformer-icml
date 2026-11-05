# Independent review: finite-family likelihood selection

Review time: 2026-11-05 13:27:09 UTC.

Disposition: **PASS for the supplied finite-family prediction guarantee and its fixed-size local root-M consequence.** This is an actual statistical estimator for the stated realizable finite experiment, not a theorem for the continuous unknown-source class.

## Exact binding

The complete amended addendum was independently read and hashed:

- `KNOWN_CHANNEL_minority_erasure_finite_testing.addendum.v1.md`
- SHA-256: `b99dea7f32b788bab94cc6ebf546c734ccf640b99aff39e01f3f9f46572a18b0`

The final version explicitly inherits N=M+2 and M>=2, handles unreachable outputs, and makes beta, B, and family-size uniformity explicit in the asymptotic corollary. Approval binds these current bytes, not the earlier version's hash.

The finite-overlap dependency is unchanged:

- Candidate SHA-256: `6e3665f563a7fb0f0f1c7033d9024fae4a240621875c805e348a5aed90e0004d`
- Independent review SHA-256: `8ca84808546998646e1638f77a1f0a92c3946eb6473e25803a8569b95d07d0ba`

## 1. The statistical experiment is well specified

The supplied family is public and fixed before observing Z, and the true source is one of its members. All members are positive stationary binary order-two sources in D2(beta), share the public minority orientation pi_j(1)<=1/2, and have uniformly bounded pairwise transition-entry log ratios B.

The physical channel C is the same under every candidate. It is source independent, one-base-state with a separately charged actual one-edit counter, and forbids nonterminal 0-to-1 changes. Its endpoint behavior may otherwise be arbitrary within the strict budget. The source-dependent output laws P_j^Z are induced by different raw source laws through this same kernel; they are not different source-specific channels.

Each candidate's stationary law, output likelihood, and own next-symbol posterior are mathematically specified. The target p_j is the source-specific conditional next probability under candidate j, not a posterior average over an unknown source index. No computational-efficiency or exact-arithmetic resource guarantee is required for this statistical construction.

All channel-reachable outputs have positive likelihood under every positive candidate. Unreachable outputs have zero probability under every member and can receive any prediction in [0,1]. Fixed tie-breaking makes the maximum-likelihood selection a source-independent measurable function of Z.

## 2. Wrong-selection likelihood dominance gives precisely the needed weight

Fix the true candidate j. If the likelihood rule selects j, its prediction equals the target p_j and the loss is zero. Thus the risk splits exactly over the selection events for k!=j.

On the event selecting k, maximum likelihood gives P_k^Z(z)>=P_j^Z(z), including ties. Consequently

    P_j^Z(z)=min{P_j^Z(z),P_k^Z(z)}

on that event. Multiplying by the nonnegative prediction difference and enlarging the event to all outputs gives the displayed pairwise-overlap upper. No likelihood ratio, prior factor, factor one half, or additional testing-error multiplier is needed.

Applying the already reviewed finite-overlap theorem separately to each fixed ordered pair (j,k) yields

    Risk_j(q_C)<=C_(beta,B) sum_(k!=j) d_H(theta_j,theta_k).

The same constant applies to all pairs because beta and B are common. Maximizing over j gives exactly the stated bound. Since predictions and targets lie in [0,1], the bound can also be capped at one.

The metric is directed through its stationary weights: d_H(theta_j,theta_k) uses Pi_j. The proof does not silently assume symmetry. For two candidates, taking the maximum of the two directed distances is therefore correct.

Although the selected index is data dependent, this argument does not substitute an output-dependent alternative into a theorem proved only for fixed sources. It partitions the loss into finitely many events, applies a fixed-source theorem to each pair, and uses a pointwise dominance property on the corresponding event. A family itself selected from the same data would require a different argument.

## 3. Family size and the root-M consequence

If the maximum directed pairwise distance is D, the displayed sum is at most (L-1)D. The proof pays this number of competitors, not its square root or logarithm. The more precise maximum-sum expression in the addendum is valid and can be smaller than this diameter bound.

For L=2 there is one competitor in either risk, giving the stated finite-family minimax upper through this explicit predictor. For fixed beta, B, and uniformly fixed or bounded L, a uniform directed diameter O(M^(-1/2)) gives an actual root-M prediction bound. The sources may remain positive while their transition probabilities approach zero with M; no fixed transition floor is assumed.

The final clarification about B is necessary and correct: B_M being finite separately at each horizon is not enough if it grows, since the overlap constant depends on B. The local distance and family-size constants must likewise be uniform for the asserted rate. Classification of the true source need not become consistent; the proof controls the incurred prediction loss directly on the overlap where a competing model wins.

## 4. No continuous-class or misspecification conclusion

The guarantee assumes that the true source belongs to the supplied family. It does not automatically handle a nearby source outside the family, a random data-built candidate set, or a continuous likelihood maximizer.

A growing grid pays its competitor sum in this proof. Covering a full parameter class would additionally require controlled localization or aggregation, approximation/misspecification analysis, uniformly valid relative-ratio control for rare rows, and boundary-source treatment. The addendum correctly leaves those steps open.

The common-channel bound is uniform over the stated legal channel class, with the predictor allowed to use the disclosed C. This does not extend it to majority-to-minority insertions or the unrestricted S=1 experiment.

## Preservation and activity

This review involved only mathematical reading and reasoning, private review writing, and file integrity checks. No scientific executable test, simulation, numerical diagnostic, model run, public write, or external disclosure was performed. The reviewer did not edit the addendum or the approved overlap candidate. No historical hash inference, resource-optimal implementation, transformer, finite-precision, training, or novelty claim is approved.
