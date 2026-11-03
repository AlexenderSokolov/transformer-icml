# ACG001: approximate positional statistics suffice without exact gate recovery

2026-11-03. Root-authored mathematical candidate, not yet independently reviewed or accepted. This is a statistical interface for a subsequent paid neural implementation, not a Transformer theorem or an optimal precision lower bound.

## 1. Experiment and claim

Observe a binary word X_0,...,X_(M+1), M>=64, from a homogeneous order-two transition table theta and arbitrary initial pair law. Write Y_i=(X_i,X_(i+1)), and suppose a stationary pair law Pi satisfies P^2(u,v)>=beta Pi(v) for every pair u,v, including unsupported states, with beta>0. The statistical target is the next-symbol law at the actual terminal pair Y_M. No stationary-start assumption is made.

An offline source-independent kernel edits at most k positions among 0,...,M-1 on every outcome, producing Z; final symbols M,M+1 stay protected. The kernel does not see predictor seeds. Let d_u=1-first(u). On the clean word define, for each pair u:

- J_u=sum_{i=0}^{M-1} 1{Y_i=u};
- C_u=sum_{i=0}^{M-1} 1{Y_i=u, X_(i+2)=d_u};
- D_u=sum_{i=0}^{floor(M/2)-1} 1{Y_i=u}.

Use primes for the same counts on Z. All are nonnegative and C_u,D_u<=J_u<=M. The selected row u=Y_M is also the final pair of Z.

Suppose an observation-measurable computation supplies real-valued estimates tilde J_u, tilde C_u, tilde D_u, with simultaneous pathwise coordinate error at most e>=0 from the primed counts, for every allowed word and every outcome of its independent coins. There is no access to the clean word or hidden theta. e is a proved error bound, not an input the decoder must know.

Clip sequentially:

    bar J_u=clip(tilde J_u;0,M),
    bar C_u=clip(tilde C_u;0,bar J_u),
    bar D_u=clip(tilde D_u;0,bar J_u).

At the selected row put

    qhat=bar C/bar J if bar J>0 and 512 bar D>=bar J;
    qhat=0 otherwise.

Predict next symbol d_u with probability qhat, and the other symbol with probability 1-qhat. Equality accepts. A further observation-measurable probability output within xi>=0 of qhat is also allowed; its extra TV loss is at most xi.

Then, for unsquared TV risk R,

    R <= min{1, 65536/sqrt(M) + 65536/(M sqrt(beta))
                  + 1072176(6k+e)/M + xi}.                 (1)

At beta=1/M this gives

    R <= min{1, 131072/sqrt(M) + 6433056 k/M
                  + 1072176 e/M + xi}.                    (2)

The decoder need not reproduce the exact gate bit of the corrupted word. Gate changes close to its threshold are allowed by the same pathwise argument that controls edits. The result does not claim the gate bit itself is robust.

## 2. Imported accepted statistical facts

All four facts below are imported from the accepted finite positional manuscript, recovered byte-for-byte at ../resumption_20261103/recovered_science/positional_manuscript_finite_20261102/sections/proofs_positive.tex. Its SHA256 is a629caebe01e614a71738f2036bd9016708f35871a15b6902dd98be967f69e88. These exact source interfaces were used in accepted O2T001; this unit does not reprove their source-probability arguments.

For the selected clean row, put q=theta_u(d_u), J=J_u, C=C_u, D=D_u. The source supplies:

1. Actual-terminal occupation: for every integer w>=1, Pr(J<w)<=16w/(M+1), with a probability cap at one (Lemma occupation).
2. Clean empirical risk: E[1{J>0}|C/J-q|]<=512/sqrt(M+1) (Lemma empirical).
3. Half-count imbalance: E[q 1{J>0,D<J/256}]<=65536/(M sqrt(beta)) (Lemma imbalance and the finite-upper application).
4. Half-count reciprocal: E[1{D>=J/1024}/(J+1)]<=130944/M (equation p-half-inverse, proved within Proposition finite-upper).

Ratios involving clean J are evaluated only on J>0. The next section proves the entire new perturbation reduction for real-valued estimates, including its integer-threshold boundary cases. Finite diagnostics will not substitute for these four imported facts.

## 3. Clipping does not magnify coordinate error

Let j in [0,M], c in [0,j], and |tilde j-j|,|tilde c-c|<=e. Projection onto [0,M] gives |bar j-j|<=e. Set bar c=clip(tilde c;0,bar j). Its upper bound bar c<=c+e follows from bar c<=max(tilde c,0)<=c+e. For the lower bound: if tilde c<0, then c<=e; if 0<=tilde c<=bar j, retain tilde c>=c-e; if tilde c>bar j, then bar c=bar j>=j-e>=c-e. Thus |bar c-c|<=e. Apply the identical argument to D. This proof does not require bar j to be integer or positive.

