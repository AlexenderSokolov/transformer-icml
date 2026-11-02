# BAI003 — Uniform arbitrary-start binary precision upper with an absorbing diagonal

2026-11-02. Author candidate v2; independent delta review required. BAI001 and BAI002 v1 files remain unchanged. This strengthens BAI002 by removing ALL compact-active-core assumptions, but does not cover nontrivial full stationary support.

## 1. Result

Fix M>=64, integer kappa>=1 and dyadic Q>=16; z=kappa Q. Consider ANY binary second-order source with theta00(1)=0, arbitrary other rows

    b=theta01(1), e=theta10(0), t=theta11(0) in[0,1],

and ANY initial pair law. The unchanged accepted SB001 finite program T obeys

    E TV(T,theta_(Y_M))
      <= min{1, 2^17/sqrt(M) + 3/Q + 1600/z}.           (BAI3.1)

The symmetric result holds when11 is absorbing. Therefore all positive-beta classes whose stationary support is a singleton satisfy this stronger no-log upper under arbitrary initialization. No beta input, stationary initialization, row-positivity assumption, or stationary-mass lower bound is required.

The proof uses a new weighted actual-terminal occupation lemma for a three-state alternating-renewal chain. It does NOT rely on square-root-beta marginal mixing, which can fail on this very class.

## 2. Reflected chain and weighted occupation lemma

For the moment let 0<b,t<1. On A=01,B=10,C=11 define

    R=[[0,1-b,b],[1,0,0],[0,t,1-t]].

Let J_s=sum_(j=0)^(M-1)1{Y_j=s}. The claim is, for every initial active law, M>=8, and every A0>0,

 E_R[ 1{Y_M=A} min(b,A0/(J_A+2))
       +1{Y_M=C} min(t,A0/(J_C+2)) ]
       <= 256 max(A0,1)/M.                            (2.1)

We prove the stronger auxiliary bounds, separately for s=A,C,

    E_R[1{Y_M=s} q_s/(1+q_s J_s)]<=64/M,
    q_A=b, q_C=t.                                     (2.2)

The elementary inequality

    min(q,A0/(j+2))
      <=2 max(A0,1) q/(1+qj), q in[0,1], j>=0,

then proves (2.1). At q=0 both sides are zero; otherwise compare min(q,1/(j+2)) with the displayed harmonic expression. Boundary b,t in{0,1} follow by continuity of finite-horizon expectations, after (2.1) and (2.2) are established with constants independent of b,t.

## 3. Macro-runs and a logarithmic renewal coefficient

An A-run starts at A and ends upon arrival at C. It has G_b A visits, where G_b is geometric on{1,2,...} with success probability b. Its duration is2G_b-1 because each failure visits B then returns A. A C-run starts at C and ends upon arrival at A, via B; it has G_t C visits and duration G_t+1. Their probability generating functions are

    D_A(z)=b z/[1-(1-b)z²],
    D_C(z)=t z²/[1-(1-t)z].

Successive runs are independent by the Markov property. A complete alternating cycle has pgf

    F(z)=D_A(z)D_C(z)
        =bt z³/[(1-(1-b)z²)(1-(1-t)z)].

Write L(z)=-log(1-F(z))=sum_(n>=1)L_n z^n. Formal power series are sufficient; F has zero constant term. All coefficients L_n are nonnegative, and

    L_n=sum_(k>=1) P(S_k=n)/k,                         (3.1)

where S_k is the completion time of k complete cycles.

Two uniform bounds are essential:

    0<=L_n<=min(b,t,3/n).                              (3.2)

For L_n<=b,t, discard1/k in (3.1). Complete-cycle times are strictly increasing, so the resulting sum is a renewal-completion probability at time n. Starting at C and taking C-run then A-run, completion at C requires an A→C transition at time n and has probability at most b. Starting at A and taking A-run then C-run gives the SAME cycle-duration distribution (convolution commutes); completion at A requires a C→B transition one step before the final deterministic B→A step and has probability at most t. Thus both bounds hold.

For3/n, direct determinant computation gives

    det(I-zR)=(1-(1-b)z²)(1-(1-t)z)(1-F(z)).

