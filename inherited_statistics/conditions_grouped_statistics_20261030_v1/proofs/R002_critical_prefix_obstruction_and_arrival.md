编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R002 — Full-prefix evidence, coupling obstruction, and arrival rigidity
Written anew 2026-10-30.
No missing S026–S032 text is reconstructed or used.

## Useful results and limits
1. A history-dependent coupling of the two canonical label systems cannot
   shrink the exceptional mass in R001 below its existing order: on the
   lawful S015 star family, every such coupling has P(E)/q0 -> 1 at
   M=K^5, beta=log(K)/K^5.
2. On the SAME family the unchanged full-history original add-one has
   risk O(1/K), proved below including the absorption tail. Its full count
   on the active exceptional event is exactly Bin(floor(M/(2m)),1/m^2).
   Thus this family cannot supply the desired stronger sqrt(log K)/K
   lower. This is a family-only statistical theorem, NOT a full-class upper.
3. For every admitted source, an exact arrival/uncertainty tradeoff and
   unconditional full-prefix arrival martingale bound are proved below.
   A refresh cannot uniquely introduce a row far from its stationary
   conditional proxy: residual arrivals into that row are quantitatively
   forced. The local inequality is sharp already on a two-letter source.
4. The remaining full-class occupation obligation is stated explicitly,
   with a proved reduction showing it would close the critical risk gap.
   That occupation obligation remains UNPROVED. No rate is inferred from
   its plausibility or from the family computation.

## Experiment and source bindings
K>=2, M>=1, 0<beta<1, delta=1-beta. The homogeneous legal table theta
induces P((a,b),(b,c))=theta_ab(c), with an arbitrary initial pair mu.
There exists pi P=pi with P^2(s,t)>=beta pi(t) for ALL states. Observe all
X_1,...,X_(M+2), let Y_j=(X_(j+1),X_(j+2)), j=0,...,M. Counts J_s use
all departures 0,...,M-1; J=J_(Y_M). Prediction q is original add-one
(C_s(c)+1)/(J_s+K) at the ACTUAL Y_M. Loss ell is half L1 to theta_(Y_M).
All labels below are hidden analysis devices, never predictor inputs.

Read/bound sources (frozen identities; public locators in SOURCE_INDEX.json):
* S015 frozen input (mapped, not byte-identical, to the inherited public copy), SHA256
  f8ad4cf098874285431be5a41087958fb89f156144da589de83b5fa1c3b00289.
  Sections 3 units 001–005 supply the fully specified legal star table,
  every-residue initialization, all-state membership, full-history product
  law, and exact vulnerable count; unit 006 supplies its statistical lower.
  These are inherited science, not new results in R002.
* proofs/R001_mixed_prefix_and_blind_transfer.md,
  SHA256 e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1.
  Candidate context only: definitions of symbol labels, endpoint-aligned
  pair labels and E. Our coupling obstruction is independently proved.
* Inherited S020 complete proof (SOURCE_INDEX.json), SHA256
  a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb.
  Its event-weighted original-stack Lemma 2 is used only in Section 6.
No conditional original-stack independence is invoked.

## 1. Label-coupling obstruction on the actual star family
Use S015's exact construction, K>=13, m=floor((K-1)/4), L=2m,
q=floor(M/L), d=M-qL, k=(2-d) mod L. The disjoint nonzero groups C,U,V,W
have m symbols each, with central 0. Its phase sets are
D_0={(1,0)}, D_1={0}xU, D_2=UxV, D_3=VxW, D_4=Wx{0}, and retained
star phases D_t={(c_t,c_(t+1))}, 5<=t<L, where c_(2i)=i+1,
c_(2i+1)=0. The base table Q traverses the replacement
(1,0)->(0,A)->(A,B)->(B,Z)->(Z,0)->(0,c_6), then the retained star.
A,B are uniform on U,V; Z has the S015 q_sigma row supported on W.
Elsewhere Q=delta_0. Actual rows are theta=beta delta_0+delta Q.
The full exact table and six initial cases are the bound S015 source.

