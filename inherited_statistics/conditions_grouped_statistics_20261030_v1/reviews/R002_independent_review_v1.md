编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R002 independent mathematical review v1

## Verdict and useful result

**ACCEPT** the bounded mathematical results in frozen R002. The coupling-invariant obstruction, restricted-star original-add-one upper and matching restricted-family lower, sharp local arrival inequality, unconditional prefix concentration, and conditional event-trimming reduction are valid. **Occupation obligation (O) remains UNPROVED and is not accepted as a theorem.** No full-class critical O(1/K) upper or stronger statistical lower is established by this submission.

Two nonblocking domain clarifications are recorded rather than silently discarded: conditional laws on A intersect E require S>0 (when S=0 the event is null and the weighted inequalities remain valid); the general reduction (7) uses the natural S020 domain 0<q<=1, epsilon>=0, b>=0, with q=0 and b=0 treated directly. Both intended applications satisfy these conditions. No source bytes were edited.

This is independent mathematical review, not formal verification or historical-source recovery.

## Exact reviewed sources

The complete 336-line R002 candidate, full S015 proof, full R001 proof/review, full recovered S020 proof, and the full three supporting scientific files below were read. Hashes identify frozen inputs, with public locators in SOURCE_INDEX.json:

| File | SHA-256 |
|---|---|
| `proofs/R002_critical_prefix_obstruction_and_arrival.md` | `87f86a5a7f4a291e50bb78a761b765f3e3f0289bec31c823e2ed30eb65a4bc98` |
| `S015 frozen input (SOURCE_INDEX.json)` | `f8ad4cf098874285431be5a41087958fb89f156144da589de83b5fa1c3b00289` |
| `proofs/R001_mixed_prefix_and_blind_transfer.md` | `e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1` |
| `reviews/R001_independent_review_v1.md` | `9238ec0d916ae1b2c3c8bb5a7daacfb9df69d9928864d0d0f11a2f5a2133eadf` |
| `S020 (SOURCE_INDEX.json)` | `a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb` |
| `L1MAX (SOURCE_INDEX.json)` | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` |
| `GU (SOURCE_INDEX.json)` | `f4abb8e565d58c5af9f6f52ca1e83fc78989dfeb70554e4d22ad1fab8308d275` |
| `S001 (SOURCE_INDEX.json)` | `7fa8b2119f84d9f382da80516aa8b3c277ebd2c4587dffd58d24bf16b11a77d4` |

R001's independent review accepts the bound frozen proof. S015's required units 001–007 contain self-contained construction, full likelihood, testing and count arguments; its historical common-selector comparisons are not needed for R002. S020's required original-stack mechanism was checked against L1MAX, rather than accepted as a conditional-iid assertion. S020 contains the full aligned splitting construction; no separate historical S018 premise is needed to reconstruct that elementary factorization here. Missing S026–S032 originals are not premises. Author diagnostics are not proof evidence; their complete execution claim was not independently rerun or certified by this review.

## 1. Experiment, legal family and every-residue initialization

The alphabet, M departures 0 through M-1, M+2 observed symbols, actual endpoint Y_M, half-L1 loss, and original K-letter add-one formula match all applied interfaces. The conventional occupation denominator n is M+1, not the symbol count M+2. No terminal departure or future label is observed.

I checked the exact S015 table, not a generic clock model. Distinct alphabet blocks separate D_1 through D_4 from retained star pairs. At m=3, L=6, c_6=c_0=1 and p_5=(0,1), so the sole retained transition returns to p_0. Vulnerable phases are exactly 0,1,2,4 and retained evens; their number is m+1. Safe phases 3,5,7,...,L-1 have deterministic zero output. A vulnerable zero emission lands in a genuinely default row (0,0), (u,0), or (v,0), not an active ending-zero row. Thus its next emission is zero and absorption follows. For arbitrary other starting rows, the two-step probability of 00 is at least beta; the proof does not falsely require the default successor to remain default. This verifies all-state membership with pi=delta_00.

All six initial cases matter. For k=1, the first A comes from initialization; for k=2 both first coordinates come from initialization. The k=3/4 initial w_* is fixed, not an unobserved random hard label. Retained phases have deterministic initial pairs. The UV times are exactly d+(i-1)L, ending at M, and only the first q are departures. Thus M=1,2 and every q=0 case have no training triples. No q=0,k=2 case occurs in the admitted M>=1 domain.

S015's reconstruction retains every symbol and all overlaps: each Z_i occurs in two adjacent pairs but contributes only one sampled label. The full path mass is exactly

    m^[-2(q+1)] product_i q_sigma(Z_i|A_i,B_i).

Consequently there are q iid triples and an independent uniform *actual endpoint*. This is a derived identity for this particular initialization and table, not an independent-query replacement or a discarded-statistic lower argument.

## 2. Observable support and coupling-invariant exceptional mass

The base-support event A equals all scheduled vulnerable coins failing: until the first such success the path follows the scheduled phase; at that success it leaves the specified phase support immediately. Safe coins do not affect any symbol. Their independent randomness remains independent of all base draws and the initial law after conditioning on A.

A successful endpoint-aligned pair block must end at 00. None of the pairs on A is 00. Therefore every pair label fails on A, for either parity, in *any* joint augmentation preserving the canonical history/pair-label marginal. At M=1 there are no pair blocks and E0 is the whole space, consistently. This support argument does not assume the two label systems are independent.

Hence A intersect E is exactly A with at least one of its S safe coins successful, giving (1). Its observed-history law remains the base product law when S>0. At S=0 the event has zero probability; conditional expressions there must not be interpreted as defined distributions. The weighted formulas (1) and (2) still hold with both sides zero.

The logarithmic expansion is uniform enough on M=K^5: beta M/(2m)=O(log K/K), beta L=o(1), and M beta^2=o(1). Therefore delta^H, delta^S, and delta^floor(M/2) are each asymptotic to K^-1/2. Since A intersect E is a subset of E and P(E)<=q0 under every coupling, (1) sandwiches P(E)/q0 to one. E need not equal A intersect E, and no distributional assertion about E outside A is used. Large event probability alone is not a statistical lower.

## 3. Original-add-one family risk and absorption tail

Conditional on A and T=s, all full-prefix visits to s are the q triple contexts; their count is Bin(q,1/m^2). Conditional on this count and T=s, selected labels are iid q_sigma(.|s). The same holds on positive-mass A intersect E because safe-label selection is independent of the complete product data. No corresponding statement is exported to general selected-row stacks.

The empirical TV bound (1/2)sqrt(m/j) follows by summing coordinate standard deviations. The exact K-letter add-one mixture costs at most K/(j+K), not m/(j+m); target replacement costs beta. For j>=1, (1/2)sqrt(m/j)<=sqrt(m/(j+1)); j=0 is covered by the loss cap and the displayed larger expression. The binomial inverse-moment identity holds also at q=0. Jensen/Cauchy-Schwarz is used in the upper-bound direction for the inverse-square-root moment. Thus D and both weighted bounds (2) are valid, uniformly over signs and both amplitude branches.

Off A, the first vulnerable success tau has probability at most beta at every specified time. At tau=M-1 the actual terminal row is already default, even though a second postfailure output was not observed. For earlier failure, the endpoint 00 has at least (M-tau-2)_+ counted departures. There was no 00 before failure. All its observed outputs are zero, so original add-one loss there is exactly (K-1)/(J+K), bounded as claimed. Summing the two zero-positive-part cases and the remaining harmonic terms proves (3); M=1 has only one case and is directly bounded by beta. This controls the original rule, not the special constant predictor used in S015.

At the critical ray q~2K^4, m~K/4, D=O(K^-1/2), so the active contribution is O(K^-1). The failure contribution is O((log K)^2/K^4), hence negligible. S015's full-data sign-testing argument gives delta^(H+1)alpha/8=Omega(K^-1); its unchanged conditional prior/test proof applies on A intersect E with the extra factor 1-delta^S. Thus the finite restricted family minimax and worst original-rule risk have order 1/K. E's original-rule contribution is also at most total risk, while its prior-average lower follows from A intersect E. This does not assert that each sign is hard for every rule, or that the full class has the same upper.

## 4. Full-prefix versus suffix diagnostic

The largest cyclic gap between safe departures is four, including the m=3 wrap. For 1<=l<=M, N>=l requires all safe coins in the last l departures to fail, so the numerator is at most delta^floor(l/4); for l>M the event is empty. Conditioning costs 1-delta^S. Summation gives at most 4/[beta(1-delta^S)]. For fixed last safe success tau, base history still has the product law, and the suffix includes at most N/L+1 UV departures, each matching the independent actual endpoint with probability 1/m^2. This proves (8).

The ratio of full mean to the displayed suffix upper bound is asymptotic to beta M/4=(log K)/4. It is a lower comparison to the actual mean ratio, not an assertion of equality of actual suffix mean with its bound. S=0 is explicitly excluded. This is a count diagnostic, not a risk monotonicity argument or a modified estimator.

## 5. Sharp local arrival constraint

The unique legal two-step product equals theta_ab(c)theta_bc(d). Summing minorization in d gives m_bc>=beta p(c). For p(c)>0, choosing a minimizing incoming probability gives theta_bc>=kappa R_c with 0<kappa<=1. Mixture decomposition implies v_bc<=1-kappa<1 (including kappa=1 separately). Rearranging yields both inequalities in (4), since T_ab(c)=(theta_ab(c)-beta p(c))/delta. This is valid at every predecessor a, including off-support pairs.

For p(c)=0 no division by p(c) or 1-v is made; successful symbol labels cannot emit c, but the states and observations remain admitted. The two-letter example is normalized for beta<=h<=1, has absorbing 00, and two-step masses 1,h,beta,beta at 00. Its row (1,0) has v=1-h and m=beta/h, making both displayed bounds equalities. No stronger universal local reciprocal tradeoff follows.

The stated propagation limitation is real: safe phase-3 refresh lands at (w,0), then a residual emission c_6 reaches (0,c_6) with p(c_6)=0, and later UV is also off support. Applying (4) to the refresh arrival cannot constrain every later row. This failed propagation route is preserved, not erased by the local result.

## 6. Prefix exponential supermartingale

With the filtration through Y_t, eligibility second(Y_t)=b is predictable, and conditional arrival probability is theta_ab(c)>=m. The displayed multiplier is at most exp(ma)(1-ma)<=1. Thus its partial-time version is a nonnegative supermartingale starting at one. On A_bc<=mN_b/2 its terminal value is at least exp[mN_b(1-log 2)/2]. Markov gives (5), with (1-log 2)/2>=1/8. The cited chord bound for 1/x on [1,2] indeed proves log 2<=3/4.

Shift legality yields the exact arrival/departure difference, hence A_bc<=J_bc+1, proving (6). The events and inequalities remain meaningful for real n>=0 and m=0, with trivial bound one. Selection of Y_M is not treated as a fixed row: a simultaneous use needs the K^2 union or a new argument. No bound on selected N_b is supplied by this lemma.

## 7. Event trimming, S020 interface, and conditional critical consequence

For the natural domain 0<q<=1, epsilon>=0, b>=0, remove r=min(epsilon,P(F)) mass from F beginning with smallest J. Since J has finite support, whole count levels are removed followed by at most one fractional boundary level. An independent Bernoulli coin with the required real probability suffices; it need not be rational. The remaining threshold mass is exactly max(0,P(F,J<w)-r). If epsilon<P(F), the assumed epsilon+bw bound gives at most bw; if epsilon>=P(F), the event is empty. The removed loss is at most epsilon.

For b>0 apply S020 Lemma 2 with c=b/q, retaining P(F')<=q rather than incorrectly requiring equality. The resulting square-root term is exactly 80sqrt(qb[K+log(1/q)]). The separate total loss cap q gives (7). If b=0, threshold w=M+1 forces F' null and the same conclusion follows directly. If q=0 the whole contribution is zero without evaluating log(1/q). The candidate should make this natural parameter domain explicit when reusing the general lemma outside its current application.

S020's proof uses unconditional original row stacks and attaches finite history-label kernels afterward. Its deterministic-prefix tail follows from the checked L1MAX bound; arbitrary-event integration uses min(event mass, unconditional tail), not a conditional tail. Dyadic threshold 2v, zero counts, and smoothing with ceil(x) preserve all integer boundary cases. Adding the one trimming coin therefore does not change any stack marginal or introduce a conditional-iid premise.

Under (O), q=q0, epsilon=C delta^M and b=C[beta K^2+q0 K^3/(M+1)]. On the critical ray these are Theta(K^-1/2), O(K^-1), and O(K^-5/2), respectively. Since K+log(1/q0)=O(K), (7) gives O(K^-1). R001's no-symbol term is at most delta^M=O(K^-1); S020's moderate-log success sum is O(sqrt(K^3/(M+1)))=O(K^-1), with its domain holding eventually on this ray. Its endpoint-aligned lengths are 2(r-j), including zero at the last block; no odd-horizon endpoint is moved. R001's nonnegative cover allows overlap of the no-symbol event and pair successes. Therefore the asserted *conditional* full-class conclusion follows if (O) is proved.

For completeness the active-family occupation scale mentioned in the final paragraph follows from the proven binomial identity: for integer w>=1,

    P(A intersect E,J<w)
      <=delta^H(1-delta^S) w E[1/(B+1)]
      <=delta^H(1-delta^S) m^2 w/(q+1).

On the critical ray this coefficient is O(K^-5/2), the required active scale. This says nothing comparable about E outside A for general sources. A future counterexample to (O) would negate a count claim, not automatically establish a statistical lower.

## Disposition and preserved limitations

**ACCEPT the stated bounded results, with the two nonblocking domain clarifications above.** No mathematical revision to their substantive conclusions is required. (O), selected occupation/propagation beyond the refresh, and the full-class critical risk gap remain open. Coupling optimization cannot supply a uniform o(q0) mass estimate, but this does not rule out sharper statistical treatment of E. No conditional-iid migration, algorithm substitution, missing-history premise, formal-certification claim, or count-to-risk lower inference was found.
