编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R001: mixed-prefix occupation and blind transfer of a full-history certificate
Written anew, 2026-10-30. Not formal verification or recovery of missing S029/S031/S032 bytes.
The conversational account of those units motivated the reconstruction;
no assertion below takes that account as a mathematical premise.

## Exact experiment and recovered dependencies
K>=2, M>=1, n=M+1. Observe X_1,...,X_(M+2), and put
Y_j=(X_(j+1),X_(j+2)), j=0,...,M. A homogeneous legal second-order
table theta induces P((a,b),(b,c))=theta_ab(c). Let pi P=pi and
P^2(s,t)>=beta pi(t) for every pair s,t. Initial pair law mu is arbitrary.
For this theorem 0<beta<1; delta=1-beta, lambda=-log(delta).
All counts use departures 0,...,M-1. J is the full count of Y_M.
The original row add-one is q; its actual target is theta_(Y_M).
Loss is half L1, not squared TV, at the actual endpoint.

The same deterministic predictor ALG from recovered S024 uses only K,M,
history:
  g=min(1,sqrt(K^5/n)),
  pooled b=(output counts from X_3,...,X_(M+2)+1)/(M+K),
  rho(J)=min(g,64sqrt(K/(J+K))),
  ALG=b if TV(q,b)<=rho(J), otherwise q.
Thus ell_ALG<=ell_q+rho(J) on every history, and its inherited general
risk is <=min(1,49g). No latent label is an algorithm input.

Recovered complete scientific dependencies:
* S020, Sections 3–7, in the recovered first increment: general first-w
  charging; exact endpoint-aligned pair splitting; event-weighted
  ORIGINAL-stack inequality; success sum and its moderate-log bound.
* S024, Sections 1,4,5: the exact ALG and pathwise guard safety.
* General original add-one bound 48g is the inherited L1MAX interface
  explicitly stated by both sources. The residual table below is itself
  a legal second-order table, so that unconditional general interface
  applies to its ordinary trajectory.
No S026–S032 missing original text is used.

## Theorem
Let r=floor(M/2), q0=delta^r, qbar=delta^floor((M-1)/2), and set
  a=min(1,sqrt(K^3/n)),
  b_mix=beta K^2 [1+(K-1)qbar],
  A=delta^M min(1,48g+beta),
  B=min(q0,80sqrt(q0 b_mix [K+log(1/q0)])),
  q_j=beta delta^(j-1), L_j=2(r-j), j=1,...,r,
  S=sum_j q_j min(1,80sqrt(K^2 [K+log(1/q_j)]/(L_j+1))),
  u_g=min(1,48g), U_mix=min(u_g,A+B+S).
For every source and arbitrary initial law in D_2(beta),
  E ell_q <= U_mix,
  E ell_ALG <= min(1,49g,2A+(13/5)(B+S)) <= min(1,3 U_mix).
The same ALG is used for every beta. The public beta appears only in
the risk certificate. This is certificate adaptation, not a claim that
U_mix is the full minimax risk.

## 1. Legal one-symbol splitting
Let p(c)=sum_d pi(c,d). Stationarity of the shift gives equality of pi's
two single-coordinate marginals. Summing the full-state minorization in d:
  theta_ab(c)=sum_d theta_ab(c)theta_bc(d)>=beta p(c).
Consequently
  T_ab(c)=[theta_ab(c)-beta p(c)]/delta
is a nonnegative normalized legal second-order table for ALL rows,
including pairs outside the support of pi.

At each departure j, independently draw a Bernoulli(beta) symbol label.
On success emit an independent p symbol; otherwise emit according to T.
The marginal transition table is exactly theta, so the entire observed
symbol history, not only a pair skeleton, has its prescribed law.

Let G be no successful symbol label in the M departures. P(G)=delta^M;
conditional only on G, the full history is an ordinary T trajectory with
initial law mu. On each row TV(theta_s,T_s)<=beta, so the unconditional
general theorem applied to this T experiment yields
  E[ell_q 1_G]<=A.                                      (1)
This conditional application is legitimate because T is a legal table;
it does not apply the original-theta stack theorem conditionally.
Also E[rho(J)1_G]<=delta^M g<=A. The last inequality uses
g<=min(1,48g+beta), which follows from 0<g<=1.

## 2. The exact law after the last successful symbol label
Write Hplus=G^c. If the last success is at departure j (0<=j<M), let
l=M-1-j. Its probability is beta delta^l. Its prefix of j departures is
unrestricted and has the ordinary P law. If nu_j is the second-coordinate
marginal of mu P^j, the pair Y_(j+1) after that success has law nu_j tensor p.
The l remaining transitions have table T, independent of the previous
prefix conditional on this starting pair. This follows directly by
factoring prefix probabilities, the independent successful p draw, and
the subsequent failure labels. The prefix is not discarded as data.

For an ordinary T chain of length l with start distribution delta_b tensor p,
define
  f_l(b)=P(J_l^T<w), integer w>=1,
where J_l^T counts departures 0,...,l-1 of its actual terminal pair.
The suffix count is a subset of the original full count J. Therefore
  P(Hplus,J<w)
  <=sum_(l=0)^(M-1) beta delta^l sum_b nu_(M-1-l)(b) f_l(b). (2)

For each fixed b all f_l(b) can be computed from a single ordinary
infinite T path starting delta_b tensor p. On any such path the indicator
J_l^T<w flags only the first w occurrences of its current pair. Hence
  sum_(l=0)^(M-1) f_l(b)<=K^2 w.                          (3)
This statement needs neither recurrence nor stationarity nor positive rows.
In particular the l=0 term, whose count is zero, is retained.