On Z, each coordinate is therefore still within e of its primed count. One symbol edit changes at most three departure triples, with histogram L1 change at most six; restricting the index set to the first half does not increase this bound. Since the selected row is protected,

    |bar J-J|, |bar C-C|, |bar D-D| <= Delta:=6k+e.    (3)

The coarse six-per-edit bound is deliberately shared with the accepted gate proof. Adjacent edits and split-crossing triples are counted by a union bound, not assumed disjoint.

## 4. Real-valued pathwise gate reduction

Let G={bar J>0,512 bar D>=bar J}, H={D>=J/1024}, and B={J>0,D<J/256}. Both C/J when defined and bar C/bar J when used belong to [0,1].

On G intersect H and J>0, ratio subtraction gives

    |bar C/bar J-q| <= |C/J-q| + 8Delta/(J+1).        (4)

For Delta=0 the ratios coincide. If Delta>0 and J>=2Delta, then bar J>=J/2 and the ratio difference is at most 4Delta/J<=8Delta/(J+1), using integer J>=1. If 0<J<2Delta, then Delta>J/2 and 8Delta/(J+1)>=1, so the unit bound suffices. This argument permits arbitrarily small noninteger Delta.

On G intersect H-complement, (3) and acceptance imply

    D+Delta >= bar D >= (J-Delta)/512,
    D < J/1024,

so J<1026Delta. On G-complement intersect B-complement with J>0, if bar J=0 then J<=Delta. Otherwise rejection and D>=J/256 yield

    J/256-Delta < (J+Delta)/512,

so J<513Delta. For Delta=0 neither false-status case with J>0 can occur. If rejection happens on B, its directional loss is exactly q.

Choose INTEGER thresholds

    w1=max{1,ceil(1026Delta)},
    w2=max{1,ceil(513Delta)}.

They cover these strict false-status inequalities and J=0. This ceiling is essential: the imported occupation lemma has an integer argument. Also w1+w2<=1539Delta+2, including Delta=0. Bounding every remaining loss by one gives the pathwise inequality

    |qhat-q| <= 1{J>0}|C/J-q|
       +8Delta 1_H/(J+1) + q 1_B
       +1{J<w1}+1{J<w2}.                            (5)

All terms are nonnegative. Randomized legal edits and arbitrary observation-measurable approximate statistics preserve (5) pointwise. It does not assume that the rounded statistics are counts of any word, nor that rounded J is an integer.

## 5. Risk bound and precision consequence

Average (5), invoke the four precise interfaces in §2, and add xi. The perturbation coefficient is

    8*130944 + 16*(1026+513) = 1072176.

The occupation remainder is at most 32/(M+1). Since

    512/sqrt(M+1)+32/(M+1) <= 65536/sqrt(M),

and 1/(M+1)<=1/M, (1) follows. The probability cap and beta=1/M yield (2). No expectation is replaced by a maximum over hidden source states.

In particular, let every normalized primed statistic J'_u/M,C'_u/M,D'_u/M be rounded to its nearest grid point of mesh 2^(-h), h a nonnegative integer, with a fixed tie rule. The grid includes 0 and 1. Then e<=M*2^(-h-1), and (2) gives

    R <= min{1, 131072/sqrt(M)+6433056 k/M
                  +536088*2^(-h)+xi}.               (6)

Thus h>=ceil(log2(M)/2) and xi<=M^(-1/2) suffice for a constant multiple of max{M^(-1/2),k/M}, uniformly in the unknown k. This is a SUFFICIENT precision for normalized statistic banks, not a necessary precision theorem. For known M, storing all twelve grid coordinates costs at most 12(h+1) bits, plus the two protected terminal labels; the value 1 requires h+1 bits in the straightforward integer numerator representation.

This representation statement does not give a streaming algorithm that maintains these rounded counts with that space: repeated rounding can accumulate error. It also does not prove that all twelve coordinates are necessary. If raw input is resident it costs M+2 bits. Addressing, exact prefix selection, accumulation precision, constructing local pair/triple features, division/readout, weights, depth, attention operations, output precision and training all remain separate costs.

## 6. What this resolves, and what it does not

This closes a specific mathematical prerequisite for a finite-precision positional neural construction: an implementation need not protect a discontinuous gate bit exactly if it approximates all three relevant statistics uniformly and produces a legal probability. It permits O(M^(-1/2)) normalized-bank error at the critical certificate without losing the statistical rate. The protected endpoint and paid first-half statistic are crucial; a count-only implementation has not acquired the extra information for free.

It is not an architecture construction, Transformer depth/width bound, optimal weight/activation precision statement, learnability result, general-order source theorem, or new general statistical principle. The same interface is available to a classical counter, so a subsequent neural theorem must use a same-information, fully costed comparison rather than claim a neural statistical advantage. The channel results concern a different transmission cut; combining the rounded banks with those coding interfaces requires an explicit changed payload and cost account.
