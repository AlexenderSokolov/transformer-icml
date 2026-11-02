# Implementation clarification for the frozen general-Markov packing constructions

2026-11-02, after the stage-seven mathematical scope freeze. This records a specific omission identified during the fresh manuscript audit. The accepted MG001/MG002 proof bytes remain unchanged. No new risk rate, source class, noise budget or capacity claim is added. This note completes the explicit finite pre-fault implementation and must accompany those two proofs.

## Omission and corrected schedule

MG001 declares that the actual finite bank before the fault belongs to [0,1]^(RK^3), but its composition paragraph explicitly proves only a uniform distance of at most 1/Q from the ideal cube-valued bank. Symmetric finite rounding need not itself preserve the cube. The clipping already specified AFTER the fault does not establish the declared membership BEFORE that fault. MG002 inherits the same construction obligation. Thus the pre-fault schedule should explicitly include the following final working-lattice operation.

Let z be a raw output coordinate of the finite encoder on its uniform P-bit fractional grid. Before exposing the bank to the adversary, replace it by

    a = C(z) = ReLU(z) - ReLU(z-1).

Implement the two ReLUs and their affine difference with fixed-size bounded primitives, retaining the required rails until the difference is formed. Constants 0,1 are exactly on the P grid, the input has a guarded signed representation, and all subtractions/ReLUs are exact on this lattice. The resulting a belongs to [0,1] on the same P grid, including both endpoints.

The ideal output f already lies in [0,1]. Append the corresponding ideal clip, which acts as the identity on f. Projection onto this interval is nonexpansive relative to any point inside it, so

    |C(z)-f| <= |z-f| <= 1/Q.

Consequently the complete pre-fault approximation certificate survives. After any allowed attack, the existing channel clipping and final Q-floor still give coordinate discrepancy at most (c+2)/Q from f. The robust geometric recovery, symmetric inverse inequality, false-mass normalization and terminal occupation proofs are unchanged.

## Depth, precision, and costs

The final clips add a fixed number of primitive stages and O(RK^3) fixed-width rails/coefficients per token, with bounded coefficients and intermediates. Count these stages in the total d BEFORE selecting P>=4h+c_FA(d+2), and retain any other stated coefficient/word guards. This removes any circular use of an old depth in the precision certificate. The generic evaluator can be applied to the whole augmented architecture; equivalently its exact final clip cannot worsen the already proved raw-bank error.

All tokens execute the clips when the declared batch syntax requires it. Dense zero slots, optional dummy heads and their masks, temporary rails, writes and clearing are included in the existing ledger with this enlarged d and fixed constants. The encoder-to-decoder w-to-b conversion and simultaneous-bank charges remain unchanged. No new source-dependent side channel or additional exposed coordinate is introduced. Both dyadic MG001 and rational-description MG002 admit these exact lattice clips; their decoder outputs remain paid finite rational probabilities, not coarse-Q probabilities.

## Evidence status

This is an implementation clarification of the frozen claims, not an originally saved part of the old proof. The old proof and its review must not be relabeled as having explicitly stated this step. A fresh review of this note and the matching manuscript change is recorded separately. The stage-seven correction register identifies this post-freeze clarification while keeping the eleven original accepted units and their original hashes intact.
