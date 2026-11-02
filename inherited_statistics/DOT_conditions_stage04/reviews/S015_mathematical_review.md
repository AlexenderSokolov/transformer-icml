# S015 原独立数学审查的科学正文

编排说明（非原文）：原独立审查日期为 2026-10-28，结论 ACCEPTED，无数学修复要求。以下保留原审查的完整逐引理推理、科学适用范围与有限检查事实；身份及运行元数据省略。审查绑定原证明哈希，而非这份新复制件。独立上下文 LLM 审查不是形式验证，也不是外部同行评审。下文有限检查是原审查历史结果，本次编排未重跑；原命令、脚本和运行记录不在本包内。

编排补充（非原文）：原审查的九个逐引理推理及全部科学有限检查保留；纯来源绑定项省略，编号不重排。S014 不是 S015 的数学依赖；旧发射族和新星形族的结论兼容。

## Useful Result

**ACCEPTED. All nine local units PASS.** The new lawful star-clock family proves the stated finite full-history lower with the exact vulnerable-departure count, and closes the specified logarithmic window for **common full-class minimax risk**:

    M=K^4, beta=(log K)/(4K^4):   R_D2=Theta(K^-1/8).

The lower-certificate ratio tends to `1/(512 sqrt(2))`; the accepted public-selector upper ratio tends to one. The same family also refutes the two precisely stated aggregate-refresh and total-risk upper proposals. This is a material partial result, not a full joint `(K,M,beta)` rate, not a matching upper for original full-history add-one, and not a contradiction of S012's different restricted-family upper.

## Exact Accepted Scope

Fix integers `K>=13,M>=1` and public `0<beta<1`; let `delta=1-beta`, `m=floor((K-1)/4)`, `L=2m`, `q=floor(M/L)` and `alpha=min(1/2,sqrt(m^3/(q+1))/8)`. The source is a normalized, fixed homogeneous legal order-two symbol shift on the original alphabet. Its arbitrary initial pair law may be singular to its hidden stationary law. Membership requires the two-step minorization from **every** starting pair, not just reachable pairs. The complete `M+2` observed symbols, all M departures, actual terminal row, expected half-L1 TV, and every common randomized predictor using public parameters only are preserved.

The accepted finite conclusions for the explicit sign family are:

1. Its stationary law is `delta_00`; the maximal two-step coefficient is exactly beta, including maximization over stationary witnesses because that law is unique for beta>0.
2. With the public deterministic vulnerable-time count `H_M`, every common predictor has prior-average risk at least `delta^(H_M+1) alpha/8`. Consequently the same lower holds for the full-class minimax risk.
3. The common constant predictor `delta_0` has risk exactly `delta^(H_M+1)` on **this family and its specified initial law only**.
4. `alpha/8 >= 2^-12 min(1,sqrt(K^4/(M+1)))`, with the exact `H_M` retained in the finite exponential.
5. Along the specified logarithmic sequence,

       1/(512 sqrt(2)) <= liminf K^(1/8) R_D2
                         <= limsup K^(1/8) R_D2 <= 1.

   This does not assert an exact limiting minimax constant.
6. In the canonical symbol-refresh implementation, with `C_ref` meaning at least one of the M refresh coins equals one,

       average_sigma E[loss 1_(C_ref)]
          >= (alpha/8)[delta^(H_M+1)-delta^(M+1)].

   The constant predictor's exact corresponding contribution is the bracket without `alpha/8`. This is an unconditional indicator-weighted contribution, not a conditional risk divided by the event probability.
7. No universal finite `C_0` and common predictor family can bound every admitted source's canonical aggregate contribution by `C_0(a+sqrt(beta))`. Nor can the full-class minimax risk, or any common predictor family's worst total risk, have universal upper order `a+delta^M g+sqrt(beta)`, where `a=min(1,sqrt(K^3/(M+1)))` and `g=min(1,sqrt(K^5/(M+1)))`. These are precise negative conclusions, not a rejection of all estimation methods.

## Per-Lemma Audit

### unit_001 — Lemma 1: Legal star geometry (`lem:s015-star`)

