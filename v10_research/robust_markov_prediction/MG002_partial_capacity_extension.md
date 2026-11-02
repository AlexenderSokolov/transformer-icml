# MG002 — general-Markov partial-capacity robust depth upper

2026-11-02. New candidate, fresh review required. MG001 remains unchanged as the dyadic RG-based construction. This extension uses the now accepted GN001 (root receipt `../intake/GN001_acceptance.json`) and MG001's NEW general-Markov symmetric inverse/occupation argument, subject to MG001 independent acceptance. No all-Q sharp-depth or output-dimensional capacity claim.

## Result

Keep MG001's complete experiment, actual-terminal target, arbitrary unknown homogeneous second-order table, arbitrary initial pair law, paid radius-three causal triple bank, D=RK^3 cut coordinates, exact fixed-position terminal pair, and rational finite post-cut prediction interface. Fix K>=2,R>=2,c>=0,M>=64 and Q=2^h>=2. Let

 B0=4 sqrt(R)(c+2), A0=max{2(c+2),4sqrt(2R)(c+2)},
 Ccap=(2B0)^(R-1), m=bitlength(M+1), chi=2^ceil(log2 m).

All executable choices replace constants by computable integer upper bounds. If

 Q^R>=Ccap sqrt(M),                                         (C)

there exists a robust finite causal architecture with risk O_(K,R,c)(M^-1/2), width O_R(K^3), and bounded-primitive depth

 d=O_(K,R,c)(1+loglog(M+2)+log_+(sqrt(M)/Q)).                 (D)

All bounded stage constants are uniform over Q,M. A sufficient global finite precision is P=4h+c_FA(d+2), enlarged for fixed required guards. The cut and full work precision remain distinct. Exact rational coefficient conversion is the explicitly proved GN001 finite-data extension, not an implicit change to FA001's original dyadic contract. Polynomial nearest-segment decoding and all resource costs are paid. This is a full unknown Markov upper, not the transfer of GN001's IID statistical upper by inclusion.

## Construction and proof

Compute the same causal normalized global triple frequencies x and compand t=g_L(x)/2 with L=ceil(log2 m) as MG001. The source-dependent variables x,t are ideal rails, not decoder side information.

If Q>=sqrt(M), expose t in one coordinate, pad the remaining R-1 with zeros for each triple coordinate, and ignore the padded labels. Entire finite evaluation differs from t by <=1/Q. Attack and Q-floor therefore give |t_hat-t|<=(c+2)/Q after clipping. Clip 2t_hat to [0,g_L(1)] and invert g_L. Its compander-space error is epsilon<=2(c+2)/Q<=A0/sqrt(M). This branch uses only O(L+1) primitive depth and no snake table.

If Q<sqrt(M), set u=(sqrt(M)/Q)^(1/(R-1))>1 and choose N=2^k as the smallest dyadic integer >=u. This choice is executable with integer comparisons: choose smallest integer k>=1 such that Q^2 2^(2k(R-1))>=M. It obeys u<=N<2u. Assumption (C) gives

 2u<=Q/B0,

by raising to R-1 and rearranging. Thus N<=Q/B0, as required by GN001's no-plateau geometry. Apply GN001's shifted recursive map P_R(t), not RG001's plateau map. Compose its bounded stages AFTER the compander at every token. The complete generic finite evaluator has uniform ideal-to-precut error <=1/Q; adding the c/Q fault and floor gives pointwise distance <=sqrt(R)(c+2)/Q from P_R(t). The nearest-segment decoder and GN001 local inverse yield

 |t_hat-t|<=2sqrt(2R)(c+2)/(Q N^(R-1)),
 |clip(2t_hat)-g_L(x)|<=epsilon
       =4sqrt(2R)(c+2)/(Q N^(R-1))<=A0/sqrt(M).

There is no extra mean-floor error: it is already part of the complete pre-cut approximation certificate. There is no additive N^-R plateau term. Feeding the compander output, whose range is only [0,3/4], is legal because the geometric inverse bound is uniform on all t in [0,1]. The scalar decoder does not need t to be an IID empirical mean; the IID sample argument in GN001 is unused.

