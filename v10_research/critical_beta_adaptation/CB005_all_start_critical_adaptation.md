# CB005 — All-start occupation-balance adaptation at the critical certificate

2026-11-02. **New complete theorem candidate; fresh independent FULL review pending.** This extends the separately frozen stationary CB004 route. No CB004/BP001 or accepted CB001–CB003 file is modified. The new proof uses target hitting-time bounds and a Doob transform, NOT a global square-root-beta mixing claim.

## 1. Result and model

Use the exact binary protected-endpoint source-corruption experiment of SC003/BT002: M+2 symbols from an unknown homogeneous order2 source; a qualifying stationary Pi with ALL-STATE P^2(i,j)>=beta Pi(j), beta>0; arbitrary actual initial pair law, including unsupported states; at most k first-M Hamming replacements by one source-independent offline randomized kernel; final pair protected; unconditional TV loss at its true actual next law. The estimator does not see the source, Pi, clean interior, mask, attack seed, or k.

Use EXACTLY the CB004 balance-gated empirical estimator A_bal: at the protected terminal row u, let J1' count row-u departures in the first floor(M/2) departure times, J' its total count, and C' its designated-successor count. The fixed orientations are q=(a,b,e,tau)=(theta00(1),theta01(1),theta10(0),theta11(0)). Output C'/J' when J'>0 and512 J1'>=J'; otherwise output designated probability0.

For M>=64,0<=k<=M and beta>0, the claimed all-start upper is

 R_all(A_bal)<=min{1, 2^16/sqrt(M)
                    +2^16/(M sqrt(beta))+2^23 k/M}. (CB5)

At beta=1/M this becomes

 R_all(A_bal)<=min{1,2^17/sqrt(M)+2^23 k/M}.          (CB5-critical)

Thus, if independently accepted, one k/beta-blind full-history procedure attains the accepted known-k order over ALL budgets on every band beta>=c/M with fixed c>0, with constants allowed to depend on c. Only four first-half row counts beyond the global triple histogram are required. The new content is the all-start weighted imbalance bound proved below. A complete proof audit of all components is required before acceptance.

## 2. A universal first-hit density bound

For any finite d-state chain, any target u, any distinct start v, and its first ordinary hit D_u,

    P_v(D_u=t)<=d/(t+1), integer t>=1.              (2.1)

This does not require irreducibility. Modify ONLY the target row to send u deterministically to v, obtaining a finite stochastic matrix Q. Its first positive return to u has law1+D_u. For any finite stochastic matrix and target, the reciprocal-return identity is

 sum_(j>=1)P_u(T_j=r)/j
    =[z^r](-log(1-F_u(z)))
    =[tr(Q^r)-tr(Q_(-u)^r)]/r<=d/r.                (2.2)

Here F_u is the positive-return pgf and Q_(-u) deletes the target row/column. To verify it, the Schur complement gives1-F_u(z)=det(I-zQ)/det(I-zQ_(-u)); expand the formal logarithms. The return expansion makes the coefficient nonnegative even for defective returns. Retain only the first-return term at r=t+1 to prove(2.1). This is the same accepted generic identity used in BAI004/BOD001, reproduced here so the reset-row trick is explicit. The modified Q is only an analytic finite-state chain; no second-order/source-class assertion about it is made.

## 3. Generic target transition bound from a hitting potential

Now let P be an irreducible finite d-state chain, target u have stationary mass p>0, and let H=max_v E_v D_u (ordinary hit, zero at u). Let h(v)=E_v D_u. Kac and the first-step equations imply

    (Ph-h)(v)=-1+1{v=u}/p.

Thus, for J_u(r)=sum_(j=0)^(r-1)1{Y_j=u},

    E_v J_u(r)=p[r+E_v h(Y_r)-h(v)]<=p(r+H).        (3.1)

A loop-rotation trace identity gives, for r>=1,

 r P^r(u,u)
   =sum_v E_v[J_u(r)1{Y_r=v}]
   <=sum_v E_v J_u(r)<=d p(r+H).                  (3.2)

Indeed the contribution of a fixed time j on the left sum is sum_v P^j(v,u)P^(r-j)(u,v)=P^r(u,u); summing j=0,...,r-1 proves the equality. This needs no reversibility.

For v!=u, first-hit convolution expresses P^r(v,u)=sum_(t=1)^r P_v(D_u=t)P^(r-t)(u,u). For t<=floor(r/2), (3.2) bounds the return term by d p(1+2H/r). For later t, (2.1) bounds the density by2d/r, and(3.1) from u bounds the sum of return probabilities by p(ceil(r/2)+H). Consequently, including v=u,

    P^r(v,u)<=4d p(1+H/r), r>=1.                   (3.3)

The numerical comparison is d p[2+2/r+4H/r]<=4d p(1+H/r). Empty early sums cause no problem at r=1. This is a target-specific pointwise bound, not convergence to stationarity.

## 4. Exponential tilt gives a JOINT terminal/upper-occupation tail

