# S004 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

## Accepted Scope

For every `K>=2,M>=1`, legal homogeneous second-order table theta, stationary pair law pi, arbitrary initial pair law mu, and deterministic `0<=b<=M-1`, write `L=M-b` and `eta_b=TV(mu P^b,pi)`. The actual-endpoint mean-TV bounds are

    suffix add-one: min{1,min{1,48 K^(3/2)/sqrt(L+1)}+eta_b};
    ORIGINAL full-history add-one:
        min{1,48 K^(3/2)/sqrt(L+1)+13 sqrt(K) eta_b^(3/4)}.

The original terminal count also satisfies `P(n_{Y_M}<w)<=min{1,K²w/(L+1)+eta_b}` for every integer `w>=1`. The full-history bound is proved by its own original-count/original-stack argument, not transferred from the suffix predictor's risk.

Under the ALL-starting-pairs minorization `P^q(s,t)>=beta pi(t)`, the proof correctly supplies the explicit envelope, including `beta=1`; the public sufficient half-window burn yields constants 69 and 81 for the two algorithms. For fixed `q>=2,0<beta<1`, the beta-scaled stationary hard family supplies the all-common-algorithm lower `(tau_beta/18)min{1,sqrt(K³/(M+1))}`, `tau_beta=min{1/10,1-sqrt(beta)}`. Matching order is claimed under the displayed sufficient burn condition, not as sharp joint mixing-parameter dependence.

Also accepted: all-state `q=1` emptiness even for sparse pi; exact `q=2,beta=1` equivalence to an IID symbol-transition table, with arbitrary initial pair still allowed; a nonmixing stationary example; positivity without a quantitative lower bound failing to give a source-uniform decaying burn envelope; and the inherited fixed-K consistency interpretation.

This does not certify an optimal initialization-floor exponent, sharp q/beta dependence, an IID-endpoint minimax rate, a `q>2,beta=1` IID characterization, a predictive-KL theorem, an optimal squared-TV theorem, or literature novelty.



## Per-Lemma Audit

### unit_001 — Lemma 1: Suffix path-law transfer, lines 127–151

- **Statement and validity:** the suffix law is exactly `(mu P^b)Q_L` for the same fixed source. Kernel contraction gives the upper distance eta_b; projection to the suffix's observed first pair gives the reverse inequality. Thus equality is justified, not merely an unproved coupling assertion.
- **Loss transfer:** fixed-theta suffix TV loss is a `[0,1]`-valued function of that suffix, so its expectation changes by at most eta_b. S001 applies to the stationary length-L comparison with the same endpoint convention.
- **Original-count bridge:** `J>=J_b` pathwise implies `{J<w} subset {J_b<w}`. Transfer of this suffix event and S001's integer occupancy bound give the claimed floor, with the final cap handled correctly. The FULL-history path law is not asserted to contract after b steps.
- **Adversarial boundaries:** b=0, L=1, unreachable stationary states visited under mu, zero probabilities, and thresholds larger than M all remain valid; no absolute continuity is needed.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Lemma 2: Arbitrary-start finite stacks, lines 153–177

- **Validity:** drawing the initial pair from mu independently of row stacks reproduces each complete path-prefix product exactly. Every row consumes at most M entries; the auxiliary 2M prefixes suffice for every later deterministic maximum. The original count identity follows pathwise.
- **Dependency audit:** the S001 deterministic-stack distribution does not depend on the initial law. Its L4 inequality therefore transfers without importing stationary independence. The displayed mean, bounded-difference tail and union/moment coefficient agree with the accepted interface.
- **Dependence audit:** endpoint, count, layer and stack deviations can all be dependent. No conditional or stopped-row IID claim is made.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Floor-occupancy empirical bound, lines 179–211

