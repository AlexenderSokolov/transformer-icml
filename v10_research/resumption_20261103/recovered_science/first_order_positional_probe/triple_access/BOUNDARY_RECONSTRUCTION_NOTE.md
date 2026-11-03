# FOT003: endpoint reconstruction from exact local counts

Root-authored small information-interface note, pending independent check. No accepted manuscript or addendum is edited. This is an elementary pathwise flow identity, not a new stochastic proof or a novelty claim.

## Exact identity

For any binary word Z_0,...,Z_(M+1), let Y_i=(Z_i,Z_(i+1)), i=0,...,M, and let H_abc be the M triple counts. For each pair u=(a,b), define

out(u)=sum_c H_abc,     in(u)=sum_c H_cab.

Then, deterministically on every word,

out(u)-in(u)=1{Y_0=u}-1{Y_M=u}.                         (1)

Proof: each triple is a directed edge Y_i->Y_(i+1); summing its contribution to out-in telescopes over i=0,...,M-1. Loops cancel as well. Therefore

I(u)=out(u)-in(u)+1{Y_M=u}=1{Y_0=u}.                    (2)

Given the exact eight triple counts and final pair, I is a one-hot vector specifying the initial pair exactly. This recovers the CORRUPTED initial pair from the corrupted counts and corrupted final pair, not the clean initial pair. No stationarity, transition model, source certificate, or clean-word information is needed. Only valid word observations occur in the experiment; an algorithm can choose an arbitrary fallback for incompatible input vectors without changing risk.

## Consequences for the accepted matched first-order interface

The accepted FOT002 suffix count identity is

N_ab(suffix)=sum_c H_abc +1{Y_M=(a,b)}-1{Y_0=(a,b)}.

Substituting (2) shows the even simpler exact formula

N_ab(suffix)=in((a,b))=sum_c H_cab.                      (3)

Indeed these are pair edges at raw positions1,...,M, the M true transitions of the truncated suffix Z_1,...,Z_(M+1). Thus the arbitrary-initial-pair repair remains valid without a separately supplied initial pair. It can be implemented directly by triple IN-degrees. The initial edge is still discarded; its law is not being assumed homogeneous. All FOT002 conditional-kernel arguments, budgets, losses and constants remain unchanged.

Consequently the accepted first-order upper uses only the exact triple histogram and raw suffix of length r>=2. The lower still grants both boundary windows. In the separate exact-message experiment, the baseline (eight triple counts plus protected final pair) is information-equivalent to the previously explicit r=2 baseline (counts plus both endpoint pairs). A deterministic inverse reconstructs the omitted pair; adding it obviously costs no information in the other direction. Thus the minimum supplemental alphabet two and its upper risk bound carry to the baseline WITHOUT separately supplying the initial pair, still with no growing raw windows or side channels. This is not a claim about noisy or approximate counts.

The decoder's reconstructed J and C now use the in-degree counts (3); its half-visit bit is still computed by scanning the corrupted truncated suffix. The proof-only conditioning on clean X0 in FOT002 is unchanged and is not confused with the reconstructed corrupted initial pair.

## Natural pair-count analogue and limits

For ordinary first-order edge counts N_ab and observed final symbol, out-in=initial-symbol indicator minus final-symbol indicator, so the initial symbol is likewise determined. This explains the matching endpoint-baseline variants in that natural model. It does not reconstruct an entire path or longer raw windows, nor make positional order generally sufficient or redundant. Counts and final pair determine only the initial pair in the richer experiment; they do not reconstruct earlier visit times.

The existing addendum's explicit both-pair baseline remains true, but its initial-pair input is redundant under exact counts. This note supplies the separate derivation that the prior selection memo prudently required before dropping that input. The no-certificate first-order theorem, known-budget sandwich and finite logarithmic factors are not otherwise strengthened or reparameterized. Future integration may simplify the reconstruction display; no accepted bytes have been modified now.
