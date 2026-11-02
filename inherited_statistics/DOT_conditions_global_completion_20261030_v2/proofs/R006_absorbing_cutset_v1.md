编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R006 — Entire absorbing-stationary subclass: full-count cutset bound
2026-10-30. AUTHOR CANDIDATE ONLY; no self-acceptance or independent review.

## Useful result
For EVERY legal homogeneous second-order source with witness pi=delta_00,
arbitrary initial pair law, K>=2, M>=1, 0<beta<1, write delta=1-beta,
r=floor(M/2), q0=delta^r, n=M+1. For ANY event E on any augmentation
whose mass is at most q0, and every integer w>=1, the original full count
J of the actual endpoint satisfies

 P(E,J<w) <= min(q0, 2 delta^M + b w),
 b=8[K^2+q0 K^3]/(M+1).                                  (A)

In particular at M=K^5,beta=log(K)/K^5 this implies the proposed R002
occupation obligation (O), with a universal constant. Using the already
accepted original-stack reduction and grouped pair-success estimate,
unchanged full-history original add-one has risk <=min(1,8000/K)
throughout this ENTIRE absorbing-stationary subclass. The source table,
initialization, excursion law and stationary witness are not predictor
inputs. This is NOT a full D_2(beta) theorem and not a theorem of sharp
adaptation for ALG.

## Exact experiment, parameterization, and sources
Observe all X_1,...,X_(M+2), Y_j=(X_(j+1),X_(j+2)), 0<=j<=M.
J_s=sum_(j=0)^(M-1)1{Y_j=s}; J=J_(Y_M). The predictor is
(C_s(c)+1)/(J_s+K), evaluated at the actual Y_M, loss half L1 to theta_s.
The unknown fixed table has theta_00(0)=1. Put t_b=theta_(b,0)(0), t_0=1.
All-state minorization is exactly theta_ab(0)t_b>=beta for every a,b.
Consequently t_b>=beta and theta_ab(0)>=beta/t_b. NO equality or
restriction of the other symbol probabilities is imposed.

Direct exact bindings (all in this resume directory):
* R002_critical_prefix_obstruction_and_arrival.md SHA256
  87f86a5a7f4a291e50bb78a761b765f3e3f0289bec31c823e2ed30eb65a4bc98:
  Section 6's event trimming/original-stack reduction (7), and Section 2's
  restricted-star matching result for comparison only. The stale producer-status sentence is
  historical; scientific review status is recorded in EDITORIAL_NOTES.md.
* R004_grouped_regeneration_v1.md SHA256
  f83f79f77ca377cb8a8991eef6a39eed4f9dabb02d810078a83e437ddaa9c2b0:
  grouped pair-success estimate (GS), including all its event-law inputs.
* R001_mixed_prefix_and_blind_transfer.md SHA256
  e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1:
  Section 4's compatible labels and covering G,E,Eplus. No new claim about
  conditional stack independence is made here.
The count proof below is self-contained and needs none of those three
statistical results. No external mathematical theorem is invoked.

## 1. A general absorption point-mass lemma
Let Q be a substochastic kernel on D transient states, with missing row
mass sent to a cemetery. For first cemetery time tau and t>=1, set
f_t(x)=P_x(tau=t). For every 1<=l<=t, the Markov property gives
 f_t(x)=sum_y Q^(t-l)(x,y) f_l(y) <=sum_y f_l(y).
Average this inequality over l. Since sum_(l>=1)f_l(y)<=1,
 t f_t(x)<=sum_y sum_(l=1)^t f_l(y)<=D.
Thus P_mu(tau=t)<=D/t for any initial subprobability on transient states.
Initial mass already in the cemetery contributes only to tau=0.
No eventual-absorption assumption, reversibility or independence of
excursions is required.

## 2. A substochastic transform preserving arbitrary excursion geometry
Let B={00}, D=K^2-1. Define a potential on pairs by
 h(a,b)=1 if b!=0; h(a,0)=1-t_a if a!=0; h(00)=0.
For b!=0, direct calculation (including possible t_b=1) gives
 (Ph)(a,b)=1-theta_ab(0)t_b <=delta=delta h(a,b).
For a!=0,b=0, the only nonabsorbing successors are (0,c), c!=0,
so (Ph)(a,0)=1-t_a=h(a,0). This is where the exact general inequality
enters; it does not constrain the remaining transition geometry.

Restrict to S={s:h(s)>0}. Define e(s)=1 if the second coordinate is
nonzero, and e(s)=0 otherwise, and
 R(s,u)=P(s,u)h(u)/[h(s)delta^e(s)], s,u in S.
The preceding identities show its row sums are <=1. Add a cemetery to
make an ordinary Markov chain, and start it with subprobability
nu(s)=mu(s)h(s); send the leftover initial mass to the cemetery.
For any complete path s_0,...,s_M in S,
 nu(s_0) product R(s_i,s_(i+1))
 =mu(s_0) product P(s_i,s_(i+1)) h(s_M) delta^(-M+N0),
where N0 is the number of zero-ending pairs among s_0,...,s_(M-1).
This is an exact full-prefix likelihood identity, not iid sampling and
not conditioning an original row stack. A path with h(s_M)>0 cannot
have visited h=0 earlier: 00 is absorbing, and a nonzero pair (a,0)
with t_a=1 goes to 00 at the next step.
Because adjacent zero-ending states would produce 00, every surviving
R path has 0<=N0<=L=ceil(M/2). The cutset C={s in S:second(s)=0}
has at most K-1 states.

