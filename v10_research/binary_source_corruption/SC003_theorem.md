# SC003 — Binary full-history source-corruption upper with square-root-beta cutoff

2026-11-02. POST-STAGE7 author candidate. Fresh independent review and root acceptance required. No frozen artifact is changed.

## Result first

Fix K=2, integer M>=64, integer 0<=k<=M and beta in [0,1]. Use exactly SC002's source-corruption experiment, now with binary symbols: a homogeneous second-order source with arbitrary unknown initial pair distribution and an existential stationary pair law Pi satisfying P²(i,j)>=beta Pi(j) on ALL pair states. Before any encoder, one offline randomized history-adaptive kernel replaces at most k symbols among positions 1,...,M of the M+2-symbol word. The final pair is preserved. The predictor sees the entire corrupted word, but not clean interior symbols, edit mask, attack seed, source law, Pi, or initial law. Risk is unconditional TV from the true next-symbol law at the actual preserved terminal pair. Kernels are maps on full histories, not supplied the unknown source parameter. Public k MAY be used by the predictor.

Let R_all and R_stat denote minimax risks, with arbitrary and stationary initialization respectively. Put s=M^(-1/2), e0=max(sqrt(beta),1/M), and

    F=(k/M)[1+ln(1+1/(k e0))], k>=1; F=0 at k=0.

Then a deterministic beta-blind, k-aware finite rational full-history estimator satisfies

    max(s,k/M)/96 <= R_stat <= R_all
       <= min{1, 2^17 s + 2^19 F}.                    (SC3)

The lower and upper need NOT match when the logarithm grows. In particular this is NOT a complete binary logarithmic minimax frontier. For every fixed beta>0, both risks are Theta_beta(max(s,k/M)); the implicit upper constant may depend on beta. At beta=1/M the upper has sqrt(beta), not beta, as its cutoff. No global sqrt(beta) mixing theorem is asserted.

## 1. The estimator and its four fixed orientations

Write Y_j=(X_(j+1),X_(j+2)), j=0,...,M. Triple counts use ONLY departures j=0,...,M-1. The canonical successor bit d(u), and its TRUE probability q_u, are

    u=00: d=1, q=a=theta00(1);
    u=01: d=1, q=b=theta01(1);
    u=10: d=0, q=e=theta10(0);
    u=11: d=0, q=t=theta11(0).

These orientations are public functions of the state, not of the unknown probabilities: d(u) is the complement of its first bit. In particular no minority test or source-dependent preferred exit is needed. The symbols a,b,e,t and the clean counts below are analysis variables only.

Count the corrupted triples. At the preserved terminal state u, let C' be the corrupted count whose successor equals d(u), and J' the corrupted total row count. For k>=1 set B=6k and output the rational binary vector with designated coordinate

    qhat=(C'-B)_+/(J'+B+2),

and other coordinate 1-qhat. For k=0 output ordinary selected-row add-one, (C'_ub+1)/(J'+2) for both successor bits. Both branches are beta-blind, deterministic maps of the entire corrupted word and public M,k. The output belongs to the simplex because 0< J'+B+2 and 0<=(C'-B)_+<=J'.

## 2. Pathwise robust lower envelope; no transferred purity assertion

Let C,J denote the corresponding CLEAN exit count and clean row mass. Every symbol replacement changes at most three triples, each with histogram l1 change at most two. Thus the complete triple histogram changes by at most 6k=B, and its selected two-coordinate row obeys

    |C'-C|+|(J'-C')-(J-C)|<=B.

This holds for arbitrary simultaneous adjacent replacements and every attack realization. It uses preservation of the terminal pair to select the same clean and corrupted row.

Set D=J+2 and D'=J'+B+2. Then D' >=D, |J'-J|<=B, and (C'-B)_+<=C. Consequently

    0<=qhat<=C/(J+2).

For n'=(C'-B)_+, we have 0<=C-n'<=2B and 0<=D'-D<=2B. Therefore

    C/D - n'/D' = (C-n')/D + (n'/D')(D'-D)/D
       <=4B/D.                                      (2.1)

For J>0 write p=C/J. Since p-C/(J+2)=2p/(J+2),

    0<=p-qhat<=min(p,(4B+2)/(J+2)).                  (2.2)

The map x↦min(x,c) is 1-Lipschitz on nonnegative reals. Taking A=4B+2=24k+2 and q=q_(Y_M), (2.2) gives

    |qhat-q|<=2|p-q|+min(q,A/(J+2)), J>0.             (2.3)

