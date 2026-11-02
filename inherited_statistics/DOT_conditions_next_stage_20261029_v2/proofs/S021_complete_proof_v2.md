# S021 固定公开乘积时钟模板的统计阻断 完整科学证明 v2

编排说明（非原文）：本文件保留完整科学证明或完整科学审查推理；只省略身份控制、原提交状态、管理路径、重复来源管理表与执行记录。所有复制区间逐字节保留，原件未改；新增、复制和省略字节区间及原件全文身份见 COPY_MAP.json。原章节号和审查所引行号沿用原件，不是本副本行号；按同名章节与公式定位。来源的准确科学版本和当前可读闭包见 SOURCES.md。有限枚举只是补充证据，不是证明或形式化验证。本次装配没有重做数学审查。

当前版本：只接纳 v2。v1 的 Lemma A 局部标题误写为条件 1–3，无法推出其存活结论；v2 明确要求条件 1–4 和已知相位初始化。完整合法反例及原五单元科学审查见 reviews/S021_mathematical_review_v1_science.md；有界修复复核见 reviews/S021_mathematical_review_v2.md。另在共同零概率历史上补齐经验规则的固定输出，使其处处为概率向量。Theorem C 原已要求 1–4，其公式、常数和范围未改。已知中心的较简上界来自论证外的复核观察，不将其冒称新学习定理。

## Immediate useful finding

**Main new outcome:** Theorem C below proves an actual statistical upper obstruction for every fixed disjoint-phase absorbing product-clock template, including arbitrary unknown W-row distributions and every intermediate period. In the finite domain M≥K⁵ it gives an exact bound with phase penalty retained; on the requested ray the restricted minimax risk is at most 5K^-1/2. Thus this architecture cannot justify the K^-1/4 endpoint. This is not an impossibility theorem for the full class. A legitimate partial-zero-row construction recipe and its precise unresolved testing obligation are supplied at the end.

**Secondary narrow corollary (not a major advance):** The exact S015 star family is statistically easier in long histories than its old family-only upper `δ^(H_M+1)` reveals. Its **restricted** minimax risk has a new finite sandwich

\[
\frac{\delta^{H_M+1}}{64}\min\{1,\sqrt{m^3/(q+1)}\}
\le R_{\mathrm{star}}\le
\delta^{H_M+1}\min\{1,\sqrt{m^3/(q+1)}\}.
\]

Here `m=floor((K−1)/4)`, `L=2m`, `q=floor(M/L)`, `H_M` is S015's exact deterministic vulnerable count, `K≥13, M≥1, 0<β<1`, and the source family, common horizon-aligned initialization, and amplitudes are exactly S015. This is an upper on that family, **not** the full `D₂(β)` class. It implies the exact S015 family has rate `Θ(K^-3/4)` on `M=K^5, β=ln K/(2K^5)` and cannot supply a stronger full-class lower there by sharper analysis of those same sources.

Full finite proofs, exact template restrictions, failed constructions, dependency hashes, and successor obligations are recorded below without changing the frozen predecessors. The initial empirical derivation is retained for the enlarged arbitrary-row family; the simpler fixed-amplitude center bound is explicitly credited to the review.

## Full finite proof of the star-family sandwich

Let `t=sqrt(m³/(q+1))`. The accepted S015 lower is `δ^(H_M+1) α/8` with `α=min(1/2,t/8)`. Consequently `α/8=min(1/16,t/64)≥min(1,t)/64`.

For the upper, use this **new common predictor**, not the original full-alphabet add-one rule. If the observed actual terminal pair is outside `U×V`, output `δ₀`. If it is `s∈U×V` but the full observed history is outside the public base-history reconstruction support of S015 Lemma 4, output `δ₀`. Otherwise let `N_s` and `C_s(w)` be the observed departures and W-label counts of that row; output `βδ₀+δ qhat_s`, where `qhat_s(w)=C_s(w)/N_s` if `N_s>0`, and `qhat_s=Unif(W)` if `N_s=0`. All of these are observed counts and public construction parameters; signs and latent coins are not inputs.

By S015 Lemma 5, on `G` the actual terminal pair belongs to `U×V` and the full conditional data are exactly `q` IID triples with uniform contexts and independent uniform actual endpoint. Off `G`, the actual target row is `δ₀` and the actual endpoint is a default row, not in `U×V`. Thus this predictor has zero loss off `G`. Conditional on `G,T=s`, `N_s∼Bin(q,1/m²)`. Conditional on `N_s=n`, its selected W labels are IID from the actual `qσ(·|s)`; this statement follows from the exact product experiment, not from a generic Markov row-count conditioning claim.

