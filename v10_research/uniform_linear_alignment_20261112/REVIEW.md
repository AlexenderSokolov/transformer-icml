# Independent review: uniform-linear predecessor obstruction

2026-11-12. Reviewed the complete statements/proofs supplied by the author. This is an analytical review, not an independent rerun of the author's reported Fraction diagnostics. No gap found under the restrictions below.

## Shared uniform-linear model

Let P_ij=1{j<=i}/i and allow arbitrary finite widths/depth with shared linear updates H_next=H A+P H B. Multiple heads using the SAME uniform prefix P combine into P H times a summed feature matrix, so do not change the argument. Homogeneous token-linear initialization and a shared final linear readout give the token-dependent component y=p(P)X. Arbitrary public affine offsets, including position-dependent offsets, contribute a data-independent vector b and do not change that component. Position-dependent TOKEN coefficients are excluded.

If max_X max_{i>=2}|[p(P)X+b]_i-X_(i-1)|<=epsilon, evaluating the same row at X and -X and subtracting cancels b. Therefore the linear error row has sign-cube supremum at most epsilon, equivalently its l1 norm is at most epsilon. In particular |d_i|<=epsilon for d_i=p(1/i), and [p(P)]_(i,i-1)>=1-epsilon.

The adjacent subdiagonal of a polynomial in a triangular matrix depends only on the two neighboring diagonal entries and their connecting entry. With P_(i,i-1)=1/i and lambda_(i-1)-lambda_i=1/[i(i-1)], it is exactly

    [p(P)]_(i,i-1)=(i-1)[d_(i-1)-d_i].

Summing i=3,...,N gives d_2-d_N >=(1-epsilon)H, H=sum_{k=2}^{N-1}1/k. The left side is <=2epsilon. Hence epsilon>=H/(H+2), tending to one. Starting at i=3 is important: d_1 is not controlled by the stated output error, and the proof correctly avoids it. The algebra remains valid even if epsilon>=1, when the bound is already trivial.

This proves a worst-word ALL-ROW predecessor limitation for linear uniform-prefix stacks, not actual nonlinear PreLN, not average source risk, and not one publicly chosen source broadcast. Arbitrarily growing coefficients or depth do not rescue this restricted p(P) class. Exact normalized attention, ReLU gating, token-dependent scores, distinct masks, or position-dependent token coefficients lie outside it.


Publication scope: this excerpt preserves only the uniform-linear section of the combined review. The separate two-row lemma is not included in this checkpoint.
