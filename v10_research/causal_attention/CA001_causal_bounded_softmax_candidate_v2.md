# CA001 v2 — Fixed-depth causal bounded-softmax terminal-cut candidate

2026-11-02. Version 2 adds the explicit public dense-mask corollary in §9; v1 is preserved unchanged. Author mathematical candidate; not independently accepted. Extends BA001's statistical argument to an explicitly different architecture. No claim of novelty, arbitrary-Transformer coverage, or all-operations finite-precision implementation.

## Result first

For the architecture below, BA001's stationary second-order prediction lower bounds persist, with architecture-dependent positive constants:

    R >= c1/Q log(1+(1/8) min{Q/(M beta0), M/Q}),
    beta0=max(beta,1/M), M>=64, 0<=beta<=1/16, Q>=1;
    R >= c2/Q, M>=64, 0<=beta<=1, Q>=1.

The conclusions combine by maximum, not addition. Decoder computation after the cut is unrestricted. The new load-bearing step is a causal influence envelope with logarithmic inflation for early positions, plus its square summability. It is NOT a uniform O(1/n) single-token lemma. The remaining source/prior/harmonic and finite-message steps are BA001's explicitly reproduced method.

## 1. Architecture and comparison with BA001

There are N=M+2 observed source symbols and one appended synthetic readout position T=N+1. At history position t<=N, initial state h_t^0 is a public, source-law-independent function of X_t and public t,M,Q,beta. Across all permitted symbols its diameter is <=Delta. The initial state h_T^0 is fixed and independent of the history. Fixed depth L>=1, maximum H_a heads/layer, fixed dimensions, and final output dimension D do not grow with M,Q. Public position-dependent functions and parameters may otherwise vary with M,Q. Constants below are uniform over that variation.

At each layer, each head at t pools **every** i=1,...,t:

    s_ti=s(h_t,h_i;public t,i), alpha_ti=exp(s_ti)/sum_{k<=t}exp(s_tk),
    o_t=sum_{i<=t} alpha_ti v(h_i;public i).

