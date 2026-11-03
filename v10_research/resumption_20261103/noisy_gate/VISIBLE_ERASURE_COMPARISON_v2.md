# Visible erasures: a sharp contrasting reliability model

2026-11-03. Abstract derivation; concrete v10 constants remain conditional on recovered-proof/dependency verification. This is a different channel from silent BSC flips.

## Single transmission

Use the same instance family, nonnegative loss, randomized estimators, positive normalizers, and post-attack independence conditions as NOISY_MESSAGE_REDUCTION.md. Send the hidden exact bit b through a visible erasure channel: output b with probability 1-epsilon and the distinguished symbol bottom with probability epsilon, independently of all pre-channel variables. Both the erasure flag and the successful bit are visible to the estimator; the base observation Z remains noiseless.

For 0<=epsilon<=1,

max{Gamma_exact, epsilon Gamma_0} <= Gamma_erase
 <= (1-epsilon) Gamma_exact + epsilon Gamma_0,

where at endpoint zero weights we read the bound by the separate exact endpoint identities rather than undefined products with infinite risks. The displayed finite upper bound assumes the two component minimax values are finite.

Lower bound: simulating erasure from the exact bit shows Gamma_erase>=Gamma_exact. The output bottom has a common submeasure of mass epsilon, so the overlap theorem gives Gamma_erase>=epsilon Gamma_0 (or trivial nonnegativity if epsilon=0).

Upper bound: for any delta>0 choose a single delta-optimal exact estimator A_exact and a single delta-optimal baseline estimator A_0. Use A_exact(Z,b) on success and A_0(Z) on erasure. The erasure event is independent of the entire instance and private estimator randomness, so, for every k,i,

R_i(A_combined)/g_k
 = (1-epsilon) R_i(A_exact)/g_k + epsilon R_i(A_0)/g_k
 <= (1-epsilon)(Gamma_exact+delta)+epsilon(Gamma_0+delta).

Take the joint suprema, then let delta decrease to zero. Both component estimators are uniform across all k and i. No sup/inf exchange or bounded-loss assumption is needed for this bound.

If a sequence of problems satisfies c_e<=Gamma_exact<=C_e and c_0 L<=Gamma_0<=C_0 L, with constants positive and independent of problem size and epsilon, then

Gamma_erase = Theta(1+epsilon L).

Indeed max(c_e,epsilon c_0 L)>=(min(c_e,c_0)/2)(1+epsilon L), while the upper bound is at most C_e+epsilon C_0 L. The constants are uniform in epsilon in [0,1].

## R independent repetitions of the same bit

For integer R>=0, independently erase each transmission with probability epsilon. The whole output determines b whenever at least one transmission succeeds. Its all-erased event has probability epsilon^R (for R=0 set this probability equal to 1).

The repeated-output experiment is equivalent to a single visible erasure channel with erasure probability epsilon^R, not merely bounded by it:

- To obtain the effective channel from the full transcript, output bottom if every coordinate was erased; otherwise output the common non-erased bit.
- To simulate the full transcript from the effective channel, if the effective output is bottom output the all-erased string. Otherwise sample the erasure mask according to its original iid law conditional on at least one success, independently of the pre-channel state and bit, then place the supplied bit in its successful coordinates. This conditional law exists whenever success probability is positive. At epsilon=1 or R=0 there is no success branch; at epsilon=0 and R>=1 use the deterministic all-success mask.

The mask is independent of the underlying state; conditioning on mask nonemptiness does not introduce bit dependence. This verifies equivalence for joint estimation with Z, not just stand-alone bit decoding.

Therefore

max{Gamma_exact, epsilon^R Gamma_0} <= Gamma_erase,R
 <= (1-epsilon^R) Gamma_exact+epsilon^R Gamma_0,

with endpoint identities Gamma_erase,0=Gamma_0, Gamma_erase,R=Gamma_exact for epsilon=0 and R>=1, and Gamma_erase,R=Gamma_0 for epsilon=1.

Under the two-sided component bounds above,

Gamma_erase,R=Theta(1+epsilon^R L).

For fixed 0<epsilon<1 and L asymptotic to log M, constant competitive ratio is possible with R=O(log log M) and requires R=Omega(log log M). More explicitly, to make the baseline contribution at most a chosen constant a>0, it suffices that epsilon^R C_0 L<=a, i.e.

R >= log(C_0 L/a)/log(1/epsilon).

