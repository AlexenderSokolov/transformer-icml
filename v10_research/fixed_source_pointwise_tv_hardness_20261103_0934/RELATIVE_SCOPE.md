# Absolute, relative and coarse-approximation scope

2026-11-03. This additive clarification concerns only the fixed-source predictor family in `RESEARCH_NOTE.md`; it preserves all earlier files and involves no new diagnostic or random operation.

Here p=1/M² and every binary input word z satisfies 1/M<=q(z)<=3/(2M). Since q(z)>p, its true-source TV is q(z)-p. Its absolute value is at most 3/(2M)-1/M²=O(1/M), but relative to the source's success probability p it is bounded below by

  TV(z)/p >= (1/M-1/M²)/(1/M²) = M-1,

and above by 3M/2-1. Thus the small absolute TV guarantee is not a small relative error for this rare-event probability.

Let z_id=h be the identity edit, which is legal for every budget k>=0, and let OPT be the pointwise maximum of q(z)-p over legal edits of the fixed h. Both are positive. Independently of the formula's satisfiability,

  TV(z_id)/OPT >= (1/M-1/M²)/(3/(2M)-1/M²)
                 = (2M-2)/(3M-2) >= 3/5   for M>=4.

The final inequality is equivalent to 10M-10>=9M-6. Hence identity is a polynomial-time 3/5-multiplicative approximation **within this constructed family**, without finding a satisfying assignment or knowing a hidden source. In particular the earlier exact and inverse-polynomial additive-witness hardness does not establish constant-factor approximation hardness; indeed this construction admits the stated coarse factor. It also does not establish the factor for other models, source distributions, losses or risk definitions. The maximum possible additive regret of the identity is at most 1/(2M), again within this family, since the complete q range has that width.
