# Independent analytic review: polynomial onset

Reviewed `polynomial_onset_addendum_v1.html`, SHA-256 `89db4cd6edce51dbb6ea9289c8f281f3d79811b2b09932456e8f4a0fc346873e`. Its input is `finite_n_explicit_bound_v1.html`, SHA-256 `fa808a23149bf3b7a4590f144cebdafe3a6ca1f1299c694d7bfe53e7b1ed0bd1`; this review is conditional on that bound and its hypotheses. The independently reviewed quantifier clarification is SHA-256 `4bde65c05294d1a624016e003e7983a508d4dd9348c727b332ffb5ee76c5f016`.

## Conclusion

I found no error in the displayed closed-form sufficient threshold, constants, domain, or strict-risk comparison. This is a conservative algebraic consequence for the specified exact-real graph, coefficient perturbation, fixed source, and true terminal risk. It is not an assertion about every perturbation, the first failure time, optimal exponent, floating-point execution, or a finite-threshold necessity. The source uses a fixed integer q; allowing q to vary with N is a different triangular quantification.

## Checks

Let t=N^(1/4)≥10^6(q+1), q≥1. Then t≥10^6, q≤t, and N≥16. The displayed logarithmic bound implies R≤(768/5)t+2≤160t. Since ln(8q)≤8q, Iq≤32q²+3; D=2q+1≤3q, so K≤32q²+480qt+24q+13≤549qt≤550qt≤t⁴=N. The last inequality uses q≤t and t²≥550. Thus the companion finite-N nontrivial branch applies.

R≥32 ln(N+2) and ln(3/4)≤−1/4 give d(R)≤(N+2)^−4≤t^−16. Inside Δ, 20(R+12)/N≤3200/t³+240/t⁴≤3440/t³<3600/t³, and sqrt(8d(R))≤3/t⁸. Subadditivity of the square root yields the stated Δ bound.

For D≤3t, floor(floor(N/D)/2)≥N/(2D)−1. Therefore d(floor(N/D))≤exp(1/4−N/(8D))≤exp(1/4−t³/24). The function t³/24−1/4−2 ln t is positive at t=8 and strictly increasing for t≥8; hence the last term is at most t^−2.

Inserting the estimates into the companion bound gives the claimed coefficients: 96·60=5760, while 96·550+32·1100+168+1=88169. The remaining terms are 160/t⁴, 288/t⁸, and 96/t^16, using e^−N≤1/N. The displayed total is strictly below 1/100 for t≥10^6, and 1/100<3/32. Consequently the lower side of the absolute-error bound gives risk>3/32. Integer N and ceiling operations have been retained in the estimates; equality at N=K is covered by the companion branch.

This is a human-readable analytic review, not formal verification or a numerical experiment. Only source reading and hashes were used; no tests, enumeration, simulations, source modifications, or external writes were performed.
