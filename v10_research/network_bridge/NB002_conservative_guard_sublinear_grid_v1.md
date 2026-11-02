# NB002 — Conservative approximate guard: beta-blind prediction without exact count recovery

2026-11-02. New author candidate, not yet independently reviewed. NB001 remains frozen. This is a new suffix and an explicitly proved extension of the **frequency prefix** to coarser grids; it is not an assertion that the original complete SRC-Pi program is legal below its old h_0(M).

## Theorem and significance

Fix integers K≥2, M≥1, N=M+2 and any integer h≥4. Set Q=2^h,

    ell=ceil(log2(M+K+4)), p=4h+4ell+64.

There is one finite deterministic causal-attention/Boolean-ReLU batch-hybrid predictor B_(K,M,h), independent of beta and the source, with the original six-head frequency front end and an explicitly charged changed suffix. For every beta∈[0,1], uniformly over every source in the full R011 class D2(beta), with arbitrary initial pair law,

    risk(B_(K,M,h);beta)
      ≤ min(1, 2^16 L + 7 Ψ(76K^5/Q) + 9K/Q),             (T1)

where Ψ(0)=0, Ψ(x)=x(1+ln(1/x)) for 0<x<1, Ψ(x)=1 for x≥1, and L is **exactly** R011's all-parameter minimax scale. The loss is same-history actual-terminal expected TV. Only the observed M+2 symbols, public K,M,h and the paid exact endpoint bits are available.

The hybrid depth O(Kp²), width O(Kp), six heads (at most four per layer), maximum QK dimension 2K, score cap 2, and full asymptotic SRC ledger remain valid, with changed constants. Full costs and a separate PURE neural expansion are stated below.

An entirely integer public precision choice is

    n=M+1, u=ceil(log2 n), v=ceil(log2 K),
    h_public=20+5v+ceil(u/2)+ceil(log2(u+1)).               (T2)

For this ONE choice, independent of beta,

    risk(B_(K,M,h_public);beta)
       ≤min(1,(2^16+1/128)L),
    risk(B;beta)/R(K,M,beta) < 2^34.                     (T3)

For fixed K and M→∞,

    h_public=(1/2)log2 M+log2 log2 M+O_K(1),
    Q=Theta_K(sqrt(M) log M)=o(M).

Thus exact count recovery at Q=Omega(M) is **not necessary as a sufficient implementation strategy** for beta-blind constant-order minimax prediction. This does not prove minimum necessary precision. It reduces the statistical master/output grid requirement; total arithmetic word p still includes ell=Theta(log M), and all full resource costs remain charged. There is no demonstrated computational advantage over paid direct counting, no training claim, and no external novelty claim.

## 1. Sources and inherited statistical interfaces

The source roots and precise versions are bound in the adjacent source manifest. The proof uses:

- Full R011 proof/review and editorial notes. Its all-parameter scale and minimax lower are inherited, not reproved. Its long-weak-beta proof explicitly retains **event radius certificates**, not only a scalar risk bound.
- Full SRC-Pi deterministic fact `fef8372728290b45.md`, particularly §§2–7 and §9. Its finite frequency construction is rechecked below at the newly asserted h-domain.
- G/U fact `a12539a93d9f1ee3.md`, §11.1, for the arbitrary-start terminal-visit bound

      P(J<w)≤min(1,K^4 w/(M+1)), integers w≥1.            (UC)

  Its proof uses homogeneous suffix domination, first-w occurrence charging over K² pair states, and max≤sum over K² starts. No stationary or independent-query premise is added.
- Actual recovered S024 §§5–7: stationary and burned-suffix **radius** bounds, including the strong-beta radius needed here; actual S025 §§6–8: count-tail CT, active-g tail GT, pooled risk and rejection-restricted SEL. The known false unconditional NEXT is never used. These bodies are in `v10_research/intake/statistical_dependencies/` with R001.
- Full R001 §5's event-radius lemma, together with R011's explicitly assembled long-history certificates. Exact-count snapping from NB001 and the historical stage-2 root is **not** used in this algorithm.

