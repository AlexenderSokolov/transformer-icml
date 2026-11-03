# Polylogarithmic-resource whole-message channel code

2026-11-03. Author candidate, pending independent review. Local research only; no publication, no accepted manuscript edit. This replaces the expensive coding implementation in `../whole_message_cost/CANDIDATE.md`, not its observation model, statistical predictor, or lower bound.

## 0. Useful result and exact scope

**Coding lemma.** For each fixed known rational binary-input, finite-output memoryless channel W with distinct rows, there is a deterministic, uniformly constructible family transmitting any B-bit message (B>=1) with:

* exactly R=O_W(B) binary channel uses;
* maximal message error at most 2^(-6B);
* preprocessing, encoding and decoding bit complexity polynomial in B, with constants and exponent depending only on W;
* explicit design storage, algorithm description, and auxiliary working space polynomial in B.

This is an elementary concatenation of familiar codes, **not a new coding scheme**. Its useful contribution here is closing the computational gap between a short communication proof and an actually polylogarithmic-resource implementation in the specified prediction experiment.

For the exact payload B=2 ceil(log2(M+1))+2 from the whole-message candidate, the resulting predictor has R=O_W(log M), coding resources poly_W(log M), and the same constant-factor adaptation guarantee. Computing the payload still requires a complete scan of M+2 input symbols: O(M log M) bit time and O(log M) counter workspace. The input is read-only or streamed. If the raw word is stored in resident memory and charged, **total resident storage is Theta(M)+poly_W(log M), not polylogarithmic**. The polylogarithmic claim concerns design plus auxiliary workspace, not an uncharged resident input.

No unknown-channel, arbitrary-real computation, neural realization, adversarial channel noise, or practical small exponent is claimed. The channel description is a fixed finite rational object of cost O_W(1), not a free arbitrary-real oracle.

## 1. Certified channel constant

Write W(y|b)=a_(b,y)/D over a fixed common integer denominator D>=1 and finite alphabet Y, permitting zero numerators. Let

    h = sum_y sqrt(W(y|0) W(y|1)).

Cauchy-Schwarz gives h<=1, with equality precisely for identical rows. Thus h<1. If h=0, the two supports are disjoint: transmit the B bits directly and recover each by a fixed support table, with zero error. All subsequent construction concerns 0<h<1.

Use rational square-root interval arithmetic to find a certified rational h_bar satisfying h<=h_bar<1. This terminates because the rows are distinct. Choose a positive integer C divisible by 4 such that

    C>=8,             h_bar^(C/4) <= 2^(-9).                (1)

Exact rational powers and integer comparisons certify (1). Incrementing C by 4 terminates. The constant-selection time, certificate, and stored rational channel table are charged as fixed-W costs. No exact real logarithms or numerical likelihood tolerances are required.

## 2. Explicit parameters, field, and inner code

Put

    k = ceil(log2(8B)),  q = 2^k,
    K = ceil(B/k),       n = 4K,
    ell = Ck,           d = ell/4.

Here k>=3, 8B<=q<16B, K<=B, and n<=4B<=q. Also k<=4B, so

    R=n ell=4CKk <=4C(B+k)<=20CB.                         (2)

All parameters are obtained by integer arithmetic. No asymptotic rounding qualification or exceptional small B is needed.

### 2.1 Field construction without an oracle

Enumerate monic binary degree-k polynomials in lexicographic coefficient order. For each candidate, test divisibility by every monic polynomial of degree 1 through floor(k/2), using binary polynomial long division. Accept the first passing candidate P. A reducible degree-k polynomial necessarily has an irreducible factor of degree at most k/2, so this is an exact test. Work in F=F_2[X]/(P), representing each field element by its k binary coefficients, with the corresponding integer label in {0,...,q-1}.

The only standard algebraic existence fact needed is that an irreducible binary polynomial of every positive degree exists. One elementary justification is as follows. In an algebraic closure of F_2, the roots of X^(2^k)-X form a field of exactly 2^k elements (derivative is -1, and Frobenius preserves sums/products/inverses). An element's degree over F_2 divides k. The elements with degree a proper divisor of k lie among the roots of X^(2^d)-X for such d<=floor(k/2). Their union has size at most sum_(d=1)^floor(k/2) 2^d<2^k for k>=2. Hence some element has degree k and its minimal polynomial is the required irreducible. Degree one is immediate.

