# AU001 independent mathematical review v1

2026-11-02. **Verdict: ACCEPT as an upper theorem at the stated interface and parameter domain.** No blocking mathematical defect found. This is an independent-context LLM audit, not formal verification, external peer review, novelty certification, or validation of an emitted implementation.

Reviewed frozen target: `v10_research/arbitrary_frontier/AU001_residual_suffix_precision_upper_v1.md`, SHA256 `1fce0c8374f372eeec6d4a21a2b683db02a754b227d39e6e8dd6b4e45e3ca6e1`. No target or accepted source was edited.

## Result and critical distinction

The refinement is real: an additive burn-TV error need not survive at infinite precision. Its replacement is `7 epsilon Psi(152 K^5/Q)`. The residual *initial distribution* can be arbitrary; the residual *suffix transitions* remain P. The universal arbitrary-start terminal-occupation inequality therefore applies directly. This is not a conditional stationary theorem, a residual-R trajectory assertion, or an independence assertion about the endpoint. The subsequent scalar absorption proves the claimed full all-Q surcharge with b0=max(beta,1/M).

The result remains an upper bound for the unchanged NB002 finite map. It is not an all-Q minimax classification, and does not itself justify replacing L by a matching statistical scale in a lower theorem.

## Sources actually read

I read AU001; IU001's actual reverse-return, tilted-operator, integration and arbitrary-start proofs (Sections 1–5), its scalar constants and resource accounting; SM001 Sections 1–4 and resource ledger; NB002 Sections 3–6, exact guard and full resource ledger; original G/U fact `a12539a93d9f1ee3` Section 11.1; R011's actual assembly and scale definition; R001's actual compatible-event/radius proof; S024 Sections 5–7; and S025 Sections 4–8. Verdict files were not used as substitutes for these arguments. The audit inherits the accepted finite prefix arithmetic and foundational statistical interfaces rather than claiming to reconstruct their whole dependency closure. Read files are bound separately in `AU001_review_bindings_v1.json`.

## 1. Universal terminal occupation and integer thresholds

For a homogeneous finite D-state kernel, let B(l,w) be the maximum over initial states of the probability that its length-l path has fewer than w earlier occurrences of its own terminal state. Suffix domination plus the ordinary Markov property gives B(l,w) nonincreasing in l. For each fixed initial state, the sum over time of these indicators is pathwise at most Dw: each state contributes only its first w occurrences. Summing this expectation over D initial states, and using max<=sum at every time, gives sum_l B(l,w)<=D²w. Thus B(m,w)<=D²w/(m+1). This is precisely the source proof. There is no illicit exchange of sum and maximum; the second D factor is retained. Pair-chain D=K² gives K⁴, without positivity, recurrence, stationary support or reverse-chain assumptions.

For 0<t<1, the event for v is J<A/t-kappa, equivalent for integer J to J<ceil(A/t-kappa). If the threshold is positive, its ceiling is <=A/t because integer kappa>=1. Empty events when the threshold is nonpositive are correctly removed. Layer cake gives Psi(K⁴ A/(m+1)) for every A>0, not merely A>=1. For C, the threshold is ceil(4A-kappa)<=4A; the probability is <=min(1,4x)<=4Psi(x). Strict inequality and integral thresholds cause no missing atom. The smoothing condition is essential and satisfied by kappa=K>=2.

## 2. Exact mixture and all-state/off-support boundary cases

For 0<beta<1, R=(P²-beta Pi)/(1-beta) is nonnegative and row stochastic on the *entire* pair space. Stationarity implies pi R=pi. Hence both Pi R and R Pi equal Pi, and expanding powers gives

`mu P^u=(1-(1-beta)^r)pi+(1-beta)^r mu R^r P^(u-2r)`.

No assumption that R is a legal one-step shift kernel is needed: it only produces a valid initial pair distribution. The subsequent suffix law is obtained by the linear probability kernel that maps an initial pair to an entire length-m ordinary P trajectory. Applying that kernel to the mixture proves an exact mixture of complete path laws. In particular, the terminal query and every suffix departure count are in the same path law. An observable regeneration event is unnecessary. One must not condition the original full-history estimator on a synthetic label; AU001 does not do so.

At beta=1, row sums force P²=Pi on all states, including off support. Since M>=64 implies r>=16, mu P^u=pi and the residual is omitted. At beta=0 the mixture is not invoked and NB002 supplies the valid arbitrary-start bound. A stationary law with singleton support is allowed. Under positive beta its support is closed, and stationary reverse-chain arguments only divide by positive masses. The arbitrary residual start can still be outside that support; universal occupation covers it.

The indices are consistent: u=floor(M/2), m=ceil(M/2), r=floor(u/2)=floor(M/4), and the suffix has m transitions and m counted departure states, excluding its actual terminal state. J_full>=J_suffix pathwise even though both use the same endpoint. This applies to both decreasing functionals, before averaging.

## 3. Stationary functional inheritance

IU001's stationary proof handles the actual query by reversing the stationary path conditionally on its endpoint. Its positive-return expectation is k/pi(s): finiteness follows from the two-step hit chance; the stopped occupation measure is invariant; minorization gives uniqueness; strong Markov gives successive return increments. Markov's inequality gives the positive-return tail with the exact integer k. This directly supplies AU001's bad-event bound 4dA/m.

