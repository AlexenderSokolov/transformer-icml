# RG001 — fixed-dimensional recursive robust grid snake

2026-11-02. EXPLORATORY CANDIDATE, NOT ACCEPTED. Depends on accepted RP001 (root receipt `../intake/RP001_acceptance.json`) and fresh RG001 independent review. IID only. No novelty claim: scalar geometric packing and folding are established; see local prior-art comparison. Frozen artifacts unchanged.

## Statement
Fix integer J>=2 and c>=0. Choose integer a>=1 with 2^a>=8 sqrt(J)(c+1). Put Q=2^h, h>=a+1, N=2^(h-a)=2^k. There is a continuous causal attention/ReLU encoder with exactly J exposed [0,1] coordinates, width O(J), bounded scalar states, coefficients at most 4, and primitive depth O_J(1+log Q). After any history-dependent randomized one-shot coordinatewise perturbation bounded by c/Q, clipping and downward Q-quantization, a paid finite decoder satisfies

 E|p_hat-p| <= 1/(2sqrt(M)) + [1+2sqrt(2J)(c+1)2^((J-1)a)+(J-1)2^(Ja)]/Q^J.

The M generated bits are IID Bernoulli(p), initial pair arbitrary and ignored. Only J labels, optional ignored finite boundary label, and public source-independent metadata survive. No unquantized data, count, timing, duplicated rail or history reread survives. Together with inherited alphabet/statistical lower bounds and admissibility of the zero attack, this would establish robust IID order max(M^-1/2,Q^-J) at fixed J,c. This is not a full Markov upper, general training claim, internal-noise theorem or efficient-decoder claim.

## Explicit recursive formula
Let T(u)=2u-4relu(u-1/2) on [0,1], C(u)=min(1,max(0,u)). Define P_1(t)=t. For j=2,...,J set L_j=N^(j-1), eta_j=1/(2L_j+2). Compute

 v=T^k(t), A=T^(k+1)(t),
 B=T^k(T_ext(t+1/(4N))),
 T_ext(x)=2x-4relu(x-1/2)+4relu(x-1),
 z=min(1-A,L_j relu(1/2-B)), s=A/2+z,
 S_j(t)=t-s/N,
 u_j(t)=C(v+v/L_j-1/(2L_j)),
 P_j(t)=(P_(j-1)(u_j(t)),S_j(t)).

Amplification L_j is realized by (j-1)k saturated doublings b<-min(1,2b), starting b=relu(1/2-B); min with 1-A makes saturation equivalent to unsaturated multiplication. No primitive coefficient exceeds 4. Division by N or L_j uses small dyadic coefficients. Sequentially compute the j-th stair and folded input, retain S_j, then recurse downward; fixed J permits O(J) rails and sum O(jk)=O(J²k) stages. T_ext input is in [0,1+1/(4N)] and output in [0,1]. Signed intermediates are bounded by an absolute constant. All dyadic biases have O_J(h) bit descriptions.

The RP phase identity yields, for t=(i+r)/N, 0<=i<N, 0<=r<=1,

 S_j=i/N for r<=1-eta_j;
 S_j=i/N+(r-1+eta_j)/(N eta_j) for r>=1-eta_j.

On each row, u_j is the alternating orientation map from 0 to 1 or 1 to 0, with initial and final clipped portions r in [0,eta_j] and [1-eta_j,1]. During its active interval |du_j/dt|=N(1+1/L_j). The terminal r=1 gives the following row consistently; at t=1 use the last row. These identities follow by substituting L_j for N in RP's scalar phase calculation, not by presuming a discrete staircase oracle.

## Full inductive geometry
Define an ordered edge list for P_1 as the single segment [0,1]. In dimension j, append for each i=0,...,N-1 a copy of the dimension-(j-1) list in the plane x_j=i/N, in forward order for even i and reverse order for odd i; then append the outer-direction segment of length 1/N from that copy's finishing endpoint to the plane (i+1)/N. N is even. Thus P_j starts at (0,...,0), ends at (0,...,0,1), and contains no final copy in plane x_j=1. The formula traces exactly this list, with possible stationary times only at its vertices. Edge count E_1=1, E_j=N E_(j-1)+N, so E_j=O_J(N^(j-1)). Every edge is parallel to one axis; every vertex lies in the N-grid.

