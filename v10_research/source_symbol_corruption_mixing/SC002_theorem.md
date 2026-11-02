# SC002 — full-history symbol-corruption frontier under two-step mixing

2026-11-02. POST-STAGE7 author candidate; independent review and root acceptance pending. SC001 and all frozen deliveries are unchanged. No novelty or formal-verification claim.

## Result and experiment

Fix integers K>=3, M>=64, 0<=k<=M and real beta in [0,1]. A homogeneous second-order K-letter source has pair transition P((a,b),(b,c))=theta_ab(c) and an existential stationary pair law Pi with P²(s,t)>=beta Pi(t) for EVERY pair s,t, including off support. Observe M+2 symbols. Before any encoder, an offline randomized corruption kernel C replaces at most k symbols in positions 1,...,M and leaves positions M+1,M+2 untouched. It is a stochastic map on complete observed words with no input theta, Pi, initial law, future symbols or hidden parameter. It may depend on public K,M,k. No edit mask, clean interior or attack seed is supplied. Prediction sees the ENTIRE corrupted word, allows arbitrary independent randomization/computation, and is assessed by unconditional expected TV against the TRUE theta at the preserved actual terminal pair.

Write R_all=inf_A sup_(theta,mu in D2(beta)) sup_C E TV and R_stat for the restriction mu=Pi. The supremum notation alone does not require the maximizing C to be the same at different sources; every lower family below nevertheless uses ONE common C across all its unknown parameters, even if the decoder knows that C and family. This stronger lower is not conflated with the nested minimax definition.

Set beta0=max(beta,1/M), s=M^(-1/2), and, for k>=1,

    epsilon=k/M, F=epsilon[1+ln(1+1/(beta0 k))].

For k=0 define F=0. Let H=min(1,max(s,F)). Then

    2^(-15) H <= R_stat <= R_all <= C_K H,             (SC2)
    C_K=2^13 K^(5/2)+12K²(17+ln80)+60K^4.

Thus both risks are Theta_K(H), uniformly over the entire stated finite domain. A single deterministic beta- and k-blind corrupted-row add-one estimator attains the upper up to C_K. No binary, joint-K-sharp, causal-online, visible-mask/seed, edited-terminal-pair, internal-network-precision, or computational-budget theorem is asserted.

## 1. Pathwise reduction and inherited clean risk

