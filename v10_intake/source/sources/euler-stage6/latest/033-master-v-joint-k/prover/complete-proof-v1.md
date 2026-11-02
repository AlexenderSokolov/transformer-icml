# 033 REL-MASTER-V-JOINT-K — complete finite proof

Exact obligation: 44f736e89336c2d8be001f8f6f5b3dfc82fcd1cb206f234c07602338fae715a4.
The native statement equals the 10358-byte frozen file
outputs/033-master-v-joint-k/lead/frozen-statement-v1.md, SHA256
ce5b7f80c718738c2d672959d4ef662023f4cc2e681ef9bbc2f7e94de8a8043c.
We prove the entire MV-MATCH/MV-SEQUENCE/finite-interface/cost conjunction.

## 0. Direct premises and exact experiment

The actual direct Fact predecessors, and the only imported mathematical
premises, are the following admitted statements and their proved lemmas:

* SRC fef8372728290b45, Evidence
  e565455ae8465695ccf1f83e7c7f203d29c2f5bc4e49eb4b5eed822057d94505:
  the same finite Pi, exact head evaluator and directed readout, master
  and V interfaces, global guards, nominal bank error 78, and full costs.
* 016 a53804d650803060, Evidence
  fef1785395851e47b5ca0b719640449061718f4c670bfcd74c24cf0aec696c88:
  48T actual add-one risk, real-threshold TRUNC, and the original Pi
  two-cut joint-fault bound, here with gamma=0.
* MM5 946d42d5bf502eb4, Evidence
  aa23c442ca1006c6ac0b12379f64a0fa500fbbd6a2e41c798b7a4de3952baa82:
  actual risk at least 2^-16 min(1,T) for some source for each common
  full-history probability predictor.
* 032 372cbc90282df2cd, Evidence
  1a61c7931a3b8ee13da63e8e24e758106308055d829d8e5e60195fbca96d0cf0:
  V-MATCH and its complete finite all-residue clock source/path law
  in the T<1 branch. Its source is restated in section 3 below.

Section 5 of outputs/005-master-joint/prover/master-joint-proof-v1.md
is a writing source for listing rho's uses. No 005 Fact or binary
actual-11 cancellation lemma is a premise. The new all-K off-diagonal
identity is proved directly from SRC's actual finite operations below.
Neither 031, Dot's results nor 030's restricted CLOCK is used. Existing
proofs and dependencies of every predecessor are preserved.

Fix arbitrary integers K>=22, M>=1, h>=h_N and D>=0, and an arbitrary
public real delta>=0, with
    h_N=ceil(log2(128(K+1)(M+3)^3)), Q=2^h.
Put N=M+2 and n_tok=M+3. The observation is all of X_1^N;
Y_i=(X_(i+1),X_(i+2)), counted departures are 0<=i<M and the target
is theta_(Y_M) on the same path. Each experiment has one fixed
homogeneous second-order table theta, allowing zeros, and any initial
pair law mu. Suprema may choose these by public parameters, but
cannot change them along a realized path. Write
    C_c=sum_(i=0)^(M-1) 1{Y_i=Y_M,X_(i+3)=c}, J=sum_c C_c,
    p_c^+=(C_c+1)/(J+K), T=K^(5/2)/sqrt(M+1),
    A_M=K^5 delta, A_V=K^4 D/Q, B=A_M+A_V.
TV is half the L1 norm; Psi(0)=0, Psi(x)=x(1+ln(1/x)) for 0<x<1,
and Psi(x)=1 for x>=1, with natural logarithms.

Let R=R_MV^Pi(K,M,h,delta,D). The first common Markov kernel replaces
the 9K+1 canonical post-quantization, pre-fanout masters H by Hbar in
G_h^(9K+1), with coordinate changes <=delta on EVERY history. All
downstream copies use these replacements. Exact query/endpoint/flag
bits and all arithmetic remain uncorrupted. The original program then
produces the CURRENT positive bank Vbar. The second common kernel
replaces it by W in {1,...,2Q}^K with ||W-Vbar||_1<=D on every history.
This second budget is not measured from the counterfactual clean V.
The two kernels may be correlated and history-dependent, using only
the permitted observed data, current stage bank, public parameters
and source-independent randomness. Hidden theta, mu, future symbols
and private predictor seeds are unavailable.

