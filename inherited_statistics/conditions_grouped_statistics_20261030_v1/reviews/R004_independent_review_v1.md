编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R004 independent mathematical review v1

## Verdict / useful result

**ACCEPT.** The frozen R004 proves its grouped-success bound (GS) for every
integer K>=2, M>=1, 0<beta<=1/2, and proves (U) and (MATCH) on their stated
finite domains. Neither log(1/beta)<=K nor r[-log(1-beta)]<=K is needed.
The constants 6400, 6641, 6897 and 20691 are valid. The original full-history
add-one rule and the SAME beta-blind ALG of accepted R001 are preserved.
No mathematical revision is required.

In particular, the new grouping is legitimate for arbitrary finite
augmented events, uses valid mass upper bounds rather than presumed exact
masses, includes the zero-length final suffix, and transfers to ALG through
individual event certificates rather than through the scalar GS inequality.
The remaining logarithmic transition gap is not solved or claimed solved.

## Procedure and exact bindings

Independent mathematical review, 2026-10-30 UTC. All 168 frozen R004 lines,
S020, R001, its independent review, and S016 were read. The proof was checked
symbolically, not accepted from numerical tests. No missing historical
S026–S032 original is a premise. Hashes identify frozen inputs; current
public locators are in SOURCE_INDEX.json.

| Object | Exact path | SHA-256 |
|---|---|---|
| Frozen candidate | `proofs/R004_grouped_regeneration_v1.md` | `f83f79f77ca377cb8a8991eef6a39eed4f9dabb02d810078a83e437ddaa9c2b0` |
| R001 | `proofs/R001_mixed_prefix_and_blind_transfer.md` | `e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1` |
| R001 review | `reviews/R001_independent_review_v1.md` | `9238ec0d916ae1b2c3c8bb5a7daacfb9df69d9928864d0d0f11a2f5a2133eadf` |
| S020 readable complete proof | `S020 (SOURCE_INDEX.json)` | `a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb` |
| S016 readable complete proof | `S016 (SOURCE_INDEX.json)` | `bfb6ab6e9bd403d4a8502da6474b51f8b31940189dad339cfa5dac1b5ecbf645` |

R001's independent review binds the frozen proof hash listed here. Its
accepted interior theorem, mixed-prefix bridge, joint augmentation and
radius lemma are available dependencies, not merely reported historical
claims. Its endpoint notation nit concerning i is irrelevant here. R003
is not a premise: the required mixed-event and matching algebra is
reproduced and independently checked in R004. This review does not re-open
all historical primitive lower-bound constructions underlying accepted
S016, nor claim formal verification or scientific novelty.

## 1. Exact experiment and inherited interfaces

The setting is the legal homogeneous second-order table with arbitrary
initial pair law, all-state P^2 minorization, full symbol history, all M
departures, and unconditional half-L1 loss at the actual terminal row.
The pair split is end-aligned with anchor M mod 2. S020 Section 4 gives
P(E_j)=beta delta^(j-1), suffix length L_j=2(r-j), and conditional-only-on-E_j
stationary suffix law. Its midpoint and every prefix observation remain in
the history. The terminal suffix count is pathwise bounded by original J.
No conditional iid claim about original row stacks is used.

S020 Lemma 2 expressly allows P(F)<=q, not only equality, and requires
P(F,J<w)<=q min(1,cw) for all positive integer w, with 0<q<=1, c>0.
It yields q min(1,80 sqrt(c[K+log(1/q)])). Its finite augmentation
construction preserves unconditional independent original stack marginals.
Thus a union of first-success labels is a valid event for this lemma.
The zero-suffix interface is valid by the trivial cap even without using
a positive-length stationary theorem.

## 2. Early successes and short horizons

If a=1, loss<=1 proves GS immediately, including M=1 and r=0. Otherwise
n>K^3, so integer M>=K^3>=8 and r>=4. Hence h=floor(r/2)>=2 and H=h+1.
For j<=h, L_j=2(r-j)>=r. Summing the disjoint E_j occupation bounds gives

    P(Fearly,J<w)<=P(Fearly) min(1,K^2 w/(r+1))
                  <=min(1,K^2 w/(r+1)).

