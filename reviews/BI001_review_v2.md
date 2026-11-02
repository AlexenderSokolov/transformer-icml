# BI001 v2 independent delta review

2026-11-02. **PASS recommendation; not root acceptance.**

The complete hostile review of v1 is `reviews/BI001_review_v1.md`, with independently executed exact diagnostics in `BI001_independent_checks_v1.py/.json`. I read the exact v1-to-v2 diff and verified both hashes. Sections 1–5 (the complete mathematical proof and constants) are byte-identical. The changes are only the candidate-status line, consequences in the Claim, and §6 consequences/scope.

V2 resolves the upper-comparison qualification from my full review: the binary matching upper is expressly limited to D>=8, r>=3, legal dyadic Q>=16 in a fixed square-root band, and a sufficiently large fixed target multiplier. Necessity continues to hold for every fixed D,r>=1 and every fixed target multiplier C>0. The new extension to beta<=M^-2 is immediate from `max(sqrt(beta),1/M)=1/M`, not a new mixing extrapolation. No proof constant, parameter domain, stationary source or decoder interface changed.

For clarity, the `C_suff` referred to in v2 can be taken to be the SH001/SB001 displayed sufficient multiplier specialized to K=2:

`C_suff=(2^13+2) 2^(5/2) + 3267/c_-`,

where `C_K=48*2^3*(2+1)+10*2^5*(2+1)=1632` and `c_- sqrt(M)<=Q`. This follows directly from the accepted SB001 upper for K>=2, not by applying SH001's K>=3 lower at K=2. In the weak regime its public budget `ceil(1+ln(1+Q))=O(log M)` gives the stated upper; integer rounding only changes constants.

I recommend the root may accept BI1 and these precisely qualified weak-mixing consequences. Optimal intermediate-positive-beta binary dependence remains unresolved. There is no formal-verification, external-novelty or unrestricted-architecture claim. No candidate or accepted dependency was edited by this review.
