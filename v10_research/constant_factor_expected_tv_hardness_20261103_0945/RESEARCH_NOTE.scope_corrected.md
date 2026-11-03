# Constant-factor expected-TV attack hardness with growing features

2026-11-03. Candidate task-specific reduction, not yet independently reviewed. It modifies the output of the earlier exact dyadic 3SAT architecture; it is not a property proved for the frozen pilot, arbitrary Transformers, actual BLAS/sigmoid implementations, or learned weights. No random operation, sampling, external publication or alteration of frozen work was performed. The underlying PCP gap is imported from the primary literature, not newly proved here.

## Imported gap and its exact scope

Håstad, *Some Optimal Inapproximability Results*, Journal of the ACM 48 (2001), Theorem 6.5, https://www.cs.umd.edu/~gasarch/BLOGPAPERS/max3satl.pdf, states that for every constant epsilon>0 it is NP-hard to distinguish satisfiable E3-CNF formulas from E3-CNF formulas whose optimum satisfied fraction is at most 7/8+epsilon. The article's Definitions 2.2–2.4 specify that E3 means exactly three literal occurrences per clause and define satisfiability fraction as the optimum over assignments. We use perfect completeness, not a weaker near-satisfiable theorem. The gap refers to all original clauses counted with multiplicity; no assumption that variables have bounded occurrence is needed for this 7/8 result. We do not assume P!=NP to prove the reduction; its consequence is that such a polynomial-time approximation would imply P=NP.

Given any E3-CNF formula, process each clause in place: remove duplicate literal occurrences within that clause; if a variable and its negation both occur, record this clause as always true. Keep one output feature for **every** original clause, including each tautology and repeated clause. This preserves the truth value of every clause under every assignment and preserves m exactly, hence neither perfect completeness nor the soundness fraction changes. Every non-tautological resulting clause has at most three distinct variables. Always-true clauses use a fixed zero violation feature; they are not discarded. No dummy clauses are added.

## 1. Exact source, model and legal edits

Fix rational constants 7/8<alpha<rho<=1, choosing Håstad epsilon=alpha-7/8. On a normalized n-variable, m-clause instance, with n,m>=1, choose M as the least power of two >=max(n²,m²,4,8/(rho-alpha)), and P as the least power of two >=m. Let k=n and h have length M+2. A legal edited z may change at most k of positions 0,...,M-1 and must preserve z_M,z_(M+1). Pad only the positional input with M-n zero-effect dummy positions, never the formula. Thus k<=sqrt(M), P<2m, and M is polynomial in input size because rho,alpha are fixed constants.

Set the public order-two transition probability for symbol 1 to p=1/M² in every state; the beta=1 source is iid Bernoulli(p) with its stationary initial pair for the policy-output theorem below. Every symbol-1 conditional next law is Bernoulli(p). For clause j define s_(j,i) in {-1,0,1} and C_j as in the previous bounded-number 3SAT construction; for an always-true clause set all s_(j,i)=0 and C_j=1. For any binary z, L_j=C_j+sum_(i<n)s_(j,i) z_i is a nonnegative integer and equals the number of true distinct literals in the normalized clause, or 1 for a tautology. Consequently v_j=ReLU(1-L_j) is its 0/1 unsatisfied indicator. Let V(z)=sum_j v_j, S(z)=m-V(z), and define

  q(z)= p + S(z)/(M P).

Each original clause contributes one to S iff it is satisfied; duplicates and tautologies retain their original multiplicity. Since 0<=S<=m<=P, q is in [p,p+1/M] subset [0,1]. The true TV of Bernoulli(q(z)) from this source's Bernoulli(p) is exactly S(z)/(MP). q can be below the add-one clean-history surrogate B(h); no claim that CE against B(h) is monotone is made.

The exact architecture is the earlier shared additive position-plus-token embedding and 2m-unit pre-attention ReLU construction:

 v_(j,i)=ReLU(s_(j,i)+z_i-1)-ReLU(-s_(j,i)+z_i-1)=s_(j,i)z_i.

It uses one uniform zero-score causal attention head with m value channels, a paid public mask selecting the M editable positions, m post-head ReLUs for v_j, and a dyadic affine readout for q. For tautological clauses s=0,C=1 gives v_j=0. It has constant stage depth, pre-head width 2m, head value width m, post-head width m and an explicit O(Mm)-entry dense positional model plus masks/indexing. No token-position product is supplied for free. Since M,P are powers of two, p and 1/(MP) are dyadic; all integers, denominators and intermediate values use O(log M) bits with adequately wide fixed-point arithmetic. Actual float backend/softmax is a separate question. A full all-query dense implementation may incur O(M²m), and position data, weights, masks, bit operations, history input and readout are charged.

## 2. Expected-TV identity and a constant value gap