For J=0, C=0 and qhat=0; since A>=2 the second term equals q and pays the loss exactly. Hence on every complete clean/corrupted history,

    TV(output,theta_(Y_M))
       <=2 1{J>0}|p-q|+min(q,A/(J+2)).               (2.4)

This is a new robust lower envelope, not an import of a quantization zero-purity lemma. Corruption may create false exit counts, but subtracting B removes their possible positive contribution. At a true q=0 row, C=0 almost surely and this estimator indeed gives qhat=0; the proof requires no access to q or knowledge that it vanishes.

## 3. Statistical comparator and general occupation interface

Let S be expected actual-terminal loss of ORIGINAL clean binary add-one. Accepted R011 gives, uniformly over all beta and initial laws,

    S<=8192 sqrt(32)/sqrt(M+1).

For J>0 its designated coordinate is (C+1)/(J+2), and

    |p-(C+1)/(J+2)|=|2p-1|/(J+2)<=1/(J+2).

The universal terminal occupation bound on the four-state pair chain is

    P(J<w)<=min(1,16w/(M+1)), integer w>=1.

It implies E[1/(J+2)]<=sqrt(32)/sqrt(M+1), as also recorded in accepted BIF001 §4 (with its factor-two B0). Thus

    E[1{J>0}|p-q|] <=(8192+1)sqrt(32)/sqrt(M+1).       (3.1)

No empirical row is claimed IID after terminal conditioning.

For A>0 and every chain/start, layer cake and the same integer threshold give

    E min(1,A/(J+2))<=Psi(16A/(M+1)),                (3.2)

where Psi(x)=x(1+ln(1/x)) for 0<x<1 and Psi(x)=1 for x>=1. At layer height v, the nonempty event has J<A/v-2 and uses integer threshold ceil(A/v-2)<=A/v. Formula (3.2) is therefore valid also when J=0. Psi is increasing.

## 4. Weighted occupation: full support, singleton support, and weak beta

Let V=min(q_(Y_M),A/(J+2)) with the FOUR TRUE probabilities from §1, A=24k+2. These weights are analysis only. We import occupation statements, not BIF's precision estimator or quantized-bank risk theorem.

### Full stationary support and beta>=M^-2

Accepted BIF001 §3, equation (3.4), gives for EVERY initial distribution and EVERY A>0,

    E V<=4s+(16672 A/M)[1+ln(1+1/(sqrt(beta) A))].     (4.1)

Its proof uses arbitrary diagonal starts and first diagonal hitting from crossing starts. In the small crossing-hazard case it crucially uses q01=b and q10=e, exactly our designated coordinates, not unit crossing caps. It does not assert fast global marginal mixing or require stationary initialization. Its suffix horizons are all valid even if beta times squared suffix length is below one.

For k>=1, k<=A<=26k and e0=sqrt(beta). Thus the logarithm in (4.1) is at most 1+ln(1+1/(e0 k)), and

    E V<=4s+433472 F.                               (4.2)

### Positive beta with non-full stationary support

For completeness, stationarity gives Pi=(y,x,x,w), ya=xe and wt=xb. If x>0, P²(10,01)=ea>=beta x and P²(01,10)=bt>=beta x force a,b,e,t>0, hence y,w>0. Otherwise stationary mass lies on absorbing diagonals. Two such diagonals cannot both have positive mass under the all-state positive certificate. Thus the remaining case is one absorbing diagonal, but the initial state can still be any transient or unsupported state.

For absorbing 00, accepted BAI003 v2 §6, equation (6.2), with the same q=(0,b,e,t), gives

    E V<=256 max(A,1)/M+16/(M+2)
       <=6672 k/M<=6672 F, k>=1.                    (4.3)

For absorbing 11, exchange symbols. This permutes q as (a,b,e,t)↦(t,e,b,a) and exchanges the designated bits, so it is the SAME fixed-orientation estimator and weighted functional, not a law-dependent estimator branch. This covers all boundary row probabilities and arbitrary initial mixtures. Equation (4.3) needs no beta-size condition.

### Weak certificate 0<=beta<M^-2

No support classification or positivity assumption is made. Here e0=1/M. Since A<=26k, (3.2) yields

    E V<=Psi(416 k/M)<=416 (k/M)[1+ln(1+M/k)]
       =416 F.                                     (4.4)

To verify the scalar inequality, put z=M/k>=1. For z<416, the right side is at least 416/z>1. For z>=416, Psi(416/z)=(416/z)(1+ln(z/416)) <=(416/z)(1+ln(1+z)). Equality beta=M^-2 belongs to the strong case. beta=0 has no singular denominator.

