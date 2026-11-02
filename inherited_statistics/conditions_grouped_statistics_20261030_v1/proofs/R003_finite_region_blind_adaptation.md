编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R003: finite-region consequence of R001 for the SAME beta-blind ALG
2026-10-30. Newly written corollary.
This is a transparent reconstruction of a historically reported matched
region and completion of its blind-algorithm implication; no novelty claim,
no recovery of missing historical proof bytes, no new difficult source.

## Statement
Use R001's exact experiment, original full row rule, and fixed ALG. Put
n=M+1, delta=1-beta, r=floor(M/2), lambda=-log(delta),
a=min(1,sqrt(K^3/n)), g=min(1,sqrt(K^5/n)),
hstar=min(1,sqrt(K^4/n)), D=delta^n g, T=delta^(M/2)hstar.
Assume
  K>=2 integer, M>=K^4 integer, 0<beta<=1/2,
  log(1/beta)<=K, r lambda<=K.                           (D2)
Put t=beta n, d=min(K,n/K^4), Z=max(a,D). Define V as D2 with
at least one of
  t<=d delta^(M+2),                                     (Vlo)
  t K delta^M<=1.                                       (Vhi)
Then for the full class and the SAME fixed ALG of R001,
  2^-18 Z <= R <= R^+ <= min(1,2675 Z),
  R <= risk(ALG) <= min(1,8025 Z).
Moreover on D2, without either additional V condition,
  R^+ <= min(1,2419a+96D+160sqrt(t)T),
  risk(ALG) <= min(1,7257a+288D+480sqrt(t)T).
These are finite-domain statements with absolute constants, not all-beta
or all-history classification.

The lower is inherited from recovered full S016:
  R>=2^-17 max(F,D,T), F=max(i,min(delta,a)),
  i=min(1,sqrt(K/n)).
No lower is obtained by taking square roots of squared-TV bounds.
All upper algebra follows below from R001 and recovered S020 Section 7.

## 1. Caps and elementary finite comparisons
M>=K^4>=16 implies n>K^4, hence
  a=K^(3/2)/sqrt(n), hstar=K^2/sqrt(n).
The cap on g is retained. Since 0<beta<=1/2, delta>=1/2.
Set q0=delta^r and qbar=delta^floor((M-1)/2); then
  q0 qbar=delta^(M-1)                                   (1)
for both parities, with no approximation.

Also n/r<=9/4:
if M=2r, r>=8 and n/r=2+1/r<=17/8;
if M=2r+1, M>=17, r>=8 and n/r=2+2/r<=9/4.
Consequently, using 1-beta<=exp(-beta) and max_(x>=0) x exp(-x)=1/e,
  t q0=beta n delta^r<=n/(e r)<=9/(4e)<1.                (2)
The strict last step follows, for example, from e>=1+1+1/2=5/2>9/4.

## 2. Bound the three R001 terms separately
Its success sum S is exactly the end-aligned sum of S020 Section 7.
D2 includes that proof's D1 conditions, so
  S<=2304a.                                             (3)
This use has no upper restriction on M; S020 proves the early/late
geometric calculation explicitly outside the old S019 strip.

The R001 no-symbol-refresh term obeys
  A=delta^M min(1,48g+beta)
   <=48 delta^M g+beta delta^M<=96D+a.                   (4)
Here delta^M g=D/delta<=2D, and
beta delta^M<=beta exp(-beta M)<=1/(eM)<=a.
For the final comparison, a^2=K^3/n>=8/(M+1)>=1/M^2
since 8M^2>=M+1 for every M>=1.

Using K+r lambda<=2K and 1+(K-1)qbar<=1+K qbar,
the R001 B term, ignoring only its helpful cap, satisfies
  B<=80sqrt(2) K^(3/2) sqrt(beta q0)
     +80sqrt(2) K^2 sqrt(beta q0 qbar).
By (2) the first summand is at most 80sqrt(2)a<114a.
By (1) and delta>=1/2 the second is at most
  160 K^2 sqrt(beta) delta^(M/2)=160sqrt(t)T.
Thus
  B<=114a+160sqrt(t)T.                                  (5)
Combining (3)–(5) gives
  A+B+S<=2419a+96D+160sqrt(t)T.                          (6)
R001 proves R^+<=min(1,A+B+S) and risk(ALG)<=min(1,3(A+B+S)).
Equation (6) gives both asserted D2 bounds. No assumption that U_mix is
a necessary risk certificate is used.

## 3. Exact finite matched region V
Because n>K^4, the g/hstar ratio has exactly two cases:
  if n<=K^5, g=1 and (g/hstar)^2=n/K^4;
  if n>=K^5, g=K^(5/2)/sqrt(n) and (g/hstar)^2=K.
At equality the formulas agree. Hence (g/hstar)^2=d, with
  (sqrt(t)T/D)^2=t delta^(-M-2)/d.                       (7)
Vlo therefore implies sqrt(t)T<=D. Independently,
  (sqrt(t)T/a)^2=t K delta^M,                            (8)
so Vhi implies sqrt(t)T<=a. In their union sqrt(t)T<=Z.
Equation (6) then gives (2419+96+160)Z=2675Z; R001 gives
the SAME ALG the bound 3*2675Z=8025Z.

For the lower, delta>=1/2 and 0<a<=1 give
  F>=min(delta,a)>=a/2.
The exact recovered S016 lower thus gives
  R>=2^-17 max(F,D,T)>=2^-18 max(a,D)=2^-18 Z.
The minimax lower also lower-bounds each fixed algorithm's worst risk.
The two-sided comparisons are consequently genuine matching on V,
with all initial laws and complete visible histories retained.

## 4. Adaptation quantifiers and boundary
The one algorithm was fixed by K,M and the history BEFORE beta is chosen.
Equations (7)–(8) are analysis conditions, not algorithmic tests. Taking
an overlap minimum with any other valid bound on this SAME algorithm is
legitimate without choosing a different predictor. In particular the
recovered S024/S025 guarantees remain unchanged. This corollary itself
uses only R001 and the recovered S020/S016 interfaces; it does not
re-certify S025's full proof or replace its historical review.

V does not cover all of D2. At the important M=K^5,
beta=log(K)/K^5 transition, the mixed certificate can still carry
sqrt(log K)/K. This corollary supplies neither a necessary logarithmic
adaptation penalty nor a stronger statistical lower there.
No extrapolation beyond D2, no beta=1 division, no stationarity assumption
on mu, no extra validation data and no new source family is introduced.