There are q candidate polynomials and fewer than 2^(k/2+1) trial divisors per candidate. A conservative bound is O(q^2 k^2) bit operations and O(k) scratch bits for this search. Polynomial multiplication/reduction costs O(k^2), and Euclidean inversion has a conservative O(k^3) bit bound, with polynomial-in-k scratch space. No discrete logarithms or search for primitive elements are needed. Choose the n evaluation points x_i to be field labels 0,...,n-1.

### 2.2 A small exhaustive-search inner code

Enumerate length-ell binary words lexicographically. Retain a word iff its Hamming distance from every retained word is at least d, and stop when q words have been retained. Label them c_0,...,c_(q-1) according to retention order.

This always terminates. A maximal greedy set covers the cube by balls of radius d-1, each of volume

    V = sum_(j=0)^(d-1) binom(ell,j) <=2^(ell H_2(1/4)).

For a direct proof of this inequality, each j<ell/4 satisfies

    (1/4)^j (3/4)^(ell-j) >= 2^(-ell H_2(1/4));

retain those terms in the binomial probability sum, which is at most one. Therefore the maximal set has at least 2^(ell(1-H_2(1/4))) words. Since

    H_2(1/4)=2-(3/4)log2(3)<7/8

(the last inequality follows from 9>8), and ell=Ck>=8k, this cardinality is at least 2^k=q. Stopping at q is consequently legitimate.

There is no 2^B-entry message codebook. This inner table has only q ell=O_W(B log(B+1)) bits. Its brute-force construction takes at most

    O(2^ell q ell)=O(q^(C+1) Ck) bit operations,           (3)

and O(q ell+ell) workspace. The enumeration counter has ell bits; no 2^ell deletion bitmap is stored. The W-dependent polynomial exponent can be very large, but it is a polynomial in B, not in M when B=Theta(log M).

## 3. Encoding and exact inner decoding

Pad the B payload bits by zeros at the end to Kk bits, and interpret consecutive k-bit groups as coefficients f_0,...,f_(K-1) in F. Let f(X)=sum_(j=0)^(K-1) f_j X^j. For each i=1,...,n, evaluate s_i=f(x_i) and send c_(label(s_i)). This gives exactly n ell binary channel inputs. All block boundaries are fixed by B and W and convey no side information.

For each received inner block v in Y^ell, decode to the label maximizing

    L_b(v)= product_(j=1)^ell a_(c_b[j], v_j),

breaking ties by smallest label. This compares exact nonnegative integers because the common denominator D^ell cancels. Zero-probability outputs and all-zero likelihood ties use the same deterministic convention. Each likelihood has O(ell log(D+1)) bits; products and comparisons require no floating point.

