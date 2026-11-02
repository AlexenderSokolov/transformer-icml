编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R008: the unchanged beta-blind ALG retains the absorbing critical rate
2026-10-30. Author corollary pending independent review.
No change of predictor, no full arbitrary-pi closure.

## Statement
Let K>=2, M=K^5, beta=log(K)/K^5. On the ENTIRE subclass with stationary
witness pi=delta_00 and arbitrary initial pair law, the SAME fixed
S024/S025/R001 count-guard ALG satisfies
  risk(ALG)<=min(1,20000/K).
Together with the accepted R002/R006 star-subclass lower, its worst risk
and the restricted common minimax risk are Theta(1/K) as K grows.
The algorithm is not given beta, pi, the absorbing symbol, source table
or initial law. This says nothing about zero-risk endpoint adaptation
for every absorbing subclass parameter, nor a full arbitrary-pi upper.

## Inputs and proof
Use the accepted R006 complete count bound and critical finite estimates:
  q0=delta^floor(M/2), epsilon=2delta^M<=2/K,
  b=8(K²+q0K³)/(M+1),
  q0 b[K+log(1/q0)]<=96/K².
For the exact compatible labels from R001, let G=no symbol success,
E=pair-no-success intersect symbol-success, and Eplus=pair-success.
They cover the full probability space, with possible overlaps.
Their labels are for analysis only.

R002's accepted event trimming removes at most epsilon mass from E to
produce E' with P(E')<=q0 and P(E',J<w)<=min(q0,bw) at each positive
integer w. The original stack marginal is unchanged by the extra
boundary coin. Define
  B=min(q0,80sqrt(q0 b[K+log(1/q0)]))<=800/K.
S020's event-loss inequality gives E[ell_q 1_E']<=B; R001's event-radius
lemma gives E[rho(J)1_E']<=(8/5)B. On the removed part each of ell_q
and rho is at most one. Thus pathwise guard safety gives
  E[ell_ALG 1_E]<=2epsilon+(13/5)B<=2084/K.              (1)
If the removed mass exhausts E this bound remains valid; no logarithm of
an actual zero event mass is evaluated.

On G, both original loss and radius are at most one, so
  E[ell_ALG 1_G]<=2P(G)<=2/K.                           (2)
For Eplus use the exact EARLY/DYADIC event partition in accepted R004,
not only its scalar GS statement. If C is the sum of its S020 event-loss
certificates, R004 proves C<=6400a, and R001's event-radius bound on
each SAME grouped event is at most 8/5 times its loss certificate.
Therefore
  E[ell_ALG 1_Eplus]<=(13/5)C<=16640a<=16640/K.           (3)
All events keep the actual terminal pair and every original departure.
Adding the nonnegative cover bounds (1)–(3) gives 18726/K<20000/K.
The loss cap gives the stated minimum with one.

R006 applies to the whole absorbing subclass, not a fixed excursion law.
The R002 legal star family is a subset and gives a true common randomized
prediction lower Omega(1/K) asymptotically with the complete data retained.
That lower applies to this fixed ALG too. This proves the asserted
restricted-class matching, with no claim of a finite all-K lower here.
Every input named above has a complete proof and independent review
in the indexed scientific closure, including the recovered S020 source. This corollary
imports no missing historical S026–S032 text, no unproved obligation (O),
and no unreviewed R007 alternative proof.
