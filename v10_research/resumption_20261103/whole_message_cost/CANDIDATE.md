# Whole-message cost: no free counts, no free endpoint

2026-11-03. Local candidate; not accepted, not published. This is a **new observation model**, not a strengthening of the previous supplemental-gate theorem.

## Result and scope

For every fixed known binary-input finite-output memoryless channel W with distinct rows, the minimum fixed physical-input length permitting a constant g_M-adaptation factor has order Theta_W(log M). This includes disjoint supports and detectable erasures: their smaller *supplemental* gate lengths do not imply smaller *total* prediction-message lengths. Identical rows make constant-factor adaptation impossible regardless of length.

The upper is statistical existence with an explicit finite greedy construction; it is not an efficient-neural claim. For fixed rational W the construction and all subsequent operations have finite explicit bit-complexity bounds below, polynomial in M with a possibly large W-dependent exponent. Nothing uses an unproved coding theorem or the pending finite-likelihood lower bound.

## 1. New experiment and quantifiers

Retain the accepted FOT002 source, attack and target: M>=64; clean binary word X_0,...,X_(M+1), arbitrary initial PAIR law, and hidden first-order transition table governing transitions after the initial edge. A strict law-independent offline kernel changes at most k of the first M coordinates, protecting X_M,X_(M+1), where k ranges over 0,...,M. The target is the actual-terminal next-symbol law. Loss is unconditional unsquared TV. Either all first-order tables are admitted or the original all-state pair certificate beta=1/M is imposed; the upper covers the former and the lower witnesses obey the latter.

An encoder scans the complete corrupted word Z and sends exactly R binary channel inputs. The receiver knows only M, W, the fixed algorithm/codebook, and the R outputs. In particular it receives **no counts, raw symbols, endpoint, histogram, source table, budget, or path-dependent seed for free**. Independent public/private randomness is permitted, but not feedback, timing, variable length, channel-aware attacks, or ancillary data. W is fixed independently of M and its noise is fresh memoryless conditional on the entire pre-channel experiment. The same encoder/decoder works for every k, source, initial law and admissible kernel at a fixed M.

Write g_M(k)=max(M^(-1/2),k/M) and let Gamma_total,W(M,R) be the infimum, over these procedures, of their supremum risk/g_M(k). A constant-factor length order asserts existence of one finite constant C independent of M, and necessary length order for any such uniformly bounded factor. It does not promise an arbitrary prescribed C below the intrinsic minimax floor.

## 2. An exact B-bit sufficient prediction payload

Discard Z_0 and use the truncated word Z_1,...,Z_(M+1), with exactly M transitions. Let t=Z_(M+1). Define, using departure positions i=1,...,M,

    J_u = sum_i 1{Z_i=u},
    C_u = sum_i 1{Z_i=u, Z_(i+1)!=u},
    A_u = sum_(i=1,...,floor(M/2)) 1{Z_i=u}.

Set J=J_t, C=C_t and G=1{512 A_t>=J_t}. The payload is

    (J,C,t,G),     B=2 ceil(log2(M+1))+2 bits.

Use fixed-width binary fields. For valid payloads the receiver outputs flip probability qhat=C/J if J>0 and G=1, otherwise zero, then converts this to next-symbol probability p_hat=qhat if t=0 and p_hat=1-qhat if t=1. For invalid fields (J>M, C>J, etc.) use any fixed distribution. Every output is a distribution and its TV loss lies in [0,1].

By the accepted exact-half-visit result in FOT002/FOU001, its risk is at most

    1024 M^(-1/2)+2^20 k/M <= Cg g_M(k),
    Cg=1024+2^20.                                      (1)

No initial-pair assumption was silently changed: condition on clean X_0=b only in the proof, prepend b to each candidate suffix to induce the original fixed legal kernel, and apply the same suffix predictor conditionally; average over b. Neither encoder nor receiver knows clean b or the source. This is precisely FOT002's repair. Alternatively, FOT003 shows these suffix edge counts equal triple in-degrees, but here the encoder directly computes them, and the receiver receives neither triples nor endpoints for free.

