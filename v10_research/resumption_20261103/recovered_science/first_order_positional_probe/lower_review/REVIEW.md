# FOL001 independent adversarial lower-proof audit

Date: 2026-11-02. Reviewer: independent LLM reviewer.

## Verdict and limits

**PASS: no blocking mathematical defect found in the finite theorem (1) or its stated logarithmic competitive consequence.** This verdict concerns the exact candidate bound to `MANIFEST.json`, not an upper theorem, not exact-oracle normalization, and not the prior second-order/triple-count experiment. It is an independent universal proof audit; finite enumeration below is corroboration only. Root retains acceptance/integration authority. The candidate and its existing checks were not edited or rerun in place.

Read in full: `../PLAN.md`, `../lower/FOL001_candidate.md`, and the author's finite check source. The proof audit below was rederived directly from the binary first-order model rather than importing an old family. No external write or network operation was performed.

## 1. Experiment and quantifiers

There are N transitions on N+1 symbols. A predictor observes four pair counts and the first/last r symbols of the possibly edited word, predicts the next-symbol law at the actual protected terminal state, and incurs unsquared TV. On a binary row with probability a of next symbol 1, that loss is absolute error from a. One terminal symbol, not a pair, is protected. Alternatives and null are stationary members of the all-table, arbitrary-start class; no certificate is used.

The finite result is about each fixed, k-blind predictor. Its common kernel may depend on N,k,r and a predeclared auxiliary family but not the unknown actual source. This is precisely satisfied here. Read together with the PLAN, Gamma is a supremum over integer budgets 0<=k<=N, stationary sources and admissible kernels of the rate-normalized risk of that fixed predictor. The literal displayed definition in candidate section 6 abbreviates the index as sup_{k,...} and should explicitly print this finite integer domain; the proof here establishes the stronger correctly domain-restricted assertion because it uses only k=0 and its legal constructed integer k<=N/8. It is not itself an infimum over predictors. Establishing the same bound for every fixed predictor permits taking an infimum afterward, without assuming an optimizer exists. The all-start class only enlarges the supremum. If Gamma is infinite, the final inequality is immediate.

## 2. Skeleton and mixture, universally

For a path starting 1 and ending 0, U=u implies u completed zero visits plus one terminal zero visit and N10=u+1. There are j zero departures: exactly u exits and j-u zero self-loops. Erasing every zero departure leaves H=N-j transitions from state 1, of which the final retained transition is a 10 and u earlier retained transitions are marked 10s whose erased 01 exits will later be restored. Choose these u marked positions among H-1. The other H-1-u transitions are 11. The retained weight is therefore

`t * binom(H-1,u) * t^u * (1-t)^(H-1-u)`.

Allocate the j-u zero self-loops among u+1 visits: stars-and-bars gives binom(j,u). The terminal visit legitimately receives loops, although the final symbol is not a departure: such loops occur after its retained entry and before the horizon endpoint. Restored factors are a^u(1-a)^(j-u). Multiply by the initial stationary mass pi1=a/(a+t). This proves (2), including the otherwise easily missed pi1 factor.

For u>=1, multiplying by da/a gives the beta integral normalization binom(j,u)B(u,j-u+1)=1/u, with the remaining pi1 inside its expectation. Consequently it is bounded above by 1/u. Summing the nonnegative h over all admissible u gives t by the binomial theorem, not approximately t. Restricting to any interval and any additional possibly parameter-dependent event only decreases mass. This proves (3); u=0 is never divided by. No random horizon has been averaged away.

## 3. Relocation and exact offsets

With l=r-1 and h=N-r+1, precisely 2r-2 boundary edges are frozen. Deleting interior self-loops retains the crossing skeleton, including its endpoint states. Inserting all removed 11 loops at its first 1 and all removed 00 loops at the first subsequent 0 preserves every crossing and total interior length. Hence edge counts, attachment indices, and both length-r windows are exactly preserved relative to the alternative. Ordered visits ensure the insertion sites exist.

Let A1,A0 be the numbers of inserted loop symbols. Apart from these blocks, the total numbers of ones and zeros in the full N+1-symbol word are respectively o=1+U+f1 and z=U+1+f0. Since J=N00+N01, q=J-A0=U+f0. These identities independently verify the candidate's offsets.

