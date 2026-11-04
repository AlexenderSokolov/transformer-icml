# Exact-file analytical review: row-tilted occupation and terminal KL

3 November 2026. **PASS for the exact candidate identified below.** No numerical experiments, simulations, sample enumeration, training, repository mutation, external uploads, or implementation runs were performed.

## Exact source and conclusion

- Source: `tilted_occupation_terminal_kl.candidate.v1.md`.
- SHA-256: `c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281`.

The entire frozen file was inspected and its likelihood, concentration, scalar, integration, and summation arguments reconstructed. The stated bound is valid:

    E D_KL(p_{Y_n}||B_{Y_n})
      <=min{log(n+A),
          A^4[log A+1536A(1+floor(log_2 n))]/(n+1)}.

This holds for every finite A>=2 and n>=1 over the stated homogeneous order-two sources and arbitrary initial pair distributions. The separate n=0 bound is log A. For fixed A it gives O_A(log(n+2)/(n+1)). Zero transition probabilities, deterministic rows, reducibility, periodicity, and actual-terminal selection are included.

This analytical review followed discussion of the candidate and its preceding j+1 rescaling. It is not blind external peer review or a claim of independent invention. A separate checker has also been examining the row-tilting mechanism. No conclusion about literature priority follows from these checks.

## 1. Kernel-uniform target occupation

The fixed-target occupation bound is correct for every D-state homogeneous kernel and every initial distribution. For target s, suffix domination makes the maximum over initial states nonincreasing in time. On a deterministic path only its first w occurrences of s can carry the flag. The charging argument, summed separately over all D starting states, gives Dw/(n+1).

It follows that the probability of E_m={Y_n=s,m<=J_s<2m} is at most 2rm, where r=D/(n+1). The fact that this upper bound may exceed one does not invalidate later uses. Its uniformity in the transition kernel is established, not assumed.

## 2. Exact row-tilting identity

For fixed s,b and p in (0,1), changing the b-coordinate to q in (0,1) and scaling all other coordinates by (1-q)/(1-p) gives a legal homogeneous second-order source. Existing zero coordinates remain zero, and the two path laws have the same support. Keeping the initial pair distribution unchanged cancels its likelihood factor.

Every observed departure from s contributes exactly one factor. All other rows cancel. Thus on every positive-probability observed path,

    P(path)/Q(path)=(p/q)^k[(1-p)/(1-q)]^(j-k).

The terminal state introduces no extra factor: the observed likelihood already contains all n transitions, and the departure from the terminal state is not observed or counted.

The logarithmic identity in (6) has the correct sign. When q>p, the coefficient multiplying -(k-jq) is positive, so k/j>=q makes the correction nonpositive. When q<p, both signs reverse and k/j<=q has the same effect. On the relevant event the likelihood ratio is therefore at most exp[-j d(q||p)]<=exp[-m d(q||p)].

Applying the occupation bound to Q gives (7). The proof deliberately keeps the original initial law even when that law was stationary for P. It does **not** assume stationarity for Q. Reusing the improved stationary occupation constant at that step would be invalid; the candidate correctly does not do so.

## 3. Joint deviation bound

For delta=sqrt(2pt/m)+2t/(3m), the binary-KL lower bound in (8) follows from the displayed centered Bernoulli moment bound for either sign. Substitution of lambda=delta/(p+delta/3) is admissible for p>0. Its objective value is delta^2/[2(p+delta/3)]. Expanding delta verifies that this is at least t/m.

On the band J_s<2m,

    J_s sqrt(2pt/m)<=sqrt(4J_spt),
    J_s(2t/(3m))<=4t/3.

Hence exceeding the candidate's random-count threshold implies exceeding the fixed empirical-frequency threshold delta. The two row-tilted tail bounds sum to 4rm exp(-t).

If a proposed q is outside (0,1), the corresponding strict tail is empty. In particular no absolute-continuity assertion at a zero-probability endpoint is silently required. When p=0 or p=1 the observed row count of symbol b is deterministic given J_s, and the deviation event is empty directly.

Different deterministic thresholds may use different tilted kernels. Tail integration only needs a probability bound at each threshold; it does not require one alternative law to represent all thresholds simultaneously. The concentration result is a joint bound for occupancy and error, not a product of two unrelated marginal estimates.

