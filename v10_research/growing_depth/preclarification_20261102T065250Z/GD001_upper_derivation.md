# GD001 upper derivation — bounded-score growing-depth companding

2026-11-02. Author candidate, independent review pending. This is a NEW encoder and finite-arithmetic certificate. Accepted CA001/FA001/CF001/SB001/TR001/BS001/BC001 files are unchanged. No novelty or universal-Transformer claim.

## 1. Experiment and theorem

Fix K>=2, M>=64, N=M+2, n=M+3, Q=2^h>=16 and integer L>=0; put κ=2^L. Use SB001's pair-chain experiment, arbitrary initialization, terminal pair S=(X_(N-1),X_N), J previous occurrences and C_c successor counts. Write Hstat for the accepted ORIGINAL R011/SB001 comparator scale, Hstat<=K^(5/2)/sqrt(M+1). Let Ψ(x)=min-cap of x(1+ln(1/x)) on (0,1), with Ψ(0)=0 and Ψ(x)=1 for x>=1.

There is a causal fixed-width (depending on K, not M) ideal affine/ReLU architecture, with uniform zero-score dense attention, O(L+1) actual primitive sequential affine/ReLU stages, bounded coefficients <=4 and bounded states <=2, and a fully paid downward finite implementation, satisfying

 R <= min{1, 2^13 Hstat + Ψ(K^5/(M+1))
       + [12K² sqrt(K(K+1)) + K-1]/Q
       + Ψ(3K^5(K+1)/(κQ))}.                         (U1)

The implementation is uniformly within 1/Q of its ideal pre-cut bank. This does not follow by substituting growing L into FA001's fixed-architecture constant; it is certified below directly.

Take m=bitlength(M+1), h=max(4,ceil(m/2)), L=ceil(log2 m), where L is computed by integer bitlength of m-1. Then sqrt(M+1)<=Q<=2sqrt(M+1), m<=κ<2m, L=O(loglog M), and (U1) is O_K(M^-1/2), uniformly in initialization and every β. β is unused.

## 2. Compander geometry and real architecture

On [0,1], T(x)=min(1,4x)=4x-ReLU(4x-1). Define g_0(x)=x and

 g_(L+1)(x)=.5 g_L(T(x))+ReLU(x-.25).

Equivalent sequential implementation: u_0=x,v_0=0; at j=0,...,L-1,

 u_(j+1)=T(u_j),  v_(j+1)=v_j+2^-j ReLU(u_j-.25),
 g_L(x)=v_L+2^-L u_L.

The simultaneous update must retain old u until both updates finish. Each stage uses a bounded fixed number of affine/ReLU primitives, bounded fan-in and width; stages are NOT hidden in one free per-layer DAG. Counting all affine/ReLU depths changes L only by a fixed factor. Inter-stage identities retain needed rails. Coefficients 2^-j are public finite dyadics of paid O(j+1) bits. No coefficients exceed 4 in magnitude. States u in [0,1], v in [0,1.5] and output g_L in [0,1.5]; exact maximum g_L(1)=1.5-.5*2^-L. A constant-factor intermediate expansion for evaluating 4u has range <=4, still uniform; the <=2 bound above applies to retained stage states, not every affine temporary.

Induction on L gives a strictly increasing concave piecewise-linear g_L: slope 2^j on [4^(-(j+1)),4^-j], j=0,...,L-1, and slope κ on [0,4^-L]. At breakpoints either one-sided slope may be used. Consequently, for 0<=y<=x<=1,

 x-y <= (2sqrt(x)+1/κ)[g_L(x)-g_L(y)].                 (U2)

Indeed the inverse derivative at g_L(t) is 2^-j<=2sqrt(t) outside the bottom segment, and 1/κ on the bottom segment; integrate from y to x, bounding t by x. Formula (U2) is boundary-safe and needs no differentiability at finitely many breakpoints.

Start from paid radius-three local one-hot triple features as SB001, with two paid singleton copy heads or a paid finite local table. One uniform zero-logit statistical head pools every observed triple position 3,...,min(t,N); declared short-row self fallbacks handle t=1,2. Terminal mask is 3,...,N. This is CA001's public density>=1/3 mask. At EVERY historical row the histogram is its own causal prefix histogram, not terminal counts copied backwards. All K³ coordinates are retained. Apply g_L coordinatewise to the histogram, divide by 2, then downward Q-grid cut. Subsequent attention stages, if a layered attention syntax requires them, may have zero output and bounded dummy heads; they must be charged but convey no additional information. The compander's depth counts actual positionwise nonlinear compositions, not growing attention score range: every statistical logit is zero.

