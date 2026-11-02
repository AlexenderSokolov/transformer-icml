# BF001 — Risk frontier after optimizing the bounded local-attention encoder

2026-11-02. Root synthesis and exact-interface inclusion candidate; independent review pending. BA001 and FR001 are separately root accepted after independent LLM review. The theorem is about a declared one-global-block encoder family, not arbitrary Transformers or trained models.

## 1. Exact family and result

Use BA001's model: D scalar coordinates, each a dense weighted ratio over all M keys i=3,...,M+2; each key uses its trailing r-symbol window and public positional metadata; the query is an arbitrary source-independent function of the exact first/last r symbols. The value magnitude is <=1 and every actual weight belongs to fixed [a,b], 0<a<=b<infinity. Position-dependent tables may depend on public K,M,Q,beta but not the unknown source. Each scalar is rounded downward to the Q-grid before arbitrary real randomized decoding. All exact first/last r symbols are available as side information, but no history reread, nonlocal precomputed feature or extra interior statistic is supplied. Shared denominators are allowed: D counts scalar outputs, not physical heads.

For this theorem fix K>=3, D>=9K+1 and r>=3, with

    0<a<=1, b>=6.

Fix M>=64 and dyadic Q=2^h, h>=4. Both encoding and decoding can be optimized within this family, with source-independent common randomness allowed. Let R_F,stat be minimax risk under hidden stationary initialization and R_F,all under arbitrary initialization. The source class is the same all-state D2(beta), beta in [0,1], and loss is unconditional expected TV at the actual terminal pair.

Define

    beta0=max(beta,1/M), s=M^(-1/2),
    W=[1+ln(1+Q/(M beta0))]/Q, H=max(s,W).

Let c_B=1/(8192A) and c_I=1/(256A_I) be BA001's explicit constants for this D,r,a,b, and put

    C_low=max{1280, 1/c_I+512, 1/c_I+24/c_B},
    c_F=1/C_low,
    C_K=2^16 K^(5/2)+2^14 K^3+5320K^5.

Then

    c_F H <= R_F,stat <= R_F,all <= min(1,C_K H).      (BF1)

Therefore, with K,D,r,a,b fixed, the same all-beta/all-Q profile survives optimization of all permitted local feature tables, positional tables, bounded weight tables and arbitrary post-grid decoder. This is stronger than a lower for a single preset SRC encoder. The conclusion ceases to be uniform if D,r or b/a grow; its constants explicitly depend on them.

## 2. Family lower with all domains retained

BA001 is uniform over all admissible encoders, including randomized encoders under one seed-independent prior. It gives a stationary full-history floor

    R_F,stat >= 1/(128sqrt(M+2)) >= s/256,

and, for all beta, R_F,stat>=c_I/Q. For beta<=1/16 it additionally gives

    R_F,stat >= (c_B/Q) ln(1+t/8),
    t=min{Q/(M beta0),M/Q}.

The last theorem actually holds at every Q, but we only use it on Q<=min(M/4,M^(3/4)); thus no rare-suffix tube is extrapolated. These are simultaneous inequalities for the same minimax experiment, not an addition of risks attained by different sources.

The domain-completion comparisons are reproduced rather than silently applying the original-SRC constants of SF001. Write x=Q/(M beta0), so x<=Q.

If beta>1/16, ln(1+x)<=x gives W<=1/Q+16/M<=1/Q+2s. Hence W<=(1/c_I+512)R_F,stat.

If Q>M/4 or Q>M^(3/4), use ln(1+q)<=4q^(1/4), obtained by integrating 1/(1+u)<=u^(-3/4). Then W<=5Q^(-3/4)<=5s. For Q>M/4 the last step uses M>=64; for Q>M^(3/4) it uses M^(-9/16)<=M^(-1/2). Thus W<=1280R_F,stat.

In the remaining domain, beta<=1/16 and Q<=min(M/4,M^(3/4)). Put y=M/Q and t=min(x,y). If x<=y, ln(1+x)=ln(1+t). Otherwise x<=Q<=y^3, giving ln(1+x)<=3ln(1+t). In both cases Bernoulli's inequality gives ln(1+t)<=8ln(1+t/8). Therefore

    W<=1/Q+(24/Q)ln(1+t/8)
      <=(1/c_I+24/c_B)R_F,stat.

Since also s<=256R_F,stat and C_low>=1280, this proves c_F H<=R_F,stat. No original-SRC-only lower is used for the enlarged family.

## 3. Exact finite SRC inclusion and constructive upper

This section checks actual finite outputs, not ideal exponentials. NB002 retains the SRC statistical prefix and proves its legality at every h>=4; its changed suffix never runs the old high-h smoothing stage.

