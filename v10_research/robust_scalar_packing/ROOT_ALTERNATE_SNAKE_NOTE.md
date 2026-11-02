# Independent alternate snake derivation (not an accepted theorem)

Root working note, 2026-11-02 07:43 UTC. This is a separately derived candidate, not the author's RP001 formula or an additional accepted unit. Do not change the reviewed RP001 candidate to match this note. Geometric output packing is established prior art; no originality claim.

For N=2^k>=4, Q=16N, let U=T^k(t) and V=T^k(t+1/(2N)), using the periodic first-step extension T_ext(u)=2u-4 ReLU(u-1/2)+4 ReLU(u-1). Later tents are ordinary. On t in [0,1], the extended first input is in [0,1+1/(2N)], and subsequent states remain bounded.

Set s=clip(N(V-1/2),-1,1), computed by k saturated doublings, and
f=min(U,ReLU(s))+min(1-U,ReLU(-s)).
Let X=clip(t-f/N+1/(2N),1/(2N),1-1/(2N)); eta=1/N and Y=clip((U-eta)/(1-2eta),0,1).

On each row i, q=Nt-i: the phase pair selects the orientation correctly and f=min(q,N(1-q)). Thus X is exactly (i+1/2)/N for q<=N/(N+1), then moves linearly to (i+3/2)/N over the final row fraction 1/(N+1). The final clamp handles the last row. Y is constant at the appropriate endpoint during each such connector, since the connector is contained in min(U,1-U)<=eta. The larger Y plateau also includes the beginning of each row. The initial and final plateaus give endpoint error of order N^-2.

For observations (Xobs,Yobs) within epsilon<1/(2N), choose i=clip(floor(N Xobs),0,N-1), y=clip(Yobs,0,1), u=eta+(1-2eta)y, and z=(i+u)/N for even i, z=(i+1-u)/N for odd i. On a vertical section the row is unchanged and inversion is exact before perturbation. On a connector the selected row is one of its neighbors; either inverse lies within eta/N plus epsilon/N of the boundary. Actual t is within eta/N of that boundary. This suggests |z-t|<=2/N²+epsilon/N. With total finite-evaluator+fault+floor error epsilon=9/(4Q), this is 548/Q². A full formal all-input proof and source binding are not completed here; do not cite this note as accepted.

Root exact Fraction checks ran for N=4,8,16, t=a/(4N²), all three endpoint/zero errors in each coordinate at epsilon=9/(4Q). All 12,123 cases passed the proposed bound. Largest observed Q²-scaled error was 831/2. Finite checks do not prove the universal bound. The scalar 1/(1-2eta) is rational, bounded by2, but not generally dyadic; a generic FA finite approximation would need its own ledger and error contract. Author's distinct RP001 candidate uses dyadic coefficients and retains a conservative nearest-segment decoder instead.
