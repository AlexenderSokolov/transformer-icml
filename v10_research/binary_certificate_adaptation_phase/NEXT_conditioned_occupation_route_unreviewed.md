# Open route after constant crossing: condition on occupation, then reuse clean risk

2026-11-02. UNREVIEWED research heuristic, not an accepted bound, proof dependency or claimed lower theorem. KH004's candidate and KH003's frozen baseline are unchanged.

## Why the current sufficient window range is limited

At beta=1/M the constant-crossing proof uses an occupation variance upper of order j²/k. It demands concentration at tolerance k with constant success for every j up to order M, hence the sufficient requirement k³/M²->infinity. The original constant boundary windows also need r k/M->0. Their simultaneous sufficient range is r=o(M^(1/3)).

This is a limitation of those sufficient inequalities, not a proved impossibility of extending the family or a sharp observation-resource threshold. A variance upper bound alone cannot establish a small-ball lower or necessity.

## A genuinely new but unfinished conditioning option

One could define the auxiliary kernel by sampling a clean source conditional on both the endpoint/window event and an occupation tolerance |J00-j|<=O(k), rather than drawing from the endpoint-conditioned law and accepting with constant probability. Such an auxiliary conditional law is a legal finite stochastic map if its probabilities are fixed publicly, but the clean-risk denominator MUST include this additional event probability. Repeated-until-success sampling cannot be treated as if the old acceptance probability remained unchanged.

A heuristic local-normal scale under constant crossing is occupation standard deviation j/sqrt(k). When j is much bigger than k^(3/2), a tolerance-k event might have probability of order k^(3/2)/j. Combined with the stationary endpoint weight j/M, this suggests joint probability of order k^(3/2)/M. These orders are NOT proved here.

Using separate per-j clean sources would then accumulate a penalty roughly S M/k^(3/2), which is not free; even this heuristic only changes the useful budget requirement, not automatically removes it.

## Possible common-parameter repair

A fixed family with b=e=1/2 and approximately fixed tau of order k/M can vary a over a common interval, with expected00 occupancy of order k/a. For a given j, an a interval of order k/j may be used. If the conditioning event includes |J00-j|<=O(k), then at a fixed clean word only O(k) integer j can match. Integrating over the SAME a before invoking clean risk could exploit that overlap, analogous in spirit to accepted BK002's same-a accounting.

A rough density/overlap calculation suggests a penalty like S/sqrt(k) times a logarithm rather than separate per-j penalties. This is only a heuristic: source normalization, stationary masses, the exact a support, the rare-event lower bound, density directions, and the joint window/occupation event all still require proof. A guessed common prior does not permit subtracting S once without these weights.

A rigorous uniform occupation small-ball lower for the actual endpoint-conditioned Markov paths is the missing ingredient. Possible approaches include an explicit diagonal-excursion/negative-binomial decomposition or exact Markov-type likelihood integration. Neither has been completed. A reference family with deterministic10->00 would violate all-state minorization unless repaired; if used only as a reference its full-word likelihood cost must be charged.

## Scope

If this route worked, it might increase the boundary-window range, perhaps toward r=o(sqrt(M)), by allowing budgets only moderately above sqrt(M). That is a target, NOT a theorem or prediction of the true sharp threshold. The full-history supplied-beta critical question remains separate. Even a larger boundary result would still concern exact triples plus two boundary windows, not arbitrary interior higher-pattern summaries or neural local-radius encoders.