- **Statement fidelity:** the finite alphabet and all K-squared rows, normalized homogeneity, legal shift, and m=3 boundary are proved in the contracted domain.
- **Disjointness:** even star pairs `(j+1,0)` and odd pairs `(0,j+2)` are internally distinct and mutually disjoint. The U/V/W coordinate types separate every replacement phase from retained star pairs and from each other. Removed `p_1,...,p_4` and unused-letter rows are genuinely default.
- **Rows:** paired W masses sum to 2/m; the odd leftover mass restores total one. Every W label is positive for alpha<=1/2. The mixture and default rows normalize without a time/count/phase variable added to the source state.
- **Wrap stress test:** when m=3, the word is `(1,0,2,0,3,0)`, `c_6=c_0=1`, `p_5=(0,1)`, and its one retained departure appends 0 to return to `p_0=(1,0)`. The five-step replacement plus this one step is exactly L=6. No L>=9 premise is used.
- **Contribution:** supplies the full lawful table and common base support for every subsequent claim.
- **Verdict:** PASS. Repair direction: None.

### unit_002 — Invariant 2: Base phases and vulnerable rows (`inv:s015-phase`)

- **Phase induction:** each replacement successor and retained clock successor lies in the next disjoint phase, including modular return. Positivity supplies reachability within D; the return-time argument proves exact period L for the **base** closed class only.
- **Count:** exceptional vulnerable phases 0,1,2,4 contribute four; retained even phases 6,...,2m-2 contribute m-3. Safe phases are 3 and the m-2 retained odd phases. Thus counts are m+1 and m-1, including the empty retained-even set at m=3.
- **Crucial successor check:** vulnerable second coordinates are exactly of types 0,U,V. Their successors after emitting zero, `(0,0),(u,0),(v,0)`, occur in no phase and are default. This is not the false claim that every ending-zero row is default: C-ending-zero and W-ending-zero active rows are present.
- **Safe coins:** at every safe phase the base and actual row both equal `delta_0`, so changing a refresh label cannot alter the appended symbol or phase.
- **Verdict:** PASS. Repair direction: None.

### unit_003 — Lemma 3: Every-pair minorization (`lem:s015-member`)

- **Stationarity:** 00 is default and absorbing, giving a valid sparse stationary witness without assuming stationary initialization.
- **Every-row calculation:** the unique two-step route to 00 has mass `theta_ab(0) theta_b0(0)`. At a vulnerable row the factors are beta and one, by Invariant 2. At a safe/default row they are one and at least beta. In particular a default row ending in a C or W symbol may reach a vulnerable active row; its second factor is then beta, not one. Deleted star pairs and leftover symbols are covered by this case.
- **All destinations:** outside 00 the stationary mass is zero and the inequality is nonnegativity. This covers all K-squared starts and destinations, not merely the sampled support.
- **Exactness/uniqueness:** phase 0 attains equality beta. The residual stochastic kernel from `P^2=beta Pi+delta R` contracts TV and forces every stationary law to equal `delta_00`. Thus the optional exact maximal-coefficient claim is justified, not assumed.
- **Verdict:** PASS. Repair direction: None.

### unit_004 — Lemma 4: Every-residue complete experiment (`lem:s015-history`)

- **Initial cases:** each of the six prescribed laws lies in its public phase `k=(2-d) mod L` and is sign-independent. The fixed W symbol in initial phases 3/4 is arbitrary initial information, not an uncounted label from a hidden previous transition.
- **Departure indices:** phase-2 times are exactly `d,d+L,...,d+qL=M`. Only the first q are observed departures; the terminal label remains unobserved. M=1,2 and q=0 are explicitly valid, including L=6.
- **Full information:** extraction and reconstruction retain the initial pair, all U/V choices, each observed W label, and every filler symbol. The repeated appearance of Z in overlapping pairs is one draw, not two samples. The public reconstruction map does not use signs or alpha and is a genuine bijection on common positive support.
- **Path law:** there are exactly two uniform factors for each of q+1 contexts, with the appropriate first factors supplied by mu when k=1/2. Exactly q row-label factors remain. This proves the entire observed-history law (14), including the uniform independent **actual** endpoint. It does not assume conditional IID for a general random visited row.
- **Verdict:** PASS. Repair direction: None.

### unit_005 — Lemma 5: Vulnerable-only event (`lem:s015-event`)