- **Validity:** on each original-count layer `v<=J<2v`, the original deviation is covered by `Z_v`, and the TV factor is `1/(2J)<=1/(2v)`. Unconditional Holder gives `||Z_v||_4 P(E_v)^(3/4)`, to which the original-count floor applies at the valid integer threshold `2v`.
- **Floor split:** `min(1,x+y)^(3/4)<=min(1,x)^(3/4)+y^(3/4)` is valid in both x regimes. Summing produces the accepted `10sqrt(2c)` series and the exact geometric sum `2+sqrt(2)`.
- **Constants and boundaries:** multiplication yields precisely `125sqrt(2)/4` and `(25/8)(2+sqrt(2))`. Finite layers partition `1<=J<=M`, including J=M, and only a nonnegative numerical series—not undefined extra stack variables—is extended to infinity. The empirical loss is never divided by J=0.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Proposition 4: Smoothing and original-rule bound, lines 213–261

- **Zero count:** `P(J=0)<=sqrt(c)+eta` follows from the occupancy floor at w=1 without assuming c<=1.
- **Real thresholds:** for positive `x=A_0/t-K`, the exact integer event is `J<ceil(x)`; `ceil(x)<=A_0/t` because K>=2. Empty x<=0 cases, exact integers, and A_0=0 are included. Integration gives `Psi(cA_0)+eta`, then `2sqrt(cA_0)+eta`.
- **Original estimator:** the convex-mixture formula is exact for J>=1; separately bounding J=0 and enlarging the nonnegative smoothing term is conservative, not an invalid reassignment of observations.
- **Coefficient audit:** the c coefficient is `125sqrt(2)/4+3<48`. The floor coefficient after `2eta<=2sqrt(K)eta^(3/4)` is `(25/8)(2+sqrt(2))+2<13`. The submitted rational comparisons are valid, including eta=0. Substitution `sqrt(Kc)=K^(3/2)/sqrt(L+1)` and cap one establish S004.2.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Lemma 5: Minorization contraction, lines 263–282

- **Assumptions:** (D) is an explicit additional source-class hypothesis, with the same stationary pi and every starting/destination pair, not an invariant inferred from stationarity.
- **Validity:** for beta<1, the residual R is stochastic and pi-invariant. Hence `nu P^q-pi=(1-beta)(nu R-pi R)` gives the block contraction, followed by the residual r transitions. This retains the stronger initial factor `TV(mu,pi)`.
- **Boundary:** beta=1 forces equality `P^q=Pi` by row sums. There is only ordinary contraction before the first q-block and exact reset afterwards; no `0^0` convention or reversibility is needed.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Corollary 6: Public burn and constants 69/81, lines 284–312

- **Admissibility:** `b=floor(M/2)` always gives `0<=b<=M-1` and `L=ceil(M/2)>=1`, including M=1. The sufficient condition is not claimed automatically when it fails.
- **Absorption:** `L+1>=(M+1)/2`; under (B), both `eta_b<=T` and `sqrt(K)eta_b^(3/4)<=T`, with the latter ratio `1/[K(M+1)^(1/4)]<=1`. The sums are `48sqrt(2)+1<69` and `48sqrt(2)+13<81`.
- **Exact test:** `floor(floor(M/2)/q)=floor(M/(2q))`; the beta<1 logarithmic condition has the correct sign. For beta=1, M>=2q makes b>=q. Fixed positive beta and fixed q yield eventual admissibility by linear versus logarithmic growth.
- **Public information:** the alternative `q ceil(log(M+1)/[-log(1-beta)])` burn depends only on allowed public parameters and must fit in the half-window. The original rule does not access or choose b, pi, mu or eta_b.
- **Verdict:** PASS. Repair direction: None.

### unit_007 — Proposition 7: Beta-scaled hard family, lines 314–337

