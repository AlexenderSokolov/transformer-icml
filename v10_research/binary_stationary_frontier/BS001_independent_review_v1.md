# BS001 — Fresh independent synthesis review

2026-11-02. **PASS recommendation within the stated stationary binary domain; not root acceptance.** Reviewed corrected candidate SHA-256 `ca116bd9c9a8ee88c62be85d5f0352c2d4f7b3d7df84df6406036c94ac86cb2b`. One extra closing parenthesis in (5.1) was reported and corrected by the author before this binding. No mathematical revision was needed.

## Scope and dependency evidence

Read the complete candidate and the accepted BU001 v2, BI001 v2, UI001, TR001 and SB001 v2 source text supplied in the review context; independently inspected current acceptance receipts and the BU/BI delta reviews. The fresh diagnostic verifies all five proof hashes against their actual receipts. This is a composition audit of accepted lemmas, not a new blind reproof of every dependency. The candidate's status line remains correctly unaccepted pending root disposition.

The exact family keeps at most D scalar downward-grid local positive-weight ratios, finite boundary side information, arbitrary positional/query tables, and unrestricted post-cut decoding. The paid upper uses the included eight-coordinate bank for D>=8,r>=3. At-most-D padding is only a lower-bound inclusion. All-state minorization and actual-terminal stationary loss are preserved. There is no illicit IID-query or arbitrary-start replacement.

## Mathematical audit

1. **Imported constants/domains.** The displayed UI constant reproduces its H,F,q,L,J,V,C,P,R definitions. BI's c_B=1/(524288 A_B), H_B=2^(2r), T_B=34r sqrt(64DH_B), mesh cardinality and N_B match the accepted binary lower. BI is used only at beta<=1/256 and z<=M/4. The proof never imports the K>=3 rare-suffix lower at K=2. The statistical two-point floor c_S=1/256 is conservative and valid after granting full history. The separate minimax lower witnesses are combined by a maximum, not an unsupported common witness or sum.

2. **Exhaustive completion.** For beta>1/256, e0>1/16 and W<=1/Q+16/M<=1/Q+2/sqrt(M). This branch permits min(c_I/2,c_S/4). For z>M/4, monotonicity gives W<5/sqrt(M). For z>M^(3/4), sqrt(M)<=z^(2/3) and (1+ln(1+z))/z^(1/3)<=1+ln2+3/e<3; the same slack constant5 applies. The remaining domain satisfies x=z/t<=z<=y^3 with y=M/z>=4, so log(1+x)<=24log(1+min(x,y)/8). Therefore W<=1/Q+24L and min(c_I/2,c_B/48) is sufficient. The single c=min(c_S/5,c_I/2,c_B/48) is below every branch constant and both separate floors. Boundary equalities belong to the remaining domain, so no gap is hidden at z=M/4, z=M^(3/4), beta=1/256 or M=64.

3. **Upper and cap.** BU2 gives precisely 2^17/sqrt(M)+3/Q+544W, hence C=131619. The beta=M^-2 equality is covered by the positive-beta argument, while beta=0 uses the inherited beta-free estimate. No constant depends on the weight envelope. The upper is stationary only, and its inherited zero-bank charge prevents treating a vanished row as an observable count. Since F<1/4 in the full domain, the claim does not omit a separate unit-risk regime.

4. **Joint threshold.** For u=a/t and v=z/a, inversion of [1+ln(1+vu)]/v<=B is correct both when v>=1 and when v<1. In the latter case concavity gives f<=B, while the numerator's unit term gives v>=1/B, hence v>=f/B². Thus the stated necessary product threshold is valid even for an infimum risk. For sufficiency, 1+fu<=f(1+u) yields W(af,t)<=(f+ln f)/(af)<=2/a. The separate Q floor is retained. The dyadic allocation Q=2^max(4,ceil(log2 a)) satisfies a<=Q<=2a even at the smallest M=64; ceil(Z_star/Q) yields a legal integer envelope.

5. **Square-root band and alphabet contrast.** The direct inequality W(kappa Q,t)>=f_Q/(kappa Q) proves the real-envelope necessity. The program upper instead uses integer ceil(f_Q), at most2f_Q, and W<=2/Q. Its explicit sufficient multiplier 2^17+1091/c_- is exactly 2^17+(3+2*544)/c_-. The least feasible integer exists for these targets, not for every tiny target. At beta=1/M the binary cutoff gives t=sqrt(M), hence f_Q bounded; TR001 for each fixed K>=3 gives t=1 and f_Q of log M order. Common fixed D>=K^3,r>=3 is permitted, but architecture-dependent constants cannot be suppressed into a uniform alphabet claim. This qualification is present.

6. **Costs and limitations.** The complete eight-coordinate program, two paid copy heads, all-token work, dense maps including zeros, exact arithmetic widths, masks/cache/controller costs, addressed-sequential and PURE alternatives reproduce SB001's unchanged ledger. No lower statistical budget is advertised as smaller full arithmetic precision or total computational cost. The improved arbitrary-start binary frontier is explicitly left open; TR001 cannot supply that missing inference. No external novelty, formal verification or unrestricted neural-architecture claim is made.

## Fresh independent diagnostics

`BS001_independent_checks_v1.py` was designed and run without importing or executing the author's diagnostic. Actual result **PASS** in `BS001_independent_checks_v1.json`:

- 27,646 parameter cases including branch equalities, adjacent floating-point values, legal dyadic/integer budgets, additional real-envelope cases, and logarithmically randomized extreme scales;
- 1,265 high-beta branch checks, 17,333 large-z checks, 20,835 z>M^(3/4) checks, 6,302 remaining-domain log comparisons (overlaps intentional);
- 27,646 each of threshold inversion, threshold sufficiency and legal integer/dyadic allocation checks;
- all five dependency receipt SHA-256 checks passed.

Observed maxima include W/s=1.91661 in branch B, 1.47164 in branch C (both bounded by5), aW(Z_star,t)=1.34067 (bounded by2), and QW(ceil(f_Q)Q,t)=1.33330 (bounded by2). These are finite floating-point corroborations with relative tolerance2e-12, not universal proof, exact transcendental verification, or an independent re-audit of every source-chain lemma. The mathematical recommendation rests on the written proof and precisely accepted dependencies. No author proof, old source, intake receipt or frozen delivery file was edited by this reviewer.
