# Independent analytical review: fixed finite alphabets

3 November 2026. **PASS within the stated exact-real scope.** No numerical experiment, simulation, sample enumeration, training, publication, external upload, or finite-bit implementation test was performed.

## Exact reviewed inputs

- Main artifact: `fixed_alphabet_terminal_kl.v1.md`.
- SHA-256: `ca5e4d0c0ee5d7b20c8dcd5a0a58775d0e570bf3571837c6c2750e4e964c4a58`.
- Preserved prior construction: `sources/alphabet_extension_candidate_v1.html`.
- Its SHA-256: `f0a9621a62655aaa41cf4c45fcfcf183580511ed52465be1bf11b988e45e24ff`.
- The prior construction identifies its public snapshot at commit `0d678eefb558d5108dd5ef893b033c6f58077d81`, Git blob `9cc4a7554fdaffc08bd89d894cb887cbfef73307`.

The main source and the full preserved finite-alphabet construction were read directly. The prior binary occupation and exact-KL argument and the narrow-Gaussian scalar proofs were independently reconstructed during this and the preceding binary review. Hash calculations are integrity checks, not mathematical numerical evidence.

## 1. Statistical theorem

The theorem is valid for every finite integer A>=2 and n>=1, with all four quantities t,c,a,U exactly as defined in Section 1. The separate n=0 statement is valid. The finite-parameter inequalities do not require A to be fixed as n varies, but their displayed asymptotic O_A rate is correctly restricted to fixed A.

### Occupation and reciprocal moment

The pair process has D=A^2 states. The suffix argument proves monotonicity of the maximum over starts, not of each initial-state probability. Summing pathwise first-w flags separately over all D initial states gives D^2 w, and therefore the arbitrary-start constant A^4/(n+1). The stationary finite-window argument gives D rather than D^2, hence A^2/(n+1). Both arguments allow zero transition probabilities, reducibility, periodicity, and arbitrary off-support starts when stationarity is not imposed.

The summation-by-parts identity in Section 2 includes J=0. Its harmonic estimate is valid for A>=2. One can also directly bound its summand by 1/(k+A+1), obtaining a harmonic sum at most log((n+A)/A); the looser displayed c[1+log(n+A)] follows. No unprovided minimum stationary mass, mixing rate, or independent query is used.

### Simultaneous categorical stacks

There are A^2 row stacks, A indicator coordinates per stack, and n deterministic positive prefix lengths. A two-sided Bernstein bound costs 2e^-t per coordinate-prefix event, giving precisely 2A^3 n e^-t. The choice t>=log[2A^3 n(n+1)^2] makes the failure probability at most (n+1)^-2.

The stack construction generates the original source law and permits pathwise evaluation at its actual terminal row and data-dependent count. No assertion is made that counts remain binomial after conditioning on J, on the terminal row, or on a chosen path. Correlation among coordinates of one categorical stack is harmless because the proof uses a union bound, not independence among those coordinates.

### All-A smoothing displacement and exact KL

For a symbol coordinate, z=jp and e=(j+A)p-(k+1) satisfy

    z<=2k+10t/3,
    (k-z)^2<=8kt+128t^2/9,
    e^2<=16kt+31t^2.

The last step uses |Ap-1|<=A-1<=t. This is why t>=A is substantive, particularly for growing A. The constants 31, 32, and 48 all check algebraically.

The chi-square route gives 32A t^2/(j+A). For the exact-KL route, the large observed smoothed count case gives at most 47t per Poisson-divergence term. In the small count case the correct all-A bound is x<7t, not the binary x<6t. The artifact correctly uses x<7t and obtains h<=15t+7t log t<=48t(1+log t). Summing the exact identity (j+A)D=sum_b h yields 48A t(1+log t)/(j+A).

Both bounds hold on the same event, so taking their minimum before expectation is justified. The j=0 inequalities are deterministic. On all outcomes the add-one probabilities are at least 1/(n+A), giving the stated log(n+A) failure cost and deterministic cap. Expectation uses the unconditional reciprocal moment, without conditioning on the confidence event. These facts prove (1), including its all-A finite-parameter form.

## 2. Exact-real architecture and all boundary cases