The original suffix sees W and the exact retained bits, recomputes
S_W=sum W, floors QW_c/S_W for c<K-1 and uses the last residual.
It cannot reread erased masters, clean banks, old sums or quotients,
scratch or history. The kernels' history permissions do not add a
decoder port. This is SRC-Pi, not the later anchor program, and R is
total actual mean TV, not excess loss and not an infimum over decoders.

## 1. Precision, grid budgets and scalar inequalities

Because 128(K+1)(M+3)^3>=16 and >2M,
    h_N>=h0=max(4,ceil(log2 M)+1), Q>2M, Q>=M+1.
Thus Q/8 is an integer. The same bound gives
    Q>78KM, epsilon_V:=78KM/Q<1,
    K^5/Q<=K^5/(M+1)=T^2.                            (1.1)
These estimates hold for every permitted h, not just h=h_N.

For coordinates on G_h={0,1/Q,...,1}, each displacement is an integer
multiple of 1/Q. Consequently the first kernel's allowed displacement
in grid units is at most min(Q,floor(Qdelta)). If delta<1/Q, every
coordinate must remain unchanged. This finite description of the
allowed kernel class does not give Pi an arbitrary-real floor oracle.
For each fixed public delta we may specify a kernel by a finite integer
budget index; the nominal program and its public inputs are unchanged.

The identity
    Psi(x)=integral_0^1 min(1,x/t) dt, x>=0,
proves monotonicity, subadditivity and Psi(cx)<=c Psi(x) for c>=1,
by applying the corresponding elementary inequalities to the integrand.
Also
    Psi(x)<=2sqrt(x), Psi(x)>=min(1,x).               (1.2)
For 0<x<1, write v=ln(1/x)>=0. Then
Psi(x)/sqrt(x)=(1+v)exp(-v/2)<=2; its maximum is 2exp(-1/2).
The endpoints and x>=1 are immediate. These inequalities include
every real threshold and the zero case.

## 2. Joint upper bound with the current-bank budget

SRC gives, for the actual Vbar after any canonical master replacement,
    V_c^*=Q(C_c+1)/M,
    |Vbar_c-V_c^*|<=78+36Qdelta,
    sum V^*=Q(J+K)/M>0.
Thus the actual second-stage edit obeys
    ||W-V^*||_1<=D+K(78+36Qdelta).                    (2.1)
For positive u,v, adding and subtracting u/(sum v) proves
    TV(u/(sum u),v/(sum v))
       <=min(1,||u-v||_1/(sum v)).
The final ordered floor/residual changes W/(sum W) by TV at most
(K-1)/Q. Equations (2.1) and this normalization use the true J+K;
the ideal V^* is only a comparison vector, never a program input.

Apply the 016 joint-fault theorem with its good event the whole space
and gamma=0, or apply its add-one risk and real-threshold TRUNC to the
resulting pathwise bound. One obtains
    R<=min(1,48T+(K-1)/Q
        +Psi(K^4 M[K(78/Q+36delta)+D/Q]/(M+1))).      (2.2)
This is valid without independence among the two kernels, history,
J or any edits: (2.1) is pointwise and the pre-cut history marginal
is the original source marginal. No random J is treated as a fixed
iid sample size. The real-threshold version includes J=0 and sub-grid
budgets, and positive-bank guards hold even for arbitrarily large
public delta and D. There is no bad-event probability term.

Since Q>=2M, the argument of Psi in (2.2) is at most
    39T^2+36A_M+A_V<=39T^2+36B.
Use section 1 to bound its Psi by 2sqrt(39)T+36Psi(B).
Further, (K-1)/Q<=T, since sqrt(M+1)<=2M and K-1<=K^(5/2).
As 49+2sqrt(39)<64, this proves
    R<=min(1,64T+36Psi(B)).                           (UPPER)

## 3. Admitted lower subclasses and the exact clock law being used

