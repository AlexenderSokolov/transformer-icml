# CB002 — A near-prefix veto with a strict-Hamming robust risk-increment bound

2026-11-02. **New partial theorem; fresh independent review pending.** This is a safe full-history estimator component at beta=1/M, not a solution of unknown-k adaptation. It strengthens CB001's exact-run test to approximate constant prefixes and controls the test under EVERY permitted corruption kernel. No accepted source is changed.

## 1. Main partial result

Use the binary protected-endpoint model in SC003/BT002. Let M>=64, beta in(0,1], and0<=k<=M. Initialization is arbitrary, including unsupported starts; the all-state certificate is P^2>=beta Pi. The predictor sees the full corrupted word Z, not k, clean history, seed or mask. Put

    n=floor(M/2), h=ceil(sqrt(M)).

Given ANY baseline predictor A, define its prefix-veto modification W(A):

- if the preserved terminal pair is00 and at most h of Z_1,...,Z_(n+1) are zeros, output symbol-1 probability0;
- if the terminal pair is11 and at most h of that prefix are ones, output symbol-0 probability0;
- otherwise use A unchanged.

The modification uses M and the full-word order but neither k nor beta. For EVERY admissible source, start and strict-k corruption kernel C,

 R(W(A),C) <= R(A,C)
      +min{1, 288(h+k)/M +1248/(M sqrt(beta))}.      (NP1)

In particular, on the prescribed critical curve beta=1/M,

 R(W(A),C) <= R(A,C)
      +min{1, 2^11 M^-1/2 +2^9 k/M}.                (NP2)

This is a **risk-increment bound**, not a standalone guarantee on W(A). It preserves any O(M^-1/2) clean guarantee, preserves AB003's optimal small-budget guarantee on this curve, and does not worsen an existing all-budget oracle-order guarantee if one becomes available. It does not create such a guarantee from AB003 outside its proved small-budget range. At beta>=c/M, the same conclusion holds with constants depending on fixed c>0.

The proof's main new ingredient is a weighted small-prefix-occupation bound, proved without treating terminal-selected samples or a random number of excursions as IID.

## 2. Embedded diagonal chain and a certificate bound

For full stationary support, use exits(a,b,e,tau), Pi=(y,x,x,w), and

    ya=xe, w tau=xb, y+2x+w=1,
    H=b+e-be,
    alpha=a b/H, delta=tau e/H.                    (2.1)

Observe successive visits to D={00,11}, counting a diagonal self-loop as a new visit and skipping only off-diagonal states. The resulting two-state trace is homogeneous Markov with transitions00->11 of probability alpha and11->00 of probability delta. To see this, the probability from01 of hitting11 before00 solves p=b+(1-b)(1-e)p, hence p=b/H; the exchanged probability from10 is e/H. The strong Markov property gives the trace transition kernel. All crossing excursions finish almost surely since b,e>0.

The all-state certificate entry b tau>=beta x and stationarity give b^2>=beta w. Also stationarity gives e=ya/x<=y/x. For any remaining horizon q>=0,

 a P^q(11,00)<=lambda:=a min(1,y/w)=min(a,a delta/alpha).
                                                               (2.2)

Here w P^q(11,00)<=y is just stationarity and nonnegativity, not a stationary-start restriction.

We need

    lambda/delta <=3/sqrt(beta).                   (2.3)

Indeed, by the flow identities,

    lambda/delta=(H/b) min(1,w/y)
       <=1+(e/b) min(1,w/y).

Since b>=sqrt(beta w), it remains to prove

    e min(1/sqrt(w),sqrt(w)/y)<=2.                  (2.4)

If w>=y and w>=1/4, the left side is at most1/sqrt(w)<=2. If w>=y and w<1/4, then x=(1-y-w)/2>1/4, so e<=y/x<=4y<=4w, and e/sqrt(w)<=4sqrt(w)<=2. If y>=w and y>=1/4, it is at most sqrt(w)/y<=1/sqrt(y)<=2. If y>=w and y<1/4, x>1/4 and e<=4y, so e sqrt(w)/y<=4sqrt(w)<=2. Thus(2.4) holds. Finally beta<=1 follows by summing one row of the certificate, and1+2/sqrt(beta)<=3/sqrt(beta), proving(2.3).

No identity theta10(1)=b is assumed. All four transition parameters are unrestricted subject to the model.

## 3. A fixed-horizon small-occupation event implies a binomial comparison

Fix an integer n>=64 and let

    J_v=sum_(j=0)^(n-1)1{Y_j=v},
    E_K={J_00+J_01+J_10<=K}.

Assume first0<=K<=n/2, and put m=n-K. On E_K, J_11>=m and J_00<=K.

Construct independent infinite Bernoulli stacks for the diagonal trace: the r-th departure from11 has a fresh Bernoulli(delta) indicator of transition to00, and the r-th departure from00 has a fresh Bernoulli(alpha) indicator of transition to11. Such a construction follows by using independent excursion randomness at each visit to each diagonal. Excursion duration may depend on its transition indicator; NO independence from the observed horizon or occupation counts is claimed. Let B_11(r),B_00(r) be the prefix sums of these two independent stacks.

On E_K intersect{Y_n=11}, all departures from a diagonal before n have completed their next-diagonal transition by n. The diagonal trace ends at11, and its first diagonal may be either state. Consequently the number of11->00 transitions is at most the number of00->11 transitions:

    B_11(J_11)<=B_00(J_00).

By monotonicity of the stacks,

    E_K intersect{Y_n=11}
       subset {B_11(m)<=B_00(K)}.                  (3.1)

The variables on the right are independent Binomial(m,delta) and Binomial(K,alpha) variables at FIXED deterministic sample sizes. This is an event inclusion on an infinite realization, not an assertion that the actually observed exit counts are conditionally binomial.