For any distribution p on m symbols, the empirical law from n≥1 IID samples obeys

\[
E\,TV(\widehat p,p)\le\tfrac12\sum_w\sqrt{p_w(1-p_w)/n}
\le\tfrac12\sqrt{m/n}\le\sqrt{m/(n+1)}.
\]

For n=0 the default-law TV is at most 1, also at most `sqrt(m/(n+1))`. Therefore, writing `ρ=1/m²`, Cauchy–Schwarz gives

\[
E TV(\widehat q_s,q_\sigma(\cdot|s))
\le\min\{1,\sqrt{m E[1/(N_s+1)]}\},
\qquad
E\frac1{N_s+1}
=\frac{1-(1-\rho)^{q+1}}{(q+1)\rho}\le\frac{m²}{q+1}.
\]

The binomial identity follows by `binom(q,n)/(n+1)=binom(q+1,n+1)/(q+1)` and includes q=0. Adding the common β mass at 0 multiplies TV by exactly δ. Multiplying by `P(G)=δ^H_M` proves the displayed upper, uniformly over every sign. The predictor is one common kernel for the whole finite family; hence it bounds the restricted minimax risk.

This proof neither conditions general-source row stacks on a stopping count nor treats latent `G` as observable advice: the actual terminal pair provides the branch used by the predictor, and the special family's exact whole-history product law supplies the binomial calculation.

### Important narrowing: the accepted shrinking-amplitude family has a simpler center bound

the exact S015 family fixes the public paired-sign amplitude α. Its known center `Unif(W)` already has

\[
TV(q_\sigma(\cdot|s),\operatorname{Unif}(W))=\alpha\lfloor m/2\rfloor/m.
\]

Thus the predictor that outputs `βδ₀+δ Unif(W)` on actual terminal `U×V`, and `δ₀` otherwise, has **exact** risk

\[
\delta^{H_M+1}\alpha\lfloor m/2\rfloor/m\le\delta^{H_M+1}\alpha/2
\]

for every sign. Together with the inherited `δ^(H_M+1)α/8` lower this gives a factor-at-most-four restricted-family sandwich immediately. Therefore matching this particular shrinking-amplitude family is a narrow standard corollary, not a major new statistical learning theorem. The empirical proof above remains useful because it applies with **arbitrary unknown distributions on W**, not merely the inherited α-sized cube. That enlarged family is used in the clock obstruction below. No stronger full-class lower or upper follows from the center bound.

The same center/empirical observation applies to S012's exact absorbing Euler family with `L=m²`, `q=floor(M/L)` and `H_M=M`. It gives restricted-family risk between `δ^(M+1)α/8` and `δ^(M+1)α/2`, with the inherited lower unchanged. At the specified K⁵ horizon its α tends to `1/256`, since `m/K→1/4`, `q/K³→16`, and `sqrt(m³/(q+1))→1/32`; hence that exact family's risk really is `Θ(K^-1/2)`. (This is its true restricted risk, not the full-class rate.)

### Finite K⁴ conversion and the K⁵ ray

For S015, `q+1>M/(2m)` and `m≤K/4`, so

\[
t²=\frac{m³}{q+1}<\frac{2m⁴}{M}\le\frac{K⁴}{128M}\le\frac{K⁴}{64(M+1)}.
\]

Together with S015's accepted `α/8≥2^-12 h_*`, this proves the accurate finite sandwich

\[
2^{-12}\delta^{H_M+1}h_*\le R_{\mathrm{star}}
\le\delta^{H_M+1}h_*,\qquad
h_* =\min\{1,\sqrt{K⁴/(M+1)}\}.
\]

This holds for every `K≥13,M≥1,0<β<1`, including q=0, all six initialized phase cases, every horizon residue, and both caps. The chosen algorithm is **not** original full-alphabet add-one; nothing here bounds that rule on the full class.

On `M=K⁵, β=ln K/(2K⁵)`, the exact S015 count is

\[
H_M=M/2+M/(2m)+e_M,\qquad |e_M|\le2m.
\]

Using `0≤−ln(1−x)−x≤x²/[2(1−x)]`,

