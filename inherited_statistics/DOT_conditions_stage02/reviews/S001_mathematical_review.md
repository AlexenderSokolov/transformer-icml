# S001 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

## Accepted Scope

For every integer K≥2, M≥1, every homogeneous second-order table θ with zero transitions permitted, and every stationary probability law π of its legal pair-shift chain, with the initial pair distributed as π:

1. For every integer w≥1, the actual terminal-row count J satisfies

       P(J<w) ≤ min{1,K²w/(M+1)}.

2. The original full-history add-one predictor, using exactly the M observed departures and the actual observed terminal pair, satisfies

       E TV(p⁺_{Y_M},θ_{Y_M}) ≤ min{1,48 K^(3/2)/sqrt(M+1)}.

3. Hence `R_stat ≤ R_stat^+ ≤ min{1,48 sqrt(K³/(M+1))}` with the frozen definitions.

This accepts the exact S001 upper-bound unit, not the entire research candidate. It does **not** establish a stationary all-algorithm lower bound, minimax optimality, a matching rate, a mixing result, a network implementation result, or literature novelty. Reducibility, multiple closed classes and stationary mixtures, periodicity, zero-mass pairs, deterministic rows, zero counts, and small M remain within the accepted scope.



## Per-Lemma Audit

### unit_001 — Deterministic finite-window count: §3.1, (3.1)

- Statement fidelity: arbitrary finite sequence, fixed state, integers M≥1 and w≥1; exactly M+1 candidate times M,…,2M.
- Proof validity: if w+1 flags exist, the last flag is preceded by the other w flags, all within its preceding length-M window because `t−M≤M≤t_j≤t−1`. This directly contradicts that last flag. No stochastic premise enters.
- Boundary/adversarial check: w=1 permits one flag, so the coefficient w rather than w−1 is correct. For w≥M+1 the claim is automatically valid. The strict `<w` event and exclusion of time t from its own count are handled correctly.
- Contribution: this supplies the new occupancy mechanism rather than assuming recurrence or an occupation-time concentration theorem.
- Verdict: PASS.
- Repair direction: none.

### unit_002 — Stationary endpoint occupancy: §3.2, (3.2), UC-stat

- Statement fidelity: the general lemma only needs equality in law of consecutive blocks of length M+1; its application derives this equality from πPθ=π and homogeneity.
- Proof validity: each of the M+1 flags has exactly the law of `{Y_M=s,n_s<w}`. Taking the expectation of unit_001 gives the divisor M+1, not M. The explicit product formula verifies block stationarity. The final state events are disjoint, so summing over K² rows gives the stated cap.
- Assumption audit: π is stationary by the primitive source-class definition, not inferred from mixing. No uniqueness, reversibility, positive mass, or irreducibility is used. Extension to 2M is a valid proof construction and does not increase the algorithm's observations.
- Boundary/adversarial check: zero-mass states have zero endpoint probability; a random stationary phase on a deterministic cycle and mixtures of stationary closed classes satisfy the same reasoning. A stationary binary pair-shift cycle `00→01→11→10→00` at M=3 has J=0 surely and attains the UC cap at w=1; this is consistent with the sharp endpoint counting factor.
- Contribution: derives `c=K²/(M+1)` from the new assumption, with all quantifiers retained.
- Verdict: PASS.
- Repair direction: none.

### unit_003 — Finite independent stacks and path identity: §4.1, (4.1)

- Statement fidelity: 2M symbols per row, drawn independently with each row's θ law and independently of the initial pair; exactly M departures are generated.
- Proof validity: a prescribed path fixes the initial pair and precisely the consumed prefix of each stack. Multiplying their probabilities recovers the original homogeneous path probability. This verifies the entire observed-history law, not just marginal transitions. The pathwise count identity follows because each departure consumes the next entry of the corresponding row.
- Assumption audit: all independence is in an auxiliary product construction. It does not say that stopped samples or samples conditional on a selected row are iid. Null prefixes are handled without conditioning.
- Boundary/adversarial check: no row can exhaust 2M entries; inaccessible or deterministic rows cause no issue.
- Contribution: transports the original actual-terminal loss to a space where deterministic row-prefix estimates are legitimate.
- Verdict: PASS.
- Repair direction: none.

