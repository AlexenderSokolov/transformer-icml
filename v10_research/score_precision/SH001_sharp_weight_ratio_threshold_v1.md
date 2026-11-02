# SH001 — Sharp weight-ratio threshold by a rescaled rare-suffix tube

2026-11-02. **Author candidate, independent review pending.** Successor to accepted BA001 and SB001 v2; their frozen statements and earlier open comparisons remain untouched. This is a new lower proof, not substitution into BA001's old deteriorating constant.

## 1. Exact experiment and results

Use BA001's stationary second-order experiment, with K>=3 symbols, M>=64, n=M+2, at most D retained scalar coordinates, and trailing windows of length at most r, where D,r>=1 are fixed. Each coordinate is exactly a ratio over all M positions i=3,...,n, with source-independent local tables, actual weights in [1,κ], actual values in [-1,1], and then downward quantization floor(QB_d)/Q. Here κ>=1 and Q>=1 may be REAL; an implementation using integer weights and dyadic Q is a subclass. Query dependence is allowed only through exact first/last-r boundary windows S and public metadata, as in BA001. The decoder receives only this bank, S, and metadata. Arbitrary positional tables and independent shared random seeds are permitted. There are no hard selected-key masks, unbounded values, exact interior side statistics, historical rereads, or recursively global features. At-most-D banks are conceptually zero-padded for the lower, not physically padded for any implementation claim.

The unknown source has stationary pair law Π, starts at its own hidden Π, and obeys the all-state certificate P²(s,t)>=βΠ(t). Loss is TV at the actual terminal query. Write R_stat for minimax risk over this stationary source class, also allowing optimization over admissible encoders. Put

    β0=max(β,1/M), z=κQ,
    H=3^(2r), T0=r sqrt(40DH), C0=4T0,
    N0=ceil(2C0+4)+1, A0=H(2+4r)N0^D, c0=1/(8192A0).

For 0<=β<=1/16 and z<=M/4,

    R_stat >= (c0/z) ln(1+(1/8)min{z/(Mβ0), M/z}).          (SH1)

Crucially c0 depends only on D,r, not κ, Q, β, M, K or table contents. This statement does not assert a matching all-Q two-resource minimax formula.

Fix 0<c_-<=c_+ and C>0. Uniformly over M>=64, β in [0,1], legal Q with c_-sqrt(M)<=Q<=c_+sqrt(M), and κ>=1, any admissible encoder attaining R_stat<=C/sqrt(M) must satisfy

    κ >= c_*(D,r,c_+,C) f,
    f=1+ln(1+Q/[M max(β,1/M)]).                            (SH2)

For fixed K>=3, D>=K³ and r>=3, SB001 v2's SAME paid complete-triple-bank construction with public integer κ=ceil(f) achieves R<=C_suff/sqrt(M), even from arbitrary initialization, where

    C_K=48K³(K+1)+10K^5(K+1),
    C_suff=(2^13+2)K^(5/2)+(2C_K+2K-1)/c_-.

Consequently for each fixed target multiplier C>=C_suff the least feasible weight budget has order Θ(f), uniformly in β and the stated grid band. Necessity holds for every C>0; feasibility for arbitrary tiny C is NOT claimed. In particular β<=1/M gives κ_min=Θ(log M), whereas effective natural score range lnκ_min=lnln M+O(1). For bounded f, the meaningful range statement is 1+lnκ_min=Θ(1+ln f), not a positive lower on lnκ itself. The result is fixed-dimensional and single-global-block only.

## 2. Source, event and integer cutoff

Reproduce the accepted witness to specify the common prior. Choose W,C0,C1, let α=1/(2M), η=β0-α, and p uniform on I=[1/4,3/4]. With p_0=1-p,p_1=p define

    T(W,W)=1-α, T(W,Ci)=αp_i,
    T(Ci,W)=η, T(Ci,Cj)=(1-η)p_j,
    π(W)=η/β0, π(Ci)=αp_i/β0.

Every unused-symbol row is π. Then πT=π and T(x,y)>=β0π(y) on ALL rows. Embed θ_(u,v)(x)=T(v,x), Π(u,v)=π(u)T(u,v); thus P²((u,v),(x,y))=T(v,x)T(x,y)>=β0Π(x,y)>=βΠ(x,y). Initialization is Π, not a deterministic WW start. Its mass Π(W,W)=(1-α/β0)(1-α)>=1/4 is p-independent.

Set

    U=min{1/(4β0), M²/(4z²)}, J=floor(U).

Both arguments of U are >=4 because β0<=1/16 and z<=M/4. Therefore J>=4, J>=U/2, J<=M/4, β0J<=1/4, and z sqrt(J)/M<=1/2. In particular there are integer suffix lengths 2<=j<=J, and n-j>=2; floor endpoints, including U=4, cause no empty range.

