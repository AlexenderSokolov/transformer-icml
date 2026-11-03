# Fixed-source pointwise TV bridge for legal attacks

2026-11-03. Candidate mathematical consequence of the bounded-number 3SAT construction in `../growing_features_hardness_20261103_0922/RESEARCH_NOTE.md`; the underlying reduction and this bridge require independent review. This concerns one observed clean history, not an expectation over histories or a general unknown-source minimax lower bound. No sampling, random operation, external write or modification of prior work was performed.

## Fixed public source and conditional target

For each public history length M of the prior construction, take the binary iid process with p=P(X_t=1)=1/M². This single source is specified by M alone, regardless of the encoded 3SAT formula, the realized history, or attack choice. Its pair-state transition P has stationary pair law Pi=Bernoulli(p) tensor Bernoulli(p), and P²(u,v)=Pi(v) for every pair u,v, so the all-state certificate holds with beta=1. Start the iid process in its stationary distribution. The all-zero observed history h of length M+2 has probability

  P(H=h)=(1-1/M²)^(M+2) >= 1-(M+2)/M² >0.

For every observed history, including this h, the true conditional next-symbol law is Bernoulli(p). In particular p is a fixed, explicitly public number computed from M, not a secret theta or oracle revealing the current episode's latent source. In this example no source is sampled from a hidden mixture. The prior candidate's t=B(h)=1/(M+2) is a clean-history add-one surrogate, **not** the true p; the two objectives are compared below without conflating their targets.

## The legal source-independent attack and pointwise threshold

As in the prior reduction, normalize a 3CNF instance with n variables and m nonempty clauses, choose M as a power of two with M>=max(n²,m²,4), P the least power of two >=m, k=n, h=0^(M+2), and protect the last pair. The explicitly encoded model has d=m bounded integer additive features, constant-depth uniform attention/ReLU hybrid semantics, and rational output

  q(z)=Q - V(z)/(2MP),    Q=3/(2M),

where V is the integer number of violated clauses represented by the first n editable bits of z. A word has q in [1/M,3/(2M)] for every binary input. Since M>=4, q(z)>p=1/M². The TV error of the model's Bernoulli(q(z)) against this fixed source's true next-token law is therefore

  TV(z)=|q(z)-p|=q(z)-p.

Consequently the pointwise maximizers of true-source TV, of q(z), and of the clean-surrogate CE(t,q(z)) coincide. The last equivalence follows from q>=1/M>1/(M+2)=t and the strict positive CE derivative on the specified q range. The maximization itself can be defined and performed using only the public model and observed h by maximizing q(z): neither p nor any next label needs to be supplied to the attack. If reporting the actual TV value or comparing its numeric threshold, p is the fixed public function of M above.

The exact rational pointwise decision is

  exists legal z: TV(z) >= Q - 1/M² ?

Because all m clauses are satisfiable iff some budget-legal z has V(z)=0, the answer is yes iff the original 3CNF is satisfiable. Every assignment requires at most n=k editable bit flips; dummy positions do not change V; the protected pair remains 00. Thus 3SAT many-one reduces to the specified **single-history, fixed-source, source-independent** decision. A candidate mask is a polynomial-size witness, and the rational score/threshold can be checked in polynomial time, so the explicit restricted family is NP-complete. If one insists on a complete history-only attack kernel rather than just its action on h, extend any witness z to a map that returns z on exactly this h and returns its input unchanged on all other histories. This kernel is legal on every history and uses no source value or future label. The condition p is uniform across the source, so computing the pointwise maximizing action uses only the publicly specified q.

## Quantitative approximation and interpretation

Let Delta=1/(2MP). In any satisfiable instance the optimum pointwise TV is exactly Q-p, whereas any word with V>=1 has TV at most Q-p-Delta. Therefore an algorithm that, on every instance in this restricted family, outputs a legal word with pointwise TV regret strictly less than Delta would have to output V=0 whenever the formula is satisfiable. Checking the returned assignment decides 3SAT. As M and P are polynomially bounded by the explicit input size, this gives inverse-polynomial additive-witness hardness under P!=NP, not a constant-additive-error result or a generic hardness claim for all networks.

For this same one iid source, q(z) is always in [1/M,3/(2M)], so TV(z)<=3/(2M)-1/M² for **every** binary word, every h and every corruption. This is a simple single-source upper bound, not a general-source robustness or training theorem. Exact or extremely fine optimization can be computationally hard even when this absolute risk is uniformly small. Nothing here establishes hardness of evaluating the expectation over histories, optimizing expected risk, or learning the model; the high probability of h alone is not such a proof. In particular, do not confuse a pointwise optimization with the original worst-source, mean-over-trajectories risk.

## Precision, prior work and evidence

M and P are powers of two; p, Q, TV, the threshold and Delta are exact dyadic rationals with O(log M) bits in this construction. Position-incidence coefficients are in {-1,0,1}; each clause feature has at most three nonzeros and at most four possible integer values. The complete variable-width model, public masks and M-by-m position data are explicitly encoded at polynomial cost; the prior reduction gives the ReLU implementation and details. This is not an actual BLAS/NumPy certificate. Classical 3SAT and ReLU verification hardness already exist, including Sälzer and Lange (2021), https://arxiv.org/abs/2108.13179; no generic novelty is claimed.

`check_pointwise.py` records **each** tested fixed formula and each legal mask, complete bit word, source and threshold fractions, signed position incidences, local ReLU intermediates, additive banks, clause literal/violation values, q, true p, TV and gap comparisons, together with per-formula maxima. These are a new deterministic run's own original records, not regenerated original records from the prior author diagnostics. `pointwise_cases.jsonl.gz` is created exclusively and `check_pointwise.log` preserves stdout/stderr. No random samples, model initialization, missing-data recovery, or rerun of prior scripts is involved. The finite diagnostics corroborate, but do not replace, the all-instance proof.