The decoder receives ONLY the complete quantized K³ bank, exact terminal pair S (a K²-valued boundary label), and public metadata. It applies the known inverse g_L to twice each represented coordinate, selects S's K-coordinate block, normalizes if its sum is positive, else returns uniform, and performs ordered Q-simplex rounding. No counts, exact denominator, unquantized row mass, other historical features or outputs survive the cut. Decoder inverse and normalization are paid post-cut operations.

## 3. Explicit downward arithmetic and purity

Choose fine-grid denominator D_f=2^P, P=h+L+4, so D_f=16κQ. All histogram numerators A and denominators m_t are accumulated exactly; write initial X=floor(D_f A/m_t), representing xhat=X/D_f<=x. Uniform finite softmax can alternatively use any identical positive finite weight on every edge: it cancels exactly in the ratio. There is no exp/log oracle.

Run U_0=X and V_0=0 as integers. For j=0,...,L-1 use

 R_j=max(0,U_j-D_f/4),
 V_(j+1)=V_j+floor(R_j/2^j),
 U_(j+1)=min(D_f,4U_j).

Then W=V_L+floor(U_L/2^L) represents a downward approximation to g_L(xhat). All T updates are EXACT on the fine grid. Each of L+1 positive dyadic-term floors loses <1/D_f, hence

 0<=g_L(x)-W/D_f <= [κ+L+1]/D_f <=3κ/D_f<=3/(16Q).    (U3)

Here g_L is κ-Lipschitz and x-xhat<1/D_f. L+1<=2^L for L>=1 and the stated 3κ bound also covers L=0. Terms and signs are nonnegative. If x=0 then X=U=V=W=0 EXACTLY; there is no artificial mass leakage.

Emit Z=floor(QW/(2D_f)), representing z=Z/Q in [0,1]. Exact integer arithmetic ensures

 0<=g_L(x)-2z < 2/Q+3/(16Q) <3/Q.                    (U4)

Thus y=g_L^-1(2z) is well-defined in [0,x], and

 0<=x-y <= (6sqrt(x)+3/κ)/Q.                         (U5)

No upward error occurs. This eliminates a quadratic inverse-error term that a symmetric rounding certificate would require. In particular all-zero decoded blocks need no exact J=0 test. The actual pre-cut value W/(2D_f) differs from ideal g_L(x)/2 by <=3/(32Q), uniformly every formal history and row, independently of L. This supplies a CA-type E/Q contract, with explicit E independent of depth.

## 4. Deterministic normalization and expectation

For J>=1 the selected true histogram coordinates x_c=C_c/M sum to r=J/M. Let y_c be inverse-decoded coordinates, and e=sum(x_c-y_c). By Cauchy-Schwarz and (U5),

 e <= 6sqrt(Kr)/Q+3K/(κQ).

If e<r, the normalized y has TV distance <=e/r from x/r, by the two-term normalization triangle inequality. If e=r, every y is zero and any simplex fallback has TV<=1=e/r. Therefore the bound INCLUDING zero-surviving-mass is

 TV(decoded,C/J)<=min(1,6sqrt(K)/(Qsqrt(r))+3K/(κQr))
 <=6sqrt(K(K+1)M)/(Qsqrt(J+K))
       +min(1,3K(K+1)M/[κQ(J+K)]).

We used J+K<=(K+1)J. Add-one comparator q_c=(C_c+1)/(J+K) differs from C/J by <=K/(J+K), and final ordered simplex rounding costs <=(K-1)/Q. For J=0 the same resulting bound holds because K/(J+K)=1 covers any discrepancy.

The accepted universal arbitrary-start occupation inequality is

 P(J<w)<=min(1,K^4 w/(M+1)), integer w>=1.

It implies both E min(1,a/(J+K))<=Ψ(K^4a/(M+1)) and

 E (J+K)^(-1/2)<=2K²/sqrt(M+1).                       (U6)

For completeness, put Z=J+K and a0=K^4/(M+1). For t<=K, P(Z<t)=0; for t>K, the event is J<ceil(t-K), whose integer threshold is <=t because K>=1. Thus P(Z<t)<=min(1,a0t). Layer cake yields E Z^-1/2 = integral_0^infinity P(Z<s^-2) ds <= integral_0^infinity min(1,a0/s²) ds=2sqrt(a0). Strict/non-strict equality at atoms changes only a null set of s. Apply the reciprocal occupation bound to the two remaining terms and √(M/(M+1))<=1 to obtain U1.

