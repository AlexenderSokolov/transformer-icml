编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R009 的词语指向问题与 R011 的历史依赖状态另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R009 — A tilted killed-label bridge for arbitrary stationary pi
2026-10-30. AUTHOR CANDIDATE; review status here is historical (EDITORIAL_NOTES.md).

## Useful result
For the ENTIRE legal class D2(beta), arbitrary initialization, K>=2,
M>=1 and 0<beta<=1/2, put delta=1-beta, r=floor(M/2), q0=delta^r.
Use the canonical endpoint-aligned pair labels and the compatible symbol
labels of R001. Let E0 be no successful pair label, N the number of
successful symbol labels, and J the ORIGINAL full departure count of the
actual endpoint Y_M. Then, for every integer w>=1,

 P(E0,J<w) <= min(q0, delta^M + 10 q0 K^3 w/(M+1)).       (A)

More strongly, for E=E0 intersect {N>=1},

 P(E,J<w) <= min(q0, 10 q0 K^3 w/(M+1)).                 (A+)

There is NO delta^M remainder in (A+). This is an actual full-class
occupation theorem candidate, not just a fixed-pi statement.
At M=K^5, beta=log(K)/K^5, it gives original add-one risk

 E ell <= min(1,8000/K)                                 (B)

using the accepted R002 trimming/original-stack reduction and R004 GS.
No conditional iid assertion is made. All tilting and labels are hidden
analysis devices. The algorithm is the unchanged full-history add-one;
no source table, pi, beta, initialization, or label is an algorithm input.

## Fixed experiment and dependency boundaries
Observe X_1,...,X_(M+2), Y_j=(X_(j+1),X_(j+2)), j=0,...,M.
P((a,b),(b,c))=theta_ab(c), with all rows normalized, pi P=pi,
and theta_ab(c)theta_bc(d)>=beta*pi(c,d) for ALL a,b,c,d.
The initial pair distribution mu is arbitrary, including outside support.
J_s=sum_(j=0)^(M-1)1{Y_j=s}, J=J_(Y_M). The target is theta_(Y_M),
loss half L1, and add-one uses all M original departures and observed outputs.
Write p(c)=sum_d pi(c,d), allowing p(c)=0. Summing minorization in d
implies theta_ab(c)>=beta p(c), so T=(theta-beta p)/delta is legal.

The count proof below is self-contained. For its statistical consequence
only, use R001's compatible joint augmentation, R002 Section 6 reduction
(7), and R004 grouped-success (GS). Accepted R006 motivated the cutset
charge but is not a mathematical premise of this new count proof.
No unavailable S026–S032 text, external theorem, or numerical check is a
premise. Exact public source bindings are in SOURCE_INDEX.json.

## 1. Exact full-history joint-label likelihood
Let e=M mod 2, so M=2r+e. Pair blocks start at times e+2j,
j=0,...,r-1. A legal block from (a,b) via (b,c) to (c,d) has ordinary
mass L=theta_ab(c)theta_bc(d). Its posterior pair-failure probability is

 W(a,b,c,d)=1-beta*pi(c,d)/L  if L>0.

Put W=0 if L=0. In that case minorization forces pi(c,d)=0, and all
original or tilted block masses below vanish, so this convention is harmless.
The posterior no-pair-success probability given the FULL observed history
is exactly the product of these W factors. For positive histories this
follows by multiplying the canonical independent pair-block splitting law:
no-success block joint mass is L-beta*pi(c,d). The unique shift midpoint
is retained, not replaced by an independent intermediate observation.

Given the full history, the canonical symbol labels have independent
posterior success probabilities beta*p(output)/theta_row(output).
Take the product of the two systems' conditional kernels given history,
exactly as in R001. Thus for z in [0,1], define

 A_z((a,b),(b,c))=delta*T_ab(c)+beta*z*p(c)
               =theta_ab(c)-beta*(1-z)*p(c),
 a_z=delta+beta*z.

For ANY event F depending on the full observed history,

 Z_F(z)=E[z^N 1_E0 1_F]
       =sum_paths mu(Y_0) 1_F product_edges A_z
                             product_pair_blocks W.     (1)

At z=0 use 0^0=1. This is a finite polynomial with nonnegative
coefficients. In particular Z_F(0)<=P(N=0)=delta^M,
Z_F(1)=P(E0,F), and EXACTLY

 Z_F(1)-Z_F(0)=P(E0,N>=1,F)=P(E,F).                     (1a) The labels are not asserted independent unconditionally.
Equation (1) is an exact complete-source-likelihood identity.

