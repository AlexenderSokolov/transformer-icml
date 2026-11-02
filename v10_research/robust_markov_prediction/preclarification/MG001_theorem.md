# MG001 — robust companded packing for general actual-terminal Markov prediction

2026-11-02. Author candidate, independent review required. New construction; frozen predecessors are unchanged. Uses accepted GD001 and RG001, not pending GN001. Independent LLM review is not formal verification or external peer review. No novelty or training claim.

## 1. Experiment, interface, and theorem

Fix K>=2, R>=2, c>=0, M>=64; let n=M+3. Observe X_1,...,X_(M+2) from ANY unknown homogeneous second-order K-letter Markov table theta with arbitrary unknown initial pair law. Write Y_j=(X_(j+1),X_(j+2)), j=0,...,M. Target is theta_(Y_M), not a fixed row, an IID proxy, or a future-conditioned target. Let C_abc count triples among positions 3,...,M+2; x_abc=C_abc/M. In the selected terminal row S=Y_M, J=sum_b C_(S,b) counts departures BEFORE the terminal occurrence. Loss is unconditional expected total variation. Optional all-state two-step minorization beta is unrestricted in [0,1] and unused by the construction.

Choose integer a>=1 with 2^a>=8 sqrt(R)(c+2), dyadic Q=2^h with h>=a+1, and Ngrid=Q/2^a. Let L>=0, chi=2^L. Exactly D=RK^3 coordinates in [0,1] cross an information cut, each after an arbitrary jointly/history-dependent randomized perturbation of absolute value <=c/Q, clipping, and downward Q-quantization. The only exact source-dependent side data are the terminal pair (two fixed-position symbols); query/mode fields, if retained, are fixed public fields or functions of those symbols. No historical work array, count, row mass, timing channel, unquantized rail, or reread survives. Decoder metadata are source independent.

IMPORTANT CONTRACT CHANGE versus SRC/GD's Q-grid output: Q here is the INTERNAL information-cut resolution. The paid post-cut decoder emits a finite exact rational probability vector, NOT a vector constrained to the same Q grid. Imposing that latter restriction would reintroduce an O(1/Q) term and invalidate the present statistical-order claim. An optional separately paid finer output grid can be used with its separate rounding loss; it is not silently identified with Q.

Define

 B=2 sqrt(2R)(c+2) 2^((R-1)a)+(R-1)2^(Ra),
 epsilon=2B/Q^R, delta=4 epsilon^2+2 epsilon/chi,
 Psi(z)=z(1+ln(1/z)) for 0<z<1, Psi(0)=0, Psi(z)=1 for z>=1.

There is a causal bounded-primitive attention/ReLU architecture of width O_(K,R)(1), equivalently O_R(K^3) retained rails up to local fixed-width expansion, depth

 d=O_R(1+L+log Q),

bounded scalar states and coefficients <=4 (constant-factor decompositions allowed), and a fully paid uniform-precision finite evaluator such that for EVERY allowed attack

 risk <= min{1, 2^13 Hstat + 8 K^(5/2) epsilon + Psi(K^5 delta)}.       (MG)

Here Hstat is R011's ORIGINAL full-history add-one scale: with delta_beta=1-beta, A=min(1,sqrt(K^3/(M+1))), G=min(1,sqrt(K^5/(M+1))), and H0=min(1,sqrt(K^4/(M+1))), it is max{A,delta_beta^(M+1)G,delta_beta^(M/2)H0}. For an arbitrary homogeneous table without a declared minorization parameter take beta=0, so Hstat=G. In all cases Hstat<=K^(5/2)/sqrt(M+1). This is a general all-initialization upper theorem, not an IID upper transferred by class inclusion.

Let m=bitlength(M+1), L=ceil(log2 m), so m<=chi<2m. Whenever Q^R>=2B sqrt(M), epsilon<=M^-1/2 and (MG) is O_(K,R,c)(M^-1/2). An integer sufficient choice is h>=max{a+1,ceil((ceil(log2(2B))+ceil(m/2))/R)}. The irrational displayed B may be replaced in all executable choices by any explicit integer upper bound (e.g. replace sqrt(2R) by 2R). At the smallest such dyadic Q, Q=Theta_(R,c)(M^(1/(2R))) and d=O_(K,R,c)(log M), while chi requires only O(loglog M) stages. No K-sharp common-minimax claim is made.

## 2. Causal triple features and complete ideal encoder

