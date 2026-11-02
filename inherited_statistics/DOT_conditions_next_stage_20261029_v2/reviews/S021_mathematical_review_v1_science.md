# S021 原 v1 科学审查与局部反例

编排说明（非原文）：本文件保留完整科学证明或完整科学审查推理；只省略身份控制、原提交状态、管理路径、重复来源管理表与执行记录。所有复制区间逐字节保留，原件未改；新增、复制和省略字节区间及原件全文身份见 COPY_MAP.json。原章节号和审查所引行号沿用原件，不是本副本行号；按同名章节与公式定位。来源的准确科学版本和当前可读闭包见 SOURCES.md。有限枚举只是补充证据，不是证明或形式化验证。本次装配没有重做数学审查。

历史版本判断：原 v1 未通过，原因是真实的 R1 局部假设范围错误，不能追认。这里保留完整反例、全部五个科学审查单元和有限检查结论，不附原始执行日志或失败档案。当前 v2 已修复 R1 并补齐非阻断 N1；其新审查须与本文件合读。

## Useful result and overall verdict

**NEEDS REVISION: one bounded, local hypothesis-scope defect.** The proposed fixed-public-template upper obstruction, its finite envelope, and the requested `5 K^(-1/2)` ray bound are mathematically valid under their stated conditions 1–4. The exact S015/S012 restricted-family rates and the state-dependent recipe's all-state membership also check. However, **Lemma A is not true under its literal local heading “Under conditions 1–3”**: its survival conclusions require the initialization/terminal-support part of condition 4. A concrete legal all-state counterexample is given below. Therefore the frozen v1 is **not accepted** as a complete five-unit submission.

The smallest required repair is to state Lemma A under conditions 1–4, or explicitly separate its conditions-1–3 structural bounds from its additionally initialized survival bridge. This is not a counterexample to Theorem C, which already assumes conditions 1–4. One optional, nonblocking totalization clarification is also identified for the preliminary empirical rule. No new route, full-class improvement, or unknown-template-mixture upper follows from this review.


## Blocking issue R1 — Lemma A's local assumption set is too weak

**Location:** candidate line 121; survival assertions at lines 131–140 and deterministic scheduled-count interpretation at lines 142–146.

The combinatorial bounds on `L,Z,v` follow from conditions 1–3 (indeed the main counting part needs only the phase geometry). But conditions 1–3 do not constrain the initial pair law to start in a phase. They do not even define the query set S. The argument that the first failed scheduled vulnerable coin occurs at an actual vulnerable row uses the known-phase initialization in condition 4. The assertion that the terminal pair is in S on G uses the terminal-support part of condition 4.

### Explicit counterexample to the literal survival statement

Take `K=3`, `beta=1/4`, `delta=3/4`, `L=1`, `D_0={(1,1)}`, and put `r=(1/3)delta_0+(2/3)delta_2`. Define **all nine base rows** by

- `Q_(a,1)=delta_1` for `a=0,1,2`;
- `Q_(0,0)=Q_(1,0)=delta_0`;
- `Q_(2,0)=r` and `Q_(a,2)=r` for `a=0,1,2`.

The singleton phase is closed under the legal shift and is vulnerable; `00` is excluded and absorbing. Set `theta=beta delta_0+delta Q` on every row. Its zero-output probabilities are

    h_(0,0)=h_(1,0)=1,     h_(2,0)=1/2,
    h_(a,1)=1/4,           h_(a,2)=1/2.

Thus the exact legal two-step mass to 00 is `h_(a,b) h_(b,0)`: it equals 1/4 for every row ending in 1 or 2, and equals 1, 1, 1/2 for the three rows ending in 0. Therefore **all** starts satisfy `P²(s,00)>=beta`, and `pi=delta_00` is stationary. Conditions 1–3 all hold.

Now choose `M=1` and `mu=delta_(2,2)`, which conditions 1–3 do not exclude. The sole scheduled phase is vulnerable, so `H=1` and `G={J_0=0}`. On `G^c`, of probability 1/4, the actual terminal pair is `(2,0)` and

    theta_(2,0)=(1/2)delta_0+(1/2)delta_2 != delta_0.

This directly contradicts the literal off-G conclusion. It also explains the missing logical step: at time zero the actual process was not in the scheduled vulnerable phase, so the vulnerable-row forcing calculation cannot be applied to its row.

**Bounded repair:** replace line 121 by “Under conditions 1–4” for the whole lemma. A more minimal split may retain conditions 1–3 for the displayed structural bounds, add a common initialization supported in a specified `D_k` before the survival bridge, and invoke condition 4 for terminal membership in S. No change to Theorem C's formula, constants, or domain is needed. Fresh bounded recheck is required after repair; this review does not accept unpublished replacement bytes.