Inductive proof of simplicity and separation: within one copy use the previous dimension. Distinct copy planes are at least 1/N apart. Two connector edges have disjoint outer intervals except possibly adjoining intervals; adjacent connectors are anchored at opposite endpoints of the lower-dimensional curve, whose distance is 1, and nonadjacent intervals are separated by at least 1/N. A connector versus a copy in a nonadjacent plane is separated by at least 1/N in the outer coordinate. In either adjacent plane the connector's anchor is one endpoint of the lower-dimensional curve. Every edge not incident to that endpoint is at least 1/N from it, by the inductive nonincident separation (or the grid geometry for the one-edge base); the sole incident edge is perpendicular to the connector. Hence all nonincident edges have Euclidean separation at least 1/N, and incident edges are perpendicular. There are no repeated vertices or nonlocal endpoint contacts. The preceding endpoint-distance assertion also follows directly from axis-aligned grid edges: a grid vertex not on a grid edge is at least 1/N away; simplicity excludes membership in any other edge.

Moving speed along every edge is at least N^(j-1). This holds for copies because the previous minimum N^(j-2) is multiplied by N(1+1/L_j), and for outer connectors because their speed is 1/eta_j=2L_j+2. Let V_j be the maximum coordinate slope. V_1=1 and V_j<=max{N(1+1/L_j)V_(j-1),2N^(j-1)+2}, giving V_j<=3·2^(j-2)N^(j-1) for j>=2. This bounds the global l-infinity Lipschitz constant, not merely a typical derivative.

Let lambda_j bound the length of the entire preimage interval of any vertex (equivalently the maximum stationary interval), with lambda_1=0. The initial clipping in a row contributes eta_j/N. An inherited endpoint plateau contributes at most lambda_(j-1)/[N(1+1/L_j)]; interior inherited plateaus contribute only that term. The final clipped portion is a moving connector and contributes no stationary duration. Even when a reversed lower copy ends in its initial plateau, it merges only with a possible initial clip at the same vertex, bounded by the same sum; a nonzero connector separates it from the next copy. Therefore

 lambda_j<=eta_j/N+lambda_(j-1)/N <= (j-1)/(2N^j).

If two curve points have Euclidean distance d<1/N, choose their containing edges. Nonincident separation forces equal or incident edges. The connecting subpath has length <=sqrt(2)d. Every edge has length at least 1/N. In the incident-edge case d<1/N therefore excludes either outer endpoint: its distance to any point on the other perpendicular edge is at least the first edge length. Thus the only possible vertex fiber inside this local subpath is the shared corner. In the equal-edge case the subpath contains at most two endpoint fibers (indeed d<1/N excludes containing both). Any two preimages differ by moving time at most sqrt(2)d/N^(J-1) plus at most two whole vertex plateaus, including any endpoint preimage choice. Thus

 |t-t'| <= sqrt(2)d/N^(J-1)+(J-1)/N^J.       (L)

This includes d=0 and arbitrary choices within endpoint fibers.

## Rational finite decoder and robust estimate
The perturbed, clipped, quantized point q differs from P_J(t) in Euclidean norm by at most r0=sqrt(J)(c+1)/Q. Enumerate the E_J segments, project q onto each by coordinate clamp, compare squared rational distances and break ties by public order. The selected point w' satisfies ||w'-P_J(t)||<=2r0<1/N. Choose an actual preimage t' on its selected affine segment. Applying (L),

 |t'-t| <= 2sqrt(2J)(c+1)/(QN^(J-1))+(J-1)/N^J.       (R)

There is no real-valued nearest-point oracle: recursive table generation retains, for each moving affine piece, both rational parameter endpoints and rational geometric endpoints. To build a row, map each child's parameter interval by the inverse of u_j, using its orientation; append the explicit outer connector interval [(i+1-eta_j)/N,(i+1)/N]. Initial and inherited stationary intervals need not be decoded: either incident moving piece supplies an endpoint preimage. Base P_1 is affine on [0,1]. The total rational numerator/denominator length is O_J(log N), since recursive products include only J factors of N and 2L_j+2. The selected projection has O_J(h) rational bit length. List generation, storage, comparisons, inversions and tie ordering all cost O_J(E_J) bounded-word arithmetic operations and O_J(E_J h) bits. Degenerate stationary pieces are excluded; every listed moving interval has positive length. Endpoints t=0,1 are covered by (L) even when decoding chooses another preimage.