Let V={0,1,2,4} union {6,8,...,L-2} be its vulnerable phases; |V|=m+1.
Let H count scheduled vulnerable departures and S=M-H count safe ones.
Then H=q(m+1)+r_M and |H-M(m+1)/(2m)|<=L. Let A be the OBSERVABLE
base-support event: Y_j is in D_((k+j) mod L) for all j=0,...,M.
S015 proves A equals failure of all H vulnerable symbol-refresh coins,
P(A)=delta^H, and conditional on A the entire history has the base law.
Safe-phase symbol refreshes are independent Bernoulli(beta) and leave
all observed symbols unchanged. None of the pairs on A is 00.

Here pi=delta_00. In any endpoint-aligned two-step pair splitting,
a successful pair label has endpoint 00. Consequently on every positive
probability history in A ALL pair labels must fail. This is a support
statement about the history/pair-label marginal, hence remains true under
EVERY joint coupling with the canonical symbol-label marginal.
Let E0 be no pair refresh, Hplus at least one symbol refresh, E=E0 cap Hplus.
Then, under every such coupling,

    P(A cap E)=delta^H(1-delta^S).                         (1)

In fact, conditional on A cap E, the entire observed history STILL has
the base law: E0 is forced and Hplus is merely at least one of the S
independent safe coins succeeding. This proof does not require conditional
independence between the TWO label systems.

At M=K^5,beta=log(K)/K^5, H=M/2+M/(2m)+O(L), S=M/2-M/(2m)+O(L).
The elementary bound 0<=-log(1-beta)-beta<=beta^2/(2delta) gives
 delta^H/K^-1/2 ->1, delta^S/K^-1/2 ->1, q0/K^-1/2 ->1,
where q0=delta^floor(M/2). Thus (1)/q0 ->1. Since P(E)<=q0 for every
coupling, P(E)/q0 ->1. In particular no choice of coupling can provide a
uniform o(q0) event-mass bound. This is NOT a risk lower of order q0.

## 2. Full-prefix count and finite original-add-one family upper
On A, the full history is exactly q IID training triples
(A_i,B_i,Z_i), law m^-2 q_sigma(z|a,b), and its independent actual endpoint
T=(A_(q+1),B_(q+1)) uniform on UxV. This is S015's full-data identity,
not an assumption about arbitrary selected rows. Therefore, conditional
on T=s, J is Bin(q,1/m^2), and conditional on J=j the j labels for s are
IID q_sigma(.|s). This remains true conditional on A cap E by Section 1.
All q possible visits occur in the FULL original history.

For j>=1, Cauchy-Schwarz and coordinate variances give expected empirical
TV to q_sigma <=(1/2)sqrt(m/j). Original K-letter add-one differs from the
empirical vector by at most K/(j+K). Its target theta_s differs from
q_sigma by beta. At j=0 use loss<=1. Both cases are bounded by
 beta+sqrt(m/(j+1))+K/(j+1), capped above by 1 after averaging.
For B~Bin(q,p), direct binomial integration gives
 E[1/(B+1)]=(1-(1-p)^(q+1))/((q+1)p)<=1/((q+1)p).
Cauchy-Schwarz gives E[1/sqrt(B+1)]<=sqrt(E[1/(B+1)]). Thus set

    D=min(1,beta+sqrt(m^3/(q+1))+K*m^2/(q+1)).

For every sign vector, including both amplitude branches,

    E[ell 1_A] <= delta^H D,
    E[ell 1_(A cap E)] <= delta^H(1-delta^S)D.              (2)

To cover the rest of the ORIGINAL rule's risk, let tau be the first
vulnerable refresh. Its probability at any specified departure is <=beta.
The pair at time tau+1 is default; by time tau+2 it is 00 forever.
If tau=M-1 its terminal target is already delta_0, with loss<=1.
Otherwise, if the endpoint is 00 it has at least (M-tau-2)_+ previous
00 departures, all with output 0. (There were no 00 pairs before failure.)
The add-one loss to delta_0 is (K-1)/(J+K), so it is at most
K/((M-tau-2)_++K). Consequently, for every M>=1,

 E[ell 1_(A complement)]
 <= min(1-delta^H, beta[2+K log(1+M/K)]).                  (3)

