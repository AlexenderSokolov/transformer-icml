# BK002 — Supplied beta does not permit all-budget full-history adaptation (candidate)

2026-11-02. New author candidate; fresh independent FULL review and root acceptance required. Accepted AB001–AB003 and BK001 are unchanged. This result concerns **unrestricted full-corrupted-history predictors**, unlike BK001.

## 1. Exact finite constrained-risk theorem

Use the accepted binary protected-endpoint source-corruption experiment: N=M+2 observed bits from a homogeneous second-order source, all-state P^2>=beta Pi with a hidden qualifying stationary law, offline strict Hamming-k edits among the first M positions, and unconditional TV loss at the original protected terminal pair. The predictor receives the entire corrupted word, may randomize and have unlimited computation, and is supplied M and beta, but not the actual edit budget.

Fix integers M>=256 and k with

    k^2>=4M,  1<=k<=T=floor(M/8).

Set

    delta=1/k, beta=delta^2, tau=1/(4M), r=1/(2M),
    I=[k/(32T),1/16].

For every a in I define a clean stationary source Q_a by its designated exit coordinates

    (a,b,e,t)=(a,delta,1-delta,tau),
    theta(1)=(a,delta,delta,1-tau),
    x_a=[(1-delta)/a+2+delta/tau]^-1,
    Pi_a=(x_a(1-delta)/a, x_a, x_a, x_a delta/tau).

All Q_a satisfy the SAME supplied certificate beta=1/k^2. Let A=A_(M,beta) be any full-history estimator, and let S be its supremum identity-corruption risk over this family. Let Q_* be the stationary symmetric first-order flip-r source; it also belongs to the same beta class. There is one common source-independent protected strict-k kernel C_(M,k) such that

    R_*(A,C_(M,k))
       >= [ (3k/(2048M)) log((T+1)/k)
                         -32 S log(2T/k) ]_+.        (BK2)

The SAME estimator map A_(M,beta) is used in the clean risk S and the corrupted null risk. No histogram restriction is imposed, and the full output words, not only their statistics, are compared.

Consequently no family A_(M,beta), independent of the actual k, attains the accepted known-k binary profile H_2(M,k,beta) with one universal finite constant for all M,beta,k. This failure already holds under stationary initialization. Section 8 proves the sharper range-envelope statement: uniform supplied-beta adaptation over all 0<=k<=b_M exists if and only if b_M=O(sqrt(M)), with constants allowed to depend on that fixed public envelope bound.

This is uniform-in-beta impossibility. It does not contradict a fixed-positive-beta upper whose constant may depend on that fixed beta. It is also not a stronger known-k minimax lower: a known-k minimax estimator need not have clean risk of order M^-1/2 when invoked with a large allowed budget.

## 2. Domain, stationarity and all sixteen certificate entries

The interval is nonempty because k<=T. Its lower endpoint obeys

    a>=k/(32T)>=k/(4M)>=1/k=delta,

where the last inequality is k^2>=4M. Its upper endpoint is 1/16. Also delta<=1/4, e=1-delta>=3/4 and tau<=1/4 in the stated domain.

Write x=x_a,y=xe/a,w=x delta/tau. The displayed vector has positive coordinates and sums to one. The identities ya=xe and w*tau=x*delta prove stationarity. Since delta/tau=4M/k,

    x<=k/(4M),
    w=[1+e k/(4Ma)+k/(2M)]^-1>=1/3.               (2.1)

Indeed a>=k/(4M) and k<=M/8 make the denominator at most 2+1/16<3. No initial-state restriction is used in the certificate.

The complete pair-kernel square is

    [ (1-a)^2, (1-a)a, a e,        a delta       ]
    [ e^2,      e delta, delta tau, delta(1-tau)  ]
    [ e(1-a),   e a,     delta e,  delta^2       ]
    [ tau e,    tau delta, (1-tau)tau, (1-tau)^2 ].

Its target lower vector is beta Pi=delta^2(y,x,x,w). To verify every entry:

- The two small entries delta*tau and tau*delta equal delta^2*k/(4M) and therefore dominate delta^2*x.
- Since y=e*x/a and x<=k/(4M), delta^2*y<=e*delta*tau/a<=e*tau because a>=delta.
- The entries a*delta and delta*(1-tau) dominate delta^2*w using a>=delta and 1-tau>=delta*w. The entry delta^2 does as well.
- (1-tau)tau>=delta*tau>=delta^2*x.
- e*delta and delta*e dominate delta^2*x because e>=3/4>=delta*x.
- The entries (1-a)a and e*a dominate delta^2*x: x<=a/e and delta^2/e<=1/12, while 1-a,e>=3/4.
- The remaining entries (1-a)^2,e^2,e(1-a),(1-tau)^2 are at least 9/16, whereas the corresponding delta^2*y or delta^2*w are at most 1/16.

This accounts for all sixteen starting/target pairs. It does not merely check stationarity or two favorable entries.

For Q_*, the one-step binary kernel T_r satisfies Pi_*(u,v)=T_r(u,v)/2 and

    P_*^2((u,v),(s,t))=T_r(v,s)T_r(s,t)>=2r Pi_*(s,t).

Its all-state coefficient 2r=1/M is at least beta=1/k^2 because k^2>=4M. Thus null and clean alternatives share the SAME valid advertised beta, although their maximal coefficients need not be equal. Its true symbol-1 probability at terminal pair 00 is r.

## 3. Rare null words and a common clean source family

For k<=t<=T let

    x^(t)=1^(N-t-1)0^(t+1).

It begins in 11, first enters a zero at position N-t, and ends in 00. Under Q_* these disjoint words have common probability

    v=(r/2)(1-r)^M,  1/(8M)<=v<=1/(4M).             (3.1)

The lower bound follows from (1-r)^M>=1-Mr=1/2.

For each FIXED a in I, under Q_a the event of initial pair 11 and first zero at position N-t has probability

    w_(a,t)=w(a)(1-tau)^(M-t-1)tau.

After that first zero the pair is 10. Let L_(a,t) be the remaining t-transition Q_a continuation law from that pair, with the entire unchanged preceding prefix retained. Since w(a)>=1/3 and Bernoulli's inequality gives (1-tau)^M>=1-Mtau=3/4,

    w_(a,t)>=1/(16M),  v/w_(a,t)<=4.                (3.2)

The prefix mismatch between null and clean laws has only this constant cost. In particular, no long-prefix event was conditioned away for free.

Define

    e_(a,t)=E_(L_(a,t))[
       |A(full_word)(1)-a| 1{terminal pair=00} ].

For a fixed a, the different first-zero events are disjoint portions of ONE clean stationary source's unconditional risk. Hence

    sum_(t=1)^(M-1) w_(a,t)e_(a,t)<=S.               (3.3)

This common-a relation will be integrated in §6; distinct sources' clean guarantees are not subtracted without the necessary weights.

## 4. Reference suffix and constant full-word likelihood domination

Let R_(a,t) be the continuation law from 10 with the same table as Q_a except that the transition 01->11 is forbidden: from 01 it goes to 10 deterministically. Its remaining transition probabilities are 00->01 with a and 10->01 with delta. Because delta<=a, at every step its conditional probability of emitting a one is at most a. It never reaches 11.

Let L be its number of emitted ones, and define acceptance event

    G={L<=k, terminal pair=00}.

For a in the interval

    I_t=[k/(32t),k/(16t)] subset I,

E_R L<=at<=k/16. Thus P_R(L>k)<=1/16. The terminal-00 probability is at least (1-a)^2>=9/16 (the t=1 version would have the stronger bound 1-a). Consequently

    P_R(G)>=1/2.                                    (4.1)

On a reference path in G, the number of departures from 01 is at most its number of emitted ones, hence at most k. All transitions except 01->10 have the SAME probability under Q_a and R. Therefore, pointwise on every accepted complete suffix,

    P_(L_(a,t))(path)
      =P_(R_(a,t))(path)(1-delta)^(N_01)
      >=(1-1/k)^k P_(R_(a,t))(path)
      >=(1/4)P_(R_(a,t))(path).                     (4.2)

