编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R003 independent mathematical review v1

## Verdict and useful result

**ACCEPT.** The frozen R003 proves its stated finite-domain bounds for the original full-history add-one rule and the SAME fixed beta-blind ALG of R001. All finite constants, cap branches, parity corrections, success budgets, region-union implications, and common-minimax quantifiers are valid. No mathematical revision is required.

This accepts a newly written finite-domain corollary, not a novelty claim, reconstruction of missing historical bytes, global classification, or logarithmic adaptation lower bound. Historical S031/S032 originals are absent and are not evidence for this verdict. No source was modified.

## Procedure and exact source bindings

Review date: 2026-10-30 UTC. All 113 lines of R003 and the full R001 candidate were read, together with the actual recovered S020 and S016 scientific text. S020 Section 7 and S016's experiment, lower theorem, and per-predictor maximum assembly were checked directly. The complete R001 independent review was also read. Author numerical checks were not premises; this is a symbolic mathematical review, not formal verification.

Frozen input identities below have public locators in SOURCE_INDEX.json.

| Object | Exact path | SHA-256 |
|---|---|---|
| Frozen R003 | `proofs/R003_finite_region_blind_adaptation.md` | `37a418027a3f354f6154761af01d3a0e5a0e1dbb3cc57fed9cbaa5115a22ed45` |
| R001 candidate | `proofs/R001_mixed_prefix_and_blind_transfer.md` | `e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1` |
| R001 independent acceptance | `reviews/R001_independent_review_v1.md` | `9238ec0d916ae1b2c3c8bb5a7daacfb9df69d9928864d0d0f11a2f5a2133eadf` |
| S020 recovered proof | `S020 (SOURCE_INDEX.json)` | `a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb` |
| S016 recovered proof | `S016 (SOURCE_INDEX.json)` | `bfb6ab6e9bd403d4a8502da6474b51f8b31940189dad339cfa5dac1b5ecbf645` |

The supplied R003 hash and supplied R001 review hash both match the readable bytes. The R001 review explicitly ACCEPTS the central theorem and binds the same R001 candidate hash above. Thus R001 independent acceptance is established for this review, not pending or silently presumed. Its nonblocking undefined `i` in a separate endpoint aside does not enter R003's interior-domain argument; R003 itself defines i. Any subsequent change of dependency bytes would require rebinding/review. Recovered proof hashes identify these actual readable copies, not unavailable historical objects.

## 1. Experiment and dependency scope

R003 explicitly adopts R001's complete observation `X_1,...,X_(M+2)`, M departure counts, actual terminal target, half-L1 TV, arbitrary initial pair law, legal homogeneous second-order table, and all-row two-step minorization. These agree with S020 and S016. No independent query, stationary-start restriction, hidden-label input, or suffix-only algorithm is substituted.

R001's original q and deterministic ALG are fixed by K,M and the history. Its algorithm uses the pooled add-one b and radius `rho(J)=min(g,64sqrt(K/(J+K)))`, choosing b when `TV(q,b)<=rho(J)` and otherwise q. Neither beta nor region membership is an input. R001 supplies the exact A,B,S expressions used by R003 and establishes uniformly over the full source class:

- `R^+<=min(1,A+B+S)`;
- `risk(ALG)<=min(1,3(A+B+S))`.

These are legitimate weakenings of R001's stronger minima with general bounds. S020 supplies the success-sum simplification; S016 supplies the common lower. Neither R001's accepted theorem nor this corollary treats a large upper certificate as a risk lower.

S024/S025 are mentioned only to retain existing SAME-ALG guarantees, not to supply an unexamined new inequality here. This review does not recertify the S025 proof or historical review.

## 2. Caps, floors, and elementary finite inequalities

D2 implies M>=K^4>=16, n=M+1>K^4 and delta>=1/2. Thus the caps in a and hstar are strictly inactive, giving `a=K^(3/2)/sqrt(n)` and `hstar=K^2/sqrt(n)`. The cap in g cannot be dropped and is retained throughout.

For M=2r, `floor((M-1)/2)=r-1`; for M=2r+1 it equals r. In both cases their sum with r is M-1, proving exactly `q0*qbar=delta^(M-1)`.

For even M, r>=8 gives `n/r=2+1/r<=17/8`; for odd M the smallest allowed odd horizon is at least 17, so r>=8 and `n/r=2+2/r<=9/4`. Consequently

`beta*n*delta^r <= (n/r)*(beta*r)*exp(-beta*r) <= 9/(4e)<1`.

The strict comparison follows from e>=5/2>9/4. There is no r=0 division on D2. The argument is uniform in both horizon parities and includes the smallest possible horizon.

## 3. Success sum and A/B budgets

### Success contribution

The R001 success masses `q_j=beta*delta^(j-1)` and lengths `L_j=2(r-j)` are exactly S020's end-aligned quantities. Therefore the last zero-length suffix and every odd-horizon correction are retained. D2 contains all D1 conditions from S020, so `K+log(1/q_j)<=3K`.

S020 Section 7 does not assume M<=K^4. It introduces m=2r and `a_m<=sqrt(2)*a`; its early portion is at most `80sqrt(6)*a_m` and its late portion at most `160sqrt(6)*a_m*(beta*m)*delta^floor(m/4)`. The latter scalar is at most `4/sqrt(e)` using beta<=1/2 and the maximum of x exp(-x/4). The displayed total is below `1520*a_m<2280*a<=2304*a`. The cap cases m=0 or a_m=1 are separately valid. Thus R003 correctly imports `S<=2304a` without extending an old restricted-horizon theorem by assertion.

