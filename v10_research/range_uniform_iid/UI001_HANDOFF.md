# UI001 handoff

Candidate result: BA001/SH001 exact one-block local ratio family admits a stationary binary IID lower c(D,r)/Q uniformly for all finite real κ>=1 and Q>=1 and every β∈[0,1]. No frozen file changed; no full two-resource theorem claimed.

Proof: `UI001_range_uniform_iid_floor_v1.md`. Heavy-window public reveal removes high-leverage terms, conditional Efron–Stein controls all residuals, and a truncated-Beta posterior bound makes the short-curve good alphabet constant. Explicit constants included.

Diagnostics: `python v10_research/range_uniform_iid/UI001_diagnostics_v1.py` passed 1,728 exhaustive conditional cases over κ=1,10⁴,10¹⁸,10¹⁰⁰ and 38 posterior-local-integral cases, plus constant/probability checks. Floating-point diagnostic initially failed at κ=10¹⁰⁰ due to subtracting a huge known selected constant; fixed by computing residual variance and score derivative directly, matching the proof. This was a numerical diagnostic issue, not a change to the theorem. Diagnostics are not formal verification.

Independent audit requested from root. Audit priorities: overlap count after reveal, max-pattern event under all frozen queries, posterior on truncated interval including boundary modes, seed-independent prior, real-grid rounding, and full-history branch when M<ceil(CQ²).