Both identity kernels are allowed for every delta,D, so MM5 implies
    R>=2^-16 min(1,T).                               (STAT)
Taking the first kernel to be identity and using the second-stage
class from 032 gives
    R>=R_V^Pi(K,M,h,D)
      >=2^-80 min(1,T+Psi(A_V))
      >=2^-80 Psi(A_V).                              (V-LOW)
Indeed Psi(A_V)<=1, so the capped expression in the middle is at
least Psi(A_V). The current post-master bank is precisely clean V
in this subclass; hence no change of the second-stage budget occurred.

If T>=1, STAT alone already proves the requested capped lower bound.
We now assume T<1 only for construction of the new master witness.
Since M is an integer and M+1>K^5, M>=K^5. Let
    a=floor((K-6)/4), P=a^2, L=P+5, m=floor(M/L), U=a^2 L.
As proved in 032, or directly from 4a+6<=K<=4a+9<=8a,
    a>=4, K/8<=a<K/4, m>=4,
    K^4/4096<=U<=K^4, U(K+1)/M<=4T^2.               (3.1)
For example L<=K^2 and M>=K^5 give M/L>=K^3, and hence m>=4.
The last comparison follows from U<=K^4, K+1<=2K and M+1<=2M.

We use EXACTLY the homogeneous all-residue source of 032 sections
2–3, whose finite existence, lack of assignment conflicts, legal
shifts and complete observed path probabilities are admitted there.
Here is its full specification to make the invocation unambiguous.
Its four disjoint symbol groups are
    A={0,...,a-1}, Bgrp={a,...,2a-1},
    Cgrp={2a,...,3a-1}, Dgrp={3a,...,4a-1},
with markers (p0,q0,p1,q1,xi,zeta)=(4a,...,4a+5).
Let w_0,...,w_P be the lexicographically first word starting and
ending at 0 whose adjacent ordered pairs list every pair on A once,
including loops. Set w^0=w, w^1=w+a. Its rows are:

* (p_s,q_s)->w^s_0, (q_s,w^s_0)->w^s_1 and
  (w^s_i,w^s_(i+1))->w^s_(i+2), 0<=i<=P-2, s=0,1.
* Last A pair ->xi, (w^0_P,xi)->zeta,
  (xi,zeta)->(1-1/m)delta_p0+(1/m)delta_p1,
  (zeta,p_s)->q_s for s=0,1.
* Last Bgrp pair ->Unif(Cgrp), (w^1_P,c)->Unif(Dgrp),
  (c,e)->p1 and (e,p1)->q1 for c in Cgrp,e in Dgrp.
* All unspecified rows are delta_0.

Define y0=(p0,q0), y1=(q0,w0), y_r=(w_(r-2),w_(r-1)) for
2<=r<=P+1, y_(P+2)=(w_P,xi), y_(P+3)=(xi,zeta),
y_(P+4)=(zeta,p0). Set d=M-mL, k=(L-2-d) mod L, mu=delta_(y_k).
The stay circle names only the initial pair. The observed gate retains
its random activation probability 1/m. All these parameters are fixed
for the entire experiment and depend only on the public K,M.

The precise 032 path lemma applies for every such T<1 and every
residue d. The first gate is at departure d, followed by the unactivated
gates d+tL; the terminal slot is M=d+mL. In particular d=0 includes
the random gate at departure 0, and k=L-1 initializes (zeta,p0)
without any unobserved earlier gate probability. Departure M is not
in the count. If A_j is activation at gate index m-j-1, 0<=j<m,
then there are j old Cgrp x Dgrp queries and the terminal query, with
    p_j=P(A_j)=(1/m)(1-1/m)^(m-j-1)>=1/(4m).
Each prescribed sequence of these j+1 choices produces a unique full
observed history of probability p_j a^(-2(j+1)). In particular, given
A_j and any actual terminal query z in Cgrp x Dgrp,
    J~Bin(j,1/a^2), C_p1=J, C_c=0 for c!=p1,
    theta_(Y_M)=delta_p1, p1=4a+2<K-1.                (3.2)
