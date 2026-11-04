# Independent exact-file analytical review

Date: 4 November 2026 (UTC).

Verdict: **PASS** for the theorem, proof, stated constants, boundary cases, and the two method barriers in the exact candidate below. No correction is required for mathematical validity. This review does not assert literature priority or full growing-alphabet minimax optimality.

## Exact binding and scope

Reviewed file:

`stationary_terminal_kl.candidate.v1.md`

SHA-256:

`1d436719744fd51bda32db723e84932c68507479383154abeb4b9724f2db1337`

The candidate was read in full and its checksum verified before review. The review covers Sections 1-9, including the changed initial law, excursion normalization, scalar integration, indexing, and legal pair-chain counterexample. The candidate itself was not modified. No numerical test, simulation, training, external upload, or repository mutation was performed.

## 1. Stationary occupation and boundary counts

The fixed-target inequality is dimension-free and valid without irreducibility, aperiodicity, or reversibility. The event at time m implies the corresponding event on a suffix of length ell. Stationarity identifies that suffix event's probability with b_ell, giving b_m <= b_ell. For each deterministic path, only the first w occurrences of the target can satisfy the flag. Therefore the sum of the probabilities through time n is at most w, and b_n <= w/(n+1).

Here J_s counts departures at positions 0 through n-1 and the terminal target is at position n. Thus the flag counts the terminal state as one of the first w occurrences, exactly as required. Taking w=2m gives the band bound. The dyadic bands beginning at m=1 and ending at 2^floor(log_2 n) partition every integer count from 1 through n, including n when n is a power of two. J_s=0 is handled separately. The statement for n=0 is correct.

## 2. Stationary distributions after the row tilt

Positive row multipliers preserve the entire directed support graph, hence all closed communicating classes. A state with positive stationary mass belongs to a finite closed irreducible class. All return and hitting expectations used in that class are finite.

For i different from s, the expected excursion occupation is a nonnegative linear combination of the outgoing probabilities from s, with coefficients independent of the changed row. Consequently its Q/P ratio is between r_min and r_max. For i=s both excursion occupations equal 1, which is in the same interval. The normalized excursion occupation formula is justified by the telescoping occupation identity given in the candidate.

There are two normalization factors, not a missing return-time factor:

    pi_i / nu_i
      = [v_i(P) / v_i(Q)] [sum_j v_j(Q) / sum_j v_j(P)]
      <= (1/r_min) r_max.

Thus the claimed bound exp(|lambda|) follows. Keeping the original recurrent-class weights cancels those weights in this ratio. Other positive-weight classes are unchanged. Transient states and zero-weight closed classes have zero mass under both stationary laws. If pi(s)=0, the original terminal event at s has probability zero and contributes nothing. Periodicity causes no failure of any of these arguments.

## 3. Initial-density term and one-count cancellation

The likelihood ratio in Section 4 correctly includes pi(Y_0)/nu(Y_0). The remaining ratio contains precisely J_s departures from row s; the terminal state introduces no additional likelihood factor.

For q>p, lambda>0 and k-jq>=1 cancels the entire possible factor exp(lambda). For q<p, lambda<0 and k-jq<=-1 cancels exp(-lambda). The remaining exponent is -j d(q||p), bounded above by -m d(q||p) on the band. Applying occupation under Q initialized in nu is legitimate because that alternative law is stationary. A different alternative law for each deterministic threshold is sufficient for the later tail integration.

The next-symbol representation of a pair-chain row is injective into its successors (the successor is the second current symbol followed by the next symbol), so the symbol tilt and grouped-destination calculation agree exactly.

## 4. Bernstein step and endpoint cases

The two-sided centered-Bernoulli moment bound with variance upper bound p yields the displayed binary-KL estimate for either sign. Substituting delta=sqrt(2pt/m)+2t/(3m) gives d(q||p)>=t/m. On m<=j<2m, both components of j delta are bounded by the displayed count threshold.

The strict deviation in (9) implies k-jq>1 in the upper direction or k-jq<-1 in the lower direction, hence the weak inequalities of (7). There is no rounding or floor issue at an integer boundary.

If the upper q is at least 1, the proposed upper strict count deviation is impossible because k<=j. If the lower q is at most 0, the lower strict deviation is impossible because k>=0. Thus no q=0 or q=1 stationary comparison or limiting argument is required. For p=0 or 1, k=jp almost surely and the deviation event is empty. The proof never assumes binomiality after conditioning on the random count or terminal context.

## 5. Scalar estimate, integration, and constants

All deterministic inequalities in Section 6 check. In particular:

- The squared-count bound is 8ku+(128/9)u^2.
- Including p-1 yields a bound at most 16ku+31u^2, since u>=1.
- Division by a=k+1 gives at most 47u when a>=u.
- If a<u, then x<6u and a>=1, giving the stated logarithmic envelope.

The exact sum-of-h identity in (11) has the correct sign and scaling; its residual is nonnegative by log(1+v)<=v.

