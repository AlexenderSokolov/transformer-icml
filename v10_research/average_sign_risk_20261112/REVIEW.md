# Independent average-sign-risk review

2026-11-12. Analytically reviewed COUNTEREXAMPLE.md. No independent diagnostic rerun. Proof passes with a minor asymptotic-scale clarification communicated to the author.

The expm1 coefficient upper ratio follows from convexity, and the lower ratio exp(-delta rho^k)rho^j follows from expm1(x)>=x and expm1(x)<=x exp(x). The finite tail is correctly bounded by a truncated GEOMETRIC upper bound; the proof does not falsely infer a deficit for actual nonlinear weights. If an agreeing old sign occurs among the first m, its positive contribution beats the entire possible tail excess. If fewer than m old signs exist, truncation alone prevents failure. Thus the stated opposite-run event is a valid necessary condition, including tie exclusion.

The reversed stationary triple law is the same transition law, so its maximum reverse transition probability is <=1-c. The first older sign is conditionally fair given the target. This even supplies a harmless extra factor1/2, but omitting it remains valid. First-stage failure union ideal second-stage failure is legitimate without conditioning the source on first-stage success. The two prediction-error factors are correct: at most2 for an erroneous innovation, and then1/2 for the actual endpoint target.

The worst-word failure criterion holds eventually because polynomial epsilon dominates both exponentially small delta and the truncated geometric tail. It does not imply frequent failure. Choosing kappa>=1/(2[-log2(1-c)]) gives the displayed root-N statistical interface.

Scale clarification: delta=(1/2+N^-kappa/16)^N=2^(-N+O(N^(1-kappa)))=2^(-N+o(N)), not necessarily a constant multiple of2^-N when kappa<1. It is still exponentially small and retains the severe precision/amplification costs. This is exact scalar-interface arithmetic, not a compiled robust PreLN predictor.

Publication note: the asymptotic-scale clarification above is incorporated in the accompanying COUNTEREXAMPLE.md.
