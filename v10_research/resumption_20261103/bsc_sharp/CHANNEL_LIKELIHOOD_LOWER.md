# CHANNEL-LIKELIHOOD-LOWER — candidate sharp BSC length order

2026-11-03. New author derivation; independent review and root acceptance pending. Local only. No accepted source, manuscript, or public repository changed.

## Finding

For the original eight-triple-counts plus actual endpoint-pairs observation (`r=2`), an arbitrary fixed-length, law-independent full-corrupted-path encoder followed by fresh independent BSC noise of fixed crossover `0<η<1/2` needs **R=Ωη(log M)** bits to achieve uniformly bounded same-map adaptation factor. This matches the already conditional repetition `Oη(log M)` upper bound when the restored exact-bit FOT002 procedure is admitted. The stronger lower follows from transporting only the *clean loss penalty* by a channel likelihood ratio, not multiplying the entire old lower bound by channel overlap.

The lower is against arbitrary codes, not just repetition. It applies to stationary first-order witnesses satisfying the original all-state pair certificate `β=1/M`, and thus to the arbitrary-initial-pair class by inclusion. Loss is unconditional **unsquared TV**, not squared loss.

## 1. Experiment and exact quantifiers

Set `N=M+1`, so there are `N+1=M+2` raw symbols `X_0,...,X_N`, `N` ordinary edges, and `M=N−1` triple departures. The baseline `Z_r(w)` comprises all eight triple counts and the actual first/last `r` raw symbols. Both final symbols are protected. Legal attacks are fixed source-independent Markov kernels on all words that change at most integer `k∈{0,...,N−1}` of the first `N−1` raw coordinates, on every input and every outcome.

At fixed `(N,r,R,η)`, choose **one** encoder `E` and decoder `D`, ignorant of source table, source initial law, true budget `k`, and attack kernel. They may know the experiment parameters and supplied certificate. After attack output `w`, `E` scans the full `w` and emits an element of `{0,1}^R`. The channel independently flips each emitted bit with probability `η`, conditionally on the entire pre-channel experiment. The decoder receives `Z_r(w)` and all `R` channel outputs and returns a predictive distribution for the actual terminal state. Its private coins are allowed. No uncharged path-dependent side information, encoder state, channel-noise seed, variable length, feedback, or timing channel is supplied.

A shared random seed is permitted only if it is independent of the source/path/attack and is already free baseline randomization in the same model. Conditional on that seed the channel must still be fresh BSC. The attack used below ignores this seed. Path-dependent encoder randomness revealed to the decoder would constitute extra information and is NOT covered by calling it a seed.

For a fixed rule `(E,D)` define

`Γ_N(E,D)=sup_{k,Q,K} R_{Q,K}(E,D)/g_N(k)`,
`g_N(k)=max(N^(−1/2),k/N)`.

The supremum may be restricted to stationary first-order sources satisfying certificate `1/(N−1)`; the bounds below already hold for that restriction. Take `inf_{E,D}` only AFTER this supremum. No source-specific choice of rule, interchange of minimax order, or attainment is needed. The same rule supplies the clean identity-attack risk at `k=0` and the null attacked risk at the constructed `k`.

## 2. Channel likelihood comparison

Let `W_R(v|h)` be the product-BSC pmf and

`κ=κ_R=((1−η)/η)^R` (with `κ_0=1`).

For every pair `h,h'` and every output `v`,

`W_R(v|h) ≤ κ W_R(v|h')`.

Indeed each coordinate ratio belongs to `{1,η/(1−η),(1−η)/η}`. For ANY input mixtures `p,q`, including unrelated private encoder randomization distributions,

`sum_h p(h)W_R(v|h) ≤ κ sum_h' q(h')W_R(v|h')`.    (6)

One proof bounds every left summand by every right channel pmf and integrates both mixtures. Thus arbitrary encoder outputs on two different words need not agree.

Suppose words `y,w` have the same baseline observation and end in `00`. Let `P_y,P_w` be their encoded/noisy-output laws. Let `d_a(b)` be TV loss of action `b` against the first-order next-symbol target with zero-to-one probability `a`; define `d_β` similarly. For every action,

`d_β(b)+d_a(b)≥a−β` for `a≥β`.