- **Canonical construction:** independent Bernoulli(beta) coins and independent base random variables reproduce the same actual table on every row, including default/safe rows. Labels remain latent and unavailable to the predictor.
- **Public event:** `T_v` is determined from K,M and the fixed phase schedule before any trajectory is drawn; its count H_M is not a realized visit count or a stopping time. Its sign-independent positive probability is exactly `delta^H_M`.
- **Conditional full law:** on G, vulnerable coins are zero and arbitrary safe coins have no effect. Induction therefore couples every one of the M+2 observed symbols to the base history. Because G only restricts independent coins, conditioning leaves the complete base randomness and path law unchanged.
- **Common prior:** `P_sigma(G,T=s)=delta^H_M/m^2` for every sign and endpoint; the single uniform sign prior and independent algorithm seed survive this conditioning. No claim is made about the posterior after the rest of H is observed.
- **First harmful coin:** before the first failed scheduled vulnerable coin the actual path follows its base phases, even after safe refreshes. That failure reaches a genuinely default pair immediately. If it is the last observed departure, the terminal row is already default; no extra sample is needed. Earlier failures then reach absorbing 00. This proves the exact target statement off G.
- **Verdict:** PASS. Repair direction: None.

### unit_006 — Proposition 6: Changed-target finite testing (`prop:s015-lower`)

- **Information:** conditional on G and any actual endpoint s, the full-history bijection gives the q-fold product law. A neighboring bit flip changes just two label atoms at one context, giving one-triple KL `(2alpha/m^3) log((1+alpha)/(1-alpha))`; the full conditional KL is exactly q times that value, also when the flipped context is s.
- **Caps/zero counts:** the integral logarithm bound and both alpha branches give KL<=1/8. When q=0, the training tuple is empty and KL=0. The finite Pinsker proof has the correct half-L1 normalization; the resulting TV<=1/4 gives error-sum at least 3/4 for any common randomized test.
- **One prior:** fixing all other bits and pairing the two tested signs gives prior-average conditional error at least 3/8. This is the same cube prior for every endpoint and every tested pair, not an endpoint-adapted prior.
- **Changed target:** the actual W contrast is `2delta alpha sigma/m`, not the old MM5 contrast. A wrong decoded sign costs `delta alpha/m` in half-L1 TV on that pair; the tie convention is sound. Disjoint pairs sum, with other output mass contributing nonnegative loss. Actual endpoint weights and `floor(m/2)/m>=1/3` give conditional loss at least `delta alpha/8`.
- **Unconditioning/quantifiers:** multiplication by the common `delta^H_M` proves the prior-average bound before taking the class supremum and algorithm infimum. No one sign is claimed hard for all algorithms.
- **Exact family upper:** on G the target has mass delta outside zero; off G it is `delta_0`. The constant predictor therefore has pathwise loss `delta 1_G` and exactly the asserted family risk. No full-class supremum is controlled by this separate calculation.
- **Verdict:** PASS. Repair direction: None.

### unit_007 — Proposition 7: Exact count and finite amplitude (`prop:s015-count`)

- **Exact count:** q complete length-L blocks each contain m+1 vulnerable phases; the remainder begins at phase k again. Thus `H_M=q(m+1)+r_M` with the displayed public remainder. Since `0<=r_M<=d`, the deviation from `M(m+1)/L` is less than L. The finite lower retains H_M exactly.
- **Alphabet comparison:** writing `K-1=4m+e`, e in 0,...,3 gives `m>=K/8` on the whole K>=13 domain.
- **Small horizon:** q=0 gives alpha=1/2 because m^3>=27>16, so the claimed capped amplitude follows directly.
- **Other branch:** q>=1 gives `q+1<=2q<=M/m`, hence `m^3/(q+1)>=m^4/M>=K^4/[8^4(M+1)]`. The two cap comparisons preserve the claimed constant: alpha/8>=min(1,t)/64 and min(1,t)>=min(1,z)/64.
- **Scope:** the resulting exponent is K^4, not an asserted replacement for the accepted stronger unrestricted K^5 baseline at beta zero.
- **Verdict:** PASS. Repair direction: None.

### unit_008 — Proposition 8: Matched logarithmic window (`prop:s015-window`)

