# Position-weighted protected-edit optimization: exact weak NP-hardness candidate

2026-11-03. Preliminary mathematical candidate, author analysis and deterministic checks, not independently reviewed. No sampling, stochastic model initialization, external repository action, or changes to prior frozen work. The numerical interval certificates and floating-point counterexample remain independent results; this note does not certify any actual NumPy or BLAS execution.

## Question and exact statement

Does a budget-legal, source-independent attacker still admit the four-counter exact optimization when the model is permitted a general position-dependent token feature, rather than the specific fixed half-bank? In a precisely defined small hybrid ReLU/uniform-attention architecture, the answer is negative unless P=NP, even for the benchmark-scale edit budget k<=sqrt(M). The result is **weak NP-hardness in the binary encoding of model/positional numbers**, via SUBSET-SUM. It is not a strongly NP-hardness, finite-fixed-precision, SGD, learned-model, average-risk, or trained-pilot result. The same computational hardness applies to an ordinary same-information subset-sum algorithm; no neural advantage is implied.

An instance of the restricted decision problem consists of M, clean history h=0^(M+2), integer budget k, a described rational-parameter hybrid network, the deterministic clean-history target t=(C1(h)+1)/(J(h)+2)=1/(M+2), and the fixed smoothed sigmoid/CE objective below. Legal z differ from h only among z_0,...,z_(M-1), with at most k differences; protected z_M=z_(M+1)=0. The decision is whether there exists legal z whose CE against t is at least log 2. The target and model are fully determined by the observed h and public network; the attack does not receive source theta or the future symbol. The exact-real nonlinear objective is specified mathematically, with comparisons reduced to rational arithmetic below; no library-level float behavior is asserted.

## Reduction

Take a positive-integer SUBSET-SUM instance a_0,...,a_(n-1), B, in binary, with n>=2 and 0<=B<=A=sum a_i. Out-of-range instances can be mapped to a fixed no-instance; this restriction preserves NP-hardness. Pad to the least power-of-two M>=n^2 (thus M>=4), and take k=n. Let a_i=0 for n<=i<M and C=max_i a_i. Then M=O(n^2), k<=sqrt(M), and input length grows polynomially. Let G be the smallest power of two >=A. The constants M,G,C,B and all positional embeddings have polynomial bit length.

Each editable token z_i has a two-coordinate representation (a_i-C,z_i); this is the sum of a position embedding (a_i-C,0) and the shared token embedding (0,z_i). A shared pointwise affine-ReLU unit forms

  v_i=ReLU((a_i-C)+C z_i)=a_i z_i,

including padded zeros. Give one causal query at the protected final position an exact mask to the M editable positions; set all query-key scores to 0. Its single attention head therefore returns the exact average V=(sum_i v_i)/M. A constant-width feed-forward readout forms S=M V, two ReLU values u_+=ReLU(S-B), u_-=ReLU(B-S), and logit

  r(z)=-(u_++u_-)/(2G)= -|sum_i a_i z_i-B|/(2G).

This is a two-stage hybrid: a shared pointwise ReLU before one uniform attention head followed by a two-unit ReLU readout. It is a realizable composition of token/position embeddings, pointwise ReLU, public masked uniform attention and a ReLU head, without layer normalization; no claim is made about a particular standard Transformer library block or the frozen tanh pilot. The M position entries are explicitly counted as model input, not free advice. The protected final query contains no hidden source information. Setting the two logits for attention to zero is exact in the real model; the explicit public mask is an architectural assumption.

Define e=(M+2)^(-2), q(z)=e+(1-2e) sigmoid(r(z)), and U(z)= -t log q(z) -(1-t)log(1-q(z)), matching the pilot's smoothed sigmoid and clean cross entropy as a mathematical function. Because 0<=B<=A<=G, we have -1/2<=r(z)<=0. Thus 1/3<sigmoid(r(z))<=1/2 (exp(1/2)<2), and smoothing moves values toward 1/2, giving 1/3<q(z)<=1/2. Since M>=4, t=1/(M+2)<=1/6<1/3; U is strictly increasing in q on this entire range. In particular U(z)<=log 2, with equality iff q(z)=1/2, iff r(z)=0, iff sum_i a_i z_i=B.

Any original subset uses at most n edits and gives a legal z; conversely a legal z at equality selects a subset of the original n items, while dummy flips have zero contribution. Hence an attack attaining CE >=log 2 exists iff the input SUBSET-SUM instance is yes. This proves NP-hardness under polynomial many-one reduction. For this restricted family, a mask is a polynomial-size witness and the equality predicate can be checked by integer summation; therefore the restricted decision problem is also in NP and is NP-complete. This membership statement exploits the proved monotonic equivalence, not an assumed exact general-purpose algorithm for arbitrary transcendental real comparisons.

