# IC001 — IID statistical-order depth / bounded-grid capacity sandwich

2026-11-02. New post-stage6 research unit; previous freezes untouched. Independent review pending. No novelty, full Markov upper, training, or formal verification claim.

## 1. Experiment and result

Fix J>=2, fixed primitive bounds admitting the causal mean/tent architecture below, fixed local radius and fixed boundary-bit budget b. Let H<=2^b bound the number of possible boundary labels. The boundary label is a function of at most b bits at public source-independent positions (and public independent seeds); it is not an arbitrary nonlocal history statistic. Public seeds/metadata and all programs are independent of the unknown p. Primitive depth d>=1 counts bounded-size attention/affine/ReLU stages, with no growing internal DAG concealed inside a stage. The synthetic terminal initialization is public except for the declared frozen finite boundary label. Historical processing is end-to-end causal; branch dependence on future boundary values is not used in the upper construction. All lower primitive influence bounds hold on every formal history with branch frozen.

Observe an arbitrary initial binary pair and M>=1 generated symbols, with every second-order transition row equal to Bernoulli(p), p in [0,1]. Thus the M generated symbols are IID and independent of the initial pair, and the next-symbol target is p. Risk is worst-case expected absolute parameter error, equivalent to binary TV loss, over p and initial-pair distributions. Exactly J actual precut coordinates in [0,1] are downward quantized at Q=2^h, integer h>=1; unused coordinates may be zero. The decoder sees only these labels, the boundary label and independent public seeds, with no history reread or surviving work state. Decoder outputs are arbitrary real parameters, not a Q-grid restriction.

For lower bounds use the accepted CA/GD/IR ideal primitive family and a uniform precut approximation contract E/Q for fixed E>=1; the finite map itself need not be Lipschitz. A common primitive constant C>=2 gives total ideal replacement influence B_d<=C^d as in IR001. Define c=c(J,b,E)>0 explicitly by

    F=J 2^b, C0=100F, L=F+b,
    P0=128 sqrt(L(C0+1)), K=ceil(2E+6)+1, R0=8 K^J,
    c=min{1/[128 sqrt(C0+1)],1/[32 R0 P0]}.

Then every admitted encoder/decoder satisfies

    R >= max{3/(64 sqrt(M)), 1/[16 H(Q+1)^J], c/(Q C^d)}.    (1)

For every integer 0<=r<=(J-1)h, an explicit finite causal encoder satisfies

    R <= 1/(2 sqrt(M)) + 2/(Q 2^r),
    d <= d0+2r, width <=W_J, precut error <=1/Q,             (2)

where fixed d0,W_J depend only on the chosen bounded primitive syntax and J. Coefficient magnitudes are at most 4; all retained scalar rails lie in [0,1]. A depth budget larger than this may simply allow this shallower architecture (or paid identity padding). The implementation pays growing internal precision and all-token work; this is not fixed-bit arithmetic everywhere.

Here is the precise all-dyadic statistical-order sandwich. For any fixed risk multiplier A>0, existence of an admitted encoder with R<=A/sqrt(M) NECESSARILY implies

    A>=3/64,
    Q^J >= sqrt(M)/[16 H A (3/2)^J],
    d >= max{0, log(c sqrt(M)/(A Q))/log C}.                (3)

Conversely, for EVERY fixed capacity constant κ>0, if Q^J>=κ sqrt(M), let

    r*=min{(J-1)h, max{0, ceil(log2(sqrt(M)/Q))}}.

Then the depth allowance d0+2r* suffices for

    R <= Aκ/sqrt(M),  Aκ=1/2+2 max{1,κ^(-1)},
    d0+2r* <= d0+2+2 log2_+(sqrt(M)/Q).                   (4)

Define log_+(x)=max{0,log(x)}. These are separate necessary and sufficient constants, NOT an iff with the same A or the same numerical depth prefactor. In particular, for any sequence of M,Q, a uniform O(M^-1/2) family requires Q^J=Ω(sqrt(M)) and d=Ω(log_+(sqrt(M)/Q))-O(1); positive constant capacity suffices with d=O(1+log_+(sqrt(M)/Q)). For diverging sqrt(M)/Q the minimal allowed primitive depth has this logarithmic order, up to fixed multiplicative/additive constants, at statistical-order risk. When Q>=sqrt(M), no fold is needed. No assertion rules out smaller constants or improves a bounded-depth endpoint to zero depth.

## 2. Partial-fold geometry, including endpoints

Let T(u)=2 min(u,1-u)=2u-4 ReLU(u-1/2) on [0,1]. For any integer e>=1, T^e is affine on each [v/2^e,(v+1)/2^e], v=0,...,2^e-1, with formula 2^e u-v for even v and v+1-2^e u for odd v. Adjacent formulas agree at their common endpoint. This follows by induction from the two branches of T.

