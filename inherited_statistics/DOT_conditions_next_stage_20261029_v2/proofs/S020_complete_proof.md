# S020 原完整历史规则的稀有事件上界 完整科学证明

编排说明（非原文）：本文件保留完整科学证明或完整科学审查推理；只省略身份控制、原提交状态、管理路径、重复来源管理表与执行记录。所有复制区间逐字节保留，原件未改；新增、复制和省略字节区间及原件全文身份见 COPY_MAP.json。原章节号和审查所引行号沿用原件，不是本副本行号；按同名章节与公式定位。来源的准确科学版本和当前可读闭包见 SOURCES.md。有限枚举只是补充证据，不是证明或形式化验证。本次装配没有重做数学审查。

当前版本：S020 v1 已经独立数学审查及最终接纳。N0/N1 的内域为 0<β<1；N2 另需 D1。TARGET 是未证明的下一步候选，不属接纳结论。下列依赖行的公共路径按 SOURCES.md 的解包层定位。

## 0. Useful result first

There is a genuine new **original full-history add-one** upper bound that gives the nonregeneration event a statistical cost. It does not condition the original row stacks to be iid, observe regeneration labels, change the endpoint, or replace the algorithm by a suffix rule.

Write

    r=floor(M/2), p=M-2r, delta=1-beta, lambda=-ln(delta),
    q_0=delta^r, q_j=beta delta^(j-1) (1<=j<=r),
    a=min(1,sqrt(K^3/(M+1))), g=min(1,sqrt(K^5/(M+1))).

For every integer K>=2, M>=1 and 0<beta<1, the new bound is

    R^+(K,M,beta) <= min{u_g(M), V},                           (N1)

    V = q_0 min{1,80 K^2 sqrt((K+r lambda)/(r+1))}
        + sum_(j=1)^r q_j min{1,
            80 K sqrt((K+ln(1/beta)+(j-1)lambda)/(2(r-j)+1))},
    u_g(M)=min{1,48 sqrt(K^5/(M+1))}.

There is no confidence tolerance and no ln M in (N1). The logarithm of each analysis event's reciprocal mass is displayed, not silently dropped. The predictor is unchanged and does not read beta.

A simpler finite-domain consequence is: if

    0<beta<=1/2, ln(1/beta)<=K, r lambda<=K,                    (D1)

then

    R^+ <= min{1,2304a + delta^r min(1,160g)}.                 (N2)

The universal constants are deliberately slack. This is a statistical nonregeneration coefficient, unlike the unit loss cap in S018. It becomes useful on long histories.

**Concrete gain and remaining gap.** At M=K^6, beta=ln K/(2K^6), K>=32, (N2) gives `R^+=O(K^-3/4)`. The optimally compared *old* S011/S018/general certificates are `Theta(K^-3/4 sqrt(ln K))` there. Thus this removes a genuine square-root logarithmic certificate loss for the original full-history rule. The known lower remains `Omega(K^-1)`, so this is not minimax matching. At the requested M=K^5, beta=ln K/(2K^5), the new nonregeneration coefficient is still capped at one. The original `Omega(K^-1/2)` to `O(K^-1/4)` risk window remains open.

## 1. Exact experiment and dependencies

The alphabet is A={0,...,K-1}; a hidden fixed homogeneous table theta has nonnegative normalized rows. The only pair transitions are `P((a,b),(b,c))=theta_ab(c)`. There is a hidden stationary pi with

    pi P=pi, P^2(s,t)>=beta pi(t) for every s,t.

The initial pair law mu is arbitrary, including off-support starts. Observe every symbol `X_1,...,X_(M+2)`. Let `Y_i=(X_(i+1),X_(i+2))`, i=0,...,M. All M departures i=0,...,M-1 are counted, and the target is the actual `theta_(Y_M)` for the unobserved next symbol. Write

    n_s=sum_(i=0)^(M-1) 1{Y_i=s},
    C_s(c)=sum_(i=0)^(M-1) 1{Y_i=s,X_(i+3)=c},
    J=n_(Y_M), p_s^+(c)=(C_s(c)+1)/(n_s+K),
    ell(H)=TV(p^+_(Y_M),theta_(Y_M)).