On all pairs of reachable configurations, require |s_ti|<=B, ||v(h_i)||<=V,

    |s(x,y)-s(x',y')|<=S(||x-x'||+||y-y'||),
    ||v(y)-v(y')||<=V_L ||y-y'||.

The next state is a positionwise map F_t(h_t,o_t^1,...,o_t^{H_a}), uniformly F_L-Lipschitz for the sum norm. This includes bounded linear output mixing, residual connections and uniformly Lipschitz feed-forward maps. Readout g(h_T^L) in R^D is G-Lipschitz into maximum norm. Fixed-width coordinate projection is a special case. A fixed output offset is harmless.

Standard bounded Q,K,V maps on bounded reachable activations imply these score/value hypotheses for dot-product attention: bounded Q and K plus their Lipschitz constants give S. Thus the hypothesis is imposed on primitive architecture components, NOT on the desired terminal influence. Bounded positional embeddings are one sufficient route; arbitrary positional biases are allowed only while the resulting scores and component Lipschitz constants remain uniformly bounded.

Only the final cut Z_d=floor(Q g_d(h_T^L))/Q is quantized in this primary theorem. The decoder receives Z and public metadata only. It has no history reread. Source-independent random seeds can be granted to it, provided all bounds hold uniformly seedwise. Fixed positive-epsilon layer normalization is allowed when its parameters give uniform Lipschitz constants; epsilon=0 normalization near zero variance is not. Sparse/global selective masks, log(T)-scaled unbounded scores, length-growing amplification, growing depth/width, and extra exact nonlocal statistics are not included.

BA001 used arbitrary finite local tables followed by ONE normalized summary; CA001 permits recursive nonlocal intermediate features and causal prefix pooling, but requires Lipschitz primitive maps. Neither bare model definition contains the other in full generality. This is an extension of the lower-bound mechanism to a new family, not a silent relaxation of every BA001 assumption.

Optional extensions proved in §7: fixed-radius local preprocessing and finitely many exact boundary branches. The primary model excludes these to keep the causal statement unambiguous.

## 2. Attention perturbation including weight change

For two reachable inputs at one layer put delta_i=||h_i-h'_i|| and C=exp(2B). Every softmax weight along the straight line between the two logit vectors is <=C/t, since this interpolation stays in [-B,B]^t. Its derivative is

    d alpha_i=alpha_i (d s_i-sum_k alpha_k d s_k).

Consequently sum_i |d alpha_i|<=2 sum_i alpha_i |d s_i|, and integration gives

    sum_i |alpha_i-alpha'_i| <= (2C/t) sum_i |s_i-s'_i|.

Separate value change from weight change using the endpoint values:

    ||o_t-o'_t||
    <= (C V_L/t) sum_{i<=t} delta_i
       + (2VC S/t) sum_{i<=t}(delta_t+delta_i)
    = 2VC S delta_t + C(V_L+2VS)/t sum_{i<=t}delta_i.

No interpolation of hidden states is required, and the endpoint value bound suffices. Summing heads and applying F proves the coordinatewise recurrence

    delta'_t <= a delta_t + b/t sum_{i<=t}delta_i,
    a=F_L(1+2 H_a VC S), b=F_L H_a C(V_L+2VS).

Take common upper bounds across layers. This explicitly retains the attention-weight-change term corrected in Hahn's 2021 supplement.

## 3. Triangular powers: causal logarithms, not uniform dilution

Let A_ti=1{i<=t}/t and Bmat=aI+bA. For t>=i and k>=1,

    (A^k)_ti = (1/t) sum_{i<=u_1<=...<=u_{k-1}<=t} 1/(u_1...u_{k-1})
              <= (1/t) (sum_{u=i}^t 1/u)^(k-1)
              <= (1/t) [1+log(t/i)]^(k-1).

The empty product for k=1 is 1. The first inequality enlarges weakly ordered tuples to all tuples; the harmonic bound follows by integral comparison, including i=t. Set

    K_L=(a+b)^L-a^L, w_i=1+log(T/i).

For i<T, binomial expansion, w_i>=1, and nonnegativity give

    (Bmat^L)_Ti <= K_L w_i^(L-1)/T.

A replacement of one input symbol i changes the final vector in maximum norm by at most

    d_i = G Delta K_L w_i^(L-1)/T.                         (C1)

Also Bmat has row sum a+b, hence sum_{i<T} d_i can alternatively be bounded by C0=G Delta (a+b)^L (use the actual matrix-entry bounds, rather than summing the envelope). For square sums put m=2L-2 and

    I_m=int_0^1 (1+log(1/x))^m dx=sum_{k=0}^m binom(m,k) k! < infinity.

The integrand is decreasing, so its right Riemann sum gives

    sum_{i<T} d_i^2 <= (G Delta K_L)^2 I_m/T <= Lambda/M,
    Lambda=(G Delta K_L)^2 I_m.                            (C2)

When i>=T/2, d_i<=G Delta K_L(1+log 2)^(L-1)/T<=Gamma/M, with Gamma=G Delta K_L(1+log 2)^(L-1). Rare suffixes of length j<=M/4 lie entirely in this range.

These statements are finite replacement bounds, not derivative assumptions on discrete embeddings. If K_L=0 then all d_i=0 and the conclusions only strengthen; covering meshes below allow zero speed.

**Sharp warning.** Uniform zero-logit scalar averaging has A as its layer map. At L=2, replacing input 1 changes readout by (A^2)_T1=H_T/T. Thus a claimed uniform O(1/T) off-diagonal causal influence is false even with bounded activations, one head, and zero scores. This is an actual counterexample to that stronger lemma, not to CA001.

## 4. Product-source concentration and expectation curves

For a scalar function f of independent Bernoulli(p) bits with replacement bounds d_i, Efron–Stein gives Var(f)<=1/2 sum_i d_i^2. The exact polynomial identity

    (E_p f)'=sum_i E_p[f(B_i=1)-f(B_i=0)]

gives |(E_p f)'|<=sum_i d_i. Apply this separately to each of D final coordinates and define h(p)=E_p g(h_T^L). Unlike BA001, there is no ratio-of-expectations shortcut: the whole nonlinear network output is averaged.

For j random suffix bits and fixed earlier waiting symbols, (C1) gives

    ||h'(p)||_infinity<=Gamma j/M,
    Var(g_d)<=Gamma^2 j/(2M^2).

For an entirely IID history, the matrix row-sum and (C2) give

    ||h'(p)||_infinity<=C0,
    Var(g_d)<=Lambda/(2M).

These are valid for arbitrary position dependence and public Q-dependent parameters with the stated uniform bounds.

Allow H_b finite frozen side branches as in §7 (H_b=1 in the primary model). Put

    U=max{Gamma,sqrt(Lambda)}, tau=sqrt(5 D H_b) U,
    Nbox=ceil(2tau+4)+1,
    A_s=H_b(2+Gamma) Nbox^D, A_I=H_b(2+C0) Nbox^D.

Chebyshev plus union over coordinates/branches yields probability >=9/10 that all deviations are at most tau sqrt(j)/M in the suffix experiment, or tau/sqrt(M) in the IID experiment. This remains true if tau=0 by treating the zero-variance case deterministically.

If Q sqrt(j)/M<=1/2, cover h([1/4,3/4]) by mesh spacing M/(Gamma Qj), using <=(2+Gamma)(1+Qj/M) points. Each curve point is within 1/Q of a mesh point. Concentration and rounding place each integer QZ_d in an interval of radius at most tau+2 about its mesh coordinate, with <=Nbox possibilities. Including the side branch, all good complete messages lie in a fixed p-independent set of <=A_s(1+Qj/M) labels.

For Q<=sqrt(M), the IID version uses a parameter mesh with <=(2+C0)Q points and the same boxes, producing <=A_I Q good complete messages. Zero-speed curves use one mesh point. The good events may depend on p; the covering sets do not.

## 5. Stationary source transfer and explicit lower constants

Use exactly BA001 §1's three-symbol family, now with N history symbols and the synthetic token not counted as an observation. For completeness: alpha=1/(2M), beta0=max(beta,1/M), eta=beta0-alpha, p in [1/4,3/4], p_0=1-p,p_1=p, and

    Tsrc(W,W)=1-alpha, Tsrc(W,Ci)=alpha p_i,
    Tsrc(Ci,W)=eta, Tsrc(Ci,Cj)=(1-eta)p_j,
    pi(W)=eta/beta0, pi(Ci)=alpha p_i/beta0.

Unused-symbol rows equal pi. Set theta_(u,v)(x)=Tsrc(v,x), Pi(u,v)=pi(u)Tsrc(u,v), initialize at Pi. Then Tsrc(x,y)>=beta0 pi(y) and P^2((u,v),(x,y))>=beta Pi(x,y). Pi(W,W)>=1/4 is p-independent.

For Q<=M/4 let J=floor(min{1/(4beta0),M^2/(4Q^2)}). Then J>=4, J<=M/4, Qsqrt(J)/M<=1/2. Event E_j, 2<=j<=J, is W^(N-j) followed by j active letters. It has p-independent probability

    e_j=Pi(W,W)alpha(1-alpha)^(M-j)(1-eta)^(j-1)>=1/(32M).

Conditional on E_j the j bits are independent Bernoulli(p). Use one uniform prior p in [1/4,3/4] across ALL events, and grant event label j to the decoder. The actual next-symbol law is eta delta_W+(1-eta)[(1-p)delta_C0+p delta_C1].

Finite-message lemma: if a uniform parameter on an interval of length ell has probability >=9/10 of a good message, all good messages ranging over <=R labels, then any randomized scalar decoder has average absolute error >=ell/(16R). Proof: fix decoder randomness; radius ell/(8R) neighborhoods of its R outputs cover at most ell/4 of the parameter interval. Joint probability of goodness outside them is >=9/10-1/4; multiply by radius and average the randomness.

Apply this with R=A_s(1+Qj/M), ell=1/2, and use TV>= (1-eta)|v(C1)/(1-eta)-p|, with 1-eta>=1/2. Average over disjoint events:

    R_minimax >= 1/(2048 A_s M) sum_{j=2}^J 1/(1+Qj/M)
              >= 1/(8192 A_s Q) log(1+(1/8)min{Q/(M beta0),M/Q}).

The last integral comparison is BA001 §5; it uses J>=U/2 and sum>=M/(4Q)log(1+QJ/M). Thus c1=1/(8192 A_s) works for Q<=M/4.

For Q>M/4, stationary binary IID sources p_±=1/2±1/(16sqrt(M+2)) give, even with the full history, risk >=1/(128sqrt(M+2)); this follows from KL<=1/8, Pinsker TV<=1/4, and two-point testing. The displayed logarithmic right side is <=2c1/M and hence smaller. This closes every Q>=1 without importing an architecture-specific large-Q theorem.

The IID good-message count for Q<=sqrt(M), the uniform prior and finite-message lemma give risk >=1/(32 A_I Q). For Q>sqrt(M) the same full-history two-point floor is >=1/(256Q). Thus c2=1/(256 A_I) works for every Q>=1 and beta<=1. Constants are uniform over admissible encoders, so optimizing the encoder within this class preserves the bounds.

## 6. All-operations finite arithmetic is a separate obligation

Intermediate rounding is discontinuous and need not satisfy §2's Lipschitz recurrence. CA001 therefore does NOT assert the same theorem merely because an implementation uses Q-level arithmetic at every layer.

A sufficient transfer contract is: for each actual implementation and each frozen branch, there is an ideal encoder satisfying the architecture uniformly, whose final prequantization vector F obeys

    ||F_actual(X)-F_ideal(X)||_infinity <= E/Q

for every relevant history (or uniformly on the experiments with explicitly budgeted failure probability), with E independent of M,Q. If the actual decoder cut is floor(Q F_actual)/Q, enlarge every tube radius by E and Nbox accordingly. The proof then transfers. A directly supplied actual integer cut within (E+1)/Q of F_ideal works identically. Establishing this contract requires a real arithmetic audit: summation error, softmax denominator, cancellation, hidden-state rounding and length dependence cannot be wished away. It is not established here and is not incorporated into the model as an assumed terminal sensitivity conclusion.

## 7. Optional finite local preprocessing and exact boundary information

**Fixed-radius causal windows.** Replace h_t^0 by an arbitrary public table of the last r source symbols ending at t, with fixed padding, output diameter <=Delta; keep h_T^0 fixed. One source coin i affects at most r initial states at u in [i,min(N,i+r-1)]. Use actual bounds

    d_i<=G Delta sum_{u=i}^{min(N,i+r-1)} (Bmat^L)_Tu.

The sum over i is <=r G Delta(a+b)^L. By Cauchy–Schwarz and counting each u at most r times, sum_i d_i²<=r² Lambda/M, where Lambda is §3's pointwise-input constant. For late coins every affected u is also late, so d_i<=r Gamma/M. Thus replace C0,Gamma,sqrt(Lambda) by r times their old values. This proof does not assume local tables are Lipschitz in any interpolated token representation.

**Boundary branches.** Grant the decoder any fixed collection of b exact source-symbol positions, e.g. first/last r windows, and allow the initial-state tables, synthetic query and all network parameters to depend on that side value s. For each fixed s require the SAME uniform architecture bounds and local input contract. Freeze s before sampling the unconditional IID suffix/history; prove all concentration and curve statements simultaneously, then select the actual s. On the three-symbol witness there are <=3^b branches; on binary IID <=2^b. Use H_b=3^b. No claim of IID after conditioning on s is made. Exact query outputs derived from s are already covered by its finite label. Arbitrary interior/nonlocal exact side statistics are not allowed.

## 8. Provenance and status boundaries

Read BA001 v1 and prior_art/bounded_attention_family_comparison.md, including Hahn's corrected-supplement warning. The primitive bounded-softmax perturbation mechanism is standard nearby material; no fresh external literature search is claimed. Causal triangular-envelope accounting and its application to BA001's complete-message tube are the new candidate proof steps in this note. The IID and stationary event proof are explicit transfers, not consequences of cross-entropy results. An independent mathematical audit and model-interface audit remain required. The diagnostic script checks finite triangular identities, square-integral domination, perturbation recurrence on random bounded examples, and the early-token counterexample; it is not a formal proof or implementation certificate.


## 9. Explicit extension: fixed public dense causal key masks

This is an additional architecture variant, not a reinterpretation of the all-keys primary model. For each layer/head/row t, choose a public deterministic subset K_t of {1,...,t}, independent of source symbols, unknown source law, and the exact boundary-query branch. It may depend on public position, M,Q,beta. Require a fixed c>0, independent of M,Q, such that |K_t|>=c t for every row. Pool only over K_t, with the same primitive bounds and positionwise maps as §1. The same K_t is used in both configurations compared in §2.

Every attention weight along the logit interpolation is now <=exp(2B)/|K_t|<=exp(2B)/(c t). The exact softmax derivative identity on K_t gives

    ||o_t-o'_t|| <= 2V exp(2B) S/c * delta_t
                  + exp(2B)(V_L+2VS)/(c t) sum_{i<=t} delta_i.

Here sum_{i in K_t} delta_i<=sum_{i<=t}delta_i and |K_t|<=t were used. This is deliberately conservative; the query term can be sharpened. Thus every result in §§3–7 holds after replacing C=exp(2B) by C=exp(2B)/c in a,b and recomputing their descendant constants. The matrix being used is still an upper bound aI+bA; no equality with a full-prefix attention matrix is asserted. The counterexample in §3 remains admissible. The all-operations caveat in §6 is unchanged.

**Declared short-row fallback.** A rule omitting the first two positions is not a legal nonempty mask at t=1,2. One admissible full specification is K_1={1}, K_2={1,2}; for history rows t>=3, K_t={3,...,t}; for the appended synthetic terminal row t=T=N+1, K_T={3,...,N}. For M>=64, every such row has |K_t|>=t/3, so c=1/3 works. First-two-row fallback may instead be any public causal masks of this same density. Another admissible fallback is a uniformly Lipschitz positionwise map with no attention at finitely many initial rows: its recurrence is delta'_t<=F_0 delta_t, and increasing a to max(a,F_0) restores the common bound. An arbitrary data-dependent fallback or unbounded historical copy is NOT covered.

**Membership limit.** The masked variant makes omission of initial padding and of the synthetic terminal key compatible with the proof. It does not itself certify the actual SRC network or an arithmetic implementation. Fixed singleton-copy heads are not dense attention heads: they are covered only when an interface audit legitimately absorbs their effect into the fixed-radius input preprocessing of §7 (with bounded diameters and no added unrestricted exact output). Singleton-copy heads interleaved arbitrarily with subsequent global layers are not silently added to this definition. Likewise this corollary forbids masks chosen from the query or source data; freezing a boundary branch does not change that restriction.
