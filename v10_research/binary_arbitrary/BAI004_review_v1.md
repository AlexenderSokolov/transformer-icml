# Fresh independent review — BAI004 author v2

2026-11-02. Reviewer: `independent LLM reviewer`, newly assigned to this unit. This review independently checks BAI004's new scalar/count/initial-delay argument; it does not import the reviews or acceptance of BAI002 or BAI003. No author file was edited. This is an independent LLM review, not external peer review or formal verification.

## Verdict: PASS for the stated intermediate result

No blocking mathematical, endpoint, source-certificate, or scope gap was found. BAI4.1 is proved for the specified initial-W/terminal-A and symbol-swapped initial-C/terminal-B components, including the unit clipping cap and all A0>0, M>=8. Sections2 and6 also establish the stated general initial-equals-target identity and crossing-start reduction. The complete arbitrary-start binary precision upper remains outside this unit's scope, as the author explicitly states.

Reviewed author v2 SHA-256:

    5add0a72306badc8c91b8c50dfcbac5fa0c528c34528e812b08780ebc3d9b3c1

The exact author and inherited source identities are bound in `BAI004_review_source_bindings_v1.json`.

## Detailed checks

### 1. General return identity and actual local time

The displayed first-positive-return pgf follows by taking a first step to s or into its complement, then using the killed resolvent. Schur complementation yields exactly the determinant ratio. Both determinants have constant term one, so formal logarithms and inverses are legal. Differentiating the log determinant gives the trace series; no analytic convergence radius or irreducibility assumption is required.

The kth positive return at time n has exactly k earlier visits to s, including the initial visit at time zero. Therefore the coefficient sum with1/k is precisely the claimed endpoint-restricted reciprocal expectation. The trace difference is nonnegative by the return expansion, and it is at most tr(P^n)<=d because the killed-submatrix trace is nonnegative. There is no hidden stationary conditioning or endpoint-independent query assumption. The ratio is evaluated only on the event Y_n=s, where J_s>=1.

### 2. Full all-state certificate and stationary algebra

With stationary masses(y,x,x,w), the balance identities give x=at/(et+2at+ab). The two direct entries used are P²(B,A)=ea and P²(A,B)=bt. The third inequality at>=beta x follows from the actual W-to-C entry ab and w=xb/t, by cancellation of positive b. These are all legitimate full-support, positive-beta consequences. In particular the argument does not miss the exceptional ea cell or substitute a restricted-start certificate.

After multiplication by M², the three inequalities are exactly gamma<=D, gamma<=ED/T, and gamma<=BD/alpha. All divisors are positive in this branch. Beta=0 and the weak-beta region are handled separately without these divisions.

### 3. Scalar bridge

All three cases bound gamma by6X²+6X with H=max(E,B/(1+T)) and X=(1+alpha)H.

- For T>=1, B/T<=2H and E<=H give the displayed bound on ED/T. The subsequent bound by3X²+2X has ample slack.
- For T<1 and alpha>=1, D/alpha=B+2T+ET/alpha<=3H+2, giving6H²+4H<=6X²+4X.
- For T<1 and alpha<1, min(E/T,B/alpha)<=(E+B)/(alpha+T) is a weighted-average inequality, and E+B<=3H. Combining it with D<=2H(alpha+T)+2alpha T gives the claimed bound, since alpha T/(alpha+T)<=1/2.

When gamma>=1, the split X>=1 versus X<1 correctly yields X>=sqrt(gamma)/12. Undoing the scaling gives the exact minimum in(3.2), not a weaker individual bound on e or b. That minimum is essential and is preserved throughout the proof.

### 4. Endpoint-inclusive excursion count

Before hitting W, every A-to-next-A attempt reaches B after a possible geometric C hold. The test at B hits W with probability e, so the complete number of A visits is geometric(e). Thus truncation gives the1/e bound.

For the other bound, the event that an A visit at time j<=M is counted is measurable before the j-to-j+1 transition. Its expected A-to-C indicator is therefore b times its counted-visit indicator. Including the outgoing step at M+1 is necessary and correctly done. Each counted C entry except possibly the last requires a preceding C exit. There are at most M eligible C-departure times1,...,M because the initial state at time zero is A. Consequently the expected number of those exits is at most Mt, and b EN<=1+Mt has no omitted endpoint term.

