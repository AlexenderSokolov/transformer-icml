# FOL001 — Natural binary first-order positional lower candidate

2026-11-02. Local author candidate, not independently reviewed or accepted. This is the PLAN's new experiment, not the original order-two/triple-count experiment. No certificate is assumed. Accepted sources were read, not modified.

## 1. Finite statement

A word is X_0,...,X_N, with N departures. Only X_N is protected. Observation T_r consists of four pair counts and the first/last r raw symbols. Risk is unconditional unsquared TV for prediction at the actual X_N. Fix any k-blind randomized predictor A. Define

c=2^-16, A0=2^12, t=ck/N, u0=floor(ck/4), T=floor(N/8), L=log(1/(4 A0 t)).

Assume integer N,k,r satisfy

N≥64, 1≤r≤k/128, k≤N/8, ck≥1024, A0 t<1/4,
N/k²≤A0 c²/2^20.

Let Q_a be the stationary first-order binary chain P_a(0,1)=a and P_a(1,0)=t, for A0 t≤a≤1/4. Let S be the supremum clean risk of the fixed predictor on this interval. There exists a stationary first-order null and ONE source-independent strict-k kernel protecting X_N on all inputs/outputs such that

R_null ≥ [u0/(8Nt)] [(t/16−S)L]_+ .                 (1)

This is a finite candidate theorem. The proof below fully specifies the kernel and constants.

## 2. Exact occupation mixture

Write F={X_0=1,X_N=0}, J=sum_{i<N}1{X_i=0}, U=N01, D=N01+N10. Stationarity is π0=t/(a+t), π1=a/(a+t). For j departures from zero, erase EVERY zero-departing transition, including loops and exits. There remain H=N−j transitions. The last one is the terminal entry 1→0, of weight t. Earlier retained transitions are either 1→1 (weight 1−t), or marked 1→0 followed by the erased exit 0→1 (retained weight t, erased factor a restored later). Therefore

h[H,u]=t binom(H−1,u)t^u(1−t)^(H−1−u),

with value zero outside H≥1 and 0≤u≤H−1. The u marks give u completed zero visits and one terminal visit. Distributing j−u loops among these u+1 slots gives binom(j,u), including the terminal slot although X_N is not a departure. Thus exactly

Q_a(F,J=j,U=u)=π1(a) binom(j,u) a^u(1−a)^(j−u) h[N−j,u].  (2)

For u≥1, integration against da/a gives h/u times E[π1(B)], B~Beta(u,j−u+1), since binom(j,u)B(u,j−u+1)=1/u. In particular it is ≤h/u. Also sum_u h[H,u]=t exactly. Hence for any interval I⊂(0,1), u0≥1, and additional event G (possibly a-dependent),

∫_I Q_a(F,J=j,U≥u0,G) da/a ≤t/u0.                 (3)

No 1/u expression is applied at u=0, no stationary initial factor is discarded from an equality, and no random outside horizon is replaced by its mean.

## 3. Pair-count and window preserving relocation

Assume F and 2r≤N+1. Put l=r−1, h=N−r+1. Freeze edges i<l and i≥h, exactly 2r−2 edges. In the interior path X_l,...,X_h, assume a visit to 1 occurs strictly before a visit to 0. Delete all interior self-loops. Retain every crossing in its original order. Insert all deleted 11 loops at the first retained 1 and all deleted 00 loops at the first subsequent retained 0. Call this deterministic map C_r. Loop deletion preserves distinct-state visits and their order. Reinsertion restores the edge count and the attachment index h, so every frozen boundary symbol is unchanged; every pair count is unchanged. These are the alternative's windows, NOT the null input's windows.

Let A1,A0 be the respective moved loop counts, and f1,f0 the frozen 11,00 counts. Since start1/end0, N10=U+1 and D=2U+1. The transformed word contains a distinguished block of A1 ones before a block of A0 zeros. Its other ones and zeros and target suffix correction are exactly

o=1+U+f1, z=U+1+f0, q=J−A0=U+f0≥0.

For any word of length m with these ordered blocks, comparison to 1^(m−j)0^j, where j=A0+q, gives

d_H≤max(z+q,2o+z−q).

Proof: if any distinguished one lies after the target cut, all distinguished zeros do also, and using the number of zeros before the cut bounds distance by z+q. Otherwise every one after the cut is one of the o other ones, giving 2o+z−q. This also handles an empty distinguished block by the same alternatives.

