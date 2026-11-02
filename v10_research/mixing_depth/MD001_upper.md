# MD001 upper — mixing-dependent primitive depth, both alphabets and starts

2026-11-02. New author candidate; independent review and root acceptance required. Accepted GD001 and BIF001 files and stage6 freeze are immutable.

Use exactly GD001's uniform bounded-primitive causal family and finite evaluator, with capacity for the complete K³ triple histogram, retained output count D>=K³, trailing locality r>=3, fixed width sufficient for its rolling coordinatewise compander, coefficients up to four and its stated bounded temporaries. D alone is NOT sufficient capacity. All statistical attention logits are zero, so their weight ratio κ is ONE. Write **γ=2^L** for compander gain, never for attention weight ratio. The actual primitive depth is d<=c_arch(L+1). Local tables, density>=1/3 causal masks and synthetic terminal query are exactly GD001; its initial terminal state depends only on public data and the fixed finite boundary label. Every frozen branch obeys the ideal contract on all formal histories.

Let s=M^-1/2, z=γQ, e_K=max(β,1/M) for K>=3 and e_2=max(sqrt(β),1/M), t=M e_K, G(z,t)=1+ln(1+z/t). For M>=64 and dyadic Q>=16, this SAME finite GD001 program satisfies, for all initial laws,

    R <= min{1,C_K [s+1/Q+G(z,t)/z]}.                 (U1)

Constants are independent of M,β,L,Q. This upper alone is not an all-Q minimax frontier.

## 1. Imported GD001 facts and larger-alphabet transfer

The accepted GD001 three proofs give monotone concave g_L, downward finite output Z, and inverse y=g_L^-1(2Z/Q), with

    0<=g_L(x)-2Z/Q<3/Q,  0<=y<=x,
    x-y <=(6sqrt(x)+3/γ)/Q.

These statements hold for the SAME generic FA evaluator with P>=max{4h+c(d+2),h+L+4}; they do not require equality of ideal and finite floor labels. Zero inputs stay zero exactly. The complete K³ bank is cut before block selection, inverse, normalization and final grid rounding. No exact count, denominator or history survives the cut.

For J>0, r=J/M, GD normalization gives error at most

    A_J+min(1,B_J),
    A_J=6sqrt(K(K+1)M)/(Q sqrt(J+K)),
    B_J=3K(K+1)M/[z(J+K)].

For J=0 its add-one comparison pays K/(J+K)=1. Universal actual-terminal occupation yields E A_J<=12K²sqrt(K(K+1))/Q. Add-one risk is <=8192K^(5/2)/sqrt(M+1); its empirical correction has expectation <=Psi(K^5/(M+1))<=2K^(5/2)s. Final rounding costs (K-1)/Q.

To bound the reciprocal term, use AU001's general occupation lemmas, not its predictor. Set a=3K(K+1)M/z. For β>=1/M, the half-suffix stationary/residual decomposition bounds E min(1,a/(J+K)) by

    [6K³(K+1)/z][17+ln(1+160z/[K(K+1)Mβ])]
      + ε Psi(6K^5(K+1)/z),
    ε=(1-β)^floor(M/4).

As in accepted SB001 §7/AU001 §4, the first term is <=144K³(K+1)G(z,t)/z and the second <=30K^5(K+1)G(z,t)/z. At β=1 residual mass is zero. For β<1/M universal occupation bounds the term by Psi(3K^5(K+1)/z)<=3K^5(K+1)G(z,1)/z. This proves U1 for K>=3 (and also the weaker β-cutoff upper for K=2), uniformly over all supports and initial states.

## 2. NEW binary purity-clipping lemma for this same program

Put u(x)=min(γx,sqrt(x)). On the bottom segment x<=4^-L, g_L(x)=γx. On segment 4^-(j+1)<=x<=4^-j, 0<=j<L,

    g_L(x)=2^j x+2^(-j-1)-2^(-L-1).

Writing x=t4^-j, t∈[1/4,1], shows

    u(x)<=g_L(x)<=1.5u(x).                           (U2)

Indeed outside the bottom segment u=sqrt(x); the ratio is (t+1/2-2^(j-L-1))/sqrt(t), with intercept between 1/4 and 1/2. Its lower bound one follows from t+1/4>=sqrt(t); its upper bound 1.5 follows from t+1/2<=1.5sqrt(t) on [1/4,1]. L=0 is simply g=x=u. Also u(cy)>=sqrt(c)u(y) whenever c>=1 and cy<=1, directly for both entries of the minimum.

The composed finite scalar stages T(U)=min(D_f,4U), their nonnegative accumulator additions, dyadic floors, and final coarse cut are nondecreasing in the input; the complete evaluated scalar map is downward. Individual subtractive affine primitives need not be nondecreasing in every intermediate rail. The same public precision and program is used for both coordinates. Hence if a selected two-coordinate bank is positive and x0 is a largest true coordinate, then its coarse Z0 is largest and Z0>=1. With y0=g^-1(2Z0/Q),

    g(x0)<g(y0)+3/Q<=2.5g(y0)<=3.75u(y0).

Because u(x0)<=g(x0) and u(x0)>=sqrt(x0/y0)u(y0), we obtain x0<(3.75)^2 y0<16y0. Here y0>0, so no zero division occurs.

Let p be the empirical exit fraction in this row, for ANY chosen successor called exit, and v its inverse-decoded normalized fraction. If p<=1/2 the nonexit coordinate is a largest coordinate, and

    v<=x_exit/y_nonexit<=16p/(1-p)<=32p.

