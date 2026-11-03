# Constant-additive expected-TV attack hardness for a fixed iid source

2026-11-03. Candidate task-specific reduction, not yet independently reviewed. It changes the probability readout of the earlier variable-width gap-SAT model. It does **not** inherit that model's O(1/M) absolute prediction-error guarantee, does not claim hardness for a trained pilot, fixed width, general unknown-source minimax risk, SGD or an actual floating backend, and does not assert novelty for PCP/Max-SAT or generic neural verification. All work is local; no random operation, sampling, publication, or modification of prior artifacts was performed.

## 1. Primary gap source and formula preparation

Håstad, *Some Optimal Inapproximability Results*, Journal of the ACM 48(4), 798–859 (2001), Theorem 6.5, https://www.cs.umd.edu/~gasarch/BLOGPAPERS/max3satl.pdf, proves that for any fixed epsilon>0 it is NP-hard to distinguish satisfiable E3-CNF formulas from E3-CNF formulas with optimal satisfied fraction at most 7/8+epsilon. Its Definitions 2.2–2.4 define E3 and the optimum satisfaction fraction. We use epsilon=1/16 and alpha=15/16. Perfect completeness is part of the cited theorem; no proof of the PCP result is claimed here.

For each original clause, remove repeated occurrences of the same literal; if it contains a literal and its negation, retain it as one always-true clause. Keep every original clause position, including duplicate clauses and tautologies, so the number m and every assignment's satisfied fraction are unchanged. No clause is padded or deleted. The resulting ordinary clauses contain at most three distinct variables; tautologies use a fixed true feature. This normalization is polynomial and preserves both sides of the cited gap, even if an input has repeated or complementary literal occurrences.

## 2. Exact model, legal edit and source

Take an n-variable, m-clause normalized input with n,m>=1. Let M be the least power of two >=max(n²,m²,128), P the least power of two >=m, and k=n. Then M=O(n²+m²+128), k<=sqrt(M), m<=sqrt(M), and m<=P<2m. Position embeddings and masks are explicitly written, so M is paid model/input size rather than free advice.

At position i, the additive position embedding has one coefficient s_(j,i) in {-1,0,1} per clause j, encoding a positive, negative or absent occurrence of variable i; dummy positions have zero coefficients. For an always-true clause all coefficients are zero and C_j=1. For an ordinary clause C_j counts negative literals. Add the shared token embedding z_i in a separate coordinate. A shared affine-ReLU layer of width 2m forms

  v_(j,i)=ReLU(s_(j,i)+z_i-1)-ReLU(-s_(j,i)+z_i-1)=s_(j,i)z_i.

A zero-score uniform causal attention head, with a public mask selecting exactly the M editable input positions, returns the m averages of v. Its value width is m. A paid scaling by M and m post-head ReLUs produce the number V(z) of unsatisfied original clauses. Let S(z)=m-V(z), and define the dyadic probability readout

  p=1/M²,      q(z)=p+S(z)/(2P).                                  (1)

There are no extra tautological or dummy **clauses**; P is a denominator only. For every binary z, 0<=S<=m<=P, so p<=q<=p+1/2<=9/16. M,P are powers of two, each scalar can be represented exactly in O(log M) fixed-point bits with sufficient intermediate width, and all local incidence coefficients belong to {-1,0,1}. The construction has constant stage depth, pre-head width 2m, one m-channel uniform head and m post-head ReLUs. Dense positional/model representation uses O(Mm) scalar entries plus explicit indexing/masks; naive all-query attention may cost O(M²m) operations rather than a final-query O(Mm). Uniform 1/M and its final rescaling, output arithmetic, storage and bit operations are not free. This is an exact dyadic hybrid specification, not a claim about a particular library's softmax, sigmoid, log, layer normalization, or rounding.

Choose the public homogeneous order-two source with every next-symbol row Bernoulli(p). Its pair-state kernel satisfies P_theta²(u,v)=Pi(v) for all pairs with Pi the iid Bernoulli pair law, so the all-state certificate is beta=1. Let H=(X_0,...,X_(M+1)) have any initial-pair law mu, followed by this transition table. The true next-symbol law at every terminal pair is Bernoulli(p). Legal history-only kernels may flip at most k positions i<M and must leave the terminal pair fixed; they can use public H and model parameters but are not given hidden theta or the future label. The source p is a fixed public function of M, not a secret oracle. The optimization concerns **true expected next-symbol TV**, not a clean-history add-one surrogate or CE; in particular no CE monotonicity is assumed for (1).

## 3. Exact expected-risk identity and constant value gap

