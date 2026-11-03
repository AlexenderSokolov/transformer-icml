# CMF001 — uniform communication cost up to the channel-identifiability boundary

2026-11-03. New local author candidate; not independently reviewed or root accepted. No accepted or published artifact is modified. Historical pending headers in dependencies are superseded only by their acceptance receipts. No publication, repository operation, calibration guarantee, or novelty certification is claimed.

## 1. Result and quantifiers

Fix a finite nonempty output alphabet Y and known nominal binary-input channel W0=(P0,P1) with d=TV(P0,P1)>0. At each horizon M a known radius α may be ANY element of [0,d/2), including an arbitrary M-dependent choice. Write

    Uα={W=(Q0,Q1): TV(Qb,Pb)≤α, b=0,1},
    γ=d/2−α>0, L_M=1+ln((M+2)/2),
    T(M,α)=ln M/[1+ln(1/α)] if α>0; T(M,0)=0.

The hidden true W is fixed within each experiment and is fresh memoryless conditional on the complete pre-channel state. It need not be fixed across M. Define H by the NOMINAL supports S_b={y:P_b(y)>0}:

    S0∩S1=∅:                    H=1+T(M,α);
    S0∩S1≠∅ and S0≠S1:          H=ln L_M+T(M,α);
    S0=S1 (rows distinct):       H=ln M.

There are two distinct observation models, specified in §2. For either source class j=F,O2, at the fixed feasible target B_j=G_j+2, the minimum fixed physical binary-input length satisfies

    SUPPLEMENTAL model: R*_sup,j(M,α)=Θ_(W0,j)( H(M,α)/γ² ),      (A)
    WHOLE-MESSAGE model: R*_all,j(M,α)=Θ_(W0,j)( ln M/γ² ).        (B)

Both comparisons hold for ALL M≥M0 and ALL 0≤α<d/2, with ONE threshold M0 and positive constants independent of α or its schedule. Thresholds and constants may depend on nominal rows, source interface and the fixed target. The lower necessities hold for every fixed finite positive target B, not just B_j; the upper only asserts the stated feasible targets or larger ones. No factor below the statistical floor is promised. These are order results, not optimal leading constants or exact risk curves.

In particular on d/4≤α<d/2 both models require Θ(ln M/γ²). Thus an arbitrarily fast approach to the identifiability boundary has an explicitly charged γ^(-2) communication cost, even for arbitrary randomized full-word codes rather than repeated gates alone. At α=0 the supplemental support distinctions survive, whereas the whole-message length remains Θ(ln M). The factors d-dependent in the proof are permitted because the nominal channel is fixed; no uniformity as d→0 is claimed.

For α≥d/2 the identical-row midpoint channel is admissible. In the supplemental model the robust minimax factor equals the no-message baseline exactly for every finite length. In the whole-message model worst clean risk is at least 1/8 at every finite length. If d=0, these impossibility statements apply for every α≥0; (A),(B) do not apply.

## 2. Experiments and imported statistical interfaces

The raw word is X_0,...,X_(M+1). A single source-independent offline attack kernel, defined on ALL words, changes at most k positions among 0,...,M−1 on EVERY outcome and protects both terminal symbols. Here k ranges over all integers 0,...,M and is hidden from the procedure. The kernel cannot inspect encoder/decoder random seeds or future channel noise. The encoder scans the full corrupted word. One fixed rule at (M,W0,α,j) must work over the entire joint supremum of sources, starts, k, kernels and W∈Uα.

**F:** arbitrary binary first-order transition table with arbitrary initial PAIR law; the initial edge need not follow the transition table. Upper bounds use the accepted FOT002 repaired suffix gate, discarding X0. Lower witnesses are stationary first-order and also obey the all-state pair certificate 1/M; restricting F to this certificate does not weaken our lower. The target is the next-symbol distribution at the actual final symbol.

