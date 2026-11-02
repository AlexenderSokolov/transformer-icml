# Independent substantive extension review — BAI004 author v3

2026-11-02. Reviewer: `independent LLM reviewer`. This review newly audits section9, rather than inferring it from approval of v2. The complete v2 audit is in `BAI004_review_v1.md`. No author file was edited.

## Verdict

**The new phase/count argument is valid; one minor zero-parameter proof branch must be explicit before clean acceptance.** The stated bound remains correct, and its positive-beta proof has no substantive gap. However the statement includes beta=0 full-support stationary sources with b=t=0, whereas(9.3) divides by b and the subsequent estimate uses ln(1/b). Add the following preliminary branch to section9:

> If beta M²<1, the universal occupation argument from section5 already proves (BAI4.2), with constant16<=100. Hence the rest of the proof may assume beta M²>=1, so beta>0 and full support forces b,t>0.

This closes every zero divisor and does not alter the theorem, constants, or scope. Alternatively b=0 could be handled directly by the deterministic one-step phase, but the inherited weak-beta branch is simpler.

Author v3 SHA-256 reviewed:

    4167ba8fa26ac6beb237016274b928682bdceb2575120b1924a7b823fd654fd6

## New section9 audit

### 1. Exact count balance

At initial W=00 and terminal B=10, the difference between counts of01 and10 over pair times0,...,M-1 is exactly X_(M+1)-X_1=1. Let k be the last A visit. No B visit can occur strictly between k and M: after such a B visit the path would either return A or enter W and subsequently need another A to reach terminal B, contradicting the last-A definition. No A visit occurs there by definition. The remaining phase is exactly either A→B, or A→C followed by C holds then C→B.

Thus J_A(M)=J_A(k)+1 and J_B(M)=J_A(k), including both relevant endpoint exclusions correctly. The smoothing denominator+2 therefore transfers with NO off-by-one correction.

### 2. Exact complete-message-compatible convolution

The phase-length masses are U_C(1)=1-b and U_C(l)=bt(1-t)^(l-2) for l>=2. Conditional on the state A at time k, future transition probabilities are independent of the previous path. Every terminal-B path has exactly one last-A decomposition. Therefore(9.1) is an exact nonnegative convolution of actual-terminal occupation functionals, not a heuristic relation between endpoint marginals. All previous visits are carried through the count equality above. No iid-row assertion is introduced.

### 3. Last-A times k>=M/2

For M>=16 this region has k>=8, so BAI4.1 applies within its proven horizon domain. Its cutoff max(sqrt(beta),1/k) is no smaller than d0 for horizon M, making its logarithm no larger. Also1/k<=2/M. This gives80A0G/M. The relevant phase masses form a sub-sum of a probability law, so their total is at most one.

### 4. Long C-hold contribution

For k<M/2, the phase length l=M-k exceeds M/2; in particular l>=2 and l-2>=M/4 for M>=8. Thus U_C(l)<=bt exp(-tM/4).

The count inequality b E_W V_A<=1+Mt is valid for the GLOBAL visit count, even after any number of returns to W. Each counted A visit's outgoing transition can be exposed one step beyond the observation endpoint. Expected C entries equal b E V_A, and their number is at most C exits plus one. The path begins W, so no time-zero C exit occurs, leaving at most M eligible departures through time M. No extra final-visit correction is needed.

The same exact chronological visit-cost identity and Jensen argument from v2 then yield(9.3), provided b>0, which the requested preliminary branch ensures. Since beta<=1, d0<=1 and G>=1+ln(1+1/A0). The stated logarithmic inequality follows from1+K/A0<=K(1+1/A0) for K=(1+x)/b>=1.

Multiplication by the phase density produces the factor b x exp(-x/4), which correctly retains b in front of ln(1/b). The bounds x exp(-x/4)<=2, x² exp(-x/4)<=9, and b ln(1/b)<=1/Euler_e give2G+9+2/Euler_e<=12G. Therefore the total92 is safely covered by100.

### 5. Short horizons, cutoff, and scope

For8<=M<16 the direct cap A0/2<=100A0/M is valid for every A0>0 and avoids an invalid short-horizon invocation of BAI4.1. The outer unit cap is legitimate. Symbol swapping preserves the pair-count argument and gives initial-C/terminal-A.

The scope updates correctly state that all crossing-terminal components from diagonal starts are controlled, while opposite-diagonal terms and the complete arbitrary-start risk remain open. Earlier sections are unchanged except for truthful status/scope language.

## Fresh independent diagnostics

`BAI004_review_phase_diagnostic_v1.py` independently computes both terminal-A and terminal-B local-time distributions and compares their exact phase convolution. It checks84 parameter sets, including b=t=0 and b=t=1 boundary examples, five A0 values from0.0001 to1000, and horizons through64. All26,880 horizon/convolution comparisons passed; the largest absolute discrepancy was approximately2.22e-16. The new upper was also checked at horizons8,15,16,31,64. These are numerical corroboration, not formal verification; the proof and the explicit zero-parameter branch remain necessary.
