编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R005 independent mathematical review v1

## Verdict and useful result

**ACCEPT. No mathematical revision required.** The frozen candidate proves
that the ONE specified deterministic beta-blind guard predictor has risk
at most `2^33 sqrt(log(eK)) R(K,M,beta)` for every integer K>=2, M>=1 and
beta in [0,1], where R is the TRUE public-beta common minimax expected TV
risk in the stated full-history actual-terminal experiment. Consequently
`1 <= Gamma_all(K,M) <= 2^33 sqrt(log(eK))` is valid.

This is an upper bound only. It does not prove a necessary nonconstant
adaptation penalty, a sharp constant, or complete minimax classification.

## Procedure and source bindings

Independent review, 2026-10-30 UTC. I read the entire frozen R005,
R004 proof and independent report, R001 proof, recovered S016,
S024 and S025 scientific proofs, and the relevant S019 theorem/domain and
full lower derivation. Long outputs were revisited in separate ranges to
recover truncated portions. Acceptance is based on symbolic proof and
actual dependency bodies, not reported summaries or finite checks.
S019's unused upper proof is not re-audited. Earlier primitive source
constructions inherited by accepted dependencies are not claimed newly
re-proved. No S026–S032 historical original is used.

Frozen input identities below have public locators in SOURCE_INDEX.json.

| Source | SHA-256 |
|---|---|
| `proofs/R005_global_adaptation_upper_v1.md` | `27f54aa4a9b8396ebb2832b78c60dc892e19d4c9cea28b39155cdb0cfef8cfb6` |
| `proofs/R004_grouped_regeneration_v1.md` | `f83f79f77ca377cb8a8991eef6a39eed4f9dabb02d810078a83e437ddaa9c2b0` |
| `reviews/R004_independent_review_v1.md` | `d1975609265a1055df3a5bb2f3c7c7a6eaaf0bac2f841fc418caada11c58bbe4` |
| `proofs/R001_mixed_prefix_and_blind_transfer.md` | `e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1` |
| `S016 (SOURCE_INDEX.json)` | `bfb6ab6e9bd403d4a8502da6474b51f8b31940189dad339cfa5dac1b5ecbf645` |
| `S024 (SOURCE_INDEX.json)` | `c84c9307ff2e72fdcb1a842de6e3db210d174aaaaa4dc4eca4f6c00a8aa27405` |
| `S025 (SOURCE_INDEX.json)` | `f8412017f3e4f13ed28ee12a320f0be6adac1bb436bbb0d818444be0d899aaca` |
| `S019 (SOURCE_INDEX.json)` | `7cf5eb6a408109d534bc1537a7123b90201795d5b6450832b2649ccba739905b` |

The candidate hash matches the assigned frozen identity. The R004 review
hash matches the assigned accepted report. The report accepts the bound frozen
R004 proof; the proof body supplies the needed upper
without either moderate-log restriction. Frozen sources were not edited.

## 1. Actual algorithm identity and experiment

S024 Sections 0–1, S025 Section 1, and R001's exact-experiment section all
specify the same map. Set n=M+1, g=min(1,sqrt(K^5/n)); q is the add-one
row estimate using every departure j=0,...,M-1 at Y_M; b is the pooled
add-one estimate from X_3,...,X_(M+2), denominator M+K. The rule selects b
iff `TV(q,b)<=min(g,64 sqrt(K/(J+K)))`, otherwise q. Ties select b.
All ingredients use only K,M and full observed history. There is no beta,
class label, latent split, source information, suffix choice, or oracle
risk input. R004 Section 4 transfers its grouped event certificates to
exactly this R001 rule, not merely to an unnamed rule of similar risk.

All sources concern legal homogeneous order-two kernels, all-state
P^2 minorization by beta times an existential stationary law, arbitrary
initialization, complete M+2 symbol observations, and expected half-L1
TV at the actual same-trajectory terminal row. R005 changes none of these.
S025's failed NEXT is explicitly rejected there and is not used here.
Its successful rejection-restricted near-IID theorem concerns the unchanged
ALG and is the theorem used in its Section 9 union assembly.

## 2. Long weak-beta domain and cap consistency

For M>=K^4, K>=2, one has M>=16, n>K^4, and the capped a and hstar in
S016 equal sqrt(K^3/n) and sqrt(K^4/n), respectively. The cap in g is
retained in D=delta^n g. Thus the D,T definitions agree exactly between
S016, R004 and R005. On 0<beta<=1/2, delta>=1/2 and 0<a<=1, so
min(delta,a)>=a/2. With H=max(a,D,T),

    max(F,D,T)>=max(a/2,D,T)>=H/2,
    R>=2^-17 max(F,D,T)>=2^-18 H.

This is a genuine common-minimax lower, inherited from S016 before the
algorithm infimum. It is not a lower bound inferred from an upper
certificate or from an occupation statistic.