For M>=2 this follows from the two terms with zero positive part and
sum_(l=1)^(M-2) K/(K+l)<=K integral_0^(M-2) dx/(K+x).
For M=1 the single failure mass is <=beta, so (3) is still valid.
Combining (2)–(3) is a finite all-horizon upper for unchanged original
add-one on this star family. It makes no full-class claim.

At the critical ray, q is asymptotic to 2K^4, m asymptotic to K/4;
D=O(K^-1/2), delta^H=Theta(K^-1/2), and the term in (3) is
O((log K)^2/K^4). Thus original risk is O(1/K).
The existing S015 lower is delta^(H+1)alpha/8, with
alpha=min(1/2,sqrt(m^3/(q+1))/8)=Theta(K^-1/2), hence Omega(1/K).
This proves the RESTRICTED family's minimax risk and original worst risk
are Theta(1/K) on this ray. It is not a new full-class lower.
Moreover the S015 testing proof can be restricted to A cap E, because
safe labels are independent of the entire base experiment. Its prior
average event-risk lower is delta^(H+1)(1-delta^S)alpha/8. Therefore the
large unavoidable event E really has risk order 1/K on these sources,
not order q0 and not the sqrt(log K)/K certificate.

### 2.1 Quantified full-prefix versus last-refresh suffix count
On A cap E let tau be the last successful symbol label, necessarily at a
safe phase, and let N=M-1-tau be the number of departures AFTER that
refresh. The suffix starts at Y_(tau+1); denote its terminal-row count by
J_suf. The largest cyclic gap between safe phases is four (safe phases
are 3,5,7,...,L-1), including the m=3 wrap. Every block of four consecutive
departures therefore contains a safe phase. Independence of safe coins
from the base experiment gives, for integer l>=1,

 P(N>=l | A cap E)<=delta^floor(l/4)/(1-delta^S).

Hence E[N | A cap E]<=4/[beta(1-delta^S)]. For any fixed tau there are
at most N/L+1 training UV departures in that suffix. Each has probability
1/m^2 of equalling the independent actual terminal UV pair, by the full
product identity. Thus, whenever S>0,

 E[J | A cap E]=q/m^2,
 E[J_suf | A cap E]<= [4/(beta L(1-delta^S))+1]/m^2.       (8)

At the critical ray q tends to infinity and 1-delta^S tends to one,
so the ratio of the displayed full mean to the suffix upper bound is
asymptotic to (log K)/4. In particular at least a logarithmic factor in
available mean count is lost by keeping only the last-refresh suffix.
This mean-count statement alone is not a risk inequality; the actual
risk conclusion used the full binomial law in Section 2, not Jensen in
the wrong direction. If S=0 the event is null and no conditional ratio
is defined. This suffix diagnostic does not modify the predictor.

## 3. General sharp arrival/uncertainty rigidity
Define p(c)=sum_d pi(c,d). Its two coordinate marginals agree by stationarity.
For p(c)>0 set R_c(d)=pi(c,d)/p(c). For a terminal row (b,c), define
v_bc=TV(theta_bc,R_c), and m_bc=min_a theta_ab(c).
The exact legal-product minorization gives, for EVERY a,d,

    theta_ab(c) theta_bc(d) >= beta p(c) R_c(d).

Summing d gives m_bc>=beta p(c)>0. Choosing a attaining the minimum,
 theta_bc >= kappa_bc R_c coordinatewise, kappa_bc=beta p(c)/m_bc.
For kappa<1 the residual normalized row is a probability, so
v_bc<=1-kappa; if kappa=1 the rows coincide. In particular v_bc<1 and

 theta_ab(c)>=m_bc>=beta p(c)/(1-v_bc),
 T_ab(c) >= beta p(c) v_bc/[delta(1-v_bc)]  for EVERY a,     (4)