The complete initial residue and all other observations remain in
this law. This is the actual terminal pair, not an independent query
substituted for it. Conditional iid choices are available only because
of this admitted full-path factorization, not for general sources.
No 030 high-kappa or concentration risk theorem is invoked.

## 4. Exact uniform rho and all of its finite-program uses

We derive the new identity from the actual SRC evaluator, rather than
from its error bounds. Write p=4h+4ell+64, ell=ceil(log2(M+K+4)),
and R_exp=2^p. SRC section 4 evaluates a score with integer numerator S
using the recurrence
    T_0=R_exp, T_j=floor(T_(j-1) S/(j R_exp)), 1<=j<=8p,
    W_exp=sum_(j=0)^(8p) T_j.
For the uniform head the score is exactly zero, so S=0, every term
after T_0 is exactly zero, and each allowed key has weight R_exp.
At the actual output position q=N+1, the allowed keys are precisely
3,...,N, exactly M keys. Its rho value coordinate is z_t=1{t=3},
which equals one at exactly one allowed key. The sums are exact integer
sums. SRC's actual returned head word is the floor of Q times its
integer numerator divided by its integer denominator, then divided
by Q. Therefore on EVERY observed history, including support-excluded
histories and M=1,
    hat rho=floor(Q R_exp/(M R_exp))/Q
           =floor(Q/M)/Q.                            (4.1)
Head clipping to [0,1] does not alter this value. This is an exact
finite identity, not an approximation obtained from the 2/Q head error.

Put d_M=ceil(log2 M) and r0=2^(-d_M-1). Since Q>2M,
    hat rho>1/M-1/Q>1/(2M)>=r0.                      (4.2)
Thus the original clean r=max(hat rho,r0) equals hat rho. The strict
first inequality also holds when Q/M is integral because floor(x)>x-1.
The value r0 itself has integer grid numerator Qr0, since h>=d_M+1.

For a declared query (u,v), denote the exact endpoint indicator by
    I_c=1{(X_(N-1),X_N)=(v,c)}.
The letter v in this definition is the query SECOND symbol. This
indicator uses only the retained exact endpoint and one-hot bits.
Use P_h(x,y)=floor(AB/Q)/Q for grid operands x=A/Q,y=B/Q: this is
one full integer product followed by SRC's directed integer quotient.
The actual readout from its canonical masters is exactly
    hat dT=1+hat alpha_v,
    initial_c=P_h(hat dT,hat h0_c)-hat f_c,
    g_c=P_h(hat dT,hat hvec_c)-hat nu_c
                  +hat rho I_c-initial_c,
    u_c=P_h(hat d2,hat q2_c)-P_h(hat d1,hat q1_c)-g_c,
    a_c=clip(u_c,0,1), r=max(hat rho,r0), V_c=Q(a_c+r). (4.3)
All additions/subtractions here are exact signed grid arithmetic;
hat rho I_c is exact selection by a BIT, not a rounded real product.
The temporary symbol u_c in (4.3) is a raw recovered frequency.

To specify the other quotients, if U_l and N_v are the integer
numerators of the selected hat v_l,u and hat nu_v, SRC computes
    D_l=floor(2Q(Q+lambda_l N_v)/(2Q-U_l)),
    hat d_l=D_l/Q, lambda_1=1, lambda_2=2.             (4.4)
The extra division-by-two guard is retained in this expression.
Thus hat d1,hat d2 depend only on v1,v2,nu and the exact query;
hat dT depends only on alpha and that query. None uses rho.

Equations (4.3)–(4.4) are the actual directed SRC operations, including
their ordering, full product and quotient remainder, not the ideal
real-head algebra. The masters are the 2K coordinates (q1,v1), 2K
(q2,v2), 2K (hvec,h0), and 3K+1 (alpha,nu,f,rho). In particular h0
and f are separate masters, not expressions to be recomputed from rho.
Replacing rho alone leaves their stored words unchanged, even though
some ideal statistical identities among them then cease to hold.
SRC's pre-fanout cut means every subsequent copy of rho is the replaced
word. The only two data uses of rho in the readout are the endpoint
term rho I_c and the shared r=max(rho,r0) displayed in (4.3). There
is no surviving clean-rho branch, empirical divisor or extra count port.

