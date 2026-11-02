编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R004: grouping pair-regeneration events removes the moderate-log hypotheses
2026-10-30.
This is a new grouping argument, not a re-run of the individual-event S020
sum. It preserves the original full-history rule and actual-terminal TV.

## Theorem and dependencies
Use the exact experiment and same beta-blind ALG of R001. Let K>=2,M>=1,
0<beta<=1/2, n=M+1, delta=1-beta, r=floor(M/2),
a=min(1,sqrt(K^3/n)), g=min(1,sqrt(K^5/n)).
Let E_j be the endpoint-aligned pair first-success events of S020,
j=1,...,r, and Eplus their union. Then
  E[ell_q 1_Eplus]<=min(1,6400a).                          (GS)
No hypotheses log(1/beta)<=K or r[-log(delta)]<=K are imposed.

For M>=K^4 put D=delta^n g, hstar=sqrt(K^4/n),
T=delta^(M/2)hstar, t=beta n, d=min(K,n/K^4).
Then uniformly over all such weak-beta parameters,
  R^+<=min(1,6641a+96D+160sqrt(t)T),                       (U)
  risk(ALG)<=min(1,3[6641a+96D+160sqrt(t)T]).
On either t<=d delta^(M+2) or t K delta^M<=1,
put Z=max(a,D). The full class satisfies
  2^-18 Z<=R<=R^+<=min(1,6897Z),
  R<=risk(ALG)<=min(1,20691Z).                            (MATCH)
Thus the corresponding finite region no longer needs either moderate-log
hypothesis. The critical logarithmic gap is NOT removed.

Dependencies: recovered S020 Sections 4–5 (exact augmented event law and
event-weighted original-stack inequality), recovered S016 lower,
and R001 Sections 1–5 (mixed-prefix bridge and event-radius transfer).
R001 has an independent ACCEPT. R003 algebra is reproduced where used;
R003 acceptance is not a premise of this argument.

## 1. Grouped early successes
If a=1, (GS) follows from the loss cap. Thus assume a<1, which implies
M>=K^3>=8 and r>=4. Set h=floor(r/2), H=h+1.
Group all j<=h into Fearly. Conditional only on E_j, the final suffix
is stationary of length L_j=2(r-j)>=r. Full count J dominates its count.
Consequently for each integer w>=1,
  P(Fearly,J<w)<=min(1,K^2 w/(r+1)).
Here summing disjoint E_j uses their actual total mass <=1; the conditional
stationary property is used only within each individual E_j.
S020 Lemma 2 with q=1 and c=K^2/(r+1) gives
  E[ell_q 1_Fearly]<=80sqrt(K^3/(r+1))<=114a,             (1)
because n<=2r+2. No log(1/beta) appears.

## 2. Dyadic late-success groups
For j>h set s=r-j, so 0<=s<=r-h-1<=H-1. For each power of two v<=H,
let F_v be the union of those E_j with v<=s+1<2v; empty groups can be omitted.
Each has at most v values of j, and j-1>=h. Hence its mass is at most
  q_v=beta v delta^h.
Also L_j+1=2s+1>=2v-1>=v, so
  P(F_v,J<w)<=q_v min(1,K^2 w/v).                         (2)
These groups are disjoint and cover all late-success labels, including
s=0 (zero-length suffix). We only use an upper bound on each event mass.

For all 0<beta<1, q_v<=beta H delta^h<1. Indeed H=h+1 and the maximum
of beta(1-beta)^h over [0,1] is h^h/(h+1)^(h+1), so
H times that maximum is (h/(h+1))^h<1 (h>=2).
Thus S020 Lemma 2 applies with q=q_v,c=K^2/v, yielding
  E[ell_q 1_F_v]
  <=80K beta delta^h sqrt(v)
       sqrt(K+h lambda+log(1/(beta v))),                  (3)
where lambda=-log(delta). The expression inside the square root is
positive because q_v<1.

Let z=beta H and A0=K+h lambda+max(0,log(1/z)).
Since log(1/(beta v))=log(1/z)+log(H/v), (3) is bounded by
  80K beta delta^h sqrt(v)[sqrt(A0)+sqrt(log(H/v))].
For all powers of two v<=H,
  sum sqrt(v)<(7/2)sqrt(H),
  sum sqrt(v)sqrt(log(H/v))<12sqrt(H).                    (4)
To verify, let V be the largest such power, H/2<V<=H, write v=V2^-k,
and extend the positive sum to k>=0. The first geometric sum is
(2+sqrt(2))sqrt(V)<(7/2)sqrt(H). For the second use
log(H/V)+k log2<=(k+1)log2<=(k+1)^2,
sqrt(V)<=sqrt(H), and
sum_(k>=0)(k+1)2^-k/2=(1-2^-1/2)^-2=6+4sqrt(2)<12.
These are bounds on numerical sums, not additional random observations.

Summing (3) over late groups and applying (4):
  late<=80K beta delta^h sqrt(H)[(7/2)sqrt(A0)+12].       (5)

