# FOP-U: first-order binary positional upper (root candidate)

Pending independent review. Throughout N>=64, 0<=k<=N, and 1<=r<=N+1 are integers. This is the new experiment in PLAN.md, not a claim for the old triple-count observation.

Let q_0=a=P(0,1), q_1=t=P(1,0); predict the flip probability at the actual protected terminal symbol. J_u counts departures i=0,...,N-1 from u, C_u counts its flips. Observe four pair counts and raw boundary windows of r symbols, 1<=r<=N+1. No minorization certificate is assumed. All transition tables and all starts are allowed.

Define the finite g-normalized factor of a single k-blind map at fixed (N,r) as its supremum of R/g_N(k) over all 0<=k<=N and qualifying sources, starts and legal kernels; then infimize over such maps. Stationary and arbitrary-start versions use the same definition. This is not the ratio to the exact known-budget minimax risk.

## Exact weighted hitting scale

For a,t>0, p=(t,a)/(a+t), H_0=1/t,H_1=1/a. Put B=max(1,a+t). Then h_0=max(H_0,1/p_0)=B/t and h_1=B/a, so

sum_u p_u q_u h_u = B <=2.                                      (1)

If a=0<t, state0 is absorbing. The weighted terminal contribution of state1 is

t P(X_N=1)=P(D_0=N+1)<=2/(N+2)                                 (2)

for starts at1, by the universal two-state first-hit bound; a start at0 contributes zero. Exchange symbols for t=0<a. If a=t=0, both flip probabilities vanish. Thus arbitrary starts and reducible boundaries require no certificate.

## Generic lemmas used and exact scope

The accepted v1 positive supplement proves universal occupation P(J_terminal<w)<=d^2 w/(N+1), generic endpoint/occupation tails, generic weighted half-imbalance <=288d/N sum p q h, and old-prefix reciprocal <=(3d^2+2d^3)L/N. These statements are about arbitrary homogeneous finite-state chains and apply with d=2 here. Their proofs do not require an order-two source. The independent row-stack empirical proof uses one Bernoulli stack per row and d^2 occupation; using two rather than four rows only reduces its bounds, so the conservative constant512/sqrt(N+1) holds unchanged. This last reduction should be checked explicitly by the independent reviewer.

Consequently, with n=floor(N/2),

E[q_terminal 1{J>0,J_half<J/256}] <=1152/N                      (3)

for the irreducible case by (1). For a reducible one-absorbing case, simply drop the event and use (2), which is smaller; for two absorbing states it is zero.

## Suffix gate

Set m=min(r-1,floor(N/2)), O'_u=J'_u - number of suffix departures from u in indices N-m,...,N-1. The last m+1 raw symbols reveal exactly these m departures. The terminal symbol is not a departure. For r=1, m=0 and O'=J'. O dominates the first-half count on clean paths.

Use qhat=C'/J' if J'>0 and 512O'>=J', otherwise0. The complementary output is a probability distribution. It is budget-blind and uses no hidden parameters.

One edited symbol changes at most two edge patterns and one state occurrence, so the safe simultaneous bounds |C'-C|,|J'-J|,|O'-O|<=6k used in the accepted deterministic gate proof continue to hold. Protection fixes the selected row. Thus exactly the same pathwise gate reduction gives empirical error +48k times the old reciprocal +weighted imbalance +tails P(J<6156k+1)+P(J<3078k+1).

With d=2, L=1+ln(N/(m+1)), the reciprocal constant is28, and the two occupation tails sum to at most

[36936k+8]/(N+1).

Combining (3), the empirical comparator, and N>=64 yields

R <= min(1, 1024/sqrt(N) +(1344L+36936)k/N).                    (4)

Indeed 512/sqrt(N+1)+1160/N <=657/sqrt(N)<=1024/sqrt(N).

For g_N(k)=max(N^-1/2,k/N), L>=1 gives

R <=39304 L g_N(k) <2^16 L g_N(k).

Since m+1=min(r,floor(N/2)+1), N/(m+1)<=max(N/r,2)<=2(N+1)/r. With ell=1+ln((N+1)/r)>=1, L<=ell+ln2<=2ell. The all-start finite g-normalized competitive factor is therefore at most 2^17 ell, with no certificate assumption. The oracle floor below converts this to at most 96*2^17 ell <=2^24 ell relative to the corresponding exact same-information known-budget minimax risk; it does not preserve the same numerical constant.