The full-chain visit count is partitioned into its initial active excursion and excursions begun by W-to-A transitions at times up to M. The expected number of additional entrances is at most Ma. Conditional at each entrance, the remaining horizon is at most M, so strong Markov and the uniform truncated-excursion estimate justify multiplying its bound by1+Ma. Random excursion counts do not require independence from their future lengths for this conditional-sum argument.

### 5. Global harmonic cost and first-hit split

Summing the fixed-A0 endpoint function f(n) over n=0,...,M counts the visits to A in their chronological order. At the jth such visit its earlier count is exactly j. Thus(5.3) is a pathwise identity for the GLOBAL count, rather than a reset-count inequality. The harmonic comparison(5.1) is valid for A0<1, N=0, and N<=A0; Jensen is applied to the increasing concave logarithm with finite V<=M+1.

Starting W, the first A hit is exactly geometric(a). No previous A count exists, so the complete convolution(5.4) retains the actual endpoint and its correct count. For the early part the remaining horizon is at least M/2>=4; the initial-equals-target reciprocal lemma applies with a positive count. For the late part, r-1>=M/2-1>=M/4, so the exponential density bound is valid, including odd M and M=8.

The logarithmic comparison uses12(1+x)²>=1 and ln12<3. The maxima x exp(-x/4)<=2 and x² exp(-x/4)<=9 are correct. Hence the early8 plus late26 constants yield34, safely below40. No lower bound on A0 is used.

### 6. Weak-beta branch

The accepted SB001 universal occupation statement specializes at K=2 to Psi(16A0/(M+1)), with smoothing2 exactly matching this unit. On terminal A, its actual query count equals J_A; discarding the terminal-A indicator and using the actual-query functional elsewhere is a legitimate upper bound. Monotonicity allows M+1 to be replaced by M. The two-case bound on Psi(16u) is valid for every u>0, and its logarithm is exactly the displayed cutoff when d0=1/M. Equality beta M²=1 is included in the positive-beta argument.

### 7. Crossing initial states

Until the first diagonal hit, either crossing start alternates deterministically conditional on survival; the two-step survival probability is(1-b)(1-e)=1-h. In the small-h case, summing over the last diagonal entrance correctly bounds aP(Y_M=W)<=e and tP(Y_M=C)<=b. No initial diagonal mass exists. Together with the crossing terms and b+e<=2h this proves(6.1).

In the large-h case, floor(floor(M/2)/2)=floor(M/4)>=M/8 for M>=8 gives(6.2). Strong Markov at the first diagonal hit produces an ordinary suffix of the original source, and its terminal prior count is pathwise no larger than the full count. The supremum in(6.3) therefore bounds the correct actual-terminal functional. This is not a marginal mixing argument, and it does not assume the missing diagonal-start terms have already been bounded.

## Independent finite corroboration

The fresh reviewer script `BAI004_review_diagnostic_v1.py` checked:

-500 binary kernels, including logarithmically tiny parameters, with stationary and all-state beta calculations;
-272 cases in the gamma>=1 branch of the scalar bridge;
- all500 truncated-excursion and full-chain expected-count comparisons;
-600 direct terminal-A local-time DP comparisons covering A0 from0.0001 to1000 and horizons8,16,64,256;
-960 comparisons of the general Schur/trace return identity against independent local-time DP for unrelated random four-state chains.

All passed within floating-point tolerance. The maximal count-bound ratio exceeded one only by approximately10^-15; no substantive violation was observed. These finite checks corroborate the algebra but do not replace the proof. Results are saved in `BAI004_review_diagnostic_v1.json`.

## Scope and acceptance boundary

The reviewed claim is an intermediate occupation theorem plus reductions. It does not supply the missing opposite-diagonal or remaining opposite-crossing terms, a complete arbitrary-initialization risk bound, a new decoder or resource claim, an initialization lower bound, or a novelty certification. Root acceptance remains a separate decision.
