# SM001 — Strong mixing removes the logarithmic master-grid overhead for the unchanged NB002 predictor

2026-11-02. **Author candidate; independent review pending.** NB002's accepted files and its algorithm are unchanged. This is a new, more informative analysis of that exact finite predictor, not a new encoder, suffix, guard, or source-dependent choice.

## 0. Result and precise scope

Fix integers K≥2, M≥1, h≥4; write Q=2^h, N=M+2,

    ell=ceil(log2(M+K+4)), p=4h+4ell+64.

Let B_(K,M,h) be **exactly** NB002's finite six-head frequency-prefix/conservative-selector predictor. For every beta∈[1/2,1], uniformly over R011's full D2(beta) class with arbitrary initial pair law,

    risk(B_(K,M,h); beta)
      ≤ min(1, (2^16+8)L + 2^13 K^3/Q).                 (SM1)

Here L is precisely the inherited all-parameter minimax scale, and risk is expected TV to the true next-symbol law at the **actual terminal pair**, using the complete original observed history. The predictor does not read beta, pi, a regeneration label, a suffix count, or a class label.

In particular the entirely integer public schedule

    n=M+1, u=ceil(log2 n), v=ceil(log2 K),
    h_strong=20+3v+ceil(u/2)                            (SM2)

has, simultaneously for every beta∈[1/2,1],

    risk(B_(K,M,h_strong);beta)
      ≤ min(1,(2^16+8+1/128)L),
    risk(B;beta)/R(K,M,beta) < 2^34.                   (SM3)

At fixed K, h_strong=(1/2)log2 M+O_K(1) and Q=Theta_K(sqrt M). Thus the extra log log M bits in NB002's **all-beta uniform** schedule are unnecessary on the strongly mixing class for the *same* finite algorithm. Only the public precision configuration changes; its function of K,M remains beta-blind.

A further, explicitly nonuniform consequence holds for every fixed beta>0: the same schedule (SM2) has risk O_beta(L), with an explicit constant in §7. There is no uniform guarantee as beta decreases to zero. This distinction is compatible with PL001's weak-mixing fixed-master lower, whose positive beta extension vanishes with M.

The new proof supplies a dependence-safe reciprocal terminal-count bound using time reversal under stationarity, then transfers a bounded count functional from a deterministic suffix. It does **not** claim that the original row samples conditioned on their count or on their terminal query are IID.

## 1. Inherited experiment, scale, and exact algorithm

A homogeneous second-order source has alphabet {0,...,K−1}, row table theta, pair kernel

    P((a,b),(b,c))=theta_ab(c),

and an arbitrary initial pair law mu. Its D2(beta) certificate is an existential stationary probability pi on the K² pair states such that

    pi P=pi,   P²(s,t)≥beta pi(t) for every pair s,t,

including off-support starting states. All symbols X_1,...,X_(M+2) are observed; Y_j=(X_(j+1),X_(j+2)), 0≤j≤M. There are M departures. The query is Y_M and the target is theta_(Y_M). Put

    J=sum_(j=0)^(M−1) 1{Y_j=Y_M}, A=J+K, n=M+1,
    delta=1−beta,
    a=min(1,sqrt(K³/n)), i=min(1,sqrt(K/n)),
    g=min(1,sqrt(K⁵/n)), hstar=min(1,sqrt(K⁴/n)),
    F=max(i,min(delta,a)),
    D=delta^n g, T=delta^(M/2) hstar, L=max(F,D,T).

The positive exponents in D,T avoid 0^0. R011 gives R≥2^(−17)L and L≥i>0. For beta≥1/2 it gives L=F.

For clarity, the exact finite map retained from NB002 is as follows. Its original master bank and exact endpoint/query bits recover Q-grid frequencies a_c,y_c with

    |a_c−C_c/M|≤76/Q,  |y_c−H_c/M|≤6/Q.

Here C_c is the complete-history queried-row successor count and H_c is the pooled count over X_3,...,X_(M+2). These are comparison objects, not supplied exact inputs. Form positive integer weights

    U_c=M(Q a_c)+Q, V_c=M(Q y_c)+Q,
    Dq=sum U_c, Db=sum V_c.

