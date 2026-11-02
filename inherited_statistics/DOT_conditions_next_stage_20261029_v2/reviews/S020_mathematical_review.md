# S020 独立数学审查 完整科学推理

编排说明（非原文）：本文件保留完整科学证明或完整科学审查推理；只省略身份控制、原提交状态、管理路径、重复来源管理表与执行记录。所有复制区间逐字节保留，原件未改；新增、复制和省略字节区间及原件全文身份见 COPY_MAP.json。原章节号和审查所引行号沿用原件，不是本副本行号；按同名章节与公式定位。来源的准确科学版本和当前可读闭包见 SOURCES.md。有限枚举只是补充证据，不是证明或形式化验证。本次装配没有重做数学审查。

原审查六个单元全部 PASS；本阶段已在该独立判断后接纳 S020。七项直接来源的实际复核接口原文保留；这不等于对全部前代证明重新认证。

## Result first

**Verdict: PASS for all six units of the bounded S020 contract.** I found no blocking mathematical defect in Lemmas 1–2, (N0), (N1), (N2), the finite K^5 certificate-window calculation, or the fully optimized K^6 comparison. The new proof really controls the unchanged original full-history add-one rule at the actual terminal row. Its rare-event step uses unconditional original-stack concentration, not conditional iid samples. Its residual occupation step uses the correct arbitrary-initialization coefficient K^4.

The valid improvement is an **upper-certificate improvement**, not a matching risk theorem: on `M=K^6, beta=ln(K)/(2K^6)`, the new original-rule upper is `O(K^-3/4)`, whereas the minimum of the enumerated old S011 original/suffix/pooling, S018, and general certificates is `Theta(K^-3/4 sqrt(ln K))`. The existing risk lower is only `Omega(K^-1)`. On `M=K^5, beta=ln(K)/(2K^5)`, the `Omega(K^-1/2)` versus `O(K^-1/4)` gap remains open. The structural TARGET in §9 is **not** a proved result and was not used as a premise.