Notation: C_c is the actual queried-row count over departures t=3,…,N; J=sum C_c; H_c is the count of x_t=c over the same M successors. At output query s=(x_(N−1),x_N),

    A=J+K, B=M+K,
    q_c=(C_c+1)/A, b_c=(H_c+1)/B,
    g=min(1,sqrt(K^5/(M+1))),
    rho=min(g,64sqrt(K/A)).

Original ALG pools exactly when d=TV(q,b)≤rho. q,b,J and source parameters in this definition are mathematical comparison objects, not supplied suffix inputs.

## 2. Proved extension of the frequency prefix to every h≥4

Use the actual SRC formulas with p=4h+4ell+64: the two paid singleton heads copy preceding symbols and actual endpoint; the other four heads are P1,P2,T,0 with the same causal masks, local bit values, query one-hots, rational L2/L3 constants, and finite integer exponential recurrence. The synthetic token has no future symbol. All n_tok=M+3 positions and their pointwise computations are charged, while only the final position emits the requested prediction.

The old full-program lower h≥ceil(log2 M)+1 was used to make

    r0=2^(−ceil(log2 M)−1)

a positive representable grid number in the **old downstream smoothing stage**. Our program stops that computation at the clipped recovered frequencies a_c, never forms r0, and replaces all later stages. We now verify the retained prefix without that lower bound:

1. Finite log constants are generated by the rational series in SRC §4 with p terms and then rounded to p fractional bits. The errors are less than 2·2^(−p). Scores are sums of at most two selected constants, remain in [0,2], and have error at most 4·2^(−p), regardless of M or Q/M.
2. The 8p-term integer recurrence retains full products and divides by positive j·2^p. Its proved exponential weight error is at most 100p·2^(−p). Exact accumulators over m≤n_tok keys have enough integer bits because ell includes log M. Each head returns floor(Q A_head/D_head)/Q; it is a closed h-grid coordinate and has absolute error ≤2/Q. Indeed p≥4h+64≥80, so the same inequality 200p·2^(−p)≤2^(−h) applies. Nothing here requires Q≥M.
3. Closed-grid bit extraction uses h+1 numerator bits, valid also at coordinate one. The denominators 2Q−U for d1,d2 lie in [Q,2Q]. Directed products and divisions use complete integers followed by exact quotient, with truncation at most 1/Q. The safe scalar ranges d1∈[1,4], d2∈[1,6], dT∈[1,2], and recovered signed frequency in [−8,9] are independent of Q/M. All endpoint corrections are retained.
4. Applying SRC's explicit error ledger with eta=2/Q,zeta=1/Q gives

       a_c∈[0,1]∩Q^(−1)Z,
       |a_c−C_c/M|≤76/Q.                                 (1)

   The 35eta+6zeta derivation precedes r0 and remains valid on this enlarged h-domain. Clipping is nonexpansive.
5. At the same unchanged master cut, the ideal uniform-head coordinates obey nu_c−f_c+rho_head·E_c=H_c/M, where E_c=1{x_N=c} is the paid exact endpoint bit. Form

       y_c=clip_[0,1](hat nu_c−hat f_c+hat rho_head E_c).

   Signed grid addition and bit multiplication are exact, so

       y_c∈[0,1]∩Q^(−1)Z, |y_c−H_c/M|≤6/Q.               (2)

   rho_head=1/M is distinct from the selector radius rho. At coarse Q the finite rho_head may be zero; (2), not a false exact-boundary assertion, is what is used.

The prefix's accumulators, masks, histories and unused projections have the same paid lifecycle as SRC and are released before the suffix's master cut. There is no reread port, clean duplicate output or supplied counts. The above proof establishes a new frequency-prefix domain h≥4; it does not silently extend SRC's old positive-V construction or its reliability facts.