Here k>=2. The last elementary inequality follows because f(x)=x log(1-1/x) is increasing on x>=2: its derivative is log(1-u)+u/(1-u)>=0 for u=1/x, using -log(1-u)<=u/(1-u). At x=2 its exponential is 1/4.

Thus for every nonnegative functional g of the FULL word,

    E_R[g 1_G]<=4 E_(L_(a,t))[g 1{terminal00}].       (4.3)

No type-class sufficiency, histogram matching, canonicalization or conditional-IID assumption is used. Equation (4.2) compares the exact probability of each complete ordered output word.

## 5. One legal full-history strict-k kernel

Define a stochastic map on every binary input word. It is identity unless the input equals x^(t) for some k<=t<=T. On such an input:

1. Draw a uniformly on I_t=[k/(32t),k/(16t)].
2. Sample its t-bit R_(a,t) continuation from pair 10.
3. Replace the original t zero suffix bits by that sample if G holds; otherwise output the input unchanged.

The prefix and the first zero remain unchanged. Every accepted continuation ends with 00, and it differs from the old zero suffix at exactly its at-most-k ones. Hence every outcome obeys the strict Hamming budget and protects the actual final pair. Rejections are identity. The map is defined on all words and uses only public M,k, observed suffix length t and private randomness. Its auxiliary parameter a is sampled by the algorithm, not read from an unknown source.

Although the clean family has beta=1/k^2, the kernel does not need an unknown source table as input. It is the same map when applied to every source. A continuous uniform auxiliary draw defines a legal stochastic map on the finite input/output set by integration; no efficiency claim is made. In fact each output probability of the reference sampler is a polynomial in a with rational coefficients, so integrating over rational endpoints gives a finite rational kernel if an explicit finite-table representation is desired.

On G the null target is r and the corresponding clean target is a. Since a>=delta=1/k>=1/M=2r and P_R(G)>=1/2,

    E[null loss after attack | x^(t),a]
       >=a/4 - E_R[|A(full_word)(1)-a|1_G]
       >=a/4 -4 e_(a,t).                            (5.1)

Rejected losses are nonnegative and are discarded. Independent estimator randomness is averaged throughout and need not be coupled to the attack seed.

## 6. Exact common-parameter constrained-risk calculation

The uniform density on I_t is 32t/k and its mean is 3k/(64t). Summing (5.1) over the disjoint null words yields

    R_* >= sum_(t=k)^T v [3k/(256t)
                       -4(32t/k) integral_(I_t)e_(a,t) da].

By v>=1/(8M), the positive part is at least

    (3k/(2048M)) sum_(t=k)^T 1/t
       >=(3k/(2048M)) log((T+1)/k).                 (6.1)

For the negative part, use v<=4w_(a,t), and note that a in I_t implies 32t/k<=2/a. Then (3.3), after exchanging a finite sum with a nonnegative integral, gives

    4 sum_(t=k)^T v(32t/k) integral_(I_t)e_(a,t) da
       <=32 integral_(k/(32T))^(1/16)
                  (1/a) sum_(t:a in I_t) w_(a,t)e_(a,t) da
       <=32 S log(2T/k).                            (6.2)

These are separate nonnegative contributions, so substituting a lower bound for the positive part and an upper bound for the error is legitimate. Nonnegativity of risk then permits the positive part in (BK2). This proves the displayed finite theorem without assuming a uniform prior survives conditioning.

## 7. Failure of full-history supplied-beta all-budget adaptation

Suppose A_(M,beta), independent of actual k, attained C H_2(M,k,beta) for a finite C independent of M,k,beta. Its clean k=0 guarantee at THIS SAME beta=1/k^2 gives S<=C/sqrt(M).

Take any sequence satisfying the finite domain, k/sqrt(M)->infinity, and log(M/k)->infinity; for example k=floor(M^(3/4)) for all sufficiently large M. The ratio of the negative to the positive term in (BK2) is at most

    (65536 C/3)(sqrt(M)/k)
       log(2T/k)/log((T+1)/k),                      (7.1)

