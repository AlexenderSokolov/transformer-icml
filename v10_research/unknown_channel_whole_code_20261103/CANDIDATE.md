# UWC001 — efficient whole-message prediction over a hidden TV-ball channel

2026-11-03. New local author candidate, pending independent review and root acceptance. This unit follows published stage `612b76d` and is NOT included in that release. No released artifact or external repository is changed. Historical pending labels inside imported candidates are superseded only by their explicit root receipts.

## 1. Result

Fix a finite nonempty output alphabet Y, known rational nominal probability rows P0,P1, and known rational α≥0, all independent of sample size. Write d=TV(P0,P1) and

    Uα={W=(Q0,Q1): TV(Qb,Pb)≤α for b=0,1}.

Neither endpoint knows true W. It is fixed during an experiment and fresh memoryless conditional on the complete pre-channel experiment. The true probabilities can be arbitrary real numbers.

**Robust coding lemma.** If 0≤α<d/2, put γ=d/2−α and m0=ceil(4/γ²). For every integer B≥1 a deterministic uniformly constructible code transmits any B-bit message with exactly R≤240m0B physical binary-input uses and maximal message error ≤2^(-6B), uniformly over W∈Uα. Preprocessing, encoding, decoding, explicit design and auxiliary space are polynomial in B. Exhaustive inner-code search costs O(B^13 log(B+1)), with a universal power independent of γ; all remaining polynomial powers are universal as well. Fixed nominal/radius-dependent factors, including m0, are charged.

For either statistical class in §2, with NO free counts or endpoint/query, B=2ceil(log2(M+1))+2 yields total physical communication Θ_(P0,P1,α)(log M) for bounded g_M-adaptation whenever 0≤α<d/2. Coding resources are poly(log M), the complete input scan costs O(M log M) bit time, and resident raw input adds M+2 bits. If α≥d/2, including equality, or if d=0, robust clean risk is at least 1/8 regardless of any finite length schedule. Thus bounded normalized adaptation is impossible there.

This is an elementary robust modification of the accepted PMC001 concatenation, not a new general coding method, optimal-constant theorem, practical implementation or neural claim. A bounded-factor length order means some feasible constant independent of M, not every arbitrarily small prescribed factor.

## 2. Exact observation model and two distinct statistical classes

For M≥64, the clean word is X_0,...,X_(M+1), and Z is its corrupted version. A single source-independent offline Markov attack kernel on ALL words changes at most k positions among 0,...,M−1 on every outcome and preserves both terminal symbols. Here k∈{0,...,M} is hidden. The kernel cannot see predictor seeds or later channel noise. One procedure must work for all sources, starts, budgets and legal kernels.

**F: unrestricted binary first order.** An arbitrary initial PAIR law is followed by a hidden homogeneous first-order transition table; the initial edge need not follow that table. Target is the next-symbol law selected by actual protected X_(M+1). The accepted FOT002 repaired suffix gate discards the first edge. The upper covers all first-order tables without mixing. Restricting to the all-state pair certificate 1/M preserves the result because the lower IID family belongs to that subclass.

**O2: binary order two with critical all-state certificate.** Write Y_i=(X_i,X_(i+1)). A homogeneous hidden θ_ab(c) has a stationary Π with P²(u,v)≥Π(v)/M for EVERY pair u,v, including unsupported rows. Every initial pair law, including starts outside stationary support, is allowed. Target is the next-SYMBOL law θ_(Y_M). The certificate supplied is 1/M, not necessarily optimal. Use the original order-two half gate, not F's suffix gate. There is no unrestricted/no-mixing order-two or all-β assertion.

The encoder sees only the full corrupted word. The receiver gets M, nominal rows/radius, fixed class convention and algorithms, the R channel outputs, and optionally independent shared seeds. NO counts, endpoint, raw windows, query, hidden table/start/budget/W, edit locations or path-dependent seeds are free. All sample-dependent information must travel through the fixed R binary inputs. Private/public randomness may be independent of the source; the upper is deterministic. There is no calibration data, feedback, timing, variable/adaptive length, seed revelation or other ancillary channel. Conditional on the entire pre-channel experiment and independent seeds, noise is W^R for one fixed hidden W; W is not selected adaptively from current inputs/seeds.

Loss is unconditional expected unsquared TV at the actual protected terminal next-symbol target. Set

    g_M(k)=max{M^(-1/2),k/M},
    Γrob,total,j(M,R)=inf_(one E,D) sup_(W∈Uα,source,start,k,kernel)
                       risk_W(E,D)/g_M(k), j∈{F,O2}.

