# Stationary terminal-KL output corollaries

Composition note, 4 November 2026 (UTC). The stationary add-one proof has received exact-file independent analytical review. This note only substitutes that statistical bound into the inherited, separately reviewed pathwise output inequalities. It leaves the five-block architecture and the specialized arithmetic algorithm unchanged. The statements are analytical, not software-tested.

## 1. Source-bound statistical input

For A>=2 and n>=1, let L=n+2+A, K_n=1+floor(log_2 n), and

    V_stat(A,n)=min{log(n+A),
                    A^2[log A+4608 A K_n]/(n+1)}.

For every homogeneous second-order source with a stationary initial pair distribution, its actual-terminal full-history add-one distribution B satisfies

    E D_KL(p_{Y_n}||B)<=V_stat(A,n).                    (1)

Zeros, reducibility, periodicity, and multiple stationary classes are allowed. The actual terminal context is Y_n=(X_{n+1},X_{n+2}), from the same observed word X_1,...,X_{n+2}; no independent query is introduced.

The exact proof source is `stationary_terminal_kl.candidate.v1.md`, SHA-256

    1d436719744fd51bda32db723e84932c68507479383154abeb4b9724f2db1337.

Its independent exact-file analytical review is `stationary_terminal_kl.independent_review.v1.md`, SHA-256

    691d02016ea4ae8e5b127840ba14dc5cb65231d0bf98af27b5e9497dd5c35ea8.

## 2. Exact-real five-block output

Let R be the output of the unchanged five-block causal attention/ReLU construction in the inherited exact-real source. Its parameters are fixed for each fixed A, independently of n and the unknown source. All architectural assumptions remain those of that source, including its positional features, full causal support, smoothing BOS tokens, and final A-way vocabulary softmax.

The inherited, all-word pathwise bounds are

    TV(R,B)<=min{1,(44A+1)/L},
    R_b>=1/[1+(A-1)L]>=1/(AL).

Their established forward-KL transfer gives

    E D_KL(p_{Y_n}||R)
      <=min{log[1+(A-1)L],
             2V_stat(A,n)+2A(44A+1)^2/L}.              (2)

The numerical constant and pathwise premises are unchanged. The only new substitution is (1).

## 3. Specialized finite-bit output

Let Q be the terminal output of the inherited integer/dyadic evaluation algorithm, not an arbitrary floating-point implementation. Set

    s=ceil(log_2(AL)),
    b=32s,
    H=2^b,
    F=H^2.

This algorithm uses exact integer positions and squares, constructed log positions, exact dyadic gates, max-shifted exponential approximation, and mass-preserving normalization. The inherited proof gives for every observed word

    Q is a nonnegative exact H-grid simplex,
    TV(Q,B)<=min{1,(46A+2)/L},
    Q_b>=1/(4AL),
    D_KL(p_{Y_n}||Q)
      <=2D_KL(p_{Y_n}||B)+8A(46A+2)^2/L.

Consequently,

    E D_KL(p_{Y_n}||Q)
      <=min{log(4AL),
             2V_stat(A,n)+8A(46A+2)^2/L}.              (3)

The explicit support floor, not TV alone, is necessary for this forward-KL statement. No extra rounding or unspecified backend may be inserted into (3).

### Fractional precision, signed range, and guard space

The value b counts fractional bits. It is not the entire signed machine-word width. The model must also represent signed raw scores and rowwise maxima before max shifting, integer positions and squares, exact accumulation, and wider products:

- Raw copy-score magnitudes are O(L^3); narrow-head scores are O(L^2).
- The broad-head O(L) score statement is terminal only. Earlier selected probability coordinates may be as large as A^2, so earlier broad scores are allowed a larger polynomial range. This still needs only O(log A+log L) magnitude bits.
- Signed differences, linear accumulations, and row sums require their corresponding O(log A+log L) magnitude and guard allowance.
- Since F=H^2, an F-grid repeated-squaring product can require approximately 4b bits before its exact division. Other products likewise receive the constant-factor wider temporaries specified in the inherited algorithm.