At the terminal synthetic position, the four statistical heads P1,P2,T,0 use exactly keys 3,...,M+2. Their values are local bits from the triple (X_(i-2),X_(i-1),X_i) and the public initial-key flag z_i=1{i=3}. The flagged value F_i=z_i e_(X_2) is a function of the same triple when z_i=1 and is zero otherwise. Thus trailing r=3 windows suffice, and larger r may ignore earlier symbols. The query consists of the actual last pair, contained in the last r symbols. Any exact initial/endpoint/flag side fields in the original cut are functions of the first/last r symbols and public metadata. The family gives at least those fields; its extra boundary symbols may be ignored by the constructive decoder.

The finite public scores are selected from 0,L2,2L2,L3,L2+L3. Write R=2^p for the internal scale. The actual evaluator uses T_0=R and

    T_j=floor(T_(j-1)(R z)/(jR)), j=1,...,8p,
    W_eval(z)=sum_j T_j.

The exact induction already proved in SRC and restated in SM002 gives

    1<=w(z)=W_eval(z)/R<=exp(z)<=6.

At score zero w=1. Every full score is evaluated separately, including L2+L3; no product of rounded weights is substituted. For every retained scalar value coordinate,

    master = floor(Q sum_i w(z_i)value_i / sum_i w(z_i))/Q.

Canceling the common R from exact integer numerator and denominator proves this identity; it does not replace the evaluator by ideal softmax. These public finite tables may depend on K,M,Q but not the source. Values are bits, so they have magnitude <=1, and w in [1,6] is within the declared [a,b]. This verifies the exact BA001 ratio/rounding model.

The complete bank has 9K+1 scalar coordinates: P1 and P2 have 2K each, T has 2K, and head0 has 3K+1. Denominators are shared within each physical head, which BA001 permits. There are four statistical physical heads and two paid singleton local-copy heads. Those copies supply only local triple features and terminal boundary information; they do not grant the decoder all intermediate token outputs or a historical reread.

If D>9K+1, append scalar coordinates with constant value zero and weight one. They disclose nothing and satisfy the model. The extra exact first/last r symbols may be ignored. Thus the actual finite SRC bank is an admissible encoder in this larger family, and the NB002 decoder is admissible behind it.

Accepted FR001 gives its arbitrary-start risk <=min(1,C_K H), with no runtime beta access. Optimizing over all admissible encoders/decoders can only lower this risk. The stationary class is a subset of the arbitrary-start class under the same allowed encoder/decoder family, proving R_F,stat<=R_F,all. Together with Section 2 this proves BF1.

The source inclusion relies on NB002 Section 2 (coarse-grid prefix), original SRC fact fef8372728290b45 Sections 2 and 4 (complete masks/local copies/finite evaluator), and SM002 Section 2 (exact actual-weight and master representation). It is not inferred merely from a similarity between ideal attention formulas.

## 4. Quantifiers, costs and interpretation

The lower permits arbitrary real source-independent tables and arbitrary decoding, making it stronger as an information obstruction; it does not assert that every such table has a cheap computable implementation. A matching *existential* upper uses the concrete finite SRC/NB002 program and all its costs. It does not bound the cost of every encoder in the family.

For that constructive member the retained word-size parameter is p=4h+4ceil(log2(M+K+4))+64, and complete coefficients/products/guards use <=128p bits. All six heads, masks, positions, input/local copies, exact endpoint acquisition, finite evaluator, full historical/QKV arrays, all-token pointwise work, zero-inclusive dense coefficients, controller/addresses, holds/copies/clears, ordered output, actual caches, offline generation/sorting/writes, simultaneous-phase peak and separate PURE expansion remain charged exactly as in NB002/FR001. New proof comparisons introduce no runtime computation. Extra D padding coordinates are only needed if the family is defined with exactly D outputs; generating/returning those zeros adds their actual D grid words and trivial writes, constant in M,Q at fixed D. Alternatively the family may allow at most D coordinates, in which case no padding is executed. Obtaining larger boundary windows S is a paid input-copy operation, O(r log K) packed bits and O(r log K) bitwork; these are constants in M,Q at fixed K,r and are included rather than supplied as a cost-free new historical channel. Neither addition changes the fixed-parameter upper rate.

This does not establish all-architecture, arbitrary-depth, variable-context, growing-width or growing-score impossibility. In particular global preprocessing before the cut, query-selective hard masks, unbounded values, length-growing effective logits or unbounded exact side information change the family. Arbitrary depth/computation *after* the quantized cut is already allowed and cannot avoid this lower. Training that produces any source-independent tables in the family is covered as an encoder choice, but this is not a training-convergence theorem; source-specific information learned elsewhere is not silently allowed as a hidden input.

The mechanism of dense bounded-attention dilution is established prior art. The additional obligation here is a distributional complete-message tube count and its common-prior prediction loss. The targeted primary comparison records Hahn's corrected supplement and Chiang–Cholak's normalization/logit escape examples; no novelty certification is made.