The infimum is outside the joint supremum; no minimizer or minimax interchange is assumed. Accepted WMC001/PMC001 and O2T001 supply the respective exact-payload bounds

    F: 1024/√M+2^20 k/M ≤ G_F g_M(k), G_F=1024+2^20;
    O2: 2^17/√M+2^23 k/M ≤ G_O2 g_M(k), G_O2=8519680.

These statistical theorems, with their source restrictions, are imported dependencies, not rederived from channel coding.

## 3. Nominal-only robust primitive

Assume 0≤α<d/2. From known rows define

    A={y:P1(y)>P0(y)}, p_b=P_b(A),
    p1−p0=d, τ=(p0+p1)/2, γ=d/2−α>0.

The event identity follows by summing positive differences. TV's event bound gives for all W∈Uα

    q0=Q0(A)≤τ−γ, q1=Q1(A)≥τ+γ.                    (1)

Repeat an input bit b exactly m0=ceil(8/(2γ²))=ceil(4/γ²) times. Decode as 1 iff the number T of outputs in A satisfies T≥m0τ. Conditional on any pre-channel state and transmitted bit, the indicators are independent Bernoulli(q_b), hence

    Pr(hard bit error | state,b,W)≤exp(−2m0γ²)
       ≤exp(−8)<2^-8=:p*.                           (2)

Ties are assigned to 1: the bit-0 error is the closed upper tail; bit-1 error is contained in the closed lower tail. For completeness, Hoeffding's bound here follows by f(t)=ln E exp(t(Z−EZ)) for a Bernoulli Z. We have f(0)=f'(0)=0 and f''(t), a tilted Bernoulli variance, ≤1/4. Taylor's integral remainder gives f(t)≤t²/8 for both signs of t. Multiply these moment bounds across trials and use exponential Markov with t=±4γ, obtaining exp(−2m0γ²). Finally ln256=8ln2<8.

Disjoint primitive blocks give independent hard-bit errors CONDITIONAL on the full input word and fixed W. Errors may be asymmetric, depend on the bit, or have probability zero. Their unconditional independence from a random path is not claimed. No true-W likelihood, training or estimation is used.

## 4. Explicit inner code and nearest-Hamming decoding

For every B≥1 set

    k_c=ceil(log2(8B)), q=2^k_c, K=ceil(B/k_c), n=4K,
    ell=12k_c, distance threshold Δ=ell/4=3k_c.

The coding symbol length k_c is not the attack budget k. We have k_c≥3, 8B≤q<16B, K≤B, n≤4B≤q and k_c≤4B. All parameters are computed by integer arithmetic/bit lengths.

Enumerate length-ell binary words lexicographically, retaining a word iff its Hamming distance from every retained word is at least Δ, and stop at q words c_0,...,c_(q−1). To see termination, a maximal such set covers the cube by balls of radius Δ−1, whose volume

    V=Σ_(j<ell/4)binom(ell,j)≤2^(ell H_2(1/4)).

For each retained j, (1/4)^j(3/4)^(ell−j)≥2^(−ell H_2(1/4)); substitute this into the binomial probability sum to prove the displayed bound. Since H_2(1/4)=2−(3/4)log2 3<7/8 (equivalent to 9>8), a maximal greedy set has at least 2^(ell(1−H_2(1/4)))>2^(ell/8)≥q words. No exponential-size deletion bitmap is required.

Send each bit of an inner word via §3. Decode the resulting ell hard bits z to the nearest codeword in Hamming distance, with smallest-label tie-break. This uses no unknown channel information.

