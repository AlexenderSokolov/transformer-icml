# FR001 — Complete fixed-interface risk and precision frontier

2026-11-02. Root synthesis candidate; independent composition review pending. Source results AU001 and SF001 have their own accepted independent LLM reviews. This file explicitly states their combined quantifiers and does not replace their proofs.

## 1. The experiment

Fix integers K>=3, M>=64, h>=4 and Q=2^h. The observations are X_1,...,X_(M+2) from a homogeneous unknown second-order table theta, allowing zero transitions. Its pair kernel P has a hidden stationary certificate pi satisfying P^2(s,t)>=beta pi(t) for every pair s,t, including off-support starts, where beta is any number in [0,1]. The target is the next-symbol distribution at the actual terminal pair Y_M. Loss is unconditional expected TV on that same trajectory.

The encoder is the exact finite SRC statistical prefix as retained and extended to h>=4 in NB002. The decoder observes its entire 9K+1 Q-grid master bank and the original exact query/endpoint/mode/flag side information and public parameters, with no raw-history or clean-evaluator reread. The decoder may have arbitrary computation, real simplex outputs and source-independent randomization. Let R_all denote minimax over arbitrary initial pair laws; let R_stat restrict initialization to the hidden stationary certificate. Stationarity does not reveal pi. Allowing the decoder to know the class promise beta does not weaken the lower.

Define

    b=max(beta,1/M),
    W=[1+ln(1+Q/(Mb))]/Q,
    H=max(M^(-1/2),W),
    C_K=2^16 K^(5/2)+2^14 K^3+5320K^5.

## 2. Combined theorem

On this entire domain,

    2^-336 H <= R_stat <= R_all
          <= risk_all(B_NB002) <= min(1,C_K H).       (FR1)

The SAME finite predictor B_NB002 is used for every beta at each supplied public K,M,h. Consequently both original-interface minimax risks satisfy

    R_stat = Theta_K(H),  R_all = Theta_K(H),         (FR2)

uniformly over beta (including arbitrary beta(M)) and all legal Q. This is an all-Q risk theorem, not just a threshold statement. The constants in Theta_K depend on fixed K; no sharp joint-K classification is asserted. Here H<1/4, so the profile has no omitted unit-risk branch.

### Proof

Accepted SF001 establishes the first inequality for the original stationary experiment and arbitrary real randomized decoder. It uses a stationary IID statistical/1-Q floor and the accepted IP002 stationary three-symbol family. Its domain-completion proof retains IP002's minimum and finite Q-domain rather than extrapolating the lower.

For every decoder, the stationary class is a subset of the arbitrary-start class, with identical observed ports and loss. Taking the respective worst cases and then infima yields R_stat<=R_all. No arbitrary-start lower is restricted in the wrong direction.

The actual NB002 finite decoder is admissible, so R_all<=risk_all(B_NB002). Accepted AU001 gives

    risk_all(B_NB002)<=min(1,2^16 L
                      +(2^14K^3+5320K^5)W).

The inherited R011 scale has L<=K^(5/2)/sqrt(M). Each nonnegative term is bounded by its coefficient times H, proving FR1. SF001 proves H<1/4 directly from M>=64, Mb>=1 and Q>=16. All inequalities hold at finite parameters. There is no limit exchange, algorithm selection according to beta, or summing of losses attained by incompatible lower witnesses. This completes FR1–FR2.

## 3. Precision threshold as a corollary

Accepted PF001 already establishes the necessary and sufficient threshold directly, on exactly this interface and domain:

    Q_star=sqrt(M)[1+ln(1+1/(sqrt(M)max(beta,1/M)))],
    h_star=(1/2)log2 M
           +log2[1+ln(1+1/(sqrt(M)max(beta,1/M)))]+O_K(1).

The threshold means: some fixed K-dependent risk multiplier of M^-1/2 is attained at a dyadic Q within a constant factor of Q_star; attaining any chosen fixed multiplier requires Q at least a positive constant times Q_star. The lower constant also depends on that multiplier. It is not a requirement that every successful h equal h_star, and it is not automatic unknown-beta budget learning.

FR1 provides the additional answer when a budget falls below, reaches or exceeds that threshold: the numerical term W and the statistical floor combine by their maximum up to fixed-K constants. If beta is zero or O(1/M), W is of order [1+ln(1+Q)]/Q; for beta sqrt(M) bounded below, Q of order sqrt(M) suffices. Intermediate beta is covered by the same expression. The IID statistical floor prevents arbitrarily high Q from improving the M^-1/2 sample rate.

## 4. What is new in the second-stage proof chain

The preexisting first-stage weak and strong endpoint results did not by themselves settle this profile. The actual additional steps are:

1. SP001/IP001/IP002: stationary rare-active-window lower witnesses, positive-beta survival, all master side fields, one common prior, and the quantization-tube finite-domain cutoff. SP001 and IP001 remain separate valid intermediate results; their limitations are not retroactively erased.
2. IU001: a beta-sensitive stationary terminal-occupation estimate using return times and a nonreversible singular-norm comparison, then a valid arbitrary-start upper with additive burn error.
3. PF001: a finite uniform threshold synthesis from those bounds, separately reviewed before the all-Q result.
4. SF001: stationary all-Q domain completion, retaining both IP002 cutoffs and using the IID statistical floor outside their useful range.
5. AU001: an exact mixture of COMPLETE suffix laws. The residual component is still an ordinary P trajectory from an arbitrary initial law; universal occupation bounds replace the additive burn error by epsilon times a quantization error. The scalar envelope gives the full arbitrary-start upper.
6. FR001: the explicit subset/admissibility composition above. This step is elementary once the preceding proofs are accepted; it is not advertised as a new method.

These are AI-assisted mathematical arguments checked in separate LLM contexts, not formal verification or external peer review. Finite rational/numerical diagnostics corroborate specified identities and inequalities; they do not prove the universal theorems or establish training behavior.

## 5. Costs, comparisons and limitations

No program is changed by FR001. All NB002 and AU001 costs remain: full arithmetic word p=4h+4ceil(log2(M+K+4))+64; six heads; hybrid depth O(Kp^2) and width O(Kp); zero-inclusive dense parameter bits O(K^3p^5); all-token pointwise/QKV work O((M+3)K^3p^6); uncached attention O((M+3)^2(K+p)p^2); all masks, positions, inputs, history/QKV, master/output banks, controller/addresses, explicit movement/holds/clears, actual cache creation, finite evaluator, offline generation/sorting/writes and simultaneous-phase peaks. The separate PURE expansion retains its larger complete accounting. A smaller grid h does not halve total arithmetic words, storage, or time.

The output-only/full-history experiment has a different result: direct counting plus output rounding reaches fixed-K M^-1/2 statistical order with Q of order sqrt(M), even at beta=0. That is not a decoder behind the frozen master bank. FR1 therefore isolates loss induced by this representation; it is not a lower bound for every encoder or every Transformer. Extra pre-cut statistics, altered normalization, nonuniform encoding or other paid representations may evade it. Establishing a broader family theorem requires a separately specified model and proof.

K=2 logarithmic necessity, small M completion, sharp joint-K rates, other source orders/losses, training attainability and architecture-wide depth/width/precision optimality remain outside the theorem. Known waiting-state/harmonic, finite-message quantization and bounded-attention ideas must be credited according to the existing primary-source comparison; no novelty certification is made.
