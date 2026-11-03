# Visual QA: pages 1-28

- Reviewed: 3 November 2026.
- PDF: `build/main.pdf`, 55 pages.
- Final PDF SHA-256: `6e3a3f2d836fd8e3a3fda0e4305f3dd290f3b3f23fe4113891f787e2c9576764` (verified before and after the final comparison).
- Method: independently rendered pages 1-28 with Poppler `pdftoppm` at 120 dpi, producing 1020 × 1320 pixel PNGs. Opened every page individually at its original rendered resolution with `view_image`, in sequential batches of four. This was not a contact-sheet-only review.
- Scope: clipping, overlaps, glyph rendering, equation and table readability, spacing, pagination, headings, margins, and page numbers. Mathematical correctness is outside this visual check.
- Final rebuild check: the original visual inspection used PDF SHA-256 `efc9a7587763389e71754c082b2a8a6a162946462e98c770f93578563c862c63`. After the bibliography-only cleanup, independently re-rendered all 28 pages with the same 120-dpi settings. Every new PNG had the same SHA-256 as its originally inspected counterpart, establishing exact rendered identity for pages 1-28 without claiming a second visual inspection.

## Result

**Pass: no visual defects requiring correction found on pages 1-28.** Text, equations, matrices, tables, and page numbers are legible and remain inside the page margins. No visible missing glyphs, clipped elements, overlapping material, or broken table layout were found. The document consistently uses no running header and centered footer page numbers.

Page 12 has substantial blank space below the conclusion of the main text; Appendix A starts on page 13. This is a clear main-text/appendix boundary, not a rendering defect. Multi-page theorem and proof continuations remain readable.

## Page-by-page coverage

| Page | Inspection result |
| --- | --- |
| 1 | Clear title, date, abstract, and introduction; no collision or clipping. |
| 2 | Clear section heading and equations (2.1)-(2.3). |
| 3 | Observation definitions and long equation (2.7) remain legible; equation tag is separated cleanly. |
| 4 | Theorem statements and displayed bounds fit within the margins. |
| 5 | Piecewise estimator and bounds render cleanly. |
| 6 | Section transition and gate-bit formula are clear. |
| 7 | Table 1 is aligned and legible; section and subsection headings are clear. |
| 8 | Piecewise decoder, numerical model, and displayed bounds are legible. |
| 9 | Table 2, resource expressions, and precision bound fit cleanly. |
| 10 | Prior-work prose and citations are readable with consistent spacing. |
| 11 | Prior-work subsections and discussion transition are clear. |
| 12 | Main-text conclusion is legible; intentional-looking appendix boundary leaves lower-page whitespace. |
| 13 | Appendix A opening, occupation estimates, and proof text render cleanly. |
| 14 | Tail bounds, subsection transition, and proof continuation are legible. |
| 15 | Hitting-time formulas and next lemma opening fit within margins. |
| 16 | Equations (A.6)-(A.11) and dense proof text remain readable. |
| 17 | Change-of-measure displays and subsection A.4 are clear. |
| 18 | Weighted bounds and subsection A.5 opening render cleanly. |
| 19 | Reciprocal-count proof and long bound (A.16) are legible without overlap. |
| 20 | Gate proof and Proposition A.9 displays are clear. |
| 21 | Equation (A.19), subsection A.7, and oracle formulas fit cleanly. |
| 22 | Dense proof and displayed bounds remain readable with clear footer separation. |
| 23 | Appendix B opening, transition matrices, and proof text are legible. |
| 24 | Mixture equations and relocation-lemma transition render cleanly. |
| 25 | Relocation formulas and Proposition B.3 opening fit within margins. |
| 26 | Matrix (B.8), covariance bounds, and proof text are legible. |
| 27 | Reversal identities and grouped bounds are aligned and readable. |
| 28 | Hitting-time formulas and null-word mass bounds render cleanly. |