- **Scaling audit:** `alpha=tau_beta a` satisfies `0<alpha<=a/10<=1/10`. S002's generic pre-choice information calculation remains valid; `16alpha²/K+36alpha²M/K³<=0.08+0.36=0.44`. Pinsker therefore still gives a conditional full-history testing distance below 1/2.
- **Lower-risk interface:** the target-row decoding and endpoint-conditional averaging give `alpha/18` for every common estimator. Revealing q,beta only changes the common test/kernel; it does not reveal the hidden sign vector or alter the common uniform endpoint law. The observed initial pair and all intervening symbols are retained.
- **Class membership:** `(1-alpha)²>=beta` follows from `alpha<=1-sqrt(beta)`. Multiplying the two-step inequality on the right by `P^(q-2)` preserves its entrywise order and gives `beta Pi` by stationarity for every integer q>=2. The stationary initial law is an allowed member of the arbitrary-mu class.
- **Quantifiers:** for each public K,M,q,beta the finite hard family is estimator-independent; supremum dominates its prior average before the infimum is taken. The beta=.81 constant is exactly 1/180. The lower coefficient tends to zero as beta approaches one and is not asserted at beta=1.
- **Verdict:** PASS. Repair direction: None.

### unit_008 — Proposition 8: All-state q=1 and exact q=2 reset, lines 339–353

- **q=1:** any pi has at least one positive-mass destination `(c,d)`. A starting pair with second coordinate different from c exists for K>=2 and has a structural zero to that destination. Thus the obstruction does not require full-support pi. Restricting starting states would be a different class incompatible with the present arbitrary-mu quantifier.
- **q=2,beta=1:** the unique legal two-step route gives `theta_ab(c)theta_bc(d)=pi(c,d)`. Summing over d yields `theta_ab(c)=p(c)` for EVERY a,b,c, including initially unreachable pairs. Substitution gives the product pi; the converse follows directly. No division by p is used, so zero coordinates are covered.
- **Scope:** the transition table is IID; the initial pair need not already be product-distributed. No extension to q>2 or IID minimax rate is smuggled into the conclusion.
- **Verdict:** PASS. Repair direction: None.

### unit_009 — Proposition 9: Sufficiency, positivity, fixed-K consistency, lines 355–386

- **Nonnecessity example:** `00->01->11->10->00` is a legal deterministic pair cycle. Uniform initialization is stationary, while a fixed start remains a point mass at TV distance 3/4 from uniform at every time. S001 still applies.
- **Inherited consistency:** the checked original-add-one L1+ interface has arbitrary mu and tends to zero for each fixed K. Therefore the wording correctly distinguishes fixed-K general consistency from the faster joint K,M stationary order recovered here. No assertion that prediction is impossible without mixing is made.
- **Positive slow family:** `theta_ab(c)=(1-epsilon)1{c=b}+epsilon/K` is positive on every legal symbol transition. Its stationary pair law `u(a)T(a,b)` is directly verified. From `(0,0)` the second-coordinate marginal is exactly `(1-epsilon)^b delta_0+[1-(1-epsilon)^b]u`; projection yields `(1-1/K)(1-epsilon)^b` as a lower bound on pair TV. Taking epsilon down to zero for each fixed b refutes a source-uniform decaying envelope.
- **Qualitative/source-specific distinction:** fixed positive minimum m implies every P² entry is at least m², hence `P²>=m² Pi` for any stationary pi. This valid, deliberately loose parameter can approach zero over the class. Positivity is not being said to prevent source-specific mixing.
- **Verdict:** PASS. Repair direction: None.

## Hidden Subclaim Scan

All independent bridges are represented in the nine local units. Additional algebraic facts used inside them—bounded-loss transfer, projection contraction, integer ceiling conversion, capped subadditivity, geometric summation, residual-kernel stationarity, terminal-law prior preservation under scaled S002, q-step propagation, and the slow family's invariant law—are either proved locally or mapped to the exact accepted dependency. None assumes selected-row independence, an unproved recurrence bound, stationarity of the full arbitrary-start history, or reversibility.





## Target Claim and Explicit Rate Audit

