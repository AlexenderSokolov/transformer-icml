# AU001 — Residual suffix laws remove the additive burn error

2026-11-02. Root-authored candidate; independent review required. This is a refinement of accepted IU001, not a correction of its valid bound. It preserves the exact NB002 finite predictor and original complete-master interface. No new runtime operation or beta input is introduced.

## 1. Theorem and experiment

Let K>=2, M>=64, h>=4 be integers, Q=2^h. Observe the same homogeneous second-order source through X_1,...,X_(M+2), with pair chain Y_0,...,Y_M. The full all-state class D2(beta), 0<=beta<=1, has a hidden stationary pi and P^2(s,t)>=beta pi(t) for every pair s,t, including off-support starts. Initialization is arbitrary. The target is theta_(Y_M), and loss is unconditional expected TV at the actual endpoint. B is exactly the accepted NB002 finite map, with its complete SRC master bank, exact side fields and no raw-history reread.

Set

    b0=max(beta,1/M),
    W(M,beta,Q)=[1+ln(1+Q/(M b0))]/Q.

For all such parameters,

    sup_D2(beta) E TV(B,theta_(Y_M))
      <=min(1, 2^16 L + [2^14 K^3+5320K^5] W(M,beta,Q)). (AU1)

L is the unchanged R011 statistical scale. In particular, since L<=K^(5/2)/sqrt(M),

    risk(B)<=min(1,2^16 K^(5/2)/sqrt(M)
                     +[2^14 K^3+5320K^5] W).           (AU2)

This holds at every legal Q, not just a threshold schedule. It is an upper theorem only. A separately reviewed stationary lower is required for an all-Q minimax classification.

A more precise intermediate bound for beta>0 is

    risk(B)<=min(1,2^16 L
        +(K^3/Q)[8360+456 ln(1+(480/76)Q/(beta K M))]
        +9K/Q+7 epsilon Psi(152K^5/Q)),                 (AU3)

where epsilon=(1-beta)^floor(M/4) (zero at beta=1, as M>=64), and Psi(x)=x(1+ln(1/x)) for 0<x<1, Psi(0)=0, Psi(x)=1 for x>=1. The corresponding compact version is

    risk(B)<=min(1,2^16 L
        +2^14 K^3/Q[1+ln(1+Q/(beta K M))]
        +7 epsilon Psi(152K^5/Q)).                     (AU4)

Compared with IU001, the additive 4 epsilon is replaced by a numerical error that also vanishes with precision. This is possible because the residual suffix is itself an ordinary homogeneous trajectory, so its occupation cost can be bounded rather than discarded by a unit cap.

## 2. Actual inherited inequalities

Accepted NB002, as explicitly assembled in SM001 and IU001, gives the same pre-integration reduction

    risk(B)<=min(1,2^16 L+3 E_mu v+P_mu(C)+9K/Q),
    A=76KM/Q, v=min(1,A/(J+K)), C={J+K<4A},
    J=sum_(j=0)^(M-1)1{Y_j=Y_M}.                       (2.1)

This is not inferred by inverting a final scalar risk theorem. NB002's near-IID branch uses rejection containment and its actual CT/GT tails; the other branches retain count-radius certificates. We inherit their validity, including finite exceptional cases and the cap. Only the two nonnegative occupation terms are refined.

For a stationary path of length m>=1 with the same P and beta>0, accepted IU001 Lemmas 2.1 and 4.1 give, for every A>0 and integer kappa>=1,

    E_pi min(1,A/(J_m+kappa))
       <=(d A/m)[17+ln(1+480/(beta A))],
    P_pi(J_m+kappa<4A)<=4d A/m,                        (2.2)

where d=|supp(pi)|<=K^2. The second line follows directly from the positive-return bound at the exact integer threshold ceil(4A-kappa)<=4A; if 4A<=kappa the event is empty. No independence of terminal query and occupation is assumed.

For ANY initial law nu, the universal terminal occupation lemma gives

    P_nu(J_m<w)<=min(1,K^4 w/(m+1)), integer w>=1.

We reproduce why it applies here. For a homogeneous D-state chain, let B_(l,w) be the largest such probability over initial states. Counts in a full trajectory dominate counts in any terminal suffix with the same endpoint. The Markov property therefore makes B_(l,w) nonincreasing in l. On each deterministic path, the indicator of fewer than w earlier visits marks only the first w occurrences of each state. Thus sum_(l=0)^m B_(l,w)<=sum_initial sum_(l=0)^m P_initial(J_l<w)<=D^2 w. Monotonicity gives (m+1)B_(m,w)<=D^2w. This is the actual argument in inherited G/U fact a12539a93d9f1ee3 section 11.1; D=K^2. It does not require positive rows, stationarity or an independent query.

Layer cake at the strict integer threshold ceil(A/t-kappa)<=A/t, and the same threshold for the bad event, consequently yield

    E_nu min(1,A/(J_m+kappa))<=Psi(K^4 A/(m+1)),
    P_nu(J_m+kappa<4A)<=4Psi(K^4 A/(m+1)).           (2.3)

These hold for every A>0; the event is empty whenever its threshold is nonpositive. Psi is nondecreasing. We do not condition a row-stack or stationary theorem on an unrelated event.

## 3. Exact mixture of complete suffix laws

Put u=floor(M/2), m=M-u=ceil(M/2), r=floor(u/2)=floor(M/4). For beta in (0,1), define the residual two-step kernel

    R=(P^2-beta Pi)/(1-beta), Pi(s,t)=pi(t).

