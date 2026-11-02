编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R011: all-parameter conditional prediction rates and constant beta adaptation
2026-10-30. Author candidate pending independent review.
This is a standard assembly and finite-domain simplification of the new
tilted-label count theorem, the grouped-success theorem, a reconstructed
original-IID interface, and the recovered lower/selector interfaces.
No literature-priority or formal-verification claim.

## 1. Exact theorem
Fix any integers K>=2,M>=1 and beta in [0,1]. A source has an unknown
fixed homogeneous second-order table theta, with legal shift kernel
P((a,b),(b,c))=theta_ab(c), and an arbitrary unknown initial pair law mu.
The class D2(beta) requires an existential stationary pi such that
pi P=pi and P²(s,t)>=beta*pi(t) for EVERY pair s,t, including off support.
Observe every symbol X_1,...,X_(M+2). Let Y_j=(X_(j+1),X_(j+2));
only departures j=0,...,M-1 are counted. Target is the actual theta_(Y_M)
for the unobserved next symbol. Loss is unconditional expected half-L1 TV.

R is the common minimax risk allowing public K,M,beta before taking the
source supremum; theta,mu,pi and future symbols remain unknown.
R^+ is the worst risk of ORIGINAL full-history K-letter add-one at Y_M.

Define n=M+1, delta=1-beta and
  a=min(1,sqrt(K³/n)), g=min(1,sqrt(K⁵/n)),
  i=min(1,sqrt(K/n)), hstar=min(1,sqrt(K⁴/n)),
  F=max(i,min(delta,a)),
  D=delta^n g, T=delta^(M/2) hstar,
  L=max(F,D,T), H=max(a,D,T).
At beta=1 the positive powers of zero in D,T are zero. No 0^0 occurs.
Then
  2^-17 L <= R <= min(1,2^14 L),                         (COMMON)
  2^-24 H <= R^+ <= min(1,2^13 H).                       (ORIGINAL)

The SAME deterministic predictor ALG for ALL beta uses only K,M,history:
  J=sum_(j<M)1{Y_j=Y_M},
  q(c)=(sum_(j<M)1{Y_j=Y_M,X_(j+3)=c}+1)/(J+K),
  b(c)=(sum_(j=3)^(M+2)1{X_j=c}+1)/(M+K),
  rho(J)=min(g,64sqrt(K/(J+K))),
  ALG=b if TV(q,b)<=rho(J), otherwise q (ties select b).
Its worst class risk obeys
  risk(ALG)<=min(1,2^16 L)                              (BLIND)
simultaneously for every K,M,beta. In particular
  1<=Gamma_all(K,M)<=2^33,                              (ADAPT)
where Gamma_all is the infimum over ONE beta-blind predictor of
sup_(beta in [0,1]) risk(A;beta)/R(K,M,beta).
Thus no growing adaptation penalty is necessary in the specified full
parameter domain. This is order-optimal adaptation, not the optimal
numerical constant.

The original-rule relative inefficiency is also characterized:
  2^-38 H/L <= R^+/R <=2^30 H/L.                         (SEPARATION)
All scales are positive for finite K,M. The capped formulas are genuine
uniform finite-parameter bounds, not fixed-ray extrapolations.

## 2. Exact dependencies and new work
- Recovered S016: COMMON lower 2^-17 max(F,D,T), for the complete
  experiment and all beta endpoints. Its lower sources retain all data.
- Recovered S019: on M<=K⁴, beta<=1/2, original upper128 H_S and
  common lower2^-18 H_S, H_S=max(a,delta^(M/2)).
- Recovered S024/S025: this EXACT ALG, general49g, strip1472 H_S,
  and strong-beta8000F (also near-IID/other closed guarantees).
- R001: compatible finite labels, no-symbol contribution
  A=delta^M min(1,48g+beta), pathwise safety and event-radius lemma.
- R004: actual capped early/dyadic pair-success certificates have sum
  C<=6400a for all beta<=1/2. This is stronger data than a scalar risk
  inequality and is the input for BLIND.
