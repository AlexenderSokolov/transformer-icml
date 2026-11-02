# PF001 — The fixed-K beta-dependent master precision threshold

2026-11-02. Root author candidate. Independent review pending. The upper uses frozen IU001, whose independent acceptance is a prerequisite for accepting this synthesis. No previously accepted source is edited. This is a precision-threshold theorem, not an all-Q minimax risk formula, a joint-K optimum, a training claim, or an architecture-universal result.

## 1. Fixed experiment and exact statement

Use the same complete actual finite SRC statistical master prefix, its NB002 h>=4 domain, all 9K+1 masters and original exact side fields, and no raw-history/evaluator reread. Sources belong to the full all-state two-step class D2(beta); theta and the stationary certificate are hidden. The actual-terminal loss is unconditional expected TV. The decoder may use arbitrary computation, real simplex outputs and a source-independent seed. Write R_master for arbitrary initialization and R_master,stat for initialization at a hidden stationary certificate. The latter is a subclass of the former. Knowledge that initialization is stationary does not supply the stationary law.

Fix K>=3, M>=64 and beta in [0,1]. Put

    b=max(beta,1/M),
    f(M,beta)=1+ln(1+1/(b sqrt(M))),
    q_star(M,beta)=sqrt(M) f(M,beta).

This definition is finite at beta=0. Equivalently its logarithm uses min(sqrt(M),1/(beta sqrt(M))) for beta>0 and sqrt(M) at zero. Let Q=2^h, h>=4.

**Sufficiency.** For every Q>=q_star, the unchanged beta-blind NB002 predictor B_(K,M,h) satisfies

    sup_D2(beta) E TV(B,theta_(Y_M))
        <=min(1,B_K/sqrt(M)),                         (PF-U)

where the following finite constant is sufficient:

    B_K=2^16 K^(5/2)
          +max(5320K^5+9K, 2^15K^3+4).

The same bound holds on the stationary subclass. A dyadic Q in [q_star,4q_star] with h>=4 always exists.

**Necessity.** For every positive C there is an explicit c(C)>0, independent of M,beta and K>=3, such that if either original-interface minimax satisfies

    R_master,stat(K,M,beta,Q)<=C/sqrt(M)

or the stronger arbitrary-start guarantee R_master<=C/sqrt(M), then

    Q>=c(C) q_star(M,beta).                           (PF-L)

Thus, at each fixed K>=3, the precision threshold for constant-order statistical risk is

    Q=Theta_K(sqrt(M)[1+ln(1+1/(sqrt(M)max(beta,1/M)))]),
    h=(1/2)log2 M+log2 f(M,beta)+O_K(1),              (PF-P)

with the lower additive constant also depending on the chosen fixed risk multiplier. These are threshold orders: larger precisions are permitted. The bounds are uniform over beta, including beta varying arbitrarily with M. They do not assert that one unknown-beta procedure automatically chooses the smallest such h.

## 2. Actual dependencies and their roles

1. R011: i<=L<=g, with i=min(1,sqrt(K/(M+1))), g=min(1,sqrt(K^5/(M+1))), and full-history minimax lower >=2^-17 L. NB002 implements its beta-blind statistical order at the actual finite prefix. No closed statistical theorem is reproved.
2. Accepted NB002: for every h>=4 and beta in [0,1], the SAME map B has

       risk(B;beta)<=min(1,2^16 L+7Psi(76K^5/Q)+9K/Q).

   Psi(0)=0, Psi(x)=x(1+ln(1/x)) for 0<x<1, and Psi(x)=1 for x>=1.
3. Frozen IU001: for that SAME map and every beta>0,

       risk(B;beta)<=min(1,2^16 L
            +2^14 K^3/Q[1+ln(1+Q/(beta K M))]
            +4 epsilon_beta(M)),

   where epsilon=1 if floor(M/4)=0 and otherwise (1-beta)^floor(M/4). This upper requires its own independent acceptance; the present manuscript does not certify it by implication.
4. Accepted IP002: for K>=3,M>=64,0<=beta<=1/16 and16<=Q<=M/4, the original stationary interface obeys

       R_master,stat >=2^-331/Q
          ln(1+(1/8)min{Q/(Mb),M/Q}), b=max(beta,1/M).

   Its actual stationary pair law is hidden and the complete bank/side information is retained. No arbitrary-start lower is improperly restricted to stationarity.
5. Accepted SM002: the original stationary interface obeys R_master,stat>=2^-226/Q for every beta and every legal M,Q. Its binary IID full-history two-point proof also gives a stationary full-history statistical lower >=1/(32sqrt(M+2)).

The last two lower witnesses need not coincide. Only simultaneous separate inequalities, not a sum of their risks, are used.

## 3. Uniform upper proof