Normalize each bank by exact ordered Q-grid quotient/residual normalization to produce simplex vectors qhat,bhat. With E0=76KM, their integer numerators m_c,r_c define

    Dhat=sum_c |m_c−r_c|,
    A0=max(KQ,Dq−E0), e0=min(A0,E0),
    Z=A0(Dhat−16K)−2Qe0.

Pool and return bhat if Z≤0. If Z>0, pool exactly when **both**

    (M+1)Z²≤4Q² A0² K⁵,
    Z²≤16384 K Q³ A0.

Otherwise return qhat. All ties pool. This is NB002's existing exact integer guard, not an approximation to a square root. Its unchanged finite implementation is legal at every h≥4. No operation in this definition uses beta or any of the analytical objects introduced below.

## 2. The inherited reduction that is actually needed

Let q be the exact queried-row add-one vector and b the exact pooled add-one vector. Write

    rho=min(g,64sqrt(K/(J+K))),
    e=TV(q,theta_(Y_M)), f=TV(b,theta_(Y_M)),
    k=K/Q, E=76KM/Q,
    v_err=min(1,E/(J+K)), Cbad={J+K<4E}.

NB002 §§3–6, checked in its accepted independent review, establish the following pathwise interfaces:

1. Delta_q=TV(qhat,q)≤v_err+k and Delta_b=TV(bhat,b)≤7k.
2. New rejection is a subset of original ALG rejection, including equality conventions.
3. The universal safety bound is

       loss_B ≤ e+2rho+3v_err+9k+1_Cbad.                (2.1)

4. In the near-IID branch beta≥1/2, delta≤a, monotone rejection instead gives

       loss_B ≤ f+e 1{e>32sqrt(K/(J+K))}
                   +1{g<1}e 1{e>g/2}+Delta_q+Delta_b. (2.2)

The second term with threshold g is present **only** when g<1. The false unconditional NEXT statement from S024 is not used.

The load-bearing inherited statistical baselines are not inferred from scalar ALG risk. NB002 proves E(e+2rho)≤2^16 L in every case where (2.1) is used, using the actual S024/R001 count-radius certificates. In the near-IID branch, S025's CT, active-GT and pooled estimates bound the first three terms of (2.2) by 8000L, when M≥5,n>K. For the remaining finite cases the loss cap proves the desired result because i>1/2 or i=1. The extra error in (2.2) is at most v_err+8k, hence at most 3v_err+9k+1_Cbad.

Consequently, for every beta∈[0,1], the **same** predictor obeys the common pre-integration reduction

    risk(B;beta)
      ≤ min(1,2^16 L+3 E_mu v_err+P_mu(Cbad)+9k).       (2.3)

This is obtained from the pointwise interfaces and their actual case-specific baselines, not by manipulating NB002's final Psi surcharge or by inferring a radius bound from a scalar risk bound. We replace only its subsequent occupancy integration.

## 3. Stationary reverse-skeleton reciprocal lemma

**Lemma 1.** Let a finite stationary Markov chain have state set of size d0, stationary law pi, and P²(s,t)≥beta pi(t), with 0<beta≤1. For an ordinary stationary path Y_0,...,Y_L of length L≥0 define

    J_L=sum_(j=0)^(L−1)1{Y_j=Y_L}, m=floor(L/2).

Let d=|supp(pi)|≤d0. For any integer K≥1,

    E_pi[1/(J_L+K)] ≤ d/[(m+1)beta].                  (3.1)

The trivial upper 1/K may also be taken. In the present pair experiment d0=K².

**Proof.** Write S=supp(pi). For t∉S, stationarity gives

    0=pi(t)=sum_s pi(s)P(s,t).

Nonnegativity implies P(s,t)=0 for every s∈S; S is closed. On S define

    P*(t,u)=pi(u)P(u,t)/pi(t).

