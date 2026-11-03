# FOT001 fresh independent adversarial audit

2026-11-02. Reviewer: independent LLM reviewer.

**Verdict:** no mathematical gap found in the bounded candidate. This is a favorable independent LLM proof review, not root acceptance, external peer review, formal verification, or a manuscript/publication action. The candidate remains a candidate until the parent/root applies its own gate. No source files were edited.

Reviewed candidate SHA256: `700db043416260a3d7e4796d6513ee60b90c2f2704a4d183be526d2aef9fef1d`.

## Inputs actually read

- Entire `FOT001_candidate.md` and companion author checker (not used as independent evidence).
- Entire `../TRIPLE_ACCESS_NEXT_QUESTION.md`.
- Entire accepted `binary_mixture_window/window_preserving/WPC001_window_preserving_canonicalization.md`; accepted SHA `a8328eb7907e20c006314e198948168b9d1da4045932d10c611dcfab42b566a6` checked against the accepted bindings and handoff. Historical candidate wording in that file is superseded by its acceptance receipt/handoff.
- WPC001/MW002 accepted bindings and accepted combined handoff, solely for dependency identity and scope. No probabilistic first-order claim was inferred from MW002/FOL001.

## Independent analytic derivation and stress points

### 1. Exact fixed-v mixture

For a start-1/end-0 path, there are u+1 transitions 10 and u transitions 01. There are u+1 zero visits, including the terminal visit; placing v zero self-loops among them contributes C(v+u,u). The u+1 one visits admit N-v-2u-1 one self-loops, contributing C(N-v-u-1,u). Thus the stated mass, including stationary factor pi1=a/(a+t), is correct with H=N-v-u, not N-v. On dropping pi1 only in the upper bound, the beta integral is C(v+u,u) B(u,v+1)=1/u. The residual sum at fixed v is t times the coefficient sum for tilings with monomers of weight 1-t and dimers of weight t. This directly yields R0=1,R1=1-t and the convex recurrence, hence Rn<=1. Restrictions can only decrease the resulting nonnegative measure. On F, ordinary 00 count includes the omitted final 00 edge, so J00=v-1 and the required substitution is v=j+1. No restricted equality is claimed.

### 2. Endpoint-pair conditioning and coupling

A stationary binary two-state chain is reversible. Reversing F gives forced initial 00 and terminal 11. After time 1 the law is the usual chain from zero; the first forced edge must be charged separately. Common atom 1 has mass a since a<=1-t. At time N-1, TV from stationarity is <=(1-a)^(N-2)<=1/[a(N-2)]. Therefore P00(E) has the stated lower bound and Q(F)=pi0(1-a)P00(E)>=3pi0/8.

Start a stationary W at time 1 and supply W0 from its reversed stationary transition; the meeting-time coupling gives E sigma<=1/a and any relevant count discrepancy <=1+sigma. This +1 covers the forced first edge. Conditioning the whole joint coupling on E costs at most 2, regardless of the dependence between coupling success and E. Reversal has U(Z)=U(X)+1, unchanged D and unchanged V00, so the additional minus-one in the U lower bound is necessary and present.

For an edge indicator of mean p, lag-s covariance in absolute value is <=p(1-a)^(s-1): condition on the first edge and contract before the second edge. Thus Var V<=Np(1+2/a)<=3Np/a. The state count obeys the same weaker bound. This justifies all three Chebyshev uses without assuming independent transitions.

The failure bounds rederive as follows: Markov on sigma gives 32N/(A c²k²); Var U<=3Nt/a gives 192N/(A c²k²); ED<=2x<=k/64 and Var D<=6N/A give 24576N/(Ak²); E Jzero<=N/A gives 16/A. Separately m=Npi0(1-a)>=3x/2 and am>=3x/8 give P(V00<m/2)<=12/(am)<=32/x. The separate V00 condition is indispensable: large U alone does not force a large ordinary 00 count. From it, v>=m/2-x/16>=11x/16>=3. The upper count bound and U,D bounds then imply exactly the claimed G count constraints, including integer floor T. Under x>=4096, 1+sigma<=x/16 is valid.

### 3. Interior ordering

Pair reversal maps interior indices [l,h] onto themselves because M-h=l; homogeneous 00/11 labels remain unchanged. From last symbol 1, the mean additional time to complete 00 solves the renewal equations and equals (1/t+1)/(1-a)<=2/t. From last symbol 0 it is no larger. Bit interchange gives the corresponding <=2/a time to complete 11. Sequential strong Markov gives <=4/t, and span h-l>=N/2 gives unconditional failure <=8/x; endpoint conditioning doubles this to <=16/x. When l=0 the forced initial 00 is already available and the future starting at time 1 is ordinary. This avoids incorrectly treating the forced initial step as an unconditioned transition.

The full conditional failure bound is exactly at most 7633633283/274877906944 = 0.027770996104663936 < 1/16 at the worst displayed parameters. Thus the weaker good mass >=1/2 is safe. a>=2 beta and a pi0>=t/2 yield (a-beta)Q(F cap G)>=3t/64, so the used t/64 has slack.

