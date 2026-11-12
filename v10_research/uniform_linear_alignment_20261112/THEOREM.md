# Uniform linear prefix stacks cannot uniformly align all predecessors

2026-11-12. A restricted linear-operator theorem, not a lower bound for full PreLN Transformers or statistical prediction risk. No novelty claim for polynomial functional calculus. Independently analytically reviewed; see REVIEW.md.

## Exact model and quantifiers

Fix N>=3 and the self-inclusive uniform-prefix matrix P_N with entries P_ij=1{j<=i}/i. Input X ranges over the FULL sign cube {-1,+1}^N. A finite stack may have any finite layer count D_N, any finite feature widths (even depending on N), and arbitrary real coefficients with no norm restriction. Each layer's dependence on input-dependent features has the form H_next=H A_l+P_N H B_l, with matrices shared across rows. Multiple uniform heads collapse into B_l. Arbitrary deterministic affine offsets are allowed; they do not depend on X. Initial token dependence is the same linear embedding X_i u at every row, plus deterministic offsets. The final input-dependent readout uses one common linear feature functional at every row, with any deterministic output offset.

Thus all coefficients, widths, depth and affine public offsets MAY depend on N. What is excluded is a nonlinear operation (including actual changing full LayerNorm), a position-dependent multiplicative map on the token-dependent features, a nonuniform head, or an additional direct shift/history input. This is not a theorem about all zero-QK full-PreLN networks: their layer normalizations are nonlinear and are outside this model.

Induction on layers shows the final scalar map is y=A X+b with A=p(P_N) for a real polynomial p of degree at most the number of prefix-reading layers. Noncommuting feature matrices do not change this conclusion: expanding their products still yields scalar coefficients multiplying powers of the single row operator P_N. Deterministic offsets contribute only b.

## Main quantitative statement

Define the all-word, all-valid-row alignment error

    epsilon_N=max_{X in {-1,+1}^N} max_{2<=i<=N}|y_i-X_(i-1)|.

The first row has no target and is ignored. Put H_N^*=sum_{k=2}^{N-1}1/k. Then every stack above satisfies

    epsilon_N >= H_N^*/(H_N^*+2).

In particular this lower bound tends to1 as N grows, irrespective of depth or coefficient magnitudes. The zero-output map has error1, so the asymptotic obstruction is nonvacuous. This does not identify the exact finite-N optimum.

## Proof

Let d_i=A_ii. Since P is lower triangular, d_i=p(1/i). Its nearest strict-lower entry has the exact divided-difference identity

    A_(i,i-1)=(i-1)[p(1/(i-1))-p(1/i)]
              =(i-1)(d_(i-1)-d_i).

One can check this on every monomial: the only paths from column i-1 to row i in a power of P stay within those two indices, giving the two-diagonal geometric sum. Linear combination proves it for arbitrary p, even degrees greater than N. It is not a degree-counting argument that fails once depth exceeds N.

If epsilon_N>=1 the claim is immediate. Otherwise use the two opposite input words X and -X to cancel any affine offset. For every row i>=2 the linear error row A_i−e_(i-1) then has sign-cube norm at most epsilon_N. Its exact supremum over signs is its l1 norm. Therefore |d_i|<=epsilon_N and A_(i,i-1)>=1-epsilon_N.

For i=3,...,N, both diagonal entries d_(i-1),d_i belong to valid rows, so

    d_(i-1)-d_i >=(1-epsilon_N)/(i-1).

Summing gives d_2-d_N >=(1-epsilon_N)H_N^*. But |d_2|,|d_N|<=epsilon_N gives d_2-d_N<=2epsilon_N. Rearranging yields the theorem. For N=2 the harmonic sum is empty and this argument intentionally gives no obstruction.

## Relation to bounded-score local alignment

This result eliminates a tempting strategy of obtaining a shift by repeatedly applying uniform prefix averages and shared linear residual/value maps. It does NOT eliminate nonlinear PreLN computation, positional multiplication, or another bounded-score mechanism.

Conversely, under the enlarged contract allowing the explicit external bounded bias log(2)1{j=i-1}, the separately reviewed diffuse-head contrast and true width-six PreLN amplifier recover local predecessor signs to accuracy eta in O(log N+log(1/eta)) blocks. Thus bounded scores alone do not prohibit logarithmic-depth local alignment. The unresolved issue in a narrower positional-QK model is implementing the appropriate positional interaction without an external indicator, growing width or exponentially tiny margins.

The external predecessor-bias construction has a global positional-array Frobenius cost Theta(sqrt N) and is not an exact fixed-dimensional QK score factorization. The rank-one exponential alternative avoids that resource but pays exponentially small signal and linear-in-N scalar decoding precision/depth. None of these facts can be promoted to an unrestricted task-risk lower bound without additional reductions.

## Verification

The author's in-memory exact Fraction diagnostic used seed20261112, N=3,...,10 and96 sampled polynomials of degrees up to20, allowing rational signed coefficients and affine offsets. It checked diagonal/polynomial identities, every nearest-lower divided difference and the harmonic error bound. Ten cases also enumerated the complete sign cube to verify the affine operator-norm error formula. All1162 assertions passed. The publication diagnostic was independently rerun with identical reported counts; an optimized-Python rejection guard was added. Finite tests verify algebraic bookkeeping, not the universal theorem. No training or CI run is claimed.