For the abstract block inequality, let b be the number of zeros before the target cut and v the number of ones after it. The total zero-count difference is z-q, so b-v=z-q and distance=b+v. If a distinguished one occurs after the cut, every distinguished zero also does; then b<=z and distance=2b+q-z<=z+q. Otherwise v<=o and distance=2v+z-q<=2o+z-q. If either block is empty the same dichotomy is still valid, with the second case applying when the one block is empty. Thus the bound is universal, not a pattern observed only by enumeration.

Substitution gives z+q=D+2f0 and 2o+z-q=D+2+2f1, each at most D+4r-2. For r=1 this yields D+2 and has no frozen edges. The null target x^(j) has j terminal zeros but only j-1 zero departures. This deliberate J(x^(j))=j-1 offset is correctly handled by labeling null words by their suffix length, not their actual occupation count. For j>=1 the target and transformed word both end 0, so Hamming distance counts only editable coordinates.

## 4. Coupling, covariance, conditioning and good mass

Both transition rows have common atom 1 of mass a. A shared Bernoulli-a regeneration coin gives a geometric meeting time sigma (in state-time indices) with E sigma<=1/a, after which the chains agree forever. Up to N departures, both state counts and directed-edge or crossing-set counts differ by at most sigma: an edge departing before meeting can differ, while all edges departing at or after meeting agree.

For a stationary edge indicator of mean p, conditioning on the earlier edge and contracting the subsequent state law bounds lag-s covariance above by p(1-a)^(s-1), for s>=1. The identical argument applies to a set of edges and, with at least as much contraction, state indicators. Summing covariances gives Var V<=Np(1+2/a)<=3Np/a. No reversibility assumption is needed for this variance calculation.

Detailed balance pi0 a=pi1 t establishes reversibility. Reversal conditioned on F starts at 0 and is conditioned to finish at 1. Contraction bounds its conditioning event E by P0(E)>=pi1-(1-a)^N>=3/4-1/(aN)>=1/2. Here aN>=A0 ck and ck>=1024, so the last bound has substantial slack. Conditioning the entire coupling on E is valid; it need not preserve stationarity of W, because unconditional failure probabilities are first bounded and then divided by P(E).

Writing x=ck, the four unconditional failure bounds are independently obtained as follows:

* Meeting time: 16/(ax)<=16N/(A0 c^2 k^2).
* U concentration: stationary mean Nt a/(a+t) lies in [x/2,x]; Var U<=3x/a; division by (x/8)^2 gives 192N/(A0 c^2 k^2).
* Crossing concentration: mean D<=2ck<=k/64, Var D<=6Nt/a<=6N/A0; threshold D>k/32 is separated by at least k/64, giving 24576N/(A0 k^2).
* Occupation: E J<=N/A0, so P(J>N/16)<=16/A0.

The finite-domain condition makes twice their sum at most

`2256535555 / 274877906944 < 1/16`.

Reversal has J(Z)=J(X)+1 because the departure endpoint is swapped; U(Z)=N10(X)=U(X)+1; D is unchanged. Applying these shifts and the meeting error gives U(X)>=5x/16-1>=x/4, D(X)<=k/32+x/16<=k/16, and J(X)<=N/16+x/16<=N/8. Also U<=J, u0=floor(x/4)>=256, so the required lower J bound follows. Integral J<=N/8 implies J<=floor(N/8).

For the ordered-visit event, the reversed interior must hit 0 and subsequently 1. From either initial state the expectation of the elapsed time is at most 1/t+1/a<=2/t (a hit at the initial time is allowed, but the subsequent distinct-state visit is strictly later). The interval has at least N/2 steps. Markov bounds failure by 4/(tN), and conditioning costs at most two, giving 8/x<=1/128. This argument does not assert endpoint independence.

The union bound yields Q(G|F)>1/2. Reversibility also gives Q(F)=pi0 P0(E)>=pi0/2, hence Q(F intersect G)>=pi0/4. Finally a-beta>=a/2, a pi0>=t/2, and multiplication proves (8), namely (a-beta)Q(F intersect G)>=t/16.

## 5. Null kernel and risk ordering

Under the proposed null, stationary mass at 1 is 2/3, the single 10 jump has probability 1/(2N), the 11 exponent is N-j, and the 00 exponent is j-1. Bernoulli's inequality bounds the prefix by 1/2 and the suffix by 7/8 for j<=floor(N/8), so v_j>=7/(48N)>1/(8N). Its terminal row has next-1 probability beta.