### 4. Exact triple relocation and editable coordinates

Re-derived WPC's ordered-block argument: deleting only 111/000 interior loops preserves the skeleton; reinsertion at ordered 11/00 vertices preserves all triple multiplicities. Restoring the same interior length fixes suffix positions. Frozen edges i<r-2 and i>=N-r+1 preserve actual clean windows, not necessarily null-input windows. WPC's counts o=cross+1-p+f1, z=cross+1-w+f0, q=u+f0 give max(z+q,2o+z-q)<=3cross+4r-5. This uses M=N-1 exactly. F makes cross=D since its omitted final ordinary edge is 00. On G, 3k/16+4r-5<k. Both null and output end 00 for j>=2, so all differences are in the first N-1 raw coordinates. The null suffix has J00=j-2, not j; no histogram equivalence with the null input is required or used.

### 5. Null masses, kernel, and signed-loss ordering

Null mass includes N-j initial 11 edges, one 10, and j-1 terminal 00 edges. Bernoulli's inequality gives prefix >=1/2 and suffix >=3/4, hence vj>=1/(8M)>=1/(8N). All label input words are distinct. The measure nuj is finite and fixed before sampling; zero masses and all unlisted inputs use identity. One proposal with an actual-distance/final-pair acceptance test is a legal source-independent pointwise strict-k kernel. Dependence on N,k,r is allowed and no predictor randomness enters it.

On accepted G proposals the observation equals that of the sampled clean path by WPC. The transported actual null loss is nonnegative, so discarding other inputs/rejections and replacing vj/muj by rho are valid before restriction to G. Only after that restriction is the potentially signed triangle lower bound used. Clean loss on F cap G is bounded by unconditional clean S, not a conditional risk. The null and alternative transition targets at last symbol zero have TV distance a-beta. In pair-state representation the next-pair targets are supported on 00,01 with those same probabilities; therefore prediction at the actual last symbol agrees with the original pair target in this subclass. Integrating predictor randomness does not change the triangle inequality. This establishes (1) with its positive part.

### 6. All-state certificate

The two-step pair transition is T(d,s)T(s,z) and stationary destination probability pi(s)T(s,z), giving ratio T(d,s)/pi(s). The four ratios in the candidate are correct and each occurs for all four combinations of b,z, so all 16 entries are covered, not only homogeneous endpoints. For alternatives each ratio >=a+t>=t>=1/(N-1); for the null they are 3(1-beta),3beta/2,3q,3(1-q)/2, all >=beta at N>=64. All entries of the underlying binary tables are positive. Hence the pair chain is irreducible and has homogeneous self-loops (aperiodic). Supplied beta is 1/M, never silently changed to 1/N.

### 7. Finite logarithmic conclusion and paid horizon conversion

The iid witnesses give a sufficient universal clean floor: n=N+1 observations, parameter gap 1/(8 sqrt(n)), product KL<1/8 and TV<=1/4. Nearest-target testing gives mean loss >=3/(128 sqrt(n)), which is stronger than 1/(96 sqrt(N)) for N>=64. Their pair-chain ratios are exactly 1, so the clean floor applies also under the restricted certificate class.

For ell<64 the floor is far larger than 2^-32 ell. For ell>=64, r>=2 implies log N>62, hence N>2^80 and N^.25>2^20. With k=ceil(max(128r,N^.75)), the ceiling costs <=2, r/N<=2 exp(-63), k/N<2^-19, x>=2^44, N/k²<2^-40=A c²/2^20. All theorem assumptions hold and integer k lies in [0,N-1]. Clean identity attack k=0 gives S<=Gamma/sqrt(N); ell<=5N^.25 then gives S<t/128. u0>=x/8 gives rho>=1/64. The two branches of L are at least ell-8 and (ell-2)/4, hence L>=ell/8. The final product rho*(t/128)/(k/N)*(ell/8) is exactly bounded below by 2^-32 ell. Contradiction proves the finite claim without assuming an attained supremum/infimum.

For M=N-1, each component of gM is between the corresponding gN component and N/(N-1) times it. Thus gN<=gM<=N/(N-1)gN, and the lower bound pays (N-1)/N. Original M>=64 is N>=65. The logarithm is 1+log((M+2)/r), with no horizon identification. Scope is relative to the explicit rate gN, not an oracle-risk equivalence.

## Independent executable corroboration

`independent_audit_checks.py` was written afresh and imports no author code. It enumerates all start-1/end-0 words for N=2..12 using exact rational path weights, reconstructs relocation from retained triple edge labels, tests endpoint shifts/windows/triple multisets/distances/protected coordinates, computes exact count variances for three parameter tables and N=2..8, checks all certificate entries, and checks null masses. It passes 814 exact mixture cells, 1,023 endpoint identities, 2,332 relocations, 105 variance bounds, 48 alternative and 64 null certificate entries, and 156 null masses. These small finite checks corroborate, not replace, the preceding analytic proof.

No blockers or required corrections identified. No external writes, accepted-source changes, or manuscript changes were performed.