## 2. A common normalized killed pair kernel for every suffix length
For fixed z define the block kernel

 H_z((a,b),(c,d))=A_z,ab(c) A_z,bc(d) W(a,b,c,d).

For any starting pair s its row sum f_s(z) is a quadratic with
nonnegative coefficients in z. Consequently it is convex on [0,1].
At z=0, W<=1 gives f_s(0)<=delta^2. At z=1, summing L-beta*pi
(including zero-L cases) gives f_s(1)=delta. Hence the convex chord yields

 f_s(z)<=(1-z)delta^2+z delta=delta*a_z.                  (2)

Therefore B_z=H_z/(delta*a_z) is substochastic. Add a cemetery for
missing row mass. This is a fixed time-homogeneous killed chain on the
K^2 pair states, for each fixed z. Its transition retains the unique
legal midpoint if needed, but the following charging uses only the block
endpoint skeleton. The cemetery is never counted as a pair state.
Any prefix of j complete H_z blocks has total mass at most
(delta*a_z)^j. An extra initial anchor A_z has row mass exactly a_z.

## 3. First-w charge from only K refreshed start laws
For any fixed subprobability start nu on the pair states, let

 f_l(nu)=P_(nu,B_z)(alive at l,
        sum_(i=0)^(l-1)1{Z_i=Z_l}<w), l>=0.

On a single killed B_z trajectory, each live pair can be flagged only
at its first w occurrences. Therefore, for any integer L>=0,

 sum_(l=0)^L f_l(nu)<=K^2 w.                            (3)

Initial mixtures and killing preserve this deterministic charging bound.
Two families of probability start laws will be used, each with K members:

 nu_b^first(c,d)=p(c) A_z,bc(d)/a_z,
 nu_c^second(u,d)=1{u=c}p(d).                            (4)

Normalization follows from sum_d A_z,bc(d)=a_z and sum_c p(c)=1.
Since a_z>=delta>0, zero p and zero transition entries cause no singularity.
Both families are FIXED as the suffix length l varies. Applying (3) to
each of their K starts bounds the corresponding double sum by K^3 w.

## 4. Differentiate, discard just one pair-label factor, retain full counts
Set F={J<w}. Differentiate (1) edge by edge. Differentiation of one
A_z edge replaces it by beta*p(output). All other edge and W factors
are nonnegative. If the marked edge lies in a pair block, replace ONLY
that block's W by 1, increasing its contribution. Keep every other W.

Consider block j, 0<=j<r, and write l=r-j-1. Its prefix has total mass
at most a_z^e (delta*a_z)^j. The l subsequent blocks contribute a
factor (delta*a_z)^l times a B_z trajectory. The suffix begins at the
END of the marked block. Its l counted block-departure times are a
subset of the original departure times 0,...,M-1. Consequently the
original event J<w IMPLIES that the suffix skeleton's endpoint count is
<w. This is only an event inclusion: no original counts are removed
from J and no empirical loss monotonicity is asserted.

If the marked edge is FIRST in the block, its two-edge mass after
removing W is beta*p(c) A_z,bc(d). Conditional on the prefix's ending
second coordinate b, this is beta*a_z times nu_b^first. If the marked
edge is SECOND, its two-edge mass is A_z,ab(c) beta*p(d). Push the prefix
through that first A_z edge: its total mass grows by exactly a_z. Its
resulting c marginal is arbitrary, and the following refreshed pair has
law nu_c^second, with multiplier beta. For each case every individual
b or c marginal is at most the appropriate total prefix mass; thus that
marked-block contribution is bounded respectively by

 beta*a_z^(e+1)*(delta*a_z)^(r-1) sum_b f_l(nu_b^first),
 beta*a_z^(e+1)*(delta*a_z)^(r-1) sum_c f_l(nu_c^second).

As j varies, l runs through 0,...,r-1 exactly once. The prefactor is
independent of j. The first-w charge (3) now bounds the sum over ALL
paired marked edges by

 2 beta*a_z^(e+1)*(delta*a_z)^(r-1) K^3 w.                (5)

If e=1, there is one extra marked edge: the initial unpaired anchor.
Its marked mass is beta and all r remaining H_z blocks have mass at
most (delta*a_z)^r. Dropping F gives the additional bound
beta*(delta*a_z)^r. There is no extra anchor for e=0. Thus for r>=1,

 Z_F'(z)<=2 beta*a_z^(e+1)*(delta*a_z)^(r-1)K^3w
             + e beta*(delta*a_z)^r.                   (6)

This is a killed-path suffix argument, NOT iid sampling from residual
rows and NOT conditioning the original row stacks on labels. The rank-K
refresh starts, rather than a cutset in the original recurrent chain,
are the replacement for R006's K-state absorbing cutset.