where T=(theta-beta p)/delta is the lawful symbol-residual table.
Thus if residual incoming mass T_ab(c) is zero for even ONE predecessor
a, then v_bc=0. More generally a refresh arrival into a row with
v_bc>=epsilon>0 is accompanied at EVERY predecessor ending in b by
residual arrival probability at least beta p(c)epsilon/[delta(1-epsilon)].
No observation or estimator of the hidden R_c is asserted.
When p(c)=0, this argument supplies no positive constraint; such symbols
cannot be emitted by a successful symbol label. Rows with p(c)=0 are
not deleted from the source or observation experiment.

Sharpness: K=2, pi=delta_00, choose beta<=h<=1, and set
 theta_00(0)=1, theta_10(0)=h,
 theta_01(0)=theta_11(0)=beta/h,
with complementary mass at symbol 1. Every row is normalized, and
P^2(s,00) equals respectively 1,h,beta,beta, all >=beta.
For (b,c)=(1,0), R_0=delta_0, v_10=1-h, m_10=beta/h;
both inequalities in (4) are equalities for a=0 and a=1.
So the local reciprocal tradeoff cannot be improved uniformly.

## 4. Unconditional FULL-prefix arrival bound
This lemma is independent of stationarity, labels, and stack conditioning.
For any fixed b,c let m=min_a theta_ab(c). Across t=0,...,M-1 put
 N_b=sum_t 1{second(Y_t)=b},
 A_bc=sum_t 1{second(Y_t)=b, X_(t+3)=c}.
These are actual original full-prefix counts. Let J_bc count departures
of pair (b,c). Shift legality gives exactly
 A_bc-J_bc=1{Y_M=(b,c)}-1{Y_0=(b,c)}, hence J_bc>=A_bc-1.

For u>0, conditional on the past, an eligible arrival has probability
at least m. Therefore
 exp[-u A_bc + m(1-exp(-u))N_b]
is the terminal value of a nonnegative supermartingale starting at 1:
at an eligible step its conditional multiplier is
 exp(m a)(1-theta_ab(c)a)<=exp(m a)(1-m a)<=1,
where a=1-exp(-u). At ineligible steps it is 1.
Take u=log 2 and apply Markov's inequality. For every real n>=0,

 P(A_bc<=m N_b/2, N_b>=n) <= exp[-m n(1-log 2)/2]
                           <= exp(-m n/8).              (5)

Consequently
 P(J_bc+1<=m n/2, N_b>=n)<=exp(-m n/8).                  (6)
The first event in (6) implies A_bc<=m n/2<=m N_b/2.
The numerical constant uses log 2<=3/4, proved e.g. by integrating
1/x<=3/2-x/2 on [1,2]. For m=0 the trivial bound 1 is retained.
A union bound gives simultaneous validity over all K^2 fixed rows;
selection of the actual endpoint AFTER observing the history needs this
union (or a separate sharper argument), not a conditional iid assertion.
Combining (4) with (5)–(6) quantifies the full-prefix visits that any
putative 'only refresh accesses the hard row' counterexample must pay.
This does not bound N_b for the selected endpoint jointly with p(c),
v_bc and E, and therefore does not close the global risk theorem.

## 5. What fails, what is new, and what remains
* Choosing an optimal conditional coupling is legitimate, but Section 1
  disproves the proposed mass-only o(q0) improvement. The obstruction is
  coupling-invariant on an observable support, not simulation evidence.
* S015 already established survival and a constant-predictor family upper.
  R002 does not rebrand these as new. New here are the coupling-invariant
  joint event identity, the full original-add-one family upper including
  its failure tail, and the general sharp arrival rigidity/reduction.
* Merely replacing the last-refresh suffix by the full prefix does not
  make the arbitrary source conditional stacks IID. Section 2's binomial
  calculation is restricted to a family with an exact full-data product
  law. It cannot be exported to all theta.
* Conditioning on a typical number of symbol refreshes was considered
  but NOT used: a lower-binomial-tail error can be much larger than 1/K
  on the critical ray, and labels are dependent on the rare event E.