## Precision, and an entirely dyadic output variant

The finite pre-logit computation uses integers, multiplication by integer C and M, ReLU, and division by M and 2G, both powers of two. It can be evaluated exactly on a sufficiently wide fixed-point grid with O(log M+log(A+1)) bits per scalar, with input embeddings and weights stored explicitly in O(M log(A+1)) bits up to ordinary indexing overhead. All coefficients have polynomial encoding length, not an infinite-precision advice trick; arithmetic time and intermediate register storage are additionally charged. The head's 1/M weights and r are exact in this chosen dyadic arithmetic. This does **not** imply that an actual float softmax, sigmoid, log, CE, or an arbitrary compiled backend implements the exact-real objective or its threshold; it establishes the rational certificate iff the precisely stated mathematical network and nonlinearities are evaluated exactly.

If one instead wants the **entire probability output** to be dyadic, set

 q_d(z)=3/(2M) - |sum_i a_i z_i-B|/(2MG).

Then 1/M<=q_d<=3/(2M)<=3/8, and q_d>t. Let Q=3/(2M), represented by a rational pair. The CE comparison U_d(z)>=CE(t,Q) is equivalent by strict monotonicity to the dyadic rational comparison q_d(z)>=Q, and hence to subset-sum equality. Thus its Boolean answer and witness are determined with exact finite fixed-point arithmetic; the logarithms in the displayed objective need not be evaluated. The threshold may be specified symbolically as CE(t,Q), rather than incorrectly claiming a rational CE threshold. This dyadic architecture differs from the pilot's final sigmoid/smoothing and is a separate variant.

Under the iid Bernoulli source with p=1/M^2, its pair-state chain satisfies P^2(u,v)=Pi(v) for all u,v, i.e. beta=1, and outputs q_d(z) on any word lie in [1/M,3/(2M)]. Therefore its TV error for this one source is at most 3/(2M)-1/M² for every attack; the clean all-zero history occurs with probability (1-p)^(M+2)>=1-(M+2)/M². This special example illustrates that exact hard optimization can coexist with a simple uniform source-specific prediction bound. It is not a guarantee over the general source class and says nothing about whether this architecture is learned.

## Complexity and the comparison with the four-counter result

The attack needs only the explicit model and observed clean history. Exact generic optimization over all edit masks is bounded by sum_{j<=k} binom(M,j) evaluations. Here the same-information classical subset-sum dynamic program maintains reachable sums using O(n A) arithmetic/bitset update units and O(A) Boolean positions, plus bit complexity, witnesses and reading the O(M) positional description; it is pseudo-polynomial in the integer A and may be exponential in its binary bit length. Binary subset-sum's weak NP-completeness is therefore the right complexity distinction, and small weights admit a polynomial solution. Fixed k permits direct O(M^k) mask enumeration with model-evaluation costs. The constructed exact-optimum value gaps can be exponentially small in the binary input size, so this proof does not show hardness of constant or inverse-polynomial additive approximation.

No contradiction with the current four-counter DP: that exact method assumes its particular position-aggregation feature and ideal arithmetic. Our bank is a learned-position-style weighted sum with up to A+1 distinct values and potentially binary-sized weights; this network is neither the six-rail fixed-half pilot nor its tanh parameter class. Restricting legal corruption to few positions does not remove the reduction when k is allowed to grow as sqrt(M). The clean history may be common under an eligible simple source, but NP-hardness is worst-case in the public model and instance, not a distributional lower bound or observed trained-model behavior.

## Prior-art check and candid framing

Shi et al., *Robustness Verification for Transformers*, ICLR 2020, https://openreview.net/pdf?id=BJxwPJHFwS, already study Transformer verification with self-attention and nonconvex input sets. Sälzer and Lange, *Reachability Is NP-Complete Even for the Simplest Neural Networks* (2021), https://arxiv.org/abs/2108.13179, already treat formal verification hardness for ReLU networks. These prior research areas make generic neural verification NP-hardness and adversarial optimization hardness unsuitable novelty claims. The present construction is an elementary task-specific reduction to a clean Markov add-one target, protected endpoints, and k<=sqrt(M) under exact hybrid semantics; a full prior-art search and independent proof review are needed before any claim that this particular combination is new. Exact prefix loss and network semantics, not a broad novelty headline, are the useful output.

## Deterministic diagnostics and preservation

`check_reduction.py` tests literal edit masks for fixed examples and exhaustively tests finite positive-integer instances, evaluating all output quantities with Python integer/Fraction arithmetic and no random calls. It does not call NumPy, a model constructor, a stochastic sampler, sigmoid, logarithm, or external code; it checks the rational equivalence, not the all-instance proof or actual float semantics. Output is retained separately in `check_reduction.log`. No data were regenerated or substituted for previously lost artifacts.