Let E_j be the history W^(n-j) followed by j active letters. These events are disjoint and

    e_j=Π(W,W)α(1-α)^(M-j)(1-η)^(j-1)>=1/(32M).

Indeed the three factors apart from α are >=1/4, >=1/2, and >=3/4, respectively. The probability is p-independent. Conditional on E_j the j suffix bits are IID Bernoulli(p), and the SAME uniform prior remains uniform for every j. Grant j to the decoder on these events and a bottom label elsewhere. The true next law there is ηδ_W+(1-η)[(1-p)δ_C0+pδ_C1]; retain the future exit mass η.

## 3. Uniform tube constants after rescaling

For each fixed j, there are at most H possible boundary values s. Freeze q(s) before sampling the entire IID suffix, without conditioning the suffix on S=s. Let A_ds and D_ds be the resulting numerator and denominator and h_ds(p)=E_p A_ds/E_p D_ds. Actual and mean denominators are >=M; |h_ds|<=1. Changing one coin alters at most r summands. The change of either sum is bounded by 2κr. Hence Efron–Stein gives variance <=2κ²r²j for each of the 2DH sums.

Chebyshev plus the union bound yields a parameter-dependent event G_pj of probability >=9/10 on which all sums differ from their expectations by at most κT0 sqrt(j). Exact ratio subtraction, not expectation-of-ratio replacement, gives simultaneously

    |A_ds/D_ds-h_ds(p)| <=2κT0 sqrt(j)/M.                   (3.1)

The derivative identity for an IID Bernoulli polynomial is the sum over coins of expected changes under forcing that coin to 1 versus 0. Thus |(EA_ds)'|, |(ED_ds)'|<=2κrj, and quotient differentiation gives

    |h_ds'(p)|<=4κrj/M.                                   (3.2)

These are uniform over arbitrary public positional tables. At actual S=s, the corresponding frozen ratio is the actual summary. No conditional-IID assertion after boundary observation is used.

Construct an economical mesh of I with gaps <=M/(4r z j); its cardinality is at most ceil(2r z j/M)+1<=2+2r z j/M<=(2+4r)(1+zj/M). Equation (3.2) puts every scaled curve point Qh_s(p) within one of a scaled mesh point in maximum norm. Equation (3.1) and z sqrt(j)/M<=1/2 put every scaled random coordinate within T0 of that curve. Downward rounding adds less than one, also at negative values and real Q. Thus a mesh box of radius C0+2 contains the integer bank QZ, and has at most N0^D possibilities. Its radius is independent of κ. Including s itself, all complete good messages belong to a fixed p-independent alphabet of size at most

    R_j=A0(1+zj/M).                                        (3.3)

The oracle j and metadata are fixed in this conditional experiment. Impossibly overlapping boundary patterns only reduce the count. A randomized encoder's mesh may depend on its independent seed: grant the seed and perform the argument conditionally with the same prior and constants.

## 4. Finite-message loss and harmonic integration

For a uniform parameter on an interval of length ell and good probability >=9/10 at every parameter, a fixed alphabet of at most R good labels forces E|estimate-p|>=ell/(16R). To see this, fix the independent decoder seed. Radius ell/(8R) neighborhoods of its at most R good-label estimates cover at most one quarter of the prior interval. Probability of being good and outside these neighborhoods is >=9/10-1/4; multiply by the radius and then average seeds. Parameter-dependent goodness is harmless; uniform posterior after goodness is never asserted.

For any simplex estimate v, TV(v,θ)>=|v(C1)-(1-η)p|. Apply the scalar lemma to v(C1)/(1-η), with ell=1/2 and 1-η>=1/2. On E_j this gives Bayes risk >=1/[64A0(1+zj/M)]. The common prior and disjoint events imply

    R_stat >=1/(2048A0 M) sum_(j=2)^J (1+zj/M)^(-1).

Put u=z/M<=1/4. Shifting j=k+2, using 1+u(k+2)<=(1+2u)(1+uk), integrating the decreasing function on [0,J-1], and using J-1>=J/2 shows

    sum_(j=2)^J (1+uj)^(-1) >= ln(1+uJ)/(4u).

Also J>=U/2 implies

    uJ >=(1/8)min{z/(Mβ0),M/z}.

These establish SH1. Constants and the prior are uniform in tables and seeds, so source supremum and encoder/decoder infima preserve the bound. The bound is positive but never conflicts with risk<=1: ln(1+x)<=x and the first logarithm argument give RHS<=c0/(8Mβ0)<=c0/8. No uncapped large lower is being asserted.

## 5. Uniform necessity of κ of order f