which tends to zero. The logarithm ratio tends to one because their difference is log(2T/(T+1)), bounded, while the denominator diverges. Thus R_* is eventually a positive universal multiple of (k/M)log(M/k).

At beta=1/k^2, the cutoff is exactly max(sqrt(beta),1/M)=1/k because k<=M. Hence

    F_2=(1+log2)k/M, H_2<=2k/M.

The ratio R_*/H_2 diverges, a contradiction. Both the clean comparisons and the corrupted null are stationary and use exactly the same supplied beta and the same estimator map. Arbitrary-start adaptation is therefore impossible as well.

The supplied beta numerically reveals the construction's scale k=1/sqrt(beta), but it does not reveal whether the realized word is clean or corrupted. The theorem still requires that one map perform at statistical order on the clean source family and at the known-k corruption order on the null. A predictor told an advertised maximum k but required to adapt pointwise to all actual budgets 0,...,k faces that same issue. In contrast, the accepted known-k minimax theorem only requires the larger H_2(M,k,beta) bound when invoked with that k, even on an identity attack; no contradiction is created.

## 8. Sharp uniform budget-range boundary even when beta is supplied

Let b_M be any public integer envelope, 0<=b_M<=M. Consider estimator families A_(M,beta) that may be designed using b_M and are supplied beta, but not actual k. Require one finite constant C such that risk<=C H_2(M,k,beta) for every M>=64, beta in [0,1], and 0<=k<=b_M, under either stationary or arbitrary initialization.

Such a family exists if and only if b_M=O(sqrt(M)).

**Sufficiency.** If b_M<=L sqrt(M) for a fixed integer L, accepted AB003 §8 supplies a predictor independent of BOTH k and beta with threshold 12L ceil(sqrt(M)) and risk <=min{1,2^18 L M^-1/2+2^22 F_2}. Giving it beta cannot hurt. Finitely many exceptional M in an asymptotic O-bound are absorbed into a finite envelope constant because b_M<=M.

**Necessity.** If b_M/sqrt(M) is unbounded, choose M_n tending to infinity along which that ratio tends to infinity and set

    k_n=min{b_(M_n),floor(M_n^(3/4))},
    beta_n=1/k_n^2.

Then k_n/sqrt(M_n)->infinity, k_n<=floor(M_n/8) and k_n^2>=4M_n eventually, and log(M_n/k_n)->infinity. Apply (BK2) to A_(M_n,beta_n). Its k=0 guarantee at beta_n bounds the required clean S by C/sqrt(M_n), and (7.1) makes the penalty negligible. But H_2(M_n,k_n,beta_n)<=2k_n/M_n, contradicting a universal finite C.

This is a range-envelope statement including the clean point k=0. It is not pointwise impossibility at every k above sqrt(M), and in particular says nothing of that form when k is comparable to M and H_2 is already constant. The constants for an achievable bounded envelope may depend on its fixed bound. The necessity is stationary; sufficiency holds for all starts.

## 9. Interpretation and remaining finer questions

This closes the uniform supplied-beta, unknown-budget question negatively, if the proof is independently accepted. It upgrades the joint-blind range boundary from AB003 to beta-informed full-history procedures. BK001 remains a distinct fixed-beta-curve result at beta=1/M for histogram-plus-endpoint-pair procedures; it should not be silently relabeled as this theorem.

The full-history behavior on a prescribed moving-beta curve such as beta=1/M, the optimal adaptation penalty beyond the square-root range, and restricted classes of sources or attackers remain separate possible questions. For a fixed positive beta, constants depending on beta can still yield k-blind order max(M^-1/2,k/M); that does not supply a uniform-in-beta constant and is consistent with this obstruction.

No causal, public-mask/seed, edited-endpoint, efficient-adversary, neural-depth, training, external novelty, or formal-verification conclusion is made. The proof directly accounts for full corrupted words and a parameter-independent strict-budget kernel.
