# BOD001 v1 — fresh hostile independent review

Date: 2026-11-02. **Recommendation: PASS within the stated positive-beta, full-support binary-chain domain. This is not acceptance.** No author or accepted source was edited. The separately generated binding manifest identifies the exact reviewed bytes.

## Scope and dependencies

Reviewed the entire BOD001 v1, BU001 v2, its acceptance receipt and independent v2 review, and BAI004 v3 as context. BU001 v2's hash matches its acceptance receipt. No result in unaccepted BAI004 is assumed: the Schur identity, terminal-count indexing, and cumulative-count argument are independently checked below. The result concerns deterministic initial W and actual terminal C, with true diagonal weight t, and by symbol exchange initial C / terminal W. It does not alone prove a full arbitrary-start risk theorem, beta-zero theorem, or changed predictor.

The domain is integer M>=8, A0>0, transition probabilities in (0,1], full stationary support and a genuine all-state P² minorization with beta>0. Summing a minorization row implies beta<=1. The certificate in fact excludes some parameter endpoints equal to one; treating such endpoints in the hit-density algebra remains harmless. All denominators are positive. No lower restriction on beta M² or A0 is needed here. A trivial additional cap t (or 1) is available but not needed for the displayed un-capped BOD1.

## 1. Mean and killed survival

I rederived the first-step equations hW=1+(1-a)hW+a hA, hA=1+(1-b)hB, hB=1+e hW+(1-e)hA. They give exactly m=[rho+a(2-b)]/(ab), hA=m-1/a, hB=m+1+(e-1)/a. Therefore m<=H<=m+1<=2m, since the W-to-C path needs at least two transitions. Also m b=rho/a+2-b>=1, proving lambda<=b<=rho and lambda<=1/2.

With L=ceil(4m), Markov gives P_i(T>L)<=H/L<=1/2. Conditioning on survival at multiples of L leaves a transient state with the same uniform bound. Thus P_i(T>n)<=2^{-floor(n/L)}. As L<=5m and floor(n/L)>=n/L-1, this is <=2 exp(-lambda n/16), using ln(2)/5>1/16. There is no ceil/floor or first-hitting-versus-return error. At n=0 the slack factor two is legitimate.

## 2. First-hit density, including early times

The killed chain on W,A,B has Q rows (1-a,a,0), (0,0,1-b), (e,1-e,0). Its recurrence A_k=a W_{k-1}+(1-e)(1-b)A_{k-2} gives the displayed convolution for d_n; n=2 is d_2=ab, n=1 is zero. Each W_l is at most killed survival at l, including l=0.

The infinite geometric majorant has ratio (1-rho) exp(lambda/8)<1: exp(lambda/8)<=1+lambda/4 implies its denominator >=rho-lambda/4>=3rho/4. Hence d_n <=(8/3)(ab/rho) exp(lambda/8) exp(-lambda n/16)<=4(ab/rho) exp(-lambda n/16). The independent bound d_n<=b P(T>n-1)<=3b exp(-lambda n/16) is also valid. Taking the weaker common prefactor four and using min(b,ab/rho)/lambda=min(1,a/rho)(rho/a+2-b)<=3 proves constant12. This is an actual uniform phase-type density estimate, not a marginal mixing analogy. All exponents retain the correct n-2 and n-1 shifts.

## 3. Certificate and weighted cumulative count

BU001's sqrt(beta) p t H<=5 applies to exactly this H (ordinary hitting time, zero at C). One can independently verify the needed bound even more directly: from the exact means H<=e/(ab)+2/b+(1-e)/a. With stationary masses y,x,x,w and p=w, wt=xb, ya=xe, we get

    wt H <= y+2x+(1-e)xb/a <= y+2x+b y/e.

The actual minorization entry P²(B,A)=ea>=beta x, combined with ya=xe, gives e²>=beta y. Thus sqrt(beta) wt H<=sqrt(beta)(y+2x)+b sqrt(y)<=2, stronger than the imported5. This rederivation uses full support (e>0), not any unaccepted lemma. Similarly the cited b²>=beta w follows from P²(A,B)=bt>=beta x and wt=xb; it is not itself a literal matrix entry.