Write x=Q/(Mβ0), so f=1+ln(1+x), x<=Q, and Q²/M<=c_+². Choose a finite F>=2(1+ln8), F>=1 such that for every s>=F,

    (exp(s-1)-1)/(8 c_+² s) >= exp(s/2)-1.                  (5.1)

Such an F exists because the ratio of the left side to the right side grows asymptotically as exp(s/2-1)/(8c_+²s). This fixes F solely from c_+, independent of M,β,Q,κ.

Exhaust the cases:

* β>1/16: x<=16Q/M<=2c_+ (M>=64), so f<=1+2c_+ and κ>=f/(1+2c_+).
* β<=1/16 but z>M/4: κ>sqrt(M)/(4c_+). Also f<=1+ln(1+Q)<=1+Q<=(1/8+c_+)sqrt(M). Hence κ>=f/[4c_+(1/8+c_+)]. This case uses no tube outside its domain.
* Otherwise SH1 applies. If f<=F, κ>=f/F. If κ>=f, nothing more is needed. In the remaining case f>F and 1<=κ<f, the first branch satisfies

      ln(1+κx/8)>=ln(1+x)-ln8=f-1-ln8>=f/2.

  For the second branch, M/(κQ)>=x/(κc_+²)>x/(f c_+²). Since x=exp(f-1)-1, (5.1) yields

      ln(1+M/(8κQ))>=f/2.

  The logarithm of 1 plus the minimum equals the minimum of these two logarithms. SH1 and Q<=c_+sqrt(M) therefore give

      C/sqrt(M)>=c0 f/(2κQ)>=c0 f/(2κc_+sqrt(M)),
      κ>=c0 f/(2Cc_+).

Taking the minimum of the five positive constants 1, 1/(1+2c_+), 1/[4c_+(1/8+c_+)], 1/F, c0/(2Cc_+) proves SH2 for ALL stated M,β, not just eventually. The c_- parameter is needed for sufficiency, not this necessity.

## 6. Sufficiency, cap, and integer versus real budgets

Only the accepted SB001 v2 upper is imported. Its full retained K³ bank, paid triple features, weights exactly {1,κ}, post-grid block normalization (including all-zero fallback), and implementation ledger are unchanged. Its §3 proof covers J=0 and positive J whose entire selected block floors to zero; SH001 adds no uncharged side statistic or pre-grid normalization. Its §7 provides for every public integer κ>=1

    R<=min{1, 2^13Hstat+Ψ(K^5/(M+1))
                     +C_K[1+ln(1+κQ/(Mβ0))]/(κQ)+(2K-1)/Q}.

Here Hstat<=K^(5/2)/sqrt(M+1), Ψ(x)<=2sqrt(x), and Ψ's cap includes x>=1. Choose κ=ceil(f), so f<=κ<f+1<=2f. Since 1+κx<=κ(1+x),

    [1+ln(1+κx)]/κ <=(f+lnκ)/κ<=2.

This yields the stated C_suff. The minimum with 1 remains valid at small M; it does not obstruct the claimed C_suff/sqrt(M) inequality. The lower allows all real budgets, and hence also integer ones. If a real envelope is prescribed, the integer sufficient budget is ceil(f)<=2f, not an assertion that a noninteger weight is implemented. The dyadic-grid implementation uses legal Q=2^h,h>=4 within the band; the lower itself permits real Q. A band containing no legal Q for some M has no instance at that M.

For an infimum definition of least feasible κ, SH2 applies to every feasible budget and hence its infimum, while the integer candidate supplies a feasible budget <=2f. No minimum-attainment assumption is necessary. Upper arbitrary-start feasibility implies stationary feasibility; conversely the stationary lower obstructs arbitrary-start guarantees too. The optional known-β selection rule is a public budget specification, not an uncharged transcendental runtime primitive. SB001's caveat about additional paid rational-input selection costs remains unchanged. Its β-blind bitlength schedule still supplies κ=O(log M) without β input.

## 7. Source bindings and evidence limits

Direct dependencies: BA001 v1 §§1–5 for the exact family, witness, query-freezing and Bayes method; SB001 v2 §§2–3,6–7 for paid construction, all-zero/cap handling, upper and ledger. Read both accepted manuscripts, both acceptance records, and the corresponding independent reviews. This proof changes the cutoff and tracks its consequences explicitly; it does NOT claim BA001's original finite constant was κ-independent. BA001 BA2 and SB001's weaker κ^(-(D+1)) lower remain true but are not used to obtain SH2. The old open optimal-κ comparison is closed here only in the specified Q~sqrt(M), fixed-K,D,r regime, conditional on successful review and root acceptance.

No implementation changes, new emitted-network execution, external literature novelty claim, formal verification, deep-family lower, growing-dimension sharpness, or all-Q matching resource tradeoff are claimed. Finite diagnostics corroborate algebra only. See SH001 source bindings and diagnostics beside this manuscript.