Apply MG001's symmetric inverse estimate, add-one reconstruction and unconditional terminal occupation to obtain exactly

 risk<=min{1,2^13 Hstat+8K^(5/2)epsilon
                    +Psi(K^5(4epsilon^2+2epsilon/chi))}.

At epsilon<=A0/sqrt(M), the same capped-Psi calculation gives O_(K,R,c)(M^-1/2), including empty rows and artificial positive mass at originally zero coordinates. No stationarity, positive transition lower bound or conditional successor independence is needed. Every beta is covered by its R011 comparator, or beta=0 for the unrestricted homogeneous class.

Because log2 N<1+log2_+(sqrt(M)/Q)/(R-1), the packing uses O_R(1+log_+(sqrt(M)/Q)) stages, while the compander uses O(loglog(M+2)); this proves (D). All coefficients are bounded by four and all retained/intermediate values have fixed bounds via GN001's saturated-doubling implementation. In particular no coefficient proportional to N is hidden in a single stage.

## Finite model and complete cost inheritance

GN001 §5 proves the only new finite-description operation needed here: for signed rational a/b, b>0, convert by floor(2^P a/b), using exact full signed integer division. Its coefficient error is <2^-P, time O((Bpar+P)^2), scratch O(Bpar+P). The rest is precisely the signed FA arithmetic; fixed per-stage constants give the same global recurrence and bootstrap as MG001. Appending exact clipping cannot enlarge error relative to the ideal [0,1] bank. The dyadic compander descriptions form a subclass of these rationals. No exact-lattice assertion is made about the rational snake stages.

Use MG001's ENTIRE paid ledger with Ngrid replaced by this N, E_R=O_R(N^(R-1)) (or E_R=1 in scalar fallback), d from (D), and Bp=O_(K,R)(h+L+log(n+1)) as a safe rational description bound. Rational rather than dyadic conversion has the same displayed U(Bp+P)^2 cost after GN001's explicit extension. Generic work word w, decoder word b, supplied records UBp, converted records UP, every mask bit F, local windows, all-token arrays and decoding, coefficient generation, exact rational edge projections/comparisons/inversion, compander inverse table, add-one normalization, original descriptions/scratch, terminal isolation and offline generation are retained. Dense zero slots and unused padded rails are paid. No reductions in one phase are substituted into a different implementation's phase bound.

The table size is O_R(N^(R-1))=O_R(sqrt(M)/Q) in the snake branch and constant in scalar fallback. This does NOT make decoder arithmetic unit cost; its rational numerator/denominator word length is O_(K,R)(h+L+log(M+1)). Use MG001's conservative addressed tape or its separately costed PURE compilation. Depth (D) is primitive neural depth only, never PURE or bit-machine depth.

## Limits and relation to lower bounds

MG001's necessary alphabet condition has D=RK^3, whereas (C) has scalar packing exponent R. That gap is unchanged. In the common fixed positional-boundary bounded-influence finite-approximation family, the IID witness still yields risk>=gamma/(Q C^d). Hence statistical-order risk requires d>=log_+(gamma sqrt(M)/(A Q))/log C for the relevant fixed risk constant A. This does not close the additive compander-depth term throughout all Q or establish a same-constant frontier. At the minimal sufficient Q=Theta(M^(1/(2R))), this lower and (D) both have order log M. When Q>=sqrt(M), (D) gives O(loglog M); it is not asserted optimal here for every K or larger Q. Existing GD001 necessity has its own explicitly restricted parameter/family scope and is not silently generalized.

RG001 remains a valid predecessor. Its additive plateau term prevents simply choosing a small N near Q≈sqrt(M); GN001's shifted no-pause timing removes exactly that obstacle. Neither result proves learnability, internal reliability, practical total complexity, sharp K rates, unrestricted Transformer necessity or novelty.
