# MD001 — Sharp mixing-dependent primitive-depth threshold at the statistical grid

2026-11-02. NEW post-stage6 author candidate. Requires fresh independent review and explicit root acceptance. No accepted file or freeze is edited.

## Theorem and exact comparison scope

Fix an alphabet K>=2 and fixed bounds on width, head count, coefficient/operator norms, reachable states, local radius r, retained output coordinates D, finite exact boundary-symbol budget, dense causal mask density, readout budget, and number of affine/ReLU primitives per counted stage. Use precisely GD001's uniform growing-depth FA family: all frozen boundary branches satisfy the ideal contracts on every formal history; the synthetic terminal initial state uses only the declared finite boundary and public data; all historical initial local tables are strictly below it. The paid evaluator has a depth-uniform pre-cut error E/Q, E=1 supplied by GD001's uniform extension. Its P=4h+c(d+2) precision is paid, not hidden. The decoder sees only the complete Q-grid bank, declared fixed boundary, public metadata and independent randomness. No interior history, unquantized denominator or auxiliary state crosses the cut.

For sufficiency require capacity admitting GD001's explicit complete K³-histogram and rolling coordinatewise compander: in particular D>=K³ and r>=3, enough fixed width, fixed per-stage coefficient budget up to four, and its bounded temporary ranges. D and r alone do not imply this inclusion. Fixed trailing local tables are paid; dense masks and causal prefixes are as in GD001. Larger admitted widths can ignore extras. No growing per-layer DAG, fan-in, hidden readout circuit, or unbounded amplification is free.

Observe M+2 symbols of the homogeneous second-order source, M>=64, with hidden stationary pair law Π and ALL-STATE certificate P²(s,t)>=βΠ(t), β∈[0,1]. Predict the actual terminal row in expected TV, for stationary initialization or uniformly over arbitrary initial laws. Fix positive constants c_-<=c_+ and legal dyadic grids Q>=16 in the band c_-sqrt(M)<=Q<=c_+sqrt(M). Define

    e_K=max(β,1/M)   (K>=3),
    e_2=max(sqrt(β),1/M),
    f_K=1+ln(1+Q/(M e_K)).

For every fixed target C_risk>0, every admitted depth-d procedure with risk<=C_risk/sqrt(M) obeys

    1+d >=c_nec(1+ln f_K).                            (MD1)

For some sufficiently large fixed target C_suff depending only on the fixed capacity/bounds, K and c_-, there is an admitted fully paid finite procedure with

    risk_all<=C_suff/sqrt(M),
    1+d<=C_depth(1+ln f_K).                           (MD2)

Thus for each fixed C_risk>=C_suff, the infimum feasible **1+primitive depth** is Θ(1+ln f_K), uniformly over β,M and legal grids in the band, for BOTH initialization experiments. With depth convention d>=1, one may omit the added one on the left. Necessity holds for every target multiplier; feasibility at arbitrarily small target multipliers is not asserted. Empty legal-grid bands create no instance. Constants are not alphabet- or architecture-uniform.

## Upper proof

MD001_upper.md proves for the SAME GD finite program

    R_all<=min{1,C_K[M^-1/2+Q^-1+G(γQ,M e_K)/(γQ)]},
    G(z,t)=1+ln(1+z/t), γ=2^L.

Choose f_K<=γ<2f_K. Then G(γQ,t)/γ<=2 and primitive depth is O(L+1)=O(1+ln f_K), proving MD2. Every attention logit is zero, so attention weight ratio κ=1. The growing quantity γ is compander gain, not attention range. This binary upper needs the newly proved purity-clipping and all-zero-bank lemmas; it is not obtained by simply substituting sqrt(β) into GD001.

## Lower for K>=3: precise adaptive extension of GD001