\[
\left|\ln\delta^{H_M+1}+\tfrac14\ln K\right|
\le \frac{\ln K}{4m}+\beta(2m+1)
 +\frac{(M+1)\beta²}{2\delta}\longrightarrow0.
\]

Also `t~(1/(8 sqrt(2))) K^-1/2` and `α=t/8~(1/(64 sqrt(2))) K^-1/2`. Thus `R_star=Θ(K^-3/4)`, whereas the S012 family has rate `Θ(K^-1/2)`. Neither can reach the `K^-1/4` full-class upper by a stronger test on the same fixed family. β=0 is obtained by the direct no-refresh experiment and the same empirical/center argument; β=1 makes every row δ₀ and the restricted risk zero without conditioning on a null event. These endpoint remarks concern the constructed family only, not the full-class positive IID lower.

## New localized obstruction: disjoint-phase absorbing product clocks

This theorem is **not** a theorem about all sources in `D₂(β)`. It rules out a specified broad extension of the accepted clocks, including merely changing their period. It does not supply a common predictor over unknown mixtures of different clock geometries.

### Template definition and information contract

Fix `K≥2`, `M≥1`, `0<β<1`, and a publicly specified family of base tables `Q_ν` on the original K-symbol alphabet. There are publicly known nonempty, pairwise disjoint sets `D_0,…,D_(L−1)` of actual pair states. Let `D=∪D_t`, with `00∉D`, and require the following:

1. **Legal closed phase structure.** Under each `Q_ν`, every transition from `D_t` lands in `D_(t+1 mod L)`. Every transition is a legal shift, and `Q_ν(00)=δ₀`. No auxiliary phase state is added.
2. **Two output types.** Every phase is either safe (all its base rows equal δ₀) or vulnerable (all its base rows have zero mass at symbol 0); this classification is public and does not depend on ν. Let Z be the number of safe phases and v=L−Z.
3. **Actual class membership.** The actual table on **every** row is `θ_ν=βδ₀+δQ_ν` and satisfies `P_ν²(s,00)≥β` for all K² starting pairs. Thus `π=δ_00` is a stationary witness and these are legitimate `D₂(β)` sources. This is not checked only on reachable rows.
4. **Full product experiment.** A public sign/parameter-independent horizon-aligned initialization starts in one phase. In the entire base experiment, the actual terminal pair T is in a known query set S contained in one vulnerable phase. The full `M+2`-symbol history is publicly and invertibly encoded by q IID labeled pairs `(S_i,Z_i)`, `q=floor(M/L)`, and this **actual** T. Contexts and T are uniform on S, `d=|S|≤K²`; T is independent of the q training pairs. Given `S_i=s`, its label has arbitrary unknown law `p_{ν,s}` on a known nonzero label set W, `w=|W|≤K`. The target base row on s is `p_{ν,s}`. The encoding and initialization do not depend on the unknown row laws.

Condition 4 is a genuine restriction on the template, not inferred for arbitrary Markov sources. S012 and S015 prove it for their own geometries. The result below also applies if the row family is enlarged from their paired signs to all strictly positive W-laws (or to any family for which this product experiment is valid). Full-support endpoint data, initial residual symbols, and repeated appearances of the same emitted label remain inside this bijection.

The public template can be hard-coded into the one predictor for its own restricted family. The predictor is not given ν, θ, hidden stationary probabilities, coin labels, or future symbols. An unknown mixture over templates is outside this statement.

### Lemma A: exact structural restrictions and survival bridge

Under conditions 1–4,

\[
L\le K²-1,\qquad
Z\le\min\{K-1,\lfloor L/2\rfloor\},\qquad
\frac vL\ge\max\{\tfrac12,1-K/L\}.
\]

**Proof.** Each phase contains an actual state and the phases are disjoint, excluding 00, so `L≤K²−1`. For every safe phase, choose one state in it. Its next state has form `(b,0)` and lies in the following phase. It cannot equal 00. Distinct safe phases have distinct following phases, whose supports are disjoint; consequently their chosen `(b,0)` states are distinct among only K−1 possibilities. Thus `Z≤K−1`. Two consecutive safe phases would append 0 twice and enter 00, contrary to closure inside D. Hence safe positions form an independent set of the cyclic L-phase sequence, with `Z≤floor(L/2)` (L=1 forces Z=0). The displayed vulnerable-fraction bound follows, with K replacing K−1 only to simplify the bound.

