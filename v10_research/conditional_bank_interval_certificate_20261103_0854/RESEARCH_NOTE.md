# Conditional interval certificate for a float attack

2026-11-03. This is a deterministic mathematical construction and exact rational interval calculation. It is not a certificate of NumPy, BLAS, libm, a saved checkpoint, or any observed attack. The explicit numerical float-error radii below are *assumptions*. No random operations, model initialization, training, publication, or changes to earlier artifacts were performed.

## The objective and a useful certificate

Fix clean h, edit budget k, protected endpoint, saved binary64 weights interpreted as exact rationals, and candidate-to-context mapping before scoring. This may be an all-candidate batch with a fixed assigned slot per candidate, or a fixed-filler batch with a prescribed slot for each candidate. Write U(z) for the actual returned finite float CE in exactly that protocol. Reject/handle NaNs and infinities under an explicitly specified comparison rule; the statements below assume finite, deterministic returned scores. Do not replace this protocol by a singleton or a different batch without a separate proof.

The exact count-bank DP enumerates all reachable banks b and a legal witness for each; call the bank set B. Let I_b be the ideal real CE of bank b with exact rational inputs, exact stored parameters, and exact tanh, sigmoid, and log. Suppose exact rational endpoints L_b <= I_b <= H_b have been proved, and independently for every legal candidate z in the actual protocol, |U(z)-I_bank(z)| <= d_bank(z), with rational d_b >= 0. The latter may be supplied by the earlier conditional floating-readout theorem or a separately verified implementation-specific analysis. It must include pooling and affine operations, tanh, sigmoid, smoothing, target, CE arithmetic/logs, exceptional values and relevant batch layout. The interval evaluation of I_b alone does not prove it.

For any legal witness w, without evaluating its actual score,

  max_z U(z)-U(w) <= max(0, max_b(H_b+d_b) - (L_bank(w)-d_bank(w))).       (A)

If U(w)=y is actually obtained and retained in the *same prescribed context*, the sharper bound is

  max_z U(z)-y <= max(0, max_b(H_b+d_b)-y).                               (B)

Treat the finite returned binary64 y as its exact rational value; no further rounding is needed to compare it to rational endpoints. A direct score in a singleton batch is not y for a different all-candidate protocol. B can be useful when y substantially exceeds the witness bank's generic lower bound, although obtaining it may entail running the complete prescribed batch and hence may erase computational savings. For fixed fillers it takes one context evaluation. Unlike the generic 2d+eta statement, (A)-(B) can use heterogeneous d_b, witnessed scores, and each competitor's interval, without first proving an ideal argmax. The correct inequality follows simply by upper bounding each candidate and lower bounding (or measuring) the witness.

For a bank b* with witness w, if L_b* - d_b* > max_{b != b*}(H_b+d_b), every actual candidate in b* beats every candidate in another bank. It does NOT prove which member of b* wins. If b* contains exactly one legal candidate, the same condition certifies its unique actual maximum. With multiple same-bank candidates, their actual scores may differ, and a bank-only bound cannot prove uniqueness: even perfect real interval evaluation does not recover reduction-order-dependent float behavior. Excluding w itself from a competitor bound is permitted only after soundly accounting for every other legal word in its own bank. Equivalently, a verified y can prove a unique maximum if y exceeds a sound upper bound on *all other candidate scores*, including same-bank alternatives.

To reuse the previous conditional R, one conservative rational score radius is

  d = R + tau_q/(e-tau_q) + beta/(e-tau_q) + tau_CE,       e=1/(M+2)^2,

provided all the corresponding hypotheses in float_readout_bound_20261103/REPORT.md hold, tau_q<e, and R, tau_q, beta, tau_CE are rational upper bounds. This replaces the target sensitivity's logarithm by log((1-e+tau_q)/(e-tau_q)) <= 1/(e-tau_q), a conservative inequality from log x <= x-1. No unproved tau or BLAS bound is filled in. Bank-dependent radii are valid if each is proved uniformly for *all words and assigned contexts* represented by that bank. The small M=1025 checkpoint figures in the cited note are conditional R contributions, not complete d values.

## Exact rational enclosures for the ideal readout

Each bank supplies rational coordinates. All affine and interval operations use exact integer/rational arithmetic, including signed weights. Apply the monotone tanh to lower and upper hidden preactivation bounds, then sign-aware interval arithmetic for v. Apply monotone sigmoid and the nonnegative smoothing affine map, then enclose log q and log(1-q); multiply by the nonnegative exact target coefficients. Repeatedly increase precision until the desired inequalities are strict or acknowledge that the desired order is unresolved. The following scheme uses no assumed transcendental implementation accuracy:

* To enclose exp(x) for rational x>=0, choose k so y=x/2^k <= 1/2. For S_N=sum_{j=0}^N y^j/j!, the remainder lies between 0 and [y^(N+1)/(N+1)!]/[1-y/(N+2)]. Raise both positive endpoints to 2^k. For negative x, take reciprocals in reverse order. Endpoint rounding, if used, is explicitly outward on a rational grid.
* Obtain tanh x=(exp(2x)-1)/(exp(2x)+1) and sigmoid x=1/(1+exp(-x)) using monotonicity and outward interval arithmetic.
* For x>=1, scale x=2^k m with 1<=m<=2. Put y=(m-1)/(m+1), 0<=y<=1/3. Bound log m by 2 sum_{j=0}^{N-1} y^(2j+1)/(2j+1), plus the nonnegative upper tail 2 y^(2N+1)/[(2N+1)(1-y^2)]. Bound log 2 the same way and combine; for 0<x<1 use -log(1/x). These are exact series inequalities. CE endpoints must remain strictly inside (0,1); refine if a coarse enclosure touches an endpoint.

The saved demonstration uses N=50 and rounds outward to a 10^-30 grid between selected operations to avoid huge denominators. Its comparisons, including its interval widths, are exact rational comparisons; printed decimal midpoints are noncertifying illustrations. The scheme admits arbitrarily narrow enclosures in exact arithmetic but does not promise a finite termination when values are exactly tied, nor inexpensive arithmetic for large banks or highly saturated readouts.

## Explicit constructive case, including a near tie

Let M=2, clean h=0000, k=1, terminal 00. The three legal words are 0000, 1000, 0100. Their (J,C1,D,E) banks are (2,0,1,0), (1,0,0,0), (0,0,0,0), with first rail x=(J-C1)/M equal to 1, 1/2, 0. The exact target from h is t=(C1+1)/(J+2)=1/4; e=1/16. A valid fixed 9-by-32 readout has W[0,0]=1, v[0]=1 and every other parameter zero. Thus r=tanh(x), q=1/16+(7/8)sigmoid(r), and U_ideal=CE(1/4,q).

On r in [0,1], sigmoid(r) lies in [1/2,3/4] since exp(1)<3. Thus q>=1/2, q-1/4>=1/4, q(1-q)<=1/4, and dq/dr >= (7/8)(3/16)=21/128. Therefore dCE/dr >= 21/128. Also tanh(1)<4/5 since exp(2)<9, so tanh'(x)=1-tanh(x)^2 >=9/25 on [0,1]. Consequently the ideal CE gap between x=1 and x=1/2 is at least (1/2)(9/25)(21/128)=189/6400; the x=0 competitor is still lower. The interval script independently verifies a strictly larger gap with exact rational endpoints. Rounded illustrative ideal scores are 0.9111393767608025, 0.8139438743148349, 0.6931471805599453.

Assume, without asserting it of any real backend, a uniform |U-I| <= 1/1000 under a fixed specified actual protocol. Then 0000 is the unique actual optimum by at least 189/6400-2/1000 = 881/32000 > 0.0275. There are no other legal words and its bank is a singleton. This is a genuine sufficient-condition example, not an observed library run.

Now change only v[0] to 2^-20. The global CE-vs-logit Lipschitz bound of 1 and tanh's 1-Lipschitz bound imply the first two ideal values differ by at most 2^-21 < 2/1000. Oppositely signed admissible errors of size 1/1000 can reverse them while preserving nonnegative scores. Therefore the same uniform-error information cannot establish the original ordering, even with arbitrarily exact ideal intervals. This does not prove an actual NumPy reversal; tighter implementation-specific bounds, direct scores, or different structure might resolve the tie.

## Is this more than a tautology?

Yes when the DP collapses a large edit space to manageable count banks, rigorous radii are available without enumerating candidates, and the output margin dominates error. Then the proof can bound every candidate without executing the backend on each one and may certify a concrete attack and its regret. The bound can also be meaningful when exact optimality is unavailable. It is conditional and potentially vacuous when errors are unproved, too loose, masks share a bank, or top scores are near tied. The DP may itself be impractical; interval arithmetic and one evaluation per bank have real costs. No claim of an actual checkpoint certificate or a speedup for these artifacts is made.

## Reproduction and record

Run from the workspace root:

  PYTHONDONTWRITEBYTECODE=1 python -B v10_research/conditional_bank_interval_certificate_20261103_0854/certificate_demo_v2.py

The first script `certificate_demo.py` kept exact, unrounded rational compositions; denominators grew and it was manually interrupted before output. Its empty `run.log` and original script were sealed before the revised file was created. The revised script rounds outward, completes, and its `run_v2.log` is retained. The script uses only Python standard-library integer and Fraction operations, no RNG, model constructor, model execution, or external writes. Source-input binding hashes accompany this note.