The hitting potential satisfies Ph-h=-1+1_C/p at every state. At C this is Kac's return identity; alternatively substituting the above rational h and stationary p verifies it directly. Telescoping times0 through M yields E_C V=p(M+1+E_C h(Y_{M+1})), with a PLUS sign. The M+1 endpoint is correct because V counts times0,...,M. Since H>=m and H>=2, pt(M+1+H)<=5/sqrt(beta)[M lambda+3/2]<=10/sqrt(beta)(1+M lambda). Weight t is retained; replacing this by an unweighted count estimate would not follow from this argument.

## 4. Same-target identity and global harmonic aggregation

Block Schur complementation of I-zP gives det(I-zP)/det(I-zP_{-C})=1-F_C(z). Both determinants have constant term one, so the formal logarithm is legitimate even without analytic convergence. The coefficient of -log(1-F) is sum_k P(tau_k=n)/k. At the kth positive return, the prior count J_C(n) is exactly k: it includes time0 and the first k-1 positive returns, not time n. This proves the reciprocal identity. The trace difference is <=tr(P^n)<=4 because P_{-C} is nonnegative and P is stochastic. Therefore f(n)<=4A0/n for n>=1. This is not claimed for n=0, where f(0)=min(t,A0/2).

For an entire path, the target visits at times0,...,M have earlier counts exactly0,...,V-1. Summing f(n) therefore produces the GLOBAL count cost, without excursion resets or endpoint conditioning. For t>0, apply the usual decreasing harmonic/integral estimate with B=A0/t to obtain sum_{j<V}min(t,A0/(j+2))<=A0[1+ln(1+tV/A0)]. It covers V=0 and arbitrary positive A0, including A0<t. Jensen and the preceding weighted expected-count bound give (4.2). The logarithm is concave in the nonnegative random variable tV.

## 5. Actual terminal convolution and constants

Before the first hit T of C there are no C visits. Conditional on T=r, the suffix starts at C and has prior count exactly J_C(M-r), including the first-hit visit when r<M. If r=M, its suffix prior count is zero, so f(0) is exactly the needed A0/2-clipped term. The convolution sum_r d_r f(M-r) is therefore an equality for the original actual-terminal functional. No independent-query substitution or conditional row-stack independence occurs.

For r<=floor(M/2), M-r>=M/2 and the probability weights sum to at most one, giving8A0/M. For r>floor(M/2), r>M/2 even at odd M, and d_r<=12lambda exp(-lambda M/32). The remaining sum of suffix f's is a sub-sum of the global nonnegative sum in (4.2); there is no multiplicity factor M.

Writing x=Mlambda, s=sqrt(beta)A0, G=1+ln(1+1/s), the logarithm is bounded by G+ln10+ln(1+x)<=4G+x, since G>=1 and ln10<3. The exact maxima are32/e<12 and4096/e²<555. Thus the late term is <=12 A0/M(48G+555)<=7236 A0G/M. The early term makes7244, safely below8192. These inequalities hold for every x>=0 and s>0; no implicit large-M or small-A0 limit occurs.

Symbol exchange sends (W,A,B,C) to (C,B,A,W), and (a,b,e,t) to (t,e,b,a); it preserves the certificate and gives the asserted opposite-diagonal counterpart.

## Independent finite evidence and limitations

`review_BOD001_exact_v1.py` is newly written, independent of author diagnostics. It uses exact Fraction arithmetic for stationary laws, maximal genuine beta, ordinary hit equations, killed powers, first-hit recurrence, survival/density bounds, count-state distributions, trace identities, first-hit functional convolutions, pathwise cumulative functional aggregation, and the finite-time hitting-potential identity. Exponential comparisons use a rational odd Taylor polynomial LOWER bound to exp(-x), so their finite checks are exact and stronger than the asserted envelope; no floating-point transcendental comparisons occur. Several beta-zero endpoint kernels test only beta-independent components. The JSON records actual completed counts. The universal theorem rests on the analytic audit above, not finite testing. No nontrivial large-horizon numerical final-bound stress is claimed.

No counterexample, missing dependency, invalid indexing, or load-bearing proof gap found. The coarse constant is legitimate rather than optimized. Root acceptance and any downstream assembly require their own decisions.
