# Expected-over-history TV hardness for a fixed simple source

2026-11-03. Candidate consequence of the explicitly encoded small-number 3SAT predictor in `../growing_features_hardness_20261103_0922/RESEARCH_NOTE.md`. This is a computational hardness claim for expected risk of that variable-width exact dyadic hybrid predictor; it is not a source-class minimax lower bound, an SGD result, a trained-pilot result, or an actual NumPy/BLAS numerical certificate. The proof and diagnostics require independent review. No random operation or earlier artifact modification was performed.

## Claim and risk experiment

Fix a normalized 3CNF formula phi with n>=1 variables and m>=1 nonempty clauses. Let M be the least power of two >=max(n²,m²,4), P the least power of two >=m, k=n, Q=3/(2M), and Delta=1/(2MP). The prior construction provides a fully specified variable-width ReLU/uniform-attention model with output q(z)=Q-V(z)/(2MP), where V(z) is the number of phi's violated clauses under the first n bits of z. Its m additive features have coefficients in {-1,0,1}, at most three nonzeros per feature, at most four prefix values per feature, and all exact dyadic scalar sizes O(log M); source, masks, model and O(Mm) dense position encoding are public and explicitly charged.

The source has every order-two next-symbol row equal to p=1/M². Equivalently, after an arbitrary initial pair, its subsequent tokens are Bernoulli(p) independently of the past. Its stationary pair law is Pi=Bernoulli(p) tensor Bernoulli(p), and its pair-chain transition satisfies P_theta²(u,v)=Pi(v) for every pair u,v, including all supported pair states; hence its all-state certificate is beta=1. p is a fixed public function of M and does not depend on the formula or on an episode's hidden variables. For each unedited history H of length M+2, an attacker may edit at most k positions among 0,...,M-1 and must preserve the last pair. The next-label law at the protected actual terminal pair is Bernoulli(p), regardless of H or the initial law.

Let A range over all fixed history-to-edited-history kernels satisfying the per-outcome edit budget and protected terminal pair. The kernel may use the public model and H, but does not receive an actual hidden theta or the future label; independent randomization is allowed. Define

  R*(phi,mu)=sup_(A legal and source-independent) E_(H~mu,theta, A)[ |q(A(H))-p| ].

The expectation is over source trajectories and the kernel's own independent randomization. Here mu may be any initial-pair distribution; stationary mu suffices as a fully specified complexity instance. The optimizer and source risk are not given B(H), a next-token label, or a hidden-theta oracle. B(H) from the earlier clean training objective is not used in this expected true-TV statement.

## 1. Gap proof, on every history

For every binary z, 1/M<=q(z)<=Q and p=1/M²<1/M, so the exact TV distance from Bernoulli(q(z)) to the source next-symbol law is q(z)-p.

If phi is satisfiable, fix any satisfying assignment x* in {0,1}^n. The history-only map A_x* takes any h, replaces positions 0,...,n-1 by x*, and leaves all other positions, including the last pair, unchanged. It flips at most n=k bits on every possible h and is independent of the current source or next label. Dummy positions and the protected terminal bits do not enter V or q. Thus V(A_x*(h))=0 and q(A_x*(h))=Q for **every** h, so this fixed admissible map has expected risk Q-p. The uniform upper bound q<=Q proves

  phi satisfiable => R*(phi,mu)=Q-p.                                (1)

Hard-coding x* here is an existential witness to the supremum. The construction does not supply an efficient algorithm to find that assignment; finding it is the hard part. It is not a hidden-source or future-label input.

If phi is unsatisfiable, every assignment to the first n bits violates at least one clause. Therefore for every binary z, irrespective of h, terminal bits, dummy bits, or the legal kernel's randomness,

  V(z)>=1,  q(z)<=Q-Delta.

Consequently

  phi unsatisfiable => R*(phi,mu)<=Q-p-Delta.                       (2)

These bounds hold for every mu because every transition row has next-symbol probability p; no high-probability all-zero history, source-dependent attack, or special treatment of null histories is required for the value gap. Restricting mu to the stationary iid start gives one fully explicit source-distribution family.

