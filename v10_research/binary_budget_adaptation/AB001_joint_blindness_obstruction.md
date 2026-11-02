# AB001 — Joint budget/certificate blindness is impossible (candidate)

2026-11-02. New research candidate; fresh independent full review and root acceptance required. No prior frozen manuscript is changed.

## Result first and exact scope

The protected-endpoint binary rate **cannot be attained by one estimator blind to both the edit budget k and the certificate beta**, even under stationary initialization. This does **not** resolve unknown-k adaptation when beta is supplied. It separates these two questions.

The experiment is the accepted SC003/BT002 full-corrupted-history experiment: N=M+2 binary symbols, homogeneous second-order source, all-state certificate P^2(u,v)>=beta Pi(v), arbitrary offline randomized strict Hamming-k corruption of positions 1,...,M, protected final pair, and unconditional TV loss at the original terminal pair. Our lower uses stationary sources only. The estimator may inspect every corrupted symbol, randomize, and have unlimited computation. The kernel constructed below is one parameter-independent map on all input words. No clean interior, edit mask, attack seed or unknown table is supplied to the estimator or kernel.

Fix M>=64 and an estimator A_M, independent of k and beta. Put r=1/(2M). For each a in [1/M,1/4], define the clean stationary source Q_a by

    theta_00(1)=a, theta_01(1)=b_a=r(1-a)/a,
    theta_10(1)=a, theta_11(1)=1-r,
    Pi_a=((1-a)/2, a/2, a/2, (1-a)/2)

in the state order 00,01,10,11. Let S_M(A) be the supremum of A_M's identity-corruption risk over this family. These are valid stationary sources in D_2(0).

Let Q_* be the stationary first-order symmetric flip-r source, represented as a second-order source, and let T=floor(M/8). For every 1<=k<=T there is a common source-independent protected strict-k kernel C_(M,k) such that

    R_*(A,C_(M,k)) >= [ (3k/(1024M)) log((T+1)/k)
                         -(8/3) S_M(A) log(2T/k) ]_+.      (AB1)

Here Q_* satisfies the all-state certificate with beta=1/M exactly. The risk on the left targets Q_*'s true row at its actual protected terminal context.

Consequently no collection A_M independent of both k and beta can satisfy a universal constant upper bound by

    H_2(M,k,beta)=min{1,max{M^-1/2,
         (k/M)[1+log(1+1/(k max(sqrt(beta),1/M)))]}}

simultaneously for all M>=64, all 0<=k<=M and all beta in [0,1], with the corruption term defined as zero at k=0. The impossibility already holds for stationary initialization; it therefore also holds for arbitrary initialization.

## 1. Membership and target checks

All Q_a probabilities are legal: 0<a<=1/4 and 0<b_a<=1/2. Write e=1-a and t=r in the fixed designated-exit coordinates (a,b,e,t). The displayed stationary vector is verified by Pi_00*a=Pi_10*e and Pi_11*t=Pi_01*b; its crossing masses agree and sum with the diagonal masses to one. At beta=0 the all-state certificate is vacuous. All these sources have full stationary support. We make no positive-beta membership claim for Q_a.

For Q_*, let T_r(x,y) be the binary one-step kernel, equal to r when y!=x and 1-r otherwise. Its stationary pair law is Pi_*(c,d)=T_r(c,d)/2, and

    P_*^2((u,v),(c,d))=T_r(v,c)T_r(c,d)
                       >=2r Pi_*(c,d).

Thus beta=2r=1/M holds for every starting pair, not merely on support. At terminal pair 00 the true probability of symbol 1 is r.

## 2. Rare one-flip words and clean conditional experiments

For each integer 1<=t<=M-1, define the full observed word

    x^(t)=1^(N-t-1) 0^(t+1).

It begins with 11, has its first zero at position N-t, and ends with 00. Under Q_* each such word has the same probability

    v_t=(r/2)(1-r)^M >=1/(8M),                       (2.1)

because (1-1/(2M))^M>=1/2. These words are disjoint events.

Under Q_a, the event that the initial pair is 11 and the first zero is at position N-t has probability

    w_(a,t)=((1-a)/2)(1-r)^(M-t-1)r.                 (2.2)

After that first zero the current pair is 10. Let L_(a,t) denote its t-transition continuation law with the Q_a table; retain the fixed preceding prefix. For an independently randomized A, set

    e_(a,t)=E_(L_(a,t)) [ |A(full_word)(1)-a| 1{terminal pair=00} ].

Different first-zero events are disjoint. Their contributions are genuine parts of the unconditional clean risk, with target a on terminal 00. Therefore

    sum_(t=1)^(M-1) w_(a,t) e_(a,t) <= S_M(A).        (2.3)

No conditional prior or conditional-IID assertion is used. Also

    v_t/w_(a,t)=(1-r)^(t+1)/(1-a) <=4/3.             (2.4)

## 3. One legal strict-budget kernel

The map is identity except on inputs x^(t) with k<=t<=T. On such an input:

