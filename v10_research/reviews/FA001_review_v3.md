# Independent narrow revision audit — FA001 v3

## Result first

**ACCEPT v3's constructive all-operations finite-arithmetic bridge for the specified finite-data affine/ReLU causal-attention subclass.** The public-record-layout ambiguity identified in the full v2 review is now explicitly resolved. No new mathematical or cost-ledger blocker was found. This is a narrow revision audit supplementing, not replacing, the preserved full v2 review and independent exact diagnostics.

Target SHA256: `94a9d64f2a2eedf50cb7e918cfeec4e8cac6e78f21de214a528a853b4f17e073`.

## Verified delta

The complete v2-to-v3 diff changes only the title, version/history paragraph, and first paragraph of §6.1. The numerical proof, model restrictions, precision selection, terminal interface, sequential row schedule, and remaining cost ledger are byte-for-byte unchanged. All six source/artifact hashes declared in `FA001_source_bindings_v3.json` match the actual files.

The new §6.1 specifies:

- each converted public parameter/table/bias/scale record has exactly `P+c_arch` bits, with a fixed architecture-only range/sign allowance;
- indices are implicit in sequential order, with no hidden per-record w-bit address;
- converted public storage, sequential format writes/reads and explicit zeroing are `O_arch(UP)`;
- hidden-state, projected Q/K/V and arithmetic scratch records retain `O_arch(w)` slots and their full guard widths;
- loading a public record into scratch explicitly sign-extends/pads it at `O_arch(w)` cost, covered by the existing affine/edge budget;
- the alternative implementation with Θ(w)-padded public records must pay `O_arch(Uw)` storage, writes, zeroing and peak instead, and is not the implementation used for the compact ledger.

These choices are consistent: primitive public scalar ranges are uniformly bounded and P>=1, so `P+c_arch` signed bits suffice after conversion. The input descriptions still separately pay b bits and conversion scratch; compact converted storage is not a claim that descriptions themselves fit in P bits. The finite number of sequential data streams and implicit positions do not require random access. Sign extension changes representation, not precision or numerical values. Its linear word cost is dominated by the already charged arithmetic work. Input reformatting, duplication, masks and metadata remain separately charged.

## Acceptance and preserved limitations

The previously accepted proof of pre-cut error `<=1/Q`, using `P=4h+C_arch`, remains intact. It establishes the numerical bridge from integer primitives, rather than assuming CA001's approximation contract. Transfer to CA001 remains restricted to its fixed-density, source-independent, branch-independent masks and formal frozen-branch domains. Nonempty masks alone support only the numerical theorem. Signed floor semantics, exact final cut rather than label agreement, full accumulators, all supplied-data/offline/peak charges and separate hybrid-versus-PURE implementation costs remain required.

No extension to layer normalization, arbitrary nonlinear maps, arbitrary old emitters, interleaved singleton-copy heads, free public generators, free RAM or mixed implementation coordinates is accepted. No rerun of the unchanged numerical diagnostics was necessary for this layout-only revision. The v2 exact-rational diagnostics and their PASS result remain preserved and hash-bound.

No frozen source or original v2 review artifact was modified by this audit.