Overall working integer lengths are O(b+log A+log L)=O(log(AL)), with these wider temporaries. The proof does not certify b total signed bits, a fixed exponent range, generic IEEE execution, GPU kernels, or automatic mixed precision.

The inherited conservative schoolbook cost is

    O(((A^2+2A+3)L^2+L)b^3
       +(A^3 L^2+A^6 L)b^2) bit operations,

and row-streamed storage is

    O(A^3 L b+b^2+A^6 log(A+2)) bits.

These are analytic resource bounds, not timing measurements, a training guarantee, or an executed implementation certificate. A changing A changes the architecture and vocabulary; the displayed formulas describe a fixed-A family and its explicit A dependence. The length-dependent precision schedule is a paid evaluation resource, not a length-dependent learned coefficient.

## 4. Zero-transition boundary

For n=0 do not evaluate K_n or V_stat. The add-one distribution is uniform, so its forward KL is at most log A. With L=A+2, the same pathwise transfers instead give

    E D_KL(p_{Y_0}||R)
      <=min{log[1+(A-1)L],
             2log A+2A(44A+1)^2/L},
    E D_KL(p_{Y_0}||Q)
      <=min{log(4AL),
             2log A+8A(46A+2)^2/L}.

The inherited evaluator covers this shortest word without inventing a data transition.

## 5. Alphabet dependence and comparison boundary

Both output penalties in (2)-(3) are O(A^3/L). Thus the stationary B, R and specialized Q all have an upper bound O(A^3 log(n+2)/(n+1)). They are consistent under the sufficient condition A^3 log(n+2)/(n+1)->0. This is not asserted necessary.

Han, Jana and Wu's Theorem 22 states a stationary second-order minimax rate of order

    A^3/(n+2) * log[(n+2)/A^3]

when 2<=A<=(n+2)^(1/3)/C_2, for an absolute constant C_2 supplied by that theorem. Their observed length is N=n+2. Our upper bound retains log n; it does not close the logarithmic gap near the growing-alphabet boundary. For fixed eta>0 in the subregime A^3<=(n+2)^(1-eta), within the theorem's domain, the logarithms are comparable up to constants depending on eta. At each fixed A>=2, the stationary worst-case rate is therefore Theta_A(log n/n) for B, R and the specified Q.

The unchanged arbitrary-start theorem remains available with its A^5 log n/n upper factor. The stationary refinement does not improve that factor without an initial-law assumption. No literature-priority claim, all-regime add-one optimality claim, or generic finite-bit implementation claim is made.

Primary source: Han, Jana and Wu, "Optimal prediction of Markov chains with and without spectral gap," IEEE Transactions on Information Theory 69(6), 2023, pp. 3920-3959. DOI: https://doi.org/10.1109/TIT.2023.3239508 ; author text, Theorem 22 and Remark 1: https://arxiv.org/html/2106.13947v2 . The earlier source audit records the exact model and indexing comparison.

## 6. Inherited source bindings

- `../fixed_alphabet_kl_sharpening_20261103_2346/sharp_kl_output_corollaries.v1.md`, SHA-256 `9173ba24c276f1fed8b08a3d59963e8fefc1b3b0c9bfea61729bffafadce5481`: prior all-start composition, pathwise outputs, and statistical substitution interface.
- `../fixed_alphabet_kl_sharpening_20261103_2346/sources/precision_budget_constructive_candidate.v1.md`, SHA-256 `e555323ee18b39b0003863e9d41084d6f2222a575c340b0a9bb8c87213d01a16`: exact integer recurrences, log construction, normalization, support floor, precision schedule, and bit resource bounds.
- `../fixed_alphabet_kl_sharpening_20261103_2346/reviews/precision_adversarial_review.v1.md`, especially Section 7: independent source-bound review of signed range, early-position broad scores, guard space, and wider product temporaries.
- `../fixed_alphabet_kl_sharpening_20261103_2346/primary_source_matching_lower_audit.v1.md`: HJW theorem hypotheses, actual-terminal loss, N=n+2 substitution, and lower-bound applicability.

The frozen source proofs and earlier reviews are preserved. A review of this composition does not constitute a fresh independent audit of every inherited architecture lemma or an implementation test.