Let s*(phi)=max_x S(x) be the maximum number of original clauses simultaneously satisfied. From every h and every assignment x, rewriting the first n bits to x uses at most n=k edits, preserves all other positions and the terminal pair, and has q-p=S(x)/(MP). Thus an existential source-independent map which hard-codes any maximizing x attains the pointwise optimum on **every** h; its construction does not give a polynomial algorithm for finding x and uses no hidden theta or future label. No other legal kernel can exceed that optimum, even if randomized. Hence for every initial pair law mu,

  R*(phi,mu)=sup_(legal history-only kernels A) E_H |q(A(H))-p| = s*(phi)/(MP).  (1)

The expression equals a true expected-over-histories prediction TV, not the clean surrogate loss. It holds independently of the source-start distribution because p is the same in every transition row. For Håstad's promise, the yes value is C=m/(MP), while the no value is at most alpha C. The m/P factor is common to both cases: powers-of-two scaling does **not** pad clauses or distort the 7/8+epsilon gap. Therefore a polynomial-time one-sided value procedure producing v with rho R*<=v<=R* would decide the NP-hard promise by comparing v with any fixed rational between alpha C and rho C. This is constant-factor inapproximability of the expected-TV **value** for this model family, conditional on P!=NP; it is not a claim that a generic expected-risk functional is in NP. For a symmetric relative-error value estimate |v-R*|<=eta R*, the same reasoning works only when (1-eta)>(1+eta)alpha, equivalently eta<(1-alpha)/(1+alpha). Absolute values still shrink as O(1/M); this is not constant additive hardness.

## 3. A separate deterministic-policy-output reduction

Assume the stationary iid start. Let h0=0^(M+2) and lambda=P(H!=h0). Bernoulli's inequality gives lambda<= (M+2)/M²<=2/M<= (rho-alpha)/4. Suppose a polynomial-time algorithm returns a polynomial-size, polynomial-evaluable **deterministic history-only kernel** A, legal for every h, satisfying E[TV(A(H))]>=rho R* on this family. On a satisfiable phi, R*=C. Write f0=S(A(h0))/m. For every other history its TV is at most C, so

  rho C <= E[TV(A(H))] <= (1-lambda) f0 C + lambda C <= (f0+lambda) C.

Thus f0>=rho-lambda>alpha. Evaluating A on h0 and explicitly counting the satisfied clauses distinguishes the satisfiable case from the no case, where every assignment satisfies at most alpha m. Therefore such a deterministic policy-output approximation with factor rho>7/8 would imply P=NP. The source is public, but the kernel need not be supplied p or any label; its legality and polynomial evaluability are essential to this reduction. This proof does not directly establish the same claim for stochastic policies, hidden or non-evaluable policy descriptions, or a procedure reporting an arbitrary non-achievable upper bound.

Håstad's Theorem 2.24 in the same primary paper attributes to Arora et al. (1998), with Feige's refinement, a universal unspecified c<1 hardness gap even when every variable appears exactly five times. The very same reduction gives a bounded-occurrence version for any fixed rho>c. Normalizing repetitions/tautologies in place cannot increase variable occurrence counts, so this secondary statement needs no clause padding. It does **not** assert that the sharp 7/8+epsilon theorem itself retains a fixed occurrence bound.

## 4. Scope, baseline, and no contradiction

Because q>=p and q-p<=1/M, the absolute expected true TV is uniformly <=1/M for this single source. A classical predictor given the same public p can output Bernoulli(p) without reading input and has zero TV under every edit, with O(log M) bits for the dyadic p. Thus hardness concerns certifying or optimizing attack value of a deliberately constructed predictor; it is not an information-theoretic difficulty of predicting this known source, not a Transformer advantage, and not a general unknown-order-two minimax theorem. The source-specific relative error (q-p)/p can be O(M) on high-satisfaction outputs despite small absolute error.

The earlier 3/5 identity-attack factor came from a different family whose q-p had a positive floor. Here q can equal p, so that bound does not transfer. For example, take a family with the single positive clause x1 OR x2 OR x3 and n explicitly declared variables, including n-3 unused ones, with n tending to infinity. The horizon chosen by Section 1 then grows at least as n² and remains polynomial in the explicit instance length. The identity attack's expected satisfied fraction is 1-(1-p)^3 under the stationary source, while the optimum fraction is 1; this ratio tends to zero. This example is not itself an NP-hardness proof. The constant gap instead comes from the cited PCP theorem. No constant-absolute-TV error lower bound, fixed-width/fixed-d lower bound, training result, or source-class risk claim is made.

## 5. Deterministic records

`check_gap_model.py` checks selected fixed formulas, four fixed histories each, all assignments, and explicitly constructed legal edit masks in exact rational arithmetic. It includes a satisfiable formula, an unsatisfiable all-eight-clauses 3-variable formula with optimum 7/8, and a raw repeated-literal/tautology example. `gap_cases.jsonl.gz` is created exclusively and retains every tested input, mask, word, coefficient, ReLU intermediate, clause status, q, p, TV and threshold; `check_gap_model.log` is the original run log. It records representative cases, not every history or the imported PCP proof, and it is not a reconstruction of earlier omitted artifacts. All general statements require independent review.