## 3. Actual approximate probability vectors and observable error envelope

Define positive real comparison-to-computation weights

    u_c=M a_c+1, v_c=M y_c+1,
    Ahat=sum_c u_c, Bhat=sum_c v_c.

These are exactly represented using integers. If A_c=Q a_c, Y_c=Q y_c,

    U_c=M A_c+Q, V_c=M Y_c+Q,
    Dq=sum U_c, Db=sum V_c,
    Ahat=Dq/Q, Bhat=Db/Q.

No nearest-integer count snapping is performed. Every U_c,V_c≥Q, so both denominators are positive on all canonical grids and at every token position.

Use ordered Q-grid normalization independently for U and V: floor the first K−1 Q·weight/total quotients and place the exact residual in coordinate K−1. Call the resulting simplex vectors qhat,bhat. This is exact integer division and produces nonnegative words summing to Q on every input. The same rounding calculation as SRC gives TV error ≤(K−1)/Q from each normalized positive vector.

Put k=K/Q and E=76KM/Q. The normalized-vector inequality

    TV(u/sum u, w/sum w)≤||u−w||_1/(sum w)

for positive vectors, applied to w=C+1 or H+1, yields

    Delta_q:=TV(qhat,q)≤min(1,E/A)+k,
    Delta_b:=TV(bhat,b)≤7k.                               (3)

For the second bound use 6KM/[Q(M+K)]≤6k and the rounding cost≤k. No conditional IID argument appears in (1)–(3).

Also |Ahat−A|≤E. Define the **observable** conservative denominator and error allowance

    Aminus=max(K,Ahat−E),
    eobs=min(1,E/Aminus)+8k.                              (4)

Then K≤Aminus≤A and Aminus≥A−2E. Consequently eobs≥Delta_q+Delta_b. It is harmless if eobs>1; it is not represented as a probability.

Set

    rhominus=min(g,64sqrt(K/Aminus)), dhat=TV(qhat,bhat).

The new rule pools (returns bhat) when

    dhat≤min(1,rhominus+eobs),                            (5)

and otherwise returns qhat. Ties pool. All quantities in (4)–(5) are computable solely from the old finite master words and public inputs. Section 8 eliminates the displayed square roots with exact integer comparisons.

## 4. Monotone rejection — the key replacement for exact ALG equality

Because Aminus≤A, rhominus≥rho. By (3),

    dhat≤d+Delta_q+Delta_b≤d+eobs.

If the original ALG pools, d≤rho, so dhat≤rhominus+eobs; since dhat≤1, (5) pools as well. Thus pointwise on every observed history,

    {new rejects pooling} ⊆ {original ALG rejects pooling}. (6)

We do not assert that new and old decisions agree, or that the new output is uniformly close to ALG. Extra pooling is permitted and must be analyzed. In particular an approximate scalar threshold by itself would not justify branch replacement; the direction of (6) is the structural safeguard.

## 5. Occupancy control of numerical amplification

Write

    v_err=min(1,E/A), Cbad={A<4E}, c=K^4/(M+1).

On Cbad's complement, Aminus≥A/2, whence

    min(1,E/Aminus)≤2v_err,
    rhominus≤sqrt(2)rho≤2rho.

Write e=TV(q,theta_(Y_M)). If new selects qhat, its loss is at most e+Delta_q. If it selects bhat, triangle inequality and (5) give loss≤e+Delta_q+rhominus+eobs. Therefore on Cbad's complement loss≤e+2rho+3v_err+9k. On Cbad use the actual simplex loss cap one. Combining gives the universal pointwise inequality

    loss_new≤e+2rho+3v_err+9k+1_Cbad.                    (7)

This use of the loss cap is why only one bad-event term is needed.

We derive both numerical expectations directly from integer UC. For 0<t<1,

    {v_err>t}={J<E/t−K}.