* A constructed source where a refresh alone moves to a wholly new hard
  component is blocked by (4): if residual incoming mass vanishes, the
  arrived row equals R_c. Nevertheless R_c is hidden and might itself be
  hard to estimate. Replacing theta_bc by R_c in an algorithm is NOT an
  authorized oracle step or a proved statistical estimate.
* Local inequality (4) is sharp. Further improvement must use temporal
  occupation, learnability of R_c, or another global constraint, not a
  stronger unsupported rowwise inequality.

### The unsupported propagation step, explicitly
Equation (4) controls the row immediately AFTER a successful symbol
refresh. It does not control an arbitrary later T row. This gap occurs
inside the lawful star witness: a safe refresh at phase 3 emits 0 and
lands at (w,0), where p(0)=1 and (4) applies. A subsequent residual step
emits c_6 != 0 and lands at (0,c_6), whose second-coordinate stationary
mass is zero. Eventually the process reaches a hard UV row; both its
coordinates have zero stationary mass. The inequality (4) gives no
constraint there. Thus even proving abundant pre-refresh visits to
(w,0) does not by itself prove abundant visits to the later actual UV
row. A full-class argument must control how those visits propagate
through the homogeneous residual dynamics, WITHOUT paying one fresh
K-dimensional start penalty for each possible refresh location. Neither
(4) nor the martingale lemma supplies this propagation theorem.

## 6. A precise remaining occupation obligation and its consequence
The following is a proposed FULL-CLASS obligation, not a theorem:
for some universal C and a compatible joint label augmentation, for all
integer w>=1,

 P(E,J<w) <= min(q0, C delta^M
               + C[beta K^2 + q0 K^3/(M+1)] w).           (O)

It deliberately retains an additive delta^M exception. No claim is made
that the exceptional event is the original no-symbol-refresh event.
The bound must use the full J, the actual endpoint, and arbitrary starts.

Here is a proved reduction, so the missing statement is sharply localized.
If an event F has mass<=q and
 P(F,J<w)<=min(q,epsilon+b w) for every integer w>=1,
remove up to epsilon probability from F in increasing order of J, using
an independent tie-breaking uniform variable if necessary. Call the
remaining event F'. For every threshold w its mass below w is exactly
max(0,P(F,J<w)-min(epsilon,P(F))), hence <=b w. Also P(F')<=q.
The removed loss contribution is at most epsilon. S020 Lemma 2, on this
finite/randomized augmentation (one finite discrete coin suffices for the
single boundary count), then yields

 E[ell 1_F] <= min(q, epsilon+80sqrt(q b[K+log(1/q)])).      (7)

This preserves the ORIGINAL unconditional stack marginal; no independent
stack property is asserted conditional on F or F'. Cases epsilon>=P(F)
are trivial. The fractional coin need not have rational probability.

Apply (7) to (O). At M=K^5,beta=log(K)/K^5,
q0=Theta(K^-1/2), epsilon=O(K^-1),
b=O(log(K)/K^3+K^-5/2)=O(K^-5/2), and log(1/q0)=O(log K).
Thus E[ell 1_E]=O(K^-1). Together with the already supplied original
no-symbol-refresh bound and stationary pair-success sum, this would close
the critical full-class original upper at O(1/K). This is a CONDITIONAL
consequence, not a proof of (O). The current rigorous evidence establishes
(O)'s needed scale on the star family's active event, but not generally.
The concrete open step is to upgrade arrival rigidity (4) and actual
prefix bound (6) into (O), paying off-support symbols and selected N_b,
or exhibit a lawful source violating (O). A violation would be a COUNT
obstruction, not automatically a statistical lower.

## Diagnostic execution record
R002_check.py constructs every row of the m=3 star family and checks
all-state minorization; enumerates all complete histories for K=13,
M=1,...,14 and beta in {0.02,0.2,0.7}; verifies exact active-event masses,
conditional binomial counts, original-add-one risks and finite upper
bounds; and checks the sharp two-letter examples. All 42 finite history
cases passed on 2026-10-30. It also records stable scalar critical-ray
values up to K=10^6. Output: R002_check_result.json. These floating-point
checks are diagnostics only, not proof, acceptance, or formal verification.