## 5. Assembly, endpoints, and finite algorithm costs

For k>=1 combine (2.4), (3.1) and (4.2), or the smaller bounds (4.3)/(4.4). Since

    2(8192+1)sqrt(32)+4 <2^17,
    433472 <2^19,

the upper in (SC3) follows, capped by the unit TV bound. For k=0 use the clean add-one branch and its bound in §3; set F=0, without evaluating a singular logarithm. M=64, beta=0, beta=M^-2, beta=1, k=1 and k=M are all included. No stationary-support test is performed by the algorithm; those cases exist only in the proof.

A simple exact rational implementation is enough here. Read and retain the M+2 corrupted input bits, identify the final pair, then scan its M preceding triples and increment two selected-row counters. Counters, k,B and the output numerator/denominator have O(log(M+2)) bits since k<=M. Increment, comparison, subtraction and copying require O(M log(M+2)) elementary bit operations conservatively, and O(M+log(M+2)) total live bits including input/output and fixed algorithm description/counters. The two rational coordinates can share denominator D'=J'+B+2 with numerators n' and D'-n'; neither division nor approximate real arithmetic is necessary. The k=0 branch similarly outputs denominator J'+2 and add-one numerators. Reading/copying/serializing input/output and public k is included. This is a full-history sequential rational algorithm, NOT a bounded-neural-depth or attention-budget result, and has no retained quantized-bank restriction.

## 6. Only the valid binary lower floors

Both lower floors use stationary binary IID sources, whose pair kernel satisfies P²=1Pi on ALL four states. They therefore lie in every beta class, including beta=1. The actual terminal target is Bernoulli(p) at all rows.

For the clean floor use identity corruption and p±=1/2±1/(16sqrt(N)), N=M+2. Their one-letter KL is at most 32/(256N), hence full-history KL<=1/8 and TV<=1/4. Nearest-target testing gives average estimation loss >=3/(128sqrt(N))>=s/64 for M>=64. This is a full-history lower and does not restrict the estimator's computation or knowledge of k.

For the corruption floor use one prior p uniform on [1/4,3/4] and one common source-independent kernel. Among the first M binary symbols, if n are ones, retain r=(k+1)floor(n/(k+1)) ones chosen uniformly and change the others to zero. Preserve the final two symbols U. This changes at most k bits. Conditional on r the retained arrangement is uniform among weight-r strings, independently of p: the probability of a specified such output conditional on n is

    binom(M-r,n-r)/[binom(M,n)binom(n,r)]=1/binom(M,r).

Thus the FULL corrupted word factors through (r,U), at most 4(floor(M/(k+1))+1) messages, followed by a parameter-independent channel. For a uniform prior on an interval of length ell, any D-message experiment with arbitrary randomized decoding has absolute-error Bayes risk at least ell/(4D): the union of D radius-v output neighborhoods covers prior mass at most 2Dv/ell, and integration proves the bound. Therefore, with b=k+1,

    risk>=1/[32(floor(M/b)+1)]>=b/[32(M+b)]>=k/(96M).

The protected bits are part of the message, not conditioned away. Taking the maximum of these separate lower witnesses gives max(s,k/M)/96. No three-symbol rare-suffix witness is transplanted into a binary alphabet.

## 7. Remaining gap and provenance

For fixed beta>0, 1+ln(1+1/(k e0))<=1+ln(1+1/sqrt(beta)), so (SC3) gives the fixed-beta order claimed at the start. In weak/moving-beta regimes, no matching logarithmic binary source-corruption lower is proved. The accepted precision lower cannot serve as one: it restricts a retained representation, whereas here all corrupted symbols are visible. Binary active-core trajectories may encode parameter information through their timing and variable two-/three-step cycles; uniform deletion of IID fixed-position ones does not establish erasure of those Markov trajectories. Exact parameter-independent full-word transport would be a separate theorem. This gap remains open.

Read and imported: accepted SC001/SC002 experiment and common-kernel IID argument; their receipts (SC002 08:38:34 UTC); BIF001 complete proof and receipt for (4.1) and universal comparator/count facts; BAI003 v2 complete proof and receipt for (4.3); ORIGINAL R011 full statement/assembly for clean add-one. Version-specific source and receipt hashes are recorded separately. Independent finite diagnostics corroborate only their tested instances. This manuscript makes no external novelty, formal-verification, publication or contact claim.
