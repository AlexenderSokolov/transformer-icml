# SC001 — intrinsic symbol-corruption minimax law at beta=0

2026-11-02. POST-STAGE7 author candidate. Not accepted, independently reviewed, formally verified, or externally novelty-certified. Frozen sources are unchanged.

## Result first

Fix K>=3, integer M>=2 and integer 0<=k<=M. Observe N=M+2 symbols from an unknown homogeneous second-order K-letter source with arbitrary unknown initial pair law. Before ANY encoder, a source-independent randomized history-adaptive kernel replaces at most k of positions 1,...,M; positions M+1,M+2 are untouched. The predictor receives the entire corrupted word and may use arbitrary computation and independent randomness. Its target is the TRUE source next law at the TRUE (and preserved) terminal pair; loss is unconditional expected TV. No clean interior observations, edit mask, or attack random seed are supplied.

Let C_k be all kernels on words supported on this Hamming constraint. A kernel is one fixed stochastic map on histories, with no input theta, initial law, future symbols, or hidden parameter; it can depend on public K,M,k. Define

 R_cor(K,M,k)=inf_A sup_{theta,mu in D2(0)} sup_{C in C_k}
   E TV(A(C(X)),theta_(X_(M+1),X_(M+2))).

Let G=min(1,sqrt(K^5/(M+1))) and Psi(z)=z(1+ln(1/z)) for 0<z<1, Psi(0)=0, Psi(z)=1 for z>=1. Then

 max{2^-17 G, (1/512)Psi(k/M)} <= R_cor(K,M,k)
 <= min{1, 2^13 G+Psi(6K^4 k/(M+1))}.                 (SC)

For k=0 the second lower term is zero. Thus at every fixed K>=3,

 R_cor(K,M,k)=Theta_K(max{(M+1)^(-1/2),Psi(k/M)}),

uniformly in the stated finite domain. The corruption lower uses ONE explicit common kernel across the entire unknown-parameter witness family, and continues to hold even if the predictor knows this kernel and the family. It is a FULL-OBSERVATION lower, not a quantized-bank lower. Internal protection, moving an information cut, or retaining the entire corrupted sequence cannot remove it.

The theorem does not assert K-sharp constants, binary lower bounds, positive-beta rates, stationary-initialized rates, causal-online adversaries, visible edit masks, shared attack randomness, or protection against edits to the final pair. The upper proof does apply to K>=2; only the matching lower here needs three symbols. k>M is equivalent to k=M since only M positions are editable. M=1 has constant fixed-K minimax order by the clean lower and trivial upper; it is excluded from the displayed corruption-specific constants.

## 1. Universal upper, independent of attack mechanism

For clean word x let C_abc count its M triples ending at positions 3,...,M+2. For corrupted word z define C'_abc similarly. A replacement of one symbol affects at most three triple positions. Each altered triple changes the complete histogram in l1 by at most two, so

 ||C'-C||_1<=6k.

