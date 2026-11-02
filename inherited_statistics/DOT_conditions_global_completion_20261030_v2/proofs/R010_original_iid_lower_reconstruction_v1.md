编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R010: original add-one IID lower, reconstructed from explicit moments
2026-10-30. Author candidate pending independent review.
This restores a needed scientific interface by a new complete proof. It
does NOT recover the unavailable historical S027 original or claim novelty.

## Theorem and inherited upper
Let K>=2,M>=1,n=M+1,a=min(1,sqrt(K^3/n)). In the exact full-history
second-order experiment, restrict all rows to a common unknown IID law p,
while the initial pair law is arbitrary. The ORIGINAL terminal-row
K-letter add-one has worst expected TV risk satisfying
  2^-24 a <= sup_(p,mu) E TV(q,p) <= min(1,sqrt(423)a).      (IID)
The upper follows by Cauchy–Schwarz from recovered S022 Sections 3–4,
which proves E TV(q,p)^2<=min(1,423K^3/n) for all p and arbitrary mu.
Only this upper is inherited; the mean-TV LOWER is proved below without
taking square roots of a squared-risk lower.

Every IID table belongs to every D2(beta), with stationary witness
pi=p tensor p and P²(s,t)=pi(t). Therefore for every beta in [0,1],
  R^+(K,M,beta)>=2^-24 a.                                (ALL)
For beta>=1/2, recovered S011's original-rule sufficient-burn bound gives
R^+<=min(1,81a); its finite use is justified in Section 4 below.
The common minimax risk is NOT asserted to be a in the IID class.

## 1. Small/moderate horizons via smoothing outside support
Choose p uniform on d=floor(K/2) letters, and mu=p tensor p. All M+2
symbols are IID uniform on those letters. For every j<M,
P(Y_j=Y_M)=1/d²: disjoint pairs have that probability, and the single
overlapping case j=M-1 requires three consecutive equal symbols and also
has probability d*(1/d)^3=1/d². Thus E J=M/d².

On every path, the original estimator assigns total probability
(K-d)/(J+K) outside the true support; TV loss is at least that amount.
By convexity of x->1/(x+K), and d>=K/3, K-d>=K/2,
  E TV(q,p)>=(K-d)/(M/d²+K)>=1/(2+18M/K³).
If M<128K³ this is at least 1/2306, hence greater than 2^-24 a.
This handles small K, zero counts and the whole capped regime without
requiring an asymptotic count approximation.

## 2. A complete fourth-moment bound for the overlapping IID noise
For the remaining M>=128K³ choose p uniform on ALL K letters and
mu=p tensor p. Let L=M-2 and keep the auxiliary departure indices
j=0,...,L-1, whose triples use only X_1,...,X_M. These variables are
independent of the ACTUAL endpoint Y_M=(X_(M+1),X_(M+2)).
The original predictor still includes the two other departures.

Fix any row s=(a0,b0) and output c. Define
 Z_j=1{X_(j+1)=a0,X_(j+2)=b0}(1{X_(j+3)=c}-1/K),
 S=sum_(j=0)^(L-1) Z_j,
 v=E Z_j²=(K-1)/K^4, sigma²=Lv.
Here 1/(2K³)<=v<=1/K³, |Z_j|<=1, and E Z_j=0.
Conditional on all symbols through X_(j+2), E Z_j=0.
Consequently distinct Z_i,Z_j are uncorrelated and E S²=Lv.
Variables whose triple index sets are separated by at least three are
independent. No conditional iid assumption at a random original count
is used.

We claim
  E S^4 <=69Lv+3L²v².                                   (4M)
Expand by multiplicities of indices:
- All four indices equal: at most Lv because |Z_j|^4<=Z_j².
- Two distinct indices with multiplicities 3 and 1: E[Z_i³ Z_j]=0
  for i<j by conditioning on X_1,...,X_(j+2). In E[Z_i Z_j³], only
  j-i=1 or 2 can be nonzero; otherwise the factors are independent and
  E Z_i=0. There are at most 2L such pairs, each absolute expectation
  <=E|Z_j|³<=v, with expansion coefficient 4. Total at most 8Lv.
- Two indices with multiplicities 2 and 2: for gap>=3 expectation is
  v²; for gap1 or2 it is at most v. With coefficient6, at most
  3L²v²+12Lv.