## 4. Weighted small-prefix occupation bound

Write mu=m delta and nu=K alpha. If mu<4nu, (2.2) gives

    lambda<=a delta/alpha<4aK/m<=8K/n.             (4.1)

If mu>=4nu, the binomial comparison has probability at most

    P(B_11(m)<=mu/2)+P(B_00(K)>=mu/2)
       <=exp(-mu/8)+exp(-mu/16)
       <=2exp(-mu/16).                             (4.2)

For completeness, exponential Markov with base1/2 bounds the first term by exp[-(1-log2)mu/2]<=exp(-mu/8); base2 bounds the second by exp[nu-(log2)mu/2]<=exp(-mu/16). The elementary inequalities2/3<=log2<=3/4 suffice. Thus(2.3), m>=n/2 and z exp(-z)<=1 give

    lambda P(E_K,Y_n=11)
       <=6 delta exp(-m delta/16)/sqrt(beta)
       <=192/(n sqrt(beta)).                      (4.3)

Combining the two branches bounds the contribution from Y_n=11 and any future terminal00 at time M>=n by

    8K/n+192/(n sqrt(beta)).                       (4.4)

For Y_n!=11, the event E_K implies J_(Y_n)<=K. Accepted SC003's universal four-state terminal-occupation inequality, valid for arbitrary initialization, gives

    P(E_K,Y_n!=11)<=16(K+1)/(n+1).

Multiplying by a<=1 and discarding the future-terminal restriction can only increase the bound. Therefore, for every M>=n,

 E[a 1{E_K,Y_M=00}]
       <=min{1,24K/n+208/(n sqrt(beta))}.           (NP3)

For K>n/2 the displayed right side is1 and the claim is immediate, so(NP3) holds for every integer K>=0. The Markov transition from time n to M is used only in the Y_n=11 term through(2.2); the probability at Y_n is not claimed stationary.

## 5. Zero counts, arbitrary corruption and predictor loss

If at most z of X_1,...,X_(n+1) are zeros, then at most2z of the pairs Y_0,...,Y_(n-1) differ from11: each zero is in at most two such pairs. Apply(NP3) with K=2z to get

 E[a 1{Y_M=00, prefix zero count<=z}]
       <=min{1,48z/n+208/(n sqrt(beta))}.           (5.1)

Symbol exchange gives the same bound for a near-zero prefix and terminal11, weighted by tau.

A strict-k attack changes the zero count of this prefix by at most k, pointwise, even if edits are adaptive, adjacent or randomized. The final pair is protected. Thus an observed veto at00 implies that the original clean prefix has at most h+k zeros and the original terminal pair is00. Replacing any baseline estimate by0 increases binary TV loss by at most a. Apply(5.1), and add the exchanged terminal11 bound. For M>=128 (so n>=64), the risk increment is at most

    min{1,96(h+k)/n+416/(n sqrt(beta))}
       <=min{1,288(h+k)/M+1248/(M sqrt(beta))},

using n=floor(M/2)>=M/3. This proves(NP1). For64<=M<128 its displayed upper bound is1, which trivially bounds the increment. No clean history, k, Pi or parameter is used by the predictor.

At beta=1/M and M>=64, h<=9sqrt(M)/8. The preceding expression is at most1572/sqrt(M)+288k/M, which is below the constants in(NP2). At beta>=c/M, replace1248/sqrt(M) by1248/(sqrt(c M)).

## 6. Boundary stationary supports and unsupported starts

Under positive all-state beta, a qualifying stationary law either has full support or is concentrated at an absorbing diagonal: this is the classification checked in SC003 and again in CB001. The latter cases are handled directly, without using any full-support formula.

More generally, for an absorbing diagonal v and the opposite terminal diagonal u, the chain avoids v throughout the observed history. For example, if11 is absorbing and Y_M=00, then no pair11 occurs before M. Hence E_K is impossible when K<n (all n departures are non11). For K>=n, (NP3) is already trivial. If00 is absorbing, a=0. This proves(NP3) for both singleton supports. Its symbol-exchanged version follows identically. Consequently the zero-count reduction and corruption argument remain valid for arbitrary starts, including every unsupported state. No division by a,b,e,tau or stationary mass is used in these cases.

## 7. Exactly what remains open

W is a computable, k/beta-blind, order-sensitive veto whose ADDITIONAL loss is controlled by the known critical-curve order under arbitrary strict-k corruption. It outputs0 on all BK001/BK002 attack supports described in CB001, because their initial long run lies inside the tested prefix. It also tolerates up to h scattered opposite symbols there, unlike an exact-run test.

This does not solve the full adaptation question: R(A,C) in(NP1) may still be too large outside the veto. In particular, an attacker with k much larger than sqrt(M) can spend h+1 edits in the initial prefix to bypass this fixed threshold; this is a route to investigate, not a proved lower for W(A). Raising h arbitrarily would charge h/M on clean data and lose the statistical-rate guarantee. A useful successor is a multiscale or transition-pattern test with a clean error bound, rather than claiming that one near-prefix threshold supplies all-budget adaptation.

## 8. Provenance and validation status

The accepted SC003 model and universal terminal-occupation inequality are the only imported quantitative premises. SC003's exact receipt/hash are checked separately. The diagonal-trace probabilities and independent-stack event inclusion are proved above; the earlier unreviewed macrocycle note suggested this direction but is not used as an accepted theorem. AB003 is used only for the statement about preserving its existing small-budget guarantee. BK001/BK002 enter only the support comparison inherited explicitly from CB001. Fresh review and diagnostics are required before acceptance; no formal/external review, publication, efficiency beyond a linear scan, neural/training or novelty claim is made.