Using q=1 is lawful even when the actual event mass is much smaller.
Lemma 2 gives at most 80 sqrt(K^3/(r+1)). Since n<=2r+2 and a is uncapped,
this is <=80 sqrt(2)a<114a. This step pays no small-beta logarithm.

## 3. Late dyadic groups, mass bounds, and suffix zero

For j>h, s=r-j ranges over integers 0,...,r-h-1. If r=2h the largest
s is h-1; if r=2h+1 it is h. In either case s+1<=H. Every such s lies
in a unique interval v<=s+1<2v with v a positive power of two <=H.
There are at most v labels in that group, and j-1>=h, so

    P(F_v)<=beta v delta^h=q_v.

Moreover L_j+1=2s+1>=2v-1>=v. Summing the individual S020 occupation
bounds therefore proves (2) with q_v and c=K^2/v. The atom s=0 is in
v=1; its denominator is 1 and its count bound is simply the cap one.
No label is omitted, duplicated, or moved to another endpoint.

Because v<=H=h+1,

    0<q_v<=beta(h+1)(1-beta)^h
          <=(h/(h+1))^h<1.

The maximum follows by differentiating beta(1-beta)^h on [0,1], whose
maximum is at beta=1/(h+1). Thus all logarithms and the event-stack
lemma's q-domain are valid, even when the upper mass exceeds the actual
mass of a partially filled last group. Applying Lemma 2 and dropping
its minimum only upwards gives exactly R004 equation (3):

    80K beta delta^h sqrt(v)
        sqrt(K+h lambda+log(1/(beta v))).

The square-root argument equals K+log(1/q_v)>0. No independence of a
grouping event and original stacks is assumed.

## 4. Numerical series and uniform success constant

Put z=beta H>0 and A0=K+h lambda+log_+(1/z). Since v<=H,
log(H/v)>=0 and the square-root split in Section 2 is valid. With V the
largest power of two <=H, V<=H<2V. Writing v=V 2^-k yields

    sum sqrt(v) <=(2+sqrt(2))sqrt(H)<(7/2)sqrt(H).

For the second series, log(H/V)+k log 2 <=(k+1)log 2<=(k+1)^2,
so it is bounded by sqrt(H) times
sum_(k>=0)(k+1)2^-k/2=6+4sqrt(2)<12. Extending these positive numerical
series is valid and adds no random observations or unobserved data.
This proves (5).

For weak beta, lambda<=2beta and

    delta^h<=exp(-beta h)=exp(-z+beta)<2exp(-z).

Also r<=2h+1 implies n<=4H, so

    K beta sqrt(H)/a=beta sqrt(Hn/K)<=2z/sqrt(K).

The estimates h lambda<=2z and K>=2 give
sqrt(A0/K)<=1+sqrt(z)+(1/sqrt(2))sqrt(log_+(1/z)), while
12/sqrt(K)<9. Thus the bracket coefficients 25/2, 7/2, 5/2 in (6)
are all legitimate upper bounds. Each displayed scalar factor is <=1:
its maximum is respectively 1/e, (3/(2e))^(3/2), or at most
1/sqrt(2e) for the third (using exp(-z)<=1 there). Consequently

    late/a <=320(25/2+7/2+5/2)=5920.

Early plus late is <=6034a<6400a. The independent loss cap supplies
min(1,6400a). Neither moderate-log hypothesis has entered. The beta=0
aside is correctly treated as an empty event, not by evaluating log(0).

## 5. Mixed-prefix cover and all-weak-beta simplification

On M>=K^4>=16, a and hstar are uncapped. R001 supplies the finite joint
augmentation and cover G,E,Eplus, with E=pair-no-success intersect
symbol-success. G can overlap Eplus, but nonnegative loss and radius
allow the cover sum. Grouping the E_j does not change this cover.

For A, delta^M g=delta^-1 D<=2D, and
beta delta^M<=beta exp(-M beta)<=1/(eM)<=a. The latter follows from
n<=K^3 M^2. Dropping the cap in A upward proves A<=96D+a.

For B, n/r<=9/4 on M>=16: even and odd cases give 2+1/r and 2+2/r,
respectively, with r>=8. Hence q0<=exp(-4t/9), tq0<=9/(4e)<1, and
r lambda<=2r beta<=t. R001's capped B can always be bounded by its
uncapped expression used in R004.