Thus |v-p|<=32p. If p>1/2, unit loss is <=2p<=32p. Together with GD normalization, on a positive bank and J>0,

    |v-p|<=min(32p,A_J+B_J)<=A_J+min(32p,B_J),
    A_J=6sqrt(6M)/(Q sqrt(J+2)), B_J=18M/[z(J+2)].

Take the actual true exit weights q=(a,b,e,t_exit), exactly BIF001's orientation on (00,01,10,11). The 1-Lipschitz truncation gives

    |v-q|<=A_J+32 min(q,A0/(J+2))+33|p-q|,
    A0=18M/(32z).                                    (U3)

Neither the exit labels nor q are program inputs; they are proof choices. The empirical statistical cost is E[1_{J>0}|p-q|]<=S_add+B0, where accepted BIF gives S_add<=8192sqrt(32)/sqrt(M+1) and B0<=2sqrt(32)/sqrt(M+1).

## 3. NEW all-zero bank control

If both coarse coordinates vanish, g(x_i)<3/Q, so u(x_i)<3/Q. Since u is a minimum, either γx_i<3/Q or sqrt(x_i)<3/Q; consequently

    x_i<=3/z+9/Q²,   J/M<=6/z+18/Q².

A strict version follows from the strict initial error. Universal actual-terminal occupation at integer threshold ceil(M(6/z+18/Q²)) bounds this event, including J=0, by

    P(zero bank)<=16(6/z+18/Q²+1/M).                  (U4)

A positive threshold is always available; ceilings add at most one. This is valid for every initial law, and does not assert an exact test for J=0. Charge loss at most one there and final binary rounding 1/Q. Since Q>=16, Q^-2<=Q^-1; in the fixed sqrt(M) band the zero-bank terms are also O(s).

## 4. All binary support/cutoff cases

For full-support positive-β kernels with βM²>=1, BIF001 §3's actual-q occupation theorem gives

    E min(q_(Y_M),A0/(J+2))
      <=4s+(16672A0/M)[1+ln(1+1/(sqrt(β)A0))].

Multiplying by 32 and substituting A0 gives 128s+(300096/z)[1+ln(1+(16/9)z/t)]. Since 1+ln(1+(16/9)x)<=2[1+ln(1+x)], this is at most 128s+600192G(z,t)/z.

For singleton stationary support, the source has an absorbing diagonal by BIF001 §2. BAI003 v2 §6.2, with actual weights including q_absorb=0, gives

    E min(q_(Y_M),A0/(J+2))<=256max(A0,1)/M+16/(M+2).

After multiplication by 32 this is <=4608/z+8704/M. Thus arbitrary transient starts are covered, not merely stationary starts.

For 0<=β<M^-2, apply the general-alphabet transfer of §1 with K=2 and β replaced by zero, which is permissible because no minorization is needed for the universal occupation bound. Then e_2=1/M and t=1, giving U1 directly. At β=M^-2 the strong case applies. For β>0 BIF's support classification exhausts full support or singleton support; no nonergodic support case is omitted.

Combining U3-U4, E A_J<=48sqrt(6)/Q, and the accepted empirical cost proves U1 for K=2; C_2=2^23 is a conservative common constant. The new proof uses BIF's all-start weighted occupation, not BU's stationary-only lemma. It modifies neither GD encoder nor decoder.

## 5. Depth selection and paid finite scope

In a fixed legal grid band c_-sqrt(M)<=Q<=c_+sqrt(M), put f_K=1+ln(1+Q/[Me_K]). Choose a public dyadic gain f_K<=γ<2f_K (γ=2^ceil(log2 f_K)). Since γ>=1,

    G(γQ,t)/γ<=(f_K+ln γ)/γ<=2.

(The bound follows f_K<=γ and lnγ<=γ.) Hence U1 gives risk <=C_K(1+3/c_-)s and d=O(1+ln f_K). No feasibility for arbitrarily tiny target multipliers is claimed.

This is a promise-based public budget specification, not a free runtime log/sqrt operation or learning β. For a supplied rational β, selection can instead use paid bitlength/rational comparisons; binary sqrt comparisons can be squared on nonnegative rationals. The rational input length and setup work must be charged separately. Alternatively the theorem is indexed by public integer L. It makes no claim that its minimal bit-cost schedule has been optimized.

All GD001 uniform-FA and upper ledgers are inherited with this L. For the generic encoder use P>=max{4h+c(d+2),h+L+4} and its own w_enc=O_fixed(P+log(n+1)+log(d+1)+log(P+1)+log(U+F+2)), where U,F are actual total supplied records and public bits across all stages. Original descriptions of maximum length Bp separately pay conversion scratch O(Bp+P). The upper note's b_d=128(h+ell+L+1) is a bespoke-evaluator/decoder word bound only, NOT a bound on an arbitrarily enlarged generic-encoder precision P. Conversion from the generic exported Q-grid bank to decoder words pays its actual O(nK³(w_enc+b_d)) writes; add both data/code volumes if simultaneously retained. In the decoder ledger below b means b_d. Pay full products and guarded temporaries, every mask/table/dense zero coefficient, causal all-token attention and compander stage, rolling buffers, inverse breakpoint generation O((L+1)²b²), exact dyadic inverse/normalization and ordered rounding, terminal isolation/copies/clears, public data/parameter descriptions and conversion, instructions/addresses and simultaneous phase sums. The uniform FA encoder ledger is ADDED to its decoder ledger when that implementation is selected; the bespoke evaluator is a separate alternative. At this schedule L=O(loglog M), P,b=O(log M) for fixed K, but all O(L+1) stages and supplied records remain paid. Primitive depth is not Boolean/PURE depth, and arithmetic precision is not grid h. No hidden per-layer growing DAG or growing-width rail concatenation is permitted.