## 3. Uniform constants without a log-domain assumption
Here beta<=1/2 implies lambda<=2beta and delta^h<=exp(-beta h)
=exp(-z+beta)<2 exp(-z). Also r<=2h+1 gives n<=2r+2<=4H.
Therefore K beta sqrt(H)/a=beta sqrt(Hn/K)<=2z/sqrt(K).
Moreover h lambda<=2z, K>=2, and sqrt(x+y)<=sqrt(x)+sqrt(y) give
  sqrt(A0/K)<=1+sqrt(z)+(1/sqrt(2))sqrt(log_+(1/z)),
  12/sqrt(K)<9.
Thus (5) divided by a is at most
  160z delta^h[(25/2)+(7/2)sqrt(z)+(5/2)sqrt(log_+(1/z))]
  <=320[(25/2)z exp(-z)+(7/2)z^(3/2)exp(-z)
         +(5/2)z exp(-z)sqrt(log_+(1/z))]
  <=5920.                                               (6)
For completeness, all three scalar factors in the final line are <=1:
max z exp(-z)=1/e<1;
max z^(3/2)exp(-z)=(3/(2e))^(3/2)<1;
the third vanishes for z>=1, and for 0<z<1,
z sqrt(log(1/z)) has maximum 1/sqrt(2e)<1, while exp(-z)<=1.
Adding (1) gives 6034a<6400a. This proves (GS), including all short
horizons through the initial a=1 case. Endpoint beta=0 has empty success
event and needs no logarithm; it can be included separately as zero.

## 4. Combine with the mixed-prefix event without moderate logs
For M>=K^4>=16, a=K^(3/2)/sqrt(n) is uncapped. Retain R001's
G=no symbol success and E=pair-no-success intersect symbol success,
with A and B as defined there. The same cover G,E,Eplus is valid.
The G contribution still satisfies
  A<=96D+a.                                             (7)
Proof: delta>=1/2 gives delta^M g<=2D, and
beta delta^M<=1/(eM)<=a, as n<=K^3 M^2.

Let q0=delta^r, qbar=delta^floor((M-1)/2).
The mixed event bound is
  B<=80sqrt(q0 beta K^2[1+(K-1)qbar][K+r lambda]).
We show, without log-domain assumptions,
  B<=240a+160sqrt(t)T.                                  (8)

First note n/r<=9/4 for M>=16: even M gives 2+1/r<=17/8,
odd M gives 2+2/r<=9/4. Therefore q0<=exp(-4t/9) and
tq0<=9/(4e)<1. Also r lambda<=2r beta<=M beta<=t.

If t<=K, then K+r lambda<=2K. Expanding sqrt(1+K qbar)
by sqrt(1+x)<=1+sqrt(x) gives
  B<=80sqrt(2)K^(3/2)sqrt(beta q0)
      +80sqrt(2)K^2 sqrt(beta q0 qbar)
   <=114a+160sqrt(t)T.
The first term uses tq0<1; the second uses the exact parity identity
q0 qbar=delta^(M-1) and delta>=1/2.

If t>K, use 1+(K-1)qbar<=K and K+r lambda<=K+t<2t.
Then
  B/a<=80sqrt(tq0[K+t])
      <=80sqrt(2)t exp(-2t/9)
      <=80sqrt(2)*9/(2e)<216<240.
This proves (8) in both cases.

Combining (GS),(7),(8) yields (U).
To transfer it to ALG, keep the grouped events Fearly,F_v from above.
For each such event, and E, R001's radius lemma charges at most 8/5
times its S020 event-loss certificate. Its G radius is <=A.
Thus the identical proof gives ALG risk <=3 times the combined certificate,
and the bounds (1)–(8) give the displayed factor-3 version of (U).
It would be incorrect to transfer from the scalar inequality (GS) alone;
the event-by-event certificates above are what justify this application.

## 5. Matched region and limitations
Since n>K^4, hstar=K^2/sqrt(n), and the retained cap on g gives
  (g/hstar)^2=min(K,n/K^4)=d.
Hence, exactly,
  (sqrt(t)T/D)^2=t delta^(-M-2)/d,
  (sqrt(t)T/a)^2=t K delta^M.
Either condition in the theorem makes sqrt(t)T<=Z.
The coefficients in (U) sum to 6641+96+160=6897;
multiplication by 3 gives 20691.

For the lower, delta>=1/2 and a<=1 imply F>=a/2.
Recovered S016 gives R>=2^-17 max(F,D,T)>=2^-18 Z.
This is the true common minimax lower, not an occupation or mixing-TV
surrogate. The same fixed ALG has both upper comparisons for all beta;
no class label or latent event is read.

This theorem does not close the remaining transition between the two
conditions. In particular beta n of logarithmic order can leave the
sqrt(t)T term larger than max(a,D). No claim of a necessary logarithm,
all-parameter minimax classification, or novelty is made. Grouping removes
a proof restriction caused by resolving extremely rare individual first
success times; it does not solve the full-prefix statistical question.