For any transmitted inner word c and competitor c', the event that c' has likelihood at least c has probability at most

    sum_v sqrt(W^ell(v|c) W^ell(v|c'))
       = h^dist(c,c') <= h^(ell/4).

Indeed, on that event the true likelihood is bounded by the geometric mean; summing and memoryless factorization prove the claim even when some probabilities vanish. A union bound and (1) give, **for every transmitted field symbol**,

    p_inner <= q h^(ell/4)
             <=2^k (h_bar^(C/4))^k <=2^(-8k).             (4)

This maximal bound, rather than an average-message guarantee, is essential for arbitrary data-dependent payload distributions.

## 4. Outer decoding with complete correctness proof

The Reed-Solomon evaluation code has minimum distance n-K+1=3K+1: a nonzero polynomial of degree <K has at most K-1 roots among the n distinct points. We only need correction of t=K errors, which is strictly within its unique-decoding radius.

Given the hard inner decisions r_1,...,r_n, use Gaussian elimination over F to find a nonzero solution (Q,E) of the homogeneous system

    Q(x_i)=r_i E(x_i),       i=1,...,n,
    deg Q < 2K,             deg E <=K.                   (5)

There are 3K+1 scalar unknown coefficients and 4K equations. Choose the first nonzero nullspace basis vector using fixed pivot conventions. If the nullspace is zero, return the all-zero B-bit fallback. A nonzero solution always has E nonzero: otherwise Q has n roots and degree <2K<n, so Q=0 too.

Divide Q by E. Return the quotient's K coefficients only if division is exact, its degree is <K, its evaluation vector differs from r in at most K positions, and its final Kk-B padding bits are all zero. Otherwise return the fixed fallback. This defines the decoder on every received word, including more than K inner errors. Polynomial zero uses the conventional degree -infinity.

If there are e<=K inner symbol errors, the nonzero error-locator polynomial

    E_*(X)=product_(i:r_i!=f(x_i)) (X-x_i)

has degree e<=K, and Q_*=f E_* has degree <2K. Thus (5) has a nonzero solution. For **any** solution (Q,E), Q-fE has degree <2K and vanishes at all n-e>=3K good positions. It is therefore identically zero. Since E!=0, exact division recovers f, and all validation checks pass. This proof does not erroneously insist that E have degree exactly K or assume a unique nullspace vector.

## 5. Maximal concatenated error

Condition on any fixed B-bit payload, hence on the whole transmitted concatenated word. Fresh memoryless channel noise makes the n hard-inner error indicators independent; their probabilities need not be identical, but each is at most p=2^(-8k). The outer decoder fails only if at least K+1 errors occur. Union-bound over subsets of K+1 erroneous positions:

    Pr(message error | payload)
       <= binom(n,K+1) p^(K+1)
       <= 2^(4K-8k(K+1))
       <= 2^(-6kK-8k)
       <= 2^(-6B).                                      (6)

The penultimate inequality uses 4K<=2kK, valid because k>=3; the last uses kK>=B. Conditional independence is invoked only after fixing the payload. Unconditional independence under a random source/attack is neither true in general nor required. The bound survives averaging over every law of the payload, and over the pre-channel experiment because channel noise is fresh conditional on that experiment.

## 6. Explicit resource ledger

All bounds below are elementary bit-operation bounds; fixed-channel factors include |Y| and log(D+1). RAM-word improvements are unnecessary. Both endpoints can reconstruct the same field and inner table from the fixed deterministic algorithms, B, and W.

| Component | Bit time | Charged storage/workspace |
|---|---:|---:|
| Certified W constant selection | finite constant depending only on W | O_W(1) |
| Field search | O(q^2 k^2) | O(k), plus polynomial-arithmetic scratch |
| Inner table construction | O(q^(C+1) Ck) | O(q ell) |
| Outer encoding via Horner | O(nK k^2) | O(Kk+k), excluding inner table |
| Writing/looking up inner words | O(n q ell) suffices even with sequential table scans | O(ell), excluding table/payload |
| Inner exact ML over all blocks | O_W(n q ell^3) conservative | O_W(ell) score/block scratch, plus table and nk hard decisions |
| Outer linear system and elimination | O(n^3 k^3), including setup within this bound | O(n^2 k), plus polynomial-in-k scratch |
| Quotient and validation | O(nK k^3) conservative | O(nk+Kk), within preceding bound |
| Output decoded B-bit payload | O(B) | O(B) |

In particular, preprocessing is poly_W(B); online coding time and full charged design/auxiliary storage are poly_W(B). The latter explicitly includes the inner table, linear system, field representation, likelihood arithmetic, received inner block, hard decisions, payload, and output serializer. The entire length-R channel-output string can instead be stored at additional O_W(B) bits; streaming inner blocks avoids even that optional buffer.

An explicit design consists of P, the q-word inner table, parameters, and rational W; its length is O_W(B log(B+1)). A uniform algorithmic description is shorter, but we **do not** use short description as an excuse to omit generation time or stored table memory. Evaluation points are generated by their k-bit labels rather than a large matrix. If sequential-tape details require additional addressing/scan overhead beyond these conventional arithmetic-operation bounds, such overhead remains polynomial in B; no exponential random-access table is hidden.

For h=0, direct coding has R=B, O_W(B) encoding/decoding time, and O_W(B) workspace (or smaller streaming buffers), without this preprocessing. Identical-row channels are excluded; the whole-message impossibility proof for them is unchanged.

## 7. Instantiation in the exact-gate first-order experiment

Use the same source/attack/target and no-free-side-information experiment as `../whole_message_cost/CANDIDATE.md`: the encoder observes only the complete corrupted binary word Z_0,...,Z_(M+1), while the receiver obtains only the channel outputs and fixed public parameters M,W. No counts, endpoint, law, budget, or data-dependent seed are free.

Discard the first edge and count transitions with departure i=1,...,M. Maintain four transition counters N_(u,v), two half-departure counters A_u (i<=floor(M/2)), the previous/current bits, and an index. One forward pass reading M+2 symbols suffices. After the last bit t=Z_(M+1), compute

    J=N_(t,0)+N_(t,1), C_flip=N_(t,1-t),
    G=1{512 A_t>=J},
    payload=(J,C_flip,t,G), B=2 ceil(log2(M+1))+2.

Both rows are counted before the terminal row is selected; no random access to the original word is required. Counter additions, comparison by the fixed factor 512, and terminal selection take O(M log M) bit time and O(log M) auxiliary bits, plus exactly one input scan of M+2 symbols. Use the name C_flip here to distinguish the flip count from the channel-code constant C.

Decode the payload, verify fixed-width counts (0<=C_flip<=J<=M) and bits, and output a fixed distribution on malformed payloads. For valid payloads with J>0 and G=1, the next-bit distribution is

    t=0: (Pr(0),Pr(1))=((J-C_flip)/J, C_flip/J),
    t=1: (Pr(0),Pr(1))=(C_flip/J, (J-C_flip)/J).

Otherwise output the point mass at t, as the original payload rule prescribes. Exact output is a pair of integer numerators and a common denominator: J in the active branch and 1 in the fallback branch. Serialization costs O(log M) bits/time and does not perform unbounded-precision division or require a decimal expansion.

By the previously accepted exact-gate predictor bound (the dependency, not reproved here), the uncoded predictor has risk at most C_g g_M(k_attack), where C_g=1024+2^20 and g_M(k_attack)=max(M^(-1/2),k_attack/M). Couple coded and uncoded predictors. Their predictions coincide on successful payload decoding; on failure TV loss is at most one. Equation (6), and B>=2 log2(M+1), imply

    risk <= C_g g_M(k_attack)+2^(-6B)
          <= (C_g+1) g_M(k_attack).

Thus the earlier Theta_W(log M) whole-message communication order is achievable without polynomial-in-M channel-code preprocessing/storage. The new fully charged bounds are

    physical communication: O_W(log M),
    preprocessing:          poly_W(log M),
    sample processing:      O(M log M)+poly_W(log M) bit time,
    design + auxiliary:     poly_W(log M) bits,
    raw-input I/O:          one pass, M+2 symbols.

If all raw input bits are kept resident and counted, add M+2 bits to storage. This construction supplies a polylogarithmic auxiliary-space procedure, not an O(log M)-total-space procedure: in particular the BW matrix and inner table are larger than logarithmic in general.

## 8. Provenance, limits, and review status

The finite greedy-distance argument and polynomial-evaluation decoder are standard ingredients. For orientation, see Anup Rao's [Lecture 2, More limits on codes](https://homes.cs.washington.edu/~anuprao/pubs/codingtheory/lecture2.pdf) for the greedy Gilbert-Varshamov method, and [Lecture 4, Reed-Solomon Codes](https://homes.cs.washington.edu/~anuprao/pubs/codingtheory/lecture4.pdf) for Reed-Solomon evaluation and the Welch-Berlekamp decoding approach. The specific parameter choices, maximal-error calculation, exact-arithmetic algorithms, and accounting used here are given explicitly above; no black-box efficient-capacity theorem is required.

The statistical payload and accepted source-risk bound are inherited only from the dependencies enumerated in the whole-message candidate. Its information lower bound and identical-row impossibility are unaffected. This note does not strengthen the supplemental-gate experiment, which gives counts and endpoints for free.

Fixed arbitrary real W with distinct rows still permits the statistical construction, but the exact rational computation theorem does not extend without a representation/access model. Constants and polynomial exponents may diverge as W approaches identical rows. This is an asymptotic feasibility repair, not evidence that exhaustive inner search is practically efficient, nor a claim of optimal leading channel-use constants.

Status: explicit mathematical construction, not executable implementation or benchmark. No claim is made that the algorithms above have been run. Independent adversarial review remains required before promotion.