## 4. Scalar forward-KL bound and smoothing

The scalar implication (10)-(11) was checked term by term. The mean/count comparison gives z<=2k+10u/3 and the stated squared error. Since x=(j+1)p, the smoothing displacement p-1 is at most one; no u>=A assumption is necessary.

For a=k+1>=u, h(x,a)<=(x-a)^2/a gives 47u. For a<u, x<6u and a>=1 give 6u log(6u)+u, which is bounded by 48u(1+log u). The proof includes x=0 and j=0.

The scaling identity (12) is also exact. Its remainder

    (A-1)-(j+1)log[1+(A-1)/(j+1)]

is nonnegative, so KL is upper bounded by the sum of the nonnegative scalar h terms divided by j+1. The inequality direction is essential and correct.

## 5. Tail integration and the constant 1536

Taking u=2t makes the scalar deviation threshold precisely the one in the joint bound. For t>=1,

    48(2t)[1+log(2t)]<=192t(1+log t).

Dividing by J_s+1>=m therefore gives f_m(t)=192t(1+log t)/m. The event Z>f_m(t) on E_m is contained in the joint deviation event.

Layer-cake integration at f_m(1) is justified because Z is nonnegative and f_m is strictly increasing to infinity. The initial interval contributes at most

    f_m(1)P(E_m)<=(192/m)(2rm)=384r.

Since f_m'(t)=192(2+log t)/m, the remaining integral is bounded by

    768r integral_1^infinity (2+log t)e^-t dt
       <=768r(3/e)=2304r/e.

Here log t<=t-1 supplies the displayed 3/e integral. Finally e>2 gives 384r+2304r/e<1536r. There is no surviving logarithmic confidence level and no additional union over symbols inside this integral.

This is precisely where the new proof gains over the log-squared argument: the count-band occupation factor multiplies an exponential error tail under an explicitly changed kernel, so it can be integrated before summing bands.

## 6. Counts, rows, symbols, and boundary event

The dyadic bands m=1,2,4,...,2^floor(log_2 n) are disjoint and cover every positive count up to n. Their number is K_n=1+floor(log_2 n). For a selected terminal row, equation (12) bounds loss by A nonnegative scalar terms. Summing their expectations over D target rows, A symbols, and K_n bands gives exactly

    1536 D A K_n r=1536 D^2 A K_n/(n+1).

On J=0 the prediction is uniform and loss is at most log A. Summing the fixed-target w=1 occupation bound gives its D^2 log A/(n+1) contribution. Setting D=A^2 yields the stated A^4 and A^5 factors. The deterministic log(n+A) cap is valid because every add-one coordinate is at least 1/(n+A).

The proof never conditions transition counts to have a binomial law, never resamples the terminal context, and never omits the last observed transition. All likelihood and count calculations use the same observed path.

## 7. Transfer, alphabet dependence, and prior-work scope

The existing exact-real five-block pathwise approximation and output floor give the unchanged entropy-variational transfer

    E D_KL(p_{Y_n}||R)
       <=2V_{A,n}+2A(44A+1)^2/L.

No new architecture or numerical implementation is proved by this note. The true p and the alternative q are analysis-only quantities, not predictor inputs.

For an ordinary D-state chain with D possible next states, the same proof gives a D^3 rather than D^2 alphabet factor. Thus the fixed-A improvement in the rate as n grows does not establish the sharp simultaneous growing-alphabet regime asked about in the cited work. The note correctly distinguishes binary first-order minimax behavior and avoids a claim of optimality in that different case.

For fixed A and order two, the rate in n agrees with the stationary minimax lower order already cited in the preceding research. This says nothing about optimal constants, optimal alphabet dependence, literature priority, or unexamined later publications. Those limitations are expressly retained.

## Verdict

**PASS** for exact source SHA-256 `c42b6f1d86c9c91aa6ba8257a86c613150e6fb477deb549cd70d1e7b79548281`. No mathematical correction was found. In particular the change-of-measure step uses a legal kernel with the same initial law, the occupation factor is valid under that altered law, and all zero-probability and terminal-selection issues are accounted for.