If the right threshold is nonpositive the event is empty. Otherwise set w=ceil(E/t−K)≥1. Since J is integer the event is exactly {J<w}, and w≤E/t−K+1≤E/t. Hence P(v_err>t)≤min(1,cE/t). Layer cake gives

    E v_err≤Ψ(cE).                                      (8)

For Cbad the event is empty if 4E≤K. Otherwise w=ceil(4E−K)≥1 and w≤4E, so

    P(Cbad)≤min(1,4cE)≤4Ψ(cE).                           (9)

No unsupported UC statement at noninteger thresholds is used. Both inequalities hold for all E>0; no E≥1 assumption is needed. Finally

    cE=76K^5 M/[Q(M+1)]≤76K^5/Q.                        (10)

Taking expectations in (7) and using (8)–(10) bounds the additional implementation cost by 7Ψ(76K^5/Q)+9k whenever E[e+2rho] is controlled at scale L.

## 6. All-parameter statistical cases: radius certificates are retained

The following is a composition of inherited exact interfaces, not a reopening of the closed statistical problem. It records why scalar R011 risk alone would not have sufficed.

### 6.1 beta=0

The inherited general row risk is E e≤48g, and rho≤g pointwise. R011 has L=g here, so E[e+2rho]≤50L. Equations (7)–(10) prove (T1) with room to spare.

### 6.2 0<beta≤1/2, M≥K^4

Use R011 §3's same compatible event cover and certificates, writing A_R,B_R,C_R to avoid confusion with count denominator A:

    E e≤A_R+B_R+C_R,
    E rho≤A_R+(8/5)(B_R+C_R),
    A_R+B_R+C_R≤6761a+96D+512T≤7369H.

The second line is the actual R001 event-radius inequality applied to the very certificates assembled in R011, including the grouped success radius sum; it is not inferred from E e alone. Thus

    E[e+2rho]≤3A_R+(21/5)(B_R+C_R)
                ≤(21/5)7369H.

R011's weak-beta comparison is H≤2L. Numerically (42/5)7369=61899.6<65536=2^16. This proves the baseline required in (T1), without a horizon upper bound or moderate-log restriction.

### 6.3 0<beta≤1/2, M≤K^4

Let H_S=max(a,(1−beta)^(M/2)). S024 §7 proves the **count** bound

    E sqrt(K/(J+K))≤21H_S,

and S019's inherited original-row bound, explicitly used there, is E e≤128H_S. Therefore E[e+2rho]≤(128+128·21)H_S=2816H_S. R011 §4 proves H_S≤2H≤4L on this strip, including all small M and both parities. The baseline is at most11264L<2^16L. The overlap M=K^4 is harmless.

### 6.4 beta≥1/2 and delta=1−beta>a

R011 has L=F=a in this regime. S024 §6 uses a paid-for-analysis suffix burn b0=floor(M/2), condition B and stationary terminal occupancy to prove

    E sqrt(K/(J+K))≤4a

for M≥32; it does not replace the actual estimator by a suffix. It also gives E e≤81a there. For M<32, a≥1/2 and the unit caps give E e≤2a and E rho≤2a. Thus uniformly E e≤81a and E rho≤256a, so E[e+2rho]≤593a≤2^16L. No invalid inference from scalar ALG risk to a radius bound has been made.

### 6.5 beta≥1/2 and delta≤a, including beta=1

Here L=F=max(i,delta), where i=min(1,sqrt(K/(M+1))). A radius safety inequality would lose the distinction between a and i, so we instead use (6).

Let f=TV(b,theta_(Y_M)), t=64sqrt(K/A). By S025's deterministic rejection argument, now restricted to the subset (6),

    loss_new
      ≤ f + e 1{e>t/2} + 1{g<1}e 1{e>g/2}
          +Delta_q+Delta_b.                             (11)