The finite alphabet makes the integrated proposal measures ordinary finite measures. By (3), mu_j<=t/u0. Each eligible input is uniquely identified by its suffix length j. For mu_j=0 use identity; otherwise draw exactly once from nu_j/mu_j. The actual-distance and actual-terminal checks enforce strict legality on every possible input and outcome, including proposals not in G. All other inputs also use identity. The proposal family is fixed in advance, so neither the true source nor predictor randomness is consulted. No acceptance resampling is hidden in the construction.

Every G proposal is accepted, since D+4r-2<=k/16+4r-2<k in the finite domain. Preservation of T_r allows evaluation of the null loss on the untransformed proposal. For positive mu_j, v_j/mu_j>=rho=u0/(8Nt). One must first discard other inputs/rejections, then lower coefficients on nonnegative losses, then restrict to G, and only then apply the potentially signed triangle lower bound. The candidate does exactly this. Zero-mass labels contribute no integral mass. Clean loss on F intersect G is bounded by the full unconditional clean risk S because all losses are nonnegative. Integrating da/a gives L. Nonnegative risk permits the positive part in (1).

## 6. Global finite logarithmic bound

The IID floor is independent of the relocation theorem. Take n=N+1 and Bernoulli parameters 1/2 +/- delta, delta=1/(16 sqrt n). These stationary first-order IID sources have the same next-symbol target at either terminal state. Their n-sample product KL is at most 1/8: explicitly it is n*(2delta)*log((1+2delta)/(1-2delta)), bounded by n*8delta^2/(1-2delta)<=1/8. Pinsker gives TV<=1/4. Nearest-target testing costs at least delta per classification error, so the larger absolute-error risk is at least delta*(1-TV)/2>=3/(128 sqrt n). Dividing by N^-1/2 gives a value greater than 1/96 for N>=64. Observation compression and randomized prediction cannot improve this testing lower bound. Identity at k=0 is admissible.

If ell=1+log((N+1)/r)<64, this floor is much larger than 2^-30 ell. Otherwise log N>=ell-1-log(1+1/N)>62, hence N>2^80. The integer choice k=ceil(max(128r,N^(3/4))) has:

* r<=k/128, k>=N^(3/4), and k/N<2^-19 (use r/N<2e^-63 and N^-1/4<2^-20, including the ceiling error 1/N).
* k<=N/8, ck>2^44, A0t<1/4.
* N/k^2<=N^-1/2<2^-40=A0c^2/2^20.

Thus the finite theorem applies. u0>=ck/8 gives rho>=1/64. The clean k=0 part of Gamma bounds S<=Gamma/sqrt N. The elementary ell<=1+log(2N)<=5N^(1/4), together with the contradiction hypothesis Gamma<2^-30 ell, gives S<5*2^-30 N^-1/4<=t/32. The inequality 1+log(2N)<=5N^(1/4) holds for N>=1: its difference is positive at 1 and has positive derivative.

Since k<=2max(128r,N^(3/4)), L=log(4N/k)>=min(log(N/(64r)),log(2N^(1/4))). The first member is at least ell-8 and the second at least (ell-2)/4; each is >=ell/8 for ell>=64. Also k/N>=N^-1/2, so the budget-k normalizer is exactly k/N. Equation (1) now gives

`Gamma >= (1/64)*(t/32)*(ell/8)/(k/N) = 2^-30 ell`,

contradicting the assumed strict reverse inequality. This proves the assertion for all integer 1<=r<=N+1, including r=1. It is not a statement at every fixed individual budget, nor an equality with an oracle-relative factor.

## 7. Fresh corroboration and provenance

`fresh_checks.py` was independently written in this review directory. Its output `fresh_checks.json` records PASS for 572 exact-rational skeleton/word-mass comparisons, 8,756 window/pair-preserving relocations, 2,047 reversal-shift checks, and 127,111 abstract block inequalities including empty distinguished blocks. Skeleton mass sums and constants are also checked exactly. N=1,...,11 is used only for combinatorial corroboration, not to claim the large-N finite domain was numerically tested.

`MANIFEST.json` binds the reviewed PLAN/candidate/author-check inputs and this review's outputs by SHA-256. No lower-proof repair, added hypothesis, or pending mathematical lemma is required by this audit. Required definition clarification before standalone integration (nonblocking for this PLAN-scoped proof): explicitly print k in {0,...,N} in the Gamma supremum, define the optimal stationary factor as inf_A Gamma(A;N,r) if that factor is used, and retain the pair-count/one-terminal scope warning. The current candidate bytes are preserved; root may request this narrow author clarification separately. This is not an assumption of unbounded k and is not a mathematical repair: every budget used in the proof already belongs to the finite domain.
