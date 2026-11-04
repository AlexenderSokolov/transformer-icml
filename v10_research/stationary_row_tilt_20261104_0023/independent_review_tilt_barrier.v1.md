# Independent exact-file review: stationary row tilt and terminal KL

Date: 4 November 2026 (UTC).

## Binding and verdict

Reviewed file: `stationary_terminal_kl.candidate.v1.md`

SHA-256: `1d436719744fd51bda32db723e84932c68507479383154abeb4b9724f2db1337`

**PASS.** The main bound, including the constant 4608, follows from the displayed arguments. The stationary-law comparison and one-count correction repair the same-initial-law obstruction. Section 9 is a valid obstruction to the stated intermediate inequalities, not a KL-risk lower bound. No mathematical correction is required for this exact version.

This is an independent symbolic review of all nine sections. No numerical experiment, simulation, training, external upload, or repository mutation was performed. The candidate was not edited. The previous all-start theorem is not reproved here; the scalar estimate needed from it is reproduced in the candidate and independently checked below.

## 1. Model and occupation estimate

The indexing is consistent: observing X_1 through X_{n+2} supplies n pair-chain transitions, from Y_0 through Y_n. The departure counts exclude Y_n, and C_{s,b} includes the observed symbol X_{n+2} when i=n-1. The queried next-symbol row is therefore the row at the actual terminal pair Y_n. No independent test context or modified estimator is introduced.

For fixed w, the sequence b_m in Section 2 is nonincreasing: its event implies the analogous event on any terminal suffix, whose probability is b_ell by stationarity. Along each path, its flags count only the first w occurrences of s, including an occurrence at time zero. Thus sum_{m=0}^n b_m <= w and b_n <= w/(n+1). This proves (2), with no irreducibility or aperiodicity requirement. Taking w=2m proves (3), even when 2m>n+1; a loose upper bound is harmless.

## 2. Stationary-law comparison and support

When pi(s)>0, s belongs to a closed irreducible class having positive pi-weight. Positive row scaling preserves the entire support graph and therefore all closed classes. The class excursion expectations are finite. Conditioning on the first step proves the coordinate bounds for v_i when i differs from s. The coordinate at s equals 1 under both kernels, and r_min <= 1 <= r_max because their P-row-weighted average is 1.

Writing V_P=sum_i v_i(P) and V_Q=sum_i v_i(Q), one obtains

    pi(i)/nu(i) = [v_i(P)/v_i(Q)] [V_Q/V_P]
                 <= r_max/r_min = exp(|lambda|).

The equality v(P)P=v(P) follows by shifting the occupation sum through the positive return time. Preserving the original class weights extends the comparison to reducible stationary laws; other classes have density ratio 1. If pi(s)=0, the original terminal event at s has probability zero. The statements about zero probabilities, periodicity, and multiple closed classes are consequently justified. A one-state class cannot require a nontrivial distinct-destination tilt and causes no exception.

## 3. Likelihood cancellation

All original positive-probability paths remain positive under Q_nu. The row likelihood is exactly

    -j d(q||p) - (k-jq) lambda.

The initial density contributes at most |lambda|. For an upper tilt, k-jq>=1 cancels this cost; for a lower tilt, k-jq<=-1 cancels it with the opposite sign of lambda. On E_m, j>=m, so the remaining likelihood is at most exp[-m d(q||p)]. The Q-probability of E_m is bounded using the genuinely stationary alternative law nu, giving (7).

The tilt q is fixed for each deterministic choice of s,b,m,t. It is not selected using the realized J_s. The two directions may use different alternative laws. Neither a conditional-binomial assertion nor a stationary claim about the original pi under Q is made.

## 4. Bernstein constants and endpoint cases

For a centered Bernoulli(p), the absolute higher moments are bounded by its variance, hence by p. The exponential-series estimate used in Section 5 follows from l! >= 2*3^(l-2), l>=2. Taking the signed variational parameter a=delta/(p+delta/3), which lies below 3 for p>0, gives

    d(p +/- delta || p) >= delta^2/[2(p+delta/3)].

For u=t/m and delta=sqrt(2pu)+2u/3, direct expansion gives

    delta^2 - 2u(p+delta/3) = (2u/3)sqrt(2pu) >= 0.

For m<=j<2m, each term of j*delta is bounded by the corresponding term in sqrt(4jpt)+4t/3. Thus either strict deviation in (9) implies the shifted event required in (7). Summing two directional bounds gives 4rm exp(-t).

If the upper candidate q is at least 1, its directional threshold exceeds the maximum possible count; the lower direction is analogous for q<=0. No endpoint tilt or limiting argument is needed. For p=0 or p=1, C_{s,b}=J_s p almost surely. These facts cover every row entry permitted by the theorem.

## 5. Scalar KL estimate

Every displayed constant in (10) is valid. In particular, with z=jp, a=k+1, x=z+p:

    sqrt(2zu) <= z/2+u,
    z <= 2k+10u/3,
    (k-z)^2 <= 8ku+(128/9)u^2,
    (x-a)^2 <= 16ku+(274/9)u^2 <= 16ku+31u^2,
    x <= 2a+10u/3.