### No-symbol-refresh A

From its exact definition,

`A<=48*delta^M*g+beta*delta^M<=96D+beta*delta^M`.

Here `delta^M*g=D/delta<=2D` is exact, with the cap on g unchanged. Also `beta*delta^M<=beta*exp(-beta*M)<=1/(eM)`. Since `a^2=K^3/(M+1)>=8/(M+1)>=1/M^2`, one has `1/(eM)<=a`. The polynomial inequality `8M^2>=M+1` holds for every integer M>=1. Hence `A<=96D+a`.

### Mixed event B

Dropping its helpful cap, replacing `K+r*lambda` by 2K and `1+(K-1)qbar` by `1+K*qbar`, and applying square-root subadditivity gives exactly

`B<=80sqrt(2)*K^(3/2)*sqrt(beta*q0) + 80sqrt(2)*K^2*sqrt(beta*q0*qbar)`.

The first term is `80sqrt(2)*a*sqrt(t*q0)<=114a`, since t*q0<1 and `(80sqrt(2))^2=12800<12996=114^2`.

The second is `80sqrt(2)*K^2*sqrt(beta)*delta^((M-1)/2)`, at most `160*K^2*sqrt(beta)*delta^(M/2)` because delta^(-1/2)<=sqrt(2). Since hstar is uncapped, this last expression is precisely `160sqrt(t)T`. Thus `B<=114a+160sqrt(t)T`.

Adding yields the asserted `2419a+96D+160sqrt(t)T`, with `2304+1+114=2419`. The factor-three ALG constants are exactly 7257, 288, and 480. The independent unit loss cap justifies both displayed minima with 1.

## 4. Region V and exact cap boundary

The two g branches give

- if n<=K^5, g=1 and `(g/hstar)^2=n/K^4`;
- if n>=K^5, g=K^(5/2)/sqrt(n) and `(g/hstar)^2=K`.

At n=K^5 both formulas equal K. In integer-horizon notation this boundary is M=K^5-1, distinct from the separately discussed ray M=K^5. No branch is lost at either point. Thus `(g/hstar)^2=d=min(K,n/K^4)` throughout D2.

All ratios are well defined because t,D,T,a,d are positive. Direct squaring gives

`(sqrt(t)T/D)^2 = t*delta^(M-2(M+1))*(hstar/g)^2 = t*delta^(-M-2)/d`,

and

`(sqrt(t)T/a)^2 = t*delta^M*(hstar/a)^2 = t*K*delta^M`.

Therefore Vlo implies `sqrt(t)T<=D`, while Vhi independently implies `sqrt(t)T<=a`. The hypothesis is a UNION, not an intersection; either implication gives `sqrt(t)T<=max(a,D)=Z`. Both a and D are at most Z, so the upper constant is `2419+96+160=2675`, and its ALG counterpart is `3*2675=8025`. No beta-dependent choice of predictor occurs when taking this union.

## 5. Common lower and adaptation quantifiers

S016 states the exact lower `R>=2^-17 max(F,D,T)` for the same full-class expected-TV experiment, with `F=max(i,min(delta,a))`. Its Proposition 4 proves the bounds for each common randomized predictor BEFORE taking the infimum; different source families may witness different lower components without adding their risks.

On D2, delta>=1/2 and 0<a<=1 imply `min(delta,a)>=a/2`: if a<=delta use a, and otherwise use delta>=1/2>=a/2. Hence `max(F,D,T)>=max(a/2,D)>=Z/2`, proving `R>=2^-18 Z`. No square root of a squared-TV lower is used. By the definition of minimax risk, `R<=R^+` and `R<=risk(ALG)`, so both original q and fixed ALG genuinely have matching scale Z on V with the stated constants.

The quantifier is one ALG for every beta at fixed K,M, not a predictor chosen after observing beta, a hidden source, labels, or a success event. At any public beta in V the uniform class upper and common lower apply. Even the beta-informed minimax R lower-bounds this particular blind ALG's worst risk. Thus taking an overlap minimum with another proven bound for this identical ALG is legitimate; choosing another predictor based on an unavailable parameter would not be, and is not done here.

## 6. Boundary and limitations

V is not asserted to equal D2. On the discussed sequence M=K^5, beta=log(K)/K^5 as K grows, the D2 restrictions hold eventually, while t~log K, delta^M~1/K and d=K. Thus the Vhi left side is asymptotic to log K and the Vlo right side is asymptotic to 1 whereas t diverges. Both conditions fail eventually. The R001 mixed certificate can retain order `sqrt(log K)/K` there, consistently with R003's limitation paragraph. This is not a necessary statistical or adaptation penalty.

No beta=1 division occurs, since D2 has beta<=1/2; beta=0 is excluded as well. All initial laws, off-support starts, complete histories, caps and parity cases remain within the inherited interfaces. The result neither creates a new difficult source nor resolves the open gap outside its matched region.

## Final disposition

**ACCEPT for the exact frozen bytes and dependency bindings above.** No mathematical defect or pending scientific dependency acceptance remains. No source edits were performed.
