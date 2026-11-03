# Growing feature count makes small-number legal attack optimization NP-hard

2026-11-03. Mathematical candidate with deterministic exhaustive diagnostics; not independently reviewed. All work is local, uses no random operations, and leaves prior artifacts untouched. This is a deliberately specified exact dyadic ReLU/uniform-attention hybrid, not a result about a trained pilot, fixed-width Transformer, generic softmax backend, SGD, or source-class minimax prediction. General neural-network verification hardness is prior art; no claim is made to discover that phenomenon.

## Statement and legal game

For an explicitly encoded, polynomial-size, variable-width hybrid predictor of the architecture in Section 2, deciding whether some protected-endpoint edit of cost at most k attains a specified rational predicted-probability threshold is NP-complete. This remains true with clean history h=0^(M+2), k<=sqrt(M), a single uniform-attention head, d growing additive coordinates whose position-local coefficients are all in {-1,0,1}, at most three nonzero coefficients per coordinate, and O(log M)-bit exact dyadic scalars. The probability q is always in [1/M,3/(2M)]. The observed-clean-history add-one target is t=B(h)=1/(M+2); since q>t throughout, the same decision is equivalent to crossing the exact clean-target cross-entropy threshold CE(t,Q), where Q is a rational probability. The threshold should be represented as the symbolic pair (t,Q) or the equivalent rational comparison, not claimed to be a rational logarithm.

The attacker receives only the clean history, public model/position coefficients, public k and B(h). It can edit only positions 0,...,M-1, must keep z_M=z_(M+1)=0, and has no hidden source parameter or future token. A candidate z is a polynomial-size witness. This is worst-case complexity in the explicit model and history, not a distributional hardness result or claim that training produces such a model.

## 1. Reduction and exact feature bank

Start from 3CNF phi with n>=1 variables and m>=1 clauses, each of length at most 3. Delete tautological clauses; deduplicate identical literals inside each remaining clause. A clause containing both signs of one variable is a tautology and is deleted, so every surviving clause contains distinct variables. An empty clause yields a fixed no-instance, and a formula with no surviving clauses yields a fixed yes-instance. These polynomial-time normalizations preserve satisfiability. Instances with surviving nonempty clauses and no same-variable repetition remain NP-hard.

Set M to the least power of two >=max(n²,m²,4), k=n, and P to the least power of two >=m. Thus M=O(n²+m²), n,m<=sqrt(M), P<2m except m=1, and k<=sqrt(M). Pad the editable sequence with M-n zero-effect dummy positions. Let s_(j,i) be +1 if clause j contains x_i, -1 if it contains not-x_i, and 0 otherwise, including dummy positions. Each clause j has at most three nonzeros. Let C_j count negative literals in clause j, so C_j in {0,1,2,3}.

For any candidate z, its first n bits represent an assignment. Define the jth additive feature A_j(z)=sum_(i=0)^(M-1) s_(j,i) z_i. The number of satisfied literals in clause j is L_j=C_j+A_j, an integer in {0,1,2,3}. Let v_j=ReLU(1-L_j). Then v_j equals 1 exactly for an unsatisfied clause and 0 otherwise. With V=sum_j v_j, define

  Q=3/(2M),    q(z)=Q - V/(2MP).

As 0<=V<=m<=P, q lies in [1/M,3/(2M)], and it is dyadic because M,P are powers of two. All satisfying assignments have q=Q and every unsatisfying assignment has q<=Q-1/(2MP). Conversely q>=Q forces V=0, so it satisfies every clause. Any truth assignment is realized by flipping its 1-valued variable positions of h, at cost at most n=k. Dummy flips are allowed but have no effect. Thus a satisfying assignment exists if and only if a legal attack attains q>=Q.

The selected-row counts of the all-zero clean history are J=M and C1=0, hence t=(C1+1)/(J+2)=1/(M+2). For M>=4, q>=1/M>t and q<=3/(2M)<=3/8<1. The derivative d CE(t,q)/dq=(q-t)/(q(1-q)) is strictly positive throughout this interval. Therefore q>=Q iff CE(t,q)>=CE(t,Q), without evaluating the logarithms. All quantities deciding the threshold are exact integers or dyadic rationals. A legal mask is a witness verifiable in polynomial time, so this restricted explicit-instance family is in NP and the 3SAT reduction makes it NP-complete.

## 2. Architecture without a free token-position product

Give each position i<M the additive input embedding (s_(1,i),...,s_(m,i),0), and token z_i the shared embedding (0,...,0,z_i); the sum is (s_(1,i),...,s_(m,i),z_i). The m position coordinates are independently specified model data, at most three nonzero entries per clause. At every position use one shared affine-ReLU layer with 2m units:

  v_(j,i)=ReLU(s_(j,i)+z_i-1) - ReLU(-s_(j,i)+z_i-1).

For s in {-1,0,1}, z in {0,1}, this equals s z, with no assumed multiplication between token and position inputs. The affine weights and offsets used here are all 0,1,-1. A single head with zero query-key scores, a public mask selecting precisely the M editable positions, and m value channels returns a_j=(1/M)sum_i v_(j,i). The final protected position is the query; a standard causal implementation must also define valid masks for any other queries it actually evaluates. The head's m outputs are exactly the additive bank divided by M. Equivalently m scalar heads can share these uniform scores, but one m-channel head suffices.