Run the SAME decoder at the common baseline and integrate first under `P_w`, including decoder private coins. Since `d_a≥0`, (6) gives

`E_w d_β(D) ≥ a−β−E_w d_a(D) ≥ a−β−κ E_y d_a(D)`.    (7)

For free independent shared seed `U`, prove (6)–(7) conditional on each `U=u`, using the same `u` at both words, then integrate its common law. This is valid because our attack and coupling do not condition or select `U`. In the pair-state formulation both targets are on `{00,01}` and their TV distance is exactly `a−β`, so the target has not been changed by passing to next-symbol notation.

**Key distinction:** the first term is integrated under a probability law and remains `a−β`; only the nonnegative clean-target loss pays `κ`. Applying overlap to the entire risk loses this feature.

## 3. Precisely imported, reviewed combinatorial/probabilistic lemma

Dependency: `../recovered_science/first_order_positional_probe/triple_access/FOT001_candidate.md`, entire proof, and its `review/independent_analytic_review.md`. That review independently checked mixture counting, endpoint conditioning, coupling, relocation, strict budget, null masses, all certificate rows, and horizon conversion. This new proof imports its channel-free structural lemma, stated fully here; it does not assume the desired channel lower bound as a premise.

Put `c=2^(−16)`, `A=2^12`, `x=ck`, `t=x/N`, `u0=floor(x/4)`, `T=floor(N/8)`, `I=[At,1/4]`, and `L=log(1/(4At))=log(4N/k)`. Assume

- `N≥64`, `2≤r≤k/128`, `k≤N/8`, `x≥4096`;
- `At<1/4`, `N/k²≤A c²/2^20=2^(−40)`.

For stationary binary `Q_a`, `a∈I`, use `T_a(0,1)=a`, `T_a(1,0)=t`. Let `F={y_0y_1=11,y_(N−1)y_N=00}`; `U(y)` is ordinary `01` count, `D(y)` the ordinary cross-edge count, and `j(y)=J00(y)` the pair-departure occupation of state `00` (not triple count `H000`). There is a measurable deterministic relocation `C_r` on a set `B` of words whose pair path has an interior `11` before an interior `00`. On

`G=B∩{U≥u0,D≤k/16,2≤j≤T}`,

it satisfies

1. `Z_r(C_r(y))=Z_r(y)` and `C_r(y)` ends in `00` on `F∩G`;
2. for `x^(j)=1^(N+1−j)0^j`, `d_H(C_r(y),x^(j))≤3D+4r−5<k`;
3. `(a−β) Q_a(F∩G)≥t/64`, with `β=1/(N−1)`;
4. the finite measures
   `ν_j(dy)=∫_I Q_a(dy;F,j(y)=j,U≥u0) da/a`
   have mass `μ_j≤t/u0`;
5. the stationary null `Q_*` with zero-to-one probability `β` and one-to-zero probability `q=1/[2(N−1)]` gives
   `v_j=Q_*(x^(j))≥1/(8N)` for `2≤j≤T`.

The mixture mass in item 4 follows by ordinary `00` count `v=j+1` on `F`, the beta-integral bound `1/u`, and the convex renewal sum `t R_n≤t`. The actual null word has `J00=j−2`; neither the lemma nor this proof asserts equality of its histogram with the proposal's. Item 1 compares the *output relocation* to the *clean proposal*, not to the null input.

All these source tables satisfy every row of the original two-step pair minorization with supplied `β=1/(N−1)`: the pair ratio is `T(d,s)/π(s)` for every initial pair `(b,d)` and destination pair `(s,z)`. The four alternative ratios are `(1−a)(a+t)/t,a+t,a+t,(1−t)(a+t)/a`, each at least `β`; the four null ratios are `3(1−β),3β/2,3q,3(1−q)/2`, each at least `β`.

This statement isolates all imported scientific premises. Their complete proofs remain in the two named local dependencies; no merely numerical check is substituted for them.

## 4. Single legal kernel, now with the channel attached

Predeclare all `ν_j` from Section 3 using only `(N,k,r)` and the auxiliary family `Q_a`. The integral over an auxiliary family does not give the kernel access to the true law. For input `x^(j)` with `2≤j≤T` and `μ_j>0`, draw one proposal `Y~ν_j/μ_j`. If `B(Y)` holds, form `C_r(Y)` and accept only if its **actual** Hamming distance to input is at most `k` and its final pair equals the input's final pair. If any test fails, return the input; do not resample. For all other inputs return the input.

