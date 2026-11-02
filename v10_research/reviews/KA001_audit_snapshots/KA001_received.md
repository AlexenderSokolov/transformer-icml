# KA001 — A partial certificate-dependent adaptation phase diagram (candidate)

2026-11-02. New author candidate; fresh full independent review and root acceptance required. Accepted AB001–AB003 and BK001–BK002 are unchanged. This note isolates proved positive/negative certificate regions and leaves the critical full-history region explicitly unresolved.

## 1. Experiment and results

Use the accepted binary protected-terminal-pair experiment with the FULL corrupted word visible, offline source-independent strict Hamming budgets, and unconditional TV at the true terminal pair. The source is a homogeneous second-order chain with the all-state certificate P^2>=beta Pi. The predictor may know beta but not the actual k. Write

    s=M^-1/2, epsilon=k/M,
    e_beta=max(sqrt(beta),1/M),
    F_2=epsilon[1+log(1+1/(k e_beta))] for k>=1,
    F_2=0 for k=0,
    H_2=min{1,max(s,F_2)}.

The rate benchmark is the accepted known-k binary profile SC003/BT002.

### A. Weak certificates admit all-budget adaptation

For each fixed finite C>=0, a SINGLE ordinary corrupted-terminal-row add-one estimator, blind to k and beta, attains risk <=C_weak(C) H_2 uniformly over all M>=64, all beta<=C/M^2, all budgets 0<=k<=M, and arbitrary initial laws. The constant may depend on the fixed band bound C, not on M,beta,k. Thus every prescribed curve beta_M=O(M^-2) is all-budget adaptive.

### B. Every strictly intermediate curve is nonadaptive

Let beta_M be any prescribed curve satisfying

    M beta_M ->0,  M^2 beta_M ->infinity.             (1.1)

There is NO family of full-history estimators supplied beta_M and blind to k, with one finite constant (even allowed to depend on this entire fixed curve) attaining H_2(M,k,beta_M) for every k and M. Failure already occurs for stationary initialization.

A finite version holds for every M>=4096 and

    256/M^2 <=beta<=1/(16M),
    k=floor(beta^-1/2), T=floor(M/8).                (1.2)

At this ACTUAL supplied beta there is a stationary null and a common strict-k source-independent kernel such that any estimator map A_(M,beta) satisfies

    R_null >=[(3k/(2048M))log((T+1)/k)
                              -32 S log(2T/k)]_+,   (1.3)

where S is its worst clean risk over an explicitly identified stationary subfamily of D_2(beta). Moreover H_2(M,k,beta)<=2k/M. The source family and kernel are exactly those in accepted BK002 for this integer k; no new attack input beta is required.

### C. Sufficiently strong certificates admit all-budget adaptation

For every fixed c>0, ordinary corrupted-row add-one attains risk <=C_strong(c) H_2 uniformly over all beta>=c/sqrt(M), all budgets, and arbitrary starts. The estimator itself is blind to k and beta.

### What is not settled

These results do NOT determine all-budget FULL-HISTORY adaptation at beta≈1/M, nor throughout the remaining moving range between order M^-1 and M^-1/2. BK001 gives a histogram-plus-initial/final-PAIR obstruction at beta=1/M, not a full-history obstruction there. BK002's general uniform-in-beta impossibility must not be reinterpreted as failure at every fixed curve.

## 2. Generic add-one interfaces and weak-band proof

Let J be the clean total departure count of the preserved terminal row. Count stability gives, pathwise,

    TV(addone_corrupted,addone_clean)
       <=min(1,6k/(J+2)).                           (2.1)

This is the generic normalization argument from SC002 §1, valid for K=2 as an upper bound. The accepted binary clean comparator is at most 8192sqrt(32)/sqrt(M+1)<=2^16 s. The universal four-state occupation/layer-cake interface gives

    E min(1,6k/(J+2))<=Psi(96k/(M+1)),               (2.2)

