# SF001 — All-Q stationary fixed-K original-master minimax risk

2026-11-02. **Author candidate; independent review required.** This synthesis proves the proposed profile rather than assuming it. It uses accepted IU001/IP002/SM002/NB002, does not edit them, and makes no external novelty or formal-verification claim.

## Result first

For every integer K>=3, M>=64, beta in [0,1], and Q=2^h with integer h>=4, set

    b=max(beta,1/M), s=M^(-1/2),
    f=[1+ln(1+Q/(Mb))]/Q, H=max(s,f).

Let R_stat be the minimax actual-terminal expected-TV risk at the **unchanged original complete finite SRC master cut**, initialized at the hidden stationary certificate. The decoder sees all 9K+1 downward-Q-grid masters, every original exact endpoint/query/mode/flag field and public metadata, but no history reread or clean statistical/evaluator ports. Arbitrary source-independent randomization, computation, and real simplex outputs are permitted. Sources satisfy the all-state two-step D2(beta) condition, including off-support starts; stationarity is an initialization restriction, not disclosure of the stationary law.

Then the following finite-domain, all-Q statement holds:

    2^(-336) H <= R_stat <= risk_stat(B_NB002) <= min(1,C_K H),       (SF1)

where one permissible explicit constant is

    C_K=2^16 K^(5/2)+max(4636K^3+9K,532K^5+9K).

Here B_NB002 is exactly the same fixed-public-h, beta-blind finite predictor, not a newly designed encoder or decoder. In particular,

    R_stat = Theta_K(max{M^(-1/2),[1+ln(1+Q/(M max(beta,1/M)))]/Q})

uniformly over beta, including beta varying with M, and every legal dyadic Q, with no upper restriction on Q. The cap is retained in the upper. The profile itself is below one: s<=1/8 and, since Mb>=1 and Q>=16, f<1/4. There is no missing constant-risk branch.

The stationary full-history benchmark is Theta_K(M^(-1/2)); thus SF1 describes an internal information loss in this particular master, not an output-grid obstruction. This is not a joint-K sharp result and proves nothing for K=2 or the excluded M<64 range beyond the inherited separate theorems.

## 1. Precisely inherited ingredients

1. IU001 (1.1), its accepted pre-integration reduction, for A=76KM/Q and J the actual terminal pair's number of prior visits:

       risk(B)<=min(1,2^16 L+3 E min(1,A/(J+K))
                              +P(J+K<4A)+9K/Q).

   Its Section 1 defines the R011 scale L; directly L<=g<=K^(5/2)/sqrt(M).
2. IU001 Lemma 4.1, for a **stationary** path, beta>0, d=|supp(pi)|<=K^2:

       E min(1,A/(J+K))<=min(1,(dA/M)[17+ln(1+480/(beta A))]).

   The return-time argument in IU001 Lemma 2.1 also gives, without taking a suffix,

       P(J+K<4A)<=min(1,4dA/M).                             (SF2)

   Indeed, if 4A<=K the event is empty; otherwise k=ceil(4A-K) is a positive integer <=4A. Conditional on the terminal state of positive mass p, its probability is <=k/(Mp), and summing against p gives SF2. This is exactly the original stationary horizon, not a transferred half-horizon. **No burn error appears.**
3. NB002 supplies, for all beta including zero and every legal h,

       risk(B)<=min(1,2^16 L+7 Psi(76K^5/Q)+9K/Q),

   with Psi(x)=x(1+ln(1/x)) for 0<x<1 and Psi(x)=1 for x>=1.
4. SM002 supplies on the original stationary interface, simultaneously as separate lower bounds,

       R_stat>=2^-226/Q,
       R_stat>=1/(32 sqrt(M+2))>=s/64.                      (SF3)

   The second is its Section 6 binary IID full-history two-point bound; it holds for all Q, not only the Q>sqrt(M) range where SM002 uses it to finish its master lower. The IID sources are stationary and lie in every D2(beta). No arbitrary-start R011 lower is silently restricted to stationarity.