This is one well-defined source-independent strict-budget kernel on every word/outcome. It preserves both final symbols everywhere, depends on no source parameter, encoder coin, decoder coin or channel noise, and in fact does not depend on `(E,D)` at all. After its output the encoder and channel run normally. On `F∩G` every proposal passes the tests, and both null input and output end `00`.

Let `ℓ_a(y)` denote the expected loss of the full encoder-channel-decoder rule on word `y` against the TRUE clean `Q_a` next-symbol target at its actual last symbol (zero-to-one parameter `a` when that symbol is zero; one-to-zero parameter `t` when it is one). On `F` this is exactly loss against target `a`. Let `b_a(y)`, used only on `F∩G`, denote its expected loss on word `C_r(y)` against null target `β`. The subscript `a` on `b_a` only records the proposal integral; the actual null target is always `β`. By (7),

`b_a(y)≥a−β−κℓ_a(y)` on `F∩G`.

Write `S=sup_{a∈I} E_{Q_a} ℓ_a(X)`, the unconditional clean risk of this same rule. Let `ρ=u0/(8Nt)=u0/(8x)`. First discard all unused null inputs, failed proposals, and accepted proposals outside `G`, and replace `v_j/μ_j` by `ρ` ONLY on nonnegative actual null losses. This gives

`R_null ≥ ρ ∫_I E_{Q_a}[1_(F∩G) b_a(Y)] da/a`
`       ≥ ρ ∫_I [(a−β)Q_a(F∩G)−κ E_{Q_a}(1_(F∩G)ℓ_a(Y))] da/a`
`       ≥ ρ (t/64−κ S)L`.

Therefore the new finite channel theorem is

**`R_null ≥ ρ [(t/64−κ_R S)L]_+`.**                 (8)

Crucially the proposal law and acceptance event are independent of channel outcomes. Applying a signed triangle inequality before discarding or lowering transport coefficients would be invalid; the order above avoids that error.

## 5. Quantitative normalized lower; no minimax interchange

For every fixed `(E,D)`, clean identity attack implies `S≤Γ_N/√N`; the exhibited legal attack implies `R_null≤Γ_N g_N(k)`. If `Γ_N=∞` all conclusions are immediate. Otherwise (8), even without its positive part, gives

`Γ_N [g_N(k)+ρ κ_R L/√N] ≥ ρ t L/64`.

Consequently, whenever the finite assumptions hold and `k≥√N`,

**`Γ_N(E,D) ≥ ρ c L / {64[1+ρ κ_R L√N/k]}`.**       (9)

The constants do not depend on the rule. Taking `inf_{E,D}` preserves (9) directly. No optimizer exists or is needed; the attack is an explicit witness within the same supremum.

### Explicit finite r=2 consequence

Assume `N≥2^160`, take `r=2`, `k=ceil(N^(3/4))`, and suppose `κ_R≤N^(1/8)`. Then:

- `N^(3/4)≤k≤2N^(3/4)≤N/8`, `k≥256`, `ck≥4096`;
- `N/k²≤N^(−1/2)≤2^(−80)<2^(−40)` and `At≤(1/8)N^(−1/4)<1/4`;
- `1/64≤ρ≤1/32` because `x≥4096`;
- `L≥(log N)/4+log2≥(log N)/4`;
- `L≤log4+(log N)/4≤N^(1/8)` for all `N≥2^160` (true at the endpoint and preserved since the exponential derivative dominates the linear derivative in `log N`).

Thus `ρ κ_R L√N/k≤1/32<1`, and the deliberately weakened denominator bound in (9) gives

**`Γ_N(E,D)≥2^(−31) log N`.**                     (10)

This conclusion holds uniformly over all length-R randomized codes and decoders.

## 6. Paid original horizon and length necessity

In the original notation `M=N−1`, the budgets are exactly `0,...,M`, and all witnesses have certificate `β=1/M`. Pointwise

`g_N(k)≤g_M(k)≤[N/(N−1)]g_N(k)`.

Thus every rule's original normalized factor obeys `Γ_M≥[(N−1)/N]Γ_N`, and so does its infimum. Equation (10) yields, for `M+1≥2^160` and `κ_R≤(M+1)^(1/8)`,