## Exact computed gate bit in the separate scan model

Replace O' by the first-half count J'_half and transmit the exact bit 1{512J'_half>=J'}. It is computed after corruption by scanning the whole word, not a raw sampled coordinate. The decoder separately tests J'>0. The generic half reciprocal calculation gives, with d=2, the bound

E[1{J_half>=J/1024}/(J+1)] <=2*d^3*1023/N =16368/N.

Thus the corruption coefficient is 48*16368+36936=822600<2^20, and

R<=min(1,1024/sqrt(N)+2^20 k/N).

No minimal-message assertion is accepted until a lower is established.

## Known-budget rate candidate

For the same observation, when k>=1 use qhat=(C'-6k)_+/(J'+6k+2); for k=0 use (C'+1)/(J'+2). The generic weighted-minimum proof with d=2 and (1) gives

E min(q_terminal,A/(J+2)) <=1536 A/N+768/N.

One-absorbing boundaries are bounded directly by (2), and two-absorbing boundaries contribute zero, so this bound covers all sources. The accepted pathwise lower-envelope inequality and A=24k+2<=26k give

R <=1024/sqrt(N)+768/N+39936 k/N <=41056 g_N(k) <2^16 g_N(k).

For k=0, universal occupation and layer cake give P(J=0)<=4/(N+1), E[1/(J+2)]<=4/sqrt(N+1), so the conservative bound1024/sqrt(N) suffices.

### Explicit known-budget lower, in the new dimensions

Use stationary IID Bernoulli sources; their next-symbol distribution is Bernoulli(p) at either terminal state, so actual-terminal TV is ordinary absolute error in the predicted probability of symbol1. Identity corruption is legal at every budget. Put n=N+1 and p_plus/minus=1/2 plus/minus 1/(16sqrt(n)). The single-letter KL inequality d(p||q)<= (p-q)^2/[q(1-q)] gives full-word KL<=1/8; Pinsker gives TV between the two word laws<=1/4. Nearest-target testing therefore gives average absolute prediction error >=3/(128sqrt(N+1))>=1/(64sqrt(N)) for N>=64. Predictor randomization does not improve the testing lower.

For k>=1, use uniform prior p in[1/4,3/4]. On the first N editable symbols with n1 ones, keep a uniformly selected b floor(n1/b) subset of its ones, b=k+1, and delete the remaining ones; preserve X_N. It changes n1-b floor(n1/b)<=k bits on every input. Conditional on retained size h and final bit U, the output arrangement is p-independent and uniform among h-subsets: for any specified retained set, conditional probability given n1 is binom(N-h,n1-h)/(binom(N,n1)binom(n1,h))=1/binom(N,h). The final bit is independent of the editable clean symbols given p, so it does not invalidate that identity.

Thus the full corrupted observation factors through at most D=2(floor(N/(k+1))+1) labels (h,U), followed by a p-independent channel. Realize that channel and the decoder using independent seeds and freeze both. There are at most D output probabilities for symbol1. On a prior interval of length ell0=1/2, the union of radius-v neighborhoods of those outputs has mass at most2Dv/ell0, irrespective of p-dependent label selection. Integrating its complement from0 to ell0/(2D) gives Bayes absolute error >=ell0/(4D)=1/[16(floor(N/(k+1))+1)] >=(k+1)/[16(N+k+1)]>=k/(48N).

Averaging frozen seeds retains this bound, so some source gives it. The same fixed strict kernel is used for the entire prior, and the last bit contributes two labels rather than being conditioned away. Combining separate clean/edit minimax witnesses gives at least g_N(k)/96, including k=0. It holds for known k and full corrupted word; hence it also holds for the natural pair-count/boundary observation, and for arbitrary starts by stationary inclusion. This completes the candidate same-information oracle sandwich g/96 <= Rstat <= Rall <=2^16 g, pending independent review.

## Boundaries

All claims above are candidate derivations in the new first-order/pair-histogram/one-protected-symbol model. They do not establish lower separation, optimal finite competitive factor, minimal alphabet, first-order restriction under triple counts, or a new version of the accepted manuscript. No files from that manuscript were changed.