The added count is absorbed using u=4t: for t>=1 the increase from 4t/3 to 8t/3 alone is at least 1. The square-root term also increases. Therefore the deterministic scalar lemma gives the stated envelope f_m(t)=576t(1+log t)/m.

Its derivative is 576(2+log t)/m. Multiplication by the joint tail 4rm exp(-t) gives coefficient 2304r. The baseline term is 1152r. The integral is at most 3/e, so the total is at most 1152r+6912r/e, strictly below 4608r because e>2. No coordinate union bound or extra factor A is hidden here.

Summation over A^2 states, A symbols, and K_n bands gives 4608 A^3 K_n/(n+1). The zero-count term is A^2 log A/(n+1). The deterministic cap log(n+A) is valid because every add-one probability is at least 1/(n+A). Together these establish exactly (1).

## 6. Alphabet and literature comparisons

The sufficient consistency condition and its asymptotic reformulation are correct. The candidate distinguishes log n from log((n+2)/A^3), retains the source theorem's domain, and does not claim uniform growing-alphabet optimality.

The cited lower-bound audit was read, and the local published text of Han, Jana and Wu was checked at Theorem 22 and the terminal-risk definition. The theorem has factor A^(m+1)/N times log(N/A^(m+1)), in the stated alphabet range, with stationary initialization. Substitution m=2 and N=n+2 matches the candidate's terminal pair and observed-symbol indexing. In the subregime A^3 <= (n+2)^(1-eta), the lower logarithm is at least eta log(n+2); thus the matching-order statement, restricted to the theorem's domain, follows. For fixed A it gives the stated order in n. The distinction from binary first-order minimax risk and the warning about pair-chain versus symbol-process reversibility are sound.

Primary publication checked locally:

`[preparation path omitted; see the DOI and source identity]`

Prior source audit:

`../fixed_alphabet_kl_sharpening_20261103_2346/primary_source_matching_lower_audit.v1.md`

This is a check of the claimed comparison, not an independent reproof of HJW's theorem or a survey of later literature.

## 7. Ring construction and original-initial-law barrier

Removing the loop (a,a) from the complete directed symbol graph leaves a balanced, strongly connected graph for A>=2. Its Euler circuit supplies all L=A^2-1 distinct pair states in a legal ring. At a visit to a, its incoming and outgoing symbols differ from a, giving consecutive states g=(b,a) and h=(a,c) as required. Both additional transitions g to (a,a) and (a,a) to h are legal overlapping-pair transitions. The self-loop at (a,a) makes the irreducible chain aperiodic for the parameter range used.

For p=epsilon/L, stationary flow into and out of s balances at pi(s)=1/2 and pi(z)=1/(2L) for ring vertices. At h the two incoming flows sum to 1/(2L); every remaining ring flow is unchanged. Thus (16) is correct.

Starting at s and entering h at time 1, the first gateway departure occurs at time L and returns to s at time L+1. The Kth gateway return is at time 1+LK=n, so on F there is exactly one earlier departure from s and one count of symbol c. The displayed P and Q path probabilities are correct. The lower bound on (1-1/K)^(K-1) follows from (1+1/(K-1))^(K-1)<=e. It yields both bounds in (17) with their stated n-1 denominators.

The occupation inequality with w=2 would require

    C >= qL(n+1) / [4e(n-1)] >= qL/(4e),

so the stated dimension obstruction holds, including when K and n/A^3 become arbitrarily large. It concerns Q initialized in the original pi, not Q initialized in its own stationary law.

## 8. Envelope and unshifted-Chernoff barriers

The M_pi(Q) envelope proof is valid: for each suffix length ell, dominate its initial distribution pi Q^(n-ell) coordinatewise by sup_t pi Q^t, then sum the fixed-start flagged probabilities over ell. Their sum is at most w. In the ring example each ring vertex receives probability at least q/2 from the initial s mass at its first-lap time, with no gateway loss before that vertex's first arrival. Hence M_pi(Q)>=qL/2.

For q=1-p and p<=1/4, the identity

    exp[-d(1-p||p)] / p
      = p^(-2p) (1-p)^(-1+2p)

and its upper bound below 4 are correct. Applying the proposed unshifted tail bound to F gives the stronger necessary inequality C>=L(n+1)/[16e(n-1)], hence the displayed C>=L/(16e). F has j=k=1 and cannot satisfy k>=jq+1 for q>0, so it does not contradict the repaired theorem. The candidate correctly presents these as barriers to particular proof factorizations, not lower bounds on add-one risk or on all possible arguments.

## Conclusion

The exact hash-bound candidate proves the claimed stationary A^3 log(n)/n upper bound for the full-history add-one predictor, with the displayed finite-sample constant and stated edge cases. The ring barriers are also correct. The prior arbitrary-start A^5 theorem remains separate; the improved alphabet factor has not been extended to arbitrary starts, and the remaining growing-alphabet logarithmic gap is accurately disclosed.