## 5. A legal rho-only kernel and exact broadcast

For the T<1 witness branch put
    b=min(floor(Qdelta),Q/8), epsilon=b/Q.
The integer b is nonnegative, epsilon<=min(delta,1/8). For each fixed
public real delta it specifies a finite common kernel, and is not a
new runtime operation of Pi on an arbitrary real input.
On ANY history whose actual query lies in the publicly defined
Cgrp x Dgrp, let the first kernel replace only rho by
    min(hat rho+epsilon,1).
On all other histories it is identity. Let the second kernel be identity
on the resulting CURRENT Vbar. This is canonical on every history;
its sole changed coordinate is nondecreasing by at most epsilon<=delta,
and its second-stage L1 edit is exactly zero<=D. It uses only the actual
query, the current rho master and public parameters, without J, counts,
hidden source data, future symbols or seeds. The cap ensures global
legality even before using any special properties of the witness source.

In the T<1 branch, M>=K^5>=2. From (4.1), on every history
    hat rho+epsilon<=1/M+1/8<=5/8<1.                 (5.1)
Thus the cap does not trigger whenever the query gate activates the
kernel. Equation (4.2) implies rbar=r+epsilon exactly; both quantities
remain in the same r=max(rho,r0) branch, with no new rounding.

An actual query (u,v) in Cgrp x Dgrp is off-diagonal, since the groups
are disjoint. Its actual endpoint is itself (u,v), whereas I_c tests
whether that endpoint equals (v,c). Equality would require u=v, so
    I_c=0 for EVERY c.                               (5.2)
This is the distinction from an actual-11 binary example.
After replacing rho, all operands of (4.4), hat dT, all four products
in (4.3), and initial_c are unchanged, bit for bit. In particular each
full product, quotient and remainder is identical, because its exact
inputs and the fixed finite algorithm are identical. The changed rho
copy used in the other fanout is multiplied/selected by I_c=0, yielding
exactly zero in both computations. Therefore every g_c and raw u_c is
unchanged. Clipping applies the same deterministic map to the identical
raw word, so every a_c is unchanged, even at a clipping boundary.

The only change in (4.3) is the shared r, whence the actual positive
bank has the EXACT finite identity
    Vbar_c=Q(a_c+r+epsilon)=V_c+Qepsilon=V_c+b
            for every c=0,...,K-1.                  (RHO-BROADCAST)
Here V denotes the counterfactual clean SRC bank on that same history;
the kernel and the suffix never access it. The operation is exact grid
addition. Since 0<=a_c<=1 and 0<r+epsilon<=5/8, its coordinates are
positive integer payloads <=(13/8)Q<2Q. No overflow, bank clip or
arithmetic guard changes the identity. For all other histories global
SRC canonical-input guards and the capped kernel already give legality.
For T>=1 no witness is required; identity kernels can simply be used.

Thus the proof accounts for EVERY rho fanout. It does not infer an
equality from the SRC 36delta stability bound, nor presume cancellation
through a changing clip. Formula (5.2), not a binary diagonal lemma,
ensures the raw and clipped frequencies are precisely fixed.

## 6. Actual output loss and the finite master harmonic bound

On an activated clock history the target is delta_p1 with p1<K-1,
by (3.2). Write S=sum_c V_c. The target output is a nonresidual
coordinate of the ORIGINAL suffix, so RHO-BROADCAST gives
    q_p1=floor(Q(V_p1+b)/(S+Kb))/Q
          <=(V_p1+b)/(S+Kb).
Consequently
    TV(q,delta_p1)=1-q_p1
       >=[S-V_p1+(K-1)b]/(S+Kb)
       >=(K-1)b/(S+Kb).                             (6.1)
The K-1 other positive coordinates and the last residual are included;
there is no floor loss subtraction in the lower bound because flooring
the true-label coordinate increases its deficit.

