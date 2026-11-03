# FOT001 — First-order sources with the original triple observation

2026-11-02. Complete local author candidate; NOT independently reviewed or accepted. No manuscript change. This is a new derivation, not an implication of FOL001.

## Finite experiment and statement

Raw word X_0,...,X_N; N ordinary edges and M=N−1 triple departures. Observe all eight triple counts and actual first/last r raw symbols, r≥2. The final TWO raw symbols are protected. Prediction is at the actual last symbol, with unconditional unsquared TV loss. One fixed randomized map at (N,r), ignorant of k, is used throughout.

Put c=2^-16, A=2^12, x=ck, t=x/N, u0=floor(x/4), T=floor(N/8), L=log(1/(4At))=log(4N/k). Require integers

N≥64, 2≤r≤k/128, k≤N/8, x≥4096,
At<1/4, N/k²≤A c²/2^20.

For stationary binary first-order alternatives Q_a with T_a(0,1)=a, T_a(1,0)=t, a∈[At,1/4], let S be the supremum clean risk of the fixed predictor. There is a stationary first-order null and ONE source-independent strict-k kernel, protecting the final pair on every input/outcome, such that

R_null ≥ [u0/(8Nt)] [(t/64−S)L]_+.                     (1)

Every displayed source, represented as a pair-state chain, satisfies the original all-state two-step certificate with supplied β=1/M. This is separately verified below; it is not used in the mixture derivation.

## Exact mixture with fixed ordinary 00 count

Write F1={X_0=1,X_N=0}, v=N00, u=N01, and H=N−v−u. Ordinary zero departures equal v+u. Erasing all zero-departing edges leaves H edges, the last a terminal 10 and u earlier marked 10 edges whose following 01 is erased. Distributing v loops among u+1 zero visits gives binom(v+u,u). Consequently

Q_a(F1,v,u)=π1(a) binom(v+u,u) a^u(1−a)^v h[H,u],
h[H,u]=t binom(H−1,u)t^u(1−t)^(H−1−u),

where h=0 outside H≥1, 0≤u≤H−1. This counts complete words, including terminal zero loops. π1=a/(a+t) is retained in the equality. For u≥1,

∫_0^1 π1(a) binom(v+u,u) a^u(1−a)^v da/a ≤1/u.

For fixed v≤N−1, n=N−v−1≥0,

sum_u h[N−v−u,u]
 =t sum_(0≤2u≤n) binom(n−u,u)t^u(1−t)^(n−2u)=t R_n≤t.

Here R_0=1, R_1=1−t, and R_n=(1−t)R_(n−1)+tR_(n−2). The inequality follows inductively as a convex combination. If v≥N all summands vanish. Hence for any extra restriction G and interval I⊂(0,1),

∫_I Q_a(F1,v fixed,u≥u0,G) da/a ≤t/u0.             (2)

Take F={X_0X_1=11,X_(N−1)X_N=00}. On F the triple-departure occupation j=J00 is exactly v−1, NOT v. Thus (2) dominates the label j after substituting v=j+1. No claim of an equality after restricting to F is needed.

## Conditional good mass, with explicit coupling bounds

Stationarity gives π0=t/(a+t), π1=a/(a+t), and reversibility. Conditional on F, the reversed word Z_i=X_(N−i) is the chain forced to start Z_0Z_1=00, conditioned on E={Z_(N−1)Z_N=11}. From time1 onwards it is an ordinary chain from0. Every transition row has common atom1 of mass a. Thus contraction is at most (1−a)^s. Since a(N−2)≥Ax/2,

P_00(E)≥[π1−1/(a(N−2))](1−t)≥(3/4)(3/4)≥1/2.

Also Q_a(F)=π0(1−a)P_00(E)≥3π0/8.

Couple Z from time1 to a stationary chain W, using the common atom. Let σ be the number of transitions until meeting, Eσ≤1/a. Supply W_0 by its stationary reverse transition. Any state-departure count or edge count on the N-edge words differs by at most 1+σ. For a stationary count V of state indicators, single directed edges, or a set of directed edges, with stationary probability p,

Var V≤Np(1+2/a)≤3Np/a.

Indeed a lag-s edge covariance has absolute value at most p(1−a)^(s−1); summing gives this bound (state counts obey the same weaker bound).

