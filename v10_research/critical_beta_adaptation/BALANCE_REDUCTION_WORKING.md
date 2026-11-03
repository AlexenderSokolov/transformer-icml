# Working successor — an occupation-balance gate reduces adaptation to one clean bias

2026-11-02. **Unreviewed working reduction, NOT a critical-curve solution.** Accepted CB001–CB003 are unchanged. This is qualitatively different from a fixed near-prefix threshold.

## Candidate and exact remaining question

Let n=floor(M/2). For the preserved terminal row u, let J1',J2',C' be the corrupted first-half occupation, second-half occupation and total designated-exit count. Put J'=J1'+J2'. Output C'/J' if J'>0 and J1'>=J'/32; otherwise output designated probability0. The estimator uses only M and the ordered corrupted word, not k or beta.

For the original clean counts define J=J1+J2 and

    I(M,P,mu)=E[q_(Y_M) 1{J>0, J1<J/16}].

The working reduction below gives, uniformly over all sources/starts and strict-k protected corruption,

    R_gate <= I(M,P,mu)+2^16/sqrt(M)+2^19 k/M.       (BR)

Thus the SOLE remaining probabilistic question for this candidate is whether

    I(M,P,mu)<=C/sqrt(M) at beta=1/M                (OPEN-IB)

uniformly over the exact binary all-state source class, preferably all starts. A stationary-only proof would establish only stationary adaptation; it must not silently be promoted to all starts. A counterexample to OPEN-IB would reject this candidate rather than prove unrestricted impossibility.

## 1. Generic balanced reciprocal-occupation lemma

Use any four-state homogeneous Markov chain and arbitrary initial law. Write m=M-n. At terminal state u, suppose J1_u>=J_u/64, equivalently J2_u<=63J1_u. Conditional on the first-half history, fix its endpoint v and J1_u=j. The accepted universal terminal-occupation bound on the m-step suffix gives

 P_v(Y_m=u,J2_u<=63j)<=16(63j+1)/(m+1).

Since(J_u+1)^-1<=(j+1)^-1, and(63j+1)/(j+1)<=63, summing the conditional first-half distribution and then the four possible terminal states gives

 E[(J_(Y_M)+1)^-1 1{J1_(Y_M)>=J_(Y_M)/64}]
       <=4032/(m+1)<=8064/M.                       (BR1)

No stationarity, minorization or conditional-IID assertion is used. The j=0 case is included. The conditioning fixes a public-time prefix, not the future terminal state. For M>=128 the suffix horizon is at least64, within the accepted occupation interface's inherited range; smaller M can be absorbed by the trivial final risk bound.

## 2. Deterministic corruption calculation

Let d=6k. The accepted Hamming-to-triple bound implies separately

    |J'-J|<=d, |J1'-J1|<=d, |C'-C|<=d.

Set H={J1>=J/64}, B={J>0,J1<J/16}, and G'={J'>0,J1'>=J'/32}. For J>0, put p=C/J and E=|p-q|; use0 for E at J=0.

On G' intersect H and J>0,

    |C'/J'-q|<=E+8d/(J+1).                         (2.1)

For J>=2d with d>0, normalization gives |C'/J'-C/J|<=4d/J<=8d/(J+1). If J<2d, the difference is at most1<=8d/(J+1). For d=0 the difference is zero. J=0 contributes at most its event probability, handled separately.

On G' intersect H^c, J1<J/64 while J1+d>=J1'>=J'/32>=(J-d)/32. Hence

    J<66d=396k.                                    (2.2)

On G'^c outside B and with J>0, J1>=J/16. If J'=0 then J<=d. Otherwise J1'<J'/32, which implies J/16-d<(J+d)/32 and hence

    J<33d=198k.                                    (2.3)

When G' fails and B holds, the loss is exactly q. Therefore, allowing harmless overlapping tail events,

 R_gate <= E E +8d E[(J+1)^-1 1_H]+I
                 +P(J<396k+1)+P(J<198k+1).         (2.4)

The J=0 contribution is included in those two tail probabilities. This inequality remains true at k=0: false-status cases with J>0 are then impossible, and the tails only pay J=0.

## 3. Assembly

Accepted SC003 supplies

    E E <=8193 sqrt(32)/sqrt(M+1)

and the four-state terminal-occupation bound gives

 P(J<396k+1)+P(J<198k+1)
       <=16(594k+2)/(M+1).

Combining with(BR1) and8d=48k gives corruption coefficient

    48*8064+16*594=396576 <2^19.

The statistical coefficient is8193sqrt32 plus32/sqrtM, at most2^16 for M>=64. This proves(BR) for M>=128. For64<=M<128,2^16/sqrtM>1 makes the asserted risk bound trivial. No k appears in the estimator itself.

## 4. Why this addresses the observed failures

CB003's attacked histories have prefix00 occupation h=ceil(sqrtM), but total00 occupation is t-1-2floor(k/4)+h. For t sufficiently larger than k and k>>sqrtM, the balance gate rejects; a small fixed prefix perturbation does not suffice to activate it across the harmonic suffix range. This is only motivation, not the missing proof of OPEN-IB.

Potential probabilistic route: binary diagonal macrocycles plus the certificate may force a clean high-exit terminal row to have appreciable first-half occupation. In stationary initialization, reverse the path from the terminal state (binary order2 reversal preserves the kernel up to pair-coordinate swap), then use accepted BU001 target-specific hitting scales satisfying sqrt(beta) pi_u q_u H_u<=5. A suitable fixed-state occupation-imbalance tail at time M/H_u would give the desired stationary order. An arbitrary-start extension needs its own endpoint-weight accounting.

The probe agent is currently checking this route. No weighted imbalance theorem, full critical-curve adaptation claim, or formal/external-review claim is made here.