1. Draw a uniformly on I_t=[k/(8t), k/(4t)].
2. Generate a length-t continuation from pair 10 using the explicit Q_a table.
3. Accept this continuation only if it never visits 11, its final pair is 00, and it contains at most k ones. On acceptance, replace the t zero suffix symbols by it. On rejection, return the original input.

All parameters used are functions of public M,k,t and the private auxiliary draw; the true source parameter is never read. The map is specified on every possible word and is identical across all sources. An accepted suffix changes exactly its number of ones, at most k. Its last two symbols are 00, so all changes are among positions 1,...,M. The preceding prefix and first zero are unchanged. Rejections make no changes. Hence this is a strict-budget, endpoint-protected offline kernel, not merely an expected-budget channel.

Continuous auxiliary randomization just defines a stochastic kernel on a finite input/output space by integration; no finite-rational implementation or efficient sampling claim is needed or made.

Every a in I_t lies in [1/M,1/4], since t<=T and 8T<=M.

## 4. Uniform acceptance mass

Compare L_(a,t) with a reference continuation having the same table except theta_01(1)=0. In the reference process, from last bit 0 the next bit is 1 with probability a, and from last bit 1 it is 0 deterministically. The continuation begins with last bit 0.

Let L be the number of emitted ones. Then E L<=at<=k/4, so P(L>k)<=1/4. The probability the final pair is 00 is at least (1-a)^2>=9/16, including t=1 (where the stronger lower bound 1-a holds).

Couple the actual continuation with this reference until its first transition 01->11. Before disagreement, each 01 departure corresponds to an earlier emitted one. A union bound over possible departures gives

    P(disagreement)<=b_a E L<=b_a a t
                   =r(1-a)t<=rT<=1/16.

On no disagreement the actual path has never visited 11. Thus the actual continuation's acceptance probability is at least

    9/16 -1/4 -1/16 =1/4.                           (4.1)

This proof uses an unconditional reference expectation before terminal conditioning.

For a in I_t we also have a>=1/M=2r. On an accepted continuation z, the triangle inequality gives

    |A(z)(1)-r| >= (a-r)-|A(z)(1)-a|.

After averaging accepted paths, (4.1) yields

    E [loss under Q_* after attack | x^(t),a]
       >= a/8 - e_(a,t).                            (4.2)

Rejected paths have nonnegative loss and were discarded. The estimator's seed is independent and can be averaged throughout.

## 5. Integrated constrained-risk calculation

The uniform density on I_t is 8t/k and its mean is 3k/(16t). Summing (4.2) over the disjoint null words gives

    R_* >= sum_(t=k)^T v_t [3k/(128t)
                            -(8t/k) integral_(I_t) e_(a,t) da].

By (2.1) and the harmonic integral, the positive part is at least

    (3k/(1024M)) sum_(t=k)^T 1/t
      >= (3k/(1024M)) log((T+1)/k).                  (5.1)

For the negative part, use (2.4), exchange finite sums and the nonnegative integral, and note that a in I_t implies 8t/k<=2/a. For each a, (2.3) controls the sum over all relevant t. Thus

    sum_(t=k)^T v_t (8t/k) integral_(I_t) e_(a,t) da
       <= (8/3) integral_(k/(8T))^(1/4)
                    (1/a) sum_(t:a in I_t) w_(a,t)e_(a,t) da
       <= (8/3) S_M(A) log(2T/k).                  (5.2)

This is the required common integration argument: the clean bound is not subtracted once from a collection of unrelated alternatives. Equations (5.1)-(5.2) and nonnegativity prove (AB1).

## 6. Impossibility conclusion

Suppose a joint-blind estimator had risk <=C H_2 for a universal finite C. Its k=0,beta=0 guarantee implies S_M(A)<=C M^-1/2. Choose k=floor(M^(3/4)); for sufficiently large M, k<=T. In (AB1), the ratio of the clean-error term to the positive term tends to zero, because M^(1/2)/k tends to zero and the two logarithms have asymptotically equal order. Consequently

    R_* >= c (k/M) log(M/k)

for some fixed c>0 and all sufficiently large M (the onset may depend on C). But at beta=1/M and k>=sqrt(M),

    F_2=(k/M)[1+log(1+sqrt(M)/k)]
         <=k/M+M^-1/2<=2k/M,

so H_2<=2k/M. The ratio diverges as log(M/k)~(1/4)log M, a contradiction. This is an asymptotic impossibility deduced from the exact finite-domain inequality, not a new finite threshold assertion.

## 7. What this theorem does not settle

A beta-informed estimator A_(M,beta) need not have small clean risk at Q_a when used with beta=1/M, because these Q_a may fail that certificate. The above proof therefore does not exclude k-blind adaptation for a supplied beta. It also does not exclude an estimator that knows k but not beta: its k=0 branch and k>0 branches are different maps, so (AB1)'s same-estimator premise does not connect their clean risks. SC003's known-k beta-blind estimator remains entirely consistent with this result.

The witness uses full corrupted words, not a fixed histogram restriction. The kernel is source-independent and endpoint-protected; its acceptance test and budget are exact. Both witness families are stationary. No causal-corruption, editable-endpoint, public mask/seed, neural-resource, external novelty or formal-verification claim is made.