On the unconditioned joint coupling impose

σ≤x/32; |U(W)−Nπ0 a|≤x/8; D(W)≤k/32;
J_zero(W)≤N/16; V00(W)≥m/2,

where U=N01, D=N01+N10, J_zero counts zero-departing ordinary edges, V00=N00, and m=Nπ0(1−a). The respective failure probabilities are bounded by

32N/(A c²k²), 192N/(A c²k²),
24576N/(A k²), 16/A, 32/x.                       (3)

The first is Markov. The second uses Var U≤3Nt/a. For the third ED≤2x≤k/64 and Var D≤6Nt/a≤6N/A. The fourth is Markov. Finally m≥3x/2, am=N at(1−a)/(a+t)≥3x/8, so Chebyshev gives P(V00<m/2)≤12/(am)≤32/x. These deliberately weak bounds use a,t≤1/4 and a≥t.

Since 1+σ≤x/16, and reversal gives U(Z)=U(X)+1, D(Z)=D(X), V00(Z)=V00(X), the above events imply

U(X)≥x/2−x/8−x/16−1≥u0,
D(X)≤k/32+x/16≤k/16,
3≤v(X)≤N/16+x/16≤N/8,
2≤j=v−1≤T.

Conditioning the joint coupling on E costs at most2.

For the pair-path interior set l=r−2 and h=N−r+1 (M=N−1). Let B mean an interior visit11 strictly before a visit00. Reversal maps B to an interior visit00 strictly before11 in Z, with the same indices l,h. From any current pair, expected additional transitions to encounter00 then11 are at most 2/t+2/a≤4/t. To verify: from last symbol1 the expected time to complete00 is (1/t+1)/(1−a)≤2/t; from last symbol0 it is no larger. Interchange bits for11. Strong Markov gives the sum. The interior span h−l=N−2r+3≥N/2. Markov and conditioning on E therefore give P(B^c|F)≤16/x. This argument also covers l=0, where the initial pair is forced00; for l≥1 the future has the usual first-order law given the current pair.

Define G=B∩{U≥u0,D≤k/16,2≤j≤T}. The total conditional failure bound is at most

2[(224+24576c²)/2^20+16/A+32/x]+16/x <1/16

under x≥4096. In particular Q_a(G|F)≥1/2. With β=1/(N−1), a≥2β, and aπ0≥t/2,

(a−β)Q_a(F∩G)≥(a/2)(3π0/16)≥3t/64≥t/64.       (4)

## Exact triple relocation and distance

Apply WPC001 with M=N−1: freeze pair edges i<l and i≥h, remove only interior111 and000 loops, and insert all111 loops at the first retained11 preceding a later retained00, inserting all000 loops at that00. On B this deterministic C_r preserves all eight triple counts, both actual windows, and endpoint pairs. The accepted deterministic proof yields

d_H(C_r(X),1^(N+1−j)0^j)≤3J_cross+4r−5.

Here J_cross=J01+J10 over pair departure indices0,...,N−2. It equals D on F, because the omitted last ordinary edge is00. Thus on G the distance is at most 3k/16+4r−5<k. Since j≥2, both words end00, so all mismatches lie in the editable first N−1 coordinates. Null x^(j)=1^(N+1−j)0^j has J00=j−2; the alternative has J00=j. This exact shift is not used as an equality of their histograms.

## Null and common kernel

Let the stationary first-order null have T_*(0,1)=β=1/(N−1), T_*(1,0)=q=1/[2(N−1)]. Its π_*(1)=2/3. For 2≤j≤T,

v_j=Q_*(x^(j))=(2/3)(1−q)^(N−j) q(1−β)^(j−1)≥1/(8N).

Indeed N−j≤N−2<M, giving prefix factor≥1/2; j−1≤N/8 gives suffix factor≥3/4, hence v_j≥1/(8M)≥1/(8N).

Predeclare finite word measures

ν_j(dy)=∫_[At,1/4] Q_a(dy;F,J00=j,U≥u0) da/a,
μ_j=ν_j(all)≤t/u0.