### unit_004 — Finite maximal inequality and row mean: §4.2, (4.2)

- Statement fidelity: only deterministic prefixes `0≤j≤2v`, with deterministic integer 1≤v≤M.
- Proof validity: for `W_j=||S_{s,j}||₂`, convexity makes W a nonnegative submartingale. First-hitting decomposition, integration, and Cauchy–Schwarz give `E max W²≤4 EW_{2v}²`. Independence and centering give `E||S_{s,2v}||₂²=2v(1−||θ_s||₂²)≤2v`. The L¹/L² comparison and Jensen/Cauchy–Schwarz then give `E F_{s,v}≤sqrt(8Kv)`.
- Rigor: all variables are bounded on finite spaces, interchanges are justified, and zero norms need no division. The compact inline maximal proof is also fully instantiated in the imported readable proof.
- Contribution: the only multiplicative sqrt(K) dimension cost in the mean-plus-deviation analysis.
- Verdict: PASS.
- Repair direction: none.

### unit_005 — Dimension-independent bounded differences: §4.2, (4.3)

- Proof validity: altering one symbol changes each affected partial sum by `e_b−e_a`, whose L¹ norm is at most 2; taking the prefix maximum preserves this oscillation bound. Exposing independent coordinates makes each conditional-expectation increment range over an interval of length at most 2. The finite tilted-variance argument proves the interval MGF bound, hence `exp(vλ²)` after 2v coordinates.
- Constants: minimizing `−λt+vλ²` at λ=t/(2v) yields `exp(−t²/(4v))` exactly.
- Assumption/adversarial audit: no factor sqrt(K) is added to this deviation, and no realized row/count is conditioned upon. Constant rows and t=0 are covered.
- Contribution: supplies the concentration estimate needed by the maximum over K² rows.
- Verdict: PASS.
- Repair direction: none.

### unit_006 — Row maximum, fourth moment, and 25/4: §4.3, (4.4)

- Proof validity: with `a²/(4v)=2 ln K`, the K² union factor cancels and the nonnegative cross term only improves the bound. The integral `∫4t³ exp(−t²/(4v))dt=32v²` is correct. Minkowski applied to `Z_v≤b+a+(Z_v−b−a)_+` gives the displayed fourth-moment bound.
- Constants: dividing by sqrt(Kv) gives at most `sqrt(8)+sqrt(3)+2^(3/4)`, using `ln K/K≤1/e<3/8` and K≥2. The three stated rational power checks are exact and their upper bounds sum to 6.246<6.25. The underlying scalar maximum of ln(x)/x and the e>8/3 check are explicit in the imported proof.
- Boundary/adversarial audit: union does not require independence between the row maxima; their actual independence is therefore not relied upon. This does not claim the separate concentration deviation has no log K term.
- Contribution: uniform `||Z_v||₄≤(25/4)sqrt(Kv)` independently of the initialization law.
- Verdict: PASS.
- Repair direction: none.

### unit_007 — Numerical dyadic series: §5, (5.1)

- Proof validity: for 0<a<1 choose the unique L with `a2^L≤1<a2^(L+1)`; the two geometric sums have the stated bounds after factoring their terminal/initial terms. For a≥1 the sum is exactly 2+sqrt(2).
- Constants: `2·27⁴=1,062,882>32⁴=1,048,576`, so `2^(−1/4)<27/32` and the first coefficient is <32/5. The second is <7/2; total <9.9<10.
- Boundary/adversarial check: equality at a dyadic threshold stays in the first part. The extension to infinitely many terms is solely numerical.
- Contribution: converts the finite selected-count layers to a sqrt(c) scale without introducing undefined stacks.
- Verdict: PASS.
- Repair direction: none.

### unit_008 — Correlated terminal selection and summation: §6, (6.1)–(6.3)