- Three distinct indices i<j<k: only the term with largest index squared
  can survive, again by the conditional mean-zero property when the
  largest exponent is one. The remaining E[Z_i Z_j Z_k²] vanishes if
  j-i>=3 (first factor independent with mean zero), or if k-j>=3
  (last squared factor independent and E Z_i Z_j=0).
  Thus both gaps are at most2: at most4L triples. Each absolute
  expectation is <=E Z_k²=v, and its expansion coefficient is12.
  Total at most48Lv.
- Four distinct indices: largest index has exponent one, so expectation
  is zero by the same conditioning.
Summing 1+8+12+48=69 proves (4M) for every row/output, including overlapping
equal-symbol contexts. Negative contributions were only replaced upward
by absolute values.

Since L>=M/2 and M>=128K³, sigma²>=M/(4K³)>=32. In particular (4M)
implies E S^4<=72 sigma^4. By elementary Cauchy–Schwarz,
  E S² <= sigma²/2 + sqrt(E S^4 * P(S²>=sigma²/2)),
which gives
  P(|S|>=sigma/sqrt(2))>=1/288.                          (PZ)
This derivation is a direct lower-tail bound, not a conversion of an
upper second moment or a squared-loss minimax result.

## 3. Restore the original count and actual endpoint
Condition on Y_M=s. The entire auxiliary S remains independent of this
conditioning. The full original count J_s consists of its L auxiliary
context indicators plus at most two additional departures. Therefore
  E[J_s+K | Y_M=s]<=L/K²+K+2=:m_D.
Markov gives P(J_s+K>576 m_D | Y_M=s)<=1/576. Combining with (PZ) by
a union bound, the event
  |S|>=sigma/sqrt2, J_s+K<=576m_D
has conditional probability at least1/576. No independence between
this denominator and S is asserted.

For the uniform target, add-one prior bias cancels exactly:
  q_s(c)-1/K=[C_s(c)-J_s/K]/(J_s+K).
The full numerator differs from S by two terms, each of magnitude at
most one. Since sigma>=sqrt32=4sqrt2, the good event gives
  |C_s(c)-J_s/K|>=sigma/sqrt2-2>=sigma/(2sqrt2).
Also L/K²>=K+2, so m_D<=2L/K².
Thus for every s,c,
  E[|q_s(c)-1/K| | Y_M=s]
  >= (1/576) * [sigma/(2sqrt2)]/[1152 L/K²]
  >= sqrt(K)/(2654208 sqrt(L)).
The final inequality uses sigma>=sqrt(L)/(sqrt2 K^(3/2)).
Averaging over the true uniform endpoint s, summing K output coordinates,
and taking half L1 yields
  E TV(q,p)>=K^(3/2)/(5308416 sqrt(L))
           >=a/5308416>=2^-24 a,
because L<n, a=K^(3/2)/sqrt(n) here, and 5308416<2^24.
Every original observation and both boundary departures were restored;
their dependence on the actual endpoint was bounded pathwise.

Together with Section1, this proves the all-K,M lower in (IID).
It is a lower for this particular ORIGINAL estimator, not a lower for
all prediction algorithms in the IID class.

## 4. Every-beta lower and strong-beta original upper
For any p, the legal IID table has P²=Pi on ALL starting pairs, including
off-support starts. Its stationary law p tensor p witnesses membership
in every D2(beta). The lower sources constructed above are therefore
admissible for every beta. This proves (ALL).

For beta>=1/2 and M>=32, set b=floor(M/2). The S011 burn coefficient is
h_b=delta^floor(b/2)=delta^floor(M/4) (with its beta=1 endpoint convention).
Writing M=4q+r, 0<=r<=3 and q>=8, one has
h_b<=2^-q<=1/(4q+4)<=1/(M+1).
The inequality 2^q>=4q+4 holds at q=8 and is preserved on increasing q
because doubling dominates the increment4. Thus S011's condition B
holds and gives the unchanged original-rule upper81a.
For M<32, a>=sqrt(8/32)=1/2, so the loss cap gives <=2a.
At beta=1 the separate IID upper also applies; no residual division is used.
Hence throughout beta>=1/2,
  2^-24a<=R^+<=min(1,81a).
No new proof of the common minimax F rate is claimed.

## Evidence and limits
Direct readable upper source:
S022 (SOURCE_INDEX.json), SHA256
028f43ae12886781bfd3641712c66720d24c667b59ca22a74c5dbbea5b0a5774.
S011 original-rule B interface is preserved in the recovered full S011
and fully stated/read in S024 Section1 and Section6. The original
S027 historical bytes remain unavailable; this proof is newly written.
It establishes mean-TV lower by a fourth-moment probability argument,
not an illicit square-root lower. No formal or external novelty claim.