**O2:** homogeneous binary order-two θ_ab(c), admitting a stationary pair law Π and supplied all-state certificate P²(u,v)≥Π(v)/M for EVERY pair u,v, including unsupported rows. Every initial pair law is allowed. The target is the next-SYMBOL distribution θ_(X_M,X_(M+1)), not a next-pair distribution. Upper bounds use the original accepted O2 half gate, not F's repaired suffix gate. No unrestricted/no-mixing O2 or all-certificate theorem is asserted.

**Supplemental receiver:** exact eight triple counts of the corrupted word and the actual protected final pair are free. The initial pair is reconstructed by flow imbalance; it is not an extra observation. No additional raw windows are free. The lower may be proved in the richer first/last-two-symbol baseline, since it includes the stated receiver's information and relocation preserves it.

**Whole-message receiver:** NO sample-dependent information is free, including counts, endpoints, query, edit locations, raw windows or encoder state. All such information must pass through the R binary inputs. Only public experiment parameters and independent public randomness are free.

In either model R is a fixed integer chosen before observing the sample. Independent private coins and independent free shared seeds are permitted. Conditional on the entire pre-channel experiment and these seeds, the channel is W^R. No feedback, variable/adaptive length, timing channel, path-dependent shared seed, revealed noise seed, calibration samples, or additional channel observations are available. W is not chosen based on the realized seeds or inputs. Receiver output is a predictive distribution; loss is unconditional expected unsquared TV at the actual terminal target, with

    g_M(k)=max{M^(-1/2),k/M}.

The robust factor is infimum over ONE encoder/decoder of the joint supremum of risk/g_M(k). No minimax interchange or attainment is needed. R* is the smallest integer for which a rule attains the target; the constructions supply a nonempty feasible set, and the lower bounds exclude smaller lengths. Lower bounds also hold directly for infima by approximation.

The accepted FOT002/BCC001/O2T001 interfaces, imported through CAF001 and UWC001, supply exact-gate/exact-payload risk at most G_j g_M(k), baseline factor between c_j L_M and C_j L_M, and full-history normalized floor 1/96, where

    G_F=1024+2^20, c_F=2^-33, C_F=2^17;
    G_O2=2^17+2^23, c_O2=2^-30, C_O2=2^20.

Their stronger risks are 1024/√M+2^20 k/M and 2^17/√M+2^23 k/M. These are accepted statistical dependencies, not independently rederived here. FOT001/BSC001's finite source-mixture lemma is explicitly isolated in §5.

## 3. A constrained-risk inequality with the correct orientation

Let P be the observation law on the CLEAN comparison word and Q the observation law on its relocated attacked word, with Q≪P. Include independent decoder coins as an extra coordinate, or fix them before this argument. Define the ordered affinity

    A(Q,P)=∫(dQ/dP)² dP=1+χ²(Q||P).

Let nonnegative pointwise losses ℓ0,ℓ1 satisfy ℓ0+ℓ1≥Δ≥0. Write a=E_P ℓ0, b=E_Q ℓ1, and A(Q,P)≤ρ. Then

    √ℓ0+√ℓ1≥√Δ,
    E_Q√ℓ0=E_P[(dQ/dP)√ℓ0]≤√(ρ a),
    E_Q√ℓ1≤√b.

The first follows by squaring; the second is Cauchy–Schwarz; the third is Jensen (or Cauchy–Schwarz). Consequently

    b≥(√Δ−√(ρ a))_+²≥Δ/2−ρ a.                   (1)

For the last inequality, if v≥u≥0 then u²/2−v²≤0; if v<u then (u−v)²−(u²/2−v²)=2(v−u/2)²≥0, with u=√Δ and v=√(ρa).

This is a self-contained standard constrained-risk argument, not a claim of a new inequality. Crucially a is the CLEAN actual-terminal risk in the source-mixture application; Q/P, not P/Q, appears in the Cauchy–Schwarz step. We prove both ordered channel affinities below so either pair of encoded words is covered. Averaging pointwise inequalities conditional on independent public seeds is legitimate with a uniform ρ; changing the seed law according to the word or attack would not be.