Every risk is unconditional expected half-L1 TV. All constructions below are analysis only. No extra observation, stationary law, table, auxiliary stack, or label is an algorithm input.

Direct frozen mathematical dependencies, all read at the indicated exact copies:

| File | SHA256 | Used content |
|---|---|---|
| `phase-review/proofs/S018_complete_proof.md` | `0bd13ecdc9d33df0cd56a5367885fa6779ce6fcabf16caf59ecbf9ed8e7b4d46` | Exact two-step complete-history splitting, unique midpoint; unconditional finite stack/count bridge; stationary count moment |
| `stage02/inherited/L1MAX_statistical_proof.md` | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` | Finite original-source stacks, deterministic-prefix maximum tail, general upper |
| `stage02/inherited/GU_UC_and_IID_interfaces.md` | `f4abb8e565d58c5af9f6f52ca1e83fc78989dfeb70554e4d22ad1fab8308d275` | First-v charging/suffix domination mechanism; its arbitrary finite-state extension is fully proved below |
| `stage02/proofs/S001_stationary_upper.md` | `7fa8b2119f84d9f382da80516aa8b3c277ebd2c4587dffd58d24bf16b11a77d4` | Stationary terminal occupation `P(J_L<w)<=min(1,K^2w/(L+1))` |
| `stage03/proofs/S011_complete_proof.md` | `8286e13dabe19b4b7adc72ab11bc65a5a8594f70c507c6321bc398f46860c762` | Exact original/suffix/pooling certificates for comparison only |
| `phase-review/proofs/S016_complete_proof.md` | `bfb6ab6e9bd403d4a8502da6474b51f8b31940189dad339cfa5dac1b5ecbf645` | All-parameter lower envelope for comparison only |
| `phase-review/proofs/S019_complete_proof.md` | `7cf5eb6a408109d534bc1537a7123b90201795d5b6450832b2649ccba739905b` | Closed finite domain and elementary early/late geometric summation; not extended as a theorem beyond M<=K^4 |

No external theorem is newly invoked and no scientific novelty claim beyond the frozen package is made. S003 is used only through S011's already-proved comparison certificate, not as a conditional residual-source theorem.

## 2. Verify the requested certificate window, including finite bounds

Fix any integer K>=2 and set M=K^5, beta=ln K/(2K^5). Since ln K<K,

    0<beta<1/(2K^4)<=1/32, delta>31/32.

Put `s=sqrt(K^5/(K^5+1))`, so `1/2<s<1`. The exact uncapped quantities are

    g=s, a=s/K, hstar=s/sqrt(K), i=s/K^2, F=a.

Indeed a<1/2<delta, so the S016 F identity is exact, including K=2. The elementary inequality

    0<=lambda-beta<=beta^2/(2delta)                            (2.1)

follows by integrating u/(1-u) from 0 to beta. Also

    M beta^2=(ln K)^2/(4K^5)<1/(4K^3)<=1/32.

Consequently, with v=delta^(M/2),

    (1/3)K^-1/4 <= v <= K^-1/4,
    (1/6)K^-1/2 <= delta^(M+1)g <= K^-1/2.                     (2.2)

For the first lower inequality the log of the ratio to K^-1/4 is at least `-M beta^2/(4delta)>-1`; use e<3. For the second, the log of `delta^(M+1)/K^-1/2` is at least

    -beta-(M+1)beta^2/(2delta)>-1,

using `(M+1)/M<=33/32`, beta<1/32 and the preceding bound; then use s>1/2. Thus the exact S016 envelope L satisfies

    (1/6)K^-1/2 <= L=max{F,delta^(M+1)g,v hstar} <= K^-1/2.    (2.3)

Its lower certificate is therefore order K^-1/2, not K^-1/4.

For S011, every suffix length 1<=L<=M has u_g(L)=1, since `48 sqrt(K^5/(L+1))>1`. Every suffix certificate is at least `h_(M-1)=delta^floor((M-1)/2)>=v`. Taking L=K^4, its other branch is bounded by

    u_s(L)+h_(M-L) <=48 K^-1/2+3K^-1/4 <=51K^-1/4.            (2.4)

To see the 3, `h_(M-L)<=exp(beta) K^(-(1-1/K)/4)`, and the ratio to K^-1/4 is `<=exp(beta+ln K/(4K))<e<3`. Hence

    (1/3)K^-1/4 <= U_suf <=min(1,51K^-1/4).                   (2.5)

The original S011 burn term is always capped at one. In fact `h_b>=v>=K^(-8/31)`, where the latter follows from `lambda<=beta/delta`, so

    13 sqrt(K) h_b^(3/4) >=13 K^(1/2-6/31)>1.

Its general branch is also one, so U_+=1. Since 2delta>1, U_pool=1. Thus the optimized S011 selector has precisely the certificate order K^-1/4.

Every S018 epsilon-certificate is at least delta^r>=v. Conversely choose epsilon=1/K; then `B_e=K+8ln K<=4K`, since e>8/3. The same early/late geometric calculation used in S019 (which itself uses no horizon upper restriction once B_e<=4K is separately checked) bounds all success terms by an absolute constant times a. Epsilon<=2a and `delta^r<=sqrt(2)v`. Thus its optimized certificate also has order K^-1/4.

These are statements about available upper certificates. Only S016 supplies a risk lower. No numerical minimum of upper certificates is promoted to actual risk.

## 3. General finite-state residual occupation lemma

**Lemma 1.** Let Q be any stochastic matrix on a set of D>=1 states, let its initial law be arbitrary, and let `Z_0,...,Z_t` be its homogeneous Markov trajectory. Set

    J_t^Q=sum_(i=0)^(t-1) 1{Z_i=Z_t}.

For all integers t>=0,w>=1,

    P(J_t^Q<w)<=min(1,D^2 w/(t+1)).                            (3.1)

This is not the stationary `Dw/(t+1)` statement.

**Proof.** For deterministic start y let `b_t(y)=P_y(J_t^Q<w)` and `B_t=max_y b_t(y)`. For 0<=l<=t, the full t-departure count of its actual endpoint dominates its count in the final l departures. Conditional on the state at time t-l, that suffix is an ordinary length-l Q-chain. Hence `b_t(y)<=E_y b_l(Z_(t-l))<=B_l`, so B_t<=B_l. This is a maximum-over-starts monotonicity statement; individual b_t(y) need not decrease.

On any deterministic sequence, `J_u^Q<w` can flag only the first w occurrences of its current state. Therefore `sum_(u=0)^t 1{J_u^Q<w}<=Dw`. Taking expectations for each deterministic start y and then summing over all D starting states gives

    sum_(u=0)^t B_u <=sum_y sum_(u=0)^t b_u(y)<=D^2w.

Since B_u>=B_t for u<=t, `(t+1)B_t<=D^2w`. Arbitrary initial laws follow by convexity, and the cap one is automatic. At t=0 the count is zero and the displayed capped bound is one. No legal-symbol structure, stationarity, recurrence or positivity was used. ∎

The D^2 here will be K^4. Replacing it by K^3 or K^2 without an additional structural argument would be an error.

## 4. End-aligned splitting and its exact joint count bounds

Set r=floor(M/2), p=M-2r in {0,1}. Generate the first p departures under theta, retaining them in the observed history and in the algorithm's counts. The pair at time p has exactly the marginal law `mu P^p`. Then apply the accepted S018 two-step split construction to the r blocks whose endpoints are p+2,...,p+2r=M. The residual kernel is

    Q_2(s,t)=(P^2(s,t)-beta pi(t))/delta.

It is a stochastic matrix on K^2 states, even for zero pi entries and off-support starts. It is not asserted to be a legal one-step second-order table.

Each block has an independent Bernoulli(beta) label. On success its endpoint is sampled freshly from pi; on failure it is sampled from Q_2. If the starting pair is (a,b) and the endpoint is (c,d), the unique midpoint is (b,c), and both symbols c,d are retained. The marginal complete block probability is

    beta pi(c,d)+delta Q_2((a,b),(c,d))
       =theta_ab(c)theta_bc(d).

Together with the possible first ordinary departure this proves equality of the **entire original symbol-history law**, not just the skeleton law. Forbidden blocks retain zero probability.

Let H_0 be no successful block and H_j be first success in block j, 1<=j<=r. They partition the augmented probability space and have masses q_0 and q_j above. On H_0 the skeleton

    Z_i=Y_(p+2i), i=0,...,r

is exactly a homogeneous Q_2 path started from `mu P^p`. This follows by summing the unrestricted prefix; labels are independent of that prefix. Its terminal pair is the actual Y_M, and its count `J_r^Q` is a sum over a subset of the original departure times. Hence J>=J_r^Q pathwise. Lemma 1 with D=K^2 gives

    P(H_0,J<w)<=q_0 min(1,c_0 w), c_0=K^4/(r+1).             (4.1)

Conditional **only** on H_j, the full suffix from pair time p+2j to M has the ordinary stationary P-path law, of length `L_j=2(r-j)`. This is the same exact factorization as S018 with the shifted anchor: prefix failures sum to one, the successful endpoint has law pi, and future unconstrained labels marginalize to P blocks. Conditioning on the observed midpoint or prefix is not used. Its terminal count is a subset of J. S001 gives, for L_j>=1,

    P(H_j,J<w)<=q_j min(1,c_j w), c_j=K^2/(L_j+1).           (4.2)

For L_j=0 the right cap is one because K^2w>=1; the zero-length suffix has count zero, so (4.2) still holds directly. The intentional parity change gives the denominator `2(r-j)+1`, not `M-2j+1` when M is odd.

## 5. An event-weighted original-stack lemma

**Lemma 2.** In the unchanged arbitrary-initialization original theta experiment, let H be an event on any finite augmentation of the complete observed history. Suppose 0<q<=1 and c>0 satisfy, for every integer w>=1,

    P(H)<=q, P(H,J<w)<=q min(1,cw).                           (5.1)

Then

    E[ell 1_H] <= q min{1,80 sqrt(c(K+ln(1/q)))}.              (5.2)

This statement does not assert a conditional iid or conditional Markov law for the original theta stacks. The optional boundary q=0 is handled directly: P(H)=0 implies zero contribution, with no logarithm evaluated. If c=0 is admitted in (5.1), take w=M+1; since J<=M, it forces P(H)=0 and again zero contribution. The displayed formula is used only for q>0,c>0. The q=1 boundary has ln(1/q)=0 and needs no limiting argument.

### 5.1 Exact augmentation of the original row-stack space

Use L1MAX's independent finite row stacks `xi_(s,l)~theta_s`, l=1,...,2M, independent of the original initial pair. They generate the exact original complete history, and

    C_s-n_s theta_s=S_(s,n_s),
    S_(s,n)=sum_(l=1)^n(e_(xi_(s,l))-theta_s).

To join any finite augmented history/label law to this space, for every history of positive original probability use its conditional augmentation kernel given that complete history, and sample from that kernel after the stack history has been generated. Define the kernel arbitrarily on zero-probability histories. This preserves the full independent stack marginal and the desired history/augmentation marginal simultaneously. The augmentation is generally dependent on the stacks; no independence is needed below. The split labels of Section 4 are one such finite augmentation.

For deterministic 1<=v<=M, define

    Z_v=max_s max_(0<=n<=2v) ||S_(s,n)||_1,
    b_v=sqrt(8Kv), a_v=sqrt(8v ln K).

The exact frozen L1MAX bound is

    P(Z_v>b_v+a_v+t)<=exp(-t^2/(4v)), t>=0.                  (5.3)

It remains valid on the augmented space because its stack marginal has not changed.

### 5.2 Truncated expectation without conditioning the stacks

For any event E with probability at most z in (0,1], tail integration and (5.3) give

    E[Z_v 1_E] <= z(b_v+a_v)
               + integral_0^infinity min(z,exp(-t^2/(4v)))dt.

Let `t_0=2sqrt(v ln(1/z))`. Integrate the cap z to t_0, then write t=t_0+x. Since `(t_0+x)^2>=t_0^2+x^2`, the remaining integral is at most

    z integral_0^infinity exp(-x^2/(4v))dx <3z sqrt(v).

For completeness, split the last integral at 2sqrt(v). The first part is at most 2sqrt(v). In the second part, x/(2sqrt(v))>=1, and integrating `(x/(2sqrt(v)))exp(-x^2/(4v))` gives `sqrt(v)e^-1<sqrt(v)`. Thus no Gaussian-integral theorem is required. Since ln K<=K/2, sqrt(8)<3 and K>=2,

    [b_v+a_v+3sqrt(v)]/(2sqrt(v)) <=4sqrt(K).

It follows that

    E[Z_v 1_E]/(2v)
       <= z v^-1/2 [4sqrt(K)+sqrt(ln(1/z))].                    (5.4)

Everything in (5.4) is an unconditional expectation; the event can select the terminal row, count, labels and arbitrary unused stack information.

### 5.3 Dyadic summation, zero counts and smoothing

Write L=ln(1/q)>=0. For v=2^l<=M, let `E_v=H intersect {v<=J<2v}` and `z_v=min(1,2cv)`. By (5.1), `P(E_v)<=qz_v`. The pathwise stack identity gives the empirical loss bound `TV(C_(Y_M)/J,theta_(Y_M))<=Z_v/(2v)` on E_v. By (5.4), its expectation on this layer is at most

    q v^-1/2 z_v [4sqrt(K)+sqrt(L)+sqrt(ln(1/z_v))].          (5.5)

Here we used sqrt(x+y)<=sqrt(x)+sqrt(y). This avoids any selected-row iid assertion.

The two scalar inequalities, for every A>0, are

    sum_(l>=0) 2^(-l/2) min(1,A2^l) <=7sqrt(A),
    sum_(l>=0) 2^(-l/2) min(1,A2^l)
                      sqrt(ln(1/min(1,A2^l))) <=12sqrt(A).   (5.6)

If A>=1 the first geometric sum is `2+sqrt(2)<7/2<=7sqrt(A)` and the second vanishes. If 0<A<1 choose integer N>=0 with A2^N<=1<A2^(N+1). The two halves of the first sum are each at most `(2+sqrt(2))sqrt(A)`, hence their total is <7sqrt(A). For the second put t=A2^N in (1/2,1] and write j=N-l on its nonzero portion. After division by sqrt(A), its j-th term is

    sqrt(t)2^(-j/2) sqrt(ln(1/t)+j ln 2)
       <=2^(-j/2)(j+1).

The infinite sum of the latter is `(1-2^-1/2)^-2=6+4sqrt(2)<12`. Equality endpoints are included. Only numerical sums, not additional row stacks, have been extended to infinity.

Apply (5.6) with A=2c to (5.5) and sum the finite actual dyadic layers. The empirical contribution is at most

    q sqrt(2c)[28sqrt(K)+7sqrt(L)+12]
       <=q sqrt(2c)[37sqrt(K)+7sqrt(L)]
       <=66q sqrt(c(K+L)),                                   (5.7)

where 12<=9sqrt(K), `37sqrt(K)+7sqrt(L)<=44sqrt(K+L)`, and sqrt(2)<3/2 were used.

The zero-count contribution is at most `q min(1,c)<=q sqrt(c)<=q sqrt(cK)`. The same exact integer-to-real layer-cake argument as L1MAX, now with the event bound (5.1), gives

    E[K/(J+K) 1_H] <=q integral_0^1 min(1,cK/t)dt
                   <=2q sqrt(cK).                           (5.8)

To check the integer step explicitly, if x=K/t-K>0 then `{J<x}={J<ceil(x)}` and `ceil(x)<=x+1<=K/t`; if x<=0 the event is empty. The original add-one mixture identity bounds its loss by empirical loss plus this smoothing term on J>=1; at J=0 use the separate cap. Combining (5.7)–(5.8) gives at most `69q sqrt(c(K+L))`, hence the advertised constant 80. Independently loss<=1 gives E[ell 1_H]<=q. This proves (5.2), including q=1. ∎

## 6. Proof of the new finite bound and a transparent alternative

Apply Lemma 2 on the exact augmented original stack/split space, separately to the partition H_0,H_1,...,H_r, with (4.1)–(4.2). Their log reciprocal masses are

    ln(1/q_0)=r lambda,
    ln(1/q_j)=ln(1/beta)+(j-1)lambda.

Sum the event risk bounds. This is exactly V in (N1). The independent inherited original-rule upper is u_g(M), so take their minimum. Every estimate is uniform over theta,mu,pi, and the final expression contains only K,M,beta. Taking the class supremum proves (N1). Because the same original algorithm is used in every bound, taking a minimum is legitimate and does not require a source-specific algorithm selector.

There is also a simpler new finite certificate directly from the accepted S018 unconditional good-event bridge. For any 0<epsilon<1, `B_e=K+ln(K^2M/epsilon)`,

    R^+ <= min{1,epsilon
       +delta^r min(1,4K^2 sqrt(B_e/(r+1)))
       +sum_(j=1)^r beta delta^(j-1)
              min(1,4K sqrt(B_e/(2(r-j)+1)))}.                (N0)

Indeed use its unconditional `E ell<=epsilon+E f_(B_e)(J)`, where `f_B(x)=min(1,2sqrt(B/(x+1)))`, then apply (4.1)–(4.2). An integer occupation bound `P(J<w)<=min(1,cw)` implies `E f_B(J)<=min(1,4sqrt(Bc))` by the exact strict-threshold/layer-cake proof in S018. This establishes (N0) without ever placing the good stack event conditionally on labels. (N1) is not claimed pointwise smaller than (N0) with its smaller numerical constants; both are valid complementary certificates.

At beta=0 one may use the direct inherited u_g(M) bound; setting q_0=1 and discarding all zero-mass success terms also gives the nonregeneration argument without defining ln(1/0). At beta=1 no Q_2 is formed: the separate accepted IID pooling result remains the correct common-minimax endpoint, and no optimal original-row claim is made. At M=1, r=0, q_0=1 and the nonregeneration cap in either new expression is one, so the statement remains valid. All odd/even cases have been covered by the anchor p.

## 7. Exact finite-domain simplification

Assume (D1). Then `K+r lambda<=2K` and each success numerator in (N1) is at most 3K. Since `r+1>=(M+1)/2`,

    min(1,80 K^2 sqrt((K+r lambda)/(r+1))) <=min(1,160g).      (7.1)

If g=1 both sides cap at one; otherwise this is the displayed uncapped comparison.

Set m=2r=M-p and `a_m=min(1,sqrt(K^3/(m+1)))`. Then `a_m<=sqrt(2)a`. If m=0 there is no success sum. If a_m=1 the success sum is at most one, so the desired bound is immediate. Otherwise use its uncapped expression and put h=floor(m/4). For j<=h the denominator m-2j+1 is at least (m+1)/2, and the early success sum is at most `80sqrt(6)a_m`. For j>h its geometric factor is at most beta delta^h. The positive denominators form a subset of {1,...,m}, so their inverse-square-root sum is at most 2sqrt(m). Thus the late contribution is at most

    160sqrt(6)a_m (beta m)delta^h.

Since h>=m/4-1 and beta<=1/2,

    (beta m)delta^h <=exp(beta)(beta m)exp(-beta m/4)
                    <=4/sqrt(e).

This gives total success contribution at most

    [80sqrt(6)+640sqrt(6/e)]a_m <1520a_m <2280a <=2304a.       (7.2)

The rough inequalities used here are sqrt(6)<3, e>2, sqrt(3)<2, and sqrt(2)<3/2. No small suffix or zero-length final atom was deleted. Combining (7.1)–(7.2) proves (N2).

Domain (D1) is sufficient, not necessary. In particular it cannot be silently dropped when M grows super-exponentially in K or beta is extraordinarily small; use (N1), (N0), and the general u_g certificate in those cases.

## 8. Genuine long-history gain, with all old branches compared

Fix M=K^6 and beta=ln K/(2K^6), K>=32. Then beta<1/2 and

    ln(1/beta)=ln2+6ln K-ln ln K <=ln2+6ln K<=K.

The last inequality holds at K=32 and its derivative is 1-6/K>0 thereafter. Also `r lambda<=M beta/(2delta)<=ln K/2<=K`. Thus (D1) holds for every specified finite K.

Here `a<=K^-3/2`, `g<=K^-1/2`, and `q_0<=sqrt(2)K^-1/4`. Therefore (N2) implies explicitly

    R^+ <=min(1,2544K^-3/4).                                 (8.1)

S016 still gives order K^-1 from its absorbing term: the exact three scales are `F~K^-3/2`, `delta^(M+1)g~K^-1`, and `delta^(M/2)hstar~K^-5/4`. This is not a matching theorem.

For the old certificate comparison let

    t_K=K^-3/4 sqrt(ln K), v=delta^(M/2).

As in Section 2, `(1/3)K^-1/4<=v<=K^-1/4`, and the original S011 mixing candidates all cap at one. Thus U_+=u_g(M), while U_pool=1. The optimized suffix certificate satisfies

    (1/3)t_K <= U_suf <=288t_K, K>=32.                        (8.2)

Here is a complete finite optimization bound, not evaluation at one selected suffix.

For every suffix length 1<=L<=M, `u_g(L)>=u_g(M)>=K^-1/2>=t_K`; the last inequality follows from ln K<=sqrt(K), whose ratio ln x/sqrt(x) is at most 2/e<1. The second candidate is at least `h_(M-L)u_g(L)`. If u_g(L)=1 this is at least v>=v K^-1/2 sqrt(ln K). If u_g(L)<1, it equals

    48 K^(5/2) h_(M-L)/sqrt(L+1)
      >=48v K^(5/2) exp(lambda L/2)/sqrt(L+1)
      >=48v K^(5/2) sqrt(lambda)
      >=(48/sqrt(2))v K^-1/2 sqrt(ln K).

For the middle inequality, write x=L+1 and minimize `exp(lambda x/2)/sqrt(x)` over x>0. Its minimum is sqrt(e lambda) at x=1/lambda; multiplication by exp(-lambda/2) is at least one times sqrt(lambda) because lambda<=1. Thus both suffix candidates are at least `(1/3)t_K`, proving the lower bound uniformly over all L.

For the upper bound choose the public integer `L=ceil(1/lambda)`. It satisfies 1<=L<=M for K>=32, since `1/lambda<=2M/ln K` and ln32>3. Since lambda L<=1+lambda, delta>=1/2 and lambda<=1,

    u_g(L)<=48 K^(5/2)sqrt(lambda)<=48K^-1/2 sqrt(ln K),
    u_s(L)<=48 K^(3/2)sqrt(lambda)<=48K^-3/2 sqrt(ln K),
    h_(M-L)<=delta^-1/2 v exp(lambda L/2)<=5v.

Their sum `u_s(L)+h_(M-L)u_g(L)` is at most 288t_K, proving (8.2). If a capped u_s or u_g is smaller, the inequalities only improve.

Every S018 tolerance-certificate is at least q_0>=v>=t_K/3; the general u_g(M) and original/pooling branches also exceed t_K/3. Consequently the finite minimum over **all** old S011, S018 and general upper certificates is Theta(t_K). The new (8.1) removes its sqrt(ln K) factor asymptotically. Constants may hide this gain at small finite K; no strict numerical improvement at K=32 is asserted.

## 9. Failure ledger and the exact remaining obstruction

1. **Rejected: multiply the inherited general original risk by the no-success mass.** Conditional on H_0 the complete path does not have the original one-step table theta. The unconditional L1MAX theorem cannot simply be applied to that conditional law. Equations (4.1) and Lemma 2 supply a legitimate alternative: only a conditional residual count law is used; original stack concentration remains unconditional.
2. **Rejected: apply stationary S001 to Q_2 on H_0.** Its initial law is mu P^p, not pi. The required safe coefficient is D^2=K^4, fully proved in Lemma 1. `pi Q_2=pi` does not make an arbitrary residual start stationary.
3. **Rejected: use only an even skeleton while silently changing the actual endpoint for odd M.** The anchor p=M mod 2 is necessary in this proof. The first ordinary departure and every midpoint are retained, and the conditional residual initial law is exactly mu P^p.
4. **Rejected: infer monotonicity of empirical risk from more observations.** Only count inclusion is used in occupation bounds. Selected-row empirical risk is controlled by unconditional stack maximal tails, not asserted to decrease pathwise.
5. **Preserved comparison error and immediate correction.** During development an update initially compared (8.1) only against the general and S018 branches and incorrectly called the old K^6 certificate Theta(K^-1/2). It was corrected immediately: a suffix of length about 1/lambda gives Theta(K^-3/4 sqrt(ln K)). Section 8 proves the complete old optimization. The theorem (N1)/(N2) itself was unaffected.
6. **The requested K^5 window remains open.** In (N1), `80K^2 sqrt((K+r lambda)/(r+1))>1` on that ray, so the no-success term is exactly q_0, of order K^-1/4. The new analysis has not supplied the extra K^-1/4 factor needed to meet the existing K^-1/2 lower.

The structural information discarded by Lemma 1 is precisely that the residual matrix is not an arbitrary K^2-state kernel: it has the constrained form

    Q_2((a,b),(c,d))
       =[theta_ab(c)theta_bc(d)-beta pi(c,d)]/delta.           (9.1)

Its first-emission marginal is

    sum_d Q_2((a,b),(c,d))=[theta_ab(c)-beta p_pi(c)]/delta,
    p_pi(c)=sum_d pi(c,d).

A rank-one subtraction and the legal product may force a tradeoff between a K^2-long transient statistical clock and the residual probability of remaining informative. The generic D^2 occupation bound does not see that tradeoff. Neither pi Q_2=pi nor the first marginal identity alone proves it.

### Concrete next proof unit

The next A-upper unit should test and, if true, prove a **source-structural weighted residual loss/occupation lemma**, not rerun Lemma 1 with a smaller unproved dimension. A useful exact target to investigate (not an asserted theorem) is

    E[ell 1_H0]
      <= C [delta^(M+1) g + delta^(M/2) hstar + a],
    hstar=min(1,sqrt(K^4/(M+1))).                              (TARGET)

Together with a success contribution at stationary scale on the present moderate-log domain this would close the proposed ray. First derive the exact residual kernel (9.1) on the accepted absorbing hard-clock and star families, keeping both symbols per block, and identify which transition opportunities make the nominal H_0 event still enter an easy/absorbing state. Search for a lawful family falsifying TARGET before using it. If it survives, isolate the weighted count or row-uncertainty inequality that distinguishes K^2-clock survival from K-clock survival. A pure unweighted `K^3/(r+1)` residual occupation claim is not justified by this result and may be false; it must not be assumed as the next theorem.



- **New mathematical output:** event-weighted original-stack lemma (5.2); exact endpoint-aligned residual occupation composition (N1), complementary (N0); finite moderate-log domain (N2); a fully compared long-history sqrt-log certificate improvement.
- **Probability:** deterministic horizon, original full history, actual endpoint, expected TV. All labels and added unused stacks are hidden proof devices. No conditional iid claim, future label, independent validation trajectory, stationary support restriction, or algorithm substitution.
- **Finite boundaries:** K=2/M=1 and zero counts covered; all Q_2 denominators require only 0<beta<1; beta endpoints separately retained; both parities and zero-length final stationary suffix included; beta is a public lower bound, not assumed maximal.