Use SRC's nominal coordinate error on clean V, not on an ideal bank:
    |V_c-Q(C_c+1)/M|<=78,
    S<=Q(J+K)/M+78K.
Thus (6.1), (1.1) and b=Qepsilon prove
    TV(q,delta_p1)
      >=(K-1)epsilon M/[J+K+78KM/Q+Kepsilon M]
      >=(K-1)epsilon M/[J+K+1+Kepsilon M].           (RHO-LOSS)
All K add-one masses and all K coordinate errors have been paid. This
is total actual loss; clean loss is never subtracted. At epsilon=0
the asserted term is zero and all denominators are still positive.

Set A=Kepsilon M and H=K+1+A>0. Given A_j and any terminal query in
Cgrp x Dgrp, (3.2) gives the finite conditional mean E J=j/a^2.
The function x -> 1/(H+x) is convex for x>=0. Conditional Jensen
applied to RHO-LOSS therefore gives
    E[TV | A_j,Y_M=z] >= ((K-1)/K) A/(H+j/a^2).
Sum over the actual terminal choices using their exact conditional
law, and then over j using p_j>=1/(4m). Loss on other histories is
nonnegative. We obtain the following new MASTER witness bound:
    E_clock TV >= ((K-1)/K) A/(4m)
                    *sum_(j=0)^(m-1) 1/(H+j/a^2)
       >= ((K-1)/K) A a^2/(4m) ln(1+m/(a^2 H)).      (6.2)
The last estimate is the integral of the decreasing positive function
1/(H+t/a^2) on [0,m], bounded above by its left-endpoint rectangle sum.
It retains the j=0 term and the finite upper limit. Since M/m>=L
and m>=M/(2L) for m=floor(M/L), M/L>=4, (6.2) gives
    E_clock TV >= ((K-1)/K) (Kepsilon U/4)
         *ln(1+M/[2U(K+1+Kepsilon M)]).              (RHO-HARMONIC)
All horizon remainders are retained in the admitted path law and in
these floor inequalities. This formula was derived from the new
master loss (6.1), not by pretending that 032's second-cut injection
performed a master broadcast. Only its source/path law was reused.

## 7. Quantized master scale and the real-budget remainder

Let y=K^5 epsilon, z=Kepsilon U and b0=U(K+1)/M. By (3.1),
    y/4096<=z<=y, b0<=4T^2, (K-1)/K>=1/2.
The harmonic bound can therefore be written
    E_clock TV>=((K-1)/K) (z/4) ln(1+1/[2(b0+z)]).
If y>T^2, then y>0, b0+z<5y, and hence
    R>=E_clock TV>= y/(8*4096) ln(1+1/(10y)).         (7.1)
For all y>0,
    y ln(1+1/(10y))>=Psi(y)/11>=Psi(y)/16.          (7.2)
Here is an elementary verification. For y>=1, ln(1+t)>=t/(1+t)
with t=1/(10y) makes the left side at least 1/(10+1/y)>=1/11.
For y<=1, put v=ln(1/y)>=0 and f(v)=ln(1+exp(v)/10). Then
f(0)=ln(11/10)>=1/11 and f'(v)=exp(v)/(10+exp(v))>=1/11;
thus f(v)>=(1+v)/11. Multiplication by y proves (7.2).
It follows from (7.1) that R>=2^-19 Psi(y).

If 0<=y<=T^2, section 1 gives Psi(y)<=2T. Since T<1, STAT implies
R>=2^-16 T>=2^-17 Psi(y). Thus in every case in this branch,
    R>=2^-19 Psi(K^5 epsilon), R>=2^-16 T.           (7.3)
When epsilon=0 the first term is zero; it does not assert a positive
master-only effect for a zero or sub-grid edit budget.

We now restore the stated REAL delta. If delta>=1/8, Q/8 is an integer
and floor(Qdelta)>=Q/8, so epsilon=1/8. Both K^5 epsilon and K^5 delta
are at least one, whence their Psi values both equal one. If delta<1/8,
then b=floor(Qdelta) and
    0<=delta-epsilon<1/Q.