- **Admissibility/amplitude:** the sequence has 0<beta<1. Floor errors give m/K->1/4 and q/K^3->2, whence m^3/(q+1)->1/128 and alpha->1/(64 sqrt(2)), strictly below the cap.
- **Survival:** `H_M=M/2+M/(2m)+e_M`, `|e_M|<=L`. The integral remainder for `-log(1-beta)` gives exactly (28). Its three errors are bounded by `(log K)/K`, `beta(L+1)`, and `(M+1)beta^2/(2delta)`, all tending to zero. Thus no finite exponential constant or phase error is silently absorbed.
- **Accepted full-class upper:** S011's exact experiment is identical and its deterministic public selector supplies `R_D2<=U`. S012 Proposition 9 is correctly bound; S015 also rechecks its scalar proof. Every suffix has u_g=1 and candidate at least `h_(M-1)`. The admissible public length `floor(K^(7/2))` has stationary term at most `48K^-1/4` and contraction ratio tending to one after scaling by K^-1/8. The displayed floor/log errors vanish uniformly where required.
- **Other algorithms:** uniformly in b the original penalty exceeds `13K^(13/32)(1+o(1))`, so U_+=1 eventually; pooling also caps at one. Hence U=U_suf eventually and its ratio tends to one. This remains a certificate assignment, not an assertion that original add-one risk equals one.
- **Conclusion:** combining the universal lower with the true full-class upper yields the displayed liminf/limsup sandwich and Theta rate. The lower-certificate constant is exactly `1/(512 sqrt(2))`; there is no claim of an exact limiting minimax constant.
- **Verdict:** PASS. Repair direction: None.

### unit_009 — Proposition 9: Same-witness refresh negatives (`prop:s015-after`)

- **Canonical identity:** the stationary symbol marginal is `delta_0`, and the actual table equals `beta delta_0+delta Q_sigma` on every row. The coins are precisely the canonical symbol-refresh implementation, not pair resets or a different stochastic mechanism.
- **Aggregate event:** all M coins zero is a subset of G, giving `P(G intersect C_ref)=delta^H_M-delta^M`. If H_M=M, the event is null and the lower is zero by nonnegativity; no null conditioning occurs.
- **Positive case:** if H_M<M, the event fixes vulnerable coins to zero and requires at least one safe coin one. It depends only on independent coins. Safe labels cannot alter any symbol, so the entire conditional path law, uniform endpoint, common sign prior and changed target remain exactly those of Proposition 6. Multiplying its conditional lower by the event mass proves (AFTER).
- **Exact family contribution:** pathwise loss `delta 1_G` immediately gives the bracket in (31), including the null case. The event need not be observed for its indicator-weighted loss contribution to be defined.
- **Precise negations:** `delta^(M+1)=K^-1/4(1+o(1))` is negligible beside `delta^(H_M+1)=K^-1/8(1+o(1))`. Meanwhile a is `K^-1/2(1+o(1))`, sqrt(beta)=o(a), and g=1. The lower/aggregate-proposal ratio grows as `[1/(512 sqrt(2))+o(1)]K^(3/8)`; the lower/total-proposal ratio grows as the same constant times K^(1/8). Averaging any proposed uniform upper over the same finite family yields the contradiction for every fixed universal constant and every common predictor family.
- **Verdict:** PASS. Repair direction: None.

## Independent Adversarial Checks

Acceptance rests on the preceding symbolic review. A reviewer-owned inline Python calculation, not a reused producer checker, completed with exit code zero and `ALL PASS`:

1. **21,580 exact full-row checks** using `fractions.Fraction`: m=3,...,7; every K=4m+1,...,4m+4; beta in `{1/7,2/3}`; rational alpha=1/3 and mixed signs. Checked all row sums, disjoint phases, every base successor, safe/vulnerable zero output, all-start two-step mass at least beta, vulnerable equality, genuinely default failure successors, and absorbing 00.
2. **12,720 exact integer phase/count cases**: m=3,...,50 and M=1,...,5L. Checked every phase-2 visit, exact q observed labels and terminal visit, exact block/remainder H_M, and its error bound.
3. **22 exact complete augmented-history experiments**: m=3, M=1,...,12; m=4, M=1,...,10; beta=1/7, alpha=1/3 and mixed signs. The augmentation retains the entire history and both G/C_ref indicators, while safe-coin branches are summed exactly. Inspected **28,825 augmented atoms** and **11,248 base histories**. Independently compared their history marginal against direct actual-table recursion. Checked normalization, extraction/reconstruction of every observed symbol, exact path-product factors, actual uniform endpoint, full-law proportionality on G and G intersect C_ref, and pathwise/exact constant-predictor losses. All six initial cases, L=6, q=0 and q=2 are covered. **Four** cases have H_M=M and null aggregate intersection.
4. **729 actual full conditional histories** for neighboring signs with m=3, q=2, M=12 and the prescribed rational alpha=3/8. Exact TV is `13/243`; KL is `0.04380318668690389`, matching the displayed formula within 1e-14 and below 1/8. Reconstruction was injective across all these complete histories. Only the logarithms in this check used floating arithmetic.
5. **4,880 exact rational scalar checks**, K=13,...,500, with M from `{1,2,L-1,L,L+1,2L-1,2L,K^3,K^4,K^6}`. Squared nonnegative quantities avoid floating square roots: checked both the KL amplitude cap and the full finite `2^-12` amplitude inequality exactly.


