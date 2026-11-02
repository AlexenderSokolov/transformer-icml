# RP001 — continuous bounded-primitive robust snake, J=2

2026-11-02. Candidate, independent review pending. Changed encoder, not FG001. IID only; no novelty claim. Geometric scalar packing and nearest-curve reconstruction are established (Uss et al., ICML 2025; local prior-art comparison). The contribution being checked is an explicit paid bounded-primitive realization.

## Statement
Fix c>=0. Choose an integer a>=1 with 2^a>=8(c+1). Let Q=2^h, h>=a+1, N=2^(h-a)=2^k. For M generated IID Bernoulli(p) bits, arbitrary initial pair, the target is p. There is a continuous causal bounded-coordinate ReLU/zero-logit-attention encoder with exactly TWO exposed coordinates in [0,1], fixed width, coefficients at most 4, and primitive depth O(1+log Q). A finite exact evaluator using O(log Q) fractional bits plus count/address guards is specified below. After arbitrary one-shot coordinatewise pre-Q-quantization perturbation at most c/Q, clip to [0,1] and downward quantize. Only the two labels and public source-independent metadata survive. The decoder satisfies

 E|p_hat-p| <= 1/(2 sqrt(M)) + [1+4(c+1)2^a+2^(2a)]/Q^2.

The adversary may depend on the whole history and randomize: the recovery bound is pointwise. Clipping is part of the declared channel; alternatively perturbations can be required to remain in [0,1]. No unquantized count, duplicated rail, timing channel, or unknown-p metadata survives. Extra fixed coordinates may be zero, but this theorem claims Q^-2, NOT Q^-J for J>2. For fixed c the inherited alphabet/statistical lower and zero-attack admissibility imply order max(M^-1/2,Q^-2) for this two-coordinate noisy interface. Depth necessity follows only in the separately stated common IR001 approximation family, not for arbitrary finite encoders.

## Explicit continuous formula
T(u)=2u-4 ReLU(u-1/2), 0<=u<=1. Write C(u)=min(1,max(0,u)), implementable by two ReLUs. For scalar t in [0,1], compute

 v=T^k(t),
 A=T^(k+1)(t),
 B=T^(k+2)(t/2+1/(8N)),
 z=min(1-A, N ReLU(1/2-B)),
 s=A/2+z,
 Y=t-s/N,
 X=C((1+1/N)v-1/(2N)).                         (1)

The factor N is NOT a primitive coefficient: start u=ReLU(1/2-B), repeat u<-min(1,2u) exactly k times, then z=min(1-A,u). This is identical since 0<=1-A<=1. All working rails are bounded by a fixed constant. Min uses min(f,g)=f-ReLU(f-g); signed intermediates are bounded as well. The three tent chains can be run sequentially with a fixed number of retained rails, giving O(k) primitive stages and fixed width. All affine coefficients, including 1+1/N and biases, are dyadic and bounded by 4. No multiplication of variable rails, discrete branch oracle, or growing intra-stage DAG is used.

## Formula verification and geometry
Let r be the fractional part of Nt, away from its endpoints; let eta=1/(2N+2). The pair (A,B) equals (tri(r),tri(r+1/4)), where tri is the period-one triangle of height 1 and slopes +/-2. This follows from the standard dyadic tent identity, including the shifted argument, which stays in [0,1]. On r in [0,1/2], B>=1/2, so s=r. On [1/2,1], A=2(1-r), and ReLU(1/2-B) equals min(A,1-A). Therefore

 s=r for 0<=r<=1-eta,
 s=(2N+1)(1-r) for 1-eta<=r<=1.

Consequently Y=i/N on t in [i/N,(i+1-eta)/N], then rises linearly to (i+1)/N during the remaining eta/N interval. X traverses from one horizontal endpoint to the other on [(i+eta)/N,(i+1-eta)/N], alternating orientation, and is constant during the connector and the following initial plateau. The initial plateau starts at t=0; the final connector ends at t=1.

Thus the image is the simple axis-aligned serpentine path consisting of horizontal H_i=[0,1]x{i/N}, i=0,...,N-1, and vertical V_i at the horizontal endpoint, from i/N to (i+1)/N, i=0,...,N-1. There is no horizontal H_N. Nonincident edges have Euclidean distance at least 1/N. Incident edges are perpendicular. The only parameter noninjectivity is a stationary plateau of duration eta/N at each horizontal starting vertex, including t=0. Horizontal speed is N/(1-2eta)>=N; vertical speed is 1/eta>=N.

If two image points have distance d<1/N, their containing edges can be chosen equal or incident. Their connecting path length is at most sqrt(2)d. Any two preimages therefore differ by at most sqrt(2)d/N+2eta/N: at most two stationary plateaus occur along that local subpath, including endpoint choices. This is a deliberately loose bound.

