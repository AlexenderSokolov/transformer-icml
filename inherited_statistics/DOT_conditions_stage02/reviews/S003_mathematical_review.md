# S003 原独立审查的科学部分

原审查日期：2026-10-28。原审查结论：ACCEPTED；无数学修复要求。证据为独立上下文 LLM 数学审查，不是形式验证。本件逐字摘录原审查的范围、逐引理推理与有限检查；省略身份、调度和运行元数据。审查针对原证明哈希，不能把此份编排误称为对复制件的新审查。各单元的历史限定只限定该单元，综合结论见中文摘要。

编排说明（非原文）：以下保留原审查实际执行的有限检查及结果；原检查脚本不随本包交付，已省略内部运行命令。本次编排未重新运行这些历史数学枚举。

## Accepted Mathematical Interface

For every integer `K>=2`, `M>=1`, and public `0<=eta<=1`, let `C_eta(K)` contain exactly the legal homogeneous order-two sources whose initial pair law is within TV distance eta of **some** stationary law of the same pair kernel. For common, possibly randomized, complete-history algorithms without hidden-source advice, and the unchanged original full-history add-one rule, put

    a=min(1,K^(3/2)/sqrt(M+1)),
    b=min(1,K^(5/2)/sqrt(M+1)),
    u_s=min(1,48K^(3/2)/sqrt(M+1)),
    u_g=min(1,48K^(5/2)/sqrt(M+1)).

Then the submitted proof establishes

    max(a/180, eta b/65536)
      <= R_eta <= R_eta^+
      <= min(u_g, u_s+eta u_g),

and hence

    max(a,eta b)/65536
      <= R_eta <= R_eta^+
      <= min(1,48(a+eta b),48b)
      <= 96 max(a,eta b).

The rate is uniformly `Theta(max(a,eta b))`, including both caps and eta endpoints. The actual terminal pair and all observed symbols are retained throughout. The regime table and sample implications in Section 7 are accepted with their stated inequalities and strict cap-removal conditions. “Exact transition” is explicitly an exact matching **rate function up to universal constants**, not an exact minimax number or optimal numerical constants.

This is an initialization-transition/tightness **corollary** of the accepted stationary and arbitrary-initialization results. It does not establish a mixing-class theorem, suffix/full-history equivalence, computational-resource lower bound, or literature priority.



## Per-Lemma Audit

### Unit 1 — Exact experiment and inherited interfaces (lines 9–83)

- **Statement fidelity:** K, M, legal pair shift, all M departures, the unobserved next symbol, full history, and actual-terminal mean TV agree with the frozen contract. The existential stationary witness may depend on the source and is not algorithmic advice.
- **Dependency applicability:** S001 gives `u_s` for every stationary law; S002 gives the all-common-algorithm `a/180` lower; L1MAX's L1+ gives `u_g` for every initial law; MM5 gives the every-fixed-algorithm `b/65536` lower. The imported interfaces use exactly this loss and history.
- **Source check:** MM5's whole-history bijection, all remainder initializations, terminal-conditional testing, and finite K comparisons support the stated interface, not a discarded-data lower. Its small-K GU interface is explicitly unrestricted by program predicate I. L1MAX's statistical upper depends on GU UC, not on its own MM5 comparison or unrelated SRC costs; there is no circular S003 dependency.
- **Public eta:** after eta is fixed, an eta-designed estimator is still one fixed common history kernel among those universally quantified by S002 and MM5. If eta is undisclosed, the universal lower still applies and the eta-blind upper remains available. No parameter-dependent source advice is introduced.
- **Verdict:** PASS. Repair direction: None.

### Unit 2 — Finite stationary-law existence (lines 85–100)

- **Validity:** the Cesaro mean lies in the compact finite simplex; `(pi_T P-pi_T)=(rho P^T-rho)/T` has L1 norm at most `2/T`. A convergent subsequence and continuity give stationarity.
- **Assumption audit:** every legal pair kernel is finite and stochastic. Neither irreducibility, positivity, aperiodicity, reversibility nor convergence of the original chain is used.
- **Selector audit:** one witness is needed pointwise per fixed theta. There is no integral over a continuum of selected witnesses, so no measurable global selector is required. Source-dependent pi is permitted by the class definition.
- **Verdict:** PASS. Repair direction: None.

### Unit 3 — Complete-path actual-terminal risk linearity (lines 102–124)

- **Validity:** deterministic-start path laws are defined at every state, including states of zero mass under a particular initial law. The finite path factorization leaves exactly one factor `mu(y_0)`; integrating the common output kernel defines a bounded nonnegative `f_A,theta(y)` independent of mu.
- **Target audit:** theta is fixed in this argument. The actual terminal row and output are both computed from the same full history. Hence the initial-law mixture identity is exact despite their dependence; it does not claim TV itself is a linear function of output or target.
- **Randomization:** the same source-independent seed/output kernel is integrated under both initial laws, including arbitrary nondiscrete kernels. Finite history sums pose no interchange problem.
- **Verdict:** PASS. Repair direction: None.

### Unit 4 — Positive-part upper on the whole TV neighborhood (lines 128–147)