For transmitted c and competitor c' at distance s≥ell/4, agreeing coordinates cancel in the distance comparison. If E is the number of hard-bit errors among their s disagreement positions, binary outputs imply

    dist(z,c')≤dist(z,c) iff s−E≤E iff E≥ceil(s/2).

Let r=ceil(s/2). Union-bound over subsets of r erroneous disagreement positions, using conditional independence and (2):

    Pr(c' at least as close as c)
       ≤binom(s,r)(p*)^r≤2^s(p*)^(s/2)=8^(−s).

This includes odd s, adverse ties, asymmetric errors and zero-probability rows. An incorrect nearest-neighbor decision implies one competing event. Thus for EVERY transmitted label and W,

    p_inner≤q 8^(−ell/4)=2^k_c 2^(−9k_c)=2^(−8k_c).    (3)

This is maximal conditional error, not an average-message assertion. Known-W ML is neither needed nor admissible as a substitute.

## 5. Explicit field, outer encoder and decoder

Construct F_(2^k_c) as follows. Enumerate monic binary degree-k_c polynomials and accept the first not divisible by any monic polynomial of degree 1,...,floor(k_c/2), testing by binary long division. Reducibility implies a factor of degree at most half, so this is exact. An irreducible of every degree exists: roots of X^(2^k_c)−X in an algebraic closure form a field of exactly 2^k_c elements (derivative −1 and Frobenius closure). Elements of proper degree dividing k_c are among roots of X^(2^j)−X for 1≤j≤floor(k_c/2), whose union has size ≤Σ_j2^j<2^k_c. Some element therefore has degree k_c and its minimal polynomial suffices. Degree one is immediate; here k_c≥3.

Represent field elements by k_c binary coefficients modulo this polynomial. Choose n distinct evaluation points with integer labels 0,...,n−1. Pad the B-bit payload by zeros to Kk_c bits; use its groups as coefficients of f(X), deg f<K. For each point x_i transmit c_label(f(x_i)), with every bit repeated m0 times. Boundaries are fixed by public parameters, not sample-dependent delimiters. Total length is

    R=m0 n ell=48m0 Kk_c≤48m0(B+k_c)≤240m0B.          (4)

After primitive and inner decoding let r_i∈F be the n field decisions. The evaluation code has distance n−K+1=3K+1 by the polynomial root bound. Correct up to K errors with the homogeneous Welch–Berlekamp system

    Q(x_i)=r_i E(x_i), i=1,...,n,
    deg Q<2K, deg E≤K.                              (5)

There are 3K+1 unknown coefficients and 4K equations. Gaussian elimination with fixed pivots selects the first nonzero nullspace basis vector; if none, return all-zero B-bit fallback. Any nonzero solution has E≠0, because otherwise Q has n roots and degree <2K. Divide Q by E, accepting only an exact quotient of degree <K, within K evaluation discrepancies of r, with the final Kk_c−B padding bits all zero. Otherwise return fallback. This defines the decoder on every output.

If e≤K inner errors occurred, the locator E_*=∏_(i:r_i≠f(x_i))(X−x_i), degree e≤K, and Q_*=fE_* give a nonzero solution. For ANY solution, Q−fE has degree <2K and vanishes at n−e≥3K good points, so is zero. The quotient is exactly f and every check passes. The proof neither fixes deg E=K nor assumes a unique nullspace vector.

Condition on any transmitted payload and fixed W (or the full pre-channel experiment). Inner error indicators are independent over n disjoint blocks and each ≤p=2^(−8k_c), not necessarily identically distributed. Failure requires at least K+1 errors. Hence

    Pr(message error | payload,W)
       ≤binom(4K,K+1)p^(K+1)
       ≤2^(4K−8k_c(K+1))
       ≤2^(−6k_cK−8k_c)≤2^(−6B).                   (6)

Use 4K≤2k_cK and k_cK≥B. Every step applies at B=1. Averaging over arbitrary sample/attack-induced payload laws preserves (6), proving the coding lemma.

## 6. Paid payloads and prediction risk

Let L=ceil(log2(M+1)), B=2L+2: two L-bit count fields and two single bits. These are sufficient widths, not a minimal-description claim.

**F payload.** Count departures i=1,...,M, discarding the initial edge. For u∈{0,1}, let J_u count departures from u, C_flip,u count such departures followed by 1−u, and A_u count departures from u with i≤floor(M/2). At final t=Z_(M+1), set J=J_t, C_flip=C_flip,t and G=1{512A_t≥J_t}; transmit

    (J,C_flip,t,G).

The receiver sets qhat=C_flip/J if J>0 and G=1, otherwise qhat=0. Symbol-1 probability is qhat for t=0 and 1−qhat for t=1. Rejection predicts t, not a universal constant symbol. This is exactly the accepted repaired suffix predictor with arbitrary initial pair.

**O2 payload.** For u=(a,b) put direction d(u)=1−a. With i=0,...,M−1 define J'_u as pair-departure count, C'_u as departures from u whose following symbol Z_(i+2)=d(u), and A'_u as departures from u at i=0,...,floor(M/2)−1. Use BOTH protected symbols to select u=(Z_M,Z_(M+1)) and transmit

    (J,C,direction,G)=(J'_u,C'_u,1−Z_M,1{512A'_u≥J'_u}).

The receiver sets qhat=C/J if J>0 and G=1, otherwise 0; symbol-1 probability is qhat when direction=1 and 1−qhat when direction=0. Thus rejection predicts the complement of direction. The orientation bit is paid even on rejection. The receiver does not need the second endpoint coordinate after the encoder selected the row; the encoder did need it. This claim concerns next-symbol, not next-pair prediction.

In both models validate 0≤C≤J≤M; invalid decoded fields receive any fixed distribution. At J=0 the denominator test returns zero even if G=1. Gate equality is accepted. Successful message decoding reproduces the accepted exact-payload predictor. Couple these two predictors; TV loss lies in [0,1], so uniformly in W and all statistical instances,

    risk_W≤G_j g_M(k)+2^(−6B)≤(G_j+1)g_M(k).           (7)

Here B≥2log2(M+1) implies 2^(−6B)≤M^(−1/2). Output rational numerators with denominator J or 1; an infinite decimal expansion is unnecessary.

## 7. Input-cardinality lower and exact impossibility boundary

Both classes contain clean stationary IID Bernoulli(p), p∈I=[1/4,3/4]. Its next-symbol target is p independently of endpoint; its pair chain has P²(u,v)=Π(v) on every row, satisfying the O2 certificate. Use identity corruption and k=0.

Fix any W∈Uα and protocol. There are at most Q=2^R physical input labels. Conditional on independent shared seed, channel plus receiver is a p-independent kernel from each input label h to prediction A∈[0,1]. Draw counterfactual reconstruction A_h from that kernel for each label, independently of p and sample; selecting actual A_H has the correct marginal law. Freeze the seed and reconstructions. All possible predictions belong to a set S of at most Q points independent of p, even for arbitrary sample-dependent randomized selection H. Pointwise |A_H−p|≥dist(p,S).

Intervals of radius v around S cover at most 2Qv of I. Layer cake under uniform p gives

    E_p dist(p,S)≥∫_0^(1/(4Q))(1−4Qv)dv=1/(8Q).

Average the frozen randomness. For every protocol some clean fixed p has risk ≥1/(8·2^R). This is valid for any fixed W, in particular nominal W0∈Uα, and therefore

    Γrob,total,j(M,R)≥√M/(8·2^R).                       (8)

A uniformly bounded factor C requires R≥(1/2)log2 M−log2(8C), also for infima by approximation. The cardinality is of binary INPUT labels, not finite output strings. Unknown W, encoder coins and independent public randomness do not invalidate it. It applies at α=0, even for disjoint nominal supports. Combining (4),(7),(8) gives Θ(log M) on the entire strict-gap region.

For α≥d/2 choose Qmid=(P0+P1)/2. Since TV(Qmid,Pb)=d/2, the identical-row Wmid=(Qmid,Qmid) lies in Uα, including equality. Its outputs and receiver action are independent of p conditional on independent seeds. For uniform p∈I every fixed prediction a has E|a−p|≥|I|/4=1/8; independent randomization cannot improve this. Thus robust clean risk≥1/8 and factor≥√M/8 for EVERY finite R(M). If d=0, nominal W0 is already identical-row for every α≥0. Conversely TV(Q0,Q1)≥d−2α by the triangle inequality, so the strict positive-gap region matches the constructive test exactly.

This no-free-information obstruction is not a statement about equality to the supplemental counts-only baseline: that is a different experiment which gives information away.

## 8. Exact precision and fully charged resources

Nominal rows and α are fixed rational objects. Compute d,A,τ,γ,m0 by exact rational/integer arithmetic once. If τ=a/D, hard decoding compares D T with m0 a. Count m0 physical outputs using O(log(m0+1)) bits and O(m0 log(m0+1)) naive bit operations per primitive, plus fixed nominal arithmetic factors. Membership in A uses a fixed finite lookup and the fixed finite alphabet encoding. These potentially large costs are charged; they are constant in B, not free. No numerical operation, input representation or oracle concerning arbitrary-real true Qb is needed.

Conservative ledger, with q=O(B), k_c=O(log(B+1)), ell=12k_c:

| Component | Bit time | Design/auxiliary storage |
|---|---:|---:|
| Nominal preparation | fixed nominal/radius cost | fixed nominal/radius cost |
| Field search | O(q² k_c²) | polynomial in k_c |
| Greedy inner table | O(q^13 ell) | O(q ell), no cube bitmap |
| Outer Horner encoding | O(nK k_c²) | O(Kk_c), plus table |
| Sequential inner lookup/write | O(nq ell)+O(m0 n ell) | O(ell), plus table |
| Hard primitive decoding | O(n ell m0 log(m0+1)), times fixed nominal arithmetic factor | O(ell+log(m0+1)) |
| Nearest-Hamming decoding | O(nq ell log(ell+1)) conservative | O(ell), plus table and nk_c decisions |
| Outer matrix/elimination | O(n³ k_c³) conservative | O(n² k_c), plus arithmetic scratch |
| Quotient/validation | O(nK k_c³) conservative | within preceding matrix bound |

Field multiply/reduction is O(k_c²), conservative Euclidean inversion O(k_c³). The irreducible search has q candidates and fewer than 2^(k_c/2+1) possible trial divisors. Greedy search enumerates at most 2^ell=q^12 candidates and compares each against at most q retained words. The exponent 13 has a logarithmic factor: O(B^13 log(B+1)), NOT a claimed strict O(B^13). An integer-polynomial upper O(B^14) removes the log with no channel-dependent powers.

The explicit design includes field polynomial, q-word table, parameters and rational nominal/radius description: O(B log(B+1)) plus fixed constants. Full charged workspace additionally includes payload, received hard block, nk_c decisions and O(n²k_c) matrix; it is polynomial in B, not generally linear. A short generating program does not waive generation time or stored table/matrix memory. Sequential addressing overhead remains polynomial. No full implementation or benchmark is claimed.

Payload formation is one M+2-symbol pass. F keeps four transition and two half-departure counters, position and rolling bits, skipping the first edge. O2 keeps eight triple and four half-pair counters, position and rolling bits. Both select the terminal row at the end. This costs O(M log M) bit time and O(log M) counter space; all M+2 input-symbol reads are included. Every R channel-output read is also included in the coding cost. Thus

    communication:             O_(nominal,α)(log M);
    coding preprocessing/time: poly_(nominal,α)(log M);
    sample plus coding time:   O(M log M)+poly_(nominal,α)(log M);
    design plus auxiliary:     poly_(nominal,α)(log M).

A read-only/streamed input need not be copied. If resident raw input is charged, ADD M+2 bits: total resident storage is Θ(M)+poly(log M), NOT polylogarithmic. m0 diverges as γ↓0 and may be enormous, but is a fixed charged factor rather than a hidden message or channel-dependent polynomial power.

## 9. Sources, limitations and disposition

Read in full: `../resumption_20261103/efficient_message_code/CANDIDATE.md` and `ROOT_ACCEPTANCE.json` (PMC001), `../resumption_20261103/whole_message_cost/CANDIDATE.md` and receipt (WMC001), and `../resumption_20261103/order_two_transfer/CANDIDATE.md` and receipt (O2T001). PMC supplies the standard small-inner-code/RS/Welch–Berlekamp architecture and exact arithmetic framework; WMC supplies the first-order paid statistical payload and input-cardinality argument; O2T supplies the separately restricted order-two bound, paid orientation and IID inclusion. All coding correctness needed here is explicitly reproved. The load-bearing change is nominal-only hard decoding then nearest Hamming, not unknown-W ML. FOT002 and the positional statistical manuscript remain accepted dependencies through these interfaces, not proofs independently rederived here.

`../channel_uncertainty_20261103/CANDIDATE.md` (UMC001) was read for the hidden-channel model and nominal-event idea. Its supplemental classification is NOT needed as an accepted theorem: the required test and midpoint obstruction are proved above. `SOURCE_BINDINGS.json` binds exact read artifacts and verifies candidate hashes against the three accepted root receipts. It does not confer acceptance on this new candidate or on UMC by association.

Independent analytic review must check maximum conditional errors, ties/odd distances, asymmetric rows, conditional independence, all-B rounding, RS fallback/padding checks, both payloads, no-free-query lower, exact midpoint and resource charges. Finite checks can corroborate but not replace universal proofs. This note is a mathematical construction, not a complete executed code implementation, formal verification or external peer review.

Excluded: unknown nominal/alphabet, M-dependent radius/channel, calibration, adversarial/correlated/adaptive channel noise, feedback, variable/adaptive length, free counts/query/path-dependent seeds, unrestricted order-two/all-β or next-pair/general-order claims, neural realization, learnability, optimal constants, practical speed and novelty certification. No external publication, repository writes, manuscript edits, permissions, licenses or deployment changes were made. Separate review and root acceptance remain required.
