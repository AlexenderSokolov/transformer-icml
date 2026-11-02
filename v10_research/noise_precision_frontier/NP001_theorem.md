# NP001 — independent fault amplitude, effective precision and IID depth/capacity

2026-11-02. New research candidate; fresh independent review pending. No frozen artifact changed. Dependencies GN001, IR001, IC001, RG001 and RP001 have root acceptance receipts. We do not vary GN001's hidden fixed-c constants: the channel estimate and constants are rederived uniformly below. No novelty, formal verification, general Markov upper, training or optimal bit-complexity claim.

## 1. Experiment, public noise specification and result

Fix J>=2, b>=0, and fixed bounds for the accepted bounded-size attention/affine/ReLU primitive family, wide enough for GN001's J-coordinate curve. Bounds on coefficients, heads, fan-ins, local radius, mask density and ideal states are independent of M,Q,d and the fault amplitude. Let H=2^b. Observe an arbitrary initial binary pair followed by M>=1 independent Bernoulli(p) generated symbols, p in [0,1]; target is the next-symbol parameter p. Primitive depth d>=1 counts actual bounded-size stages, not a growing circuit inside one stage. Only J coordinate labels, at most b source bits at public fixed positions, and source-independent public seeds/metadata survive; no history reread, timing port, duplicate unquantized rail, counts or residual work memory is available. The unknown p is never metadata. The lower permits randomized encoders with its contracts holding seedwise. The upper ignores the boundary label and initial pair.

The actual finite precut bank a belongs to [0,1]^J. Its ideal bounded-primitive bank f has uniform error ||a-f||_infinity<=E/Q on every formal history with boundary branch frozen, for a fixed E>=1. Quantization resolution is Q=2^h, h>=1. The adversary applies ONE coordinatewise REAL precut perturbation e, ||e||_infinity<=δ, then the channel sends

    q_j = floor(Q clip(a_j+e_j))/Q,     0<=δ<=1/4.

The adversary may see the history, finite bank and public seed and may randomize; it may not change the declared side label. Real perturbed values, not just points on the evaluator's fine grid, are permitted. Arithmetic at other stages is reliable. This is NOT the old canonical post-Q-grid channel, nor a claim of identical lower bounds for fine-grid-restricted attacks. Real-valued adversarial operations need no finite implementation, while the constructive encoder and decoder below do.

Let R be minimax worst-case expected |p_hat-p| over p, arbitrary initial-pair laws, and this attack class. Put

    s=M^(-1/2),  τ=max{Q^(-1),δ},  Q_eff=τ^(-1)=min{Q,1/δ},

with 1/0=+infinity. Thus 0<τ<=1/2 and Q_eff>=2. The admitted primitive family has a fixed C>=2 with total ideal replacement influence <=C^d. There is γ=γ(J,b,E)>0, independent of δ,Q,M,d, such that every admitted construction satisfies

    R >= max{3s/64, c_cap τ^J, γ τ/C^d},                  (1)
    c_cap = 1/[16 H (3/2)^J].

To avoid any free real-description oracle in the upper, supply the public integer m>=1 with the certificate

    τ <= t:=2^(-m) < 2τ.                                 (2)

Such m exists (take m=floor(log2(1/τ))); its numeric value is at most h. The upper uses only m and h, not arbitrary digits of δ. The certificate is a declared public budget promise, not information about the sampled history or p. For rational δ given as signed numerator/positive denominator, it can instead be computed by exact comparisons, with the input bit cost paid in §6. For an arbitrary real δ, no algorithm to extract m from an unspecified real is claimed: the scale certificate is an explicit part of the upper interface. Lower (1) requires no such certificate and remains valid with it.

Choose once and for all the INTEGER D>=12 sqrt(J). Set K=6 sqrt(2J). For every dyadic N>=2 with

    N <= 1/(D t),

a finite causal encoder and rational decoder give

    R <= s/2 + K τ/N^(J-1) <= s/2 + K t/N^(J-1),
    d <= a_J+b_J log2 N, width <=W_J, ideal-to-finite error <=1/Q. (3)