If r=0 retain only time t0=0. If r>0, put m=ceil(r/h), let t_i=ih for 0<=i<m and t_m=r. The retained times are strictly increasing and every increment e_i=t_(i+1)-t_i lies in [1,h]. There are m+1<=J rails y_i=T^(t_i)(x), with floor labels k_i=floor(Q y_i), including possible label Q. Pad with zeros to exactly J coordinates.

Decode by an interval C initially [0,1] and affine y_i=a_i x+b_i, initially a0=1,b0=0. For k_i<Q intersect C with the inverse of the CLOSED coarse interval [k_i/Q,(k_i+1)/Q]. Its length in x is 1/(Q |a_i|). Empty intervals are invalid and may decode to zero. If k_i=Q, impose y_i=1; since a_i is nonzero, at most one x remains. For valid inputs it is the true x: return that singleton directly; subsequent rails cannot alter it. This also covers x=1 and turning points, without inventing branch Q. If any intersection is a singleton, return its point directly on valid inputs.

For a nonsingleton interval and an upcoming increment e<=h, the dyadic Q-bin is contained in the closed branch interval of T^e with index

    v=floor(k_i / 2^(h-e)).

Indeed its endpoints lie between v/2^e and (v+1)/2^e since 2^e divides Q. A bin may touch a branch boundary but cannot straddle its interior; continuity makes the chosen affine formula valid at both closed endpoints. Compose this formula with a_i x+b_i. Thus |a_(i+1)|=2^e |a_i|=2^(t_(i+1)). Orientations can be negative; intersections are taken after sorting inverse endpoints. Closed intervals merely enlarge a true floor-label fiber by boundary points.

After the last label C has length at most 1/(Q2^r). Return its lower endpoint z. For valid x,

    z<=x<=z+1/(Q2^r).                                    (5)

All constraint endpoints have denominators dividing 2^(h+t_i), hence dividing 2^(h+r). Decoder affine coefficients are signed integers of O(h+r) bits, and interval endpoints can be stored on this one fixed dyadic grid. Intersection uses O(J) bounded-length integer operations. No enumeration of all fine cells, unsigned-orientation shortcut, real arithmetic oracle, or hidden large decoder table is required. The case r=0 is ordinary scalar quantization; zero-width intersections and k_i=Q are legitimate exact recovery cases.

## 3. Causal and finite realization

Use FG001's causal zero-logit mean at each history row t>=3 over positions 3,...,t and at a synthetic terminal over 3,...,M+2. Rows 1,2 have public singleton self fallbacks. All masks are public, causal, nonempty, branch-independent, and have density at least 1/4 among each row's potential keys. Each historical row computes its OWN prefix mean; the final mean is never copied backwards. Initial local tables have radius one; the upper ignores boundary bits. Retain each selected time rail while advancing one working rail through r copies of T. Each T is exactly two stages, ReLU(u-1/2) followed by 2u-4 ReLU(u-1/2), retaining u until the update. Signed preactivation lies in [-1/2,1/2]; coefficients <=4 and fixed width O(J) suffice. Optional zero-output heads required by syntax and their masks are paid. Fixed pooling/readout overhead is d0.

Choose fine fractional precision P>=h+r and D=2^P. For a row with m valid bits and count A compute U0=floor(D A/m), and use integer updates U<-2 min(U,D-U). Half-bias and every tent step are exact on this lattice, including U=0,D/2,D. Retained labels are floor(Q U/D), exactly the ideal partial-fold labels of xhat=U0/D. Decode by §2. At terminal x=A/M, and

    0<=x-z<=1/(Q2^r)+2^-P<=2/(Q2^r).                    (6)

Also each ideal/finite rail at fold time t<=r differs by at most 2^t 2^-P<=1/Q. Thus the same actual finite architecture has a DIRECT uniform E=1 precut certificate on all rows/formal histories, without hiding a depth-dependent constant. Nonmonotonic folding creates no problem: decoding reconstructs xhat, not a monotone inverse of each individual rail.

This is included in FA001's signed full-product affine/single-floor evaluator: zero logits give identical positive Taylor weights that cancel exactly in the normalized ratio; integer tent coefficients and half-bias are represented exactly, so its affine output floors cause no further tent error. One may additionally choose P>=max{h+r,4h+c_FA(d+2)} from the accepted GD001 uniform extension. This conservative generic precision is paid; it is not necessary for the direct special-case certificate.