- The target remains **expected TV at the actual same-trajectory terminal pair**, with exactly M observed departures. Suffix and original algorithms are separately defined and separately justified.
- Exposed variables K,M,b,L,eta_b,q,beta and all domains are explicit. Constants 48/13/69/81 are numerical; the lower dependence on beta is displayed through tau_beta. Fixed-q/fixed-beta asymptotics are not asserted uniformly as those parameters vary.
- The horizon and burn are deterministic. There is no data-dependent stopping/burn, simultaneous-all-time or high-probability upgrade.
- At b=0 and mu=pi the original bound reduces exactly to the accepted S001 upper. At a later exact reset, retaining L rather than M is an explicitly conservative bound, not a claim that the whole history was stationary.
- (D) is a local hypothesis; path transfer, occupancy floor and contraction are derived conclusions. No generated event is promoted to a primitive assumption.
- The conditional-history KL used in the lower proof is only a testing-information bound. Predictive KL is not controlled by the bounded-loss TV transfer. `E[TV²]<=E[TV]<=u` is the stated elementary consequence; the invalid squaring `E[TV²]<=u²` is explicitly rejected.

## Notation Surface Audit

All new quantities are defined and scoped. Public objects are the suffix rule, eta_b, D_K(q,beta), envelope and risk inequalities; stack maxima, occupancy aliases, c, Psi, residual R and temporary scalar T are proof-local. The later first-order kernel T is explicitly local and does not affect the earlier scalar-rate calculation. No hidden parameter is passed to either estimator.

## Focused Adversarial Checks

Acceptance rests on the symbolic audit above. As a limited indexing/boundary sanity check, an independent exact-rational Python calculation enumerated binary symbol histories only for M=1,2,4, for five explicitly specified sources: the four-cycle, deterministic copy-last-symbol with sparse stationary pi, an IID law `(1/3,2/3)`, the positive persistent family at epsilon=1/5, and a doubly-stochastic second-order table assigning 3/4 to `c=a XOR b`. Initial laws were point masses; the stationary comparison laws were supplied exactly.

For all 35 source/horizon/burn cases, the calculation verified exact suffix-path TV equals the burn marginal TV, `J>=J_b` on every path, and the original occupancy-floor bound for `w=1,...,M+2`. All checks passed. No large exhaustive search or numerical evidence is used to establish the infinite-parameter theorem.

The coefficient checks were also recomputed with exact fractions: `(36/25)^2>2`, `(38/25)^2>2`, and `(17/12)^2>2`; the last gives `48*(17/12)+1=69` and `48*(17/12)+13=81`, with strict bounds because `sqrt(2)<17/12`. The floor identity was independently checked for M=1,...,100 and q=1,...,20; its general proof remains elementary integer division, not the finite check.

## Target-Step Assembly Audit and Review Rationale

The noncircular chain is:

1. S001 stationary suffix occupancy/risk plus Lemma 1 gives S004.1 and the ORIGINAL count floor.
2. Lemma 2 retains the ORIGINAL arbitrary-start stack identity; Lemma 3 combines its deterministic maximum with that original-count floor using unconditional Holder.
3. Proposition 4 supplies zero-count/smoothing control and constants, yielding S004.2 independently of the suffix-risk transfer.
4. Lemma 5 and Corollary 6 give the exact all-state mixing envelope and public finite burn specialization.
5. S002's exact generic-amplitude calculations plus Proposition 7 give the beta-dependent minimax lower on a stationary subclass of the arbitrary-start mixing class.
6. Propositions 8–9 delimit empty/exact-reset/positivity/nonnecessity boundaries without extending the lower across beta=1.

These results jointly establish the authorized S004 interface with no missing mathematical bridge or dependency flaw. ACCEPTED with no retry is therefore the smallest justified outcome. The separate IID-endpoint algorithm/rate question remains a legitimate successor, not a defect in this unit.