- R009: full-class exceptional event E count bound
  P(E,J<w)<=min(q0,10q0K³w/n), q0=delta^floor(M/2),
  with NO additive exception, every positive integer w.
- R010: independently to be bound before adopting this assembly,
  newly written original-IID mean-TV lower2^-24 a, hence original
  every-beta floor; strong-beta original upper81a.

New local algebra below uses R009 at ALL weak-beta parameters, removes
the former critical gap, and combines the recovered endpoint/short/strong
interfaces. Missing historical S026–S032 originals are not premises.
R010 is an explicit reconstruction, not recovered historical S027 bytes.
R006/R008 absorbing-subclass results are valid earlier steps but not needed
to substitute for the arbitrary-pi R009 theorem.

## 3. Long history and weak beta
Assume M>=K⁴ and 0<beta<=1/2. Then M>=16, a=K^(3/2)/sqrt(n) and
hstar=K²/sqrt(n) are uncapped. Put r=floor(M/2), lambda=-log(delta),
t=beta n and q0=delta^r. Because delta>=1/2, lambda<=2beta and
r lambda<=t. Also n/r<=9/4: for even M it is 2+1/r<=17/8,
for odd M it is 2+2/r<=9/4. Hence
  q0<=exp(-4t/9).                                       (3.1)

Use R009's E with the actual compatible original-stack augmentation.
The S020/R001 event-loss interface gives
  E[ell_q 1_E]<=B_E,
  B_E=min(q0,80 q0 sqrt(10K³[K+r lambda]/n)).
The radius lemma on this SAME event gives
  E[rho(J)1_E]<=(8/5)B_E.                               (3.2)
This uses an upper event mass q0; it does not condition original stacks
to be iid.

We claim the uniform simplification
  B_E<=360a+512T.                                       (3.3)
If t<=K, use r lambda<=t and q0<=sqrt(2)delta^(M/2):
  B_E<=80sqrt(20) q0 hstar
       <=80sqrt(40)T<512T.
If t>K, use (3.1), hstar/a=sqrt(K), and
  B_E/a <=80sqrt(10) sqrt(K)exp(-4t/9)sqrt(1+t/K)
          <=80sqrt(20) sqrt(t)exp(-4t/9)<360.
Indeed sqrt(t)exp(-4t/9) has maximum sqrt(9/(8e))<1, and
80sqrt(20)<360. These two cases prove (3.3) without any moderate-log
hypothesis or upper limit on M.

Let G be no symbol success and Eplus the pair-success union. R001 gives
the nonnegative cover G,E,Eplus and
  E[ell_q1_G]<=A, E[rho(J)1_G]<=delta^M g<=A.
Moreover
  A<=48delta^M g+beta delta^M<=96D+a,                    (3.4)
since delta>=1/2, beta delta^M<=1/(eM), and a>=1/M.
The last inequality follows from K³M²>=M+1.
R004 provides success certificates with sum C<=6400a, and its exact
event partition plus R001 radius comparison gives radius cost <=(8/5)C.
Therefore
  R^+<=A+B_E+C<=6761a+96D+512T<=7369H<2^13 H.            (3.5)
For the SAME ALG, sum pathwise safety over this cover:
  risk(ALG)<=2A+(13/5)(B_E+C)
            <=3(A+B_E+C)<=22107H<2^15 H.                (3.6)
These bounds are uniform over all sources in the full class, not only
an absorbing-stationary subclass. Taking cap one is independent.

For weak beta, delta>=1/2 and a<=1 imply F>=a/2. Consequently H<=2L.
Equations (3.5)–(3.6) imply the COMMON upper2^14 L and BLIND upper2^16 L
on the long weak-beta domain. Neither a large certificate nor a mixing-TV
distance is used as a statistical lower.

## 4. Short history and weak beta
For 0<beta<=1/2 and M<=K⁴, use S019/S024:
  R^+<=128H_S, risk(ALG)<=1472H_S.