where Psi(v)=v[1+log(1/v)] for 0<v<1, Psi(v)=1 for v>=1, and Psi(0)=0. Thus, for k>=1,

    R_add<=min{1,2^16 s+96 F_0},
    F_0=(k/M)[1+log(1+M/k)].                        (2.3)

The scalar bound follows by splitting M/k below or above96, exactly as in the accepted universal corruption bound. At k=0 omit this term and use the clean comparator; no singular expression is evaluated. These bounds hold for arbitrary starts and every admissible attack.

Fix the weak-band constant C and put D=max(1,sqrt(C)). If beta<=C/M^2, then e_beta<=D/M. For z=M/k and D>=1,

    1+log(1+z)
       <=1+log D+log(1+z/D)
       <=(1+log D)[1+log(1+z/D)].                  (2.4)

Here 1+z<=D(1+z/D), and the bracket in the last line is at least one. Since F_2>=epsilon[1+log(1+z/D)], (2.4) gives F_0<=(1+log D)F_2. Consequently

    R_add<=min{1,2^16 s+96(1+log D)F_2}
          <=[2^16+96(1+log D)]H_2.                 (2.5)

This proves A. If an O(M^-2) bound only holds eventually, the finitely many earlier M values can be absorbed into a finite risk constant: H_2>=M^-1/2 and loss<=1. The algorithm does not change.

## 3. Exact rounding and class inclusion for the intermediate band

Assume (1.2), put delta=sqrt(beta), and set k=floor(1/delta). Then

    16/M<=delta<=1/(4sqrt(M))<=1/4,
    k delta<=1,
    k delta>=1-delta>=3/4.                          (3.1)

Also

    k<=1/delta<=M/16,
    k>=4sqrt(M)-1>=2sqrt(M),                        (3.2)

so k<=floor(M/8) and k^2>=4M. Thus the exact finite domain of accepted BK002 is satisfied, including integer floors. The interval in (1.2) is nonempty only once M>=4096, as stated.

Because k<=1/delta,

    beta=delta^2<=1/k^2.                            (3.3)

Every stationary clean source Q_a used by BK002 at this k belongs to D_2(1/k^2), and therefore also to D_2(beta). The null has certificate1/M, also at least the supplied beta. The family is explicitly

    a in [k/(32T),1/16], b=1/k, e=1-1/k, t=1/(4M),
    Pi=x(e/a,1,1,b/t), x=(e/a+2+b/t)^-1.

The protected kernel is precisely BK002's common map C_(M,k), depending only on M,k and the input history; it has no extra runtime beta or unknown-source parameter port.

BK002's finite constrained-risk inequality is valid for ANY fixed map on the full word. Apply it to the map z->A_(M,beta)(z). Formally it could be named A_tilde_(M,1/k^2)(z)=A_(M,beta)(z) for the purpose of applying that theorem, but this does NOT change the algorithm's supplied beta or pretend that beta equals1/k^2. The source inclusion (3.3) is what licenses its clean risk guarantee. The same map is used in the clean and corrupted experiments, both at the actual supplied beta.

This gives (1.3), where S is the clean supremum over the displayed subfamily. It is not an exchange of distinct public metadata values within one risk guarantee.

Finally, delta>=16/M implies e_beta=delta. With (3.1),

    F_2=epsilon[1+log(1+1/(k delta))]
       <=epsilon[1+log(7/3)]<2epsilon.              (3.4)

The final strict inequality follows from 7/3<exp(1). Equation (3.2) gives s<=epsilon/2. Hence H_2<=2epsilon, including the cap. This establishes the entire finite assertion.

## 4. Impossibility on every strictly intermediate curve

Suppose a family on a fixed curve satisfying (1.1) attained risk<=C_curve H_2 for every actual budget. Eventually that curve lies in the finite band (1.2). Choose its prescribed k_M=floor(beta_M^-1/2). Then

    k_M/sqrt(M) >=(3/4)/sqrt(M beta_M)->infinity,
    M/k_M >=M sqrt(beta_M)->infinity.               (4.1)