## 5. Integrate the polynomial; finite constants and boundaries
Integrate (6) from 0 to 1, substituting da_z=beta dz:

 Z_F(1)-Z_F(0)<=
    2 delta^(r-1) [1-delta^(r+e+1)]/(r+e+1) K^3w
  + e delta^r [1-delta^(r+1)]/(r+1).                    (7)

This more precise form holds for every 0<beta<1 and r>=1.
For 0<beta<=1/2, delta>=1/2. With n=M+1=2r+e+1,
n/(r+e+1)<=2, so the second term is at most
8 q0 K^3w/n. If e=1, n=2(r+1), so the last term is at most
2q0/n <=(1/4)q0 K^3w/n because K>=2,w>=1. Thus the coefficient
10 in (A+) is conservative. For M=1 (r=0), the linear term
10 q0 K^3w/(M+1)>=40 already exceeds one, so the trivial cap proves
(A+). Finally P(E)<=P(E0)=q0 provides the other cap. This proves (A+)
for all stated parameters, including all large w and arbitrary starts.
Adding Z_F(0)<=delta^M and retaining P(E0)=q0 proves (A).

## 6. Critical original-rule risk consequence
Let M=K^5, beta=log(K)/K^5. As in accepted R006, beta<1/16,
delta^M<=1/K, q0<=2/sqrt(K), and K+log(1/q0)<=2K.
Set b=10q0 K^3/(M+1)<=20 K^(-5/2).
The event E=E0 intersect {N>=1} has mass<=q0 and satisfies (A+).
The accepted R002 reduction (7) with epsilon=0 (equivalently R001's
S020 event-stack certificate), preserving the original unconditional
row-stack marginal, gives

 E[ell 1_E]<=80sqrt(q0*b*[K+log(1/q0)])
            <=80sqrt(80)/K <=720/K.

The no-symbol-success event G has mass delta^M<=1/K and loss<=1.
The pair-success union Eplus contributes <=6400 sqrt(K^3/(M+1))
<=6400/K by R004 GS. The R001 cover G,E,Eplus therefore yields
E ell<=7121/K, and the independent loss cap gives (B) with constant 8000.
This is the SAME parameter-independent original add-one throughout the
full class. The accepted absorbing-star lower Omega(1/K) lies in this
class, so after independent acceptance this would close the full-class
critical minimax and original worst-risk orders at Theta(1/K).
No all-parameter minimax formula or automatic blind-selector transfer is
claimed here; the latter would require its own event-radius argument.

## 7. Failed extensions retained, and why this route is different
(a) A nonnegative original-P potential satisfying Ph<=delta^e h with
e>=0 must satisfy (1-delta^e)h=0 pi-almost surely: integrate against
stationary pi. If P is irreducible on finite full support, Ph<=h implies
h is constant (a minimum propagates), so any positive contraction at a
state forces h identically zero. This rules out a positive R006-style
original-P contraction on recurrent support. It does NOT rule out the
killed H_z kernel used here, whose mass genuinely decreases.

(b) Fixed-symbol taboo integration also cannot supply beta-rate survival.
The lawful first-order special case theta_ab(c)=delta*1{c=b}+beta/K has
pi(b,c)=K^-1[delta*1{c=b}+beta/K]. Its P^2((a,b),(c,d)) is
[delta*1{c=b}+beta/K][delta*1{d=c}+beta/K]>=beta*pi(c,d).
Starting at (b,b), for every c!=b, avoidance of C_c={(*,c)} through M
steps has exact probability (1-beta/K)^M. Weighted by p(c)=1/K, these
terms total (1-1/K)(1-beta/K)^M, tending to one on the critical ray.
This is an original-path method obstruction, NOT an E0-weighted count
counterexample and NOT a statistical lower. Sticky endpoint rows receive
substantial prefix information. The new proof retains E0's exact W
likelihood and integrates z; it does not use fixed-symbol taboo survival.

(c) Merely conditioning on a typical symbol-refresh count was not used.
Rare-event selection and small-count binomial tails would introduce new
errors. The polynomial integral includes EVERY refresh-count value
exactly; its 1/(r+e+1) factor is the source of the missing 1/M improvement.

## Diagnostics and status
R009_check.py and R009_check_result.json check exact rational block
contraction, joint-likelihood derivatives, parity/zero-mass cases, and
first-w charge on finite lawful examples. They are diagnostics, not proof.
No source file was modified. The independent scientific review is
included separately; current status is clarified in EDITORIAL_NOTES.md.