## Exact uniform-precision causal evaluator
Set p0=Jh+b_J, b_J=ceil(log2(3·2^(J-2)))+1; let G=(J-1)(J-2)k/2 and P=p0+G. The initial mean must have only p0 fractional bits: a naive P-grid mean followed by divisions in u_j would NOT be exact on the P-grid. Implement the required coarsening within the uniform-P signed affine/full-product/floor family as follows. Scale input bits by 2^-G, use causal zero-logit attention on the scaled bits, then apply G doublings to the pooled output. At each row this yields exactly t=floor(2^p0 x)/2^p0, since floor(2^P·2^-G x)·2^G/2^P equals this value. In the ideal real architecture scaling and doublings cancel and recover x. At each doubling the actual and ideal rails remain in [0,1]. If G=0 no scaling/doubling is needed. Coefficient 2^-G is exactly P-representable.

Use FG001's own-prefix masks, excluding the arbitrary initial pair; public singleton fallbacks cover rows 1,2, and the synthetic terminal averages all M generated bits. No final mean is copied backwards. All allowed masks are causal and have fixed positive density. Uniform Taylor weights at zero logits cancel exactly; the initial scaling merely changes the values in this same exact attention ratio.

For the recursive stages, suppose incoming t has fractional exponent at most e, initially p0. Since e>=k+2, the shifted argument in B is on this grid. Tent multiplication by 2 followed by integer biases makes v have exponent at most e-k, A and B at most e-k-1. The relu bias 1/2, saturated doublings and min operations preserve these bounds. Then s has exponent at most e-k, and s/N has exponent at most e. Thus S_j is exactly representable with exponent e. The output u_j has exponent at most e+(j-2)k: the division v/L_j contributes (j-1)k after the k tent doublings; its bias has exponent (j-1)k+1, no larger than this bound since e>=k+1. Clipping preserves it. Descending j=J,...,2 consumes at most G additional bits in total. Every intermediate lies on the single P-grid and every affine-floor stage is exact after the initial attention floor. Half-biases and endpoint branches are covered. Products retain their full signed guarded length before the floor; no sequential partial-product truncation is assumed.

Initial mean error is at most 2^-p0<=Q^-J. The final ideal-to-finite coordinate error is at most V_J 2^-p0<=1/Q, by N<=Q and the choice of b_J. This is a direct uniform E=1 pre-cut certificate on every row/formal history; no intermediate-rail E/Q claim is needed. Combining (R), this mean error, and E|x-p|<=1/(2sqrt(M)) proves the stated risk.

## Paid resources and inherited scope
Let d=O_J(1+h), n=M+3, w=C_J(P+log(n+1)+log(d+1)+1), with sufficient factor for signed full products, rational decoder integers, count and address guards. With E_J=O_J(N^(J-1)), conservative costs are

 T0=O_J(d n²(P+1)w²+(d+n+E_J)w²),
 S0=O_J(d n²+d J²w+n Jw+E_J w+w^4).

All token/layer masks (including excluded entries), dense affine/QKV zero slots, scalar coefficients and generation, optional dummy heads, scaled input acquisition, integer counts/divisions, all row rails, temporary products, segment generation/table, final labels and clearing/isolation are paid. The decoder is explicitly polynomial in N, NOT logarithmic-time. Loop-program and table descriptions are source independent and paid. The same conservative addressed-tape compilation as FG001 stores O(T0 w) instruction/address bits and scans S0 bits per instruction, giving online bitwork O(T0 S0 w), peak O(T0 w+S0) plus actual offline scratch, offline generation O((T0+S0)w²). PURE Boolean/ReLU compilation pays its actual larger gate-slot/depth costs; O(log Q) concerns attention/affine/ReLU primitives with finite evaluation, NOT bit-machine or PURE depth. No arbitrary-real constants or uncharged nearest-segment oracle appear.

No quantitative necessity beyond inherited alphabet/statistical lower bounds is established here. IR001 applies only to its named common bounded-influence/approximation family; noisy upper admissibility does not enlarge that lower theorem. This is a changed encoder, not a repair or claimed robustness of FG001's reflection-vulnerable rails. RP001 is accepted; all fresh RG001 review gates must pass before accepting RG001.