The constants a_J,b_J,W_J and evaluator constants are uniform in δ,Q,M,N. A fixed-depth scalar-mean fallback gives

    R <= s/2 + δ+2/Q <= s/2+3τ <=s/2+3t.                 (4)

Consequences, with constants depending only on J and fixed primitive bounds:

* At depth allowance O_J(1+log Q_eff), risk O_J(s+τ^J) is achievable for every M,Q,δ. Together with (1), this is the robust capacity risk order max{s,τ^J} when this depth is allowed.
* Let κ_J=2^J(2D)^(J-1). If Q_eff^J>=κ_J sqrt(M), statistical order R<=A_J/sqrt(M) is achievable with depth O_J(1+log_+(τ sqrt(M))), where A_J=1/2+max{3,K} is one sufficient multiplier.
* Conversely, R<=A/sqrt(M) necessarily implies A>=3/64,

    Q_eff^J >= (c_cap/A) sqrt(M),
    d >= max{0, log(γ τ sqrt(M)/A)/log C}.                (5)

This is a necessary/sufficient ORDER sandwich with distinct numerical constants; sufficiently large fixed effective-capacity ratio suffices. It does not assert same-multiplier iff, sharp all-depth exponential base, or sufficiency for every positive capacity constant at the displayed A_J.

In particular, fixed δ>0 and fixed J impose R>=c_cap δ^J for every M,Q,d. Increasing transmission precision or depth alone cannot make this risk vanish. Any consistent family with fixed J must have δ->0 (and Q->infinity); allowing width/exposed dimension to grow is outside this fixed-J theorem and is only a possible escape, not a sufficiency claim.

## 2. Two common attacks prove the capacity and depth lower bounds

Use the admissible zero attack first. There are at most H(Q+1)^J labels. For each fixed public/decoder seed, at most that many estimator outputs are possible. A uniform parameter prior on [1/4,3/4] and the union of small intervals around these outputs give the accepted IC001 finite-alphabet lower

    R>=1/[16 H(Q+1)^J] >= c_cap Q^(-J).

The argument is valid with randomized observations and source-independent encoder/decoder seeds, by fixing and then averaging them; it does not count seed values as additional source-dependent messages.

For δ>0 define the same deterministic coordinate attack for EVERY p and history:

    A_δ(a)=δ floor(a/δ),  a in [0,1].                    (6)

It moves down by a-floor(a/δ)δ in [0,δ), so it is legal, including a=0,1. It remains in [0,1], making clipping redundant. There are at most floor(1/δ)+1 coordinate values before final Q-flooring; that flooring cannot increase the alphabet. Including the boundary label, the count is at most H(floor(1/δ)+1)^J. The same covering argument gives

    R>=1/[16H(floor(1/δ)+1)^J]
      >= δ^J/[16H(5/4)^J] >= c_cap δ^J.                 (7)

Here 1+δ<=5/4 since δ<=1/4. Taking the maximum of zero-attack and coarse-attack lower bounds proves c_cap τ^J. These are common attacks independent of the unknown p, not pair-specific attacks or an illicit adversary choosing a different channel for each p.

For depth, distinguish two cases. If δ<=1/Q, zero attack invokes IR001 at its original Q and error E/Q, yielding γ/(Q C^d)=γτ/C^d. If δ>=1/Q and δ>0, use (6), but GRANT the decoder the complete coarse index k_j=floor(a_j/δ). This is a lower-bound oracle only: it can reconstruct the actual received label as floor(Q δ k_j)/Q using public δ, so it is at least as informative as the attacked channel. For arbitrary real δ this simulation is mathematical, not an upper finite-computation assertion. Source-independent knowledge of δ can be granted without harming a lower bound.

