# Exact Max-3SAT identity

2026-11-03. This additive derivation uses the model, source and legal edit budget of `RESEARCH_NOTE.md` and does not change it or add any experiment.

Let v*(phi)=min_(x in {0,1}^n) V_phi(x), the minimum number of violated clauses. From any history h, replacing its first n editable positions by any prescribed assignment x changes at most n=k positions and leaves all other positions and the protected terminal pair unchanged. Since the model output depends on the first n edited bits only through V_phi and p=1/M²<q(z), the maximum of the true next-symbol TV over legal edits is exactly

  max_(z legal from h) |q(z)-p| = Q-p - v*(phi)/(2MP),

for every h, not merely for all-zero h. The fixed map that replaces the first n bits by a minimum-violation assignment attains this value at every h; this is an existential source-independent map, and finding the assignment is not assumed free. Therefore, for every initial pair law mu,

  R*(phi,mu) = Q-p - v*(phi)/(2MP).

The equality upgrades the preceding satisfiable/unsatisfiable bounds to an exact affine relation with the Max-3SAT optimum m-v*. If an algorithm outputs R* exactly, v* can be recovered using rational arithmetic. If it outputs v with |v-R*|<1/(4MP), nearest-integer rounding of 2MP(Q-p-v) recovers v*. These are complexity reductions from already-known Max-3SAT, not a new general Max-3SAT algorithm or generic neural verification novelty. They concern this fixed-source expected-TV value, a specified variable-width model family, and unrestricted legal source-independent history kernels. No claim of NP membership for the general expected-value functional, strong hardness under unspecified encodings, or a coarse constant-factor approximation lower bound follows.
