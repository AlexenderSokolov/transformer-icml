# Independent review: terminal quantization of one exact injective scalar

2026-11-12. Verdict: PASS for the frozen representation and centered terminal-only quantizer. This is not a finite-precision execution theorem or a lower bound for all networks.

Reviewed THEOREM.md SHA256 d85a93a34b1f0eae28a37ed13a5310ba199194d1e1c2d0350d63729522087402; check.py SHA256 078d2cda930d79738c462c2933ab4e786023a11060884b97b4a27fc2e215837c; results.json SHA256 761a68c650632535473aa039abd4a95926626517bbd7d261566dcca2245057ff; RECEIPT.json SHA256 d48528b58f0317092438dfd32d5e87090c187867f908a64c230490a6d2e4f6ba. I also reread the complete inherited width-4 actual-PreLN encoder in fixed-c-bridge/BRIDGE_OBSTRUCTION.md rather than treating injectivity as a new numerical claim.

## Representation and variance

The displayed v_i, gamma_i and public denominator reproduce that encoder's terminal attention scalar exactly. Scores/exponent parameters do not depend on word signs. The Lindemann-Weierstrass injectivity premise is the existing analytic theorem; no numerical gap bound is inferred. The loose bound 0<w_i<=W/N with W=2exp(4) is valid and |A|<2.

For stationary three-spin source, means are zero. The recursion X_(i+3)=Z_i Z_(i+1) X_i gives E X_i X_(i+3r)=theta^(2r); other residues have zero expectation after averaging the uniform initial pair. The covariance absolute row sum is bounded by (1+a^2)/(1-a^2). Therefore Var(A)<=W^2(1+a^2)/[(1-a^2)N] is valid, uniformly over the fixed-c class. It is an actual source-average variance bound for deterministic weights, not an assumption about evolved hidden-state mixing.

## Centered quantization and endpoint coupling

The nearest grid is specifically centered at zero. Y!=0 implies |A|>=Delta/2, including the fixed boundary convention, so Chebyshev supplies the displayed tail bound. Under each source, couple (Y,T) to (0,T) on the same word. Since T is uniform under both sources, the reference law is exactly the same delta_0 times uniform pair law, even though A and T need not be independent. The joint-TV comparison follows from coupling and a triangle inequality. No conditioning on the endpoint or count is used. If zero lies on a quantizer boundary, or a preprocessing rescaling is introduced, this proof cannot be reused without charging that change. For Delta=N^-beta, beta<1/2, the tail probability tends to zero; no fine-grid conclusion is obtained.

## Information statement

I(X;Y|T)<=H(Y) and H(Y)<=h2(epsilon)+epsilon log2(M-1) follow by separating the zero label. The label-count M=floor(4/Delta)+2 safely bounds a grid in (-2,2). Since epsilon=O(N^(2beta-1)) and log M=O(log N), the stated information upper tends to zero. The exact-real comparison H(X|T)=(N-2)h2((1+theta)/2) is valid: for any fixed innovation word, each update (a,b)->(b,Zab) is a bijection on the four pairs. The uniform initial pair therefore maps to a uniform terminal pair independent of all innovations. Exact A injectivity then retains the full conditional word entropy. This statement concerns exact observation information, not the bounded actual final head's useful prediction.

## Risk and arbitrary decoders

On a common observed (Y,T), the two source targets differ by h, with the sign determined by the shared terminal parity. Integrating triangle inequality over the common part of the two observation measures yields equal-prior absolute risk at least h(1-TV)/2. This is valid for any measurable decoder of (Y,T), including independent randomized decoders. Free endpoint disclosure is explicitly included in the observed measure, rather than silently assumed independent of Y. The bound is a two-source Bayes/max-risk result for this quantized representation; it says nothing about every possible architecture encoding.

## Resolution limits

Whole-word success under the iid source is at most 4M/2^N when the endpoint is also supplied. Thus p>=N-5+log2(1-rho) is a necessary coarse counting bound for success 1-rho. It is not sufficient, and whole-word recovery is not needed for good next-token risk. Exact finite-N injectivity provides g_N>0 but no effective lower bound. Delta<g_N is sufficient for injective quantization; additive observation error below g_N/2 is sufficient for nearest-codeword recovery. The pigeonhole upper g_N<=4/(2^N-1) and the explicit warning that linear p may be insufficient are both correct. None of these statements concerns rounding every intermediate layer.

## Independent diagnostic replay

I ran the frozen script and compared parsed JSON against results.json: all fields matched, including 108 assertions. The checks enumerate small source laws with binary64 encoder weights and support covariance/TV bookkeeping. They do not certify exact transcendence, minimum gaps, large-N thresholds or an actual intermediate finite-arithmetic implementation. The analytic constants are loose and may be vacuous at these small sizes.

Conclusion: the candidate correctly contrasts exact information retention with coarse-grid statistical collapse for one already audited encoder. The centered grid, fixed scale, terminal-only quantization, fixed-c stationary source, and restricted observation (Y,T) are essential. Alternative macroscopic statistic encoders, additional channels, adaptive quantizers or fine grids remain outside the theorem. No novelty or formal-verification claim is certified by this review.