Acquire the two preceding symbols by paid singleton heads/local radius-three tables as SRC and GD001. The one-hot triple coordinate is ReLU(e_a(previous2)+e_b(previous1)+e_c(current)-2), with constant-size decomposition if needed. A uniform zero-logit head pools these K^3 local coordinates over observed triple positions 3,...,t at a historical row t and over 3,...,M+2 at the synthetic terminal. Rows 1,2 have public singleton self fallbacks. Every history row has its OWN prefix histogram. No terminal quantity is copied backwards. The terminal's symbol is zero and never included among triples. The two endpoint symbols are exact boundary data, obtained by the paid local copies. These local copies are the declared finite-radius front end, not falsely treated as positive-density statistical heads. The statistical pool has a fixed positive density. All subsequent attention heads, if syntax requires them, have zero output and are paid.

Apply GD001's compander separately to every x coordinate:

 u_0=x, v_0=0;
 u_(j+1)=min(1,4u_j), v_(j+1)=v_j+2^-j ReLU(u_j-1/4),
 g_L(x)=v_L+2^-L u_L.

Retain old u until both updates finish. Retained u in [0,1], v in [0,3/2], g in [0,3/2]; affine temporaries stay in a fixed range. Each j uses a bounded number of actual primitive stages. Let t=g_L(x)/2 in [0,3/4]. Feed t into RG001's explicit dimension-R recursive snake P_R with Ngrid=2^(h-a), and expose its R coordinates. Run the K^3 copies in parallel. All divisions in its ideal formula are dyadic powers; connector parameter lengths involving 2Ngrid^(j-1)+2 occur only in the rational decoder, not as arbitrary-real network coefficients. Width is fixed in M,Q; total primitive stages are O_R(L+h+1), with no growing DAG hidden inside one layer. No extra prepool coarsening from RG's bespoke evaluator is used: this composition instead uses the generic uniform-FA certificate below.

## 3. Composed finite approximation and robust scalar recovery

All per-stage dimensions, coefficient bounds, state bounds, head counts, primitive counts, local radius and statistical mask-density constants are fixed once K,R,c are fixed. GD001's accepted uniform-FA extension therefore gives a single integer c_FA depending only on those bounds and the signed full-product affine/Taylor evaluator, such that

 P>=4h+c_FA(d+2)

ensures every final coordinate differs from its COMPLETE ideal composed encoder by <=1/Q on every formal history and every row. Increase P further to cover the largest dyadic coefficient exponent O_R(h)+L+O(1). Its proof uses a fixed recurrence A^(d+2)(P+1)2^-P<=1/Q; it does NOT substitute growing depth into an unquantified fixed-architecture constant. Signed affine temporaries and full products are guarded; floors need not be one-sided after the snake. Coefficient conversion is exact once P covers all exponents. Parameter descriptions and work precision are paid.

For one triple coordinate, the ideal message is P_R(t). Finite evaluation plus the adversarial fault gives coordinate error <=(c+1)/Q before clipping. Clipping to [0,1] is nonexpansive relative to the ideal curve, and Q-flooring adds <1/Q. Thus q has Euclidean distance <=sqrt(R)(c+2)/Q from P_R(t). Apply RG001's GEOMETRIC nearest-segment decoder, not its special mean/lattice statistical argument. RG's local inverse theorem works for every real t in [0,1] and every q with this distance bound, including arbitrary correlated signed errors and endpoints. It gives

 |t_hat-t| <= 2sqrt(2R)(c+2)/(Q Ngrid^(R-1))+(R-1)/Ngrid^R =B/Q^R.

Specifically nearest projection w' obeys ||w'-P_R(t)||<=2sqrt(R)(c+2)/Q<1/Ngrid; the local subpath inverse includes endpoint plateaus. This is why adding FA error to the fault radius is legitimate. Clip 2 t_hat to [0,g_L(1)], obtaining zhat. Since true g_L(x) is in that interval, |zhat-g_L(x)|<=epsilon. Define xhat=g_L^(-1)(zhat). This quantity is nonnegative and at most one; unlike GD001's one-sided decoder it may exceed x, even when x=0.

## 4. Symmetric inverse estimate — no false zero-purity assumption

The accepted compander geometry gives, for 0<=y<=x<=1,

 x-y <= (2sqrt(x)+1/chi)(g_L(x)-g_L(y)).                 (I)

It follows from slopes 2^j on [4^(-(j+1)),4^-j], j=0,...,L-1, and chi on [0,4^-L]. If xhat<=x, (I) directly bounds the error. If xhat=x+e>x, applying (I) with upper endpoint xhat gives

 e <= (2sqrt(x+e)+1/chi)epsilon
   <=2sqrt(x)epsilon+2sqrt(e)epsilon+epsilon/chi.

The inequality 2sqrt(e)epsilon<=e/2+2epsilon^2 yields

 |xhat-x| <= 4sqrt(x)epsilon+4epsilon^2+2epsilon/chi.    (II)