## 3. Scalar suppression checked on the whole range

Put c=M/n>=16/17, t=beta n, L=1+log K. Since log(1-beta)<=-beta,

    T/a=sqrt(K) delta^(M/2)<=sqrt(K) exp(-ct/2).

H>=a,T and H>0 imply

    (sqrt(t)T/H)^2 <= t min(1,K exp(-ct)).

For x>=0 the scalar inequality `x min(1,K exp(-x))<=1+log K` is valid.
For x<=log K it is at most log K. For x>=log K and log K>=1,
xe^-x decreases, so Kxe^-x<=log K. If log K<1, the second region is
bounded by the global maximum K/e<1. These branches include equality
x=log K and x=0; the K=2 branch is covered. No large-t restriction exists.
Substitution x=ct gives

    t min(1,K exp(-ct)) <= L/c <= (17/16)L,
    sqrt(t)T <= sqrt((17/16)L)H.

The exponential comparison is essential and is actually present. The
proof never simply asserts sqrt(t)=O(sqrt(log K)).

## 4. Exact arithmetic

R004 gives the same ALG upper `3[6641a+96D+160sqrt(t)T]` on this domain.
Since a,D<=H, the first two coefficients sum to 6737. Also

    17/16 = 1088/1024 < 1089/1024 = (33/32)^2,
    160*(33/32)=165, L>=1,
    3*(6737+165)=3*6902=20706<=21000.

Hence risk<=21000 sqrt(L)H<=21000*2^18 sqrt(L)R. Exactly,

    21000*2^18=5,505,024,000 < 8,589,934,592=2^33,
    8000*2^18=2,097,152,000 < 2^33.

Equivalently 21000<2^15 suffices. No omitted multiplicative factor is
needed. The cap one in the inherited upper can be dropped upward safely.

## 5. Complement, endpoints, and overlaps

The long weak-beta domain is `{M>=K^4, 0<beta<=1/2}`. Its complement in
the full parameter set consists of beta=0; beta>1/2 (including beta=1);
and 0<beta<=1/2 with M<K^4. Each lies in S025's EXACT Omega_closed:
endpoints; beta>=1/2; or its strip `M<=K^4, beta<=1/2`, respectively.
The equality M=K^4 is covered by both proofs, as is beta=1/2 when long;
there is no gap or excluded small horizon. K=2 and M=1 need no asymptotics.

S025 Section 9 defines r_closed as the minimum of the applicable g at
beta=0, i at beta=1, H_S on the strip, and F on N or B or beta>=1/2.
Its proof establishes every applicable upper for the SAME ALG: 49g,
858i, 1472H_S, and 8000F (or 337F in the other F branch). Thus the
minimum bound 8000 r_closed is a simultaneous certificate, not a rule
that selects algorithms using beta.

The corresponding lower constants are 2^-16 for g at beta=0,
1/(32sqrt(6)) for i at beta=1, 2^-18 for H_S on the strip, and 1/180
for F. S016 explicitly retains the first, second and fourth. S019's
lower derivation uses F>=a/2 and hstar>=sqrt(16/17)>1/2 throughout the
closed strip, preserving its caps even at M=K^4; hence its stated 2^-18
constant is valid. Each of these constants is at least 2^-18.

For every applicable scale s, R>=2^-18 s, so in particular
R>=2^-18 min s=2^-18 r_closed. There is no incorrect reversal from a
minimum or mismatch at overlaps. Beta=0 has r_closed=g; beta=1 has
r_closed=i; equality delta=a in the F branches is already covered by
S025. This proves the complementary upper with the exact arithmetic above.

## 6. Strict positivity and adaptation quantifiers

S016 Section 3.1 preserves the IID stationary subclass lower
`R>=i/(32sqrt(6))` for every beta, with all M+2 observations retained.
The witnesses have all rows p and stationary initial p tensor p, and
satisfy the minorization for every beta in [0,1]. For finite K,M,
i=min(1,sqrt(K/(M+1)))>0, so every denominator is strictly positive.

At any fixed beta, every beta-blind admissible algorithm is also an
admissible public-beta algorithm (one which ignores that input). Its
worst class risk therefore dominates the infimum R. Division by R,
supremum over beta and then infimum over beta-blind algorithms yield
Gamma_all>=1. The explicit single ALG proves the upper with the same
order of quantifiers. There is no interchange of infimum and supremum.
This lower 1 is distinct from S025's scale-normalized lower constant;
R005 correctly uses the actual minimax denominator, not r_closed or U_mix.

## Final disposition

**ACCEPT.** No mathematical blocker, missing required premise or required correction
remains in this review's scope. The result leaves open constant adaptation and the exact
adaptation cost. No source edits were performed, and no priority or formal-verification
claim is made.