If t<=K, expand sqrt(1+K qbar)<=1+sqrt(K qbar) and use
K+r lambda<=2K. The first term is at most
80sqrt(2)a sqrt(tq0)<114a. For the second, the exact parity identity is
r+floor((M-1)/2)=M-1, so q0 qbar=delta^(M-1). The factor delta^-1/2
costs at most sqrt(2), giving at most 160sqrt(t)T.

If t>K, use 1+(K-1)qbar<=K and K+r lambda<=K+t<2t. Division by a gives

    B/a<=80sqrt(tq0[K+t])
        <=80sqrt(2)t exp(-2t/9)
        <=80sqrt(2)*9/(2e)<216<240.

The scalar maximum is over all positive t, so it certainly bounds the
restricted t>K case. The stated looser 240a+160sqrt(t)T holds in both
cases. Adding 6400a, 96D+a, and 240a+160sqrt(t)T proves exactly (U),
with coefficient 6641. The loss cap is independent and can be imposed.

## 6. Same-algorithm transfer, including certificate minima

On the M>=K^4 domain the nontrivial grouping construction is available
because a<1. For Fearly use (q,b)=(1,K^2/(r+1)); for each F_v use
(q,b)=(q_v,q_v K^2/v). These obey the hypotheses of R001's event-radius
lemma. Its comparison is with the capped certificate

    D(q,b)=min(q,80sqrt(qb[K+log(1/q)])).

This comparison is valid for upper masses, not just exact event masses.
For E it uses the original R001 q0,b_mix certificate. For G its radius
is <=A. Therefore, if C is the sum of the grouped capped success
certificates, then

    E ell_ALG<=2A+(13/5)(B+C)<=3(A+B+C).

Every estimate used to prove GS bounds C itself: equations (1) and (3)
are upward relaxations of those event certificates. Thus C<=6400a,
and the derived bounds for A and B yield the displayed factor-3 version
of (U). The proof does not incorrectly infer a radius bound from the
scalar inequality E[ell_q 1_Eplus]<=6400a alone.

ALG remains exactly the R001 history-based guard using q, pooled b,
g and rho(J)=min(g,64sqrt(K/(J+K))). No beta, class label, success time,
group label, or conditional stationary suffix is used by that predictor.
No suffix-only algorithm or source-dependent selector is substituted.
The cap one can be applied directly to ALG's probability-vector TV loss.

## 7. Matching identities, lower bound, and scope

Since n=M+1>K^4, hstar^2=K^4/n. Retaining both branches of the g cap gives

    (g/hstar)^2=min(K,n/K^4)=d.

Consequently the exact ratios are

    (sqrt(t)T/D)^2=t delta^(-M-2)/d,
    (sqrt(t)T/a)^2=t K delta^M.

The two alternative conditions in MATCH are precisely sufficient for
sqrt(t)T<=D or sqrt(t)T<=a. With Z=max(a,D), either gives
6641a+96D+160sqrt(t)T<=6897Z, and 3*6897=20691.
Both equality boundaries are included. No cap on g or hstar is silently
removed outside the stated horizon domain.

S016 supplies the true common-minimax lower
R>=2^-17 max(F,D,T) in the identical experiment, where
F=max(i,min(delta,a)). Since delta>=1/2 and a<=1,
min(delta,a)>=a/2, hence max(F,D,T)>=max(a/2,D)>=Z/2.
This proves R>=2^-18 Z. R<=R^+ and R<=risk(ALG) follow because each is
a fixed admissible common predictor's worst class risk. No upper
certificate is mistaken for a statistical lower, and no occupation,
mixing-TV, alternate endpoint, or conditional loss is substituted.

The theorem removes two sufficient proof-domain restrictions. It does
not establish matching where neither displayed matching condition holds,
prove that a logarithmic factor is necessary, or classify every parameter
regime. The concluding limitation is accurate. R003's review status at the time of submission affects no premise.

## Final disposition

**ACCEPT, no mathematical revision required.** No unresolved scientific dependency remains within this review's scope.
Frozen R004 bytes are unchanged.
