# GN001 — robust IID statistical-order depth/capacity sandwich without plateaus

2026-11-02. New candidate, independent review pending. No frozen artifact edited. RP001, IC001, IR001 and GD001 are accepted dependencies; RG001 was accepted by root during this derivation (receipt `../intake/RG001_acceptance.json`); its geometry is compatible background, but the new timing and conversion needed here are proved independently. The geometry and finite conversion needed here are proved below. No novelty, general Markov upper, training, formal verification or efficient-decoder claim.

## 1. Experiment and theorem

Fix J>=2 and c>=0. Use IC001's bounded-size attention/affine/ReLU primitive family, with enough fixed width depending on J for the construction below. Bounds on fan-ins, coefficients, heads, local radius and mask density are independent of M,Q,d. Observe an arbitrary initial pair followed by M>=1 IID Bernoulli(p) generated symbols; next-symbol target is p. Minimax risk is expected absolute parameter error (binary TV), supremized over p, initializations, and all history-dependent randomized one-shot coordinatewise precut perturbations of magnitude <=c/Q. Clip after perturbation and floor at Q=2^h, h>=1. Exactly J coordinates in [0,1] are exposed; unused coordinates are zero. Only these labels, public source-independent metadata/seeds, and an optional boundary label consisting of at most b bits at public fixed positions survive. No history reread, timing port or residual work state is allowed. All ideal frozen-branch bounds hold on every formal history; the actual finite encoder has uniform ideal-to-precut discrepancy <=1/Q. More generally the lower permits any fixed E/Q. Rational descriptions in this upper are explicitly evaluated by the finite extension in §5.

Write H=2^b. Accepted IC001/IR001 constants C>=2 and gamma=gamma(J,b,E)>0 give, by choosing the admissible zero attack,

 R_rob >= max{3/(64 sqrt(M)), 1/[16 H(Q+1)^J], gamma/(Q C^d)}.       (1)

Let B=4 sqrt(J)(c+2), K=2 sqrt(2J)(c+2). For every dyadic N=2^k>=2 satisfying N<=Q/B, the construction below gives

 R_rob <= 1/(2sqrt(M)) + K/[Q N^(J-1)],
 d <= a_J+b_J log2 N, width <=W_J,                              (2)

where fixed constants depend only on the admitted primitive implementation and J. There is also a depth-a_J scalar-mean construction with

 R_rob <=1/(2sqrt(M))+(c+2)/Q.                                  (3)

Set kappa_*=(2B)^(J-1). For EVERY M>=1 and dyadic Q>=2 with Q^J>=kappa_* sqrt(M), these constructions give

 R_rob <= A_*/sqrt(M),  A_*=1/2+max{c+2,K},
 d <= A_J+B_J log2_+(sqrt(M)/Q).                                (4)

Indeed use (3) when Q>=sqrt(M). Otherwise choose N to be the least power of two >=(sqrt(M)/Q)^(1/(J-1)); then N>=2, N<2(sqrt(M)/Q)^(1/(J-1))<=Q/B. Formula (2) proves (4). These are sufficient large capacity constants, not a claim for every positive capacity constant at the same risk multiplier.

Conversely existence of any admitted robust encoder with risk <=A/sqrt(M) necessarily implies

 A>=3/64,
 Q^J>=sqrt(M)/[16 H A (3/2)^J],
 d>=max{0,log(gamma sqrt(M)/(AQ))/log C}.                         (5)

Thus this is an honest necessary/sufficient constant sandwich: robust statistical order requires capacity Q^J=Omega(sqrt(M)) and logarithmic depth when sqrt(M)/Q diverges, while a sufficiently large fixed capacity ratio suffices with depth O_J(1+log_+(sqrt(M)/Q)). Necessary and sufficient constants are DIFFERENT. We do not assert same-constant iff or a sharp exponential base.

## 2. Shifted no-plateau snake formula

