# Exact statement — A-interface-001/prover v1

Obligation: `e63118febbe61f49babfa4ff00fd3f98670834ab63719699cc3023e336bd6736`.

Under D1-D3 and prototype A of D4, for every fixed K>=2 and beta>0 construct a theta-independent causal family implementing the finite-history smoothed conditional reference P_{N,s}=(a_s+lambda_N v0)/(u_s+lambda_N), lambda_N=1/(N-2), v0=1/K, to a deterministic uniform error sup_{H in [K]^N,s} TV(Pi_N(H;s),P_{N,s}) <= epsilon_N with an explicit theta-independent epsilon_N->0. Prove the complete actual circuit: charged fixed predecessor copying, K^2 ReLU context encoding, beta full-context Q/K scores, query-independent values producing matched q_s and uniform (r,mu_all), terminal frequency selection, all residual/query/length channels, and a strictly simplex probability readout covering n_s=0. Give an explicit finite resource upper bound (L,W,H,D_qk,B_param,B_arith,score_range), with defined precision semantics and accounted multiplication, reciprocal, projection or legal replacement, smoothing and rounding. Derive a deterministic located-error bound including q,r,u and query/binding errors; use the shared-statistic identity to avoid an unjustified universal u^{-2} gain. Clearly separate nominal fixed beta from arithmetic errors and fixed networks from accuracy-dependent families. This is a local actual-circuit prerequisite, not C1 or root closure.

## Constructive specialization proved

For each fixed K>=2 and beta>0, for every N>=3 and integer J>=4 the proof constructs a finite, theta-independent, rationally encoded D3 implementation Pi_(N,J), strictly positive and exactly summing to one, with sup_(H,s) TV(Pi_(N,J)(H;s),P_(N,s)) <= 1/J. Taking J=max(4,N-1) gives epsilon_N=1/max(4,N-1). All resource/precision conventions and a conservative all-inclusive upper bound are given in exact-proof.md. The network is a family indexed by N,J; no fixed-network convergence, learnability, C1 completion, C2 lower bound, or root completion is asserted.

This file and exact-proof.md are versioned together by VERSION.json, containing their SHA-256 digests. No self-referential file hash is claimed.