A pointwise readout forms L_j=C_j+M a_j, applies m ReLUs to 1-L_j, sums V and applies the displayed dyadic affine output for q. The architecture has a shared pre-attention width 2m, one head of value width m, a post-attention ReLU width m, and a constant number of affine/ReLU/attention stages. It does not claim this is the architecture or trained parameterization of the existing six-rail tanh pilot. No layer normalization, arbitrary softmax-score exponentials or actual library implementation are assumed. The explicit mask, position embeddings, residual/routing choices and target all belong to the specification.

## 3. Precision, storage and computation

The entire pre-readout and rational-probability computation can be represented exactly using signed fixed-point scalars of O(log M) bits: s and local ReLU arguments are small integers, 1/M and 1/(2MP) are dyadic, each partial signed sum has magnitude at most 3, 0<=V<=m<=sqrt(M), and multiplying the uniform average by M recovers an integer exactly when the common grid and sufficient intermediate width are used. Explicit dyadic numerators/denominators, constants M,P, C_j and Q have O(log M) bits. No hidden exponentially fine precision is used. Correctly rounded arbitrary hardware softmax, sigmoid or CE are not established; they are not needed for the rational decision.

Writing all position embeddings as a dense M-by-m matrix and explicit network coefficients costs O(Mm) scalar entries, each O(log M) bits or fewer, plus masks, index widths, biases and output; a sparse representation has only 3m signed clause incidences but must explicitly encode positions and routing. The reduction writes its chosen encoding in polynomial time. One final-query-only implementation costs O(Mm) elementary arithmetic operations plus bit complexity and input handling; a standard dense all-query implementation may cost O(M²m) and needs corresponding memory, and no unproved pruning or kernel speedup is claimed. A literal exact reference implementation can check the rational threshold in polynomial time. Paying separately for model representation ensures position-dependent coefficients are not free advice.

The proof is NP-hard even when the rational numerators and denominators and all integer parameters are polynomially bounded in the explicitly written input length. After clearing the common dyadic denominators, it gives an integer-normalized bounded-number family with the same yes/no predicate; this is the usual small-number condition relevant to strong NP-hardness. We refrain from asserting a formal strong-NP-completeness classification for every possible encoding of the broader neural-verification problem: that would require fixing its complete integer/rational encoding and unary-size definition. The stated restricted-family NP-completeness needs neither that terminology nor a weight whose magnitude is exponential in its bit length.

## 4. An inverse-polynomial additive approximation consequence

The probability gap is Delta_q=1/(2MP), inverse-polynomial in the explicitly represented instance length. If a polynomial-time algorithm always outputs a legal word whose q is within a strictly smaller additive error than Delta_q of the optimum, then on a satisfiable instance it must output V=0; on an unsatisfiable instance no such word exists. Checking V decides 3SAT. Thus even this inverse-polynomial additive-witness guarantee is NP-hard; it is not a constant-additive-error hardness statement.

For CE, q-t >= 1/M-1/(M+2)=2/[M(M+2)] and q(1-q)<=1/4 over the interval, so dCE/dq >=8/[M(M+2)]. A satisfiable instance's optimum CE(t,Q) exceeds the CE of any V>=1 word by at least

  Delta_CE = [8/(M(M+2))] [1/(2MP)] = 4/[M²(M+2)P].

A polynomial-time algorithm guaranteed to output a legal word with additive CE regret strictly smaller than Delta_CE would also have to return V=0 on every satisfiable input, so checking V decides 3SAT. The algorithm's guarantee concerns the exact real CE but its returned witness can be checked using the integer V; no evaluation of logs is necessary in the reduction. This is not a claim about fixed d, constant additive accuracy, worst-case source risk, all networks, or existing SGD.

## 5. Connection to the finite-d DP and prior work

For each j and every prefix, A_j lies between minus the number of negative clause occurrences and the number of positive occurrences. Its total integer range contains at most 4 values because a clause has at most 3 literals. Thus the generic additive-feature DP can use at most 4^m bank tuples (times its finite-state/window factors); it is exponential when d=m grows, even though every coordinate has only O(1) possible sums. The previous pseudo-polynomial theorem assumes fixed d for polynomiality. This example shows the dependence on feature count is substantive rather than merely an artifact of exponentially large binary weights, assuming P!=NP; it does not prove a matching 4^m lower bound or exclude better exponential algorithms. The result also does not contradict direct O(M^k) enumeration when k is fixed: k=n here grows.

Sälzer and Lange, *Reachability Is NP-Complete Even for the Simplest Neural Networks* (2021), https://arxiv.org/abs/2108.13179, already prove neural verification hardness for simple networks; Shi et al., *Robustness Verification for Transformers* (2020), https://arxiv.org/abs/2002.06622, study Transformer verification. Bounded-number SAT reductions and multidimensional feature-table growth are classical; this is a task-specific legal-edit construction and is not asserted as new generic hardness. A complete literature search and independent review remain needed before any novelty claim.

## 6. Deterministic diagnostics and limitations

`check_reduction.py` checks all normalized clauses and formulas up to the saved finite bounds and all assignments using exact Python integers and Fractions. It compares the embedding/ReLU/head output and rational score to literal SAT evaluation and checks some full masks including dummy positions and protected endpoints. It additionally checks explicit tautology/repetition normalization examples. The retained `check_reduction.log` is the original deterministic output, not a regeneration of prior lost material. Finite cases do not replace the general proof, and do not test a floating backend, a trained model, or SGD.