At the integer operating point, κ>=m, Ψ(C/(κQ))<=Ψ(C/(mQ))<=3C/Q by SB001's elementary bitlength estimate; Ψ(K^5/(M+1))<=2K^(5/2)/sqrt(M+1). This proves the asserted statistical-scale risk.

## 5. Finite paid ledger and distinct notions of depth

The inverse is an exact finite procedure: enumerate endpoints 0,4^-L,...,4^-1,1; evaluate g_L at them using the finite dyadic formula; scan all L+1 intervals, choose the interval containing 2Z/Q with fixed tie rule, and solve its affine formula of slope 2^j. All breakpoints/intercepts have O(L) denominator exponent, all inverse outputs have common dyadic denominator dividing 2^(h+2L+O(1)); a larger uniform denominator is allowed. No real square root, log, or exact arbitrary-real primitive is executed. Subsequent sums, zero tests and normalized ordered simplex rounding use exact integer arithmetic with a safe positive fallback denominator.

Let ell=ceil(log2(n+K+2)), b=128(h+ell+L+1). Persistent scalar words use b bits, full products use 2b bits and guarded temporaries <=4b+4 bits. Counts <=n, initial dividend D_f A<=D_f n, fine states <=2D_f, inverse common-denominator integers and Q-times decoding dividends all fit. Addresses and instructions have O(b) bits. Dense parameter records for O(L+1) fixed-width stages cost O((L+1)K^6 b) bits; local and triple tables and all mask writes are paid. Breakpoint generation can evaluate the L-stage formula separately at each of L+2 points, O((L+1)^2 b²) bit gates, included below.

For the attention-free compander-stage implementation, a conservative fixed-loop Boolean instruction budget and simultaneous live data bound are

 T0=O([n²K^6+n(L+1)K^6+(L+1)^2] b²),
 S0=O(n²+nK³b+(L+1)K^6b+b²).

If literal dummy dense heads are evaluated at all compander stages, replace the n²K^6 term in T0 by n²(L+1)K^6 and add any explicitly duplicated layer masks to S0; the uniform-FA companion gives a full alternative ledger for that syntax. These cover dense Q/K/V/local matrices including zeros; three head scans including masked edges; exact histograms; all-token companders, inverse scans and normalizations; complete K³ bank; inputs, masks, positions, outputs, controllers, breakpoint tables, parameter generation, allocation/clearing and arithmetic scratch. A rolling two-stage compander buffer is used; no growing-width concatenation stores all intermediate stages. Released counts and intermediate rails are physically inaccessible to the decoder. Initial local windows can be acquired by the same paid copies as SB001, not an uncharged source-dependent feature port.

A fully paid addressed sequential evaluator stores O(T0 b) instruction/address bits, scans the S0-bit tape for each bounded-arity elementary instruction, and has

 forward bitwork O(T0 S0 b), forward peak O(T0 b+S0),
 offline bitwork O((T0+S0)b²), offline peak O(T0 b+S0+b²).

Alternatively a separate bounded-fan-in ReLU Boolean PURE compilation with T=T0+b and S'=S0+b has depth O(T), width O(S'), addressed sparse coefficient bits O(bTS'), dense coefficient bits O(bT(S')²), dense offline/forward bitwork O(b²T(S')²), and rolling numeric storage O(bS'). Full phase peaks ADD stored chosen coefficients/program, input/public masks/constants if separately retained, output, rolling arrays, and generation scratch. These alternatives cannot be mixed to claim smaller resources.

The O(loglog M) claim concerns fixed-width ideal attention/positionwise primitive depth (and its explicitly specified finite evaluator stages), NOT Boolean circuit depth or PURE compiled depth, which is much larger. Work precision P=h+L+4 and b=O(log M+log K) at the operating point are paid. Exact bit gadget rounding is discontinuous; lower bounds for finite evaluators require the established uniform E/Q transfer, not a false Lipschitz claim about rounding itself.

## 6. Dependencies and scope

Directly read CA001 v3 (architecture, masks and late influence), FA001 v3 (fixed-architecture caveat and paid semantics), SB001 v2 (local triple bank, occupation and inherited add-one risk), and their acceptance receipts, together with CF001/TR001/BS001/BC001 acceptance scope. This note proves its new geometry, one-sided arithmetic, normalization, fractional occupation and ledger, while inheriting the stated occupation and original statistical comparator results. The intended lower is for a uniformly bounded primitive family with fixed width/head counts/locality and fixed number of primitive operations per counted layer. Fixed per-layer DAG size and bounds are essential: otherwise arbitrary amplification could be hidden in one layer.