This remains true for simultaneous nearby replacements, by counting affected positions (or telescoping). The selected terminal row S is identical for x,z. Therefore ||C'_S-C_S||_1<=6k. Let J=sum_b C_Sb. The predictor applies add-one smoothing directly to the corrupted selected-row counts:

 q'_b=(C'_Sb+1)/(sum_c C'_Sc+K).

The clean add-one vector is q_b=(C_Sb+1)/(J+K). For arbitrary nonnegative vectors u,v of positive masses A,B,

 TV(u/A,v/B)<=||u-v||_1/A.

Indeed insert v/A, use |A-B|<=||u-v||_1, and divide the resulting l1 bound by two. Consequently

 TV(q',q)<=min(1,6k/(J+K)).                            (1)

This is pathwise, including J=0, altered row membership, and arbitrary attack randomization. MG001's universal terminal-occupation bound, applied to the K^2-state pair chain, gives

 P(J<w)<=min(1,K^4 w/(M+1)), integer w>=1.

With a=K^4/(M+1), layer cake yields E min(1,A/(J+K))<=Psi(aA): at threshold A/t>K use w=ceil(A/t-K)<=A/t; otherwise the event is empty. Integrate min(1,aA/t) over 0<t<1. Apply A=6k, then add R011's clean original add-one bound 2^13 G. This proves the upper in (SC). No empirical successors are presumed IID conditional on the selected terminal state.

For completeness the occupation argument is general finite-state, not a mixing assumption. For a d-state chain, let b_m(y)=P_y(J_m<w), B_m=max_y b_m(y). Visits before terminal over a whole path dominate those over an ending suffix, hence B_m is nonincreasing. Pathwise sum_{t=0}^m 1{J_t<w}<=dw. Therefore sum_{t=0}^m B_t<=sum_y sum_{t=0}^m b_t(y)<=d^2w, giving B_m<=d^2w/(m+1). Arbitrary initial mixtures are covered.

## 2. Exact exchangeability-erasure lemma

Let V=(V_1,...,V_l) consist of IID Bernoulli(p) bits, with n=sum V_i. Fix a positive integer b and let r=b floor(n/b). Choose uniformly a subset of n-r of the positions containing ones and change those to zeros. Let Z be the resulting vector. Exactly n-r<=b-1 changes are made.

Conditional on n, V is uniform among its binomial(l,n) arrangements. For any fixed z of weight r, the probability of output z conditional on n equals

 binomial(l-r,n-r) / [binomial(l,n) binomial(n,r)]
 = 1/binomial(l,r).                                  (2)

The equality follows either by factorial cancellation or counting nested subsets. Thus conditional on r, output Z is uniform on weight-r arrangements, independently of p. In particular the experiment p -> Z factors exactly through the finite message r, followed by a p-independent channel. This holds for l=0 and p in (0,1), and for all attainable cells, including truncated last cells.

If two additional independent Bernoulli(p) bits U are left unchanged, the joint experiment p -> (Z,U) factors through (r,U), followed by the SAME p-independent uniform-arrangement channel. There are at most

 4(floor(l/b)+1)                                     (3)

such messages. We do NOT condition the prior on U or falsely claim it stays uniform after endpoint conditioning. U is part of the finite message.

The random arrangement cannot convey parameter information beyond r: any decoder of (Z,U), however complicated, composes with this p-independent channel to become a randomized decoder of (r,U). Uniform subset selection may be realized with independent public-algorithm/private-attack randomness; its actual draw is not supplied separately to the predictor. No knowledge of p is used.

## 3. One homogeneous three-symbol source and one common kernel

Choose distinct alphabet symbols W,C0,C1. Set alpha=1/M. For p in [1/4,3/4], define a first-order symbol kernel

 T(W,W)=1-alpha, T(W,C1)=alpha p, T(W,C0)=alpha(1-p),
 T(Ci,C1)=p, T(Ci,C0)=1-p, i=0,1.

Unused-symbol rows can equal delta_W. Set theta_(u,v)(x)=T(v,x) for EVERY pair and initialize X1=X2=W. This is a homogeneous second-order source (in fact first-order), belonging to D2(0). An explicit stationary symbol law is pi(C1)=p, pi(C0)=1-p, pi(W)=0, and pair law pi tensor pi; beta=0 imposes no positive minorization. This stationary law is NOT used as the initialization.

For each j=2,...,M, let E_j be the event that the observed word is W^(M+2-j) followed by j letters in {C0,C1}. These disjoint events have

 e_j=P_p(E_j)=alpha(1-alpha)^(M-j)>=1/(4M).             (4)

For M>=2, (1-1/M)^(M-1)>=e^-1>1/4, for example from ln(1-x)>=-x/(1-x). The event probability is independent of p. Conditional on E_j, the j active suffix bits are IID Bernoulli(p), before any terminal-pair conditioning. At EVERY possible active terminal pair the true next law is

 (1-p)delta_C0+p delta_C1.                            (5)

Thus the true terminal query is retained, not replaced with an external query, but its four possible values share the same target row.

Define the corruption kernel on ALL K-letter words, not merely on supported witness words. If the word is of the form W^(N-j) followed by j symbols from {C0,C1}, with 2<=j<=M, apply the lemma to its first j-2 active symbols with b=k+1, leaving its last two symbols and entire W prefix untouched. Otherwise output the input unchanged. Pattern recognition and b are public and source independent. The word remains in the same pattern with the SAME j. At most b-1=k symbols are replaced and neither final position is edited. Hence this is one valid common kernel C* in C_k, simultaneously for every p. It does not require the unknown table or source law.

On E_j the entire corrupted word is generated from the finite message

 (r, U), r=(k+1)floor(n/(k+1)), U=last two active bits,

by appending to the known W prefix a uniform arrangement of j-2 bits with r ones and the protected pair U. Exact j can even be granted to the predictor; it is already visible in the W/active boundary. This accounts for the ENTIRE corrupted sequence, not only its triple counts. There is no clean original coin order, source-dependent edit mask, or uncounted endpoint port.

## 4. Finite-message Bayes lower and unconditional summation

Elementary lemma: if p is uniform on an interval of length ell and a channel emits at most D messages, every randomized real-valued estimator has expected absolute error at least ell/(4D). To prove it, fix independent decoding randomness and let z_1,...,z_D be possible outputs. The union of their radius-t neighborhoods has prior mass at most 2Dt/ell. Integrating 1-2Dt/ell for 0<=t<=ell/(2D) proves ell/(4D); then average decoding randomness. This permits an arbitrary stochastic message channel.

Use ONE prior uniform on [1/4,3/4] for all E_j. By (4) it remains uniform conditional on E_j, but is not conditioned further on terminal bits. Equation (2) lets every full-word decoder be treated as a finite-message randomized decoder. With ell=1/2, b=k+1 and l=j-2, (3) and TV(q,theta)>=|q(C1)-p| give conditional Bayes risk

 >=1/[32(floor((j-2)/b)+1)]
 >=1/[32(1+(j-2)/b)].                               (6)

No concentration event, restriction j<=k^2, or localization in p is needed. This is stronger and simpler than a rare-suffix tube: the kernel erases coin-order information exactly.

Discard nonnegative losses outside the disjoint E_j. Equations (4),(6), followed by integration of a decreasing function, give

 R_cor >= (1/(128M)) sum_{l=0}^{M-2} 1/(1+l/b)
       >= b/(128M) ln(1+(M-1)/b).                    (7)

The same prior and common kernel were used throughout, so a source supremum dominates this Bayes average. This proves a lower even when the adversary must commit to C* independently of the unknown source.

For 1<=k<=M, b>=k and the function b ln(1+A/b) is increasing in b (derivative ln(1+x)-x/(1+x)>=0). Since M-1>=M/2,

 b ln(1+(M-1)/b)>=k ln(1+M/(2k))
 >=(k/4)(1+ln(M/k)).                                (8)

The final inequality follows for t=M/k>=1 by evaluating ln(1+t/2)-(1+ln t)/4 at t=1 (positive) and noting its derivative 1/(t+2)-1/(4t)=(3t-2)/(4t(t+2))>=0. This proves the Psi(k/M)/512 lower. When k=0 this term is simply zero, without a singular expression.

Identity corruption is allowed for every k, so the inherited full-observation R011 lower supplies 2^-17 G independently. The two witnesses need not coincide: taking their maximum proves (SC), not an unjustified sum of their risks.

## 5. Interpretation and preserved abandoned routes

1. Earlier PL/IP/SH/GD lower bounds concern information after a specified encoder and quantization. They cannot simply be transferred to full corrupted observations. Here an exact common-kernel factorization accounts for every corrupted symbol; its loss is intrinsic to data acquisition.
2. Initially proposed concentration plus coarse-count route would restrict j to O(k^2), yielding a shorter logarithm. This restriction is unnecessary: uniform deletion of ones makes arrangements exactly ancillary conditional on the coarse count. Finite-message Bayes lower handles binomial noise without concentration.
3. A five-symbol fixed-cycle witness could also work, but three symbols suffice because active rows share the target and the two protected bits are counted as four labels. Silently dropping or conditioning on these bits would not be valid.
4. This common kernel is offline/history-adaptive and randomized. Revealing its random seed or requiring a strictly causal replacement strategy changes the experiment; no extension is asserted.
5. The lower is not an output-grid or network precision limitation. An arbitrarily expressive encoder/decoder observing all corrupted data still obeys it. Conversely a direct count predictor attains it up to fixed-K constants; implementation depth, width, training, and bitwork are separate questions.
6. The statistical-order tolerance is k(1+ln(M/k))=O_K(sqrt(M)); equivalently k=O_K(sqrt(M)/ln M) for diverging M (up to constants). Sufficiency and necessity follow from (SC), not from a presumed clean reconstruction requirement.

## Sources actually read

- v10_intake/source/DOT_START_PROMPT.txt and START_HERE.md: original open-ended research mandate and frozen-source discipline.
- v10_intake/source/sources/dot-return/readable/proofs/R011_global_rates_and_constant_adaptation_v1.md: full-history actual-terminal minimax lower and original add-one upper at beta=0.
- v10_research/robust_markov_prediction/MG001_theorem.md §§4–5: normalization and universal terminal-occupation lemmas.
- v10_research/precision_lower/PL001_fixed_master_log_precision_lower_v1.md: uniform-prior finite-message lemma and fixed-cycle rare-entry construction.
- v10_research/intermediate_precision/IP002_stationary_finite_domain_master_lower_v1.md §§2–3: three-symbol IID rare suffix and endpoint side semantics.
- v10_research/score_precision/SH001_sharp_weight_ratio_threshold_v1.md §§2–4 and v10_research/growing_depth/GD001_lower_derivation.md §§2–3: common-prior rare-window summation; their concentration cutoffs are NOT imported here.

The source text's historical author-candidate headers are not new acceptance receipts. Root must bind inherited acceptance records separately before accepting this new theorem. No external prior-art search was needed for the elementary proof; external novelty remains unassessed.