To verify directly: on new pooling, loss≤f+Delta_b. On new rejection with e≤f, loss≤f+Delta_q. Otherwise e>f and original rejection holds; d≤e+f<2e. Therefore rejection requires d>t or d>g, the latter impossible at g=1 because d≤1. At least one displayed tail then contains e. This proof preserves equality conventions and introduces no false unconditional tail.

S025 §§6–8 prove CT≤870delta+316i, GT≤436delta+3540i **only when g<1**, and E f≤2delta+(3/2)i, giving the sum≤4000(delta+i)≤8000L for M≥5,n>K. If n≤K, i=1 and the loss cap proves (T1) immediately; if M≤4 then i>1/2 and the cap does so as well. Thus all endpoints and finite small cases are included. By (3),(8), E(Delta_q+Delta_b)≤Ψ(cE)+8k, which is bounded by the surcharge in (T1).

These cases exhaust beta∈[0,1] and every K,M. A fixed algorithm was analyzed in different regimes; beta never enters the program. Taking the independent loss cap proves (T1).

## 7. Explicit sublinear-grid configuration

Take (T2). Since 2^v≥K and 2^u≥n,

    Q≥2^20 K^5 sqrt(n)(u+1).

Put x=76K^5/Q. Since 76<128,

    x≤2^(−13)/[sqrt(n)(u+1)] =: y <1.

The function Ψ is nondecreasing. For u≥1, ln n≤u, ln(u+1)≤u and 1+13ln2≤14, so

    1+ln(1/y)
       =1+13ln2+(1/2)ln n+ln(u+1)
       ≤14+(3/2)u≤8(u+1).

Consequently

    Ψ(x)≤Ψ(y)≤1/[1024 sqrt(n)]≤i/1024.

Also K/Q≤1/[2^20 sqrt(n)]≤i/2^20. Hence

    7Ψ(x)+9K/Q≤(7/1024+9/2^20)i < i/128≤L/128.

This proves (T3), using R011's lower R≥2^(−17)L for the ratio. Computing u,v and the ceilings in (T2) is a bounded integer bitlength operation on public parameters; no real logarithm or square-root oracle enters offline generation. The sufficient schedule is intentionally conservative and makes no optimal-constant claim.

At fixed K the dyadic ceiling choices bound Q above and below by constant multiples of sqrt(n)(1+log n), proving Q=o(M) and the stated h asymptotics. Only master/output grid precision is reduced in this sense. The number of integer accumulator bits still grows with M through ell, and p=Theta(log M) remains. Because (T2) has deliberately large constants, it may exceed the exact-count grid schedule for many practical finite horizons; the asymptotic conclusion does not imply pointwise finite-size savings or a smaller exact implementation ledger.

### 7.1 Separate output-grid necessity, not an internal-master lower bound

For any Q≥1, every predictor whose output coordinates are integer multiples of 1/Q, even one with unrestricted full-history computation and source-independent randomization, has worst risk on every D2(beta) at least

    (1/8)min(1,K/Q).                                     (QLOW)

Here is the complete elementary witness. Put r=min(K−1,Q). Choose an IID all-row table p with r coordinates equal to 1/(2Q), one further coordinate equal to 1−r/(2Q), and all remaining coordinates zero. The residual is at least 1/2, so p is a legal probability vector. Take the initial pair from p tensor p. Its pair chain has P²(s,t)=pi(t), pi=p tensor p, for every pair s,t including off support, hence this source belongs to D2(beta) for every beta. For every possible grid output v, each of those r half-grid coordinates differs from p by at least 1/(2Q). Thus TV(v,p)≥r/(4Q), pointwise regardless of the data or random seed. Since K≥2, r≥min(K,Q)/2, proving (QLOW).

The iid witness may depend on K,Q, as a finite-parameter supremum permits. Its conclusion is valid even if p were known; it is purely a representation obstruction. Combining by maximum with the separately witnessed R011 statistical lower gives grid-constrained minimax risk

    R_grid(K,M,beta,Q)
       ≥max(2^(−17)L,(1/8)min(1,K/Q)).                    (QSTAT)