Put Hbar=max(H,1/p) and lambda=1/(4Hbar). For a positive return T from u and an ordinary first hit D_i from i, the same survival-closed hitting/return family as BU001/BP001 gives

 E T=1/p, E T^2<=2Hbar/p,
 E exp(lambda D_i)<=4/3,
 E exp(lambda T)<=exp(2lambda/p),
 f:=E exp(-lambda T)<=exp[-3lambda/(4p)].           (4.1)

The moment induction E V^r<=r!Hbar^(r-1)E V proves the positive-transform bounds. The inequality exp(-x)<=1-x+x^2/2 proves the bound on f. Also exp(-x)>=1-x gives f>=3/4 and

 h_i:=E_i exp(-lambda D_i)>=3/4, h_u=1.            (4.2)

Define a new stochastic matrix Q by

 Q_ij=exp(-lambda) P_ij h_j/h_i, i!=u,
 Q_uj=exp(-lambda) P_uj h_j/f.                     (4.3)

The ordinary hitting equations and positive-return decomposition show that each row sums to one. Q preserves the directed support and is irreducible. No source-class or binary-pair constraint is asserted for this auxiliary chain.

Its ordinary hitting law from i!=u is the original law tilted by exp(-lambda D_i)/h_i, so H_Q<=2H. Its positive-return law is tilted by exp(-lambda T)/f. Therefore

 E_Q T>=E[T exp(-lambda T)]>=E T-lambda E T^2>=1/(2p),
 E_Q T<=E T/f<=2/p.

Kac for Q gives p_Q<=2p and Hbar_Q<=2Hbar. Apply(3.3) to Q:

    Q^l(i,u)<=16d p(1+Hbar/l), l>=1.               (4.4)

For every complete length-l path from i to u, its likelihoods satisfy

    Q(path)=P(path) exp(-lambda l) f^(-J_u(l))/h_i.

This is an exact telescoping product: J_u(l) counts departures, and the ending factor is h_u=1. Hence, on J_u(l)>4lp+1,

 P_i(Y_l=u,J_u(l)>4lp+1)
    <=h_i exp(lambda l) f^(4lp) Q^l(i,u)
    <=16d p(1+Hbar/l) exp[-l/(2Hbar)].             (4.5)

The crucial stationary-mass factor p is present in this JOINT bound even for arbitrary starts. We did not multiply an unconditional tail by a terminal probability without justification.

For comparison, the same positive-transform calculation after the first hit gives the ordinary all-start lower tail

    P_i(J_u(l)<lp/16)<=2exp[-l/(8Hbar)].            (4.6)

Exact indices: K=ceil(lp/16); fewer than K visits means D_i+T_1+...+T_(K-1)>=l. Use(4.1), K-1<=lp/16 and exponential Markov. These returns are IID before the random horizon restriction, not after conditioning on the terminal state.

## 5. Generic arbitrary-start weighted imbalance theorem

Let M>=2, n=floor(M/2), m=M-n, and let J1_u,J2_u count departures in these two consecutive windows. For any fixed target weight q_u in[0,1], put

    L_u=p_u q_u Hbar_u.

For every initial law and0<c<=1/256,

 E[q_(Y_M)1{J1_(Y_M)<c(J1_(Y_M)+J2_(Y_M))}]
       <=(288d/M) sum_u L_u.                       (5.1)

To prove it, first fix u with np_u>=1. If J1_u>=np_u/16 and J2_u<=4mp_u+1, then m<=2n implies J1_u/(J1_u+J2_u)>=1/145. Thus imbalance requires a first-window lower tail or second-window upper tail.

For the lower-tail event, condition on the prefix history through time n, and bound the future terminal probability using(3.3). Combine with(4.6). For the upper-tail event, condition only on Y_n and use the JOINT inequality(4.5). Since m>=n, their sum gives

 P_i(Y_M=u,imbalance)
    <=24d p_u(1+Hbar_u/n) exp[-n/(8Hbar_u)].        (5.2)

Write x=n/Hbar_u. Multiplying by q_u gives

    <=(24d L_u/n)(x+1)exp(-x/8)<=96d L_u/n,

because sup_(x>=0)(x+1)exp(-x/8)=8exp(-7/8)<4.

If np_u<1, simply use(3.3) at horizon M. Since Hbar_u>=1/p_u, L_u>=q_u; hence p_u q_u<q_u/n<=L_u/n. Thus

 q_u P_i(Y_M=u)<=4d[p_u q_u+L_u/M]<=8d L_u/n,

which is within the same96d bound. Sum over u and use n>=M/3. This proves(5.1), including zero target weights and arbitrary initial mixtures. The event is false at total occupation zero. No stationarity of the ACTUAL start is assumed anywhere in this section.

## 6. Full-support binary specialization

For a full-support binary source with positive all-state beta, accepted BU001 v2 gives the target hitting-scale bound with gamma=(a,1,1,tau):

    Pi(u) gamma_u Hbar_u<=10/sqrt(beta).