Let C_abc be the M clean triple counts and C'_abc their corrupted counterparts. One changed symbol affects at most three triples, so ||C'-C||_1<=6k. Clean and corrupted selected rows agree because the terminal pair is untouched. Let J be the clean selected-row mass and q,q' its clean/corrupted add-one vectors. For nonnegative vectors u,v of positive masses A,B, insertion of v/A and |A-B|<=||u-v||_1 give TV(u/A,v/B)<=||u-v||_1/A. Hence, pathwise,

    TV(q',q)<=min(1,6k/(J+K)).                         (1)

This includes changed row membership and arbitrary attack randomness. Accepted R011 ORIGINAL gives E TV(q,theta)<=2^13 H_R011 with H_R011=max(a,D,T)<=K^(5/2)/sqrt(M); the letter H_R011 is unrelated to the SC2 profile H. Thus only the expectation of (1) remains. For k=0 it is zero and no singular logarithm is used.

We use accepted IU001 Lemma 4.1: for a stationary m-transition pair path, d=|supp(Pi)|<=K², A>0 and integer kappa>=1,

    E_Pi min(1,A/(J_m+kappa))
       <=(d A/m)[17+ln(1+480/(beta A))], beta>0.        (2)

This is conditional actual-terminal reverse-return analysis, not an independent-query or IID-row formula. Accepted AU001 §§2–3 also supplies, for ANY initial law nu,

    E_nu min(1,A/(J_m+kappa))<=Psi(K^4 A/(m+1)),        (3)

where Psi(x)=x(1+ln(1/x)) for 0<x<1, Psi(0)=0, and Psi(x)=1 for x>=1. Its universal occupation proof uses P(J_m<w)<=min(1,K^4 w/(m+1)) and the strict integer threshold ceil(A/t-kappa)<=A/t.

## 2. Arbitrary-start upper without additive burn error

For beta>0 set u=floor(M/2), m=ceil(M/2), r=floor(M/4), eta=(1-beta)^r. At 0<beta<1, R=(P²-beta 1Pi)/(1-beta) is stochastic on ALL pair states, Pi R=Pi, and

    mu P^u=(1-eta)Pi+eta nu,
    nu=mu R^r P^(u-2r).

Extending both initial laws with the ordinary kernel P gives an exact mixture of ENTIRE suffix trajectories Y_u,...,Y_M. The residual trajectory uses P, not R. At beta=1, P²=1Pi and eta=0, so the residual is omitted. The full count J dominates the suffix count with the same actual endpoint. Applying (2),(3) with A=6k,kappa=K therefore gives

    E min(1,6k/(J+K))
      <=12K² epsilon[17+ln(1+80/(beta k))]
          +eta Psi(12K^4 epsilon).                   (4)

No estimator is conditioned on a synthetic regeneration event; the suffix is only an analysis object.

For beta>=1/M put z=M/k>=1, t=M beta>=1, D=12K^4, and G=1+ln(1+z/t), so F=G/z. Since eta<=1 and eta<=e exp(-t/4), the AU001 scalar proof applies directly. If z<D, eta Psi(D/z)<=1<=D G/z. If z>=D,

    eta Psi(D/z)<=(D/z)eta(1+ln z),
    ln z<=ln(1+z/t)+ln t,
    eta(1+ln z)<=G+e exp(-t/4)ln t<=G+4<=5G.

Thus the residual is <=60K^4 F. Also ln(1+80x)<=ln80+ln(1+x), so the first term in (4) is <=12K²(17+ln80)F. For 0<=beta<1/M use (3) directly on the full history: Psi(6K^4 k/(M+1))<=Psi(6K^4/z)<=6K^4[1+ln(1+z)]/z=6K^4 F. The elementary last inequality follows separately from z<6K^4 and z>=6K^4. This includes beta=0 without division by beta.

Adding the clean risk proves risk(q')<=min(1,2^13 K^(5/2)s+[12K²(17+ln80)+60K^4]F). Since C_K>=1, this implies the upper in SC2, including max(s,F)>=1 and k=M. Stationary initialization is a subclass and needs no separate estimator.

## 3. Exact erasure and finite-message lemma

For l IID Bernoulli(p) bits with count n, put b=k+1, r=b floor(n/b), and choose uniformly n-r one positions to change to zero. At most k changes occur. For a fixed output word z of weight r, conditional on n its probability is

    binom(l-r,n-r)/[binom(l,n)binom(n,r)]=1/binom(l,r).

Consequently, conditional on r, the output arrangement is uniform and independent of p. With two additional untouched IID bits U, the ENTIRE resulting word is generated from (r,U) by a p-independent uniform-arrangement channel. It has at most D_l=4(floor(l/b)+1) messages, including l=0 and incomplete last cells.

For p uniform on an interval of length ell, any channel with at most D messages and any randomized real estimator has expected absolute error >=ell/(4D). Indeed fix decoding randomness, giving D possible output points; radius-t balls have total prior mass <=2Dt/ell. Integrate the complement on 0<=t<=ell/(2D), then average randomness. Stochastic encoding is permitted. Thus ell=1/2 yields error >=1/[32(1+l/b)]. The random arrangement is ancillary; composition with its channel reduces every full-word decoder to such a randomized finite-message decoder. The actual attack seed is not revealed.

## 4. IID floors, valid for every beta

Use the stationary IID source supported on C0,C1 with probabilities 1-p,p, with ALL symbol rows equal to this law, including unused symbols. Then P² has all rows equal to stationary pair law, so it belongs to D2(1) and therefore every D2(beta).

For the corruption floor use p uniform on [1/4,3/4]. On any all-binary word, round the ones among its first M symbols as in §3 and preserve the final two; on every other word use identity. This is one common source-independent kernel. The whole output factors through at most 4(floor(M/b)+1) messages. Its actual future law is Bernoulli(p), giving

    R_stat >=1/[32(floor(M/b)+1)]
           >=b/[32(M+b)]>=k/(96M), k>=1,              (5)

since b<=M+1<=2M and b>=k.

For the clean floor use identity corruption and p_±=1/2±1/(16sqrt(N)), N=M+2. For these Bernoulli laws KL(p_+||p_-)<=32/(256N); product KL<=1/8 and Pinsker gives product TV<=1/4. Their target TV distance is 1/(8sqrt(N)). Nearest-target testing and triangle inequality give average loss at least distance*(1-TV)/4>=3/(128sqrt(N))>=s/64 for M>=64. This is full IID data, not a compressed-observation lower. It also applies at k=0.

## 5. Weak-beta stationary rare suffix

Assume beta0<=1/16. Let a=1/(2M), e=beta0-a, and p uniform on [1/4,3/4], p_0=1-p,p_1=p. Use symbols W,C0,C1 and define

    T(W,W)=1-a, T(W,Ci)=a p_i,
    T(Ci,W)=e, T(Ci,Cj)=(1-e)p_j,
    pi(W)=e/beta0, pi(Ci)=a p_i/beta0.

Unused pi masses are zero and unused starting-symbol rows equal pi. All parameters are legal: 0<a<=beta0/2, 0<e<=1/16. Directly pi T=pi. For all starting symbols y and target symbols v, T(y,v)>=beta0 pi(v): W-to-active and active-to-W ratios equal beta0; remaining supported inequalities reduce to beta0<=1; unused rows equal pi, and zero columns are automatic. Set theta_(x,y)(v)=T(y,v) for EVERY pair and Pi(u,v)=pi(u)T(u,v). Then Pi P=Pi and on ALL pair states

    P²((x,y),(u,v))=T(y,u)T(u,v)
       >=beta0 pi(u)T(u,v)=beta0 Pi(u,v)>=beta Pi(u,v).

Initialize at Pi itself. This is a legitimate stationary member even though Pi is unknown and depends on p. Its initial WW mass Pi(W,W)=(1-a/beta0)(1-a)>=1/4 is independent of p.

Let L=floor(1/(4beta0)); then 4<=L<=M/4. For j=2,...,L let E_j be the complete word W^(M+2-j) followed by j active letters, with no return. These disjoint events have p-independent weight

    w_j=Pi(W,W)(1-a)^(M-j)a(1-e)^(j-1).

Bernoulli's inequality gives (1-a)^(M-j)>=(1-a)^M>=1/2 and (1-e)^(j-1)>=1-beta0 L>=3/4. Hence w_j>=3/(64M)>=1/(32M). Conditional on E_j the j active bits are IID(p), and the SAME prior remains uniform before observing protected endpoint labels.

Use SC001's common marker kernel: on any word W^(N-j) followed by j active symbols, 2<=j<=M, round the count of ones among its first j-2 active symbols with b=k+1; preserve the entire marker prefix and final two bits. On all other words use identity. This is defined on every input, uses neither p nor beta, preserves j, and edits at most k positions outside the final pair. Complete output conditional on E_j factors through (r,U) with D<=4(floor((j-2)/b)+1). Exact j may be granted; it is already visible.

At EVERY active terminal pair the ACTUAL future law is

    e delta_W+(1-e)[(1-p)delta_C0+p delta_C1].

The future return mass e is not dropped merely because no return occurred in the selected past. Since TV(q,theta)>=|q(C1)-(1-e)p|, apply §3 to the real estimator q(C1)/(1-e). As 1-e>=1/2, conditional Bayes risk is >=1/[64(1+(j-2)/b)]. Thus, discarding only nonnegative risks outside the disjoint events,

    R_stat >= b/(2048M) ln(1+(L-1)/b).                (6)

The sum-to-integral bound uses l=0,...,L-2. If A=1/(4beta0)>=4, floor(A)-1>=A/2, so L-1>=1/(8beta0). The function b ln(1+c/b) increases in b>0, and log concavity gives ln(1+x/8)>=ln(1+x)/8. Since b>=k,

    R_stat >=epsilon ln(1+1/(beta0 k))/16384.         (7)

No k² concentration cutoff or parameter-dependent kernel occurs. Whole histories outside the events remain visible; their losses are simply nonnegative. The single prior and single kernel across all p justify the source-supremum Bayes lower; no source is selected separately for each j.

## 6. Assembly and endpoints

For beta0<=1/16, combine (5) and (7): max(epsilon/96,epsilon log(1+1/(beta0 k))/16384)>=F/32768. For beta0>1/16 and k>=1, log(1+1/(beta0 k))<=ln17<3, so F<=4epsilon and (5) gives R_stat>=F/384>=F/32768. Combine with s/64 to get R_stat>=2^-15 max(s,F), which implies the stated capped lower. k=0 uses only the clean floor. beta=0, beta=1/M, beta=1/16, beta=1, k=1, k=M, and M=64 are all covered by these explicit cases.

The two different corruption witnesses need not use the same kernel as each other: each establishes a lower against its own fixed common kernel across its full parameter family. Their maximum is legitimate. No sum of risks from unrelated sources is taken.

## 7. Provenance and preserved diagnostics

Directly read: SC001 full theorem, stationary corollary and full independent review; SC001 acceptance receipt; IU001 complete proof and review; AU001 complete proof and review; IU/AU acceptance receipts; R011 full theorem/assembly; IP002 stationary family and event calculation (§§2–3). Only IU/AU occupation/residual lemmas and R011 ORIGINAL are inherited analytic interfaces; SC001 erasure is re-proved here. IP002 supplies the source template, not its precision-limited lower.

Rejected route retained: importing IP002's Q-dependent concentration cutoff or SC001's earlier j=O(k²) tube would unnecessarily lose the full logarithm. Exact arrangement ancillarity eliminates that cutoff. A bare additive mixing burn error is valid but insufficient for the sharp frontier; exact residual suffix occupation removes it. No failed counterexample was suppressed; finite tests and independent review are separate artifacts. No external prior-art search is needed for this elementary assembly, and novelty remains unassessed.