Conversely a ratio at most C implies epsilon^R c_0 L<=C and hence R>=log(c_0 L/C)/log(1/epsilon). Thus the minimum repetition count to achieve a fixed feasible bounded ratio (for example C_e+a) is Theta(log log M), up to integer rounding and small-size truncation. This does not claim attainability for an arbitrarily prescribed target C below Gamma_exact.

## Conditional v10 specialization

Using the root-reported bounds

L=ell_M=1+ln((M+2)/2),
2^(-33)L<=Gamma_0<=2^17 L,
1/96<=Gamma_exact<=1024+2^20,

the erasure experiment obeys, uniformly over epsilon and R,

max{1/96, 2^(-33)epsilon^R ell_M} <= Gamma_erase,R
 <= (1024+2^20)+2^17 epsilon^R ell_M.

The clean lower floor 1/96 is a historical input reported by root and is not reproved here. Consequently the conditional erasure result is Theta(1+epsilon^R log M), with sharp order Theta(log log M) repetition complexity for fixed interior epsilon and feasible constant-ratio targets.

This sharp result does **not** close the silent-BSC gap. The erasure flag lets the estimator select an exact-gate estimator on success and a baseline estimator on known failure. A silent corrupted bit does not reveal this branch, so the same switching proof is unavailable. No claim of a sharp BSC threshold follows from this contrast.

## Fixed-length arbitrary encodings: conditional concrete strengthening

This section concerns **fixed-length R-bit, parameter/law-independent path encoders**, followed by coordinatewise independent visible erasures of probability epsilon. The encoder may use the corrupted full word, Z, and independent private randomness, but is not supplied the unknown parameter or a law-dependent oracle. Encoding and corruption finish before the fresh erasure mask is sampled. The receiver retains the noiseless base observation Z. Variable-length messages, adaptive transmissions, feedback-driven encoding, noise-aware corruption, and correlated erasure masks are outside this statement.

Write Gamma_any,R for the infimum over all admissible such encoders and joint estimators, with a single procedure uniform over the same budgets and instances. For every fixed encoder, the event that all R positions are erased has probability epsilon^R independent of the complete pre-channel experiment. Conditional on that event the supplemental output is the constant all-erased string. Thus the common-component proof, applied to each procedure before the infimum, gives

Gamma_any,R >= epsilon^R Gamma_0,

with the usual R=0 convention epsilon^0=1. This is the general nonnegative-loss conclusion. **It does not assert Gamma_any,R>=Gamma_exact for the historical single-bit gate:** an arbitrary R-bit clean message can be more informative than that gate.

For the concrete v10 experiment there is instead a separate clean floor from the full-history IID lower-bound subfamily. At k=0 the encoder's message, independent erasure noise, receiver's base observation, and receiver's private randomness together form a randomized function of the full history. A law-independent composite encoder/receiver can therefore be simulated by a full-history estimator. Under the same target, normalizers, and admissible IID subfamily used in the historical lower bound, this gives Gamma_any,R>=1/96. This is conditional on the historical full-history lower bound, not on any claimed ordering with the single-bit Gamma_exact.

Combining these lower bounds with the concrete baseline gives

Gamma_any,R >= max{1/96, 2^(-33)epsilon^R ell_M}.

For R>=1, repeating the already-established exact bit R times is one admissible fixed-length encoding. The switching construction proved above therefore gives

Gamma_any,R <= (1-epsilon^R)(1024+2^20)+epsilon^R 2^17 ell_M
             <= (1024+2^20)+2^17 epsilon^R ell_M.

For R=0, no supplemental message exists and Gamma_any,0=Gamma_0; the same final relaxed upper bound is valid. It follows, with numerical constants uniform in M>=64, R>=0, and epsilon in [0,1], that

                     Gamma_any,R = Theta(1+epsilon^R ell_M).

Consequently for each fixed 0<epsilon<1 the optimal length among **all** admissible fixed-length encodings needed for a feasible constant-ratio target (for example 1024+2^20+a, with a>0 fixed) is Theta(log log M). Necessity uses only the all-erased component and baseline lower bound; sufficiency uses repetition of the historical exact gate. This sharp order is stronger than a repetition-only necessity claim, but is specific to visible erasures and the concrete full-history floor. It neither closes the silent-BSC gap nor imports a false general Gamma_any,R>=Gamma_exact comparison.