- Proof validity: on `E_v={v≤J<2v}`, both the selected row and index are included in Z_v; `1/(2J)≤1/(2v)`. Hölder is unconditional: `E[Z_v1_E]≤||Z_v||₄P(E)^(3/4)`. UC-stat is applied only at the valid integer threshold 2v.
- Constants: multiplication gives `(25/8)sqrt(K)v^(−1/2) min(1,2cv)^(3/4)`. Summation and unit_007 at a=2c yield `(125sqrt(2)/4)sqrt(Kc)`.
- Boundary/adversarial check: the final layer includes J=M when M is a power of two; 2v≤2M ensures all maxima exist. The empirical loss is only formed for J≥1 and is extended by zero elsewhere. No conditioning-away of the Y_M/J/error correlations appears.
- Contribution: this is precisely the original actual-terminal empirical error, not a fixed-row, independent-query, or average-time substitute.
- Verdict: PASS.
- Repair direction: none.

### unit_009 — Real-threshold truncation: §7, (7.1)

- Proof validity: for A>0 and 0<t<1, the event is `{J<A/t−K}`. At x>0, integer J gives `{J<x}={J<ceil(x)}`, with `1≤ceil(x)≤x+1≤A/t` since K≥2. At x≤0 the event is empty. Integer UC therefore implies the integrated bound Ψ(cA).
- Constants: splitting `∫₀¹min(1,cA/t)dt` gives the stated three cases of Ψ. The pointwise bound `min(1,z)≤sqrt(z)` gives the coefficient 2.
- Boundary/adversarial check: A=0, exact integer x, arbitrarily small positive x, noninteger A, and J=0 all work. No illegal noninteger UC substitution occurs.
- Contribution: controls add-one smoothing with the same occupancy coefficient.
- Verdict: PASS.
- Repair direction: none.

### unit_010 — Add-one assembly and the final cap: §7, (7.2)–(7.3)

- Proof validity: at J≥1 the add-one vector is the exact convex mixture of the empirical row and uniform. Convexity/triangle inequality gives empirical TV plus K/(J+K). At J=0 the loss is ≤1. Extending the nonnegative smoothing term to all paths is a permissible conservative overcount, not a missing cancellation.
- Constants: `P(J=0)≤min(1,c)≤sqrt(c)≤sqrt(Kc)`; smoothing ≤2sqrt(Kc); empirical contribution is unit_008. Thus the total coefficient is `125sqrt(2)/4+3≈47.1942<48`. The rational comparison sqrt(2)<36/25 proves this without numerical approximation.
- Target assembly: the probability cap gives the minimum with 1. All constants are uniform in θ, π, K, M. Supremum over exactly the stationary class preserves the bound.
- Verdict: PASS.
- Repair direction: none.

### unit_011 — Admissibility and minimax direction: §§1,7–9

- Proof validity: the add-one formula uses only public K,M and the full observed history. It is therefore a common deterministic member of the all-algorithm class, giving `R_stat≤R_stat^+` in the correct direction.
- Scope audit: neither the initial stationary law nor the auxiliary stacks are supplied to the algorithm. The proof explicitly leaves the lower bound and optimality unresolved; it does not transplant the older nonstationary MM5 construction.
- Contribution: connects the accepted estimator result to the original statistical question without claiming the unresolved half of the candidate.
- Verdict: PASS.
- Repair direction: none.

## Hidden Subclaim Scan

The independent mathematical subclaims are all accounted for above: deterministic flags; Markov block stationarity and disjoint summation; finite path-law coupling; norm submartingale and second moment; finite maximal inequality; coordinate-interval MGF; union and shifted moment; scalar constants; dyadic summation; unconditional Hölder selection; real-threshold conversion/integration; exact smoothing identity; zero-count cap; admissibility. No hidden recurrence, mixing, stationary-mass lower bound, conditional-iid assertion, or lower-bound bridge is needed.





## Target Claim Audit