Its rows sum to one by stationarity; pi is stationary for P*. For any finite path in S, telescoping pi ratios shows that its forward stationary path probability equals its reversed stationary path probability. Thus, conditional on Y_L=s∈S, the reversed sequence Y_L,Y_(L−1),...,Y_0 is a Markov path with kernel P* started at s. This statement conditions on the terminal state of a stationary path; it does not assert a conditional IID law for its original transitions.

For t,u∈S, closure of S and direct multiplication give

    (P*)²(t,u)
       =sum_(v∈S) [pi(v)P(v,t)/pi(t)]
                      [pi(u)P(u,v)/pi(v)]
       =pi(u)P²(u,t)/pi(t)
       ≥beta pi(u).                                  (3.2)

There is no division by a zero stationary probability: every denominator is indexed in S. No reverse kernel on zero-mass states is needed.

For beta<1 define the stochastic residual on S

    R*(t,u)=((P*)²(t,u)−beta pi(u))/(1−beta).

Generate the conditional even reverse skeleton from s by m steps. At step j, take independent B_j~Bernoulli(beta) and W_j~pi, independent across j and of all previous randomness. If B_j=1 put the new skeleton state equal to W_j; otherwise draw it from R* at the current state, using additional independent randomization. This exactly realizes kernel (P*)². At beta=1 simply take B_j=1 always and draw W_j~pi; no residual division is formed.

For each j=1,...,m, the skeleton state is Y_(L−2j), a valid departure index in {0,...,L−1}. Whenever B_j=1 and W_j=s it is a counted visit to s. Consequently, conditional on Y_L=s, the law of J_L admits a coupling with

    J_L≥V_s,  V_s=sum_(j=1)^m B_j1{W_j=s}
                     ~Binomial(m,beta pi(s)).          (3.3)

The independent objects in (3.3) are only the constructed regeneration hits in the reversed skeleton. The actual full count need not be binomial, the odd reverse states need not be independent, and the observed row successors are not declared IID.

For V~Binomial(m,z) with z>0,

    E[1/(V+K)]≤E[1/(V+1)]
       =integral_0^1 (1−z+zt)^m dt
       =[1−(1−z)^(m+1)]/[(m+1)z]
       ≤1/[(m+1)z].                                  (3.4)

This includes m=0. Apply decreasing monotonicity to (3.3), then (3.4) with z=beta pi(s)>0. Weight by P(Y_L=s)=pi(s) and sum over S. The stationary masses cancel exactly:

    E_pi[1/(J_L+K)]
       ≤sum_(s∈S) pi(s)/[(m+1)beta pi(s)]
       =d/[(m+1)beta].

This proves (3.1). ∎

## 4. Arbitrary starts: a bounded functional of the whole suffix

Fix b=floor(M/2), L_suf=M−b=ceil(M/2), and m=floor(L_suf/2). Define the suffix count, with the *same actual query*, by

    J_suf=sum_(j=b)^(M−1)1{Y_j=Y_M}.

Pathwise, J≥J_suf. The suffix law is the ordinary P-path from initial law mu P^b; it includes its terminal pair, not an independent query.

Put r=floor(b/2)=floor(M/4) and define

    epsilon_beta(M)=1                         if r=0,
                    (1−beta)^r               if r≥1.   (4.1)

In particular epsilon_1(M)=0 when M≥4 and equals one when M<4. No 0^0 convention is used.

The all-state minorization gives

    TV(mu P^b,pi)≤epsilon_beta(M).                     (4.2)

For 0<beta<1 this follows by writing P²=beta Pi+(1−beta)R, where Pi has every row pi. The residual R is stochastic and pi R=pi; therefore each two-step block contracts TV by at most 1−beta. An optional final P step cannot increase TV. At beta=1, P²=Pi, so stationarity is exact after two steps; before then the unit TV bound applies. This proof uses minorization at off-support starts, as required by the original class.

Applying the same path-extension kernel to mu P^b and pi shows that the TV distance of their **complete suffix-path laws** is also at most epsilon_beta(M). Hence expectations of any measurable suffix-path function valued in [0,1] differ by at most that amount. This applies even when its definition uses the terminal pair, so no endpoint independence is required.