These finite checks corroborate but do not replace the all-parameter proof or constitute formal certification. The structural checks at alpha=1/3 are valid checks of claims proved for any 0<alpha<=1/2; they are not substituted for checking the prescribed horizon-dependent testing amplitude.

## Hidden Subclaim, Assumption and Notation Audit

The nine named units cover table normalization, legal period and support, every-pair membership, coefficient exactness/uniqueness, every-residue initialization, full observation equivalence, public coin restrictions, first harmful transition, conditional testing, changed target, finite amplitude, exact family upper, quantitative specialization and both negative corollaries. Supporting finite inequalities and testing facts are proved locally. No independent load-bearing claim is missing from the local map or smuggled in by a diagnostic assertion.

Primitive conditions are exactly the finite experiment, legal homogeneous table, public parameters, arbitrary mu, existential stationary witness, all-pair inequality and algorithm information restriction. The constructed membership, phase invariant, conditional product law, endpoint independence, source-independent event probabilities and default target after failure are derived conclusions. No stationary initialization, full support, general pair-matrix relaxation, hidden sign advice, observed refresh labels, conditional-IID assumption for general visited rows, or unproved generated-event condition is added.

Public-facing exports are the class/risk, lower, finite amplitude, exact count and matched/negative conclusions. Alphabet blocks, signs, reconstruction, phase sets, latent coins and decoded tests are proof-local. H is the history and H_M the deterministic coin count; V and V_phase, C and C_ref are distinguished. This notation does not hide a missing derivation or expand the predictor's information.

## Target Claim and Explicit Rate Audit

- The finite K>=13,M>=1,0<beta<1 domain is exactly the contract. No unsupported small-K patch or beta endpoint is needed. Existing beta-zero K^5 and beta-one IID baseline results are preserved rather than replaced by this weaker K^4 witness.
- All risks retain fixed-horizon expected half-L1 TV at the same trajectory's actual terminal row. Zero training counts, M=1,2, full initial information, overlapping symbols and endpoint/count dependence are handled by exact path laws, not discarded-data lower bounds.
- The conditioning events have explicitly computed source-independent probabilities; only positive events are conditioned on. Aggregate refresh loss remains an unconditional contribution. No stopping-time, high-probability, squared-TV, predictive-KL or independent-query substitution occurs.
- Constants 1/8, 2^-12 and the lower-certificate limit are derived; 48,13 and U are inherited through the checked S011 interface. Limits vary only K on the exact displayed sequence. Hidden order constants are numerical and independent of source, signs, algorithm, K,M,beta,mu or pi.
- Count error remains explicit in finite bounds and is controlled by (28) only for the asymptotic bridge. The suffix floor and burn admissibility, both amplitude cap branches, and all dominating-term ratios are checked.
- S012's old all-nonzero family has its own exact `delta^(M+1)` upper. The new star family has harmless zero-output phases and a different exact upper. The two results are compatible; no old acceptance is revoked.

## Target-Step Assembly Audit and Review Rationale

Lemma 1 and Invariant 2 supply the lawful star dynamics. Lemma 3 establishes membership for every starting state. Lemma 4 supplies the actual full-history experiment, and Lemma 5 supplies the positive common conditioning and exact post-failure target. Proposition 6 then yields the changed-target lower and separate family upper; Proposition 7 proves the finite amplitude/count exports. Proposition 8 combines the new universal lower with the accepted **full-class common-selector** upper, and Proposition 9 uses the same family/coin law to refute the two precise proposed bounds. This chain is noncircular and does not rely on S014, a diagnostic, or the producer's supplementary calculations.

The exact bounded S015 contract is proved without changing an assumption, interface, target, algorithm quantifier or constant. **ACCEPTED with no retry** is therefore the smallest justified outcome. The result closes a source-relevant previously unresolved sequence, while explicitly leaving full joint-rate identification and a matching original-add-one upper open.