Let T(x)=2x-4relu(x-1/2) on [0,1], clip(x)=relu(x)-relu(x-1). For arguments up to 1+1/(4N), use T_ext(x)=2x-4relu(x-1/2)+4relu(x-1), then ordinary T for subsequent iterations. Denote this k-fold periodic tent by V_k(x)=T^(k-1)(T_ext(x)); on [0,1] it is T^k. Define P_1(t)=t. For j=2,...,J let L=N^(j-1), eta=1/(2L+2), and compute

 A=T^(k+1)(t), Bphase=T^k(T_ext(t+1/(4N))),
 z=min(1-A,L relu(1/2-Bphase)), s=A/2+z,
 S_j(t)=t-s/N,
 v=V_k(t+eta/(2N)),
 u_j(t)=clip((v-eta/2)/(1-eta)),
 P_j(t)=(P_(j-1)(u_j(t)), S_j(t)).                              (6)

Do not use an ordinary tent on the first shifted input when it exceeds 1. Both shifts stay in T_ext's stated range. The apparent amplification L is implemented by exactly (j-1)k saturated doublings x<-min(1,2x), followed by min with 1-A. This is identical since 0<=1-A<=1. All intermediate magnitudes are bounded by an absolute constant, and every scalar coefficient has magnitude <=4. In particular 1/(1-eta)<=6/5 for N>=2. Min and clipping have fixed-size affine/ReLU implementations. Sequentially computing each level and retaining S_j uses O(J) rails and O_J(k+1) primitive stages, NOT a growing hidden DAG inside one stage. Shift and rescaling coefficients are rational with O_J(log N) description bits; they are generally NOT dyadic.

For t=(i+r)/N, i=0,...,N-1, r in [0,1], the RP phase computation gives

 S_j=i/N for r<=1-eta;
 S_j=i/N+(r-1+eta)/(N eta) for r>=1-eta.                        (7)

For completeness, A=tri(r), Bphase=tri(r+1/4), where tri has period one, height one, slopes +/-2. For r<=1/2 the positive part vanishes and s=r. For r>=1/2 its positive part is min(A,1-A), so s=min(r,(2L+1)(1-r)); these expressions cross at 1-eta. This proves (7), including boundaries by continuity.

On an even row V_k at phase r+eta/2 rises from eta/2, so u_j=r/(1-eta) until r=1-eta and then equals 1. On an odd row it descends from 1-eta/2, so u_j=1-r/(1-eta) until r=1-eta and then equals 0. The turn in the shifted tent occurs inside the clipped final portion; its minimum or maximum there remains beyond the clipping threshold. This applies to the final row using T_ext across 1. Adjacent row formulas agree at common endpoints. Thus movement starts immediately at every row start. The only flat portion of u_j coincides with strictly moving S_j. There are NO stationary intervals of P_j.

## 3. Full geometry and local inverse

The edge list is defined inductively. P_1 is [0,1]. At level j append N copies of the lower list in planes x_j=i/N, forward for even i and reversed for odd i, each followed by an outer-axis connector of length 1/N to plane (i+1)/N. There is no copy in plane 1. Since N is even, endpoints are (0,...,0) and (0,...,0,1), distance one. Edge count satisfies E_1=1, E_j=N E_(j-1)+N, so E_J=O_J(N^(J-1)). Formula (6) traces this list in order without pauses.

Every edge is axis aligned, has length >=1/N, and has grid vertices. Inductively the path is simple. Different copies have outer separation >=1/N. Nonadjacent connector intervals have outer separation >=1/N; adjacent connectors are anchored at opposite lower endpoints, distance one. Connector versus nonadjacent copy has outer separation >=1/N. In either adjacent plane its anchor is an endpoint of the lower path; any lower edge not incident to that endpoint is separated from the anchor by >=1/N. To justify the last claim without circularity: all lower vertices are on the N-grid, and a grid vertex not on an axis-aligned grid segment is at least 1/N from it; simplicity excludes an endpoint's membership in any nonincident edge. Incident lower edge and connector are perpendicular. Inside a copy use induction. Thus distinct nonincident edges are separated by >=1/N, while incident edges are perpendicular and meet only at their shared endpoint. There are no nonlocal vertex contacts.

Every moving edge speed is >=N^(j-1): inherited speed >=N^(j-2) is multiplied by N/(1-eta)>=N, and outer connector speed is 1/eta=2N^(j-1)+2. No stationary intervals and simplicity imply P_j is injective, including t=0,1. If two image points have Euclidean distance delta<1/N, their edges are equal or incident; the connecting subpath then has length <=sqrt(2)delta. On equal edges it is exactly delta. On incident perpendicular edges this follows from a+b<=sqrt(2)sqrt(a²+b²). Nonincident separation rules out any other local itinerary, including choices at vertices. Integrating the inverse speed along this subpath yields

 |t-t'|<=sqrt(2) ||P_J(t)-P_J(t')||_2/N^(J-1).                 (8)

