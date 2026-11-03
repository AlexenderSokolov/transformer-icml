# Independent review of history-length corollary v2

**Disposition: ACCEPT conditional on the companion statistical bound.** Reviewed `history_length_corollary_v2.html` SHA-256 `a579c445522658691ac9686f804f28e0bcc3f695647c901242ab66875af375f5` and compared it with preserved `history_length_corollary_v1.html` SHA-256 `936695593c9b1dd7daf923f67771281bb439fb8e351286a364e9a38fcbcbe040`. The companion statistical note is SHA-256 `87b8129d99c89f8909a77fa9d711df70dfbe8a64bd107ccda1dc7fb90e8cb788`.

The v1 text stated ε<1/288 without excluding ε=0 even though its reciprocal expressions were undefined there. V2 expressly requires 0<ε<1/288 and separately states that the positive minimax lower bound forbids zero worst-source risk at finite N. Both corrections are mathematically sound.

For that positive range, c min{1,sqrt(A³/N)}≤ε with c=1/288 forces the square-root branch and N≥A³/(288²ε²). The add-one sufficient condition M=N−2≥(50+120 max{1,B})²A³/ε² follows from the companion upper on its stationary bounded-reverse-mixing class; its witness family belongs when B≥7 because the chosen reverse-mixing majorant sums to 7 from t=1. The iid binary necessary bound and source/estimator quantifiers remain correct. No changes to the v1/v2 source files, no tests, RNG, simulations, enumeration, or scientific-code execution.
