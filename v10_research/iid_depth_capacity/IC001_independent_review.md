# IC001 — fresh independent adversarial review

2026-11-02. Reviewer: child `independent LLM reviewer`, distinct from theorem author. **PASS within the stated common IID primitive/interface family.** This is independent LLM mathematical/model review, not root acceptance, formal verification, emitted-network validation, or novelty certification.

Reviewed theorem SHA-256: `a443306b90e55bb05c76f3935b8cca676f9f8b3c6211c21d2e2b34e23dd979e3`.

## What was independently checked

Read the whole IC001 theorem. Consulted IR001's exact boundary/seed/influence interface and constants, its accepted receipt, FG001's full-fold finite evaluator/ledger and acceptance, FA001's signed full-product normalized sum semantics, and GD001's uniform-family precision/resource extension. The author conclusion and finite diagnostics were not used as proofs.

1. **Partial folds rather than only full Q-folds.** For r>0, retained times 0,h,...,(ceil(r/h)-1)h,r have positive increments no larger than h and at most J members. When r is an exact multiple of h there is no duplicate time; r=0 gives one rail. An e-fold tent has breakpoints v/2^e and alternating affine slope ±2^e. Because 2^e divides Q, each closed Q-bin is contained in precisely the specified closed branch (up to shared endpoints), with v=floor(k/2^(h-e)). Thus a coarse label genuinely determines the next affine formula. This would fail for arbitrary nondyadic Q; the theorem does not claim that extension.

2. **Endpoints, orientations, and zero-width fibers.** Shared branch formulas agree at endpoints, so replacing half-open floor bins by closed intervals can only add boundary points and does not make the affine formula wrong. Inverse endpoints must be sorted for negative slope, as explicitly required. At time t the slope magnitude is 2^t and never zero. Label Q imposes y=1 and therefore a unique x on the existing affine branch; returning that singleton is valid for every valid input. Returning any earlier zero-width intersection is equally valid. No fictitious branch Q is used. Invalid-label behavior need not reproduce a true source; the zero fallback makes a total decoder possible.

3. **Reconstruction and bit complexity.** The final interval is contained in an affine inverse of a width-1/Q bin, so its length is at most 1/(Q2^r), even if earlier intersections shrink it. All affine intercepts are integers; constraint endpoints have denominator dividing 2^(h+t), so a common denominator 2^(h+r) suffices. Slopes/intercepts and endpoint numerators require O(h+r) bits. The decoder requires only O(J) interval/affine updates, not Q^J enumeration. The lower-endpoint reconstruction error is one-sided only in the original scalar, not in intermediate tent values.

4. **Finite evaluator and primitive admission.** Fine precision P>=h+r represents the half-bias and integer weights exactly. Integer tent updates have no rounding error and preserve [0,2^P]. Uniform zero-score attention in FA001 has identical positive integer Taylor weights, so its exact normalized sum really is floor(2^P A/m); it is not an ideal exponential substituted for the finite implementation. The initial scalar error is below 2^-P, propagated through at most r tents by Lipschitz factor 2^r, giving the claimed uniform 1/Q precut certificate. Decoding the labels of the fine scalar gives error at most 1/(Q2^r)+2^-P. This handles all formal histories and endpoint states, and does not require equality of finite and ideal floor labels. The optional generic GD precision is larger and paid.

5. **Causality, width, and primitive depth.** Each history row pools its own prefix, not a copied final statistic. The terminal mask has density M/(M+3)>=1/4; first-two-position fallbacks and remaining prefix masks meet that fixed density as well. Retaining selected rails plus one working rail costs O(J) width. Two bounded affine/ReLU stages per tent justify d0+2r; zero-output dummy heads/masks, if syntax requires them, are explicitly charged. There is no unbounded per-layer computation or unquantized source-dependent terminal side channel.

6. **All-Q capacity/depth quantifiers.** The chosen r* is a clipped nonnegative ceiling. If it is unclipped, Q2^r*>=sqrt(M); if clipped, it equals Q^J. Consequently Q2^r*>=min(sqrt(M),Q^J), which yields exactly Aκ=1/2+2 max(1,κ^-1). Its depth is at most d0+2+2 log2_+(sqrt(M)/Q), including Q>=sqrt(M), Q=2 and M=1. Conversely, (Q+1)^J<=(3/2)^J Q^J and the three separate lower floors yield precisely (3). The theorem correctly does not identify the necessary multiplier A with the sufficient Aκ, nor the lower and upper exponential bases. Its order statement is valid with the explicitly allowed fixed multiplicative/additive constants.

7. **Initialization and lower-bound intersection.** The 3/(64sqrt(M)) statistical witness fixes initial bits to 00, while IR uses stationary initial bits and hence N=M+2 independent observations. The arbitrary-initialization minimax permits both. Combining their lower risks by maximum is valid; no single common prior or worst-case initial law is required. The IR bound's common deterministic influence budget and uniform error E/Q are retained. The alphabet lower needs only H possible labels, but the depth lower uses the stricter boundary restriction to functions of fixed public positional bits. The theorem preserves this distinction and makes no unsupported claim about arbitrary nonlocal finite side information.

8. **Paid resources and claim boundaries.** The ledger is deliberately conservative. It charges fine work precision, count/address guards, every token/layer, dense masks/zero slots, optional heads, coefficient/mask generation, signed decoder arithmetic, and terminal clearing/isolation. Decoder word sizes fit P>=h+r. Its explicit scanning realization eliminates unit-cost random-access assumptions and charges program/address storage and offline generation. The primitive-depth assertion is expressly not a fixed-width PURE bit-gadget depth bound. Nothing here proves work-optimality, training, a general Markov upper, or an exact same-constant threshold.

## Independent executable evidence

`IC001_independent_checks.py` was written independently for this review. Exact rational/integer checks cover:

- 70,209 geometry cases: every fine-cell endpoint and midpoint for a finite grid of J,h,r, testing reconstruction containment, interval diameter and endpoint-denominator divisibility; 4,717 cases yield singleton fibers.
- 91,770 finite count-mean cases at minimal and enlarged work precision, testing the decoded deterministic error and every intermediate precut error.
- 2,178 closed coarse-bin / partial-fold-branch containment cases.
- 47,652 capacity/ceiling cases, including exact powers and neighbors, Q=2, M=1, saturated and unsaturated depth, and several positive capacity constants.

The JSON records the theorem hash and exact counts, including encountered negative-slope stages. These finite checks supplement the preceding mathematical reasoning; they do not establish universal claims by exhaustion. No substantive defect or mandatory theorem revision was found.
