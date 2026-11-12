# Two evolving-value reads: a corrected source-average risk bridge and an exact counterexample

2026-11-12, 12:00 research iteration. Starting sources: the published single-read QK risk bridge and its independent review in ../qk_risk_bridge_20261112/. This unit extends that specific bridge under additional explicit first-layer restrictions. It does not repeat the earlier unrestricted bounded-gain mean-field theorem as a new discovery, and does not claim an arbitrary multi-read lower bound.

## 1. Why the direct count-summary extension is false

Here is an ACTUAL width-six, two-read, full-PreLN counterexample to exact count sufficiency. All LayerNorm epsilons/gains are one, shifts zero; all FFN outputs are zero. Both reads have Q=K=0, hence realized global key-array Frobenius norm F=0. Every attention mask is the full self-inclusive causal prefix. Raw h_i^0=(X_i,-X_i,0,0,0,0); public terminal h_T^0=0, T=N+1. First value projection selects normalized coordinate1; first output projection writes its scalar read into coordinates3,-4. With c0=sqrt3/2, at a raw row

    h_i^1=(X_i,-X_i,c0 mu_i,-c0 mu_i,0,0),
    mu_i=i^-1 sum_{j<=i}X_j.

The second read selects normalized coordinate3 of the EVOLVED state and writes the result into coordinates5,-6. Therefore raw second values equal

    f(mu_i)=c0 mu_i/sqrt(4/3+mu_i²/4).

Take the two N=6 words +++--- and ++-+--. They have the same total count S_N=0 and the same endpoint pair (--). Their prefix means agree everywhere except i=3, where they equal 1 and 1/3, respectively. Their first-read terminal states are both zero, including its own initial zero value. Their second-read terminal scalar values therefore differ by

    [f(1)-f(1/3)]/7 >0.

Finally use full final LN and logits (normalized coordinate5,0). This is strictly increasing in the second-read scalar, so the two final probabilities differ. All matrices have fixed finite norm, clean row states are uniformly bounded, and scores/global key arrays are identically zero. The actual end-to-end computation is not a function of (S_N,endpoint pair).

This refutes any two-read extension whose ONLY error terms are the first/second score-to-uniform deviations: those terms vanish here. It is NOT a small-risk counterexample. Both words have positive probability under every fixed-c source, but the example does not establish asymptotically useful parameter information or violate the earlier source-average approximation theorem.

## 2. Additional contract for a valid two-read bridge

Use the stationary spin source P_theta(z|xy)=(1+theta xyz)/2, |theta|<=1-2c, c fixed. Let n=N+1. There is one head per read for notation; projections/gains must be summed appropriately for multiple heads.

Initially every raw row is the SAME token-only embedding h0(X_i), independent of position. Its first value is the SAME map v1(X_i), ||v1||<=V1. The first residual output is

    h_i^1=F1(h0(X_i)+O1 A_i^1),

with ||O1||op<=Lo1 and F1 L1-Lipschitz on a common domain containing the comparisons. F1 is identical across raw positions. It may include the actual residual FFN and full positive-epsilon normalization. No raw positional encoding, local mask or position-specific map is allowed to bypass these conditions into values/residuals. Public position information may affect QK SCORES, but may not be exposed as a separate historical input to later local computation. All model rules are theta-independent.

The COMPLETE first-layer score is q_i^1 dot k_j^1, up to an arbitrary row-constant offset that cancels in softmax. Any additive positional bias must be included in this controlled factorization or separately bounded and charged; no uncharged additive bias is permitted. For EVERY first-layer row query, ||q_i^1||<=Q1, each realized prefix key array has Frobenius norm <=F1key, and causal scores lie in [-S1,S1]. A whole-array bound implies the prefix bound; a bound on a projection matrix or each individual key does not. Arbitrary query dependence is harmless to the pathwise score estimate as long as it has no extra bypass to the output.

The terminal is initialized from public N and optionally the freely supplied actual endpoint pair tau. Its first value vT(tau), initial residual hT0(tau) and local map FT are public functions of that input, with the SAME V1, Lo1 and L1 bounds (enlarge constants if needed). No other history is supplied. It can be the same shared map as raw rows; allowing a separately specified terminal map only enlarges the theorem class.

True first-layer states and reference states lie in a declared radius-H domain; references may be projected onto its closed ball, nonexpansively fixing actual states. The second value map v2 is identical across raw positions, bounded by V2 and Lv-Lipschitz on this domain. It is applied to the actual EVOLVED first-layer states. The terminal may use the same v2; a separate public/free-tag-dependent map is allowed only with the same uniform bounds and explicit dependence.

The COMPLETE second-read score is likewise qT2 dot k_j^2 up to a row-constant offset; uncharged additive biases are excluded. At the second terminal read, ||qT2||<=Q2, realized whole key-array Frobenius <=F2key, and scores lie in [-S2,S2]. Keys/queries may depend on evolved states and positions, subject to these realized bounds and no decoder bypass. The downstream probability decoder sees only this read and the first-layer terminal residual (plus public/free endpoint input). It is G-Lipschitz in the concatenation of those two vector arguments along the common comparison domain. G includes output projections, remaining row-local processing, final LN and softmax. No third retrieval or direct observation of other evolved rows is allowed.