Since v_err is decreasing in J and bounded by one, Lemma 1 gives

    E_mu v_err
      ≤ E_pi min(1,E/(J_Lsuf+K))+epsilon_beta(M)
      ≤ E K²/[(m+1)beta]+epsilon_beta(M).

Here E is a public deterministic scalar, not an expectation symbol. To avoid any ambiguity, substituting E=76KM/Q yields

    E_mu v_err
      ≤ 76 K³ M/[Q(m+1)beta]+epsilon_beta(M)
      ≤ 304 K³/(beta Q)+epsilon_beta(M).              (4.3)

Indeed m+1≥(L_suf+1)/2≥(M+2)/4, hence M/(m+1)≤4 for every M≥1 and both parities.

Likewise {J+K<4E} is contained in {J_suf+K<4E}. Its indicator is a bounded suffix functional, and pointwise

    1{J_suf+K<4E}≤4E/(J_suf+K).

Therefore

    P_mu(Cbad)≤1216 K³/(beta Q)+epsilon_beta(M).        (4.4)

There is **one** TV charge for this indicator, not a multiplication of the TV error by an unbounded reciprocal. In (4.3), the clip is retained until after the path-law comparison; transferring the unclipped E/(J+K) would not justify the same TV charge.

Combining (4.3)–(4.4),

    3 E_mu v_err+P_mu(Cbad)
      ≤2128 K³/(beta Q)+4epsilon_beta(M).              (4.5)

Thus (2.3) proves the useful all-positive-beta intermediate inequality

    risk(B;beta)
      ≤min(1,2^16 L + 2128 K³/(beta Q)
                       +9K/Q+4epsilon_beta(M)),
                       0<beta≤1.                     (4.6)

The burn, suffix, reverse chain and regeneration labels are exclusively analytical. No original data are removed from B, and no suffix predictor is evaluated instead of it.

## 5. Uniform absorption at strong mixing, including all small horizons

For beta≥1/2, epsilon_beta(M)≤2^(−r), with r=floor(M/4), including r=0. Write M=4r+d, 0≤d≤3; then

    n=M+1≤4(r+1),  r+1≤4^r.

The second inequality holds at r=0 and inductively since r+2≤4(r+1). Therefore

    n epsilon_beta(M)²≤4.

If i=1 then epsilon≤1≤2i. If i<1 then

    epsilon≤2/sqrt(n)≤2sqrt(K/n)=2i.

Thus, uniformly for all K≥2,M≥1,beta≥1/2,

    epsilon_beta(M)≤2i≤2L.                            (5.1)

This deliberately loose estimate handles M=1,2,3, all parity cases and beta=1 without a special asymptotic assumption.

Using beta^(−1)≤2, K≥2 and (5.1) in (4.6),

    2128 K³/(beta Q)+9K/Q
       ≤(4256+9/4)K³/Q<2^13 K³/Q,
    4epsilon_beta(M)≤8L.

This proves (SM1). There is no deduction of an i-scale bound from the a-scale row-radius estimate near IID: that branch was already handled by the rejection-restricted reduction (2.2).

## 6. Public integer precision and the output-format comparison

With (SM2), 2^v≥K and 2^u≥n, so

    Q≥2^20 K³ sqrt(n).

Consequently

    2^13 K³/Q≤1/[128sqrt(n)]≤i/128≤L/128,

which proves (SM3)'s risk bound. Dividing by the inherited R≥2^(−17)L gives

    risk/R≤2^17(2^16+8+1/128)<2^34.

The bound is finite and uniform over K,M and beta∈[1/2,1]. The integer quantities u and v are bitlength ceilings; ceil(u/2) is integer arithmetic. No real logarithm, square-root oracle, beta estimate, or hidden distribution parameter is needed to generate the public configuration.

Dyadic ceilings change Q by only bounded factors. At fixed K, Q=Theta_K(sqrt(M+1)) and h=(1/2)log2 M+O_K(1). Its generous constants can make this schedule less economical than another finite configuration for practical M; no finite-size computational saving is asserted.