The formal identity -log det(I-zR)=sum_(n>=1)tr(R^n)z^n/n follows, for example, by differentiating and using the formal inverse geometric series, then comparing constant terms. Consequently

 nL_n=tr(R^n)-(1-t)^n
                   -2*1{n even}*(1-b)^(n/2)<=3,

since R^n is stochastic and each diagonal entry is at most one. This establishes (3.2), without any eigenvalue-gap estimate.

## 4. Exact run-count reduction for weighted terminal queries

Let

    g_q(r,N)=binom(N-1,r-1)q^r(1-q)^(N-r), N>=r>=1,

be the probability that r independent geometric(q) variables sum to N. For r>=2,

    g_q(r,N)/[q(N-1)]
      =g_q(r-1,N-1)/(r-1).                            (4.1)

Here N>=r>=2, so all denominators are positive. In particular

    g_q(r,N)/[1+q(N-1)]
      <=g_q(r-1,N-1)/(r-1).                           (4.2)

### Terminal A

For each path ending A at time M, virtually append the single transition A→C. Its probability multiplier is b. The completed A-runs contain exactly N_A=J_A+1 A visits. Therefore its contribution to the left side of (2.2) is the complete-run probability divided by1+b(N_A-1).

If the path starts A, the augmented path has k+1 A-runs and k C-runs, k>=0, and total duration M+1. For k>=1, apply (4.2) to its A-run count. Decreasing both the number of A-runs and their total visits by one reduces their duration2N_A-r_A by exactly one. The resulting run sequence consists of k full A/C cycles of duration M, with weight1/k. Summing gives at most L_M.

The k=0 term means only A/B cycling before the terminal query. It is zero unless M is even; then it equals

    b(1-b)^(M/2)/[1+bM/2] <=2/M,

using q(1-q)^l<=1/(l+1). Thus initial A costs at most L_M+2/M<=5/M.

If the path starts C, the augmented path has k A-runs and k C-runs, k>=1, with duration M+1. For k>=2, the same reduction leaves k-1 full cycles and one extra C-run, total duration M, with weight1/(k-1). Their total is bounded by the coefficient [z^M]D_C(z)L(z). The k=1 contribution is at most [z^(M+1)]F(z), since its denominator is at least one.

### Terminal C

Virtually append C→B→A, whose probability multiplier is t and duration is two. Now N_C=J_C+1. If the path starts C, it has k+1 C-runs and k A-runs after augmentation. Applying (4.2) for k>=1 removes one C-run and one C visit, decreasing duration N_C+r_C by two; the remaining cycles have duration M and give L_M. The k=0 term is at most t(1-t)^M<=1/M.

If the path starts A, augmented counts are k A-runs and k C-runs. For k>=2 the reduction gives [z^M]D_A(z)L(z); the k=1 term is at most [z^(M+2)]F(z).

These are exact nonnegative run-probability comparisons. No conditional IID claim about a terminal-selected empirical row is used. The independence concerns only complete geometric runs under R.

## 5. Bounding the remaining coefficients uniformly

For n>=4,

    [z^n]F(z)<=8/n.                                   (5.1)

To see this, split the convolution of D_A and D_C according to which duration is at least n/2. At a supported A duration l, its mass is b(1-b)^((l-1)/2)<=2/(l+1); at a supported C duration l, its mass is t(1-t)^(l-2)<=1/(l-1). Each is at most4/n on its respective large-duration part, and the other distribution sums to one.

For M>=8,

    [z^M]D_C L<=15/M,
    [z^M]D_A L<=41/M.                                (5.2)

Split the waiting duration l at M/2. On l<=M/2, (3.2) bounds L_(M-l) by6/M and the waiting probabilities sum to at most one. On l>M/2, use L_(M-l)<=t for D_C and <=b for D_A (L_0=0). The geometric masses satisfy

    D_C(l)<=t exp(-tM/4),
    D_A(l)<=b exp(-bM/8),

at their supported l in this range. There are at most M terms. The remaining contributions are bounded by

    M t² exp(-tM/4)<=64/(Euler_e² M)<9/M,
    M b² exp(-bM/8)<=256/(Euler_e² M)<35/M.

This proves (5.2).