The target is matched exactly. K and M range over all admitted integers, including the smallest ones. Each source is fixed within a trajectory but may vary with K,M in the supremum. The risk is **mean TV at the actual terminal pair on the same complete trajectory**, not squared loss, a conditional row risk, independent test risk, or a random-time average. The predictor is the original full-history add-one rule. Stationarity is the only added source restriction; periodic and reducible sources remain allowed. The proof's full observation law preserves every visible symbol.

## Explicit Rate Audit

- Exposed variables: K,M; source parameters θ,π are universally quantified and do not enter constants.
- Probability mode: UC-stat is an unconditional tail bound at a fixed horizon; the final result is expected TV. There is no simultaneous-all-horizons or high-probability upgrade.
- Norm mode: TV is half L¹; all factors 1/2 in selected-row bounds are retained.
- Auxiliary choices: deterministic dyadic v≤M; finite stack size 2M; numerical series a=2c. All their admissibility conditions are checked.
- Substitution: `sqrt(Kc)=sqrt(K·K²/(M+1))=K^(3/2)/sqrt(M+1)` is exact. Nothing substitutes into a fixed old K⁵ theorem; the proof retains c through the analytic derivation and supplies its new value separately.
- Constants: 25/4, 10, the Hölder factor 25/8, empirical 125sqrt(2)/4, zero-count 1, smoothing 2, and final 48 all check.
- Baseline: the inherited analytic argument has no initialization dependence outside UC. Replacing the old arbitrary-initialization coefficient by the independently proved stationary coefficient preserves that mechanism and the original estimator. It does not reverse the old theorem or export a stationary lower bound.

## Notation Surface Audit

The public outputs are UC-stat and the original-add-one risk inequality. Stack variables, F, Z, the shifted excess, dyadic events, c, T_stat, D, and Ψ are proof-local helpers defined from the setting or a displayed construction. They do not hide unknown quantities supplied to the estimator. The scalar A in §7 locally shadows the alphabet label A from §1, but its scalar quantification and section scope are explicit; no type confusion affects an inference. No notation change is required for acceptance.

## Local Adversarial Computation

As a supplement to, not a substitute for, the symbolic proof, exhaustive binary sequence enumeration checked the deterministic flag inequality for M=1,…,7, both states, and w=1,…,M+2: **757,296 (sequence,w,state) cases passed**. The following reproduces the check:

```python
from itertools import product
cases = 0
for M in range(1, 8):
    for seq in product((0, 1), repeat=2*M+1):
        for w in range(1, M+3):
            for s in (0, 1):
                flags = sum(seq[t] == s and seq[t-M:t].count(s) < w
                            for t in range(M, 2*M+1))
                assert flags <= w
                cases += 1
assert cases == 757296
```

The integer comparisons 283²=80089, 1733²=3003289, 1683⁴=8022993935121, 2·27⁴=1062882, and 32⁴=1048576 were also recomputed exactly. These are finite sanity checks, not claims of exhaustive verification over the theorem's infinite parameter range.

## Target-Step Assembly Audit

The dependency chain is noncircular:

1. Unit_001 + stationary block law → unit_002 (new stationary UC).
2. Unit_003 + deterministic-prefix units_004–006 → the inherited L⁴ row maximum.
3. Those results + unit_007 + unconditional Hölder → unit_008 (actual selected-row error).
4. Unit_002 → unit_009 and the zero-count bound.
5. Unit_008 + unit_009 + exact add-one identity → unit_010; admissibility → unit_011.

The only new load-bearing probabilistic bridge is unit_002. The inherited maximal analysis is applied to precisely the source/path/count objects for which it was proved. No missing bridge or unsupported independent subclaim remains.

## Review Rationale

ACCEPTED is the smallest justified status: the exact local upper theorem follows under the allowed assumptions, all quantitative and dependence-sensitive steps check, and the cited inherited files match the pinned hashes. No mathematical repair, changed interface, or upstream retry is necessary. The remaining scientific task is a legitimate stationary all-common-algorithm lower bound or evidence that a better achievable rate exists; that unresolved work does not invalidate this scoped upper-bound unit. No author proof or other producer-owned artifact was edited by this reviewer.