## 2. Exact and approximate expected-value complexity

The model and source reduction are polynomial in the input formula's explicit size, since M=O(n²+m²), and M,P are powers of two. The rational midpoint

  tau=Q-p-Delta/2

has O(log M) bits and is part of the public decision instance. Equations (1)-(2) give a promised gap: deciding whether R*>=tau is NP-hard. If a polynomial-time algorithm returned a rational v satisfying |v-R*|<Delta/2 on every instance in this family, comparing v to tau would decide 3SAT. Delta=1/(2MP) is inverse-polynomial in the explicit model size, because P<2m<=2 sqrt(M) and the model contains the M position entries. This is NP-hardness of **exact expected-risk value or sufficiently fine inverse-polynomial additive value approximation**, not a claim that the unrestricted functional-policy decision problem lies in NP or is NP-complete.

The supremum here is over all admissible source-independent history kernels, not only over an efficiently searchable policy class. A value oracle need not produce an attacker; the reduction checks its value. The existential map A_x* in the yes proof is simple when x* is known, but the reduction does not provide x*. A generic algorithm that merely returns an unevaluated policy, a randomized kernel, a score under B(H), a source-averaged different objective, or a possibly illegal map is not automatically a value oracle. Finite precision for an actual numerical implementation must be addressed separately; this result is in the exact dyadic model.

## 3. A separate representable deterministic-policy consequence

For the following additional statement, take the stationary iid initial law. The all-zero h0 of length M+2 has probability

  pi0=(1-1/M²)^(M+2) >= 1-(M+2)/M² >= 5/8  for M>=4.

Suppose a polynomial-time algorithm always returns a polynomial-description, polynomial-evaluation **deterministic** history-only kernel A that is legal on every history and whose expected regret R* - E[TV(A(H))] is strictly less than Delta/2. On a satisfiable instance, if its action at h0 had V>=1, its loss at h0 alone would create expected regret at least pi0 Delta >=5Delta/8, a contradiction. Thus evaluating A(h0), verifying legality and checking V=0 would decide 3SAT; on an unsatisfiable instance no output word has V=0. This is an inverse-polynomial additive-witness hardness statement under these explicit output and evaluation conditions. It does not automatically cover randomized policies or policy descriptions that cannot be evaluated in polynomial time; no algorithm is assumed to output the hidden source or future label. The bound pi0 uses stationary initialization, unlike (1)-(2).

## 4. Scale and limitations

Across every binary word, 1/M<=q<=3/(2M), so this fixed source's absolute TV error is uniformly at most Q-p=O(1/M), despite the fine expected-value computational gap. The relative error TV/p is at least M-1. The identity map is uniformly legal and achieves at least the ratio

  (1/M-p)/(Q-p) = (2M-2)/(3M-2) >= 3/5

of R* for every formula and initial law. Thus this family does not prove constant-factor approximation hardness and in fact has a simple 3/5-factor attack; neither this factor nor the small absolute risk is claimed for other models/sources. The risk gap is for a fixed known simple iid source and this model family. It does not prove a lower bound on statistical risk, minimax robustness over all unknown order-two sources, sample complexity, learned attention, or SGD. Generic neural verification/3SAT hardness precedes this task-specific reduction; see Sälzer and Lange (2021), https://arxiv.org/abs/2108.13179, and Transformer verification Shi et al. (2020), https://arxiv.org/abs/2002.06622. No generic novelty claim is made.

## 5. Exact deterministic record

`check_expected.py` enumerates all source histories and all legal masks for three fixed tiny formulas, separately computes each source history's exact rational probability and each legal candidate's ReLU features, output and true TV, then exactly sums the pointwise maxima. It checks the explicit satisfying-assignment map, expected-value gap, midpoint and identity ratio. `expected_cases.jsonl.gz` was created exclusively for this run and contains the full per-history, per-mask input/intermediate/output records emitted by the script, not regenerated earlier records. `check_expected.log` is the original stdout/stderr. These are finite diagnostic evidence, not a proof, float-backend result or recovery of prior missing data.