## Nonblocking note N1 — totalize the preliminary empirical predictor

**Location:** line 25, compared with the explicit support guard already present at line 161.

The preliminary star empirical formula normalizes on the common family support. Interpreted literally on every alphabet history, it need not. For `M=3` and the impossible history `(u,v,0,u,v)` with `u in U,v in V`, the terminal pair is `(u,v)`, there is one departure from that row, and all W-label counts vanish. With `N_s` counting every observed departure, the displayed output then has total mass beta, not one.

This is a common-null-history completion issue, **not a failure of the risk bound**: under the exact family, terminal membership in U×V implies G, so that history cannot occur; the center predictor is already normalized everywhere. Add the same public reconstruction-support/default-output guard used in Lemma B, or explicitly extend the rule arbitrarily outside the common family support. No hidden parameter is needed for this extension. Only R1 is blocking.

## Unit-by-unit review

### Unit 1 — Exact S015 center risk, empirical upper, finite scales and S012 comparison

**Candidate:** lines 9–100. **Verdict: PASS mathematically; N1 is a totalization clarification.**

- The relevant S015 source definitions and proofs were actually read: alphabet and all-row table, disjoint phases, all-state membership, every-residue initialization/full-history bijection, vulnerable-only event, changed-target testing lower, and exact count/amplitude bound (source lines 1–300, especially Lemmas 4–5 and Propositions 6–7). S012 definitions and corresponding construction/conditional-experiment/testing/upper proofs were read through its Proposition 8 (source lines 15–320). These are exact restricted families with their specified common horizon-aligned mu, **not** a supremum over arbitrary initial laws for each restricted family.
- For paired signs, each perturbed coordinate differs from `1/m` by `alpha/m`, and the `2 floor(m/2)` perturbed coordinates give half-L1 distance `alpha floor(m/2)/m`, independent of signs. The odd leftover coordinate has zero contribution. Multiplication of both rows' nonzero part by delta multiplies TV by exactly delta; the default-target complement of G contributes zero. The exact center risk in line 61 and factor-at-most-four sandwich therefore follow.
- The inherited lower is `delta^(H_M+1) alpha/8`, for **every** common randomized full-history predictor before taking its infimum. `alpha/8=min(1/16,t/64)>=min(1,t)/64` is correct in both caps.
- Conditional on G and the actual endpoint `T=s`, the complete source-specific product experiment supplies q independent uniform contexts and corresponding labels. Consequently `N_s` is binomial and, conditional on selected context positions (or their number), the labels are IID from the row law. There is no generic Markov stopped-count assertion. All initial residual symbols and repeated occurrences of an emitted label remain in the bijection; the same emitted symbol is not counted twice.
- The empirical-TV bound follows from coordinate variance and Cauchy–Schwarz; for `n>=1`, `(1/2)sqrt(m/n)<=sqrt(m/(n+1))`, and the `n=0` default is bounded by one. Jensen/Cauchy–Schwarz and the exact binomial inverse moment give the stated upper, including `q=0` and `d=1` in its later generalized form.
- `q+1>M/(2m)` and `m<=K/4` give `t²<K⁴/(128M)<=K⁴/[64(M+1)]` for `M>=1`. With the inherited S015 `2^-12 h_*` lower, both finite caps and all six initialization cases are retained.
- On the requested ray, `m/K->1/4`, `q/K⁴->2`, hence `t~K^(-1/2)/(8 sqrt(2))`. The exact `H_M=M/2+M/(2m)+e_M`, `|e_M|<=2m`, and displayed logarithmic remainder prove `delta^(H_M+1)~K^(-1/4)`. The restricted risk is therefore `Theta(K^(-3/4))`.
- For S012, `L=m²`, `q/K³->16`, `t->1/32`, and `alpha->1/256`; its survival is `delta^M`, so its restricted risk is `Theta(K^(-1/2))`. These statements do not assert either full-class rate.
- The constructed-family beta-zero extension can be proved directly with no refresh and the same product/test calculation. At beta one, every constructed actual row is delta_0 and risk is zero. Neither endpoint assertion is substituted for the separate positive full-class IID risk. No K<13 star construction is asserted.

### Unit 2 — Structural safe count and first-failure survival bridge

**Candidate:** lines 108–149. **Verdict: structural assertions PASS; local survival statement NEEDS R1; survival proof PASS under condition 4.**