For the survival bridge, use condition 4’s common initialization supported in its specified phase `D_k`, and realize the actual table by independent Bernoulli(β) refresh coins. Let H be the number of scheduled vulnerable phases among the M departures, and G the event that every such coin is zero. Then `P_ν(G)=δ^H`, common to ν. On G the actual full history agrees with its base history, including all initial symbols, because safe refreshes change no output.

At a vulnerable state `s=(a,b)`, the unique legal path to 00 in two steps gives

\[
P_\nu²(s,00)=\theta_\nu(s)(0)\theta_\nu(b,0)(0)
=\beta\theta_\nu(b,0)(0)\ge\beta.
\]

Since β>0 and the second factor is at most one, `θ_ν(b,0)=δ₀`, and therefore `Q_ν(b,0)=δ₀`. The first failed vulnerable coin thus enters a row whose actual target is already δ₀; one later departure reaches 00 forever. This row cannot be in D: if it were, closure under its zero output would put 00 in D. Thus off G the terminal pair is outside D and its target is δ₀, including failure on the last observed departure. On G the terminal pair lies in S. In particular the predictor can branch on the observed terminal membership in S without being given G.

Finally every complete block of L departures contains v vulnerable phases. Writing `M=qL+r`, `0≤r<L`, and retaining the exact partial count h_r,

\[
H=qv+h_r,\quad0\le h_r\le r,\qquad
H\ge Mv/L-L.
\]

All horizon residues and odd/even M are retained; no mixing-distance lower is used. ∎

### Lemma B: arbitrary-row statistical upper inside each fixed template

Under conditions 1–4, there is one fully observable predictor for the fixed template with

\[
\sup_\nu E_\nu TV(\widehat p,\theta_\nu(Y_M))
\le\delta^{H+1}\min\{1,\sqrt{dw/(q+1)}\}
\le\delta^{H+1}\min\{1,\sqrt{K³ L/M}\}.
\]

**Proof.** Output δ₀ outside S. On S, extract the q training pairs from the observed full history (give any fixed output if the history is outside the public reconstruction support), form the empirical W-law at the actual terminal context, using Unif(W) when its count is zero, and output `βδ₀+δ` times that law. This is one deterministic common kernel over the family. Lemma A shows zero loss off G. Given G and the actual `T=s`, condition 4 retains the q independent training pairs, so `N_s~Bin(q,1/d)`. Conditional on their context positions, the labels at s are IID from `p_{ν,s}`; the elementary empirical-TV calculation proved earlier gives conditional loss at most `min(1,sqrt(w E[1/(N_s+1)]))≤min(1,sqrt(dw/(q+1)))`. This bound is independent of s and ν. Multiply by the exact target scaling δ and `P(G)=δ^H`. Finally `q+1>M/L` and `dw≤K³`. No random-row IID statement is made outside the explicit product experiment. ∎

### Theorem C: no intermediate period beats both endpoints in the long-history template

Assume conditions 1–4 and **M≥K⁵**. Define `λ=−ln δ`. Then each fixed template has restricted minimax risk at most

\[
\boxed{\min\left\{1,\ \delta^{-K²}\max\left(
 \sqrt{2K⁴/M}\,\delta^{M/2},\ 
 \sqrt{K⁵/M}\,\delta^{M(1-1/K)}\right)\right\}.}
\]

This finite statement preserves the phase-error factor `δ^-K²`; it is not silently absorbed into a parameter-independent constant.

**Proof.** Set `A=Mλ`. Because `L≤K²` and M≥K⁵, the square-root in Lemma B is at most one. Lemma A gives

\[
\delta^{H+1}\sqrt{K³L/M}
\le\delta^{-K²}\sqrt{K³/M}\,
\sqrt L\exp[-A\max(1/2,1-K/L)].
\]

For `L≤2K`, the last expression without its two common prefactors is at most `sqrt(2K) exp(-A/2)`. For `2K≤L≤K²`, consider the continuous extension

\[
f(x)=\sqrt x\exp[-A(1-K/x)],\qquad
\frac{d}{dx}\ln f(x)=\frac{x-2AK}{2x²}.
\]

The derivative changes, if at all, from negative to positive. Thus f has no interior maximum; its maximum on this compact interval is attained at 2K or K². The endpoint values are `sqrt(2K) exp(-A/2)` and `K exp[-A(1-1/K)]`. Multiplying the prefactors proves the displayed bound. K=2 has a degenerate interval with the same conclusion; possible integer periods are a subset of the continuous interval, so no rounding issue is hidden. ∎