This includes x=0, L=0 and all breakpoint cases. It is strictly a symmetric error estimate; the quadratic and epsilon/chi leakage terms cannot be deleted using the predecessor's downward-only proof.

## 5. Add-one reconstruction and unconditional occupation

For S=Y_M take its K reconstructed coordinates xhat_b. Decoder outputs EXACT rational probabilities

 qhat_b=(xhat_b+1/M)/(sum_c xhat_c+K/M).

The denominator is always positive. It uses only decoded labels, exact S and public M,K: it does not obtain J, C or exact row mass. True add-one is q_b=(x_b+1/M)/(r+K/M), r=J/M. For arbitrary nonnegative vectors u,v with positive masses A,B, the triangle inequality using v/B versus v/A shows TV(u/A,v/B)<=||u-v||_1/A. Apply this with u=x+1/M, v=xhat+1/M. By (II) and Cauchy–Schwarz,

 Delta=sum_b |xhat_b-x_b| <=4epsilon sqrt(Kr)+K delta,
 TV(qhat,q)<=min(1,Delta/(r+K/M))
 <=4epsilon sqrt(KM)/(sqrt(J+K)) + min(1,MK delta/(J+K)). (III)

This proof covers J=0 and all-off-support rows. Artificial positive mass is not assumed absent. No conditional-IID successor assertion is used.

For completeness, any homogeneous d_state-state chain started anywhere satisfies P(J_m<w)<=d_state^2 w/(m+1). Let b_m(y) be that probability from state y and B_m=max_y b_m(y). Complete visits dominate visits in an l-step suffix, so B_m<=B_l for m>=l. For every deterministic path, sum_(t=0)^m 1{J_t<w}<=d_state w. Taking expectations, then max<=sum over initial states, gives sum_(t=0)^m B_t<=d_state^2 w. Monotonicity yields the claim. Mixtures handle arbitrary initial laws. Thus with d_state=K^2,

 P(J<w)<=min(1,K^4w/(M+1)), integer w>=1.                (UC)

Set a0=K^4/(M+1). Layer-cake with integer thresholds (K>=1) gives

 E min(1,A/(J+K))<=Psi(a0 A),
 E (J+K)^(-1/2)<= integral_0^infinity min(1,a0/s^2) ds
                  =2K^2/sqrt(M+1).

For the latter, P(J+K<t)=0 for t<=K, otherwise use w=ceil(t-K)<=t. Substitution into (III) proves the approximation term 8K^(5/2)epsilon+Psi(K^5 delta), using M/(M+1)<=1 and Psi monotone. Add R011's ORIGINAL add-one risk <=2^13 Hstat. This proves (MG) uniformly over every theta, initialization and allowed attack.

At epsilon<=M^-1/2 and chi>=bitlength(M+1), delta<=4/M+2/(chi sqrt(M)). Psi is increasing, capped, concave and subadditive. Psi(4K^5/M)<=4K^(5/2)/sqrt(M) using Psi(z)<=2sqrt(z). For fixed A=2K^5>=1, if A/(chi sqrt(M))>=1 the cap is <=A/sqrt(M); otherwise

 Psi(A/(chi sqrt(M))) <= A[1+ln chi+(ln M)/2]/(chi sqrt(M))
                       <= C_K/sqrt(M),

since ln chi<=chi, ln M<=chi ln 2, and chi>=1. The operating-point risk follows without a mixing assumption.

## 6. Finite rational decoder and fully paid resources

RG001 supplies a public list of E_R=O_R(Ngrid^(R-1)) moving segments with rational geometric/parameter endpoints of O_R(h) bits; stationary intervals need not be stored as moving segments. The decoder enumerates them, projects by coordinate clamp, compares squared rational distances using integer cross products, breaks ties publicly, and inverts the selected affine segment. All O_R(h)-bit intermediate lengths remain so up to R-dependent constants. This polynomial-in-Q enumeration is explicitly paid, NOT an efficient/logarithmic decoder claim.

Generate g_L's L+2 endpoints, evaluate their rational images, scan its L+1 intervals with a fixed endpoint tie rule, and invert the selected slope exactly. Endpoint data have O(L) bits; recovered xhat has O_R(h+L) rational numerator/denominator length. Summing K such rationals and adding 1/M gives exact output numerator/denominator lengths O_(K,R)(h+L+log(M+1)). K is fixed for these asymptotics; a common denominator may be a product, so do not claim K-independent bit lengths. The output is a genuine finitely represented simplex vector. No real sqrt/log is executed by the decoder; all square roots in constants are replaced by integer upper bounds for setup.