## 3. Identical token-only first-layer references

Let mu=E_theta v1(X_i)=(v1(+)+v1(-))/2, independent of theta. Define raw reference

    bar_h(s)=Pi_H F1(h0(s)+O1 mu).

This is the SAME two-valued function at every raw position. For the terminal define

    bar_hT(tau)=Pi_H FT(hT0(tau)+O1 [N mu+vT(tau)]/n).

It is a public/free-pair function independent of theta. Averaging terminal values separately is necessary because they are not raw token-only values.

The already established fixed-c covariance estimate gives, with kappa_c=sqrt(4+8/c²),

    E||i^-1 sum_{j<=i}(v1(X_j)-mu)|| <=kappa_c V1/sqrt(i).

At the terminal, the corresponding raw fluctuation has bound kappa_c V1 sqrt(N)/n<=kappa_c V1/sqrt(n). The terminal value cancels identically in the comparison, even though tau is dependent on the history. No conditioning on tau and no extra factor four are needed: the leftover random vector is just the unconditional raw sum. The local Lipschitz constant is uniform over tau.

Using the single-read softmax Jacobian estimate, the actual first head differs from its uniform-score read by at most

    V1 exp(2S1)Q1 F1key/sqrt(i)

pathwise at each raw row, and with i=n at the terminal. Consequently, letting

    A=L1 Lo1 V1 [exp(2S1)Q1 F1key+kappa_c],

we have E||h_i^1-bar_h(X_i)||<=A/sqrt(i) and E||h_T^1-bar_hT(tau)||<=A/sqrt(n). The reference projection does not worsen these estimates. Actual later states are NOT assumed token-local.

## 4. Second evolving-K/V read and direct risk transfer

First replace the actual second attention weights by uniform weights while keeping its actual evolved values. The deterministic deviation is at most C2/sqrt(n), where

    C2=V2 exp(2S2)Q2 F2key.

Then replace all evolved values by v2(bar_h(X_i)) and the reference terminal value. Their average expected deviation is bounded by

    (Lv/n) [sum_{i=1}^N A/sqrt(i)+A/sqrt(n)]
       <=2 Lv A/sqrt(n).

The last inequality follows directly from sum_{i=1}^n i^-1/2<=2sqrt(n), treating the terminal as index n. Thus the total expected second-read discrepancy is <=(C2+2LvA)/sqrt(n). The first-layer terminal residual has its own A/sqrt(n) error. Lipschitzness on the concatenated input, followed by the triangle bound for its norm, gives

    E|Q_actual-Q_reference| <=G[(1+2Lv)A+C2]/sqrt(n).      (1)

The reference raw value map v2(bar_h(s)) is identical across positions; hence the uniform reference read is a function of the total count and tau. Its residual is a function of tau. Therefore its probability output is measurable in the existing count-plus-endpoint summary. For fixed equal prior theta=+h,-h, the already established Bayes risk B_N gives

    R_equal_prior(Q_actual) >=B_N-G[(1+2Lv)A+C2]/sqrt(n),
    max(R_h,R_-h) >=max(0,B_N-G[(1+2Lv)A+C2]/sqrt(n)).    (2)

All constants are charged as written. In particular, the covariance term in A remains nonzero at F1key=F2key=0. The concrete two-read counterexample is consistent with (1)-(2). A claim that global key Frobenius alone eliminates contextual value information would omit precisely this term.

## 5. What is new here and what remains limited

This is a direct two-stage extension of the new global-QK-to-count-risk bridge, with a source-average error for the first contextualization stage. It combines already reviewed tools: fixed-c covariance, identical-token mean-field reference, softmax Jacobian control and the count Bayes obstruction. No new novelty claim is made for these ingredients.

It is stronger than simply repeating 'uniform second reads are count functions', which is false, but much more restricted than a general two-read architecture theorem. Position-dependent raw residual/value embeddings can destroy the identical reference map; arbitrary all-row gain or extra retrieval can amplify/reuse the contextual residual. The displayed total G and L1 must be retained, and global realized key norms cannot be replaced by projection bounds. The result yields another bounded-gain/root-N approximation and constant-risk obstruction, not a sharp mother frontier or a matching resource theorem.

### Diagnostic qualification

The 34 assertions in check.py comprise four explicit summary-counterexample checks, 15 source-mass checks and 15 conservative bridge-bound comparisons. All 15 numerical probability-error bounds exceed one and are therefore vacuous as quantitative risk bounds; they do not numerically validate a nontrivial lower bound. The actual summary counterexample is nonzero and meaningful. The universal bridge rests on the analytical proof, not these loose finite inequalities. Optimized Python is rejected so assertions cannot silently be disabled.