### Exact finite weak-hazard domain and the requested ray

The same theorem yields, on the finite domain

\[
M\ge K⁵,\quad0<\beta<1,\quad
\lambda(K²+M/K)\le C_0,
\]

where C₀ is any specified numerical constant,

\[
R_{\text{fixed template}}\le e^{C_0}
\max\{\sqrt{2K⁴/M}\,\delta^{M/2},
       \sqrt{K⁵/M}\,\delta^M\}.
\]

For the exact requested parameters `M=K⁵, β=ln K/(2K⁵)`, β<1/2 and `λ≤2β`. Using `ln K≤K/2`,

\[
\lambda(K²+M/K)\le\ln K(K^{-3}+K^{-1})
\le\tfrac12+\tfrac1{2K²}\le5/8.
\]

Also `δ^M≤exp(−βM)=K^-1/2` and `δ^(M/2)≤K^-1/4`. Consequently **every fixed template satisfying the listed conditions** has

\[
R_{\text{fixed template}}
\le e^{5/8}\max\{\sqrt2 K^{-3/4},K^{-1/2}\}
\le5K^{-1/2}.
\]

The loose constant 5 uses only `e<3` and `sqrt2<3/2`. Thus changing only the period, safe-phase allocation, or arbitrary W-row laws within this observable product-clock architecture cannot produce a `K^-1/4` full-class lower on the requested ray. This is a genuine restricted-experiment upper obstruction, not merely a bound on one chosen lower certificate.

## Failed constructions and exact limitations retained

1. **Simply lengthen the star clock while keeping half the phases safe.** This is impossible within disjoint actual-pair phases: Lemma A gives `L/2≤Z≤K−1`, hence L≤2(K−1) when half are safe. A Θ(K²) clock necessarily has vulnerable fraction at least `1−O(1/K)`.
2. **Mix a zero-containing Euler word with the same β symbol refresh and assume membership.** Pair uniqueness alone is insufficient. For the cyclic word `(0,1,0,2,1,1,2,2)` the eight pair states are distinct and exclude 00. But its base rows `Q_(2,1)=δ₁` and `Q_(1,0)=δ₂` are both vulnerable. After mixing each with βδ₀, the legal two-step mass from `(2,1)` to 00 is **β²<β**, so all-state minorization fails. Default all other rows to δ₀; π=δ_00 remains stationary, but the claimed β condition still fails. This explicit failed construction must not be repaired merely by checking the sampled support or invoking a general K²-state reset kernel.
3. **Strengthen S015's testing while leaving the source cube unchanged.** Its known-center upper already has the same order as its lower; on the K⁵ ray it is Θ(K^-3/4). No test sharpening can produce a larger restricted minimax risk.
4. **Use intermediate L to interpolate to K^-1/4.** Within the complete template the actual empirical-risk upper, not just the chosen lower certificate, is bounded by Theorem C; its period objective has only an interior minimum. On the requested ray the template cannot beat the inherited K^-1/2 lower scale.
5. **Interpret this as a full-class impossibility or a completed minimax formula.** Invalid. The theorem deliberately assumes a common public absorbing center 0, a fixed known geometry, exact disjoint cyclic phases, safe/nonzero output dichotomy, and a complete product experiment with uniform independent actual endpoint. Arbitrary source-dependent stationary laws, mixtures over unknown geometries, stochastic clock recurrences without these phases, partial-zero rows, and non-product endpoint/data dependence are outside it. In particular the genuine full-class interval `Ω(K^-1/2)` to the existing `O(K^-1/4)` certificate remains unresolved.
6. **Use an absorbing-state mixing distance as a statistical lower.** No such inference is used. Every result here is either an inherited full-data statistical lower, a new observable-predictor upper on an exactly specified restricted experiment, or a structural membership/count obstruction. No loss is replaced by TV mixing distance.

## A lawful construction space beyond the obstruction and concrete successor

The next lower-route unit must break at least one substantive template restriction, rather than adjust L or its constants. A concrete algebraically lawful starting point is the following **state-dependent absorption recipe** (a source construction, not a proved stronger statistical lower).

Choose public or hidden parameters `t_b∈[β,1]` for `b≠0`, and set `t_0=1`. Define 0-output probabilities on all original pair rows by