5. IP002 supplies only on K>=3,M>=64,beta<=1/16,16<=Q<=M/4,

       R_stat >= 2^-331/Q ln(1+t/8),
       t=min{Q/(Mb),M/Q}.                                  (SF4)

   Its finite-domain and min cutoff are retained throughout the argument below. These lower witnesses need not coincide; we use simultaneous inequalities, not summed risks from one witness.

## 2. Stationary upper, including zero beta

Combining the first two ingredients and d<=K^2 gives for beta>0

    risk_stat(B)<=min(1,2^16 L
       +(K^3/Q)[4180+228 ln(1+(120/19)Q/(beta K M))]+9K/Q).  (SF5)

The constant is **76(3*17+4)=4180**, not the arbitrary-initialization coefficient 8360, and the original +9K/Q is still present. There is no epsilon_beta term, since IU001 Lemma 4.1 is already a stationary actual-terminal result.

If beta>=1/M, b=beta. Set x=Q/(Mb). Since K>=1,

    ln(1+(120/(19K))x)<=2+ln(1+x).

Consequently SF5 is at most

    min(1,2^16 K^(5/2)s+(4636K^3+9K)f).                    (SF6)

If 0<=beta<1/M, b=1/M and f=(1+ln(1+Q))/Q. Put c=76K^5>=1. For every Q>0,

    Psi(c/Q)<=c[1+ln(1+Q)]/Q.

For Q<=c this follows from the unit cap and c/Q>=1. For Q>c it follows from ln(Q/c)<=ln(1+Q). NB002 therefore gives

    risk_stat(B)<=min(1,2^16 K^(5/2)s+(532K^5+9K)f).        (SF7)

Both bounds concern the very same predictor. Equations SF6–SF7 prove the upper in SF1, including beta=0 and the crossover beta=1/M. The proof's case analysis does not change the predictor and does not implement beta estimation or adaptive budget selection.

## 3. A domain-completion lemma for the lower

Write x=Q/(Mb); always 0<x<=Q. We show that the truncated IP002 logarithm plus the statistical and IID floors controls f uniformly. All comparisons below hold for real Q>=16, so in particular for the required dyadics.

### 3.1 beta>1/16

Here b>=beta>1/16. The inequality ln(1+x)<=x yields

    f<=1/Q+16/M<=1/Q+2s,                                  (SF8)

using M>=64. By SF3, f<=(2^226+128)R_stat.

### 3.2 Outside the useful IP002/Q range

For all q>0, ln(1+q)<=4q^(1/4): integrate

    1/(1+u)<=u^(-3/4), u>0,

which follows from u^(3/4)<=1+u. For Q>=1, therefore

    f<= [1+ln(1+Q)]/Q<=5Q^(-3/4).                          (SF9)

If Q>M^(3/4), SF9 gives f<=5M^(-9/16)<=5s. Independently, if Q>M/4, it gives

    f<=5*4^(3/4) M^(-3/4)<=5s,

since M>=64 and 4^(3/4)=64^(1/4). Thus either failure of Q<=M/4 or Q<=M^(3/4) is covered by the stationary statistical floor alone: f<=320R_stat. This is an all-Q argument, not a large-M asymptotic exclusion.

### 3.3 Remaining domain: beta<=1/16, Q<=min(M/4,M^(3/4))

IP002 is now legal. Let y=M/Q and t=min(x,y). If x<=y, ln(1+x)=ln(1+t). If x>y, Q<=M^(3/4) implies Q<=y^3; hence x<=Q<=y^3, and

    ln(1+x)<=ln(1+y^3)<=3ln(1+y)=3ln(1+t).

Also (1+t/8)^8>=1+t, so ln(1+t)<=8ln(1+t/8). In either case,

    f<=1/Q+(24/Q)ln(1+t/8)
      <=(2^226+24*2^331)R_stat <2^336 R_stat.              (SF10)

Together with s<=64R_stat, SF8–SF10 prove the lower in SF1 in every parameter branch. In particular the IP002 cutoff M/Q has **not** been discarded: it is absorbed only where the logarithms are explicitly comparable; elsewhere the statistical floor controls the whole target surcharge.