For delta=0 injectivity gives equality of parameters. In contrast to plateau constructions, there is NO additive N^-J term.

## 4. Rational decoder and noise

Let x be the exact terminal empirical mean, part of the ideal causal architecture. Its ideal bank is P_J(x). The actual finite bank a lies in [0,1]^J and satisfies ||a-P_J(x)||_infinity<=1/Q. Attack, clipping and final flooring produce q with

 ||q-P_J(x)||_2<=sqrt(J)(c+2)/Q=:r0.

Clipping cannot increase distance to an ideal [0,1] point. Enumerate E_J edges, project q onto each by clamping its varying coordinate, compare squared rational distances, choose the minimum with public fixed tie order, and call the projection w'. The true curve point is an available competitor, hence ||w'-P_J(x)||<=2r0<=1/(2N)<1/N. Invert the selected affine parameterization. Equation (8) gives

 |xhat-x|<=2sqrt(2J)(c+2)/(Q N^(J-1)).                         (9)

This is pointwise for every attack and history. E|x-p|<=1/(2sqrt(M)) proves (2). No separate mean-rounding term is added: §5 already includes all initial-mean and later arithmetic error in the uniform precut tube.

The edge table includes rational geometric and parameter endpoints. Build it recursively: a child's interval [a,b] becomes [(i+(1-eta)a)/N,(i+(1-eta)b)/N] in even rows, and [(i+(1-eta)(1-b))/N,(i+(1-eta)(1-a))/N] in odd rows. Append [(i+1-eta)/N,(i+1)/N] for each connector. Base interval is [0,1]. All intervals have positive duration and concatenate without gaps. Each endpoint uses at most J factors of N and (2L+2), giving O_J(log N) rational numerator/denominator length. Projecting Q-grid q and inverting requires O_J(log N+h) bits; squared distances can be compared by exact cross multiplication. List construction, nearest-edge search and inversion cost O_J(E_J) bounded-word arithmetic operations, O_J(E_J(log N+h)) stored bits. Rational inverse results are not required to lie on the transmitted Q-grid.

## 5. Explicit finite rational-data extension, not exact arithmetic assertion

FA001 v3 and accepted GD001 literally supply DYADIC parameter descriptions. We extend only their input-description conversion to finite rationals a/b, b>0, with signed numerator and positive denominator of total length <=Bpar. Convert by the exact signed integer quotient floor(2^P a/b), including negative-floor correction. This costs O((Bpar+P)^2) bitwork and O(Bpar+P) scratch and gives coefficient error <2^-P. All subsequent signed full-product affine, ReLU, Taylor and normalized-attention operations are EXACTLY FA001's finite operations, not exact evaluation of the rational network. FA's one-step error proof uses only this conversion bound and bounded ideal coefficients, not dyadic ideality. Therefore every estimate and the GD uniform induction carries over verbatim after this proved conversion replacement. This is an explicitly enlarged finite-data class; it does not rewrite accepted FA/GD scope.

The ideal initial scalar is obtained by causal zero-logit mean over positions 3,...,t at each history t>=3, and over all M generated bits at the synthetic terminal. Positions 1,2 use public singleton fallbacks; masks are public, causal, branch-independent, nonempty and density >=1/4. Initial pair is ignored. All historical tokens compute their own prefixes, never a final mean copied backwards. Zero logits are admissible; optional dummy zero-output heads are paid. The synthetic initialization is public and has no hidden history statistic. Apply the recursive bounded primitives to every row's own mean. Ideal outputs and all retained rails remain bounded on every formal history.

Fixed per-stage bounds give computable alpha,beta and A>=max(2,alpha+beta+1), independent of N,M,h,d. With c_FA>=4 chosen so A(c_FA+5)2^(1-c_FA)<=1, set

 P=4h+c_FA(d+2).

The GD induction gives maximum stage/readout discrepancy <=A^(d+2)(P+1)2^-P<=1/Q, closes its own discrepancy<=1 bootstrap, and includes coefficient conversion, initial attention mean floor and all intervening arithmetic. Append exact lattice clipping of finite output coordinates to [0,1]; because ideal outputs already belong there this cannot worsen the bound. Include corresponding fixed ideal identity clip stages in d or increase its fixed overhead. This proves uniform E=1 on every row/formal history. NO claim that shifted rational tent stages are lattice exact is made. The lower uses the bounded ideal primitive family with this fixed E tube; it does not require finite-map Lipschitzness or equality of ideal and finite floor labels.

