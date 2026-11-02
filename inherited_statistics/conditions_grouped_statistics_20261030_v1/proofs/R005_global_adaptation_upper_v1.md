编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R005: one beta-blind predictor has a uniform sqrt(log(eK)) oracle ratio
2026-10-30.
This is an upper bound on adaptation to TRUE public-parameter minimax risk,
not a claim that the logarithm is necessary or that all joint rates are known.

## Exact claim
For every integer K>=2,M>=1 there is the SAME deterministic predictor ALG
from recovered S024/S025 and R001, using only K,M and the full observed
history, such that for EVERY beta in [0,1],
  sup_(theta,mu in D_2(beta)) E TV(ALG,theta_(Y_M))
      <= 2^33 sqrt(log(eK)) R(K,M,beta).                  (1)
Here R is the beta-informed common minimax expected TV risk in the same
legal homogeneous order-two, arbitrary-initialization, full-history,
actual-terminal experiment. The predictor reads no beta or class label.

Consequently, defining the full-domain adaptation ratio
  Gamma_all(K,M)=inf_(beta-blind A) sup_(beta in [0,1])
                   risk(A;K,M,beta)/R(K,M,beta),
one has
  1<=Gamma_all(K,M)<=2^33 sqrt(log(eK)).                   (2)
R is strictly positive since the stationary IID subclass gives i/(32sqrt6).
This is a bounded upper on the remaining possible adaptation cost, not
matching upper/lower as a function of K, and not an optimal numerical constant.

## Dependencies
1. R004 independently reviewed ACCEPT: on all M>=K^4 and 0<beta<=1/2,
   without either moderate-log hypothesis, the SAME ALG has risk at most
     3[6641a+96D+160sqrt(t)T],
   where n=M+1, t=beta n, a=sqrt(K^3/n),
   D=delta^n min(1,sqrt(K^5/n)), T=delta^(M/2)sqrt(K^4/n).
2. Recovered S016: R>=2^-17 max(F,D,T), F=max(i,min(delta,a)).
3. Recovered S025: SAME ALG <=8000 r_closed throughout its original union
   Omega_closed, consisting of beta endpoints, the S019 strip
   M<=K^4,beta<=1/2, and N or B or beta>=1/2. Here r_closed is the minimum
   of the applicable scales g,i,H_S=max(a,delta^(M/2)),F.
4. Recovered S019 lower 2^-18 H_S on its exact strip, S011/S012 lower F/180,
   general beta=0 lower 2^-16 g, and IID lower i/(32sqrt6), as explicitly
   preserved in S016 and S025's stated source interfaces.
These are inherited accepted lower bounds, not new constructions.
Missing historical S026–S032 original files are not premises.

## 1. Scalar suppression of the apparent sqrt(t) factor
On M>=K^4, M>=16 and c=M/n>=16/17. Let L=log(eK)=1+log K and
H=max(a,D,T). Then
  T/a=sqrt(K)delta^(M/2)<=sqrt(K) exp(-ct/2).
Since H>=a and H>=T,
  sqrt(t)T/H<=sqrt(t) min(1,sqrt(K)exp(-ct/2)).            (3)
For any x>=0 and K>=2,
  x min(1,K exp(-x))<=1+log K.                           (4)
Indeed if x<=log K the left side is <=log K. If x>=log K and
log K>=1, x exp(-x) is decreasing on that interval, so the left side
is at most log K. If log K<1, its global maximum on x>=0 is K/e<1,
since then K<e. These cases prove (4).
Set x=ct in (3), square, and apply (4):
  sqrt(t)T<=sqrt((17/16)L) H.                            (5)
This controls t arbitrarily large; replacing sqrt(t) by sqrt(log K)
without the exponential comparison would have been invalid.

## 2. Full weak-beta long-history ratio
For 0<beta<=1/2, delta>=1/2 and a<=1 give F>=a/2. S016 yields
  R>=2^-18 max(a,D,T)=2^-18 H.                           (6)
R004 and (5) show
  risk(ALG)<=3[6737+160sqrt((17/16)L)]H.
Since sqrt(17/16)<33/32, and L>=1,
  risk(ALG)<=3[6737+165]sqrt(L)H
            =20706sqrt(L)H<=21000sqrt(L)H.
Combine with (6):
  risk(ALG)<=21000*2^18 sqrt(L)R <=2^33 sqrt(L)R,          (7)
because 21000<2^15. This covers all long-history weak-beta parameters,
even when neither finite matched condition of R004 holds.

## 3. Cover every remaining parameter without changing the algorithm
Everything not covered by Section 2 lies in Omega_closed: beta=0 or 1;
beta>=1/2; or M<K^4,beta<=1/2. On that union S025 gives
risk(ALG)<=8000 r_closed. Every applicable benchmark scale has a lower
with constant at least 2^-18:
- g at beta=0: constant 2^-16;
- i at beta=1: constant 1/(32sqrt6)>2^-18;
- H_S on S019's strip: constant 2^-18;
- F on its applicable regimes: constant 1/180>2^-18.
Thus R>=2^-18 r_closed. Even if several certificates overlap, taking their
minimum does not weaken this lower; each already holds at that parameter.
It follows that risk(ALG)<=8000*2^18 R<=2^33 sqrt(L)R.
Sections 2–3 exhaust every K,M,beta and concern the identical fixed rule.
There is no beta-informed algorithm switch concealed in this proof.

For any admissible beta-blind A and any beta, its risk is at least the
infimum R over beta-informed algorithms. Strict positivity of R makes the
ratio at least one. Taking the supremum and then infimum proves the left
side of (2); ALG proves the right side.

## Limits
This does not show a necessary nonconstant adaptation penalty, exact
Gamma_all, or all-parameter minimax classification. The remaining critical
statistical gap can still permit constant adaptation, or a sharper oracle
comparison than supplied here. Constants are deliberately conservative.
The theorem does not compare original add-one to minimax in near-IID
regions where it can be inferior; it concerns the fixed guard selector.
No external literature-priority claim, formal verification, or restored
historical-source identity is asserted.