The preserved prior finite-A construction supports the retained first three blocks. A BOS token of each alphabet symbol contributes one pseudocount to its corresponding coordinate. At valid successor keys the two previous symbols are copied and snapped exactly; at invalid keys the validity gate makes all candidate indicators zero. The terminal query has an exact previous-symbol copy even at N=2. The A^2 context heads therefore produce the stated add-one/distractor mixture, and the FFN chooses the actual terminal row. A separate uniform head supplies 1/L. No count, reciprocal, or row-selection oracle is added externally.

Each new rescaling head has the correct score -(j-mu_b)^2/L up to a query-only constant and produces |x_b-Lp_b|<=20 with x_b in [0,L]. The unit-cell quadrature, boundary integral, normalizer lower bound, and analytical maximum used for its constant were checked. The narrow readout head has score -(j-x_b)^2 up to a query-only constant. Its geometric-mean lemma provides |G_b-x_b|<=24 and 1<=G_b<=L. The lattice bound, two log-deficit regions, and boundary cases in that lemma were checked.

It is important that the x_b need not sum to L. The proof does not assume otherwise. Instead |G_b-Lp_b|<=44 and the exact simplex property of terminal p imply

    ||G/S-p||_1 <= |1-S/L|+||G/L-p||_1 <=88A/L.

This proves TV(R,p)<=44A/L for every L>=4, with no denominator threshold or hidden L>>A assumption. The distractor error obeys Ne^-N/A<=1/L for every A,N>=2, giving the stated (44A+1)/L approximation to B.

From G_b>=1 and G_a<=L for the other coordinates, R_b>=1/[1+(A-1)L]>=1/(AL). This is the claimed floor, rather than an incorrectly binary floor. It also gives the deterministic log[1+(A-1)L] forward-KL cap. All these statements hold at N=2.

## 3. Multiclass transfer

The entropy-variational inequality used in Section 8 is valid for arbitrary truth and positive reference/prediction distributions. Add-one and the implemented output have the needed positivity on every history, including zero visits.

For delta=B-R, the positive and negative parts each sum to TV(B,R). Thus sum delta_b^2<=2TV(B,R)^2. Combining this with the floor 1/(AL) gives exactly

    chi-square(B,R)<=2A(44A+1)^2/L.

Consequently the stated 2V plus that penalty follows pointwise and then in expectation. No reverse-Pinsker conversion or independence is being used. The constants remain valid for growing A, although they need not tend to zero in that regime.

## 4. Resources and limitations

The head allocation A^2+1 accommodates the A new coordinatewise heads, and d_h>=4(A+10) accommodates all vector values. Multiplying by A^2+1 gives width exceeding the stated A^3+2A^2+9A+8 disjoint residual slots for every A>=2. The slot count, five-block depth, and active head total A^2+2A+3 are consistent. At A=2 this nonminimal general construction uses 11 active heads, unlike the separately optimized binary construction's 10; the artifact does not conflate them.

The active FFN widths (4A+5,2A^2,A^3,2A,0) are valid. Taking their maximum, rather than calling A^3 the largest for every A, correctly handles A=2. Dense parameter count O(A^6), coefficient bit descriptions O(log(A+2)), conservative exact-real operation bound O(A^3 L^2+A^6 L), and row-streamed real-slot bound O(A^3 L+A^6) are consistent with the displayed architecture. Exponential/logarithm evaluation and positional generation remain separately paid assumptions.

The source correctly declines to transfer the old specialized backend to the new readout. This review does not establish finite-word accuracy, floating-point positivity, gate margins under numerical error, training attainability, optimal alphabet dependence, or a common fixed-width network for unbounded A. For fixed A the statistical rate and the O_A(1/n) output penalty follow; for growing A only the explicit inequalities and A-dependent resource family are asserted.

## 5. Evidence boundary and verdict

No mathematical defect requiring a change was found in Sections 1-9 or in their fixed-A/growing-A scope statements. Bibliographic claims about HJW23 and the public snapshot attribution are separately sourced by the author; this review is not a fresh comprehensive prior-art or publication-priority audit.

**Verdict: PASS** for the exact source hash above, with the limitations already stated in the artifact. No numerical or external action is needed to establish this analytical verdict.