Write s=ln M and q0=q_star=sqrt(M) f. For M>=64,

    1<=f<=1+ln(1+sqrt(M))<=2+(1/2)ln M.              (3.1)

Also L<=g<=K^(5/2)/sqrt(M). We analyze the same predictor in two parameter regions; beta never enters its runtime computation.

### 3.1 Slow burn region: beta M<=8 ln M

Since 8ln M>=1, b=max(beta,1/M)<=8ln M/M. Therefore

    f>=1+ln(1+sqrt(M)/(8ln M))>= (ln M)/16.          (3.2)

To check the final inequality, if s<=16 it follows from f>=1. If s>=16, use ln(1+e^(s/2)/(8s))>=s/2-ln(8s). The function 1+7s/16-ln(8s) is positive at s=16 and increasing thereafter, so 1+s/2-ln(8s)>=s/16. No asymptotic exception is hidden here.

Put A_K=76K^5>=1. The function Psi is nondecreasing, so Q>=q0 implies Psi(A_K/Q)<=Psi(A_K/q0). If q0<A_K, then sqrt(M)<=A_K and

    Psi(A_K/q0)<=1<=A_K/sqrt(M).

If q0>=A_K, the defining formula (including equality) gives

    sqrt(M) Psi(A_K/q0)
       = (A_K/f)[1+ln(sqrt(M)f/A_K)]
       <= (A_K/f)[1+(1/2)ln M+ln f]
       <=10 A_K.                                    (3.3)

The last step uses f>=1, (3.2), and ln f<=f. Hence in both cases Psi(A_K/Q)<=10A_K/sqrt(M). NB002 yields

    risk(B;beta)
      <=min(1,[2^16 K^(5/2)+5320K^5+9K]/sqrt(M)),   (3.4)

because Q>=sqrt(M)f>=sqrt(M). This includes beta=0 and every very small positive beta; IU001 is not used at zero.

### 3.2 Effective burn region: beta M>8 ln M

Here beta>1/M and b=beta. Since M>=64, floor(M/4)>=M/8. Thus

    epsilon_beta(M)<=exp(-beta M/8)<=1/M.            (3.5)

At beta=1 the explicit epsilon is zero, so the same inequality holds without forming 0^0.

For fixed c>0, the function [1+ln(1+cQ)]/Q is decreasing for Q>0: after multiplying its derivative by Q², the numerator is cQ/(1+cQ)-1-ln(1+cQ)<0. Therefore the IU001 numerical term at Q>=q0 is bounded by its value at q0.

Put x=beta sqrt(M)>0, so f=1+ln(1+1/x). Because K>=1 and f>=1,

    1+ln(1+q0/(beta K M))
      <=1+ln(1+f/x)
      <=1+ln f+ln(1+1/x)
      =f+ln f<=2f.                                  (3.6)

The middle inequality uses 1+f/x<=f(1+1/x). Consequently IU001, (3.5) and L<=K^(5/2)/sqrt(M) give

    risk(B;beta)
      <=min(1,[2^16 K^(5/2)+2^15 K^3+4]/sqrt(M)).    (3.7)

Equations (3.4),(3.7) prove PF-U with the stated B_K. The arbitrary-start theorem immediately restricts to stationary sources.

Choose the first dyadic Q>=max(16,q_star). Since q_star>=sqrt(M)>=8, this Q is at most 2max(16,q_star)<=4q_star and has h>=4. No algorithm is asserted to compute an arbitrary real beta or logarithm: PF-U is a performance certificate for any supplied public integer h satisfying its inequality. A compiler using a known rational class promise would have to pay that input/configuration work separately.

## 4. Uniform stationary lower proof

Suppose R_master,stat<=C/sqrt(M), C>0. Set

    c0=min(1,2^-226/C)>0, q=Q/sqrt(M),
    F0=max(32,2[1+ln(8/c0)]),
    c(C)=min(1/2,c0/3,c0/F0,2^-332/C).              (4.1)

The accepted stationary IID bound first forces q>=c0. We prove q>=c(C) f by exhaustive cases.

### 4.1 beta>1/16

Since M>=64, b>=beta>1/16 and

    f<=1+ln(1+16/sqrt(M))<=1+ln3<3.

Thus q>=c0>=(c0/3)f.

### 4.2 Q>M/4

Let z=sqrt(M)>=8. The inequality 1+ln(1+z)<=z/2 holds at z=8 and remains true because the derivative of z/2-1-ln(1+z) is positive for z>=8. Therefore f<=sqrt(M)/2, and

    q>sqrt(M)/4>=f/2.

This handles large Q without extrapolating IP002 beyond its proved domain.

### 4.3 Remaining domain