All-state minorization makes R stochastic even off stationary support. Also pi R=pi, R Pi=Pi R=Pi. Hence for every initial law mu,

    mu P^u=(1-epsilon)pi+epsilon nu,
    epsilon=(1-beta)^r,
    nu=mu R^r P^(u-2r).                               (3.1)

This is a probability mixture identity, not only a TV estimate. It follows by expanding (beta Pi+(1-beta)R)^r and using Pi's absorption relations, then applying zero or one final P step. At beta=1, P^2=Pi and r>=1, so mu P^u=pi; define epsilon=0 and omit the residual component. No division by zero or 0^0 is formed.

Given Y_u, the subsequent m transitions use the original P. Applying this same path-extension kernel to (3.1) gives the exact law of the ENTIRE suffix Y_u,...,Y_M as a mixture of an ordinary stationary P path and an ordinary P path started from nu. It is not necessary to identify an actual observable regeneration event. The residual path's kernel is P, not R, and its terminal query is its own actual endpoint. No discarded history is supplied to the predictor.

Let J_suf=sum_(j=u)^(M-1)1{Y_j=Y_M}. Pathwise J>=J_suf. Both occupation functionals in (2.1) are nonincreasing in J. Use (2.2) on the stationary component and (2.3) on the residual component. With

    c_suf=K^4/(m+1), H=17+ln(1+480/(beta A)),

we obtain

    E_mu v<=(1-epsilon)(dA/m)H+epsilon Psi(c_suf A),
    P_mu(C)<=(1-epsilon)4dA/m+4epsilon Psi(c_suf A).

Dropping only the harmless factor 1-epsilon and adding gives

    3E_mu v+P_mu(C)
      <=(dA/m)[55+3ln(1+480/(beta A))]
          +7epsilon Psi(c_suf A)
      <=(dA/M)[110+6ln(1+480/(beta A))]
          +7epsilon Psi(152K^5/Q),                    (3.2)

since m>=M/2, A=76KM/Q and c_suf A<=152K^5/Q. Substituting d<=K^2 in (2.1) proves AU3. All constants, including +9K/Q, remain visible. Exactly as in accepted IU001, 8360+9/K^2<=8363 and ln(1+(120/19)x)<=2+ln(1+x), so the compact constant 2^14 proves AU4.

## 4. A finite uniform scalar envelope

First assume beta>=1/M. Put t=beta M>=1, D=152K^5, and G=1+ln(1+Q/t), so W=G/Q. The first numerical term of AU4 is at most 2^14 K^3 W, because K>=1. Also epsilon<=1 and

    epsilon<=(exp beta)exp(-t/4)<=e exp(-t/4),        (4.1)

using floor(M/4)>=M/4-1. At beta=1, epsilon=0 and the inequalities remain valid.

If Q<D, Psi(D/Q)=1<=D/Q, and hence epsilon Psi(D/Q)<=D W. If Q>=D, D>=1 and

    Psi(D/Q)=(D/Q)[1+ln(Q/D)]<=(D/Q)(1+ln Q).

For t>=1,

    ln Q<=ln(1+Q/t)+ln t,
    epsilon(1+ln Q)<=G+e exp(-t/4)ln t<=G+4<=5G.     (4.2)

The last bound uses ln t<=t and max_(t>=0) t exp(-t/4)=4/e. Thus, in all cases,

    7epsilon Psi(D/Q)<=35D W=5320K^5 W.

Together with AU4 this proves AU1 when beta>=1/M, including equality.

If 0<=beta<1/M, b0=1/M and W=[1+ln(1+Q)]/Q. Accepted NB002 applies, including beta=0:

    risk(B)<=min(1,2^16 L+7Psi(76K^5/Q)+9K/Q).

For D0=76K^5>=1, direct inspection of Q<D0 and Q>=D0 gives Psi(D0/Q)<=D0[1+ln(1+Q)]/Q. Therefore the surcharge is at most (532K^5+9K)W, which is no greater than (2^14K^3+5320K^5)W for K>=2. This finishes AU1. The inequality L<=K^(5/2)/sqrt(M) proves AU2.

No asymptotic exception, positive stationary-mass lower bound or unknown hidden constant is used in this envelope. The constants are not optimized. The cap at one remains the probability loss cap, not an assertion about equality of rates.

## 5. Runtime, costs and evidence limits

The complete original interface is unchanged. The program does not compute pi, beta, R, nu, a burn, a suffix, a return time or the scalar envelope. These are analysis objects. B remains beta-blind at each supplied public K,M,h. A hardware budget chosen using a known class promise is not automatic learning of unknown beta.

All NB002/IU001 costs remain: six heads; bounded finite scores and charged evaluator; full arithmetic word p_word=4h+4ceil(log2(M+K+4))+64; hybrid depth O(Kp_word^2), width O(Kp_word); dense coefficient bits O(K^3 p_word^5); all-token dense pointwise/QKV bitwork O((M+3)K^3 p_word^6); uncached attention O((M+3)^2(K+p_word)p_word^2); masks, positions, input, history/QKV, controller/addressing, explicit holds/copies/clears, output, actual cache creation, offline generation/sorting/writes, and simultaneous-phase peak sums. The separate PURE expansion still has its separate larger full accounting. No resource term is removed by the mixture proof. Arithmetic precision, master grid h, total storage, and depth are different coordinates.

This upper does not by itself establish a sharp all-Q lower, K=2 logarithmic necessity, joint-K optimality, training attainability, a universal architectural limit, physical-noise robustness or computational advantage over paid direct counting. The old IU001 burn bound remains valid; the new result avoids its looseness with residual-law occupation control. First-stage delivered materials are not edited.

Independent LLM review is pending. Source identities and diagnostics are bound separately. Finite checks can corroborate mixture identities and inequalities but are not formal verification or external peer review.