Since q(z)>=p, the TV error to the fixed source law is q(z)-p=S(z)/(2P). Let S*=max_(x in {0,1}^n) S(x). Every assignment can be obtained from every clean H by overwriting at most its first n bits, leaving all other positions including the protected pair unchanged. Hence a fixed history-only map that hard-codes a maximizing assignment attains S*/(2P) on every H, independently of mu. Such a map is an existential witness to the supremum; the reduction does not supply a polynomial method to discover the assignment. No legal randomized or deterministic kernel can exceed the global maximum S*. Therefore the unrestricted source-independent expected-TV optimum is exactly

  R*(phi,mu)= S*/(2P).                                             (2)

This equality is for the specified exact model family and any initial law mu. It immediately reduces the imported gap: satisfiable instances have R*=C=m/(2P), whereas at-most-alpha-satisfiable instances have R*<=alpha C. Because m/P>1/2, C>1/4 and their separation (1-alpha)C=C/16 is strictly greater than 1/64.

The rational midpoint tau=(1+alpha)C/2 has O(log M) bits. Its distance to each promise side is at least C/32>1/128. Therefore a polynomial-time algorithm that outputs any rational estimate v satisfying |v-R*|<=1/128 on every instance of this family could decide the Håstad promise by comparing v with tau. Constant-additive **expected-risk value approximation** at this accuracy is NP-hard; no claim is made that the general expected-value functional decision problem is in NP or NP-complete. The algorithm's guarantee must concern the true expected optimum (2), not a surrogate target, a single history, an arbitrary upper bound or an unevaluated attack.

## 4. Separate polynomially evaluable deterministic-policy consequence

Now fix the stationary iid initial pair law. Let h0=0^(M+2), lambda=P(H!=h0), and suppose a polynomial-time algorithm returns a polynomial-size/evaluable deterministic history-only kernel A that is legal for every h and guarantees expected TV at least R*−1/128 on every constructed instance. Bernoulli's inequality gives

  lambda<= (M+2)/M² <= 2/M <= 1/64,

where the last step uses M>=128. On a satisfiable instance R*=C>1/4. Let f0=S(A(h0))/m. At all other histories TV is at most C, so

  C-1/128 <= E TV(A(H)) <= C[f0+lambda],
  f0 >= 1-(1/128)/C-lambda > 1-1/32-1/64 = 61/64 > 15/16.

Evaluating A(h0), verifying that it obeys the edit/protection constraints and counting its satisfied clauses therefore distinguishes the satisfiable case from the no case, in which every assignment satisfies at most 15/16 of clauses. Thus this particular deterministic legal-policy output guarantee also implies P=NP. This conclusion explicitly requires a deterministic, polynomially evaluable policy representation and the stationary start; it is not automatically a result for randomized kernels, arbitrary implicit policies, or a raw value oracle. The value gap in Section 3 did not require stationary start.

## 5. Scale, classical baseline, and limitations

By design, this rescaling allows TV as large as 1/2 and **does not preserve** the earlier O(1/M) absolute-error statement. On satisfiable formulas the worst expected TV equals C>1/4; relative to p=1/M² this predictor can be extremely inaccurate. This is essential to obtaining a constant additive gap in the unnormalized true-TV value. A source-specific classical predictor told the same public p can return Bernoulli(p) on every history and achieve exactly zero TV under every corruption, using O(log M) bits to encode p. Thus this is hardness of evaluating/optimizing attacks against an explicitly supplied intentionally inaccurate model, not an information-theoretic difficulty of predicting this known iid source, not a Transformer benefit, and not a lower bound for the unknown order-two class or its minimax predictor.

The clause dimension and pre-/post-head widths grow with the input; fixed-d/fixed-width conclusions do not follow. The result is a worst-case computational reduction under P!=NP, not evidence that any training algorithm learns these parameters, that actual GPU/BLAS execution has the same arithmetic, or that a constant error is possible when the true risk is constrained to vanish. Generic Max-3SAT and simple ReLU verification hardness predate this task-specific embedding (e.g. Sälzer and Lange 2021, https://arxiv.org/abs/2108.13179); no generic novelty is claimed.

## 6. Deterministic evidence

`check_additive.py` uses exact rational arithmetic for three fixed formulas and four fixed histories per formula. It checks every assignment with its legal reset mask, plus selected dummy edits, storing complete raw formula, history, mask, word, position/ReLU intermediates, clause indicators, q, p, TV and gap data in the exclusively created `additive_cases.jsonl.gz`. It includes a satisfiable formula, an unsatisfiable 3-variable formula containing all eight distinct 3-literal clauses, and a repeated/tautological clause example. `check_additive.log` is the original run log. This is representative finite evidence, not an exhaustive check of all source histories or a replacement for the imported gap theorem and proof. No prior missing per-case record was regenerated.