## 3. Full-prefix weighted cutset charging
Let F={J<w} on a surviving length-M R path, with J computed from ALL
M original departures. For c in C and l>=0, define b_l(c) as the
R-probability of surviving to l and having fewer than w previous visits
to its actual endpoint during departures 0,...,l-1.
For any one R trajectory (including killed paths), first-w charging gives
 sum_(l=0)^M 1{alive at l, J_l<w} <=D w.
Thus sum_(l=0)^M b_l(c)<=D w for each start c.
At any i<M, full-count domination by the suffix count and the Markov
property imply
 P_R(F,alive at M,Y_i=c)<=P_R(Y_i=c)b_(M-i)(c)<=b_(M-i)(c).
Summing i and c proves, for the subprobability initial law nu as well,
 E_R[N0 1_F;alive at M] <= |C| D w <=K^3 w.                (B)
All prefix visits remain in F; only a valid one-sided domination is used.

Convexity of x->delta^(-x) on [0,L] yields the chord bound
 delta^(-x)<=1+[delta^(-L)-1]x/L.
Apply the exact likelihood identity and h(Y_M)>=1/2 to obtain
 P_original(J<w,h(Y_M)>=1/2)
 <=2delta^M E_R[delta^(-N0)1_F;alive at M]
 <=2delta^M+2[delta^(M-L)-delta^M]K^3 w/L
 <=2delta^M+4q0 K^3 w/M.                                (C)
This bounds all nonzero-ending endpoints and also zero-ending endpoints
with t_a<=1/2. The possible transformed cemetery is not counted among
D states or among endpoint events.

## 4. Dangerous zero endpoints and recent absorption
If Y_M=(a,0)!=00 and t_a>1/2, then with conditional probability t_a the
original chain first enters 00 at M+1. Hence, by Section 1,
 P(Y_M dangerous)<=2P(tau_00=M+1)<=2D/(M+1).              (D)
This includes h(Y_M)=0. No upper bound beta on the absorption hazard is
assumed; hazards may be arbitrarily large.
If Y_M=00 and tau_00=t in {0,...,M}, then J=M-t exactly. For w<=M/2,
J<w forces t in {M-w+1,...,M}, excluding t=0. Section 1 gives
 P(Y_M=00,J<w)<=sum_(t=M-w+1)^M D/t<=2D w/M.             (E)
Combining (C)--(E), using w>=1, proves for w<=M/2,
 P(J<w)<=2delta^M+4[q0 K^3+K^2]w/M.
Since (M+1)/M<=2, this implies the uncapped RHS of (A). Intersect with
any E of mass<=q0 to obtain its cap. If w>M/2, the term
8q0K^3w/(M+1) alone is >=q0 for every M>=1,K>=2, so (A) follows simply
from P(E)<=q0. This also covers M=1. These cases prove (A) in full.

## 5. Critical consequence for the ORIGINAL prediction rule
Now M=K^5, beta=log(K)/K^5, K>=2. Then beta<1/16, delta>15/16,
 delta^M<=1/K, q0<=2/sqrt(K),
 b<=24/K^(5/2), K+log(1/q0)<=2K.
For the last inequality, -log(delta)<=beta/delta gives
log(1/q0)<=log(K)/(2delta)<=8log(K)/15<=K.
Also K^2/(M+1)<=K^-3<=beta K^2/log(2), so (A) implies the proposed (O)
with a universal constant on this ray, without any label-coupling choice.

Take exactly the compatible pair/symbol augmentation in R001, so
P(E)<=q0. R002 reduction (7), with epsilon=2delta^M and coefficient b,
gives
 E[ell 1_E]<=2/K+80sqrt(q0 b[K+log(1/q0)])<=802/K,
since q0 b[K+log(1/q0)]<=96/K^2 and sqrt(96)<10.
The no-symbol-success event G has mass delta^M, so contributes <=1/K
by the loss cap (no residual-stack argument is needed here).
The pair-success union contributes <=6400a<=6400/K by R004 (GS).
Their cover therefore gives risk<=min(1,7203/K)<=min(1,8000/K).
The estimator is the same original add-one for every source and beta.

R002's legal star subfamily lies inside this absorbing subclass and has
critical minimax lower Omega(1/K). Thus the ENTIRE absorbing subclass's
critical minimax and original worst risk are Theta(1/K) asymptotically,
using that already accepted lower. This does not export the upper to
other stationary laws. No assertion that the original estimator must be
given the witness 00 is needed: it uses no witness at all.

## 6. Failed avenues, limits, and diagnostic role
* Directly declaring a conditional surviving excursion sample iid is
  invalid. The transform above is a complete-path likelihood change and
  is used only with Markov suffix domination and deterministic charging.
* A fixed hard lower threshold on N0 discards too much probability or
  leaves a logarithmic factor: N0 about M/log(K) only suppresses the
  nozero term by a constant. The convex chord uses the whole weighted
  distribution and (B), rather than making a typical-count assumption.
* Dividing by h at all endpoints fails when t_a approaches 1. This is a
  real singularity, not removable by a positive-row assumption. Section
  4 handles those endpoints through a separate exact absorption event.
* Initially one might assume late absorption has hazard <=beta, as on
  the restricted star family. That is false for arbitrary legal rows;
  the D/t bound replaces it with no hazard restriction.
* General nonabsorbing stationary support has no established analogue
  of this h-transform/cutset. The present proof does not claim (O) there.
* Finite enumeration checks the likelihood, charging and endpoint
  partitions, not large-K sharp constants or formal correctness.

Artifacts: R006_check.py and R006_check_result.json. The independent
scientific review is included separately.
