# BT001 — binary renewal transport: exact obstruction and conditional reduction

2026-11-02. POST-STAGE7 exploratory work. **No binary logarithmic corruption lower is proved.** Accepted/frozen sources are untouched. Numerical LP evidence is not an asymptotic theorem. Fresh review requested.

## Result first

1. For uniform words formed by short cycles S=01 and long cycles L=101, the proposed count transport cannot have expected Hamming cost O(|Δl|) uniformly over all counts. At horizon t=2s+6, transport from (s,2) to (s+3,0) has exact optimal cost **t/3+1**.
2. A modified binary stationary source realizes this renewal reference with the desired cutoff e=max(sqrt(beta),1/M); its all-state two-step certificate is proved below. This modification is not the already accepted BI001 witness.
3. An interior expected-cost transport theorem WOULD suffice for a common source-independent strict-budget corruption kernel and common-prior harmonic lower. The exact sufficient theorem and reduction are recorded; the transport theorem itself remains open.
4. Small finite LPs support interior bounded mean cost, but neither certify uniform asymptotics nor a strict budget. The failed adjacent-long deletion rule is preserved explicitly.

## 1. Exact microcanonical model and boundary obstruction

Let U_(s,l) be uniform over the binomial(s+l,l) cycle orders containing s copies S=01 and l copies L=101. Their emitted words have t=2s+3l bits and uniquely decode because {01,101} is prefix-free. Each is a reference path starting in pair A=01 and ending in A. The last two emitted bits are always 01.

For l=2 write the word S^g0 L S^g1 L S^g2, where (g0,g1,g2) is uniform over weak compositions of s. The only possible target under U_(s+3,0) is S^(s+3). Before the first L and after the second L the words align. Direct comparison of L S^g1 L with S^(g1+3) gives exactly 2g1+3 bit disagreements. Exchangeability gives E g1=s/3. Thus every coupling has cost 2s/3+3=t/3+1. No source-independent randomization can improve a coupling to a point mass.

This is NOT a counterexample to interior transport with s,l both proportional to t. Under p bounded away from 0 and 1, l=2 is an exponentially rare boundary event. It does show that tail handling cannot be silently omitted as in IID one-erasure.

## 2. Failed local replacement, preserved

Encode a general word by gaps g0,...,gl of S cycles between L cycles, with sum g_i=s; these gaps are a uniform weak composition. Select uniformly one of the l-1 consecutive pairs in the ordered list of L cycles (allowing S cycles between them), and replace L S^r L by S^(r+3). The operation costs exactly 2r+3 edits and gives counts (s+3,l-2).

If h=(h0,...,h_(l-2)) is the output gap vector, the number of preimages for a merge at coordinate i is binomial(h_i-1,2), interpreted as zero for h_i<3. Hence its output density relative to uniform target is proportional to

    D(h)=sum_i binomial(h_i-1,2).

D is generally nonconstant. The expected operation cost is 3+2s/(l+1), bounded in the interior, BUT its target marginal is not U_(s+3,l-2). Repeating this map and treating count alone as sufficient would be invalid. Example source (s,l)=(1,3): target gaps have total4 in two coordinates; D(4,0)=3 but D(2,2)=0. This is not repaired merely by observing bounded average edit cost.

## 3. Modified stationary witness with renewal reference

Let M>=64, 0<=beta<=1/256, a=1/(2M), e=max(sqrt(beta),1/M), p in [1/4,3/4]. For W=00,A=01,B=10,C=11 use

    theta_W(1)=a, theta_A(1)=p,
    theta_B(1)=1-e, theta_C(1)=e.

Set x=(e/a+2+p/(1-e))^-1 and Pi=x(e/a,1,1,p/(1-e)). Direct balance verifies stationarity. Since e/a>=2 and 2+p/(1-e)<=2.8, Pi_W>=2/4.8>1/4. Also x<=a/e. The two-step matrix is

    [(1-a)^2, (1-a)a,       a(1-p),          ap]
    [(1-p)e,  (1-p)(1-e),   p(1-e),          pe]
    [e(1-a),  ea,           (1-e)(1-p),      (1-e)p]
    [e(1-e),  (1-e)^2,      e(1-e),          e^2].