On input x^(j) with μ_j>0, draw Y ONCE from ν_j/μ_j. If B holds, form C_r(Y); accept only when its actual Hamming distance from the input is ≤k and its actual final pair equals the input's final pair. Otherwise return the input unchanged. Return the input on all other inputs or zero-mass labels. This defines a single source-independent kernel on every word, with strict pointwise budget and final-pair protection. It does not resample after rejection and depends on neither true source nor predictor randomness. Its predeclared auxiliary family is allowed to depend on N,k,r.

Let ℓ_a(y) and ℓ_*(y) denote expected predictor losses against a and β on the common observation of y, integrating predictor randomness independently. They satisfy ℓ_*≥a−β−ℓ_a on F. Discard unused inputs and rejected proposals, replace v_j/μ_j by ρ=u0/(8Nt) only on nonnegative accepted losses, restrict to G, and only then use this signed triangle bound. Equations (2),(4) give

R_null≥ρ ∫ E_Qa[1_(F∩G) ℓ_*] da/a
≥ρ ∫[(a−β)Q_a(F∩G)−E_Qa[1_(F∩G)ℓ_a]] da/a
≥ρ(t/64−S)L.

Nonnegativity supplies the positive part in (1).

## Certificate: all rows, not just endpoint rows

For any positive first-order table T with stationary symbol law π, the induced pair law is Π(s,z)=π(s)T(s,z), and

P²((b,d),(s,z))/Π(s,z)=T(d,s)/π(s).

For alternatives the four ratios are (1−a)(a+t)/t, a+t, a+t, (1−t)(a+t)/a. Since a,t≤1/4, each is at least a+t≥t=x/N≥1/(N−1). For the null the four ratios are 3(1−β), 3β/2, 3q, 3(1−q)/2, each at least β. Each ratio covers both initial first bits and both terminal last bits, checking all sixteen entries. Positivity, irreducibility and aperiodicity hold. These checks concern the original certificate β=1/M, not β=1/N.

## Finite logarithmic factor and paid horizon conversion

For 2≤r≤N+1 let Γ(A;N,r) be the supremum over integer 0≤k≤N−1, stationary first-order sources, and source-independent strict-k kernels protecting the final pair, of R_A/g_N(k), where g_N(k)=max(N^-1/2,k/N). The same conclusion holds if this source class is restricted to the certificate β=1/(N−1). Then

Γ(A;N,r)≥2^-32 [1+log((N+1)/r)].                  (5)

Proof: clean iid Bernoulli alternatives with parameters 1/2±1/(16sqrt(N+1)) give Γ≥1/96 even with full words observed: product KL≤1/8, TV≤1/4, and nearest-target testing suffice. Their pair-chain certificate ratios all equal1. Put ell=1+log((N+1)/r). If ell<64 this floor proves (5). Otherwise suppose Γ<2^-32 ell and choose k=ceil(max(128r,N^(3/4))). As in the elementary inequalities below, N>2^80, k/N<2^-19, x≥2^44, N/k²≤N^-1/2<2^-40=A c²/2^20, and all finite assumptions hold, including k≤N−1. Since ell≤1+log(2N)≤5N^(1/4),

S≤Γ/sqrt N<5·2^-32 N^-1/4≤t/128.

Also ρ≥1/64. The ceiling costs at most a factor2, so

L=log(4N/k)≥min(log(N/(64r)),log(2N^(1/4)))≥ell/8.

For ell≥64 the first term is ≥ell−8 and the second ≥(ell−2)/4. Dividing (1) by k/N now gives Γ≥2^-32 ell, a contradiction. For the ancillary bounds, r/N≤2e^-63, log N≥ell−1−log(1+1/N)>62, and N^.25>2^20; these imply each displayed numeric bound directly. Infimizing over all randomized maps preserves (5), with no attainment requirement.

This is a lower relative to explicit g_N, NOT an oracle-risk equivalence. With M=N−1 and the same budget, g_N≤g_M≤[N/(N−1)]g_N. Thus R/g_M≥[(N−1)/N]R/g_N, explicitly paying the conversion. The logarithm becomes exactly 1+log((M+2)/r); no N=M substitution is made. Arbitrary-start classes contain the stationary witnesses.

## Status and checks

This candidate settles the requested bounded exploration at author-proof level only. The independent acceptance gate remains open. The companion exact finite checker enumerates mixture coefficients, renewal identities, pair shifts, relocation and certificates. Those finite checks are corroboration, not proof or independent review. Actual construction/revision history is retained; accepted earlier files were read only.