- Nonempty disjoint actual-pair phases excluding 00 give `L<=K²-1`; no auxiliary clock states are counted.
- A representative safe row has deterministic successor `(b,0)` in the next phase. Those successors are nonzero and distinct for distinct safe phases because their successor phases are disjoint. There are only K−1 such states, giving `Z<=K−1`.
- Two cyclically consecutive safe phases would append zero twice and enter 00, contradicting closure. Thus `Z<=floor(L/2)`, including `L=1` (where safe is impossible). The vulnerable fraction is at least 1/2 and at least `1-(K-1)/L`; weakening K−1 to K is harmless.
- At an **actual vulnerable row**, the legal two-step identity and all-state condition force `beta theta_(b,0)(0)>=beta`. Interior beta is essential: `beta>0` forces `theta_(b,0)=delta_0`, and `delta>0` then forces `Q_(b,0)=delta_0`. If that row belonged to D, its base zero output would put 00 in D, a contradiction. Therefore a genuine first failed vulnerable coin already creates a default target, even when it is the final observed departure; one more departure reaches 00 forever.
- With the condition-4 known-phase initialization, scheduled phases are deterministic before any failure. Induction using independent coins and base draws proves equality of the **entire** actual/base history on G; safe refreshes do not affect outputs. Conditioning on G changes no initial/base randomness and gives `P(G)=delta^H`, uniformly in nu. The terminal set S then distinguishes G from its complement on the source's actual support, without exposing coins.
- `H=qv+h_r`, `0<=h_r<=r<L`, and `H>=Mv/L-L` are correct for every starting phase and residue. Neither parity, partial blocks, nor the phase error is discarded. R1 is exactly the missing initialization qualifier in the lemma's own heading, not a defect in these calculations.

### Unit 3 — Arbitrary-row observable predictor in one fixed public template

**Candidate:** lines 106–117, 151–161. **Verdict: PASS under the explicitly stated conditions 1–4.**

- Public geometry, the safe/vulnerable classification, S, W and the full reconstruction map can be hard-coded into one predictor for a fixed family. The parameter nu, actual row laws, hidden stationary probabilities, refresh labels and future observations are not inputs. The initialization may depend on the public horizon but not on unknown row parameters.
- The public-support fallback makes this a normalized kernel on all histories. On actual support, off G it outputs the exact target delta_0; on G it reconstructs all q training pairs from the full observation and uses the actual terminal context.
- For each fixed nu and actual endpoint s, independence of T from the q training pairs is an explicit experiment hypothesis. It gives `N_s~Bin(q,1/d)`. No independence of unknown parameters across rows or prior factorization is needed. Row laws can have zeros whenever the stated product experiment remains valid; no KL or positivity assumption is used by this upper.
- `E[1/(N_s+1)]=[1-(1-1/d)^(q+1)]d/(q+1)<=d/(q+1)` includes `q=0,d=1`. The cap and the delta target factor are both retained. Finally `q+1>M/L` and `dw<=K³` give the second bound. The coarse budgets `d<=K²,w<=K` are valid even though sharper support budgets are available.
- The result is `inf_B sup_nu` within each one fixed public family. A separate predictor may be used for a different publicly specified geometry. It is **not** `inf_B sup_(geometry,nu)` with an unknown geometry. The candidate explicitly excludes unknown mixtures and does not reverse these quantifiers.

### Unit 4 — All-period finite envelope, weak-hazard domain and K⁵ ray

**Candidate:** lines 163–224. **Verdict: PASS under conditions 1–4.**

- `M>=K⁵` and `L<=K²` ensure `sqrt(K³L/M)<=1`; removing the inner cap in the proof is legitimate. From `H>=Mv/L-L`, one obtains `H+1>=M max(1/2,1-K/L)-K²`. Since delta lies in (0,1), the displayed exponential upper has the correct inequality direction and retains the full `delta^(-K²)` loss.
- For `L<=2K`, `sqrt(L) exp(-A/2)<=sqrt(2K) exp(-A/2)`. On `[2K,K²]`, `(log f)'=(x-2AK)/(2x²)` changes only from negative to positive, so any interior critical point is a minimum. Both continuous endpoints are retained. Integer allowable periods are a subset, and K=2's second interval is a single point. This proves all intermediate-period coverage without rounding or asymptotic substitutions.
- Multiplying the common `sqrt(K³/M)` factor gives exactly `sqrt(2K⁴/M)` and `sqrt(K⁵/M)`. The outer probability-loss cap one is valid. No constant absorbs the phase factor outside the explicitly declared weak-hazard domain.
- The second branch differs from `delta^M` by `exp(lambda M/K)`. Thus `lambda(K²+M/K)<=C_0` controls both branch inflation factors and proves the finite weak-hazard corollary. If a chosen C_0 makes the domain empty, the assertion is simply vacuous.
- On `M=K⁵`, `beta=ln K/(2K⁵)`, for every integer K>=2, beta<1/2 and `lambda<=2beta`. The inequality `ln K<=K/2` gives the displayed uniform bound <=5/8. Also `delta^M<=K^(-1/2)` and `delta^(M/2)<=K^(-1/4)`. Finally `e^(5/8) max(sqrt(2)K^(-1/4),1)<5` proves the advertised `5K^(-1/2)`, including small K where this upper can exceed one but remains valid.
- The theorem is not extended to beta=0 or 1: its stated domain avoids both the forcing division by beta and the `lambda,delta^(-K²)` singular endpoint. The separate exact-family endpoint comments in unit 1 are not an extension of Theorem C.
- This is an upper on actual statistical prediction risk in each stated restricted experiment, not a failed-certificate argument or a mixing-distance lower. It cannot by itself settle the full-class gap or a mixture over unknown public templates.