This is reproduced/checked in BP001 section3; its sharper source constant is6, but10 suffices. Since the actual designated q=(a,b,e,tau)<=gamma, summing L_u gives at most40/sqrt(beta). Apply(5.1) with d=4 to obtain

 E_mu[q_(Y_M)1{J1_(Y_M)<J_(Y_M)/256}]
       <=46080/(M sqrt(beta))<2^16/(M sqrt(beta)).  (6.1)

This time the proof is genuinely all-start and does NOT use stationary time reversal. Unit crossing caps enter only the accepted hitting-scale estimate; no equality b=e is used.

## 7. Singleton stationary supports, including unsupported starts

Positive all-state beta has only two non-full-support possibilities: a singleton absorbing00 or11, by the SC003 support classification. Consider absorbing00. Then a=0. For an initial active state in{A=01,B=10,C=11}, paths ending active have never hit00. Reflect the killing transition B->00 into B->A to obtain the three-state stochastic chain

    R(A,B)=1-b, R(A,C)=b,
    R(B,A)=1,
    R(C,B)=tau, R(C,C)=1-tau.                       (7.1)

For each active ordered path, its original probability is at most its R probability, since the only changed factor is1-e<=1 on B->A. Counts and endpoints of such paths are unchanged. This domination is unconditioned.

For b,tau>0, R is irreducible with

    Z=2tau+b, p_A=p_B=tau/Z, p_C=b/Z.

Direct hitting equations give H_A=1+1/tau and H_C=2/b. Therefore

    Hbar_A<=2+1/tau, Hbar_C<=1+2/b,
    p_A b Hbar_A<=1, p_C tau Hbar_C<=1.             (7.2)

Apply(5.1) to R with weights(b,0,tau). Its total weighted imbalance is at most1728/M. The same conclusion for boundary b=0 or tau=0 follows by approximating b,tau by positive probabilities and taking a finite-horizon limit: the expectations are finite polynomials in the transition entries and weights, and the bound is uniform. This limit is only for the auxiliary R and makes no minorization-preserving approximation claim about the original source.

The remaining original target B has designated weight e. For any active initial state,

    e P(Y_M=B)=P(T_00=M+1)<=4/(M+2)                (7.3)

by(2.1), since B->00 is the only way to enter the absorbing state. An actual start at00 contributes zero; mixtures follow by linearity. Drop the imbalance event to bound this contribution. Thus the original source's weighted imbalance is at most1732/M<2048/M, and hence below2^16/(M sqrt(beta)) because beta<=1. Symbol exchange proves the absorbing11 case with the SAME fixed designated orientations.

Combining with(6.1), the ALL-START clean-bias bound is

    I_all<=min{1,2^16/(M sqrt(beta))}.              (7.4)

## 8. Corruption assembly and scope

The frozen CB004 sections2–3 and clean-comparator part of section4 prove, for the SAME gate and ANY initial law,

    R(A_bal,C)<=I_all+2^16/sqrt(M)+2^23 k/M.

They use the generic balanced-history inverse-occupation lemma, the strict Hamming perturbation |J'-J|,|J1'-J1|,|C'-C|<=6k, and the accepted arbitrary-start terminal-occupation/clean-empirical interfaces. No stationary premise is used in that deterministic reduction. Substitute(7.4) and apply the unit cap to prove(CB5). At beta=1/M the statistical coefficients sum to2^17.

On beta>=c/M, the upper is O_c(M^-1/2+k/M); the accepted stationary BT002 lower already applies to the all-start minimax problem and is at least a universal multiple of max(M^-1/2,k/M). The known-k profile on this band is equivalent to that scale with c-dependent constants. Thus this SAME predictor is unknown-k oracle-order adaptive over all budgets for both initialization conventions on and above the critical band, if the new proof is accepted. It does not contradict the supplied-beta subcritical obstructions, where1/(M sqrt(beta)) can exceed the clean floor.

This is not a claim of global or weighted sqrt(beta) exponential mixing. The target heat-kernel bound(3.3) contains1+H/r, not decay to stationarity; the auxiliary Doob chain is an analysis device, not an observable source or sampling algorithm. All-state minorization, arbitrary unsupported starts, strict first-M edits, the protected terminal pair and hidden seeds/masks are retained.

## 9. Provenance and review requirement

The new generic reset-row, loop-rotation, pointwise-target and tilted joint-tail arguments are proved here. BU001 v2 supplies only the accepted binary hitting-scale inequality; SC003 supplies the exact model/support classification and empirical/occupation interfaces. The reciprocal-return identity is also proved here and was checked against accepted BOD001/BAI004. CB004 supplies the frozen all-start-valid gate reduction; BP001 supplies a separately written version of the return-moment argument, which is restated in this proof. Read exact receipts for inherited acceptance, and require fresh independent review of this WHOLE extension plus its frozen gate interface. Finite diagnostics are not formal or external peer review. No publication, external novelty, neural/training or architecture claim is made.