IR001 explicitly permits real resolution Q'>=1, not only dyadic grids. Apply it to the ORIGINAL actual bank a and ideal f with Q'=1/δ>=4. The oracle observes floor(Q'a_j)/Q'=δ k_j. Since δ>=1/Q,

    ||a-f||_infinity <=E/Q <=Eδ=E/Q'.

All ideal formal-history influence bounds and the positional-bit boundary are unchanged. Thus IR001 gives γ/(Q'C^d)=γδ/C^d. The same γ(J,b,E) works in both cases; no Qδ-dependent approximation constant is introduced. One must not apply a Lipschitz argument to the discontinuous attacked bank: IR is applied to a, with its coarse label, NOT to A_δ(a) as a new ideal network.

For the statistical term, choose zero attack and the fixed initial pair (0,0), and grant all M generated bits; IC001's testing bound gives 3/(64sqrt(M)). For the IR term instead choose the stationary Bernoulli(p) product initial pair, so ALL M+2 observed bits are IID exactly as required by IR001. Arbitrary-initialization minimax contains both witnesses. Their priors and initializations need not agree. The three lower bounds combine by maximum, not by an unsupported common witness. Public fixed-position boundary bits (possibly depending on public seed) remain precisely IR's allowed side information, not an arbitrary nonlocal finite statistic.

## 3. Uniform robust upper, without varying fixed-c hidden constants

We import GN001 §§2–3's proved no-plateau curve P_J:[0,1]->[0,1]^J for each dyadic N=2^k>=2. To identify the exact object, let T(u)=2u-4relu(u-1/2), T_ext(u)=T(u)+4relu(u-1), V_k=T^(k-1) composed with T_ext on the first input. Start P_1(u)=u. At recursive level j>=2 use L=N^(j-1), η=1/(2L+2), and

    A=T^(k+1)(u), Bphase=T^k(T_ext(u+1/(4N))),
    z=min(1-A,L relu(1/2-Bphase)), zeta=A/2+z,
    S_j(u)=u-zeta/N,
    v=V_k(u+η/(2N)), u_j=clip((v-η/2)/(1-η)),
    P_j(u)=(P_(j-1)(u_j),S_j(u)).                         (8)

The multiplication by L is implemented by (j-1)k saturated doublings before the final min; it is not a coefficient of size L. All coefficients have magnitude <=4, fixed J gives bounded state/fan-in/width, and sequential stage count is <=a_J+b_J k. Rational parameter descriptions have O_J(1+log N) bits. These bounds depend on J and N through stage count/description only; they do not depend on c,δ,Q or M.

GN001 proves: the curve is a simple axis-aligned N-grid snake, with E_1=1, E_j=NE_(j-1)+N edges, hence E_J=O_J(N^(J-1)); nonincident edges have separation >=1/N, incident edges are perpendicular, every moving edge has speed >=N^(J-1), and there are NO stationary plateaus. Consequently

    ||P_J(u)-P_J(v)||_2<1/N
       => |u-v|<=sqrt(2)||P_J(u)-P_J(v)||_2/N^(J-1).     (9)

This import is independent of any fault bound. The shifted first tent is T_ext, including the last row past 1; using an ordinary unextended tent would invalidate the formula. The no-plateau fact is essential: the older RP/RG inverse's additive N^-J term would not establish the present shallow statistical selection.

Let x be the exact mean of the M generated bits. Use §5's finite evaluator, so ||a-P_J(x)||_infinity<=1/Q. After ANY legal attack, clipping cannot increase distance to a point in [0,1], and final flooring has error <1/Q. Therefore

    ||q-P_J(x)||_2 <=sqrt(J)(δ+2/Q) <=3sqrt(J)τ=:r.

Project q onto every edge, and choose a nearest projection w with public deterministic ties. The true P_J(x) is a competitor, so ||w-P_J(x)||_2<=2r<=6sqrt(J)t. As N<=1/(Dt) and D>=12sqrt(J), this is <=1/(2N)<1/N. Invert the selected rational affine edge parameterization; (9) gives

    |xhat-x| <=6sqrt(2J)τ/N^(J-1)=Kτ/N^(J-1).            (10)

This is pointwise for every history, initial pair and randomized/adaptive attack. Then E|x-p|<=1/(2sqrt(M)) proves (3). All δ,Q dependence is visible in (10); neither geometric nor per-stage evaluator constants have been allowed to vary with Qδ. The scalar construction retains the mean and J-1 zeros, and the same argument gives (4). No duplicate mean or noncut work state survives.

The decoder enumerates E_J rational edge segments, projects the rational q by coordinate clamping, compares squared distances by exact cross multiplication, and inverts the chosen affine parameter map. Edge geometric and parameter endpoints have O_J(log N) rational bit length; q has O(h) bits. Thus output and comparisons use O_J(h+log N) bits up to a fixed factor. The output is a finite high-precision rational, NOT required to be a Q-grid probability. Imposing that extra output grid would change the theorem. Arithmetic cost is polynomial in E_J,N and h, not logarithmic in N.

## 4. Selections and all endpoint regimes

Full effective-capacity packing: if Dt<=1/2, choose the largest dyadic N<=1/(Dt). It is >=2 and N>1/(2Dt). Equation (3) gives

    R<=s/2+K(2D)^(J-1)t^J <=s/2+K(2D)^(J-1)2^J τ^J.

Its primitive depth is O_J(1+log(1/τ)). If Dt>1/2, use scalar fallback. From t<2τ follows τ>1/(4D), hence 3τ<=3(4D)^(J-1)τ^J. This proves the full-risk statement including Q=2 and all coarse/noisy cases with no admissible snake. At Dt=1/2, N=2 is admissible.

Statistical selection: suppose τ^(-J)>=κ_J sqrt(M), where κ_J=2^J(2D)^(J-1). Because t<2τ,

    t^(-J)>2^(-J)τ^(-J)>=(2D)^(J-1)sqrt(M).             (11)

If t sqrt(M)<=1, choose scalar fallback and obtain R<=(1/2+3)/sqrt(M). Otherwise let N be the least dyadic number >=(t sqrt(M))^(1/(J-1)); then N>=2 and

    N<2(t sqrt(M))^(1/(J-1))<=1/(Dt),

where the final inequality follows from (11). The constructive error is <=K/sqrt(M), and

    log2 N < 1+log2(t sqrt(M))/(J-1)
             <=1+[1+log2_+(τ sqrt(M))]/(J-1).

This proves the claimed depth and A_J. Square roots need not be numerically approximated: choose the least k>=1 such that 2^(2k(J-1))>=t² M; the scalar decision is t²M<=1. All tests are exact rational/integer comparisons. Capacity (11) is a sufficient hypothesis on resources, not an algorithmic test requiring real δ. The selected public m is enough. Necessity (5) follows directly by rearranging (1), so necessary and sufficient constants are not conflated.

## 5. Causal finite implementation and uniform arithmetic tube

Use exactly GN001 §5's accepted rational-description extension of FA/GD, rather than pretending (8) has dyadic coefficients. A rational a/b with positive denominator and total bit length Bpar is converted to floor(2^P a/b) by signed integer quotient with negative-floor correction, cost O((Bpar+P)^2) bitwork, O(Bpar+P) scratch, coefficient error <2^-P. FA's signed full-product affine/single-floor, ReLU, Taylor and normalized-attention operations follow unchanged. Their one-step estimates use only bounded ideal coefficients and this conversion error, so the uniform GD induction applies to the rational-data extension.

The exact ideal scalar at each historical row is its OWN causal mean over generated positions 3,...,t; at the synthetic terminal it is the mean of all M generated bits. Positions 1,2 have public singleton fallbacks. Public masks are causal, nonempty, branch-independent and have density >=1/4. The synthetic initialization contains no source-dependent mean or count. All rows undergo (8) with bounded ideal retained rails on every formal history. Fixed primitive constants provide A>=2 independent of N,M,h,d,δ. Choose fixed c_FA>=4 so A(c_FA+5)2^(1-c_FA)<=1 and set

    P=4h+c_FA(d+2).

The GN/GD induction yields maximum stage/readout discrepancy

    A^(d+2)(P+1)2^(-P)<=1/Q,

closing its <=1 bootstrap and paying initial attention error, parameter conversion, and every intervening arithmetic step. Exact lattice clipping keeps the actual bank in [0,1]^J and cannot worsen error to the ideal bank; fixed clip-stage overhead is included in d. This E=1 certificate is uniform in δ and N: δ enters only AFTER the evaluator. No plateau formula, lattice-exact rational-stage assertion, or depth-dependent E is used. Scalar fallback uses the same evaluator and certificate.

## 6. Paid metadata, program, working precision and decoder

Let n=M+3, U=O_J(d n²) supplied scalar slots and F=O_J(d n²+n log(n+1)) mask/metadata bits; zeros and excluded slots count. Bpar=O_J(1+log N), or O(1) in scalar fallback; set E_J=1 for its decoder. If the only noise input is integer m, let Lnoise=O(1+log(h+1)); it must be supplied and read, with promise (2). If δ is a rational input of total description length Lδ, set Lnoise=Lδ+O(1+log(h+1)); compute the least bounding dyadic scale using at most h+1 exact rational comparisons. Arbitrary real δ is NOT a free computable input. The attack itself is not charged as part of the constructive algorithm.

A safe word/guard size is

    w=C_J[P+Bpar+h+Lnoise+log(n+1)+log(d+1)
             +log(P+1)+log(U+F+2)+1].

This includes scale selection, signed full products, coefficient conversion, counts, decoder rational cross products, table indices, addresses and loop counters. Resource selection and rational-noise certification have conservative cost O((h+1+log(n+1))w²), already bounded by the following ledger because h<=w; add w^4 explicitly. As in GN001, parameter/mask generation streams compact Bpar-bit records and single-bit masks, not Uw- or Fw-padded arrays. Edge tables take O_J(E_J w) retained bits. A safe phase-sum bound is

    T0=O_J(d n²(P+1)w²+(U+F+E_J+n+d+Lnoise)w²+w^4),
    S0=O_J(UBpar+UP+F+n w+E_J w+w^4+Bpar+P+Lnoise).

The ledger pays all tokens, masks and dense/zero slots; rational generation and conversion; arithmetic/Taylor/full products; metadata acquisition and budget selection; rational nearest-edge construction, projection, comparison and inverse; label production; memory isolation/clearing and reusable scratch. A conservative explicit addressed-tape unrolling stores O(T0 w) program/address bits, scans the S0-bit tape per instruction, and has online bitwork O(T0 S0 w), peak O(T0 w+S0) plus actual offline scratch, and offline generation O((T0+S0)w²). No unit-cost random access or real arithmetic oracle is needed. All noncut source-dependent arrays are disabled/cleared before decoder access. Transmitted labels cost J(h+1) bits (endpoint Q is allowed), plus at most b positional bits. Working precision P and public metadata are distinct from that cut capacity.

PURE Boolean/ReLU compilation, if desired, pays actual bitwork depth/width and dense held/gate slots. The logarithmic depth asserted here is only bounded attention/affine/ReLU primitive depth with the paid finite evaluator, not logarithmic Boolean depth or fixed h-bit arithmetic everywhere.

## 7. Scope and relation to earlier noise contracts

GN001 fixes amplitude c/Q with fixed c. Here δ is an independent resource; Q_eff=min(Q,1/δ) replaces Q in capacity and statistical-order depth, with constants uniform in both. This conclusion is obtained by the coarse common attack/IR oracle and rederiving GN geometry's channel error, not by silently letting its fixed c grow. RG/RP's pointwise real-perturbation upper guarantees are compatible but their plateau error is insufficient for the selected shallow upper. FN001's exact folded-encoder erasure uses a finite prequantization-grid attack and concerns a particular fragile encoder; it is neither this universal lower nor a contradiction to the redesigned no-plateau upper. PE1's old canonical post-grid channel has different behavior below a cell; no transfer of (6) to that channel is claimed.

Attribution: local `../prior_art/analog_channel_comparison.md` records Taylor, Mili and Zaghloul (2013), *Analog Error Correction via Tube Packing*, for established scalar stretching/folding, separated curves and nearest-curve reconstruction in an AWGN setting. Geometric noise suppression and dimensional expansion are not claimed new. The bounded-adversarial statistical-depth/finite-cut model here is different; that distinction is not a proof of novelty or absence of closer prior results. The prior-art comparison is not a mathematical dependency.

The upper is IID and arbitrary-initialization only. The lower's IID witnesses transfer to larger source classes containing them, but the upper does not. Internal repeated noise, general Markov sufficiency, unrestricted side statistics, growing J uniform constants, arbitrary real-input computation without a scale certificate, sharp all-depth exponential constants, same-risk-multiplier feasibility, learning reachability and optimal resource work are not established. Finite exact diagnostics and independent LLM review are evidence, not formal proof certification or external peer review.
