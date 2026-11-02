# BT002 — finite-domain scalar completion for the entropy cutoff

2026-11-02. Independent scalar derivation. This note proves only the displayed numerical inequalities; it does not establish the entropy-channel lower bound to which they may be applied. BT001 is unchanged.

## 1. Result

Let M>=64, 1<=k<=M, e>=1/M (in particular e=max(sqrt(beta),1/M)), and let c,C be any fixed positive real constants. Define

    s=M^(-1/2), epsilon=k/M,
    A=1/(e k), B=c k/log(k+2),
    L=log(1+min{A/C,B}),
    F=epsilon[1+log(1+A)].

Set

    D(c,C)=7+log(max(1,C))+6 log(max(1,2/c)).

Then, uniformly over the entire stated finite domain,

    F <= D(c,C) max{s, epsilon, epsilon L}.             (SCALAR1)

The constants do not depend on M,k,e,beta. For k=0 define F=0, omit A,B,L, and the desired risk-profile completion is immediate from the clean floor.

Consequently, if a risk R has three separate lower bounds

    R>=a_s s,  R>=a_e epsilon,  R>=a_l epsilon L,

with positive constants independent of M,k,e, then

    R >= min(a_s,a_e,a_l)/D(c,C) * max{s,F}.            (SCALAR2)

Here distinct witness sources may establish the three bounds; only their maximum is used. No sum of their risks or exchange of source supremum with a suffix sum occurs.

## 2. Proof of (SCALAR1)

### Small k: the complete corruption profile is below the clean floor

If k<=M^(1/4), use e>=1/M and k>=1 to obtain A<=M/k<=M. Thus

    F/s <= M^(-1/4)[1+log(1+M)]
         <= M^(-1/4)[1+log 2+log M]
         <= 1+log 2+4/exp(1) <4.

The last bound follows by maximizing x^(-1/4) log x over x>=1; its maximum is 4/exp(1), at x=exp(4). Since D(c,C)>=7, (SCALAR1) follows in this case. This is a finite inequality, not an asymptotic statement about thresholds.

### Large k: the truncated logarithm retains the full logarithm up to constants

If k>M^(1/4), then M<k^4 and

    A<=M/k<k^3.                                      (1)

For k>=1,

    log(k+2)<=2 sqrt(k).                              (2)

Indeed 2 sqrt(k)-log(k+2) is positive at k=1 and has derivative 1/sqrt(k)-1/(k+2)>0. Put q=max(1,2/c). Equation (2) gives B>=(c/2)sqrt(k), and hence

    1+sqrt(k)<=q(1+B).

Using (1), 1+k^3<=(1+k)^3, and 1+k<=(1+sqrt(k))^2, we get

    log(1+A)<=3 log(1+k)
             <=6 log(1+sqrt(k))
             <=6 log q+6 log(1+B).                   (3)

There are two exhaustive branches.

- If A/C<=B, then L=log(1+A/C). Since 1+A<=max(1,C)(1+A/C),

      F<=epsilon[1+log max(1,C)+L]
       <=[2+log max(1,C)] max{epsilon,epsilon L}.

- If A/C>B, then L=log(1+B). Equation (3) implies

      F<=epsilon[1+6 log q+6L]
       <=[7+6 log q] max{epsilon,epsilon L}.

Both constants are bounded by D(c,C). This completes the proof.

For (SCALAR2), the separate floors imply R>=a min * max{s,epsilon,epsilon L}, where a min=min(a_s,a_e,a_l). Equation (SCALAR1), D>=1, and the same clean floor imply max{s,F}<=D max{s,epsilon,epsilon L}.

## 3. Completion directly from a truncated suffix sum

Fix a positive integer j0, c>0, and C>=1. Let

    U=min{1/(C e), c k^2/log(k+2)},  J=floor U,
    T=(1/M) sum_(j=j0)^J (1+j/k)^(-1),

with the sum defined to be zero if J<j0. Then

    F <= D(c,C)[1+log(1+j0)] max{s,epsilon,T}.         (SCALAR3)

This statement includes cutoffs below j0, floors in J, bounded k, and all finite M>=64.

To prove it, put L0=log(1+U/k), which equals L from §1 with the same C. If J>=j0, monotonicity gives

    T/epsilon = sum_(j=j0)^J 1/(k+j)
       >= integral_(j0)^(J+1) dx/(k+x)
       =log((k+J+1)/(k+j0))
       >=log(1+U/k)-log(1+j0/k).

If J<j0, then U<j0 and directly L0<=log(1+j0/k). In both cases, since k>=1,

    epsilon L0<=T+epsilon log(1+j0)
               <=[1+log(1+j0)] max{epsilon,T}.

Apply (SCALAR1) with the same C to conclude (SCALAR3).

Thus, if the entropy argument proves R>=a_T T and separate bounds R>=a_s s and R>=a_e epsilon, all with positive constants independent of M,k,e, then

    R >= min(a_s,a_e,a_T)
         /{D(c,C)[1+log(1+j0)]} * max{s,F}.

No supplementary requirement that J>=j0, that k diverge, or that the logarithm be large is needed.

### Author-cutoff specialization

For C=8, c=2^(-44), and j0=4096, the constant is explicitly

    D(2^(-44),8)[1+log 4097]
      =[7+273 log 2][1+log 4097] <1830.

Thus the author cutoff `J=floor min{1/(8e),2^(-44) k^2/log(k+2)}` and the sum beginning at j=4096 satisfy

    F<=1830 max{s,epsilon,T}.                         (SCALAR4)

If the sum starts at 4097 instead (for example after changing from transition horizon t to suffix length j=t+1), use `[7+273 log 2][1+log 4098]<1830` as well. The indexing in the underlying probability lower bound must still be matched exactly.

## 4. Scope

The only process-related input used here is the scalar inequality e>=1/M. In particular no new stationarity, Hamming-kernel, entropy, terminal-pair, or common-prior claim is proved in this note. Such lower-bound ingredients must be established separately before this completion is invoked.