Section4 therefore bounds (2.2) by56/M for initial A or C (a common slack constant covers all four cases). For initial B and M>=9, the first transition to A is deterministic, after which the same terminal query and prior A/C counts are those of a length M-1>=8 path. Thus the bound is56/(M-1)<=64/M. At M=8, the integrand in (2.2) is at most one, which is at most64/M directly. Mixtures cover arbitrary initial active laws. This completes the proof of (2.2) and (2.1).

## 6. Transfer to the original absorbing binary source

The original source differs from R only because each departure from B goes to absorbing W=00 with probability e, rather than certainly returning A. Any original path ending in A,B,C has never visited W. Relative to the reflected path with the same initial active state, its probability multiplier is(1-e)^(N_B), interpreted as a product of transition factors at endpoints e=0,1. It is at most one. This dominates every nonnegative COMPLETE-path functional with its own actual terminal query and count. Initial mass at W never contributes to active endpoints.

Use row weights

    q_W=0, q_A=b, q_B=e, q_C=t.

By (2.1), the A,C contributions to E min(q_(Y_M),A0/(J+2)) are at most256max(A0,1)/M.

For the B contribution, note that absorption has never happened when Y_M=B. Consequently

 e P(Y_M=B)=P(Y_M=B,Y_(M+1)=W)
          <=P(J_(M+1)=0)<=16/(M+2).                  (6.1)

The final inequality is the accepted universal terminal-occupation bound for the four-state chain at horizon M+1, with integer threshold one. The transition into W in this event is its first visit. Therefore

    E min(q_(Y_M),A0/(J+2))
      <=256max(A0,1)/M +16/(M+2).                     (6.2)

Boundary b,t values follow by continuity as already noted. This also covers nonunique stationary classes at beta=0; no irreducibility assertion is needed.

## 7. Unchanged finite predictor and explicit risk constant

The deterministic binary floor argument in accepted BU001 v2 section4 works for arbitrary initialization and ANY choice of a true row exit probability q_s: min(p_hat,1-p_hat)<=p_hat, followed by1-Lipschitz truncation. Choose exactly the four q_s above, representing successor1 for W,A and successor0 for B,C. Let S be the true arbitrary-start add-one prediction risk, and B0=E[2/(J+2)]. The same unchanged SB001 decoder therefore obeys

 R<=2S+2B0+E min(q_(Y_M),A0/(J+2))
                        +64/z+16/M+3/Q,
 A0=6M/z, S<=2^13 sqrt(32)/sqrt(M+1),
 B0<=2sqrt(32)/sqrt(M+1).                              (7.1)

This imports only BU001's historywise floor inequality and universally valid empty-bank bound, NOT its stationary occupation lemma. The target in S is always the true original source row. In particular no reflected transition law replaces the next-symbol target.

Substitute (6.2) and max(A0,1)<=A0+1:

 R<=2S+2B0+1600/z+3/Q+288/M.

For M>=64,

 2S+2B0+288/M
 <=[(2^14+4)sqrt(32)+36]/sqrt(M)<2^17/sqrt(M).

This proves (BAI3.1), with the unit loss cap.

The complete paid SB001 program, its eight-coordinate grid bank, pair side field, uniform empty-bank fallback, ordered simplex rounding, finite arithmetic widths, decoder cut, and all resource accounting are unchanged. All runs, virtual transitions, weights, counts and generating functions here are analysis objects, never added inputs or runtime operations.

## 8. Scope and review status

For beta>0, a binary stationary class with zero crossing mass has exactly one absorbing diagonal; hence this result resolves that entire boundary case of the general arbitrary-start question. Full-support sources remain open. The theorem does not claim a new lower, a global mixing improvement, optimal constants, external novelty, or external peer review.

Direct dependencies: accepted SB001 v2 for the original add-one comparator and universal terminal occupation; accepted BU001 v2 section4 for the deterministic binary floor reduction and empty-bank bound. The alternating-renewal weighted occupation lemma is newly proved here. Independent review, source hashes, and diagnostics must accompany any proposed acceptance.

## 9. v1-to-v2 correction

The independent reviewer identified one horizon bookkeeping omission in the initial-B proof of (2.2): the M-1 reduction at M=8 would invoke an estimate stated only for horizons at least8. Section5 now handles M=8 by the unit integrand cap and applies the reduction only for M>=9. No theorem constant, source class, predictor, diagnostic formula, or M>=64 risk argument changed. v1 remains preserved.