Here a<=1/128, e<=1/16, beta<=e^2 and beta<=e/16. For target W every entry is >=beta (use (1-p)e>=e/4, e(1-e)>=15e/16). For target A, the exceptional ea>=beta a/e>=beta x; all other entries dominate beta x, using (1-a)a>=beta a/e and the constant lower bounds. For B, row W is a(1-p)>=a/4>=beta a/e; row C is e(1-e)>=beta>=beta x; others have fixed positive lower bounds. For C, row W satisfies ap>=beta p a/[e(1-e)]>=beta Pi_C because e(1-e)>=beta; rows A and B satisfy pe,(1-e)p>=beta p x/(1-e); row C has e^2>=beta>=beta Pi_C. Thus P²(s,t)>=beta Pi(t) for every pair, with no off-support exception.

Initialize at Pi. Reference R on A,B,C has A→B with1-p, A→C withp, B→A and C→B deterministic. For E_j consisting of N-j initial zeros, a first1, then j-1 reference transitions, actual path density relative to the reference law is

    Pi_W (1-a)^(M-j) a (1-e)^(N_B+N_C).

For j<=1/(4e), this is >=1/(32M), using Pi_W>=1/4, (1-a)^M>=1/2, and (1-e)^j>=3/4. E_j are disjoint. Their probabilities need not be p-independent: use pathwise domination and the SAME uniform prior on [1/4,3/4]. At terminal A the true prediction target is Bernoulli(p).

Reference return cycles are precisely S,L. Conditional on terminal A and counts (s,l), their order is U_(s,l), since each has likelihood (1-p)^s p^l. Moreover R^5(u,A)>=1/16 for every u: the entries for u=A,B,C are respectively 2p(1-p),(1-p)^2,p. Hence P(terminal A)>=1/16 for every j-1>=5.

There are absolute eta>0 and j0 such that, uniformly in p and j>=j0, the event terminal A AND s,l>=eta(j-1) has probability >=1/32. To see this, expose IID cycle choices. At time t=j-1 at least floor(t/3) cycles have completed. Among those first n choices both cycle types occur at least n/8 except with probability <=2 exp(-n/32), by the Bernoulli Hoeffding bound at p in [1/4,3/4]. For large enough absolute j0, n/8>=t/32 and the failure probability is <=1/32. Take eta=1/32 and subtract from the terminal probability. This is a genuine tail step, not conditional IID of the fixed-time suffix.

## 4. Sufficient missing transport theorem

For every fixed eta>0, does there exist C_eta<infinity such that for every integer s,l with t=2s+3l and s,l>=eta t, l>=2, there is a coupling

    X~U_(s,l), Y~U_(s+3,l-2), E d_H(X,Y)<=C_eta ?       (T)

Both source and target are finite known distributions. A coupling is selected once for each public count pair, with no p input. Arbitrary computation is allowed. It is enough to prove (T) for a smaller fixed eta covering intermediate counts. No pointwise bounded-cost assertion is required.

**Conditional consequence:** (T) implies a corruption lower of order

    (k/M) [1+ln(1+1/(e k))]

up to absolute constants, supplemented by the clean M^-1/2 lower; not an established result until (T) is proved.

Here are the essential quantifiers and proof. Enlarge C_eta to at least 1. Choose b=floor(k/(128 C_eta)), restricting first to k large enough that b>=1. On a terminal-A reference-shaped word read t, s,l and parity r=t mod2. Quantize h=(l-r)/2 down to h0=b floor(h/b); let l0=r+2h0. Compose at most b-1 couplings (T) to reduce l to l0 and increase s by 3 per step. If s,l>=2eta t and t>=2b/eta, every intermediate count has s,l>=eta t, so the composition has expected Hamming cost at most C_eta b. Output its sampled target if its Hamming distance from the ORIGINAL word is <=k; otherwise leave the original word unchanged. Outside the indicated patterns/count range the kernel is identity. Thus the kernel is defined on all binary words, uses no p, changes at most k positions, and preserves the exact final pair. Its attack random seed is private; the decoder's own independent/public randomness remains permitted.