The inequality h(x,a)<=(x-a)^2/a is valid also at x=0. When a>=u it yields at most 47u. When a<u, the bounds a>=1 and x<6u yield h<=6u log(6u)+u<=48u(1+log u), since u>=1. This verifies the full stated deterministic estimate without relying on the prior theorem.

In (11), the exact identity follows by summing x_b=(j+1)p_b and a_b=k_b+1. Its nonnegative correction is A-1-(j+1)log[1+(A-1)/(j+1)], by log(1+x)<=x. The KL orientation is forward throughout.

## 6. Integration and theorem constant

For t>=1, the one-count correction is absorbed by u=4t because

    sqrt(4jpt)+4t/3+1 <= sqrt(8jpt)+8t/3.

Dividing (10) by j+1>=m gives the first bound in (12). The second uses 1+log 4<=3 and log t>=0. Thus f_m(t)=576t(1+log t)/m and f_m'(t)=576(2+log t)/m.

The low layer contributes at most (576/m)(2rm)=1152r. The upper layers contribute at most

    2304r integral_1^infinity (2+log t) exp(-t) dt
      <= 6912r/e.

Here log t<=t-1 makes the integral at most 3/e. Since e>2, the total is strictly less than 4608r. The layer-cake change of variable is legitimate because f_m is continuous, increasing, and unbounded on [1,infinity).

There are exactly K_n=1+floor(log_2 n) disjoint bands covering all positive integer visit counts up to n. Summing the nonnegative scalar losses over A symbols, D=A^2 contexts, and these bands gives (14). Applying (2) with w=1 separately to each context proves the zero-visit term (15). Finally, B_s(b)>=1/(n+A) gives the pathwise bound log(n+A). The n=0 claim follows from the uniform add-one prediction. This establishes all constants and both terms of (1).

## 7. Ring barrier and its scope

The directed symbol graph with all edges except (a,a) is balanced and strongly connected for A>=2. Its Euler circuit gives a legal ring of the L=A^2-1 non-s pair states. A visit to vertex a in that circuit supplies consecutive states g=(b,a), h=(a,c), with b,c different from a.

With p=epsilon/L, stationary flow into and out of s matches at epsilon/(2L); every ring state has mass 1/(2L), proving (16). For K>=2, all required probabilities are interior and the chain is irreducible and aperiodic.

Starting at s and exiting at time 1, the gateway is reached at times L,2L,...,KL. The Kth gateway transition reaches s at n=1+LK. There are exactly K-1 bypasses, J_s=1, and C_{s,c}=1. Consequently the probabilities in (17) are exact. The inequality (1-1/K)^(K-1)>=exp(-1) follows from log(1+x)<=x with x=1/(K-1).

The proposed same-initial-law occupation constant must in fact obey

    C >= qL(n+1)/[4e(n-1)] >= qL/(4e).

Every ring vertex receives at least q/2 mass from the initial s-wave before any gateway decision; hence the envelope bound is valid and can be strengthened to M_pi(Q)>=(1+qL)/2. The stated weaker lower bound suffices. The general envelope inequality follows by bounding each suffix's initial law by the coordinatewise marginal envelope and then summing the first-w-occurrences flags for each possible suffix starting state.

For the unshifted Chernoff obstruction, the exact identity is

    exp[-d(1-p||p)]/p = p^(-2p)(1-p)^(-1+2p).

For p<=1/4 it is at most (4/3)exp(2/e)<4, as stated. Combining the hypothetical bound with F gives C>=L(n+1)/[16e(n-1)]>=L/(16e). F fails the shifted condition since 1<q+1. Thus neither barrier contradicts (7), and neither is a lower bound on add-one risk. Taking K/A arbitrarily large permits n/A^3 arbitrarily large.

## 8. Alphabet regime and source caveats

The leading alphabet factor is A^3, with the logarithmic factor retained. The consistency condition and comparison in fixed polynomial-separation regimes follow algebraically; the theorem does not give a uniform match near A^3 comparable to n. The ordinary-state-chain and binary-first-order caveats are appropriate.

I independently checked the [primary preprint](https://arxiv.org/html/2106.13947v2), definition (95), Theorem 22, Remark 1, and the introduction's binary first-order statement. The cited stationary terminal forward-KL model, alphabet domain, and rate agree with the candidate after substituting observed-symbol length N=n+2. Remark 1 concerns full rate optimality of ordinary first-order add-one; the candidate correctly does not claim to resolve that entire question. This review does not audit all proofs in that paper, recheck the published PDF, or establish literature priority.

## Conclusion

The frozen candidate's theorem is mathematically supported by its proof, including all stated constants and exceptional cases. The stationary change of initial law is the decisive additional ingredient; retaining pi under Q would invalidate the dimension-free occupation step, exactly as Section 9 demonstrates. The stated caveats correctly restrict what follows from the new bound.