## 3. Mixed-prefix improvement
Put Pi(s,t)=pi(t) and Q=(P^2-beta Pi)/delta. Q is stochastic,
pi Q=pi, and Q Pi=Pi Q=Pi. Thus for any integer j>=0, k=floor(j/2),
  mu P^j=(1-delta^k)pi+delta^k mu Q^k P^(j-2k).
After taking the second marginal,
  nu_j=(1-delta^k)p+delta^k xi_j
for a probability vector xi_j. No stationarity of p tensor p under T
is asserted or needed.

For j=M-1-l, k<=floor((M-1)/2), so
  delta^l(1-delta^k)<=1-qbar,
  delta^(l+k)<=qbar,
the second because l+k=floor((M-1+l)/2)>=floor((M-1)/2).
Since f_l is nonnegative, (2)–(3) imply
  P(Hplus,J<w)
  <= beta(1-qbar) sum_b p(b) sum_l f_l(b)
     + beta qbar sum_b sum_l f_l(b)
  <= beta K^2 [1+(K-1)qbar] w = b_mix w.                 (4)
The additional K is paid only on the nonstationary part of the prefix.
Replacing xi_j by an independent or fixed law would be unjustified; the
inequality sum_b xi_j(b)f_l(b)<=sum_b f_l(b) is what was used.

## 4. Joint construction with pair labels and original stacks
Use S020 Section 4's endpoint-aligned r pair blocks, with anchor M mod 2.
Let E0 denote no successful pair block, probability q0.
Let E_j denote first successful pair block j, with mass q_j. Conditional
only on E_j, the final length-L_j suffix is an ordinary stationary P path.
The unique legal midpoint is retained in each two-step block.

Construct pair labels and symbol labels jointly by taking their conditional
kernels given the FULL original history, and sampling their product
conditional on that history. This preserves both history-label marginals.
It does NOT assert unconditional independence of the labels. Attach these
finite joint labels to the original row-stack construction using S020
Section 5.1. The original stacks remain independent unconditionally;
no concentration inequality is conditioned on either system of labels.

Set E=E0 intersect Hplus. Equations (4) and P(E0)=q0 give
  P(E)<=q0, P(E,J<w)<=min(q0,b_mix w).                     (5)
The stationary count interface for each E_j gives
  P(E_j,J<w)<=q_j min(1,K^2 w/(L_j+1)).                   (6)
This includes L_j=0 by the trivial cap.

S020 Lemma 2 applied to (5), with c=b_mix/q0, gives
E[ell_q 1_E]<=B. Applied to (6) it gives the summands defining S.
G, E, E_1,...,E_r cover the augmented space: if not in a pair success,
a path is in E0 and is either in G or Hplus. G can overlap pair successes;
nonnegative losses allow this over-cover. Thus (1),(5),(6) prove
E ell_q<=A+B+S. Combining with the separate general risk bound proves
the first conclusion of the theorem.

## 5. Event-radius lemma and blind transfer
For any event F on any such augmentation, assume P(F)<=q and
P(F,J<w)<=min(q,bw) for all positive integers w, where q>0,b>0.
For 0<t<g, put x=4096K/t^2-K>0 and w=ceil(x). Since K>=1,
w<=4096K/t^2. Strict inequalities and integrality give exactly
  {rho(J)>t}={J<x}={J<w}.
Layer cake therefore proves
  E[rho(J)1_F]<=integral_0^g min(q,4096bK/t^2)dt
               <=min(qg,128sqrt(qbK)).                    (7)
To check the second bound, set z=64sqrt(bK/q).
If z>=g, the integral is qg<=qz<=2qz.
If z<g, it is 2qz-qz^2/g<=2qz.
If q=0 or b=0, the event is null (for b=0 use w=M+1);
its contribution is zero without evaluating logarithms.

The corresponding S020 event-loss certificate is
  D(q,b)=min(q,80sqrt(qb[K+log(1/q)])).
For 0<q<=1, (7) is <=(8/5)D(q,b):
if D=q use rho<=g<=1; otherwise use sqrt(K)<=sqrt(K+log(1/q)).
Apply this separately to E and every E_j. Together with the G bound,
the same covering argument gives
  E rho(J)<=A+(8/5)(B+S).
Pathwise guard safety then proves the displayed 2A+(13/5)(B+S)
bound, which is <=3(A+B+S).
When u_g=1 the loss cap is <=3u_g. When u_g<1, inherited general
ALG risk 49g=(49/48)u_g<=3u_g. Taking both bounds proves 3U_mix.
Every constant is uniform in K,M,beta. M=1 has r=0, no success
summands, q0=qbar=1; all formulas and the covering proof remain valid.
Neither beta endpoint requires division by zero: at beta=0 retain
general ALG 49g, and at beta=1 retain recovered IID ALG 858i.

## 6. What this does and does not settle
This reconstructs the reported mixed-prefix bridge without relying on
unavailable original proof bytes, and completes a broad guard-transfer
statement from recovered full interfaces. It does not claim a second
independent verification of historical S031, nor a first-ever result.
For any region where THIS explicit U_mix is later bounded by a matched
risk scale, the SAME ALG inherits that bound with factor 3. The comparison
is simultaneous over beta and requires no beta estimator.

At M=K^5, beta=log(K)/K^5, this certificate still contains a term of
order sqrt(log K)/K; the current proof cannot claim its removal.
The next substantive question is whether full prefix visits reduce the
mixed-label event risk below its present count-only certificate, or a
legal source forces the logarithmic gap. No statistical lower is inferred
from a large upper certificate.