- **Validity:** equal total masses imply `sum(mu-pi)_+=TV(mu,pi)=e`. Pointwise `mu<=pi+delta`; multiplying by nonnegative f and summing gives `L(mu)<=L(pi)+e L(delta/e)` when e>0. At e=0 the separate stationary argument avoids normalization by zero.
- **Applicability:** L1MAX is uniform over every initial law of the same theta, so a residual law depending on mu and theta is admissible. S001 applies to the witnessing pi. Independent direct application of L1MAX to mu supplies the additional `u_g` minimum.
- **Critical distinction:** the upper uses domination, not the false assertion that every TV-close mu equals `(1-e)pi+e nu`. Thus it covers the full requested class, rather than only the contamination subclass used later for the lower.
- **Algorithm audit:** original add-one uses the original M departures, without deleting a prefix, changing its smoothing, or using eta. It is an admissible common algorithm, yielding `R_eta<=R_eta^+` in the correct direction.
- **Verdict:** PASS. Repair direction: None.

### Unit 5 — Capped upper simplification (lines 149–157)

- **Validity:** `min(1,48x)<=48min(1,x)` implies `u_s<=48a`, `u_g<=48b`; also `u_g<=1`. Therefore the exact upper is bounded by each of `1`, `48(a+eta b)`, and `48b`.
- **Absorption:** `a+eta b<=2 max(a,eta b)` proves the final coefficient 96. No uncapped expression is substituted through a minimum in the opposite direction.
- **Verdict:** PASS. Repair direction: None.

### Unit 6 — Stationary subclass lower (lines 161–168)

- **Validity:** each stationary initialization belongs to every C_eta. For each fixed common algorithm, its C_eta supremum therefore dominates its stationary supremum, which S002 bounds below by `a/180`.
- **Quantifiers:** the infimum is taken only after the per-algorithm comparison. Fixed public eta is already included in Unit 1's universal-kernel audit.
- **Verdict:** PASS. Repair direction: None.

### Unit 7 — Contaminated arbitrary-initialization lower (lines 170–199)

- **Membership:** for each fixed theta and nu choose a stationary pi_theta; `mu=(1-eta)pi_theta+eta nu` is a probability law and has distance `eta TV(nu,pi_theta)<=eta` from that witness. Exact distance eta is neither claimed nor required.
- **Loss:** Unit 3 at the same theta and same algorithm gives `L(mu)=(1-eta)L(pi_theta)+eta L(nu)>=eta L(nu)`. The stationary component can reveal information about theta without invalidating this equality or reducing the nu-component risk of the same kernel.
- **All information retained:** the algorithm sees the initial pair and entire path on both sides. It receives no component label or stationary law. Any inference available from a nu-generated history is already permitted in MM5 for that fixed algorithm.
- **Supremum/infimum:** the pointwise comparison for every theta,nu yields `sup_C L_A>=eta sup_theta,nu L_A`. MM5 then supplies the lower before the algorithm infimum. Suprema need not be attained. Eta=0 yields zero without division. No single hard source for all algorithms or horizons is claimed.
- **Verdict:** PASS. Repair direction: None.

### Unit 8 — Assembly of matching bounds (lines 201–207)

- **Validity:** the two separately proved lower inequalities combine by a maximum, not a sum at a fictitious common witness. Since `1/180>=1/65536`, their maximum is at least `max(a,eta b)/65536`.
- **Closure:** Units 4–5 and admissibility supply the whole upper chain. Add-one's own worst-case risk is no smaller than the minimax risk, so matching order for this unchanged algorithm follows.
- **Verdict:** PASS. Repair direction: None.

### Unit 9 — Regimes, crossover, and endpoint recovery (lines 209–230)

- **Algebra:** with `B_0=K A_0` and a<=b, crossover is eta=a/b. For n<=K^3 both caps are one; between K^3 and K^5 only b is capped; beyond K^5 neither is. The displayed table and shared boundary equalities follow directly.
- **Threshold:** `b<=K a`, so eta<=1/K implies eta b<=a at every horizon. For eta>1/K, `K^3<=K^3/eta^2<=K^5`, giving the stated decay/plateau/decay sequence. Zero-length and integer-empty intervals are expressly allowed.
- **Baselines:** eta=0 gives exactly stationary initialization. At eta=1 every legal source/initial law is included because a stationary witness exists and TV<=1; the exact upper reduces to u_g. At eta=0, u_s<=u_g, so the exact upper reduces to u_s, retaining the accepted stationary constant.
- **Verdict:** PASS. Repair direction: None.

### Unit 10 — Sufficient and necessary sample statements (lines 232–268)

