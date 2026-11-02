# FN001 handoff

## Useful result

The specific FG001 IID folded-grid encoder loses its deeper packing benefit under one fine-grid perturbation just BEFORE coarse quantization: radius delta=1/(4Q), M=Q^4 and paid P>=max(log2 M,Jh) give worst-source risk Omega(Q^-1), while its clean risk is O(Q^-2) for J>=2. Only the first rail is changed. All later folded rails are unchanged by sample complementation. The source-independent attack clips the first rail to 1/2 in the delta-window.

Exact terminal-pair side information is retained, not silently discarded: pin the same pair 01 under both source laws, complement the remaining generated symbols, and keep initial flags fixed. The common mass costs p_+p_- and yields

    max risk >= (delta/2)(1/4-delta²/4)[1-2exp(-Mdelta²/2)]_+.

If Mdelta²>=2log4 this is >=3delta/64. With no side port the stronger lower delta/4 holds under the same condition.

## Status and evidence

Fresh independent review: PASS; see FN001_independent_review.md for binding verdict. Separate same-model reviewer with inherited context, not a blind/cross-model/formal review. Independent execution passed 9,396 collision cases and 360 exact full observation-law comparisons retaining all terminal-pair outcomes. The theorem's candidate header records writing-time status; the final review/handoff is the status authority.

Author diagnostics: 74,016 exact integer count cases, 39,264 attacked gate collisions, 34,752 outside-gate identities, 24 exact rational probability cases. Separation cases through Q32,M2^20: at Q32,J3 the rigorous terminal-side lower is approximately .00097650 and clean upper .00054932. Non-dyadic mean-rounding mismatch retained as negative control. Reproduce with `python v10_research/folded_noise/check_fn001.py`. Independent diagnostics are separate.

## Model diagrams / boundaries

FN001: history -> exact finite mean and folded G_P rails -> ONE bounded G_P fault -> floor at Q -> J labels plus specified exact side bits -> any decoder.

PE1: raw finite H -> digital codeword in G_h -> ONE bounded canonical G_h fault -> decoder/cleaner. For delta<1/Q that canonical fault is necessarily identity. These are not the same fault timing.

FG001 broad arbitrary H-valued boundary labels are NOT all covered: an additional orientation label can defeat this particular pairing. Likewise arbitrary M with rounded mean, universal encoders, Hilbert-curve encodings, internal arithmetic faults, or guard fixes are not covered. No source noise/training/hardware claim is made.

## Next decision

This bounded counterexample is closed once independent review passes. It is more informative to retain it as a representation-specific scope result than claim a universal robustness law. A new guard or robust fixed-capacity construction would require a newly specified complete noisy port and paid implementation; no such theorem or speculative fix is asserted here. Root may choose whether that separate question is scientifically worth pursuing. No existing frozen artifacts were edited and no publication, purchase, user send, or external contact was performed.
