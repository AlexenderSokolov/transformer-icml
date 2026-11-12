# One public source alignment from a scalar position: actual bounded PreLN compilation

2026-11-12. A complete local alignment submodule, not a full predictor or simultaneous all-row predecessor construction. Unlike the earlier external pairwise predecessor-bias interface, this module starts from an additive scalar position and compiles its own source gate with actual PreLN/ReLU blocks.

## 1. Interface, public target and resources

N>=2 raw signs X_i occupy rows1,...,N; append row n=N+1 with synthetic sign X_n=+1. A SINGLE source index j in {1,...,N} is chosen PUBLICLY when configuring the module; j may be N-1 or N. The network is not discovering an unknown source index and is not receiving a data-dependent source marker.

Initial width14 paired state has seven pairs:

    (X_i,-X_i), (p_i,-p_i), (1,-1), (0,0), (0,0), (0,0), (0,0),
    p_i=i/N, including p_n=(N+1)/N<=3/2.

This is additive token embedding plus public scalar-position/anchor embedding. There is NO initial one-hot marker, pairwise positional score bias, local mask, or global statistic. The source index enters only through bounded layer coefficients t_-=(j-1/2)/N and t_+=(j+1/2)/N. A contract requiring one parameter set independent of both N and j, or forbidding this scalar positional input, is not covered. The coefficients have O(log N) rational description length, not a fixed N-independent finite alphabet.

Every block is the actual residual PreLN form with full width14 LayerNorm epsilon=1, gain1, shift0 both before attention and before the FFN. All attention Q,K are zero. There is exactly ONE nonzero full self-inclusive causal uniform attention read, after the source gate has been constructed. Other blocks set attention output zero. ReLU FFNs have fixed hidden widths and finite layerwise matrix/bias bounds independent of N,j and requested error eta. Total depth is O(log N+log(1/eta)); the sum of squared parameter norms over all layers grows with depth and is NOT bounded independently of it.

## 2. Threshold registers from normalized scalar position

Use the fourth and fifth pairs as scalar registers x,y. A zero-attention block with a linear-as-two-ReLUs FFN writes

    x=(p_i-t_-)/(4 d_i^0), y=(t_+-p_i)/(4 d_i^0),
    (d_i^0)²=1+(2+p_i²)/7.

This is a legal linear map of the normalized position and anchor coordinates. It does not divide by an unnormalized state or use a comparison oracle. The source grid lies halfway between the thresholds. Thus x,y are both positive exactly when i=j; every other row has one negative register. No threshold is zero, and both magnitudes are at least

    delta0=1/[8N sqrt(45/28)],

since (d_i^0)²<=1+(2+9/4)/7=45/28. Both magnitudes are <1. The initial token sign affects neither divisor nor the registers, since its square is one.

## 3. Actual two-register PreLN amplification

Keep the token, position and anchor pairs unchanged. At each amplifier block, write paired FFN increments phi(x/d), phi(y/d), where

    phi(t)=t-2 ReLU(t-.1)+2 ReLU(-t-.1),
    d²=C_i+(x²+y²)/7, C_i=1+(2+p_i²)/7.

This uses eight ReLU units and fixed coefficients. On |x|,|y|<=1,

    9/7<=C_i<=45/28,
    1<d<=dmax1=sqrt(53/28)<sqrt2.

As in the audited amplifier, signs are preserved and the box is invariant: the coordinate map is nondecreasing, is nonnegative at zero, and decreases at magnitude1. For magnitudes below .1, growth is at least factor1+1/dmax1. One extra step takes [.1,.1*dmax1] above .1*dmax1 because min(.1/dmax1,.2-.1*dmax1)>.1*dmax1-.1. Therefore O(log N) steps bring both signed magnitudes into the invariant saturation region.

There F(w)=w+.2*1-w/d. Its Jacobian eigenvalues are 1-1/d and 1-C_i/d³. Both are nonnegative and at most

    q1=1-(9/7)/dmax1³<1.

It contracts to equal magnitudes b_i=.2 sqrt(C_i/(1-.08/7)). Their PHYSICAL amplitudes depend on public position, but their normalized amplitudes are exactly .2. No continuous position lane is reset and no position-dependent inverse normalization is computed. The contraction acts on the scalar register vector (x,y), whose initial distance to its fixed point is at most sqrt2. Its full paired-state Euclidean error is sqrt2 times the register error and hence at most 2*q1^L1. Choose L1=ceil(log(eta_gate/2)/log(q1)), with eta_gate=.001. Then the FULL width14 paired-state error is <=eta_gate, independent of N. This paired-state factor is included before using the global LayerNorm Lipschitz bound below.

## 4. A fixed ReLU plateau gate writes exactly one token

After this amplification, normalized token magnitude is in a fixed interval near [0.784,0.877]. Define the FFN input functional

    u=LN(token)+10 LN(x)+20 LN(y).

For a source row i=j, the two register signs are positive, so u lies in the plateau centered at 6+.83 if X_j=+1, and at 6-.83 if X_j=-1. With eta_gate=.001, the input perturbation is at most sqrt(501)*.001<.023, and both source cases lie within plateau half-width .14. Every non-source sign pattern has u far outside either plateau (its register contribution is +/-2 or -6, rather than +6).

For center c define the actual four-ReLU trapezoid

    B_c(u)=10[(u-c+.24)_+ -(u-c+.14)_+
              -(u-c-.14)_+ +(u-c-.24)_+].