Here z+q=D+2f0 and 2o+z−q=D+2+2f1. Since f0+f1≤2r−2,

d_H(C_r(X), x^(j))≤D+4r−2,
x^(j)=1^(N+1−j)0^j, j=J.                         (4)

For j≥1 both terminal symbols are zero, so every mismatch is in the first N editable coordinates. EXACT SHIFT: J(x^(j))=j−1, whereas J(X)=j. There is only one protected symbol here.

## 4. Uniform good-event mass with finite constants

Throughout a≥A0 t≥t and a,t≤1/4, so π1≥1−1/A0≥3/4. Every row has common atom at 1 of mass a: P_a(0,1)=a and P_a(1,1)=1−t≥a. Common-atom coupling gives contraction ≤(1−a)^s at lag s, and a coupling of a chain Z started at 0 to stationary W with meeting time σ satisfying Eσ≤1/a. For any departure-state-set count or directed-edge count V of stationary probability p,

Var(V)≤Np(1+2/a)≤3Np/a.                           (5)

Indeed lag-s edge covariance is at most p(1−a)^(s−1); state covariance is no larger. The same proof applies to D, the indicator of the SET of crossing edges. Every count changes by at most σ between Z and W.

The chain is reversible (π0 a=π1 t). Hence conditioned on F, the reversed path Z_i=X_(N−i) has law of the chain started at 0 conditioned on E={Z_N=1}. By contraction,

P_0(E)≥π1−(1−a)^N≥3/4−1/(aN)≥1/2,

using aN≥A0 ck. Set x=ck. In the coupling impose

σ≤x/16; |U(W)−Nt a/(a+t)|≤x/8;
D(W)≤k/32; J(W)≤N/16.                            (6)

The stationary mean of U lies in [x/2,x]. The respective failure probabilities are at most

16N/(A0 c²k²), 192N/(A0 c²k²),
24576N/(A0 k²), 16/A0.                           (7)

The first is Markov. The second uses Var U≤3Nt/a and Chebyshev. For the third E D≤2ck≤k/64 and Var D≤6Nt/a≤6N/A0; Chebyshev at k/64 gives the bound. The fourth uses π0≤1/A0 and Markov. Conditioning the joint coupling on E costs at most two. Under the displayed finite domain, twice their sum is ≤2[(208+24576c²)/2^20+16/A0]<1/16.

Exact reversal shifts on F are J(Z)=J(X)+1, U(Z)=U(X)+1, D(Z)=D(X). Thus (6), count discrepancies ≤σ, and x≥1024 imply

U(X)≥x/2−x/8−x/16−1≥x/4≥u0;
D(X)≤k/32+ck/16≤k/16;
2≤u0≤J(X)≤N/16+ck/16≤N/8.

In particular J(X)≤T since J is integer.

Let B be the ordered interior visit event used in §3. Reversal maps it to a visit to 0 strictly before a visit to 1 in Z_l,...,Z_h; note N−h=l and N−l=h. From any state, expected additional time to hit 0 and then 1 is at most 1/t+1/a≤2/t. This follows from geometric hitting times and the strong Markov property. The available span h−l=N−2r+2≥N/2. Markov gives unconditional failure ≤4/(tN), and conditioning on E gives failure ≤8/(ck)≤1/128. No independence from the endpoint is asserted.

Define G=B∩{U≥u0,D≤k/16,2≤J≤T}. Then Q_a(G|F)≥1−1/16−1/128>1/2. Consequently

Q_a(F∩G)≥π0/4.

Set β=1/N. Since aN≥A0 ck≥2, a−β≥a/2, and aπ0=at/(a+t)≥t/2. Therefore

(a−β) Q_a(F∩G)≥t/16.                            (8)

## 5. Null, one-draw common kernel, and risk inequality

Take stationary first-order P_*(0,1)=β=1/N and P_*(1,0)=q=1/(2N). Its stationary initial masses are π_*(1)=2/3 and π_*(0)=1/3. For 2≤j≤T, the full word masses of x^(j)=1^(N+1−j)0^j are

v_j=(2/3)(1−q)^(N−j) q(1−β)^(j−1)≥1/(8N).