Monotonicity, subadditivity, (1.1) and (1.2) give
    Psi(K^5 delta)<=Psi(K^5 epsilon)+Psi(K^5/Q)
                   <=Psi(K^5 epsilon)+2T.           (7.4)
The same weak inequality holds in the first, saturated case. Combining
(7.3)–(7.4) yields
    Psi(A_M)<=(2^19+2^17)R<=2^20 R,
    R>=2^-20 Psi(A_M), for T<1.                     (MASTER-LOW)
This comparison uses two lower bounds on the same supremum, possibly
with different source witnesses. It is not addition of risks from two
sources into a single experiment.

In particular 0<delta<1/Q cannot be discarded: it forces an identity
master kernel, but its continuous expression Psi(K^5 delta) is bounded
by 2T and thus paid by the statistical lower bound. The proof keeps
delta in the theorem and in the sequence statement, rather than
silently replacing it by epsilon. At large delta, the legal small
rho perturbation supplies the saturated lower term.

## 8. Joint lower bound and exact sequence equivalence

For T<1 we have STAT, MASTER-LOW and V-LOW simultaneously as bounds
on R. Their sources and kernels need not agree. Since 2^-80 is no
larger than the other two coefficients,
    R>=2^-80 max(T,Psi(A_M),Psi(A_V))
      >=2^-82 (T+Psi(A_M)+Psi(A_V))
      >=2^-82 min(1,T+Psi(A_M+A_V)).                 (8.1)
The middle inequality uses max of three nonnegative numbers >=their
sum/3>=their sum/4. The last uses subadditivity of Psi. This is only
a scalar comparison AFTER taking the common supremum. The master
witness uses T2=id; the V witness uses T1=id; the statistical witness
uses both identity. Each is an allowed pair of kernels for these same
public budgets, even if their worst sources differ.

For T>=1, STAT gives R>=2^-16, which dominates the requested capped
lower bound. Thus (8.1) and UPPER imply, for ALL stated finite parameters,
    2^-96 min(1,T+Psi(K^5 delta+K^4 D/Q))
       <=R_MV^Pi(K,M,h,delta,D)
       <=min(1,64T+36Psi(K^5 delta+K^4 D/Q)).        (MV-MATCH)
The stronger intermediate constants only establish the frozen
conservative constant; no subsidiary constant claim is split off.
Small M, including M=1, is covered by STAT and UPPER, without defining
a clock with an invalid m. Delta=0, D=0, sub-grid delta, every horizon
residue, all h>=h_N, delta>1 and arbitrarily large D are covered.

For a public sequence in this domain, let T_n, A_(M,n), A_(V,n) have
the meanings above, and B_n=A_(M,n)+A_(V,n). If all three nonnegative
terms T_n,A_(M,n),A_(V,n) tend to zero, then B_n->0, Psi(B_n)->0 by
(1.2), and UPPER implies R_n->0. Conversely if R_n->0, MV-MATCH forces
min(1,T_n+Psi(B_n))->0. The uncapped nonnegative sum must then tend
to zero, so T_n->0 and Psi(B_n)->0. As Psi(B_n)>=min(1,B_n), B_n->0;
both of its nonnegative summands tend to zero. This proves exactly
    R_MV^Pi(K_n,M_n,h_n,delta_n,D_n)->0 iff
    K_n^(5/2)/sqrt(M_n+1)->0,
    K_n^5 delta_n->0 and K_n^4 D_n/Q_n->0.           (MV-SEQUENCE)
The necessary terms may be witnessed by different sources, and
sources may vary with public n. No uniform almost-sure claim or
single source difficult across all parameters is asserted.

## 9. Full costs of the same SRC implementation

This proof changes no nominal Pi computation, decoder or port. Its
true word parameter remains p=4h+4ell+64, ell=ceil(log2(M+K+4)); the
statistical M+1 denominator is distinct from n_tok=N+1=M+3. The six
heads, finite logs, separately evaluated full scores, all head floors,
all n_tok rows, endpoint acquisition, directed readout, guards, clip,
r0 and original ordered suffix remain as realized by SRC.