It is one on |u-c|<=.14, zero on |u-c|>=.24. A single eight-hidden-unit FFN writes into the initially empty sixth pair

    z=B_(6+.83)(u)-B_(6-.83)(u), and its negative.

On every raw word this gives z_i=1{i=j}X_i EXACTLY in real arithmetic, including zero at the synthetic terminal. The gate does not subtract any unknown continuous register. Token, position and threshold lanes are retained. The plateau argument is why approximate threshold amplification suffices for exact seed isolation.

## 5. One full-prefix read and a second actual amplifier

The nonzero attention head selects normalized payload coordinate z_i/d_i. All non-source values are exactly zero. At the selected source this value is c_j X_j, where c_j is a deterministic public positive scale: all other energy terms depend only on p_j and the threshold dynamics, while token and payload signs enter squared. In particular

    c_j>=1/sqrt(57/28).

Write the uniform read into the initially empty seventh pair. Its scalar is

    v_i=0 for i<j; v_i=c_j X_j/i for i>=j.

No near-hard attention is used; the target weight is only1/i. The sentinel receives the same attenuated message. Other lanes, including the seeded payload, remain untouched.

Apply the same phi amplifier to ONLY v_i. Its nonscratch energy C_i is now fixed throughout these blocks and satisfies 1<C_i<=57/28. For |v_i|<=1, its divisor obeys d<=dmax2=sqrt(61/28)<1.5. The zero registers at i<j remain EXACTLY zero; the others preserve sign, grow from at least

    delta1=1/[(N+1)sqrt(57/28)],

and enter [.1*dmax2,1] after O(log N) steps. The same boundary argument works since dmax2<1.5. On the saturation interval, the scalar map contracts with derivative at most q2=1-1/dmax2³<1 to

    b_i=.2 sqrt(C_i/(1-.04/7)).

At the fixed point the normalized seventh coordinate is exactly .2 X_j. After O(log(1/eta)) further blocks, the ordinary bounded linear readout 5*LN(seventh coordinate) differs from X_j by at most eta at EVERY i>=j. It is zero before j. This is a bit-alignment readout, not an uncharged probability/logit head.

## 6. Bounds, errors and what the module delivers

All seven pairs remain bounded: token magnitude1, position<=1.5, anchor1, thresholds<=1, payload<=1, broadcast<=1. Thus every clean physical row norm is at most sqrt(16.5). Both normalizations in each standard block have positive epsilon1 and bounded gain. The threshold and broadcast FFNs use constant-sized matrices; the plateau gate has larger but fixed weights10,20 and fixed biases. Initial threshold coefficients t_+<=1.25 and t_->=0 are bounded. The uniform attention value and output projections have fixed norms. No total key-array energy budget or nonzero positional QK is used.

For generic full-vector residual/evaluation perturbations, use a common-domain Lipschitz tube through the O(log N+log(1/eta)) sites. Sufficient precision is O(log N+log(1/eta)) fractional bits with a sufficiently large constant. Initial position/threshold coefficient rounding must be smaller than the O(1/N) classification margin and be charged separately. This is not a constant-noise tolerance theorem: adversarial noise larger than the attenuated 1/N signal can erase the broadcast. Common-mode errors are not exactly reset, and the finite tube accounts for their accumulation.

The gate/compiler and broadcast are joined end to end; this is not an isolated exact-real encoding. Nevertheless it aligns ONE PUBLICLY CHOSEN SOURCE j across its causal future. It does NOT simultaneously give every row i its distinct predecessor i-1, does not compute a transition statistic, and does not by itself solve parameter estimation or next-token risk. Running a separate copy for every source would increase width or depth by a factor depending on N. A constant number of selected sources could be processed with additional charged lanes, but changing width changes LayerNorm constants and is not asserted by reusing these numerical formulas.

This module is a potential terminal-local alignment component when j=N-1 or N is allowed as a public configuration. It is not a hidden response to an unknown content-addressed target. Its precise scope should be retained when composing it with future statistic/output modules.

## 7. Explicit layerwise norm ledger and diagnostic

A literal two-layer FFN implementation can use the following Frobenius bounds (biases are separate): threshold initialization W1<=.801, W2=sqrt8; two-register amplifier W1=sqrt8, W2=sqrt40, hidden bias norm .2; marker gate W1=sqrt(8*501), W2=40, with fixed hidden biases given by centers 5.17 and 6.83 shifted by +/- .14,.24; one-register amplifier W1=2, W2=sqrt20, hidden bias norm sqrt2/10. The lone attention value projection has norm1 and paired output projection sqrt2; final normalized bit readout has norm5. All LN gain vectors are the fixed all-ones width14 vector (norm sqrt14), shift vectors zero, and epsilon1. These are finite per-layer budgets, some larger than a small prescribed cap. They do not imply a fixed sum of norms across growing depth.

`check.py` executes the joined scalar-position compiler, all-row marker gate, one uniform head and broadcast amplifier. Seed1907 is used for three random words per configuration, alongside all-plus and all-minus words. It covers N=2,3,8,32,128,512 and public targets at the first, middle, penultimate and final raw positions (deduplicated), 105 cases total. It checks every row, including zeros before the source and the synthetic terminal, with 27,540 gate/alignment assertions plus all intermediate broadcast-state norm assertions. Maximum observed gate and final alignment discrepancies were 2.23e-16 at requested eta=1e-5; this floating arithmetic observation does not imply exact finite-depth real convergence. Maximum observed state norm was2.983, below the analytical sqrt16.5 envelope. It is not a risk experiment or an adversarial-error certificate. Near-grid-boundary margins and coefficient precision are paid analytically, not randomized away.