\[
h_{a,0}=t_a,\qquad
h_{a,b}=\beta/t_b\quad(b\ne0).
\]

For each `(a,b)≠00`, choose any fixed probability vector `r_(a,b)` supported on nonzero symbols, and let

\[
\theta_{a,b}=h_{a,b}\delta_0+(1-h_{a,b})r_{a,b},\qquad
\theta_{0,0}=\delta_0.
\]

The table is fixed, normalized and a legal second-order shift. For b≠0,

\[
P²((a,b),00)=h_{a,b}h_{b,0}=(\beta/t_b)t_b=\beta;
\]

for b=0 the product is `t_a≥β`. Thus **all** starts satisfy the condition with π=δ_00, for arbitrary μ. Choosing larger `h_(a,b)` above β/t_b at b≠0 retains membership as long as the `h_(b,0)=t_b` values remain fixed. This family permits partial-zero rows and non-phase Markov excursions, so it is not covered by Theorem C. Its membership is fully proved; no forecast-risk conclusion is attached.

The boundary choices t_b=β and t_b=1 explain the old geometries: at t_b=β, every row ending in b is forced to output 0, permitting safe alternating star motion; at t_b=1, rows ending in b may have minimal hazard β but the ending-zero row `(b,0)` absorbs immediately. Intermediate values necessarily charge `β/t_b>β` on rows ending in b, so they cannot be treated as β-hazard-free extra memory.

**Concrete successor contract, remaining within the same lower route:** construct or rule out a full-history hard prior in this state-dependent-absorption family that exceeds `c K^-1/2` by an unbounded factor on `M=K⁵, β=ln K/(2K⁵)`. Fix `t_U=t_V=1` for the two unknown-context symbol blocks and use sign-perturbed nonzero W labels on the U×V rows; allow a separate clock-symbol block C to have genuinely intermediate t-values and stochastic returns rather than deterministic disjoint phases. Initial pair law must be common across signs and horizon-aligned by an explicit distribution, not by an added clock state.

The exact proof obligations are:

- Give all K² rows and actual nonzero return transitions. The product identity above certifies membership but does not certify a desired phase, survival law, or endpoint concentration.
- Prove the full observed-history likelihood under each neighboring sign pair. The original initial pair and repeated occurrences of the same emitted labels must be counted exactly once.
- Quantify the **actual** endpoint distribution jointly with informative departures. One cannot simply condition on “no absorption” and reuse IID triples; with intermediate hazards the conditioned law can be biased and endpoint-dependent.
- Retain target contrast `(1−h_s)` and all information in failure/absorption histories. A no-absorption probability of K^-1/4 alone would not be a prediction lower.
- To reach the larger endpoint with constant row contrast, show simultaneously an event of probability order K^-1/4, appreciable actual terminal mass on unknown rows, and conditional sign information bounded while `M=K⁵`. Under the accepted m²-by-m row cube, this heuristically requires at most O(K³) informative triples during that event, i.e. spacing order K², but the needed full conditional testing statement must be proved rather than inferred from this heuristic.
- If every such explicit finite family is easier, give an observable-predictor upper or a specific information/survival obstruction for that family, not an inference from failed construction attempts. A rigorous impossibility for this larger recipe would be a new result and is **not** claimed here.


The producer-owned executable `long_history_lower_diagnostic_check_v1.py` independently checked 4,001 cyclic safe-phase patterns, 245,711 partial-horizon/start cases, 23,988 scalar endpoint-objective probes, and 13,022 exact rational all-state hazard-recipe rows. Its saved JSON says PASS. The safe-pattern and hazard tests use integer/Fraction arithmetic; scalar objective probes use floating arithmetic and a `1e-12` tolerance. These finite checks corroborate but do not prove the theorems and are not independent review or formal verification.

**Candidate theorem for a fresh proof/review contract:** Lemmas A/B and Theorem C, with the exact five limitations (known absorbing center, fixed public template, disjoint phases, zero/nonzero output dichotomy, full uniform-context product experiment) made theorem hypotheses. Its substantive outcome is a rigorous localized obstruction to the most direct intermediate-clock extension in a finite M≥K⁵ weak-hazard domain. The center-bound corollaries are secondary explanatory facts. The statistical full-class lower gap is still open. A successor should use the state-dependent recipe above or another explicitly justified escape, not re-run the same phase-clock calculation.


