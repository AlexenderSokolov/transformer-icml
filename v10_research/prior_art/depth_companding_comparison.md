# Depth and companding: bounded primary-source comparison

Checked 2026-11-02 about07:02UTC, after the06:56 scientific theorem freeze but before v4 production. This is attribution/context, not a new accepted mathematical unit or a novelty certificate. Generic search terms only were sent externally; no private proof text was uploaded.

## Probability companding is established prior art

Aviv Adler, Jennifer Tang, Yury Polyanskiy, *Efficient Representation of Large-Alphabet Probability Distributions*, IEEE Journal on Selected Areas in Information Theory3(4),651–663, issue December2022; DOI10.1109/JSAIT.2023.3234502. The primary PDF states publication6January2023 and current version13June2023. Source: https://web.mit.edu/jstang/www/papers/companders_JSAIT.pdf ; arXiv:2205.03752.

Read abstract, SectionI encoding definitions, SectionII Theorem5(power companders), SectionIII background and Remark9. Scalar nonlinear transformation followed by uniform quantization and inverse/normalization is established. Theorem5 covers powers x^s, including s=1/2; the minimax compander behaves like a square root near zero. The paper studies quantizing a known probability vector under KL, with asymptotic and nonasymptotic statements and its own decoding choices. It does not supply this project's actual-terminal Markov occupation argument or its bounded-primitive depth certificate. GD001 must NOT present square-root companding itself as newly invented. The specific explicit dyadic network, directional arithmetic, conditional-row normalization and required/sufficient depth order are separate obligations proved in the dossier.

## Depth–weight-precision conversion is also established

Weigutian Ou, Philipp Schenkel, Helmut Bölcskei, *Three Quantization Regimes for ReLU Networks*, arXiv:2405.01952v1,3May2024. Primary source https://arxiv.org/pdf/2405.01952 . Read abstract/introduction and Section4 Proposition4.1 with its immediate interpretation (PDFpp18–19). The result constructively replaces higher-weight-precision networks by functionally equivalent lower-precision deeper networks, increasing width by a constant factor; its parameter is coefficient precision and it discusses memory scaling. The full AppendixF proof was not audited here.

This is relevant prior depth–precision language but not the same resource coordinate: GD001 keeps internal precision and all parameter/working-memory costs paid, changes bounded-primitive depth before an observed-summary grid cut, and measures Markov prediction risk. Do not claim priority for the general idea that depth can trade with precision, or cite Proposition4.1 as proving GD001. State the different experiment explicitly.

## Evidence boundary

No identical theorem was located in this narrow screen. That is not proof of novelty, exhaustive coverage, or publication suitability. No claim about unread appendices or a stronger prior-art exclusion is made. Existing weighted-inventory, Hahn sensitivity/correction, and Han–Jana–Wu source-construction attributions remain necessary.