The ideal untruncated output, conditional on eligibility and (t,l0), is exactly U_(s0,l0), independently of p, even after mixing all original counts in the cell. For fixed j there are at most D_j=1+t/(2b) possible l0 labels. The actual and ideal output differ with probability <=C_eta b/k<=1/128 on any eligible original microcanonical class. Endpoint-A interior input mass is >=1/32 for large j; choose the eta used in (T) as half of the eta in §3. Therefore good retained ideal mass is at least 3/128. A finite-message covering argument with ONE uniform parameter prior gives reference risk >=c/D_j: fix independent randomization generating each ideal arrangement and decoder output; the union of D_j radius-delta intervals has prior mass <=2D_j delta/|I|. Take delta a sufficiently small absolute multiple of1/D_j, then subtract the truncation/interior bad mass. For a fully explicit seed construction, draw original counts first, generate the ideal arrangement from an independent uniform seed using its common target law, then reverse-sample the original arrangement from the chosen coupling conditional on those counts and that ideal arrangement. The reverse coupling depends on counts, not p. This reproduces the original joint coupling, including its possibly seed-dependent truncation event; that event is controlled only by its total probability. No posterior is claimed uniform after endpoint or count conditioning.

The same prior and the same full-history kernel work for every j. Sum pathwise-dominated reference losses for

    max(j0, 1+ceil(2b/eta)) <= j <= floor(1/(4e)).

The sum is >=c(k/M) ln(1/(C e k)) when that logarithm is sufficiently positive. The independent IID corruption lower c k/M supplies the baseline and covers the complementary bounded-log regimes, and a clean two-point lower supplies c/sqrt(M). Constants and bounded k can be absorbed into these baseline bounds. This produces the stated profile if (T) holds; the upper is SC003, not established here.

## 5. Why a fixed two-point common attack is not the missing harmonic proof

An attack constructed for one pair p_-,p_+ has one target separation delta. It cannot simply be reinterpreted as a lower of size k/j at every suffix length j, because that would require choosing a new source pair for each j. The source supremum is outside the unconditional sum. Taking sup separately at each j reverses the valid inequality. A common mixture of two attacks can fix source-independence for that ONE pair, but does not supply a common continuum prior and exact count-cell factorization. This note does not claim a general impossibility theorem for all two-point arguments; it identifies the quantifier gap in that proposed substitution.

## 6. Finite evidence and remaining gap

`transport_lp.py` enumerates exact finite cycle classes and solves a transportation LP with Hamming cost and uniform marginals. Floating-point HiGHS optima are diagnostics, not exact rational certificates. Examples: (s,l)=(6,6) gives 3.392041292..., (4,5) gives3.542857143..., (6,5) gives3.510822511..., (4,4) gives3.687301587.... Boundary l=2 reproduces2s/3+3. These modest sizes neither prove nor refute (T).

Remaining substantive task: prove interior (T), construct a different common erasure kernel, or produce an interior sequence with diverging optimal transport cost. The known gap-density bias must not be discarded. No concentration cutoff j<=k² is assumed or proved necessary here.

Sources read: SC001 theorem full erasure argument; SC002 theorem and experiment; BI001 v2 full source/coupling/prior proof; BC001 v1 §§1–4; MD001 binary lower; original DOT_START_PROMPT and START_HERE. No upload, publication, or claim of novelty. A later generic primary-literature search is recorded below; no theorem was imported from it.

Exact diagnostic: `check_bt001.py` passed 5,282 rational/algebraic finite checks of stationarity, all-state certificate, boundary cost, merge density, and merge cost. It does not check or prove (T).

## Limited literature triage

Generic queries on conditioned Markov-chain Hamming transport and fixed-count tilings returned [O’Connor, McGoff and Nobel, JMLR 23(45), 2022](https://www.jmlr.org/papers/v23/21-0519.html), whose abstract was opened. Its stated object is long-run transition couplings of stationary Markov chains, not the finite-horizon count-conditioned laws in (T). This is only scope triage from the abstract, not a full-paper exclusion or novelty assessment. No applicable transport theorem was established by this limited search.