For the claimed profile cap, f<=[1+ln(1+Q)]/Q is decreasing in Q>0, since ln(1+Q)>Q/(1+Q). At Q=16 this is <1/4 (ln17<3), while s<=1/8.

## 4. Interpretation and genuinely closed gap

The candidate is confirmed on its stated domain. The earlier IP002 warning that its lower was not by itself an all-Q formula remains correct. The new step is the domain-completion comparison in Section 3 together with extracting the zero-burn stationary bound from IU001. In particular, the loss of the M/Q cutoff is a real algebraic step, not an extrapolation of its finite-message tube argument.

The stationary full-history lower in SF3 and R011's inherited full-history upper <=2^16 L give the benchmark Theta_K(s). Alternatively the upper benchmark follows by using B_NB002 at arbitrarily large public Q and letting the upper numerical error tend to zero in the infimum over full-history procedures. This is not a claim that an infinite-precision implementation has finite resources.

This all-Q theorem strictly strengthens the stationary part of a precision-threshold result. It does not establish an all-Q arbitrary-initialization profile: SF5 uses stationarity essentially and its zero burn must not be transferred to that larger class. No conclusion is made about modified master encoders, extra exact ports, different grids, or architecture-universal precision limits.

## 5. Implementation and costs remain unchanged

No kernel, master, finite weight, decoder port, suffix, grid, guard, or word-size convention changes. For ell=ceil(log2(M+K+4)), p=4h+4ell+64, N=M+2, n=M+3, all accepted NB002/IU001 full-resource charges remain:

| Coordinate | Same charge |
|---|---|
| Hybrid depth / width | O(Kp^2) / O(Kp) |
| Heads total / max layer; max QK dimension; score cap | 6 / 4; 2K; 2 |
| Complete online arithmetic words/products/guards | <=128p bits |
| Dense coefficient slots / bits (zeros and biases included) | O(K^3p^4) / O(K^3p^5) |
| Active records / explicit holds | O(Kp^2+K^2) / O(K^2p^3) |
| Addressed sparse program/coefficients/holds | O(K^2p^4) bits |
| Masks / positions | O(n^2+n log(n+1)) bits |
| Observed one-hot input | O(NK) bits; acquisition/conversion separately paid |
| Rolling scalar-neural work, excluding stored data | O(nKp^2) bits |
| Uncached attention bitwork | O(n^2(K+p)p^2) |
| Equally cached attention bitwork | O(n^2Kp^2), plus actual cache creation/storage/selection |
| Dense all-token pointwise and QKV bitwork | O(nK^3p^6) |
| Rational-log work / scratch | O(p^3 log^2(p+1)) / O(p log(p+1)) |
| Five full-score cache creation / evaluator code | O(p^3) plus logs / O(p^4) bits |

Offline generation still pays all public configuration, layouts, masks, positions, constants, gates/terms/holds, addressing, sorting and actual format writes. For R_rec records, conservative generation/sorting costs O(R_rec p^2) bitwork and O(R_rec p) scratch; dense coefficient-bit writes include zero entries.

Peak means maximum simultaneous phase sums: program/parameters, input, metadata/masks, history/QKV, residual/master/weight/normalized/output banks, controller/addresses, and scratch. A safe dense forward sum remains O(K^3p^5+n^2+n log(n+1)+NK+nKp^2), replacing only the stored program by O(K^2p^4) in sparse format. Offline scratch coexists with retained generated data. Rolling work is not peak; packed bits and scalar-neural bit channels are different accounting conventions; one requested output does not erase all-token work.

The separate PURE expansion retains depth O(T_bit+p), width O(S_bit+p), sparse gates/holds O((T_bit+p)(S_bit+p)), dense coefficient bits O(p(T_bit+p)(S_bit+p)^2), and generic dense bitwork O(p^2(T_bit+p)(S_bit+p)^2). T_bit includes every online control/movement/copy/clear/attention action and S_bit includes all simultaneously live data. No hybrid resource assignment is transferred to PURE.

No total-word savings, training attainability, measured emitted artifact, hardware-fault theorem, or time/space advantage over paid direct counting is claimed. Publicly configuring Q from a beta promise is not automatic unknown-beta budget adaptation.