Since E|x-p|<=1/(2 sqrt(M)), (6) proves (2). Set r=r*. If sqrt(M)<=Q then Q2^r>=sqrt(M). Otherwise the unclipped ceiling gives Q2^r>=sqrt(M), unless clipped at (J-1)h, where Q2^r=Q^J. In all cases Q2^r>=min{sqrt(M),Q^J}; the capacity hypothesis yields (4). There is no rounding gap or missing Q=2 case.

## 4. Lower quantifiers and initialization

The finite-alphabet argument of FG001 gives 1/[16 H(Q+1)^J] even with arbitrary history-derived finite labels; the present narrower positional-bit boundary model is used only for the IR depth bound. It fixes seeds and uses a uniform prior on [1/4,3/4]; the epsilon-neighborhoods of at most H(Q+1)^J decoder outputs cannot cover more than half that prior. It does not require deterministic observations or decoder grid outputs.

For the statistical term, fix the initial pair to (0,0) and use the FG001 two-point IID argument on the M generated bits, which gives 3/(64 sqrt(M)). For the influence term, instead use the stationary Bernoulli(p) product initial pair, so all N=M+2 observed bits are IID and IR001 applies literally with D=J and B_d<=C^d. Arbitrary-initialization minimax contains BOTH experiments; their witnesses need not coincide, so taking their maximum is valid. Do not substitute M for N in the IR sample argument. The lower class has no extra source-dependent port, and the boundary positions are public fixed positions conditional on seed. The upper bound holds for every initial pair because it ignores those first two symbols.

If d stages have uniform nonnegative perturbation majorant a I+b_att A where A_tu=1{u<=t}/t, local radius ρ and diameter Δ, and projection Lipschitz G, IR001 establishes B_d=max{1,ρGΔ(a+b_att)^d}<=C^d for C=max{2,max(1,ρGΔ)max(1,a+b_att)}. These are fixed primitive constants, not learned or data-dependent sensitivities. Dense masks use their fixed-density enlarged constants. This supplies (1); Q+1<=3Q/2 for Q>=2 supplies (3). None of these arguments prove a sharp risk function in d with the same exponential base as the construction.

## 5. Fully charged finite resources and PURE distinction

Let n=M+3 and w=C_J(P+log2(n+1)+log2(d+1)+1), with sufficient fixed factor to store signed decoder endpoints/coefficients, counts, addresses and common attention weights; products retain 2w bits. Because P>=h+r, decoder O(h+r)-bit integers fit. Fixed-loop generation of retained times, coefficients and zero padding is paid; no parameter depends on p. A conservative ledger, inherited with total folds r replacing FG001's (J-1)h, is

    T0=O_J(d n^2(P+1) w^2+(d+n)w^2),
    S0=O_J(d n^2+d J^2 w+n J w+w^4).

T0 pays all tokens and layers, dense attention/mask entries including excluded edges and zeros, QKV/affine zero slots, optional dummy heads, fine Taylor work if used, count/division, source acquisition, positions, masks, coefficients and their generation, final labels, O(J) signed interval decoder operations, outputs, and clearing/isolation. S0 pays stored dense masks, parameters, rolling arrays and arithmetic scratch. Direct uniform-mean arithmetic may omit the P+1 Taylor factor; the displayed bound safely retains it. Fixed-length labels use J(h+1) bits because endpoint Q is allowed; the boundary adds at most b bits. Internal P and count guards are distinct from those transmitted bits.

For an explicitly non-unit-cost addressed tape realization, store O(T0 w) program/address bits and scan an S0-bit data tape for each instruction: safe online bitwork is O(T0 S0 w), peak O(T0 w+S0) plus offline scratch, and offline generation O((T0+S0)w^2), with its actual phase scratch included. All noncut history/count/work/token arrays are disabled or cleared before unrestricted decoding. A separate PURE Boolean/ReLU compilation may unroll this finite program with its actual much larger bit-operation depth/width and dense gate-slot costs. It is NOT a fixed-width d0+2r PURE depth theorem. The logarithmic depth comparison concerns bounded attention/affine/ReLU primitives together with fully paid finite evaluation, not a free arithmetic oracle or efficient bit-machine claim.

## 6. Remaining boundaries

This closes the IID statistical-order, all-dyadic-Q, fixed-J capacity/depth ORDER sandwich in the stated common family. It does not give a full unknown second-order Markov upper theorem, exact same-constant feasibility frontier, sharp exponential rate base, minimum internal precision, optimal total work, non-dyadic-Q construction, a lower with arbitrary nonlocal H-valued side information, training reachability, measured emitted-network verification, novelty certification, or external peer review. Lower IID witnesses remain valid necessary obstructions for larger source classes, but upper claims do not transfer merely by inclusion.