GD001 lower §1 supplies Γ_d<=C^d and single-late-symbol sensitivity <=Γ_d/M, with C fixed independently of d,M,Q. Its rescaled tube §3 supplies, for β<=1/16 and z=Γ_d Q (at least 1),

    R_stat >=(c/z)ln(1+min{z/[M max(β,1/M)],M/z}/8),

where c>0 depends only on fixed architecture/boundary/E bounds, not depth. Only z<=M/4 is needed here; no new large-z claim is used. Source is GD's three-symbol stationary waiting/active witness, extended on unused symbols as stated there. All-state minorization, actual terminal query and common-prior scope are inherited exactly.

Here are all fixed-band inversion cases. Set x=Q/(M e_K), f=1+ln(1+x), Γ=Γ_d, z=ΓQ. Pick F>=max{1,2(1+ln8)} sufficiently large that

    (exp(t-1)-1)/(8c_+²t)>=exp(t/2)-1 for all t>=F.

If β>1/16, f<=1+16Q/M<=1+2c_+, hence Γ>=f/(1+2c_+). If z>M/4, Γ>sqrt(M)/(4c_+) whereas f<=1+Q<=(1/8+c_+)sqrt(M), giving Γ>=f/[4c_+(1/8+c_+)]. In the remaining tube domain, f<=F gives Γ>=f/F, and Γ>=f is immediate. Otherwise f>F and 1<=Γ<f. The first logarithm branch is at least f-1-ln8>=f/2. The second satisfies M/(ΓQ)>=x/(Γc_+²)>x/(fc_+²), so its logarithm is at least f/2 by choice of F. The risk target implies Γ>=cf/(2c_+C_risk). Thus Γ>=c_*f uniformly in every case.

From Γ<=C^d follows d>=ln(c_*f)/ln C. Combined with 1+d>=1, this yields MD1 with a positive fixed constant: when ln f>=2|ln c_*|+2 use the logarithmic bound, and on the remaining bounded range use 1+d>=1. This avoids claiming a positive lower on ln f when f is bounded. The fixed stage-zero convention can be handled by Γ_0=1; if no global stage exists the late sensitivity is zero and this is an admissible overbound.

## Binary lower and initialization inclusion

MD001_binary_lower.md independently writes the complete nonlinear active-Markov coupling proof. It transfers GD's late sensitivity to Doob range and parameter derivative <=34Γ_d/M and <=34Γ_d j/M. At z=Γ_dQ and suffix cutoff floor(min{1/(4e_2),M²/(4z²)}), its tube has depth-independent good-message constant. BI001's active chain has terminal informative pair A probability at least 1/8; the target-specific finite-message lemma and pathwise stationary domination yield

    R_stat >=(c_B/z)ln(1+min{z/(M e_2),M/z}/8)

for β<=1/256,z<=M/4. The full inversion cases are in its §6; for β>1/256, e_2>=1/16 gives the same bounded-f branch. Hence Γ_d≳f_2 and MD1. This is not an IID-suffix argument or a conditional-uniform-prior claim. Stationary sources are contained in arbitrary-start sources for exactly the same procedure class, so both lower bounds obstruct arbitrary-start guarantees as well. The all-start upper implies stationary sufficiency.

## Consequences and limits

At β=0, both alphabets give f_K=Θ(log M) and depth Θ(1+loglog M). At β=1/M, K>=3 still needs Θ(1+loglog M) while K=2 needs Θ(1), for both initialization experiments. The contrast uses the same all-state certificate and actual-terminal loss, not a claim of global sqrt(β) mixing.

No all-Q depth frontier, growing-depth uniform 1/Q grid-floor lower, exact leading depth constant, optimal total storage/work, PURE fixed-width/shallow compilation, arbitrary internally rounded-network theorem, external novelty, publication/upload/contact or training attainability is claimed. All three MD proof files are new; the final statement is conditional on fresh review and root acceptance. Full cost meaning and promise-selection limitations are in MD001_upper §5 and the accepted GD ledgers; none is removed by this theorem.
