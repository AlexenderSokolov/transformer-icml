# Independent review of BAI002 v1

2026-11-02. Reviewer: independent LLM reviewer. This is an independent LLM mathematical review, not external peer review or formal verification. The author file was not edited.

## Verdict

**PASS for the stated restricted-class theorem.** No blocking mathematical or scope gap found in BAI2.1 or BAI2.2. This does NOT accept or establish the complete arbitrary-start binary square-root-beta theorem.

The reviewed source and inherited accepted SB001 theorem/receipt are SHA-256-bound in `BAI002_review_source_bindings_v1.json`.

## Checks

1. **All-state source certificate.** For a=0 the00 column of P² is exactly `(1,(1-b)e,e,te)`. With e>0 and b,t in the specified compact interval, every active state can reach absorbing00, so its stationary law is uniquely delta00. Thus beta<=e min(t,1-b) is necessary and sufficient for the displayed stationary witness's full all-state certificate. No positive stationary active mass is claimed.

2. **Complete-path domination.** On a terminal-active true path, absorption has never occurred. Its density against the reflected active chain is the product of factors1-e for departures from10, and all other factors cancel. This proves domination for the entire nonnegative occupation functional with its own actual terminal query. It is valid for arbitrary initial laws by retaining the initial active subprobability and completing it only for an upper bound. The e=0 and e=1 endpoints are covered; the document explicitly interprets products to avoid relying on undefined0^0.

3. **Fixed-block count lower tail.** Direct multiplication gives the reflected R² B column `(bt,1-b,t(1-t))`, uniformly at least eta². Offset3 reaches A after the offset2 B event; offset4 reaches C with an additional b>=eta. Each selected-visit probability is therefore at least delta=eta³ conditional on its block-start history. Success indicators do not need independence: previous indicators are measurable before the next block starts, so the iterated exponential-moment estimate is valid. For n=floor((M-1)/4), all selected times are among0,...,M-1 and n>=M/8 at M>=64. Since delta M/16<=delta n/2, the stated count event is contained in the proved low-success event. The exponential constants1/8 and1/64 are valid. A union bound over all three states genuinely controls the actual terminal state's count.

4. **Error reduction is for the unchanged program.** The accepted SB001 v2 deterministic bound specializes to K=2, A=6M/z and additive3/Q exactly as quoted. The arbitrary-start statistical comparison remains with the true source, not the reflected source. Therefore the changed row10 transition law is not silently substituted in the risk target. The reflected comparison is used only for a nonnegative numerical count functional.

5. **Absorbing endpoint and quantized empty branch.** On terminal00 all previously observed00 successors are0. A nonempty selected floor block normalizes to exactly delta0 and final ordered rounding preserves it. The empty condition is `[kappa(Q-1)+1]J<M`, implying J<2M/z. For integer J, this is precisely contained in J<ceil(2M/z), including J=0 and exact-integer thresholds. The inherited universal four-state occupation bound gives at most32/z+16/M. The argument neither adds a count oracle nor modifies the fallback.

6. **Constants and asymptotic simplification.** The active numerical term is16A/(delta M)=96/(delta z). The universal add-one smoothing correction isPsi(32/(M+1)). The bound `3exp(-delta M/64)<=12/(sqrt(delta)sqrt(M))` follows from the maximum3sqrt(32/(Euler_e delta));12 is safely larger than3sqrt(32/Euler_e). Hence the constant in BAI2.2 depends only on eta and no hidden dependence on e, initialization, M, Q or kappa is introduced.

## Independent finite corroboration

The reviewer separately checked a grid of b in{.1,.3,.5,.9}, t in{.1,.4,.9}, and e in{0,.01,.5,1}. Direct matrix computations verified the complete minorization column and fixed-block success bounds. Enumeration over all six-step reflected active paths from each active initial state produced2640 density comparisons; every true-path coefficient equaled the reflected coefficient times `(1-e)^N10` and was no larger. These checks corroborate algebra only; the proof above supplies the general argument.

## Nonblocking editorial observations

- The sentence “On that event” after the simultaneous-good-event failure probability could be made unambiguously “On the simultaneous good event.” Its intended meaning and all equations are clear.
- Eta enters cubically through a conservative four-step bound. No optimal dependence on eta is claimed or needed.

## Scope limit

This theorem resolves a genuine arbitrary-initialization family that includes the singleton-stationary weighted-mixing obstruction. It does not handle t approaching0 or b approaching the endpoints with a uniform constant, nor full-support sources. Those limitations are explicitly acknowledged. No new implementation or resource claim is inferred from the analysis.