For comparison, NB002 §7.1's accepted output-grid lower, independently of any prefix, is

    R_grid(K,M,beta,Q)≥(1/8)min(1,K/Q).

It uses an IID source in every D2(beta). At beta=1, L=i; if risk≤C i with C fixed and C i<1/8, this forces

    Q≥sqrt(K(M+1))/(8C),
    h≥(1/2)log2(M+1)+(1/2)log2 K−log2(8C).

Thus at fixed K the leading half-log exponent is necessary for output-grid-valued predictors that attain IID risk, and (SM2) now suffices with **no log log M overhead** on the whole beta≥1/2 range. This necessity is an IID/output-format statement. It is not, by itself, an internal-master lower with unrestricted real outputs; it does not establish alphabet-uniform optimality or claim that each fixed positive-beta class requires the same precision. A separate complete-master lower, if established, must retain its own proof and review status.

## 7. Every fixed positive beta: a nonuniform extension

Equation (4.6) was proved for every beta>0. For r=floor(M/4), the geometric-sum estimate gives, also at beta=1 with the convention in (4.1),

    (r+1)delta^(2r)
       ≤sum_(j=0)^r delta^(2j)
       ≤1/(1−delta²)=1/[beta(2−beta)]≤1/beta.

When delta=0, the first term is interpreted explicitly as one for r=0 and zero otherwise; no undefined power is needed. Since n≤4(r+1),

    epsilon_beta(M)≤2/[sqrt(beta)sqrt(n)]
                  ≤2 beta^(−1/2)i.                   (7.1)

For i=1 the last inequality follows directly from epsilon≤1; for i<1 it follows from i=sqrt(K/n) and K≥1.

Using exactly the same beta-independent schedule (SM2) in (4.6) yields

    risk(B;beta)
      ≤min(1,C(beta)L),
    C(beta)=2^16+8 beta^(−1/2)
                    +2128/(2^20 beta)+9/2^20,         (7.2)

for every beta∈(0,1]. In the final 9K/Q term we used K³≥K. Therefore, at every fixed positive beta, the same half-log schedule is constant-order minimax with a constant allowed to depend on beta. The statement is uniform in K,M and sources at that fixed beta; it is **not** uniform as beta approaches zero. More generally it is uniform on beta∈[beta0,1] for any externally fixed beta0>0, with constant C(beta0), without supplying beta0 to the predictor.

This is compatible with the separate, pending PL001 statement that the fixed master interface needs Q=Omega_K(sqrt M log M) to attain all-beta uniform risk, or even along certain beta=O_K(M^(−2)) sources. Inserting such a vanishing beta into C(beta) does not give a bounded risk multiplier. No precise threshold in beta(M) separating the two precision regimes has been established here.

## 8. Exact architecture, full costs and scope of reuse

All operations, word ranges, master lifecycle, endpoint charges, arithmetic gadgets and all-token evaluations are **identical** to NB002. In particular there is no additional reverse-chain generator, stationarity check, burn counter, suffix scan, random seed or oracle in the program. Hence NB002 §9's full finite construction ledger applies verbatim for any h≥4 with p=4h+4ell+64. The following are the inherited upper bounds, not measured implementation performance:

| Coordinate | Bound / property |
|---|---|
| Hybrid neural depth / width | O(Kp²) / O(Kp) |
| Heads total / maximum per layer; QK dimension; score cap | 6 / 4; 2K; 2 |
| Online coefficient / arithmetic word | ≤128p bits, with complete products and guards |
| Dense coefficient slots / bits | O(K³p⁴) / O(K³p⁵), zeros and biases included |
| Active records / explicit holds | O(Kp²+K²) / O(K²p³) |
| Sparse addressed program, coefficients and holds | O(K²p⁴) bits |
| Masks / positions, n_tok=M+3 | O(n_tok²+n_tok log(n_tok+1)) bits |
| Observed one-hot input | O((M+2)K) bits; acquisition/conversion separately charged |
| Rolling scalar-neural work, excluding stored data | O(n_tok Kp²) bits |
| Uncached attention bitwork | O(n_tok²(K+p)p²) |
| Equally cached attention bitwork | O(n_tok²Kp²), plus cache creation/storage/selection |
| Dense all-token pointwise/QKV bitwork | O(n_tok K³p⁶) |
| Finite rational-log work / scratch | O(p³log²(p+1)) / O(p log(p+1)) |
| Five full-score cache creation | O(p³), plus logs; direct complete-score evaluation |
| Finite arithmetic evaluator code | O(p⁴) bits |