- **Exact rate equivalence:** for `0<epsilon<1`, `a<=epsilon` forces `n>=K^3/epsilon^2`. If eta<=epsilon then eta b is automatic; if eta>epsilon it forces `b<=epsilon/eta<1`, hence `n>=eta^2 K^5/epsilon^2`. This proves (7.1), including eta=0, without an invalid cap removal.
- **Sufficiency:** setting epsilon=tau/96 in that equivalence yields (7.2) and the add-one risk guarantee. Separately `u_s+eta u_g<=48sqrt(K^3/n)+eta`; when tau>eta, (7.3) indeed suffices. The eta<=tau/2 specialization is valid.
- **Necessity:** uniform risk<=tau implies `a<=180tau` and `eta b<=65536tau`. Only under the stated strict `tau<1/180` and `tau<eta/65536`, respectively, may those caps be removed. The two displayed necessary sample inequalities have the correct constants, squares, and directions.
- **Uniform and small-error forms:** `r<=65536tau` is always necessary; using (7.1) requires `65536tau<1`. For positive eta and the stated sufficiently small tau, the sample order is `max(K^3,eta^2 K^5)/tau^2`; eta=0 has the separate stationary case. The proof correctly rejects an always-necessary eta term at coarse accuracy.
- **Verdict:** PASS. Repair direction: None.

### Unit 11 — Boundary and provenance assertions (lines 270–333)

- **Boundary audit:** all new steps are finite and valid at K=2,M=1; then a=b=1. Zero edges, deterministic rows, null initial states, reducibility, periodicity, nonunique stationary laws, and stationary mixtures create no conditioning or normalization gap.
- **Scope:** stationary witnesses remain existential; no common pi across sources, minimum stationary mass, mixing requirement, or monotonicity of empirical estimation error is assumed. Auxiliary full-history risk functions are proof devices, not algorithm inputs.
- **Classification:** standard measure domination and mixture comparison are accurately described as standard tools; the new combined initialization-dependent boundary is called a corollary, not a new tool or priority result. The suggested mixing successor is not claimed as an output.
- **Verdict:** PASS. Repair direction: None.

## Independent Exact Adversarial Checks









All tests use Python `Fraction` rational arithmetic, not floating-point tolerances. Results:

- Seven legal binary source/stationary-law pairs: five iid parameters including zero/one, a deterministic period-four pair cycle, and a reducible chain with a nontrivial mixture of two closed classes.
- Horizons M=1,...,5; 1,736 complete histories enumerated. Two common algorithms are checked: original add-one and an independently randomized mixture of add-one with an initial-symbol point-mass predictor.
- **2,450** exact whole-path linearity cases and **2,450** positive-part-domination cases passed, using all 35 initial laws on the denominator-four pair simplex.
- **9,800** exact contamination cases passed for eta in `{0,1/7,1/2,1}`: membership distance, the complete-path mixture identity, and the nonnegative lower comparison.
- Exact counterexample to the false contamination claim: pi=(1/2,1/2), mu=(3/4,1/4) have e=1/4, but solving `mu=(1-e)pi+e nu` yields nu=(3/2,-1/2), not a probability law. S003 explicitly avoids this mistake.
- **3,430** exact squared-rate/cap/regime cases passed over K=2,...,50, n values at and immediately adjacent to K^3 and K^5 plus other horizons, and seven eta values including 0,1/K,1.
- **17,150** exact sample-equivalence cases, **13,720** sufficient-condition equivalence cases, and **2,266** nonvacuous necessary-condition checks passed.

These are finite indexing, cap, and boundary sanity checks only. They do not establish the universal theorem or replace the symbolic audit. The imported minimax theorems are not claimed to have been independently verified by these finite tests.

## Hidden Subclaim, Assumption, and Notation Audits

Every independent new subclaim is audited above: finite stationary existence, deterministic-start full-path law, bounded nonnegative conditional loss, initial-law linearity, positive-part mass, residual-law normalization, source-class membership, fixed-eta algorithm quantifiers, supremum comparison, maximum-only assembly, capped regimes, and sample-direction algebra. No hidden measurability selector, independence assumption, ergodicity premise, or source-dependent algorithm is needed.

The primitive assumptions are exactly K,M ranges, homogeneity/legal pair shift, initial TV-neighborhood membership, and the algorithm-information restrictions. Stationary-law existence and contamination membership are derived before use. Nonnegativity/boundedness of loss comes from probability-vector TV. The public exports are the risk inequalities and their explicit regime/sample consequences. A_0,B_0,a,b,u_s,u_g,r are declared rate shorthand; f,delta,e,nu and Cesaro means are proof-local and do not hide new input assumptions.

## Target Claim, Explicit Rate, and Assembly Audit

The exact target is met with no narrowed parameter domain. Probability mode is expected TV; horizon mode is each fixed but arbitrary M, not all-time or stopping-time. Source/horizon-dependent worst-case selection is allowed; each experiment remains homogeneous. Constants 48,96,180,65536 are absolute, independent of K,M,eta and the source. All cap simplifications and sample cap-removal conditions are displayed and checked.

The dependency DAG is noncircular:

1. S001 + L1MAX L1+ + new positive-part/full-path comparison -> upper on all C_eta.
2. Finite stationary existence + exact full-path mixture identity + MM5 -> eta b lower, independent of S002.
3. S002 + stationary subclass inclusion -> a lower.
4. Maximum-only assembly -> matching capped transition; algebra -> regime and sample statements.

No unsupported bridge remains, and none of the comparisons modifies the observation experiment or estimator. The smallest justified verdict is ACCEPTED with no retry target.