The two terms are not added as if witnessed by the same source. At beta=1, L=i. In the noncapped IID regime M+1>K, if an algorithm promises risk≤C i and C i<1/8, (QLOW) forces

    Q≥K/(8C i)=sqrt(K(M+1))/(8C),
    h≥(1/2)log2(M+1)+(1/2)log2 K−log2(8C).

Therefore, at fixed K, the leading one-half log M **output-grid** bit exponent is necessary for constant-order IID risk, while (T2) suffices with only an additional log log M+O_K(1). The upper and lower do not settle the logarithmic gap or the K dependence. This basic quantization argument is not claimed novel, and it gives no lower bound on internal master precision if a different, finer output format is permitted.

## 8. Exact finite selector with no square-root oracle

All new operations use SRC's exact bit/ReLU arithmetic gadgets. Let Q-grid numerator vectors of qhat,bhat be m_c,r_c, with sums Q, and put

    D=sum_c |m_c−r_c|, E0=76KM,
    A0=max(KQ,Dq−E0), e0=min(A0,E0),
    Z=A0(D−16K)−2Q e0.                                  (12)

Then A0=Q Aminus>0, e0/A0=min(1,E/Aminus), and

    z:=dhat−eobs=Z/(2Q A0).

If Z≤0, pool. Otherwise z>0, and z≤1 follows from dhat≤1,eobs≥0. Thus the cap-one part of g imposes no extra condition. Formula (5) is exactly equivalent to the two integer comparisons

    (M+1)Z²≤4Q² A0² K^5,
    Z²≤16384 K Q³ A0.                                   (13)

Both sides are nonnegative; no approximate-root or real-comparison margin is required. Weak inequalities preserve all pooling ties. The decision bit muxes the already normalized numerator vectors m,r, followed by paid dyadic decode. Every path and all non-output token rows remain legal even when (1)–(2) do not describe a meaningful shorter experiment; positivity of U,V and actual-sum normalization ensure simplex output.

The retained prefix plus new suffix reads only the original masters, exact query/endpoint bits and public data. In particular Dq is computed from the actual approximate frequencies; the true A is never supplied. E0 is public, not a data-dependent oracle error estimate. All loops have public bounds; branching is realized by muxes, so circuit depth is input independent.

## 9. Words, full costs, and architectural scope

The two sets of positive integer weights satisfy Q≤U_c,V_c≤Q(M+1), with totals in [KQ,KQ(M+1)]. Each quotient dividend is at most Q²(M+1); no Q≥M or Q≥K assumption is needed. Let U=Q(M+K+2). All count-like factors K,M+1,Q are at most U. Then A0≤KQ(M+1)≤U³; e0≤A0; D≤2Q; |Z|≤20U^4. Consequently every square/product in (13), including their evaluation when the Z≤0 branch is ultimately selected, is bounded by a constant times U^13. At most 13(h+ell)+O(1) bits suffice, within the original 128p allowance. Full signed products, shifted division remainders and guard bits are retained. The prefix word proof uses ell for row accumulation and never Q≥M.

The additional normalization of two K-vectors and exact guard take O(K) arithmetic operations on O(p)-bit words. Serial school multiplication/restoring division uses O(p²) active gates and depth per operation, O(p) scratch. Retaining all masters, two normalized banks, weights and selector state costs O(Kp) logical bit channels. Explicit holds across serial stages cost O(K²p³). All cleared/released buffers and every copied/retained word are charged.

With n_tok=M+3, the full batch-hybrid construction has the following **upper bounds**, not measured emitter performance:

| Coordinate | Bound / property |
|---|---|
| Neural depth / width | O(Kp²) / O(Kp) |
| Heads total / max per layer; max QK dimension; score cap | 6 / 4; 2K; 2 |
| Online coefficient / arithmetic word | ≤128p bits, including full products and guards |
| Dense coefficient slots / bits | O(K³p⁴) / O(K³p⁵), zero slots and biases included |
| Active records / explicit holds | O(Kp²+K²) / O(K²p³) |
| Sparse addressed program incl coefficients/holds | O(K²p⁴) bits |
| Masks and positions | O(n_tok²+n_tok log(n_tok+1)) bits |
| Observed one-hot input | O(NK) bits; binary conversion/acquisition separately charged |
| Rolling scalar-neural work, excluding stored data | O(n_tok Kp²) bits |
| Uncached attention bitwork | O(n_tok²(K+p)p²) |
| Equally cached attention bitwork | O(n_tok²Kp²), plus cache creation/storage/selection |
| Dense all-token pointwise/QKV bitwork | O(n_tok K³p⁶) |
| Finite rational log work / scratch | O(p³log²(p+1)) / O(p log(p+1)) |
| Five full-score cache creation | O(p³) plus logs; not rounded-exponential products |
| Finite arithmetic evaluator code | O(p⁴) bits |

Offline charges include public bitlength/configuration computation; layouts, masks, positions; constants; all new normalizer/guard microcode; generation/addressing/sorting of every gate, term and hold; and actual chosen-format writes. For R_rec actual records, the same conservative O(R_rec p²) generation/sorting bitwork and O(R_rec p) scratch apply. Dense files additionally pay their true O(K³p⁵) coefficient-bit output including zeros. Public K^5 uses a fixed multiplication chain with charged O(p²) arithmetic, not a supplied irrational constant.

Total peak is the maximum of phase sums over all simultaneous program/parameters, input, masks/metadata, QKV/historical arrays, residuals, master/weight/normalized/output banks, controller/address words and scratch. A safe forward dense sum is O(K³p⁵+n_tok²+n_tok log(n_tok+1)+NK+n_tok Kp²), replacing only the stored-program term by O(K²p⁴) for sparse format. Offline scratch coexists with retained generated data when live. The rolling entry alone is not total peak. Packed-bit evaluation and scalar-neural O(p)-bit-per-channel storage are distinct conventions; all-token work is not discounted because only q is returned.

For a separate PURE expansion, let T_bit include **all** online bitops, control, movement, copies/clears and finite attention evaluation, and let S_bit include the simultaneous live work/input/mask/public data (plus program rails if interpreted). Instructionwise ReLU unrolling and explicit holds give depth O(T_bit+p), width O(S_bit+p), sparse gates/holds O((T_bit+p)(S_bit+p)), dense coefficient bits O(p(T_bit+p)(S_bit+p)^2), and generic dense bitwork O(p²(T_bit+p)(S_bit+p)^2). This is not assigned the smaller hybrid L,W. No theorem about arbitrary standard floating-point/LayerNorm Transformers or learning dynamics follows automatically.

## 10. What was and was not established

- Exact-count recovery is bypassed. The algorithm intentionally permits extra pooling and may differ from ALG even at clean finite inputs.
- The new load-bearing step is monotone rejection plus controlled observable inflation, allowing inherited actual-rejection tails near IID and inherited radius certificates elsewhere. Approximate q risk alone would not establish this theorem.
- Low h legality is proved for the frequency prefix and new suffix, not inherited from the old full SRC theorem outside its h-domain.
- The bound is nominal finite computation. Arbitrary physical faults, corrupted endpoint/query bits, or a new delta-noise claim require a separately stated theorem and charges. NB001's bounded-master result is not automatically copied here.
- O(sqrt M log M) Q at fixed K is a sufficient master/output grid schedule, not a lower bound, exact error-optimal schedule, or overall time/space separation. p and full masks/history costs remain.
- A paid direct-counting comparator still computes the desired statistical predictor without the huge batch dense cost. No network efficiency advantage or training attainability is claimed.
- Supplemental exact-integer diagnostics and independent review are tracked separately. This author candidate does not certify itself by its file existence or by a finite numerical pass.
