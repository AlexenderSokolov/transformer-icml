# BU001 v2 independent delta review

2026-11-02. **Recommendation: PASS for BU1 and explicit BU2-v2 within the stationary binary and inherited legal SB001 parameter domain.** Not root acceptance. Read the complete v2 and actual v1→v2 diff; this supplements the full fresh review `BU001_review_v1.md`.

Candidate v2 SHA-256: `2dc9cf9d13faa6cfa15fffd5ec83a67326ccc95eb6a63291c7b2349136b166f5`.

## Delta audit

1. The explicit supported irreducibility paragraph is correct: support closure follows from stationarity and P²(s,t)>=beta p_t>0 gives finite supported hitting/return means. The q=0 paragraph correctly omits zero contributions before division and handles singleton support. Its appeal to e²>=beta y is justified because irreducibility already rules out a supported absorbing00 alongside positive x. In fact nontrivial positive-beta binary support must contain all four states: y=0 would force e=0 and P²(10,01)=0 despite x>0; w=0 similarly forces P²(01,10)=0. The author's smaller-support analysis is harmless and does not weaken the argument.

2. The earlier crossing-weight notation concern is fully resolved. v2 distinguishes q_actual from q_s=1 and explicitly uses the direct floor bound for crossing rows. Equation (4.1) follows by the pathwise add-one comparison on J>0 and the unconditional actual-terminal comparator S. No conditional independence or estimator substitution occurs.

3. The floor algebra and signs are valid. On N>=1, N integer implies N>=1, and positive/negative deviations are respectively bounded by p_hat/N and (1−p_hat)/N, with complementary trivial bounds. Equation (4.2) follows with exactly two empirical-error copies. The integration is **2S+2B**, not 2S+B or an unjustified true-exit comparison on crossing rows.

4. Empty selected block implies Qr<2 on J>0. The rearrangement (Q−2)kappa J<2(M−J), Q>=16, implies J<4M/z. Since 4M/z>0, J=0 already satisfies that strict inequality. For integer J, {J<c}={J<ceil(c)} even when c is an integer; w=ceil(4M/z)>=1 therefore suffices without the extra +1 used in v1. Universal occupation gives 16ceil(4M/z)/(M+1)<=64/z+16/M. Uniform fallback remains unchanged. Final ordered rounding charges 1/Q, giving total **3/Q** in (4.4).

5. Substitution A=6M/z into BU1 gives exactly 24/z[17+ln(1+16z/(sqrt(beta)M))]. For x>=0, 1+16x<=16(1+x) and ln16<3 imply

       24[17+ln(1+16x)] <=480[1+ln(1+x)].

   Adding 64/z and using 1+ln(1+x)>=1 gives **544[1+ln(1+x)]/z**. There is no missing factor of four, smoothing factor or stationary mass.

6. From S<=2^13sqrt(32)/sqrt(M+1) and B<=2sqrt(32)/sqrt(M+1),

       2S+2B+16/M
       <=[(2^14+4)sqrt(32)+16]/sqrt(M)
       <[(2^14+4)6+16]/sqrt(M)
       <2^17/sqrt(M).

   Thus **2^17** is valid uniformly, with considerable slack. For beta<M^−2 (including beta=0), the actual SB beta-free bound has Psi(32/(M+1)) and Psi(96/z), since K^5=32 and K^5(K+1)=96. Its numerical term is <=96[1+ln(1+z)]/z and statistical terms fit 2^17/sqrt(M). The equality beta=M^−2 is handled by BU1; e0=1/M on the other branch. The final cap is exactly min{1,derived upper}, not a cap that would invalidate any constant.

7. Added implementation paragraph correctly inherits every SB001 v2 §6 resource charge and the same 8-coordinate bank. No new ports or online analysis variables appear. Public kappa,Q must still be legal SB configurations (integer kappa>=1, Q=2^h,h>=4), as expressly stated in the final paragraph. AU001's residual-mixture theorem is not needed and no arbitrary-start extrapolation is made. Calling BI001 background rather than using its accepted lower is harmless: BU upper does not depend on BI.

## Fresh diagnostic evidence

The independent v1-named diagnostic is equally applicable to unchanged BU1 and v2's floor/decoder algebra. Actual run PASS: 625 rational kernels; 209 positive genuine all-state certificates (128 zero-support singleton cases); 324 relevant hitting targets; 1,296 moment checks through order4; 3,888 finite count-functional checks; 280,694 positive-floor cases; 13,584 decoder algebra cases. Rational checks are exact; transcendental exponential/logarithmic checks are numerical only. The observed maximum of beta(pqH)^2 is 1, below the theoretical 25. This is finite corroboration, not universal proof.

All requested exact constants, support cases, J=0, beta=0 and stationary-only scope pass independent review. The only downstream presentation requirement is to retain the legal SB domain and no arbitrary-start or unrestricted lower-match claim. No candidate/accepted source was edited and no acceptance was written.