For an explicit conservative ledger let U=O_(K,R)(d+n) count supplied scalar/position/local records including dense zeros, F=O_(K,R)(d n^2) total mask bits, Bp=O_(K,R)(h+L+log(n+1)) maximum supplied description length. Put

 w=C_(K,R)(P+log(n+1)+log(d+1)+log(P+1)+log(U+F+2)+1),
 b=C'_(K,R)(h+L+log(n+1)+1).

Here w is generic encoder/guard precision and b is decoder rational word length, distinct from the h+1 bits per cut label. Original coefficient conversion scratch is O(Bp+P), not falsely bounded by a source-independent constant. A deliberately overcounting Boolean arithmetic instruction budget is

 T0=O_(K,R)(d n^2(P+1)w^2+(U+F)w+w^4
              +U(Bp+P)^2+n K^3(E_R+(L+1)^2+1)b^2),
 S0=O_(K,R)(UBp+UP+F+nK^3 w+w^4+Bp+P
              +K^3 E_R b+nK^3 b+(L+1)b+b^2).

The n factor on decoding safely pays an all-token decoder if the batch syntax demands it; terminal-only decoding is cheaper but not mixed into this ledger. Finite generation of segment tables and inverse breakpoints (O_R(E_R) rational operations and O(L^2) respectively) is included. Total bit addresses fit a constant multiple of max(w,b), since E_R is polynomial in Q for fixed R. Every token/layer, local copy, dense QKV/affine zero slot, excluded mask edge, temporary full product, conversion, coefficient/position generation, all K^3 packed banks, boundary flags, input/output serialization, exact rational normalization and isolation/clearing is paid. Any chosen separate table generator's actual scratch is added to its offline phase peak. No source-dependent offline advice is permitted.

For a non-unit-cost sequential tape realization, let v=C max(w,b,Bp). Store O(T0 v) instruction/address bits and scan the S0-bit tape per bounded-arity instruction. Safe online work is O(T0 S0 v), peak O(T0 v+S0) plus actual generator scratch; safe offline work O((T0+S0)v^2) with its actual phase-sum storage. A separate PURE Boolean/ReLU compilation unrolls these bit operations with its actual larger depth/width and all sparse or dense gate slots paid. The claimed d=O_R(L+h+1) concerns bounded attention/affine/ReLU primitives WITH finite evaluation, not PURE/Boolean depth or total bitwork. All noncut source-dependent arrays are physically inaccessible after the cut.

## 7. Necessary bounds, precise gap, and preserved failures

An IID Bernoulli subfamily belongs to every beta class. At fixed K,R and finite exact boundary alphabet H, the accepted scalar alphabet bound gives risk >=c/[H(Q+1)^D], D=RK^3, even with unrestricted decoder outputs; an independent full-data two-point argument gives Omega(M^-1/2). These witnesses are valid general-class lower bounds. They do NOT prove Q^R>=sqrt(M) necessary: the universal alphabet condition is only (Q+1)^D>=constant sqrt(M). The construction-specific sufficient exponent R and lower exponent D differ; no sharp output-dimensional capacity theorem is claimed.

In the SAME uniformly bounded primitive/fixed-locality/density family, with boundary labels from fixed public positions and a complete uniform E/Q certificate, IR001 gives risk>=c/(Q C^d). Zero attack is admissible, and clipping can be included as a bounded final primitive; finite clipping preserves the <=1/Q certificate. For the IID witness the initial pair is its stationary product law, which is allowed by arbitrary-initialization minimax. At Q=Theta(M^(1/(2R))) and statistical-order target, C^d>=constant M^((R-1)/(2R)), hence d=Omega(log M). Our d=O(log M) matches this order at that named precision schedule. This is NOT an all-Q sharp-depth claim, and fails if arbitrary nonlocal exact boundary information is silently permitted.

Failed/insufficient routes retained explicitly:
* Ordinary signed reconstruction of raw frequencies incurs reciprocal-occupation loss without the square-root companding gain.
* Applying GD001's one-sided finite-floor/zero-purity inequality after robust packing is invalid; (II) includes quadratic and zero-coordinate leakage.
* Applying RG001's special exact-prefix evaluator independently after companding does not certify the composed network. We use the uniform-FA bound on the ENTIRE composition instead.
* Rounding final predictions back to the coarse Q grid adds (K-1)/Q and loses the R-coordinate benefit.
* IID mean estimation alone never establishes the actual-terminal second-order upper. The triple bank and unconditional occupation argument are indispensable here.
* Pending GN001 partial-capacity depth improvements are NOT dependencies. No efficient decoder, minimum internal P, sharp K dependence, unrestricted Transformer lower, internal fault guarantee, learnability or novelty claim is supplied.