For (3), use the same mean and generic evaluator, retain one scalar and pad J−1 zeros. Its finite error <=1/Q, fault <=c/Q and final floor <1/Q give pointwise error <=(c+2)/Q. This covers every Q>=2 including cases admitting no separated snake.

## 6. Paid finite resources and necessity scope

Let n=M+3, U=O_J(d n²) supplied scalar records in a fully expanded sequential public layout and F=O_J(d n²+n log(n+1)) public mask/metadata bits; all zero and excluded slots count. Here Bpar=O_J(log N+1) for the snake (O(1) for scalar fallback); use E_J=1 for the scalar fallback decoder. Put

 w=C_J[P+Bpar+h+log(n+1)+log(d+1)+log(P+1)+log(U+F+2)+1].

This safely includes rational decoder cross products, full affine products, counts, counters, table indices and address guards, rather than identifying transmitted h with working precision. Exact rational coefficient/table generation has O_J((U+F+E_J)w²) conservative bitwork. It streams compact Bpar-bit rational parameter records and single-bit masks, with O_J(w) reusable generator scratch; recursive edge tables retain O_J(E_J w) bits (including child tables). No Uw- or Fw-padded parameter/mask array is retained. These generation records and scratch are included in the displayed phase-sum peak. Supplied-data acquisition pays UBpar+F, conversion pays U(Bpar+P)^2. A conservative arithmetic instruction ledger is

 T0=O_J(d n²(P+1)w²+(U+F+E_J+n+d)w²+w^4),
 S0=O_J(UBpar+UP+F+n w+E_J w+w^4+Bpar+P).

T0 includes all tokens, dense heads/edges and affine zero slots, Taylor work, source acquisition, masks, parameter generation/conversion, repeated tape movement, rational edge generation/projection/comparison/inverse, final labels, and clearing/isolation. S0 is a safe sum of coexisting arrays, not rolling activations alone. A fully explicit addressed unrolling alternative stores O(T0 w) program/address bits and scans S0 bits per instruction: online bitwork O(T0 S0 w), peak O(T0 w+S0) plus actual offline scratch, offline generation O((T0+S0)w²). Thus no unit-cost random access or real arithmetic oracle is used. This deliberately loose alternative alone suffices; no optimal machine complexity is asserted. Decoder costs are polynomial in N, NOT logarithmic.

All noncut source-dependent arrays are disabled/cleared before decoder access. Labels cost J(h+1) bits since endpoint Q is allowed, plus at most b boundary bits. Public programs are independent of p. PURE Boolean/ReLU unrolling pays its actual bitwork depth/width and held/dense slots; logarithmic depth here is ONLY bounded attention/affine/ReLU primitive depth, not PURE depth or h-bit-everywhere arithmetic.

For lower (1), robust supremum includes zero attack. Apply IC001 to the same fixed positional-bit boundary model and fixed E ideal-to-actual contract; use its coefficient/range bounds enlarged once to include (6). Statistical witness fixes initial pair; depth witness uses stationary product initial pair, both permitted by arbitrary-initialization minimax. Finite alphabet bound allows only H(Q+1)^J labels. No nonlocal H-valued history side statistic is substituted for positional bits. No source-dependent synthetic initialization is smuggled into the bounded-influence theorem.

## 7. Relationship and limits

The failure motivating this change is real: RP/RG-style initial clipping creates vertex plateaus and an additive N^-J inverse error; selecting N from a shallow statistical target can leave that error too large when Q is close to sqrt(M). The shift in (6) eliminates that obstacle rather than declaring old folds robust. Scalar geometric packing/folding is known (local Uss et al. 2025 prior-art record); no novelty claim follows from this explicit bounded-primitive realization. This unit concerns IID upper bounds only; IID lower witnesses transfer to larger source classes, upper bounds do not. Internal faults, learning reachability, optimal total work, non-dyadic Q, unrestricted side information, and exact same-constant feasibility remain outside the result. Independent LLM review and finite rational tests are not formal verification or external peer review.