Indeed the prefix factor is ≥1/2 and the suffix factor ≥7/8, giving the stronger 7/(48N). These words have actual terminal target β.

Predeclare finite measures

ν_j(dy)=∫_[A0t,1/4] Q_a(dy;F,J=j,U≥u0) da/a,
μ_j=ν_j(all words)≤t/u0.

On input x^(j) with μ_j>0, draw Y ONCE from ν_j/μ_j. If B holds, compute C_r(Y). Accept only if its ACTUAL Hamming distance from the input is ≤k and its actual last symbol is the input's last symbol. Otherwise output the unchanged input. On all other inputs and zero-mass labels output the input. This is one fully specified source-independent kernel on all words, depending only on N,k,r and the predeclared auxiliary family, not the true source or predictor randomness. It is strict pointwise, with identity rejection, and never resamples until acceptance.

On G, (4) bounds distance by k/16+4r−2<k, so acceptance holds. Also T_r(C_r(Y))=T_r(Y). Boundary edits relative to the null are allowed and included in the distance check.

For y ending0 let ℓ_a(y) be expected predictor absolute error from a, and ℓ_*(y) its expected error from β on T_r(y), integrating independent predictor randomness. Then ℓ_*≥a−β−ℓ_a. Because v_j/μ_j≥ρ=u0/(8Nt), first discard other null inputs and rejected proposals (nonnegative losses); next replace the coefficient by ρ on NONNEGATIVE accepted losses; next restrict to G; only then apply the signed triangle bound. This gives

R_null≥ρ∫ E_Qa[1_(F∩G) ℓ_*] da/a
      ≥ρ∫[(a−β)Q_a(F∩G)−E_Qa[1_(F∩G) ℓ_a]] da/a
      ≥ρ(t/16−S)L.

Nonnegativity of risk completes (1).

## 6. Finite logarithmic competitive consequence

For Γ(A;N,r)=sup_{k, stationary P, strict common K} R_A/max(N^-1/2,k/N), the candidate implies Γ(A;N,r)≥2^-30[1+log((N+1)/r)] for N≥64 and 1≤r≤N+1. This is a lower bound only, not an upper/equality claim.

Details: the clean IID two-point floor gives Γ≥1/96 even with full word observed (parameters 1/2±1/(16sqrt(N+1)); product KL≤1/8, TV≤1/4, and nearest-target testing). Thus if ell=1+log((N+1)/r)<64, the assertion follows. Otherwise assume Γ<2^-30 ell. Then log N≥ell−1−log(1+1/N)>62 and N>2^80. Choose k=ceil(max(128r,N^(3/4))). We have r/N≤2e^-63, k/N<2^-19, ck≥2^44, N/k²≤N^-1/2<2^-40=A0 c²/2^20. All finite-domain conditions hold. Also ρ≥1/64. Since ell≤1+log(2N)≤5N^(1/4), S≤Γ/sqrt N<5·2^-30 N^-1/4≤t/32 (t≥2^-16 N^-1/4).

Moreover L=log(4N/k)≥min(log(N/(64r)),log(2N^(1/4)))≥ell/8 for ell≥64: the first is ell−1−log(1+1/N)−log64≥ell−8; the second is ≥(ell−1−log(1+1/N))/4≥(ell−2)/4. Thus (1) implies Γ≥ρ(t/32)(ell/8)/(k/N)≥2^-30 ell, contradiction. A randomized predictor is already covered by all loss steps. The lower passes to infimum without attainment. Arbitrary-start class contains the stationary witnesses.

## 7. Scope and verification status

This proof's two-state stationary alternatives, pair-count histogram, N+1 raw symbols, and ONE protected terminal bit are deliberate. It provides NO automatic first-order lower when eight triple counts are observed, nor a replacement for the accepted order-two manuscript. No certificate is needed or asserted. No claim at every individual budget is made. `check_fol001.py` performs finite exact enumeration of the combinatorial identities and relocation conditions; its JSON is supporting evidence, not independent review or a formal proof.

Read-only mechanism sources: `binary_mixture_window/OMD001_occupation_mixture_domination.md` and `positional_manuscript_finite_20261102/sections/proofs_negative.tex`, plus `proofs_finite_horizon.tex`. This candidate derives the first-order skeleton, covariance/coupling, endpoint shifts, relocation and finite constants anew.