### Unit 5 — Failed Euler membership and lawful state-dependent recipe

**Candidate:** lines 226–274. **Verdict: PASS, membership only; successor remains an unproved obligation.**

- The cyclic word `(0,1,0,2,1,1,2,2)` gives the eight distinct ordered pairs `01,10,02,21,11,12,22,20`, excluding 00. Its specified rows `Q_21=delta_1`, `Q_10=delta_2` are both vulnerable, so the actual two-step mass from 21 to 00 is beta²<beta.
- There is no rescue by a different stationary witness: every row after the same beta refresh gives zero probability at least beta, so from every state the two-step chance of reaching absorbing 00 is at least beta². Any stationary law must therefore put all mass on 00 (apply stationarity to the complement of 00). Thus the example really violates class membership, not merely one optional choice of pi.
- In the recipe's inherited interior-beta domain, `t_b in [beta,1]` makes every `beta/t_b` well defined and in [beta,1]. All K² rows normalize and induce legal shifts, including `h_00=t_0=1`. For b nonzero, the exact two-step product is beta; for b zero it is t_a>=beta. Other destination inequalities follow from the point-mass stationary witness. No initial-law restriction is needed for this membership fact.
- Increasing an ending-nonzero hazard above `beta/t_b` while fixing the ending-zero hazards preserves the product inequality, provided it remains at most one. This upper endpoint is implicit in “0-output probabilities”; it is not a permission to leave the simplex.
- At `t_b=beta` every row ending in b outputs zero; at `t_b=1`, the row `(b,0)` immediately outputs zero. Intermediate values give hazard strictly greater than beta on rows ending in b and a genuinely partial-zero row `(b,0)`. Thus the construction can violate the template dichotomy/first-failure absorption; the membership proof does not imply a product conditional law.
- The formula is not asserted at beta=0 with a zero t_b (which would require a separate convention). At beta one all t_b=1 and the trivial absorbing table is well defined. No stronger prediction lower, survival scale, endpoint concentration, or full-data sign-testing claim is proved for the proposed successor. Its explicit warnings about initial data, failure histories, target contrast and conditional bias are appropriate. The heuristic O(K³) informative-label budget is labeled heuristic, not used as a theorem premise.


The producer checker and saved result were read. Their bindings are respectively `ad0f07ea67eebeb7afa8ec57bf9cf158fe445689e82ca3516ad16a2b9d5f1c24` (1,858 bytes) and `2e41d60e3c4c6fa45821dc60c3518b89c67b1e5b8f401145242b62303a5b19cd` (271 bytes). They are finite corroboration, not an independent review or proof. In particular their phase-pattern filter already imposes the safe-count structural restriction; it does not experimentally derive that restriction from actual pairs. The symbolic injectivity proof supplies the restriction, and the reviewer added actual legal-cycle checks below.


Result: `PASS_WITH_CONFIRMED_LOCAL_SCOPE_COUNTEREXAMPLE` — **this is not an acceptance status**. Exact rational tests independently confirm R1 and corroborate the intended statements; floating probes corroborate only the scalar envelope.

- 64 actual deterministic simple legal pair cycles examined for K=2,3; 15 satisfy all-state beta membership.
- 277 initialized full coin/state survival experiments on those member cycles, all starting phases and partial horizons in the stated finite range.
- 520 exact binomial inverse-moment identities, including q=0 and d=1.
- 372 exact paired-sign center-row losses, both amplitude choices and odd/even m.
- 7,650 exact full-table state-dependent-recipe rows.
- One explicitly instantiated failed Euler table.
- 590,000 log-space floating all-integer-period probes, K=2,…,60 and eight hazard values, tolerance `1e-12`.
- The explicit nine-row R1 counterexample and all its exact two-step masses are saved in JSON.