A single left-to-right scan suffices: keep four pair counters and two half-departure counters, adjacent bits, and position; ignore the first edge. After reaching the final symbol select its row. Thus payload formation takes O(M log M) elementary bit operations and O(log M) auxiliary working bits, excluding its read-only or streaming input; it does not create a stored copy of the word. Reading all M+2 input symbols once is included in this scanning-operation bound. If the original word is resident in memory and its storage is charged to total live storage, add M+2 input bits to the auxiliary-space figure. With O(log M)-bit counters as RAM words the scan takes O(M) word operations. These costs are separate from communication and channel coding.

## 3. Elementary fixed-block code, including maximal error

Let h=sum_y sqrt(W(y|0)W(y|1)). Cauchy-Schwarz gives h<=1, with equality exactly when the rows are identical (the two nonnegative square-root vectors have norm one). Distinct rows therefore give h<1.

If h=0 the supports are disjoint. Send the B payload bits directly and decode each by support membership, with zero error: R=B. Consider now 0<h<1. Fix delta=1/4 and a=1-H_2(delta)>0, where H_2(x)=-x log2 x-(1-x)log2(1-x). Choose integer

    R >= max{ B/a, (B ln 2 + (ln M)/2)/(delta (-ln h)) }.       (2)

Let d=ceil(delta R), K=2^B. Build a binary length-R code greedily in lexicographic order: select the first available binary word and delete all words at Hamming distance at most d-1 from it; repeat until none remain. This is a deterministic finite algorithm. Each selection deletes at most

    V=sum_(j=0)^(d-1) binom(R,j) <= 2^(R H_2(delta)).

For completeness, for j<=d-1<delta R and delta<1/2,

    delta^j(1-delta)^(R-j) >= delta^(delta R)(1-delta)^((1-delta)R)
                            =2^(-R H_2(delta)).

Insert this bound into 1=sum_(j=0)^R binom(R,j)delta^j(1-delta)^(R-j), retaining the indicated terms, to obtain the displayed V bound. A maximal greedy selection covers all 2^R words by its deletion balls, so its cardinality L obeys L V>=2^R and L>=2^(aR)>=K. Retain its first K words, assigning them in order to the B-bit payloads. Their pairwise distances are at least d>=delta R.