We preserve SRC's dense/uncached batch hybrid construction bounds,
with their original absolute constants and representation conventions:

| Resource | Same SRC bound or structure |
|---|---|
| neural depth / width | O(Kp^2) / O(Kp) |
| heads total / maximum per layer; QK dimension; score cap | 6 / 4; at most 2K; 2 |
| single coefficient / full arithmetic word | at most 128p bits, including complete products, remainders, guards |
| dense coefficient slots / parameter bits | O(K^3 p^4) / O(K^3 p^5), zeros and bias included |
| active gates/projections / identity holds | O(Kp^2+K^2) / O(K^2 p^3) |
| alternative sparse program/coefficient/address/holds format | O(K^2 p^4) bits, not substituted for dense work/storage |
| masks / position metadata | O(n_tok^2+n_tok log(n_tok+1)) bits |
| observed input | O(NK) one-hot bits, or paid binary acquisition/conversion |
| rolling work arrays only | O(n_tok Kp^2) bits |
| uncached attention bitwork | O(n_tok^2 (K+p)p^2) |
| dense pointwise / QKV bitwork | O(n_tok K^3 p^6) |
| finite rational log generation / scratch | O(p^3 log^2(p+1)) / O(p log(p+1)) |
| finite arithmetic evaluator code | O(p^4) bits |

Input/query/actual-endpoint acquisition, QKV projections, masks,
residual copy, holds, clears, full arithmetic and output decode are
all charged. The offline package includes layout for K,N,h, masks,
positions, microcode and all actual-format gate/term/hold records.
For actual counts G_rec,T_rec,I_hold its generation/assembly retains
O((G_rec+T_rec+I_hold)p^2) bitwork and O((G_rec+T_rec+I_hold)p) working
bits; dense file output writes all coefficient bits including zeros.
At each phase sum all simultaneously live program/parameters, input,
mask/metadata, QKV, residual, banks, address/controller, temporary and
output storage. Total peak is the maximum of those phase sums; the
rolling-work line alone is not total peak. A separate PURE expansion
or cached/sparse representation keeps its own costs, not selected
cheaper entries mixed into this dense/uncached implementation.

The proof's clean V and ideal counts are analytical comparisons and
never become a snapshot, count table, cache or history bypass. The
fault kernels define an information-level replacement experiment.
Physical injection/protection, selection, movement, storage and
program costs must be charged separately if implemented. No physical
correction construction or equal-numerical-resource advantage is
claimed. In particular rho's nominal value is publicly computable
from M,Q; another paid decoder could use that information. The present
master witness therefore proves neither arbitrary-decoder irreversible
information loss nor a lower bound for all Transformers.

No compiler, literal ledger, network batch measurement or profile was
run. Bounded integer/Fraction diagnostics checked only the new finite
zero-score/readout algebra and do not replace the general proof.
[Non-scientific operational metadata omitted.]

## 10. Submission scope and preserved boundaries

Sections 1–8 prove the complete frozen finite conjunction, including
the exact new rho broadcast, loss, harmonic and real-budget bridges.
Section 9 preserves the same SRC realization and full costs. Direct
predecessors are exactly SRC,016,MM5,032; 005 supplies writing context
only and the old binary cancellation is not invoked. The source/path
lemma from 032 is used in its admitted T<1 range, not extended from
030's concentration branch. This is one complete submission.

No extension to K<22, h0-only precision, other corruptible bits,
extra arithmetic faults, excess loss, or optimal arbitrary decoders
is claimed. Prior roots/Fact dependencies, 031 and 032 remain accepted
without resubmission or reverse dependencies. The 027 two obstacles,
030 low-kappa/small-K gaps, 029 OPEN/PARKED, 021 closure, 022 OPEN/PARKED,
[Non-scientific operational metadata omitted.]
Dot's exclusive statistical continuation and the recorded absent
delivery endpoint remain separate; this proof does not claim Dot was
contacted or create a replacement member. Arbitrary-decoder sharp fault
rates, physical correction and genuine resource comparisons remain
outside this result. Acceptance of 033 does not solve the v10 mother task.