The complete offline ledger still includes public bitlength computation and this chosen schedule; layouts, positions and masks; constants; normalizer/guard microcode; generating, addressing and sorting every gate, term and hold; and actual output-format writes. For R_rec records, the inherited conservative O(R_rec p²) generation/sorting work and O(R_rec p) scratch remain. Dense files additionally pay their true O(K³p⁵) coefficient-bit output, including zeros.

Total peak is the maximum of simultaneous phase sums, not the rolling-work coordinate. A safe dense forward sum is

    O(K³p⁵+n_tok²+n_tok log(n_tok+1)+(M+2)K+n_tok Kp²),

with only the stored-program term replaced by O(K²p⁴) for sparse format. Generated data coexist with offline scratch while live. Input, all masks/history/QKV data, master/weight/normalized/output banks, controller/address words and released/copied buffers retain their original paid lifetimes.

For the separate PURE expansion, if T_bit includes **all** online bitops, movement, copies/clears, control and finite attention evaluation, and S_bit includes simultaneous live work/input/masks/public data (plus program rails if interpreted), the inherited instructionwise expansion has depth O(T_bit+p), width O(S_bit+p), sparse gates/holds O((T_bit+p)(S_bit+p)), dense coefficient bits O(p(T_bit+p)(S_bit+p)²), and generic dense bitwork O(p²(T_bit+p)(S_bit+p)²). These are not assigned the smaller hybrid depth/width.

At schedule (SM2), p=Theta(log(M+K)) still contains ell. Reducing master/output precision does not reduce total arithmetic word length to h alone, eliminate masks or history arrays, establish a computational advantage over paid direct counting, or prove training attainability. There is no new physical-fault guarantee and no theorem about an arbitrary floating-point or LayerNorm Transformer.

## 9. Failure checks, limits, and status

- **Tempting but invalid shortcut:** declare the original count binomial given its queried terminal row. Not used. Only an auxiliary even reverse skeleton, constructed under the exact conditional stationary law, has independent regeneration hits.
- **Zero stationary masses:** reverse divisions occur only on supp(pi); its closure and full all-state forward burn bound are both proved. Arbitrary off-support initialization remains allowed.
- **Endpoint dependence:** the suffix-law TV comparison is on the entire suffix including Y_M. No separate independent query is substituted.
- **Unbounded transfer error:** E/(J+K) is clipped before path-law comparison. The indicator Cbad also receives only one bounded-function TV charge.
- **Near-IID radius mismatch:** an a-scale radius estimate is insufficient at beta=1. The accepted rejection-subset argument, not radius safety, supplies the i-scale statistical baseline there.
- **Beta=1 and small M:** residual kernels are not divided by zero; epsilon is separately defined at r=0; the burn may be zero; m=0 is included in the binomial reciprocal identity.
- **Scope of optimality:** the proved upper is for the exact accepted NB002 finite map. The accepted output-only lower does not prove an internal-master necessity. No joint-K sharpness, intermediate beta(M) phase transition, novelty priority, neural-resource optimality, or learning result is claimed.
- **Actual failures:** none was found in this new argument as of author freeze. The hazards above are examined proof obligations, not fabricated counterexamples. PL001's separate failed/simple witness ideas and pending status are not rewritten here.

Source identities, finite diagnostic results and independent review status are recorded separately. Finite checks can corroborate formulas and boundary cases; they cannot establish the universal theorem or verify an emitted neural artifact. This file is a new author candidate, not self-certified acceptance.