**`inf_(E,D) Γ_M(E,D)≥2^(−32) log(M+1)`.**          (11)

For fixed `0<η<1/2`, write `b_η=log((1−η)/η)>0`. If a length schedule and same-map rules achieve original factors bounded by a fixed `B` for every sufficiently large `M`, then for all sufficiently large `M` with `2^(−32)log(M+1)>B`, (11) rules out `exp(b_η R)≤(M+1)^(1/8)`. Necessarily

**`R(M)>log(M+1)/(8b_η)`**, hence `R=Ωη(log M)`.

If the bound is expressed only on the minimax infimum, the same conclusion follows from (11), with no attainment assumption. The threshold in `M` may depend on `B` and `η`; the explicit leading necessary coefficient above is intentionally not claimed optimal.

The lower uses stationary initial pairs, which are a subset of arbitrary initial-pair laws. It never assumes that an arbitrary initial pair's initial edge follows the source transition. The known upper must discard raw `X0` and work on `X1,...,X_(M+1)` as repaired in FOT002; this lower needs no such repair because its witnesses are stationary.

## 7. Matching sufficiency and scope

The restored FOT002 exact-bit procedure over `r=2` has risk `≤1024/√M+2^20 k/M` for arbitrary initial pairs and legal strict-budget kernels, using the first-order truncated suffix and its exact half-visit bit. Its encoder is a law-independent full-corrupted-path scan and its decoder uses precisely the original counts and endpoint pairs. This is an additional upper-bound dependency, not an inference from (8).

Repeat that bit `R` times through BSC and majority-decode (fair tie). Put `a_η=2√(η(1−η))<1`. The bit error is `δ_R≤a_η^R/2`. Coupling the noisy and exact procedures, TV loss is bounded by one, so the normalized risk is at most `1024+2^20+√M δ_R`. Taking integer

`R≥log(√M/2)/[−log a_η]`

when the numerator is positive bounds the extra term by one. This proves an `Oη(log M)` sufficient length in exactly the same scan-and-message model, conditional on that independently restored exact-bit upper. Together with (11), the sharp **order** is `Θη(log M)`, not a sharp leading constant.

Endpoints differ: at `η=0` a fault-free exact bit suffices and the finite likelihood ratio is unavailable. At `η=1/2`, the message is independent of its input, so arbitrary R cannot improve the baseline; (8) has `κ=1`. If `η` varies with M, the formulas remain meaningful where their assumptions hold, but the fixed-η Θ statement does not assert uniform constants. This is not an adversarial-noise, adaptive/variable-length code, source-oracle, growing-window, squared-loss, or second-order-source theorem.

## 8. Failed/weaker routes retained

1. The full-alphabet common minorizer `(2η)^R` only transports the old logarithmic lower multiplicatively and yields `Ω(log log M)` necessity. It is valid but insufficient here.
2. The sharper two-codeword repetition overlap still gives a multiplicative attenuation and does not by itself prove a general `Ω(log M)` lower.
3. It is false that relocation preserves an arbitrary encoder's word. This proof never asserts that: it compares the different messages by (6).
4. It is invalid to transport the signed triangle expression before restriction/transport of nonnegative actual null loss. Section 4 retains the legal ordering.
5. It would be invalid to let baseline or attack reveal the BSC noise and still use the conditional BSC pmfs. Fresh conditional noise is essential.
6. It would be invalid to claim arbitrary initial-pair upper bounds by treating the first edge as homogeneous; the repaired FOT002 suffix interface is explicitly used instead.
7. A channel with zero transition probabilities (for example an erasure channel retaining an unerased symbol) need not have any finite all-input likelihood ratio. The BSC proof must not be silently exported to such channels; this is why it can give a different length order from an overlap-only argument.
8. No claim is made that the overlap review was wrong. Its abstract result remains valid; this is a stronger application-specific use of the restored mixture construction.

## Review status

Author proof only, awaiting an independent adversarial review of (6)–(11), model scope, and the imported exact-bit upper interface. The load-bearing advance is (7), followed by the original legal mixture transport. Finite numerical checks are optional corroboration and cannot certify the large-horizon asymptotic argument. No external writes or publication authorized/performed by this note.