## 4. A least-informative admissible channel and arbitrary-code affinities

For 0≤α<d/2 define signed measure ν=P1−P0, probability μ=(P0+P1)/2, and s=γ/d∈(0,1/2]. Set

    Q0*=μ−sν, Q1*=μ+sν, W*=(Q0*,Q1*).             (2)

These are probability distributions because |ν|≤2μ pointwise and s≤1/2. Direct subtraction gives

    TV(Qb*,Pb)=(1/2−s)d=α.                       (3)

Thus this witness lies exactly on the allowed row boundaries. Symbols with μ(y)=0 have ν(y)=Q0*(y)=Q1*(y)=0 and are omitted in sums. No true channel in the full uncertainty ball is assumed to omit them; only this legal lower-bound witness does.

On the near-boundary interval α≥d/4 we have s≤1/4 and both Qb*≥μ/2. Since Q1*−Q0*=2sν,

    χ²(Q1*||Q0*)=Σ_y 4s²ν(y)²/Q0*(y)
       ≤8s²Σ_y ν(y)²/μ(y)≤32s².

The last bound uses ν²/μ≤4μ and Σμ=1. Reversing the rows gives the same bound. Put

    ζ=1+32γ²/d²>1.                               (4)

For two arbitrary fixed R-bit words h,h', product factorization gives

    A(W*^R(·|h),W*^R(·|h'))≤ζ^R.                 (5)

This includes identical coordinates (affinity 1) and R=0. It persists for UNRELATED randomized encoder mixtures. Explicitly let f_i,g_j be the corresponding product pmfs and p_i,q_j any two mixing distributions. At each output v, Cauchy–Schwarz with weights w_ij=p_i q_j yields

    (Σ_ij w_ij f_i(v))²/(Σ_ij w_ij g_j(v))
       ≤Σ_ij w_ij f_i(v)²/g_j(v).

Indeed apply Cauchy–Schwarz to √(w_ij g_j) and √w_ij f_i/√g_j. All denominators are positive on the common effective alphabet; zero common coordinates contribute zero. Summing v proves A(Σp_i f_i,Σq_j g_j)≤ζ^R. This is the elementary joint-convexity proof for χ², not an assumption that encoder outputs agree under relocation.

Conditional on each independent shared seed, the encoder distributions may change arbitrarily but (5) remains uniform. Adding independent decoder coins with the same conditional law preserves the affinity. Thus (1) applies to the SAME decoder at any common baseline, before averaging the free seed. The source attack never selects or conditions on that seed.

## 5. Finite FOT mixture transport, now using affinity

Use N=M+1 ordinary edges, r=2, c=2^-16, A=2^12,

    x=ck, t=x/N, u0=floor(x/4), T=floor(N/8),
    I=[At,1/4], L=ln(1/(4At))=ln(4N/k),
    β=1/(N−1), ρ_stat=u0/(8Nt).

The following accepted FOT001/BSC001 source lemma is imported under its exact finite hypotheses:

    N≥64, 2≤r≤k/128, k≤N/8, x≥4096,
    At<1/4, N/k²≤A c²/2^20=2^-40.                 (6)

For stationary first-order alternatives Q_a with transition probabilities T_a(0,1)=a, T_a(1,0)=t, a∈I, let F be the event of first pair 11 and final pair 00. There is a measurable good event G and deterministic relocation C_r such that:

* on F∩G, y and C_r(y) have the same full baseline and final pair 00;
* writing j=J00(y) for pair-departure occupation, 2≤j≤T and C_r(y) is within strict budget k of x^(j)=1^(N+1−j)0^j, with the same protected final pair;
* (a−β)Q_a(F∩G)≥t/64;
* finite measures ν_j(dy)=∫_I Q_a(dy;F,J00=j,U≥u0) da/a, where U is ordinary 01 count, have masses μ_j≤t/u0;
* the stationary null with T_*(0,1)=β and T_*(1,0)=1/[2(N−1)] assigns v_j=Q_*(x^(j))≥1/(8N).

The underlying identities use ordinary 00 count v=j+1 on F, not v=j; the null input has J00=j−2, and is NOT claimed to share the proposal histogram. Only the relocated OUTPUT shares the clean proposal baseline. All alternatives and the null satisfy every row of P²(u,v)≥Π(v)/(N−1), via T(d,s)/π(s); this embeds the witnesses in O2 as θ_ab(c)=T(b,c). The complete mixture counting, good-mass estimates and relocation proof remain the accepted dependency, not a consequence of affinity.

Predeclare one attack using only (N,k,r) and these auxiliary measures. On x^(j) with μ_j>0 draw exactly one Y from ν_j/μ_j. If relocation is defined, accept C_r(Y) only after testing its actual Hamming distance ≤k and actual protected pair equality; otherwise return the input. On every other input return the input. Do not resample after rejection. This is one source-independent kernel on ALL words, independent of predictor seeds, source table and channel outcomes. All proposals in F∩G pass.

Fix any full protocol and freeze W=W*. Let ℓ_a(y) be its expected TV loss on CLEAN y against the actual-terminal Q_a target, averaging channel and independent protocol coins. Outside F it is NOT globally replaced by loss against parameter a; inside F its target is a. Let b_a(y) be its expected null-target loss on C_r(y), on F∩G. The two targets there are a and β, separated by a−β. By §§3–4,

    b_a(y)≥(a−β)/2−ζ^R ℓ_a(y) on F∩G.            (7)

Let S=sup_(a∈I) E_Qa ℓ_a(Y), the unconditional clean actual-terminal risk. First discard unused null inputs, rejected proposals and accepted proposals outside G. Replace v_j/μ_j by its lower bound ρ_stat ONLY while multiplying nonnegative actual null losses. Only AFTER this operation insert the possibly signed (7). Therefore

    R_null ≥ρ_stat ∫_I E_Qa[1_(F∩G) b_a(Y)] da/a
       ≥ρ_stat ∫_I [(a−β)Q_a(F∩G)/2
                         −ζ^R E_Qa(1_(F∩G)ℓ_a(Y))] da/a
       ≥ρ_stat (t/128−ζ^R S)L.

Nonnegativity supplies the positive part:

    R_null ≥ρ_stat [(t/128−ζ^R S)L]_+.             (8)

The original t/64 gap has only been halved. No signed-loss expression was transported by a smaller coefficient. This is the load-bearing change from the L∞ likelihood argument of BSC001; its source kernel and certificates are unchanged.

For the same rule let Γ_N be its worst source/attack factor under fixed W*, normalized by g_N(k)=max{N^-1/2,k/N}. Then S≤Γ_N/√N and R_null≤Γ_N g_N(k). If Γ_N=∞ the conclusion is immediate; otherwise, for k≥√N, rearranging (8) gives

    Γ_N ≥ρ_stat c L /[128(1+ρ_stat ζ^R L√N/k)].    (9)

There is no rule-dependent constant and no optimizer assumption. The robust supremum includes W*, so infimizing over robust rules preserves the inequality.

For N≥2^160, r=2 and k=ceil(N^(3/4)), all of (6) hold as in the accepted BSC001 finite arithmetic. In particular

    1/64≤ρ_stat≤1/32,
    (ln N)/4≤L≤N^(1/8), k≥N^(3/4).

If ζ^R≤N^(1/8), then ρ_stat ζ^R L√N/k≤1/32<1. Weakening the denominator of (9) to 256 and using c=2^-16 gives

    Γ_N≥2^-32 ln N.

The horizons must be converted: g_N≤g_M≤[N/(N−1)]g_N for the same k. Thus

    M+1≥2^160 and ζ^R≤(M+1)^(1/8)
       ⇒ Γ_rob,sup,j(M,R,α)≥2^-33 ln(M+1).        (10)

This finite implication has no hidden γ-dependent threshold. Once 2^-33 ln(M+1)>B, every protocol attaining factor at most B must satisfy, for d/4≤α<d/2,

    R>ln(M+1)/(8ln ζ)
      ≥d² ln(M+1)/(256γ²),                       (11)

because ln(1+32γ²/d²)≤32γ²/d². The same necessary inequality follows if only the minimax infimum is ≤B. It holds at every such M, not merely along a fixed-γ limit.

## 6. Supplemental upper and assembly of the full frontier

Let A_nom={y:P1(y)>P0(y)}, p_b=P_b(A_nom), τ=(p0+p1)/2. Then p1−p0=d, and every W∈Uα has

    Q0(A_nom)≤τ−γ, Q1(A_nom)≥τ+γ.

Repeat the accepted source-class gate R times and decode 1 iff the empirical frequency of A_nom is at least τ. Conditional on each complete pre-channel state and on either bit, the error probability is at most exp(−2Rγ²). This follows from the Bernoulli centered log-mgf bound f''≤1/4, hence f(t)≤t²/8, and exponential Markov. Ties belong to the bit-0 closed upper-tail event and are included in that bound; the bit-1 error is contained in its closed lower tail.

Couple the noisy and exact-gate predictors using identical receiver coins. Loss is at most one and they coincide on correct decoding, so

    Γ_rob,sup,j≤G_j+√M exp(−2Rγ²).

Consequently R=ceil(ln M/(4γ²)) attains G_j+1 for M≥64. This algorithm never uses unknown-W likelihoods or calibration. Together with (11) it proves the near-boundary Θ(ln M/γ²) statement uniformly in α≥d/4.

For 0≤α≤d/4, apply the accepted CAF001 theorem with the FIXED αmax=d/4<d/2. It supplies uniform Θ(H) with threshold independent of α at the target G_j+2. Its support-aware upper and finite likelihood lower are used as an accepted interface, not rederived from a nonuniform fixed-radius asymptotic. On this interval d/4≤γ≤d/2, so 4/d²≤γ^-2≤16/d². Multiplying H by γ^-2 changes only nominal constants.

On d/4≤α<d/2, the denominator 1+ln(1/α) lies between the positive fixed constants 1+ln(2/d) and 1+ln(4/d). Hence T(M,α) is uniformly comparable to ln M. For M≥64, 1 and ln L_M are bounded by constant multiples of ln M. Therefore every H is uniformly comparable to ln M on this near interval. Combining the two intervals proves (A), including their shared endpoint α=d/4 and α=0. Take the maximum of CAF001's threshold with 2^160−1, 64, and a threshold ensuring 2^-33 ln(M+1)>B. None depends on α or γ.

## 7. Whole-message upper with fully paid sample-dependent payload

UWC001 proves the following explicit uniform coding inequality. For any payload length B_payload≥1, put m0=ceil(4/γ²). Nominal-event repetition makes each hard bit have maximal conditional error ≤e^-8<2^-8. Its fixed-distance binary inner code, nearest-Hamming decoder, and Reed–Solomon/Welch–Berlekamp outer decoder then give

    R≤240 m0 B_payload,
    Pr(message error | every payload, W)≤2^(-6 B_payload)         (12)

for every W∈Uα. All calculations in that proof are pointwise in m0 and γ; they do not require α to be independent of M. We import that accepted finite construction, not its former fixed-gap Θ statement. The decoder uses nominal event membership then Hamming distance, NEVER unknown-W maximum likelihood.

The respective accepted statistical payloads have B_payload=2ceil(log2(M+1))+2: F pays its suffix row count, flip count, terminal bit and repaired gate; O2 pays its pair-row count, directed-transition count, orientation bit and original O2 gate. Successful decoding reproduces the corresponding accepted estimator with risk ≤G_j g_M(k). Their orientation bits, including on rejection, are paid; no endpoint or query is free. Failure costs at most one. Thus the robust factor is ≤G_j+1 for M≥64.

Since 0<γ≤d/2≤1/2, ceil(4/γ²)≤(4+1/4)/γ². Equation (12) is therefore O(ln M/γ²) with constants and a horizon threshold independent of γ. This proves the upper half of (B).

## 8. Whole-message lower: finite grid and channel capacity

Use the SAME admissible W* from (2), now for the ENTIRE interval 0≤α<d/2, where 0<s≤1/2. No ratio Q1*/Q0* is needed; rows may have zeros at α=0. Relative to μ, using ln z≤z−1 and the usual zero-mass conventions,

    D(Qb*||μ)≤χ²(Qb*||μ)
       =s² Σ_y ν(y)²/μ(y)≤4s²=4γ²/d².            (13)

For any input distribution π, with output law Qbar=Σπ_b Qb*, expand the logarithms to obtain

    Σ_b π_b D(Qb*||μ)=I(H;Y)+D(Qbar||μ)≥I(H;Y).

Thus single-use capacity in NATS is at most C*=4γ²/d². This is an upper bound, not an assertion of the exact capacity or a coding theorem.

For a fixed-length encoder without feedback, conditioned on independent public seed U, the data-processing chain is parameter J → sample/private encoder coins → H^R → Y^R. Memorylessness gives

    I(H^R;Y^R | U=u)
       =H(Y^R|u)−H(Y^R|H^R,u)
       ≤Σ_i [H(Y_i|u)−H(Y_i|H_i,u)]≤R C*.

The entropy equalities concern finite-alphabet inputs/outputs; arbitrary source randomness has been absorbed into their distribution. U is independent of J, hence I(J;Y^R,U)≤R C*. Independent receiver coins V can be added (or generated conditionally on U independently): I(J;Y^R,U,V)=I(J;Y^R,U). These conclusions require the no-free-baseline model; they would be false if free counts or a terminal query were silently included.

Both F and O2 contain the clean stationary IID Bernoulli(p) family, p∈[1/4,3/4], with k=0, identity attack and next-symbol target p independent of endpoint. Its pair-chain P²(u,v)=Π(v) holds on every row, so the critical O2 certificate is satisfied. Fix a claimed finite factor B>0. For large M define

    δ=8B/√M, n=floor(√M/(16B))+1,
    p_j=1/4+jδ, j=0,...,n−1.

Then all points lie in [1/4,3/4], their spacing is δ, and n≥√M/(16B). Choose J uniformly from these finitely many points before sampling the clean IID word. If the protocol has risk ≤B/√M for every p_j, its prior-averaged absolute error E|p_hat−p_J| is ≤B/√M. Decode J_hat by the nearest grid point, with deterministic tie-breaking. An error requires |p_hat−p_J|≥δ/2=4B/√M, so Markov gives P_e≤1/4.

For completeness the finite Fano bound follows by E=1{J_hat≠J}. Given the full transcript Z=(Y^R,U,V), J_hat is determined. The entropy chain rule gives

    H(J|Z)≤H(E|Z)+H(J|E,Z)
       ≤ln2+P_e ln(n−1)≤ln2+(1/4)ln n.

The term for E=0 is zero; for E=1 there are at most n−1 candidates. Therefore

    I(J;Z)≥(3/4)ln n−ln2
       ≥(3/8)ln M−(3/4)ln(16B)−ln2.             (14)

This proof uses finite Shannon entropy, not differential entropy or an unproved continuous-parameter Fano substitution. For example if

    ln M≥max{8ln(16max{B,1}), 8ln2},

then the right side of (14) is at least (1/8)ln M. This threshold depends only on B, not the channel gap. Combining with I(J;Z)≤4Rγ²/d² yields

    R≥d² ln M/(32γ²).                            (15)

This proves the lower half of (B) for every actual target-B rule. For a claim expressed only as an infimum ≤B, apply the argument to approximating rules with target B+1; the displayed coefficient remains the same after enlarging the B-dependent threshold. Arbitrary private encoder randomization and public seeds are covered by the information bound, and the full raw sample does not escape the physical channel bottleneck.

## 9. Boundary, computation, and limitations

If α≥d/2, Wmid=(μ,μ) is admissible because TV(μ,Pb)=d/2. Its output can be generated independently by a baseline-only randomized receiver; thus the supplemental robust minimax factor is exactly its baseline counterpart (lower by simulation at Wmid, upper by ignoring the channel, with infima approximated if necessary). In the whole-message model its output and all independent coins are independent of clean IID p. Under uniform p∈[1/4,3/4], every fixed action has average absolute error at least |[1/4,3/4]|/4=1/8; averaging any independent random action cannot improve this. Worst clean risk is therefore ≥1/8, and factor ≥√M/8. The equality α=d/2 is included. If d=0, W0 itself is identical-row. Conversely TV(Q0,Q1)≥d−2α establishes strict separation throughout the constructive region, without substituting separation alone for the communication lower proof.

The nominal channel is fixed for the theorem. For rational nominal rows and supplied rational α, γ, event membership and rational thresholds can be computed exactly. Read/processing cost of an arbitrarily long α representation is additional; it is not uniformly poly(log M). Logarithmic ceiling bounds can be conservatively implemented using integer bit lengths and rational arithmetic, rather than an exact transcendental oracle. Arbitrary real parameters give statistical existence unless a computational representation/access model is separately provided. The unknown true rows may be arbitrary real: the algorithms never query them numerically.

The source scan costs O(M log M) conservative bit time and O(log M) auxiliary counters. Supplemental channel decoding requires every one of R output reads, O(log(R+1)) counter bits and O(R log(R+1)) conservative counter time. In the whole-message construction the accepted finite-field/inner-table/outer-matrix costs are polynomial in B_payload=O(log M), with nominal primitive repetition m0=Θ(γ^-2) explicitly charged, as are its counter bit costs. Whole-message design and arithmetic space remain as in UWC001, with an additional dependence on log(m0+1) and on the supplied radius representation; no uncharged codebook or unknown-W decoder is introduced. Resident input, if charged, adds M+2 bits rather than being called auxiliary polylog space.

At least R output/input operations are required by these explicit protocols, and R may be far larger than any polynomial in log M when γ→0. Therefore there is NO uniform polylog(M) communication or coding-time claim over the full open interval. The original fixed-gap computational exponents can be retained with the gap-dependent factors made explicit; those factors are not constants uniform in α.

Imported sources read: FOT001 `../resumption_20261103/recovered_science/first_order_positional_probe/triple_access/FOT001_candidate.md` and `../resumption_20261103/recovered_science/intake/FOT001_root_acceptance.json`; BSC001 `../resumption_20261103/bsc_sharp/CHANNEL_LIKELIHOOD_LOWER.md` and receipt; UMC001 `../channel_uncertainty_20261103/CANDIDATE.md` and receipt; UWC001 `../unknown_channel_whole_code_20261103/CANDIDATE.md` and receipt; CAF001 `../channel_accuracy_frontier_20261103/CANDIDATE.md` and receipt. The O2T001 receipt was inspected for the separately constrained source-class interface; its statistical proofs are imported through the accepted CAF/UWC interfaces, not claimed freshly rederived. Exact source bindings and independent adversarial review are subsequent gates, not implied by this author note.

Standard ingredients used here are the constrained-risk Cauchy–Schwarz argument, joint convexity of χ², product affinity, KL-to-reference capacity bound, finite Fano, nominal-event concentration, and accepted robust concatenated coding. No new inequality or new coding architecture is claimed. The contribution being checked is their application to the accepted common source-mixture transport and the resulting joint uniform α,M frontier. Scope excludes calibration-sample complexity, changing nominal channel/alphabet, correlated/adversarial/adaptive channel noise, feedback, variable length, uncharged path information, unrestricted O2, next-pair/general-order results, neural implementation, learning guarantees, sharp leading constants, and novelty certification. Local mathematical derivation only; no external publication, repository writes, permissions, licenses, deployment changes, formal verification or external peer review.