The clean k=0 guarantee at the SAME supplied beta_M gives S<=C_curve/sqrt(M) on the BK002 subfamily, by class inclusion. The error-to-positive ratio in (1.3) is bounded by

    (65536 C_curve/3)(sqrt(M)/k_M)
       log(2T/k_M)/log((T+1)/k_M),                  (4.2)

which tends to zero. The log ratio tends to one because its numerator and denominator differ by a bounded quantity and M/k_M tends to infinity. Thus the actual risk is eventually bounded below by a fixed positive multiple of

    (k_M/M)log(M/k_M),

whereas its benchmark is at most2k_M/M. Their ratio diverges. This contradicts any finite C_curve, even though the algorithm may know the entire fixed curve and beta_M at each M. Stationary witnesses suffice; the arbitrary-start class is larger. The same conclusion holds if these two limits occur only along a subsequence.

This argument changes neither BK002's accepted source family nor its proof. It extends its interpretation to non-square real certificate values by exact rounding and monotonicity of the source classes.

## 5. Strong-band proof and its exact inherited scope

The generic ordinary-add-one upper proved in SC002 §§1–2 has, at K=2,

    R_add<=min{1,2^16 s+2^12 F_gen},
    F_gen=epsilon[1+log(1+1/(k max(beta,1/M)))]       (5.1)

for k>=1, with F_gen=0 at k=0. The loose powers of two dominate its exact constants: 8192*2^(5/2)<2^16 and 48(17+log80)+960<2^12.

SC002's matching theorem statement is restricted to K>=3, but its upper proof uses count stability, clean prediction, pair-state occupation and the all-state suffix-mixture argument, all valid at K=2. Its three-symbol restriction is needed for the matching lower construction, not these upper steps. This upper-interface use was explicitly checked in the fresh BK002 review and separately documented in BK002_FIXED_POSITIVE_BETA_PROVENANCE.md. We are not relabeling SC002's full nonbinary theorem as binary.

If beta>=c/sqrt(M), then log(1+u)<=u gives

    F_gen<=epsilon+1/[M max(beta,1/M)]
           <=epsilon+s/c.                          (5.2)

At k=0 the asserted upper is immediate from the clean branch without evaluating a singular logarithm. Therefore

    R_add<=min{1,(2^16+2^12/c)s+2^12 epsilon}
          <=(2^16+2^12+2^12/c)H_2,                 (5.3)

because H_2 dominates min{1,max(s,epsilon)} and the coefficient is at least one. This proves C with a constant depending only on the fixed band lower bound c.

## 6. Power-law summary, not a complete classification

For the prescribed curves beta_M=M^(-gamma), the proved regions are:

| Exponent gamma | All-budget full-history adaptation established here |
|---|---|
| 0<=gamma<=1/2 | Possible, by ordinary add-one; constants uniform in M,k. |
| 1/2<gamma<=1 | Not settled by this note. At gamma=1, histogram-only impossibility is known from BK001, not full-history impossibility. |
| 1<gamma<2 | Impossible, even with supplied beta and stationary initialization. |
| gamma>=2 | Possible, by ordinary add-one/profile comparison. |

For fixed multiplicative constants in these curves, the same conclusions in the open exponent intervals and the two proved endpoint bands hold with constants allowed to depend on those fixed multipliers. The gamma=1 boundary is intentionally not classified. The nonmonotone-looking diagram concerns adaptation to the KNOWN-k rate, which itself becomes larger in the weakest certificate regime; it is not a claim that observing a less-mixing source makes estimation intrinsically easier.

No pointwise impossibility at every positive budget follows. The negative statement requires simultaneous clean accuracy and robustness across all budgets. No efficient/causal attacker, visible mask/seed, edited endpoint, neural-resource, training, external novelty or formal-verification claim is made.