Use maximum-likelihood decoding over these K words with a fixed index tie-break. For transmitted c and competing c',

    Pr_c{ W^R(V|c') >= W^R(V|c) }
       <= sum_v sqrt(W^R(v|c) W^R(v|c'))
       = h^(dist(c,c')) <= h^(delta R).

The first inequality holds termwise wherever the competitor likelihood is at least the true one; null-probability outputs cause no problem. Product factorization gives factor one at matching coordinates and h at differing coordinates. A decoding error implies one such competing event, so **for each individual transmitted codeword**

    Pr(error|c) <= (K-1)h^(delta R) <= 2^B h^(delta R) <= M^(-1/2).   (3)

This is a maximal conditional error bound, not merely uniform-message Bayes error. Consequently it survives arbitrary source/attack-induced payload distributions. Couple to the exact payload receiver. On success the outputs coincide; loss is bounded by one on failure. Equations (1) and (3) give, uniformly over all admissible instances,

    risk <= (Cg+1) g_M(k).                                  (4)

Both B and R in (2) are O_W(log M). The encoder has no source oracle, no k input and no channel feedback. Padding, if a longer length is prescribed, uses fixed inputs ignored by the receiver.

## 4. Information lower: binary input cardinality, not output cardinality

Use the clean k=0 stationary IID Bernoulli(p) subfamily with p uniform on I=[1/4,3/4]. Its actual-terminal next-symbol probability is p regardless of either endpoint; it obeys the required pair certificate, as in the accepted IID witnesses. Identity corruption is legal. Let Q=2^R.

The encoder may depend arbitrarily on its full sample and private coins, but its output H lies in a Q-element alphabet. Conditional on any independent shared seed U=u, the combined channel-plus-receiver is a p-independent Markov kernel from H to an output prediction A in [0,1]. Receiver and channel randomness can be realized as follows: independently of p and the sample, draw a random output A_h from that kernel for **each** possible h, using fresh seeds. Given the actual H, use A_H. This construction reproduces the exact marginal prediction distribution conditional on every H and u; correlations between unused counterfactual outputs are irrelevant. It includes channel zeros and stochastic decoders. Dependence of the encoder's distribution on p through its sample is unrestricted.

Now freeze u and this entire Q-vector of independent random reconstructions. The resulting set S={A_h:h in {0,1}^R} has at most Q elements. For every p and every sample/encoder outcome,

    |A_H-p| >= dist(p,S).

A union of radius-v intervals around S covers at most 2Qv of I. Since |I|=ell=1/2, averaging p uniformly and using layer cake gives

    E_p dist(p,S) >= integral_0^(ell/(2Q)) (1-2Qv/ell) dv
                   =ell/(4Q)=1/(8*2^R).                    (5)

Average the frozen reconstruction seeds and U. Encoder private randomness never needed to be frozen: the pointwise minimum bound already covers every selection. Thus every randomized protocol has prior-average clean risk at least (5), and therefore some fixed p has at least that risk. The argument does not condition away a data-dependent endpoint or assume the source-independent encoder is deterministic. Independent shared coins are harmless precisely because their law does not depend on p.

Consequently, for **every** channel W (even with infinite outputs, provided the stated kernels exist),

    Gamma_total,W(M,R) >= sqrt(M)/(8*2^R).                 (6)

Any procedure achieving risk<=C g_M(k) uniformly must satisfy

    R >= (1/2)log2 M - log2(8C).                         (7)

This applies to an infimum of factors as well by approximation; no minimizer is needed. The bound is stronger than the finite-output-cardinality alternative 1/(8|Y|^R). It does not claim a sharp leading constant for achievable R.

## 5. Identical rows

If W(.|0)=W(.|1), the output law is independent of H and the sample, even conditional on the independent shared seed. With no other receiver information, its prediction A is independent of p. For p uniform on I, every fixed a has E_p|p-a|>=ell/4=1/8; independent randomization cannot lower this. Hence

    Gamma_total,W(M,R) >= sqrt(M)/8

for every finite R, however it grows with M. In particular no constant-factor schedule exists. This is not the earlier identical-channel equality to a counts-baseline factor: in this new model there is no such baseline. Together with Sections 3–4, this proves the stated total-cost dichotomy, independently of the pending supplemental-channel classification lower.

## 6. Real resource ledger; no free codebook

Let K=2^B<16(M+1)^2. For 0<h<1, choose R as in (2), or any explicitly certified larger length; R=O_W(log M), 2^R=M^(O_W(1)). The following intentionally conservative implementation is sufficient.

* **Physical communication:** exactly R binary channel uses; receiver stores R finite-alphabet outputs, O(R log|Y|) bits. Payload is B bits before coding; raw word length is M+2, not a free receiver input.
* **Preprocessing / code selection:** enumerate at most 2^R binary candidates, compare each to at most K retained codewords, and retain it iff all distances are >=d, stopping at K. This yields precisely the first K greedy words and costs O(2^R K R) elementary bit operations. Working/storage space O(KR+R) bits suffices; a 2^R-bit deletion bitmap is unnecessary. Code generation is once per M, W and chosen R, not once per sample.
* **Stored explicit code:** KR bits per endpoint, O_W(M^2 log M). This codebook is not assumed preinstalled for free. Either provision these bits as design storage (not sample-dependent communication) and charge their description/storage, or use the fixed greedy algorithm and reproduce it locally at both endpoints with the stated preprocessing cost. A uniform algorithm's description is O(log M)+description(W), but its small description does NOT remove its runtime or storage cost.
* **Online encoding after the scan:** form the B-bit index and retrieve/write R codeword bits. With indexed random-access codebook storage and word size O(log(KR)), this takes O(B+R) conservative bit-transfer work plus addressing; it is not a claim for an unindexed sequential tape. A sequential scan implementation instead costs O(KR) bit operations. Scan working memory O(log M) does not include the codebook.
* **Fixed rational W and exact ML:** put entries over a fixed common denominator Q_W, W(y|b)=a_(b,y)/Q_W, allowing a=0. For each candidate c, compare the nonnegative integer product product_i a_(c_i,V_i); common denominator Q_W^R cancels. Integers have O(R log(Q_W+1)) bits. Grade-school arithmetic gives a conservative O(K R^3 log^2(Q_W+1)) bit-operation bound for all scores and O(R log(Q_W+1)) extra scratch space if one streams candidates and retains the best. No floating-point likelihood tie is hidden. Add codebook and output storage. Convert the decoded rational C/J to a symbolic rational prediction with O(log M) description; an approximate numerical rendering is optional, not part of the exact theorem.
* **Rational-W length selection:** h may be irrational, but certified rational square-root upper approximations can be refined until a rational h_bar<1 is obtained (termination follows from distinct rows). Replace h by h_bar in (2), or choose an integer multiplier giving the inequalities using exact rational powers and powers-of-two comparisons. This is fixed-W preparatory computation with a finite certificate; no oracle for exact real logarithms is needed. One may likewise use a fixed rational a_lower>0 below 1-H_2(1/4) in the rate inequality and certify it once. For a fully elementary choice a_lower=1/8 works because H_2(1/4)=2-(3/4)log2 3<7/8, equivalent to 3>2^(3/2), i.e. 9>8.
* **Arbitrary fixed real W:** the finite statistical construction and likelihood decision regions remain mathematically defined. Without a representation/access/precision model for W, no computable exact-ML runtime is asserted. The rational-W ledger is a separate computational statement, not an implicit assumption in the statistical theorem. For a known BSC with crossover below 1/2, ML is exactly nearest Hamming distance and needs only O(KR) bit operations for decoding (above 1/2 complement outputs first).
* **Disjoint supports:** R=B, no distance codebook is needed, and decoding by a fixed support-membership table uses O(B) fixed-channel operations. Total communication is still Theta(log M) by (7), despite the old supplemental gate costing only one use.

All constants and exponents may deteriorate as W approaches identical rows. No uniform-in-W bound or practical low-complexity code is claimed. The polynomial construction deliberately trades substantial storage and preprocessing for a self-contained coding proof.

## 7. Dependencies and limitations

Accepted inputs: `../recovered_science/first_order_positional_probe/UPPER_CANDIDATE.md` (FOU001 exact half-visit predictor), `../recovered_science/first_order_positional_probe/triple_access/FOT002_matched_original_experiment.md` (accepted repaired arbitrary-pair transfer and exact-gate risk), and `.../BOUNDARY_RECONSTRUCTION_NOTE.md` (FOT003 count identity). Acceptance is established by their root receipts, not stale candidate labels inside original files. The new lower is proved here and uses only the admissible stationary IID subfamily.

Context, not a logical dependency: `../channel_classification/CANDIDATE.md` studies only noisy supplemental information while exact counts and terminal pair remain free. No claim here accepts its pending finite-likelihood argument. The distinction between supplemental and total cost is the central point.

Excluded: second-order generalization, efficient neural realization, adversarial channel noise, unknown/M-dependent W, variable-length or feedback coding, free side information, leading constants, and external novelty claims. The scan remains full-word and offline; its cost is charged as computation, not channel uses. No accepted manuscript was edited and no repository publication was made. Status: author candidate requiring independent adversarial review.