## Noise and finite decoder
Let w=(X(t),Y(t)). After perturbation, clipping and downward quantization, the decoded coordinate pair q obeys ||q-w||_2<=r0=sqrt(2)(c+1)/Q. Choose a Euclidean nearest point w' on the path (ties by fixed edge order), and choose a preimage t' using the inverse affine segment formula. Then ||w'-w||<=2r0<1/N by the selected a. The local bound gives

 |t'-t| <= 4(c+1)/(QN)+2eta/N <= 4(c+1)/(QN)+1/N^2.       (2)

The decoder enumerates exactly 2N edges, projects by coordinate clamping, compares squared rational distances without square roots, and inverts the selected segment. For H_i, orient the coordinate f=X if i even and 1-X otherwise, and choose t'=(i+eta+(1-2eta)f)/N. For V_i choose t'=(i+1-eta)/N+eta(Y-i/N). These are actual preimages, including endpoints. On the shared start endpoint H_0 the formula chooses eta/N rather than 0, which is permitted. All arithmetic is rational with O(log Q) bits. This costs O(N) arithmetic operations and O(N log Q) bits if the entire path table is stored; no efficient decoder lookup is assumed.

## Exact finite causal evaluator and statistical step
Use FG001's causal prefix-mean pooling masks, including its public singleton fallbacks. At terminal set t=floor(2^p x)/2^p, x=A_count/M, p=2h. At other rows use their own causal means, never terminal means. Perform (1) exactly. A common fractional grid of P=p+2k+6 bits suffices: initial t has denominator 2^p; shifted input has denominator dividing 2^max(p+1,k+3); tent/min/clipping/doubling do not increase denominators; final coefficients 1/N and 1/(2N) add at most k+1 bits. P is intentionally loose. All constants and products therefore fit the fixed lattice exactly. One can first use a p-bit pooling stage and then embed exactly into the P-bit subsequent stage; both precision schedules are paid. A uniform-P alternative is to use t=floor(2^P x)/2^P and increase later precision to P+2k+6; stage-varying fine precision, rather than impossible closure under arbitrary dyadic multiplication at one initially saturated grid, is explicit.

The terminal rounding error is <=Q^-2. Combining (2) and E|x-p_source|<=1/(2sqrt(M)) proves the displayed risk. The source parameter is here denoted p_source to distinguish the work exponent p. Pooling excludes the arbitrary initial pair as in FG001. Any declared finite side label may be ignored.

Admission to the uniform E/Q ideal-to-finite contract follows directly: the map (1), being the parameterized snake above, has coordinate slopes bounded by 2N+2, so coordinate error <=(2N+2)Q^-2<=1/Q for N<=Q/8, Q>=16. Intermediate rails need not satisfy this final-cut certificate. No internal fault robustness is asserted.

## Paid resource ledger
Let d=O(1+h), n=M+3, P=O(h), w=C(P+log(n+1)+log(d+1)+1), for a sufficiently large absolute C. Coefficients, all dense affine zero slots, dyadic biases, masks, counters, addresses, source acquisition, rolling row rails, precision schedules, temporary full products, output labels and clearing are included. Using FG001's conservative generic Taylor/uniform-pooling implementation before the exact dyadic stages, safe arithmetic bitwork/storage bounds are

 T0=O(d n^2 (P+1)w^2+(d+n+N)w^2),
 S0=O(d n^2+d w+n w+Nw+w^4).

The Nw term pays an explicit decoder edge table and generation; it can be streamed but need not be. The O(N) decoder and its table are intentionally NOT claimed logarithmic-time. The network architecture is logarithmic primitive depth, while full evaluation and decoding work is larger and paid. Coefficient/program generation can use fixed loops with O(h)-bit dyadic constants. As in FG001, a conservative sequential tape compilation storing O(T0 w) instruction/address bits and scanning S0 bits per instruction gives bitwork O(T0 S0 w), storage O(T0 w+S0), and offline generation O((T0+S0)w^2). No free giant real constants, arbitrary-real nearest-point oracle, hidden table, or unit-cost arbitrary-length arithmetic is granted.

## Failed approaches and limits
* Original mean plus folds is not robust to the FN001 reflection attack; this changes both coordinates.
* Clipping a tent alone makes suitable horizontal plateaus but supplies no vertical staircase. Claiming the monotone rail without its phase-shifted triangle formula would be a gap.
* A direct sum of N hinge functions supplies a staircase only at linear width or linear sequential depth. It is a valid expensive baseline, not the O(log Q) construction.
* A naive smoothed binary-digit extraction produces long diagonal connectors and lacks the required nonincident-edge separation.
* An unrestricted coefficient N violates the primitive bound, and its unbounded intermediate violates the state bound. Saturated repeated doubling is essential.
* The claim currently stops at two coordinates. A higher-dimensional recursive snake may be possible but is not supplied here.
* No optimal decoder cost, training result, full Markov upper, internal-noise guarantee, hardware result, or novelty certification is asserted.