Here hstar>=sqrt(K⁴/(K⁴+1))>=sqrt(16/17)>1/2, including the cap
branch hstar=1. Thus H_S=max(a,delta^(M/2))<=2max(a,T)<=2H.
We obtain original upper256H<2^13H and ALG upper2944H<2^15H.
Again H<=2L gives COMMON and BLIND at their stated constants.
The overlap M=K⁴ is harmless; the two derivations concern the same
actual algorithms and exact data. M=1 and all small alphabets are included.

## 5. Strong beta and endpoints
If beta>=1/2, then delta<=1/2 and
  D<=delta^n<=delta^(M/2), T<=delta^(M/2).
For integer M>=1, (M+1)2^-M<=1 (equality at M=1, decreasing thereafter).
Thus delta^(M/2)<=i: if i=1 it is trivial; otherwise square and use
(M+1)delta^M<=1<=K. It follows that
  L=F, H=a                                               (5.1)
throughout this domain. R010 supplies original upper81a; S025 supplies
the SAME ALG upper8000F. These are below the asserted upper constants.
At beta=1 no residual division is used; the separate IID interfaces and
the direct D=T=0 definitions apply.

At beta=0, D=g,T=hstar,F=a, so L=H=g. The inherited general original
48g and ALG49g bounds cover this endpoint directly. No beta logarithm
or residual convention is substituted at zero.

Together Sections3–5 exhaust every K>=2,M>=1,beta∈[0,1] and prove both
upper assertions for the originally specified algorithms.

## 6. Lower bounds, separation, and one-algorithm quantifiers
S016 gives R>=2^-17 L on the entire parameter domain. Since every
fixed original algorithm is admissible, it also gives R^+>=2^-17D and
R^+>=2^-17T. R010 adds the all-beta original floor R^+>=2^-24a.
Taking the MAXIMUM of these scalar lower bounds yields
  R^+>=2^-24 max(a,D,T)=2^-24H.
The witnesses need not be the same; no addition of risks is claimed.
R010's original-rule lower is not incorrectly imposed on common IID
minimax, which has scale i rather than a.

Thus both COMMON and ORIGINAL are proved. Divide their positive
two-sided bounds to get SEPARATION exactly:
  2^-24H/(2^14 L)=2^-38 H/L,
  (2^13H)/(2^-17 L)=2^30 H/L.
All positive scales are at most one, so the stated cap-one uppers
are consistent in every regime.

ALG was fixed once from K,M and history before beta comparisons.
Every case above analyzes that SAME map; there is no parameter-dependent
choice of threshold, source-dependent algorithm or hidden class test.
COMMON lower and BLIND upper give
  risk(ALG)/R<=2^16 L/(2^-17 L)=2^33
for every beta simultaneously. The denominator is positive because
L>=F>=i>0, also witnessed by the inherited full-data IID lower.
Every beta-blind A belongs to the larger beta-informed admissible set
at each fixed beta, so risk(A;beta)>=R. Infimum after supremum yields
Gamma_all>=1; the explicit ALG gives its upper. This proves ADAPT.

## 7. What is completed, and what is not claimed
These formulas give the requested all-parameter orders for common minimax
and original full-history add-one in the fixed experiment, and constant
adaptation without reading beta. Row-count/pooling selection suffices;
an additional suffix branch is not necessary to attain these orders.
Earlier sqrt(log(eK)) upper R005 remains true but is superseded by the
stronger constant upper; it is not retroactively labelled a false result.

The theorem does not optimize numerical constants, claim exact minimax
values, certify novelty, prove a network implementation or computational
budget, treat higher-order or nonhomogeneous sources, change the terminal
query, or establish physical reliability. Those are not hidden premises
for completion of the user's two stated statistical objectives.
Independent LLM review is not external peer review or formal verification.
Full source and review bindings must be verified before accepting this
assembly, especially the pending R010 reconstruction.