The sharper reciprocal bound uses the same return tail together with IU001's conditional exponential lower-count tail. I checked its nonreversible operator comparison: the two-component mean/centered Cauchy bound controls the singular norm of DHD by the positive comparison DH0D, rather than assuming H reversible. The 2x2 determinant and trace lead to the stated spectral deficit. Its stationary moment bound and whole reverse-suffix transfer give the conditional tail. The integral is split at 16A/(m pi(s)); the later threshold is strictly below m pi(s)/16, and `5 mu exp(-beta mu/96)/A<=480/(beta A)`. Summing the statewise bounds cancels pi(s) only after conditioning. These steps justify AU001 (2.2); they do not require terminal-count IID.

## 4. Pre-integration statistical baseline is available

NB002's approximate vectors satisfy Delta_q<=v+K/Q, Delta_b<=7K/Q. Its observable denominator is lower than the true J+K, and its monotone-rejection property follows from inflated radius and error allowance. Off the bad-count event, denominator loss is at most a factor two and the pointwise safety bound is `e+2rho+3v+9K/Q`; the bad event is charged once by the loss cap.

The baseline is not extracted from a final scalar risk result. For beta=0 it is <=50L. In the weak-beta long-history region, the actual R011 compatible event-loss certificates and R001 event-radius comparison give <=(42/5)7369L=61899.6L<2^16L. In the short-history weak region S024's count-radius bound gives <=11264L. In the strong non-pooling region its count bound and row bound give <=593L. Near IID, NB002 instead uses rejection containment and S025's actual CT and active-GT inequalities; their sum with the pooled estimate is <=8000L. GT is used only when g<1. The known-false unconditional NEXT statement is not used. Finite exceptional cases are covered by the cap. Thus the common pre-integration reduction with `3 E v+P(C)+9K/Q` is indeed valid before occupancy integration.

## 5. Constants and scalar envelope

Mixture evaluation yields `(dA/m)[55+3 log(1+480/(beta A))]+7 epsilon Psi(K⁴A/(m+1))`. Using m>=M/2, d<=K² and A=76KM/Q gives exactly 8360 and 456 in AU3. The original 9K/Q has not disappeared. With K>=2, its contribution inside K³/Q is <=9/4, so the stated 8363 relaxation is safe. The log comparison with 120/19<exp(2) and constant 2^14 are valid.

For beta M=t>=1, epsilon<=e exp(-t/4). With D=152K⁵>=1 and G=1+log(1+Q/t)>=1, Q<D gives Psi(D/Q)<=D/Q<=DG/Q. For Q>=D, Psi(D/Q)<=(D/Q)(1+log Q), including equality Q=D. Since log Q<=log(1+Q/t)+log t and epsilon<=1, epsilon(1+log Q)<=G+e exp(-t/4)log t<=G+4<=5G. Multiplication by 7D gives 5320K⁵, exactly as stated. The use of log t<=t is safe because t>=1. beta=1 has zero residual.

For beta<1/M, W=(1+log(1+Q))/Q, and direct two-case evaluation of Psi(76K⁵/Q) supplies the weaker all-beta envelope. There is no beta division at zero. At beta=1/M either route is valid. Finally each component of L is at most g<=K^(5/2)/sqrt(M), so AU2 is a valid but potentially looser corollary. The independent cap at one remains throughout.

## 6. Algorithm and full cost retention

No proof object becomes an input, port, initialization rule, suffix recomputation, or runtime operation. The finite map remains NB002 at every public legal h>=4. Beta is not estimated or read. I compared the accounting against NB002 and IU001: the arithmetic word includes the log(M+K) term; dense coefficient bits, all-token QKV/pointwise work, attention, exact guard products, masks and positions, input/history arrays, master and output banks, control/addressing, copies/holds/clears, actual cache generation and offline sorting/writes are retained. Peak remains simultaneous-phase sums, not rolling storage. The separate PURE expansion is not assigned hybrid costs. AU001's shorter ledger explicitly inherits all source costs and makes no missing-cost subtraction.

## 7. Independent finite corroboration and limits

`AU001_independent_checks_v1.py` uses exact rational arithmetic for legal binary pair kernels: nonreversible positive support, absorbing/off-support starts, and beta=1 with full or singleton support. It compares every complete suffix path probability for several burns and lengths, enumerates joint endpoint/count laws, and checks a visited-mask dynamic program through m=64 to make the universal w=1 bound nontrivial. It separately checks strict-ceiling identities at rational thresholds. A finite floating-point scalar grid covers all beta endpoints, the beta=1/M boundary, all M mod 4 classes, large M, and h through 500. Results are stored in the adjacent JSON. These are diagnostics, not proofs over all real beta or all kernels.

No revision to frozen AU001 is required. A useful editorial improvement in a future successor would be to list the direct SM001 and R011 source identities alongside AU001's existing binding list; the present review binds both. This is provenance completeness, not a mathematical blocker. A matched lower theorem must still be audited separately; in particular, this review certifies neither K=2 logarithmic necessity nor joint-K sharpness.