| Direct source | Recomputed SHA256 | Exact binding checked |
|---|---|---|
| `stage02/inherited/L1MAX_statistical_proof.md` | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` | Lines 19–33: arbitrary-initialization, full-history, actual-terminal TV experiment. Lines 41–77: independent finite length-2M original-source stacks and simultaneous count identity. Lines 103–125, 129–191: deterministic-prefix maximum mean, direct L1 bounded differences, and **exact shifted exponential tail**. Lines 275–315: selected-row pathwise inequality and final dyadic layer. Lines 317–368: integer smoothing, zero counts, general original upper `u_g(M)`. |
| `phase-review/proofs/S018_complete_proof.md` | `0bd13ecdc9d33df0cd56a5367885fa6779ce6fcabf16caf59ecbf9ed8e7b4d46` | Lines 13–45: legal all-pair minorization setting and old finite certificate. Lines 86–148: unconditional `E ell <= epsilon+E f_B(J)` with `B=K+ln(K^2 M/epsilon)`. Lines 150–205: stochastic two-step residual, unique legal midpoint, exact full-history law, conditional-only-on-first-success stationary suffix, and count inclusion. Lines 207–233: exact strict integer threshold and capped negative moment, including L=0. Lines 239–251: uniform source supremum and unconditional tolerance payment. |
| `stage02/inherited/GU_UC_and_IID_interfaces.md` | `f4abb8e565d58c5af9f6f52ca1e83fc78989dfeb70554e4d22ad1fab8308d275` | Lines 31–72: suffix domination, maximum-over-starts monotonicity, deterministic first-w charging, and the safe D^2 coefficient. The manuscript independently supplies the arbitrary finite-state extension, rather than claiming this legal-pair interface already covers an arbitrary residual kernel. Its IID lower section is not needed. |
| `stage02/proofs/S001_stationary_upper.md` | `7fa8b2119f84d9f382da80516aa8b3c277ebd2c4587dffd58d24bf16b11a77d4` | Lines 7–35: same actual-terminal stationary experiment. Lines 39–84: `P_pi(J_L<w)<=min(1,K^2 w/(L+1))` for integer L>=1,w>=1, any stationary law, with zeros/reducibility allowed. No L=0 result or arbitrary-initialization improvement is silently imported. |
| `stage03/proofs/S011_complete_proof.md` | `8286e13dabe19b4b7adc72ab11bc65a5a8594f70c507c6321bc398f46860c762` | Lines 9–46: common algorithm and original/suffix/pooling distinction. Lines 48–82: exact `h_b`, `u_s`, `u_g`, `U_+`, `U_suf`, `U_pool`, and assignment of certificates. Lines 102–116 and 149–182: inherited interfaces and legitimate public selector. Lines 162–173: legal product/all-row marginal identity, also consistent with manuscript §9. |
| `phase-review/proofs/S016_complete_proof.md` | `bfb6ab6e9bd403d4a8502da6474b51f8b31940189dad339cfa5dac1b5ecbf645` | Lines 9–22: exact `F,D,T` lower envelope and universal `2^-17` multiplier, not a matching formula. Lines 28–45: same all-pair, arbitrary-start, full-history class and all-common-algorithm quantifiers. Lines 61–76: retained stronger absorbing and endpoint bounds. Used only to compare available lower scales. |
| `phase-review/proofs/S019_complete_proof.md` | `7cf5eb6a408109d534bc1537a7123b90201795d5b6450832b2649ccba739905b` | Lines 9–15 and 184–192: theorem restricted to `1<=M<=K^4,0<=beta<=1/2`. Lines 103–153: finite-log, early/late geometric summation, short-suffix atoms, exact parity no-success comparison. Only the explicitly rechecked scalar summation is reused beyond K^4; the old matching theorem is not extended. |

The S003 interface enters only through the **old genuine suffix certificate** in S011. It is never applied to the conditional residual source, and no source-specific algorithm or conditional residual risk theorem is inherited from it.

## Unit 1 — K^5 finite certificate window

**Status: PASS.** Manuscript lines 69–116.

1. For `M=K^5`, `beta=ln K/(2K^5)`, `K>=2`, the bounds `beta<1/(2K^4)<=1/32`, `delta>31/32`, and `M beta^2<1/(4K^3)<=1/32` are valid. With `s=sqrt(K^5/(K^5+1))`, all four scales are uncapped and the exact identities `g=s,a=s/K,hstar=s/sqrt(K),i=s/K^2,F=a` hold, including K=2.
2. Integrating `u/(1-u)` proves `0<=lambda-beta<=beta^2/(2delta)`. Applying it to `v=delta^(M/2)` and `delta^(M+1)` gives the displayed finite lower/upper comparisons. The S016 **envelope**, before its inherited universal multiplier, is between `K^-1/2/6` and `K^-1/2`; it is not itself the risk. The manuscript preserves that distinction.
3. At every suffix length L<=M, `u_g(L)=1`. Therefore each old suffix certificate is at least `h_(M-1)>=v`. The chosen `L=K^4` proves the upper `51 K^-1/4`, using the legal deterministic suffix rather than changing the new original rule. The floor estimate for `h_(M-L)` follows from `floor((M-L)/2)>=(M-L)/2-1` and `ln delta<=-beta`.
4. The old original mixing terms really cap at one: `lambda<=beta/delta` implies `v>=K^(-8/31)`, so `13sqrt(K)h_b^(3/4)>=13K^(1/2-6/31)>1`. The old original general branch is one, as is pooling because `2delta>1`.
5. Every capped S018 certificate remains at least `q_0>=v`, since `q_0<=1`. For its upper comparison, epsilon=1/K gives `B=K+8ln K<=4K` because `sup_(x>0) ln(x)/x=1/e` and `e>8/3`. The S019 early/late calculation depends on this B bound and beta<=1/2, not otherwise on M<=K^4. Also epsilon<=2a and `q_0<=sqrt(2)v`. Thus its optimized order really is `K^-1/4`.

No numerical upper-certificate minimum is converted to a true risk lower. On this ray, N1's H0 coefficient cannot improve the power: `r+1<=K^5+1<=(33/32)K^5` gives `80K^2sqrt(K/(r+1))>=80sqrt(32/33)>1`, even before adding `r lambda` to the numerator.

## Unit 2 — Arbitrary finite-state occupation and exact endpoint-aligned split

**Status: PASS.** Manuscript lines 120–167.

### General Q lemma

For fixed Q and w, write `b_t(y)=P_y(J_t^Q<w)` and `B_t=max_y b_t(y)`. A suffix of l departures has exactly the same endpoint as the full trajectory and no larger count. Conditioning at deterministic time t-l, **not at the endpoint**, gives `b_t(y)<=E_y b_l(Z_(t-l))<=B_l`; hence `B_t<=B_l`. Individual `b_t(y)` are not claimed monotone.

For each deterministic path, at most w occurrences per state have fewer than w predecessors of that state. Thus the total number of flags is at most Dw. Taking expectations separately under each of D starts and using `max<=sum` gives `sum_(u=0)^t B_u<=D^2w`. There is no exchange of max and sum in the wrong direction. Monotonicity then yields `(t+1)B_t<=D^2w`. Convexity handles arbitrary initial laws, and t=0 gives the cap one. The proof needs neither legal-symbol transitions nor stationarity, so it genuinely applies to Q2 on D=K^2 states.

### Full-history split and parity

All-pair minorization, including every off-support starting pair, makes `Q2=(P^2-beta Pi)/delta` nonnegative and stochastic. The denominator delta is positive on the stated theorem domain. No division by stationary mass or a block transition probability occurs.

For start `(a,b)` and endpoint `(c,d)`, the **unique** legal midpoint is `(b,c)`. The mixture weight is exactly `theta_ab(c)theta_bc(d)`, so multiplying the initial law, optional first ordinary departure, and every block factor recovers every complete original symbol-history probability. Matching the skeleton alone would not establish this, but the manuscript does more: both symbols per block and the first p departure are retained in the observations and original counts. If the original product is zero, both nonnegative split components are zero.

The end anchor `p=M mod 2` is essential and correct. The residual skeleton `Z_i=Y_(p+2i)` ends at the actual Y_M for both parities. Given H0, the initial skeleton law is exactly `mu P^p`, because the labels are independent of the unrestricted first prefix. Its subsequent kernel is Q2. Its departure times `p,p+2,...,p+2r-2` are a subset of the original departure times, hence `J>=J_r^Q` pathwise. This gives `c_0=K^4/(r+1)` without a stationary-start assumption.

Given **only** first success H_j, the endpoint at p+2j has law pi, the unrestricted prefix sums out, and the later unconditioned labels recover ordinary P blocks. Thus the full suffix is a stationary P trajectory with `L_j=2(r-j)`, not a residual path. Its count also has the actual Y_M endpoint and is a subset of J. The stationary S001 coefficient is therefore `c_j=K^2/(2(r-j)+1)`. In particular, the final success has L_j=0 even at odd M, and its count bound is separately trivial because `c_j w>=1`. The odd-M denominator has not been inherited incorrectly from S018's different, start-aligned construction.

## Unit 3 — Rare-event original-stack lemma

**Status: PASS.** Manuscript lines 171–257. This is the principal new proof step.

### Exact tail and augmentation premises

The frozen L1MAX variable is exactly `Z_v=max_s max_(0<=n<=2v)||S_(s,n)||_1`, with integer `1<=v<=M`, finite row stacks through 2M, `b_v=sqrt(8Kv)`, and `a_v=sqrt(8v ln K)`. The frozen lines 182–191 give

`P(Z_v>b_v+a_v+t)<=K^2 exp(-(a_v+t)^2/(4v))<=exp(-t^2/(4v))`, for all t>=0.

The row union is over exactly K^2 rows and is paid by `a_v^2/(4v)=2ln K`. No union over M selected lengths is substituted into this tail. L1MAX's L4 consequence alone would not yield the new q-weighted logarithmic estimate; the manuscript correctly imports the stronger exponential tail actually present in the frozen proof.

The finite augmentation kernel is legitimate: if the desired history/label joint law is `P_H(h)k(l|h)`, first generate the original history from the independent stacks, then sample labels with k. Summing over labels preserves the original product-stack marginal, while summing over stacks at a fixed history gives the desired joint law. Zero-probability histories may receive an arbitrary kernel without changing any law. The labels need not remain independent of the stacks; only their correct joint history law and the unchanged unconditional stack marginal are needed. This realizes all count and loss events on one space without conditional iid.

### Tail integration

For an arbitrary event E with `P(E)<=z`, the pointwise bound by `b_v+a_v+(Z_v-b_v-a_v)_+` and layer cake give

`E[Z_v 1_E]<=z(b_v+a_v)+integral min(z,exp(-t^2/(4v)))dt`.

This uses `P(E intersect {Z_v>b_v+a_v+t})<=min(z,tail)`; it is not a statement about the tail conditional on E. At `t0=2sqrt(v ln(1/z))`, the initial integral is z t0. For t=t0+x, the remainder is at most `z integral exp(-x^2/(4v))dx<3zsqrt(v)`. The manuscript's elementary split at 2sqrt(v) is correct: the second comparison integrates to `sqrt(v)e^-1`. This also covers z=1, t0=0.

For K>=2, `ln K<=K/2` yields

`(b_v+a_v+3sqrt(v))/(2sqrt(v)) <= (sqrt(8)+2+3/sqrt(2))sqrt(K)/2 <4sqrt(K)`.

Hence the coefficient and normalization in (5.4), including the half-L1 factor, are valid.

### Dyadic event selection and scalar sums

The layers `v=2^l<=M`, `v<=J<2v`, partition every positive integer J<=M, including J=M when M is dyadic. The maxima require at most 2v<=2M, so no undefined infinite stack is used. The empirical selected-row bound is pathwise `||S_(Y_M),J||_1/(2J)<=Z_v/(2v)`.

The occupation premise at the **integer** threshold w=2v gives `P(E_v)<=q z_v`, `z_v=min(1,2cv)`. Applying (5.4) with z=q z_v gives `ln(1/z)=ln(1/q)+ln(1/z_v)` exactly; splitting the square root produces (5.5). A zero-probability actual event is harmless because q z_v is positive on the stated q,c domain.

For `A2^N<=1<A2^(N+1)`, the two halves of the first scalar sum are each bounded by `(2+sqrt(2))sqrt(A)`; their sum is below 7sqrt(A). For the second sum, `t=A2^N in (1/2,1]` and `j=N-l` give the normalized term in manuscript line 239. It is at most `2^(-j/2)(j+1)`, whose sum is `6+4sqrt(2)<12`. Equality at an exact dyadic A contributes a zero logarithmic term and is included. For A>=1 the logarithmic sum vanishes. Only scalar nonnegative upper bounds are extended to infinity, not the stack space or the actual dyadic events. There is no hidden ln M payment.

After A=2c, the empirical coefficient obeys

`sqrt(2)[28sqrt(K)+7sqrt(L)+12] <=sqrt(2)[37sqrt(K)+7sqrt(L)] <=66sqrt(K+L)`.

This verifies the stated empirical constant without optimizing it.

### Zero counts, smoothing, q/c boundaries

The zero-count contribution is bounded separately by `q min(1,c)<=q sqrt(cK)`. On J>=1, the exact add-one mixture with the K-uniform law gives empirical TV plus `K/(J+K)`. Enlarging the smoothing expectation to include J=0 only makes the bound larger; the resulting double payment at zero is conservative, not an identity error.

For t in (0,1), `{K/(J+K)>t}={J<K/t-K}`. The conversion to `J<ceil(K/t-K)` is exact, including an integer threshold, and its positive integer threshold is at most K/t because K>=1. The joint occupation premise therefore bounds the event on H by `q min(1,cK/t)`. Its integral is at most `2q sqrt(cK)`. Together the constants are at most 66+1+2=69, safely below 80. Independently `ell<=1` gives the q cap, proving (5.2).

The q=1 boundary is direct. At q=0 the event has zero probability and no logarithm is evaluated. If c=0 is separately admitted, w=M+1 forces the event mass to zero. The main formula uses only q>0,c>0. All calculations are unconditional and allow selected endpoints, counts, labels, and correlated events.

## Unit 4 — Composition into N1 and N0

**Status: PASS.** Manuscript lines 261–277.

The finite events H0,H1,...,Hr partition the augmented space, with exact masses `q_0=delta^r`, `q_j=beta delta^(j-1)`. In Lemma 2, substitution of c0 and cj produces the precise K^2 and K prefactors in N1, and the log masses are `r lambda` and `ln(1/beta)+(j-1)lambda`. Their sum is V. The capped terms sum to at most the total partition mass one. All estimates are uniform in theta,mu,pi, so the class supremum can be taken after the bound. The minimum with `u_g(M)` combines inequalities for the same unchanged original algorithm, not distinct unknown risks.

For N0, the S018 good-stack bridge is an unconditional inequality under the original history law. The end-aligned split has that same law; its conditional occupation bounds can therefore bound the scalar expectation of f_B(J). At an integer J and 0<t<1,

`{f_B(J)>t}={J<ceil(4B/t^2)-1}`,

with a positive integer threshold strictly below 4B/t^2 because B>=K>=2. The resulting integral `integral_0^1 min(1,4Bc/t^2)dt` is at most `min(1,4sqrt(Bc))`. Each event gets its own q-weighted moment; epsilon is still paid only once, unconditionally, and is not divided by q or conditioned on labels. This yields all coefficients and parity denominators of N0. No pointwise dominance of N1 over N0 is asserted or needed.

At M=1, r=0 and H0 has mass one, so the expressions reduce to the valid loss cap. At beta=0 the separately stated nonregeneration argument uses only q0=1 and the general bound; no log(1/0) occurs. At beta=1 Q2 is not formed, and the manuscript correctly leaves the pooled IID **common-minimax** endpoint distinct from any optimal original-row claim.

## Unit 5 — N2 and its exact finite domain

**Status: PASS.** Manuscript lines 281–302.

Under D1, the H0 numerator is at most 2K and the success numerator at most 3K. Since `r+1>=(M+1)/2`, the uncapped H0 coefficient is at most `160sqrt(K^5/(M+1))`; preserving the outer cap gives `min(1,160g)` even when g=1.

Set m=2r. The parity comparison `a_m<=sqrt(2)a` holds with caps. If m=0 there is no success term. If a_m=1 then `a>=1/sqrt(2)`, so the total success mass at most one is already bounded by 2304a; no uncapped a_m formula is used in that branch.

Otherwise, early j<=floor(m/4) have denominator at least (m+1)/2 and total contribution at most `80sqrt(6)a_m`. On late j, the weights are at most `beta delta^h`, and all positive denominators are distinct members of {1,...,m}, including the final denominator 1. Thus their inverse-square-root sum is at most 2sqrt(m). Converting `K^(3/2)sqrt(m)` to `a_m m` costs at most sqrt(2), giving the stated `160sqrt(6)a_m (beta m)delta^h`.

The scalar bound is correct: `delta^h<=exp(beta)exp(-beta m/4)`, the maximum of `y exp(-y/4)` is 4/e, and beta<=1/2 yields `(beta m)delta^h<=4/sqrt(e)`. Therefore the success constant is `80sqrt(6)+640sqrt(6/e)<1520`, and parity gives `<2280a<=2304a`. Caps and zero/short suffixes remain covered.

D1 is a genuine sufficient restriction, not an omitted assumption: `ln(1/beta)<=K` and `r lambda<=K` control precisely the reciprocal-event logarithms. The global theorem is N1, not an unrestricted extension of N2. In particular, the phrase “no ln M in N1” means no **separate horizon-union log term**; the displayed `ln(1/beta)` can depend on M along parameterized rays. The manuscript already exposes that dependence and warns against dropping D1, so this is a scope clarification, not a required repair.

## Unit 6 — K^6 gain, every old branch, and remaining obstruction

**Status: PASS.** Manuscript lines 306–378.

For K>=32, `ln2+6ln K<=K` holds at 32 and thereafter has increasing slack because the derivative is `1-6/K>0`. Since ln ln K>0, this proves `ln(1/beta)<=K`. Also beta<1/2, `lambda<=beta/delta`, and `r<=M/2` give `r lambda<=ln K/(4delta)<=ln K/2<=K`. Hence D1 applies at every stated finite K.

The scales `a<=K^-3/2`, `g<=K^-1/2`, and `q0<=sqrt(2)K^-1/4` give

`2304a+160q0 g <=2304K^-3/2+160sqrt(2)K^-3/4 <=2544K^-3/4`.

This is the finite capped (8.1); no actual numerical gain at K=32 is asserted. The S016 entries have orders `K^-3/2`, `K^-1`, `K^-5/4`, so its strongest displayed lower scale on this ray is K^-1.

For the old certificates, all S011 original mixing branches cap at one by the same `13sqrt(K) v^(3/4)>1` argument as at K^5; beta is even smaller. Therefore `U_+=u_g(M)`, pooling is one, and S018 is at least q0. The only potentially stronger old branch is the suffix optimization, and the manuscript bounds **every** suffix, not just a guessed minimizer:

- `u_g(L)>=u_g(M)>=K^-1/2>=t_K`, since `ln K<=sqrt(K)`; the ratio's maximum is 2/e<1.
- The other suffix candidate is at least `h_(M-L)u_g(L)`. If `u_g(L)=1`, it is at least v, which dominates `v K^-1/2sqrt(ln K)`.
- If `u_g(L)<1`, the exact floor direction gives `h_(M-L)>=v exp(lambda L/2)`. Minimizing `exp(lambda(L+1)/2)/sqrt(L+1)` over positive L+1 gives `sqrt(e lambda)`. Multiplication by `exp(-lambda/2)` leaves at least sqrt(lambda), since lambda<=1. Finally lambda>=beta. This proves the asserted lower `U_suf>=t_K/3` uniformly over all lengths and both cap branches.

For the upper, `L=ceil(1/lambda)` is an allowed public integer: `1/lambda<=2M/ln K<2M/3`, and M>=3 also pays the ceiling. The bounds on `u_g(L)`, `u_s(L)` use `lambda<=ln K/M`; the floor penalty is at most `delta^-1/2`, and `lambda L<=1+lambda`. Thus `h_(M-L)<=sqrt(2)e v<5v`, giving `U_suf<=288t_K`. The cap branches only decrease this upper.

Every old S018 capped tolerance certificate is at least q0>=v>=t_K/3, and the original/general/pooling branches also exceed t_K/3. Together with the explicit suffix upper, the minimum of all named old certificates is indeed Theta(t_K). The new original-rule certificate is asymptotically smaller by a square-root logarithm. This is stronger than merely comparing it against a poorly chosen old branch, and the preserved earlier comparison error is correctly corrected, not silently erased.

The residual formula (9.1) and its first-emission marginal follow by summing the legal two-step product over d. Neither that identity nor `pi Q2=pi` proves the conjectured structural loss/occupation estimate. The manuscript labels TARGET as a proposal requiring testing and proof, and no review acceptance is extended to it. Likewise an unweighted K^3 residual occupation coefficient is not established. The K^5 gap and absence of a global joint minimax result are explicit and correct.


The checker was written independently of the author, pins the released manuscript hash, and completed with **PASS**. It is supplementary evidence, not a proof or exhaustive validation of an infinite parameter domain.

1. **Exact Fraction arithmetic:** 70 experiments across five lawful sources (uniform IID, non-IID uniform-stationary binary source, sparse absorbing source, deterministic sparse IID source, and a ternary source with zero stationary coordinates), stationary and singular/off-support point initial laws, and M=1,...,7. It checks every-pair minorization, normalization, the direct complete symbol-history law against the end-aligned augmented law, every H0 residual skeleton law, every first-success stationary full-suffix law, same-endpoint pathwise count inclusions, and the integer joint occupation bounds. Totals: **2,030 all-pair checks; 3,866 direct histories; 26,485 augmented atoms and count comparisons; 70 exact residual skeleton laws; 120 exact stationary success-suffix laws; 1,090 integer joint bounds**.
2. **Exact Fraction general occupation checks:** D=1,...,4; deterministic cycles, transient-to-absorbing chains, uniform chains, and lazy-uniform chains; t=0,...,20; w=1,...,4. **1,344 checks** confirm maximum-over-starts monotonicity, the summed D^2 budget, and the capped endpoint bound. This is not a claim that these examples establish the general lemma.
3. **Floating scalar supplements:** **1,124 dyadic A values**, including exact powers of two; **301 rare-event tail-integral values** from z=1 down to 10^-300; and **20,004 K^5/K^6 ray scalar points**, including K=2,...,10000 and larger sparse values. The first dyadic sum includes its analytic remaining geometric tail; the logarithmic sum is finite below its saturation threshold. Observed normalized dyadic maxima were about 5.82843 and 3.68202, safely below the symbolic constants 7 and 12. No floating check is used to justify universal validity, source identity, or a missing symbolic argument.


Do not promote this to a K^5 closure, matched-risk K^6 theorem, unrestricted N2, beta-one original-rule optimum, full global joint rate, or a proved structural TARGET. Any successor is a separately authorized bounded continuation; this reviewer has not initiated one.