Now beta<=1/16 and Q<=M/4, so IP002 applies. If q>=f the conclusion is immediate because c(C)<=1/2. If f<=F0, q>=c0>=(c0/F0)f. It remains to consider

    q<f, f>F0, q>=c0.

Put x=b sqrt(M), y=1/x, so f=1+ln(1+y). The first argument in the IP002 minimum is Q/(Mb)=q/x=qy. Because c0<=1,

    ln(1+(1/8)q/x)
      >=ln(1+(c0/8)y)
      >=ln(c0/8)+ln(1+y)
      =f-1-ln(8/c0)>=f/2.                            (4.2)

For the other argument, b>=1/M implies y<=sqrt(M), hence sqrt(M)>=e^(f-1)-1. Since q<f and f>=32,

    ln(1+(1/8)sqrt(M)/q)
      >=ln(1+sqrt(M)/(8f))
      >=f-1-ln(16f)>=f/2.                            (4.3)

To justify the last two steps, e^(f-1)-1>=e^(f-1)/2 for f>=32, and f/2-1-ln(16f) is positive at32 and increasing thereafter. These are finite scalar inequalities, not limiting comparisons.

The logarithm of one plus the minimum equals the minimum of these two logarithms. IP002 therefore gives

    C/sqrt(M)>=R_master,stat
       >= (2^-332 f)/(q sqrt(M)),

so q>=(2^-332/C)f. Together with the preceding cases this proves PF-L with the explicit c(C).

Any arbitrary-start predictor guarantee also holds on the stationary subclass, so the same necessity applies to R_master. The lower uses an original-interface stationary IID witness and the separately witnessed IP002 family; neither theorem is asserted after the other's extra proof oracle. No sum of two source risks is taken.

## 5. Why the target is the statistical order

For every beta and M>=64, the full-history arbitrary-start minimax has order M^-1/2 at each fixed K, uniformly in beta: R011 gives

    2^-17/sqrt(M+1)<=R_full<=2^14 K^(5/2)/sqrt(M+1).

For stationary sources, the upper restricts and the stationary binary IID full-history proof of SM002 gives a lower at least 1/(32sqrt(M+2)). Thus that experiment has the same fixed-K benchmark order uniformly in beta. We do not infer its lower by restricting an arbitrary-start lower.

Therefore PF-U and PF-L characterize the master precision needed to retain this statistical order, for either initialization convention, with K-dependent constants and a chosen fixed risk multiplier. They do not identify the exact risk at every insufficient Q, the sharp K dependence, or the optimal numerical minimax constant.

Some consequences of the single profile are:

- beta=0, or beta at most a constant times 1/M: f has order ln M and the extra log log M bits are required.
- beta sqrt(M) bounded below by a positive constant: f is bounded, giving a half-log master-bit threshold.
- beta=M^-alpha with any fixed alpha in (1/2,1): f has order ln M, even though M beta tends to infinity. IP001's ray is one explicit instance.
- Slowly vanishing beta sqrt(M) is covered by the same expression, rather than forced into a binary strong/weak classification.

These are statements about the declared fixed finite master interface. In the output-only experiment, direct counting and output rounding need only Q of order sqrt(M) at fixed K. Changing the representation or adding accessible pre-cut statistics can evade the present lower; arbitrary extra suffix depth cannot.

## 6. Budget interpretation and unchanged implementation costs

The predictor family B_(K,M,h) itself never reads beta or the stationary law. The same exact finite map has been analyzed for every class and every public h. However, selecting a near-minimal budget h from the profile f(M,beta) uses a class promise. This is not an algorithm that learns an unknown beta and automatically selects optimal hardware precision. Without such information, the earlier all-beta schedule remains a valid common worst-case configuration.

No new head, arithmetic primitive, state buffer or data port is introduced by this synthesis. The original NB002 complete charges remain: finite attention work, all-token pointwise evaluation, full arithmetic word p_word=4h+4ell+64, parameter/zero coefficient bits, masks/positions, input and history storage, copies/holds/clears, controller/addressing, output, offline generation and simultaneous-phase peak. The separate PURE expansion still has its larger charged resources. A changed h does not erase ell, turn hybrid depth into total computation, prove time/space superiority, or establish training attainability.

## 7. Evidence status and source identities

PF001 is a new root synthesis of the actual inequalities in R011, NB002, frozen IU001, accepted IP002 and SM002. Acceptance of this file requires independent checking of both IU001 and the scalar two-case/four-case synthesis above. Earlier SP001 and IP001 remain valid separate steps; they are not retroactively marked failures or silently expanded. No first-stage guide or delivered ZIP is modified.

All fixed-prefix, all-state, arbitrary-real-decoder and source-independent-seed conditions of the source theorems are retained. No external novelty or complete statistical/all-resource classification is claimed. Exact source hashes and any finite scalar diagnostics are to be saved separately before final review.
