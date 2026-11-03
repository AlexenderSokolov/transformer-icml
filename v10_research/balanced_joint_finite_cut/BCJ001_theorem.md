# BCJ001 — Budget-blind balanced decoding of a twelve-coordinate finite noisy cut

2 November 2026. **New author candidate; independent full review and root acceptance required.** No accepted file is changed. Stationary claims use accepted CB004/BP001. All-start claims additionally use CB005, root accepted on 2 November 2026 at 14:25 UTC; they are not inferred from stationary reversal. This new BCJ001 unit itself is not yet accepted.

## 1. Fixed experiment and result

Fix binary homogeneous order-two sources with a qualifying stationary pair law Pi and ALL-STATE certificate P_source^2(i,j)>=beta Pi(j), 0<beta<=1. Let M>=64, n=floor(M/2), Q=2^h>=16, D=2^P with integer P>=h. The word has M+2 symbols, Y_j=(X_(j+1),X_(j+2)), 0<=j<=M. The target is the true next-symbol distribution at the actual terminal pair Y_M. Risk is unconditional expected TV, not conditional row risk.

A single source-independent offline randomized kernel replaces at most k of positions 1,...,M, with 0<=k<=M, preserving the last two symbols. It may inspect the complete word but has no source table, Pi, true initialization law, or future-symbol input. After the fixed encoder below, a cooperating one-shot VECTOR attack adds eta with ||eta||_infinity<=delta, 0<=delta<=1/4, to its twelve coordinates. Each coordinate is then clipped to [0,1] and floored to the Q grid. The second attack may inspect the actual finite bank and prior history, but has the same source-information exclusions; masks/seeds remain hidden. One-shot does NOT mean one scalar only. These are precisely the sequential channel conventions of JP001, now with a different explicitly fixed bank.

Only twelve received labels, the exact protected terminal pair, and public source-independent format metadata (M,h,P and fixed code/tables) cross the cut. NO history, initial pair, raw counts, denominators, clean bank, other outputs, internal residuals, or seeds survive. Public k,delta,beta may additionally be supplied when defining a more informed minimax decoder, but the constructive decoder ignores them. It needs no budget certificate or real-number input.

Put s=M^(-1/2) and tau=k/M+delta+1/Q. There is ONE deterministic finite-rational decoder, independent of k,delta,beta, such that

    R_stat(A)<=min{1, 2^16 s +4096/(M sqrt(beta))+2^23 tau}.       (U-stat)

Using the now-accepted CB005 all-start weighted imbalance theorem, the SAME decoder obeys

    R_all(A)<=min{1, 2^16 s +2^16/(M sqrt(beta))+2^23 tau}.       (U-all)

The encoder likewise depends on none of those three budgets. These hold simultaneously for ALL budgets, not only tau<=s.

For this fixed prefix, let R_stat^* and R_all^* be infima over arbitrary randomized real simplex-valued decoders, even supplied the public budgets. With e=max(sqrt(beta),1/M), f_e(x)=x[1+ln(1+1/(M e x))] for x>0 and f_e(0)=0, a universal c_*>0 satisfies

    R_stat^* >= c_* min{1,max{s,f_e(k/M),delta,1/Q}}.             (L)

Consequently for every FIXED c>0 on the nonempty band beta>=c/M,

    R_stat^* = Theta_c(min{1,max{s,k/M,delta,1/Q}}),              (F-stat)

and A attains this order simultaneously without knowing any budget. The same statement holds for arbitrary initialization using accepted CB005. Below that band, (U-stat) and (L) are only the proved bracket, not a claimed matching surface. This is a fixed twelve-coordinate encoder result, not a lower bound for redesigned deep encoders.

## 2. Encoder and exact finite identities

At key t=j+3, 0<=j<M, the paid radius-three local table outputs twelve bits:

* eight indicators of the trailing triple (X_(j+1),X_(j+2),X_(j+3));
* four indicators 1{j<n}1{Y_j=u}, u in {00,01,10,11}.

The second group uses a PUBLIC positional bit, not a data-dependent mask, future observation, or free history statistic. For padding positions 1,2 use public zero tables. The synthetic query is at M+3. One uniform head uses zero Q/K maps and the JP001 causal masks K_1={1}, K_2={1,2}, K_t={3,...,t} for 3<=t<=M+2, and K_(M+3)={3,...,M+2}. All tables, indicators, masks and zero coefficients are counted. Density remains at least 1/3. All twelve coordinates use the SAME denominator M; the last four are first-half subfrequencies J1_u/M, not J1_u/n. This normalization is part of the fixed interface.

Write N'_abc for corrupted-word global triple counts and L'_u for corrupted-word first-half row counts. Execute FA001's full-width integer evaluator with its positive shifted Taylor recurrence. At zero scores every edge has the SAME positive integer W_* (T_0=D already ensures positivity), including at P=h. The exact terminal accumulators are Z=M W_*, N_i=W_* D A'_i, where A' is (N',L'). Thus the actual pre-port output is EXACTLY

    a_i=floor(D A'_i/M)/D.                                      (2.1)

No approximation theorem or P=4h+C_arch premise is substituted: positivity, common-weight cancellation and exact quotient prove (2.1) for every P>=h. Output copying and identity padding add no further numerical truncation.

Let z_abc and w_u be the received grid labels. With x=A'_i/M in [0,1], clipping fixes x and is 1-Lipschitz, so

    |received_i-x| <= delta+1/D+1/Q <= delta+2/Q.                (2.2)

At zero noise, nested floors give exactly received_i=floor(Q A'_i/M)/Q. This also holds for the four positional coordinates. There is no assumption that independently perturbed coordinates sum to one or arise from any word.

## 3. Decoder and real perturbation lemma

Let u be the protected terminal pair and d(u) the complement of its first bit. Form

    C'=M z_(u,d(u)), J'=M(z_(u,0)+z_(u,1)), J1'=M w_u.

Output designated probability C'/J' when J'>0 AND 512 J1'>=J'; otherwise output zero. Output its complement for the other symbol. Nonnegative labels give 0<=C'<=J', so the active output is in [0,1]. Nothing requires J1'<=J', cross-bank consistency, row normalization, integer pseudo-counts, or an actual corrupted word realizing the pseudo-bank.

Let C,J,J1 be the original CLEAN counts at that same terminal row, q its true designated probability, and

    d=6k+2M(delta+2/Q) <=6M tau.                                (3.1)

An edited symbol changes at most three global triples, each by histogram l1 at most two; adjacent edits do not enlarge the union bound. Hence ||N'-N||_1<=6k. The first-half row indicators depend on two symbols per departure, so their coordinate changes are at most 2k (the looser 6k is also valid), including edits near the split. Equation (2.2) and the two selected triple coordinates therefore imply

    |C'-C|<=d, |J'-J|<=d, |J1'-J1|<=d.                          (3.2)

Here d is a real ANALYSIS quantity, never an estimator input.

Set G'={J'>0, J1'>=J'/512}, H={J1>=J/1024}, B={J>0,J1<J/256}, and E=1{J>0}|C/J-q|. On G' intersect H with J>0, normalization gives

    |C'/J'-q|<=E+8d/(J+1).                                     (3.3)

For J>=2d, J'>=J/2 and the ratio perturbation is <=4d/J<=8d/(J+1), since J is a positive integer. For J<2d, both ratios are probabilities and 1<=8d/(J+1); the latter follows from d>J/2 and J>=1. At d=0 the empirical ratios agree.

On G' intersect H^c, J1<J/1024 and J1+d>=J1'>=J'/512>=(J-d)/512 imply J<1026d. On G'^c outside B with J>0, if J'=0 then J<=d; otherwise J1'<J'/512 and J1>=J/256 imply J<513d. Therefore false gate statuses can occur only on small CLEAN rows even when the pseudo-bank has no cross-bank consistency. Rejection on B costs q. Paying J=0 and all false statuses by harmless enlarged tails yields

    R(A)<=E[E]+8d E[(J+1)^(-1)1_H]+E[q1_B]
            +P(J<1026d+1)+P(J<513d+1).                         (3.4)

This pointwise reduction works for all starts and arbitrary admissible adaptive/cooperating attacks; no independence of the errors is used.

## 4. Expectation, real thresholds, and constants

Accepted CB004 proves for ANY initial law and M>=128

    E[(J+1)^(-1)1_H]<=130944/M,
    E[E]<=8193 sqrt(32)/sqrt(M+1),
    P(J<w)<=min{1,16w/(M+1)} for every integer w>=1.             (4.1)

Its inverse-occupation proof conditions on the deterministic first-half history and applies the SC003 suffix terminal-occupation bound. It does not condition rows into IID samples. For a real t>=1, J<t implies J<ceil(t), so the two real-threshold tails in (3.4) sum to at most

    16(1539d+4)/(M+1).                                         (4.2)

This explicitly pays the ceiling overhead even when 0<d<1. Together (3.4)-(4.2) give

    R(A)<=8193sqrt(32)/sqrt(M+1)+64/(M+1)
            +1072176 d/M+E[q1_B].                             (4.3)

The first two terms are <=2^16 s for M>=64, and 1072176*6=6433056<2^23. Accepted BP001 gives E[q1_B]<=4096/(M sqrt(beta)) for stationary initialization. This proves (U-stat) for M>=128. For 64<=M<128 its capped displayed upper is 1, so unit loss completes the domain. Accepted CB005's all-start imbalance bound permits substituting its 2^16/(M sqrt(beta)) instead to obtain (U-all).

This use of CB005 is confined to the clean weighted bias. No all-start stationary-reversal argument is made here, and unsupported initial states are not silently dropped.

## 5. Fixed-prefix lower: fresh complete-bank IID calculation

JP001's eight-coordinate precision lower cannot simply be reused after adding four new informative ports. Instead we prove the needed lower for this complete twelve-coordinate bank using SM002's good-message argument, reproduced quantitatively here.

Let all observed symbols be IID Bernoulli(p), p in I=[1/4,3/4], and make every source row the same Bernoulli law. Then Pi is the product pair law and P_source^2(i,j)=Pi(j) for ALL i,j, so these stationary witnesses qualify for every beta<=1. The target designated orientation may vary, but TV for an arbitrary output is exactly its absolute error in probability assigned to symbol 1 relative to p. Use identity source editing and zero noise initially.

For each triple frequency, indicators have dependence radius two, so variance is <=5/(4M). For each first-half subfrequency L_u/M, pair indicators have dependence radius one; variance <=3n/(4M^2)<=3/(8M). These bounds use covariance magnitude <=1/4, counting all ordered overlapping pairs, with disjoint windows independent. Sum of the twelve variance bounds is <=23/(2M)<12/M. The mean vector g(p) has eight entries p^a(1-p)^(3-a) (with multiplicities by patterns), and four entries (n/M)p^b(1-p)^(2-b). By direct product differentiation, each coordinate has absolute derivative <=3 on [0,1].

If M>=120Q^2, Chebyshev plus union bound gives

    P_p(max_i |A_i/M-g_i(p)|<=1/Q)>=9/10.                        (5.1)

Choose a mesh of I of spacing at most 1/(3Q), including endpoints. It needs at most ceil(3Q/2)+1<=2Q points for Q>=16. Every p is within 1/(3Q) of a mesh point. On (5.1), each unrounded coordinate is within 2/Q of that mesh mean. Its final integer Q-grid numerator is therefore within 3 of the corresponding scaled mean, allowing at most seven integers per coordinate. Nested floors make this exact for the actual P-bit evaluator. Including all four protected-terminal-pair values, every good complete decoder message lies in a SINGLE parameter-independent set of size

    R<=8 Q 7^12.                                               (5.2)

Take the uniform prior on I. For a fixed independent decoder seed, at most R good messages yield R real estimates of p. Their radius a=1/(16R) neighborhoods have prior mass at most 4Ra=1/4. The joint good-event probability is >=9/10, even though the event depends on p. Hence expected absolute error >=(9/10-1/4)a>=1/(32R). Averaging the decoder seed and taking a source supremum proves

    R_stat^* >= 1/(256*7^12 Q)                                 (5.3)

in this large-M regime. No posterior-uniformity or deterministic parameter-to-message map is assumed.

For M<120Q^2 grant the entire history. Put N=M+2 and p_±=1/2±1/(16sqrt(N)). Their one-symbol chi-square is <=1/(12N), so product chi-square <=exp(1/12)-1<=1/11, and total variation <=1/(2sqrt(11))<1/4. The two-point absolute-estimation Bayes risk is >=1/(32sqrt(N)). Since N<122Q^2, this is >=1/(32sqrt(122)Q). Thus the uniform constant

    c_I=1/(256*7^12)

works for every M>=64,Q>=16. This also verifies the standard full-history statistical floor without granting any forbidden encoder port. This proof is a new specialization, not an unsupported invocation of UI001's no-hard-mask model or JP001's different bank.

## 6. Port coarsening and source corruption lower witnesses

If delta>=1/Q, take Q_c=max(16,least dyadic integer >=1/delta). Then Q_c<=Q, divides Q and D, and 1/Q_c<=delta. At EACH of the twelve coordinates the common source-independent map a_i -> floor(Q_c a_i)/Q_c is a legal perturbation of magnitude <1/Q_c. Clipping has no effect and final Q-flooring fixes the coarse label. Crucially,

    floor(Q_c floor(D A_i/M)/D)/Q_c
          =floor(Q_c A_i/M)/Q_c.                               (6.1)

Thus the attacked complete cut is EXACTLY this same twelve-port encoder at grid Q_c, including the first-half coordinates and protected pair. Applying section 5 gives R_stat^*>=c_I/Q_c. If delta<=1/16, 1/Q_c>delta/2; otherwise delta<=1/4 and 1/Q_c=1/16>=delta/4. If delta<1/Q, the fine-grid floor already dominates delta. Hence generally

    R_stat^* >=(c_I/4)max(delta,1/Q).                            (6.2)

The attack only reads the actual bank and public grids. It can even use fine-Q-grid shifts: set b_i=floor(Qa_i)/Q, c_i=floor(Q_c a_i)/Q_c, eta_i=c_i-b_i. Then a_i+eta_i=c_i+(a_i-b_i), with remainder in [0,1/Q), so final flooring is c_i and clipping is inert. This is one VECTOR attack, not twelve sequential injections.

Separately, set port noise to zero and use accepted BT002's protected-source-corruption witnesses. Any decoder behind this twelve-port encoder can be simulated from the full corrupted word, including the exact finite encoder and its labels. Source-independent public budgets add no unknown-source information. BT002 therefore supplies

    R_stat^* >=2^-54 max{s,f_e(k/M)}.                            (6.3)

These witnesses need not share a worst source with the IID witness. Taking their maximum, not summing risks, proves (L), for example with c_*=min(2^-54,c_I/4). Lower bounds remain valid for arbitrary starts because stationary starts form a subset; they do not depend on CB005.

On beta>=c/M, 1/(M sqrt(beta))<=s/sqrt(c). Also f_e(k/M)<=k/M+s/sqrt(c), using ln(1+t)<=t (k=0 separately). Therefore the upper and lower match the displayed rate on that band, with c-dependent constants. The construction is the SAME map throughout, so this is simultaneous unknown-budget attainment, not separately selected known-budget estimators.

## 7. Complete paid realization and information isolation

Let N=M+3, ell=ceil(log2(N+4)). Width sufficient for twelve old indicator coordinates, twelve output coordinates and paid finite local labels is fixed. The half indicator is generated/read by comparing the public departure counter to floor(M/2), or by a supplied position table; this is charged for all tokens. The local radius-three table, all twelve projections, all zero Q/K slots (including dense zero slots), public padding, every mask cell, synthetic query and acquisition of the protected two-symbol endpoint are generated/read/stored, not free heads or uncharged side channels.

Use the FA001/JP001 fixed-control sequential multi-tape schedule, with actual numerical-record count U and mask/metadata bit count F. Explicit fixed-width layouts have U=O(N^2), F=O(N^2+N ell), supplied description bitlength b=O(1) for the bit/zero tables. Take

    w=O(P+ell+log(P+1)+log(U+F+2)).

Full products, Taylor divisors, quotient remainders, counters and count guards fit this full word length; fractional P is not the accumulator width. Generate/copy public data in nested-loop order with O((U+F)w^2+w^4) bitwork, retaining descriptions Ub, converted numerical records UP and F metadata bits. Execute all tokens' QKV, all candidate edges/mask tests, Taylor steps even though weights coincide, value products, exact accumulations, row quotients, updates and copies. Forward work is O(N^2(P+1)w^2); rolling numerical arrays use O(Nw). Sequential scans/rewinds and all position tests are included, not random-access operations. A safe encoder peak is

    O(Ub+UP+F+N ell+Nw+w^4+b+P).

Here compact P+O(1) converted public records and wider w-bit arithmetic arrays are distinct. Retaining/clearing descriptors and duplicate tapes uses actual paid lengths. The w^4 allowance pays finite arithmetic microcode construction/storage, not a free interpreter scanned afresh per operation. Its one-time work is separately added above.

The external noise channel is not a claimed reliable finite physical injector. Read/write the twelve grid labels in 12(h+1) bits and the two endpoint bits. After the cut, terminal decoding needs only exact integer arithmetic on v=O(h+ell+1) bits: select the two triple labels and one half label, compare 512 w_u against z_u0+z_u1 (M cancels), compare the row sum with zero, and output the rational designated probability z_ud/(z_u0+z_u1), or zero. The complementary numerator is nonnegative and denominator positive on the active branch. Serialization includes full numerators/denominator. O(v^2) bitwork and O(v) data scratch suffice for fixed-count comparisons, additions, muxes and unreduced rational output; a conservative separately paid code allowance O(v^4) work/storage covers finite arithmetic templates. If all-token output syntax is used, pay O(Nv^2+v^4) extra work and O(Nv+v^4) stored code/output/work bits; other token outputs cannot be read by the terminal decoder. No integer square root, rho certificate, source table or real budget is needed.

At handoff disable all input/history/QKV/numerator/denominator/unexported output tapes. Release or zero dead arrays with full writes charged; endpoint acquisition and allowed copying are paid. Total work is the SUM of public generation/conversion, forward execution, handoff/cleanup and decoding; peak is the maximum across phases of the SUM of every simultaneously live description/data/code/output/scratch buffer, including encoder-decoder handoff overlap. Do not take minima from incompatible implementations. Abstract isolation is not a physical protection gadget supplied for free.

Optional Q-grid rounding of the final binary probability changes TV by <=1/Q and can be paid separately, with a corresponding upper-constant increase; the main theorem uses finite rational output. A PURE unrolling, if wanted, pays depth O(T_bit), width O(S_bit), gates/holds O(T_bit S_bit), dense slots O(T_bit S_bit^2), and actual index/coefficient/generation costs. No fixed neural-depth, training, computational advantage, or resource lower claim follows.

## 8. Dependency and status boundary

Read the full CB004, BP001, JP001, JB001, FA001 v3 and SM002 proofs and their acceptance receipts; read CB005 and its new root acceptance receipt. CB004 supplies the accepted all-start-valid deterministic-time inverse occupation and clean comparator; BP001 supplies only stationary bias. The twelve-port IID lower and real-threshold gate extension are proved here. BT002 supplies the full-history corruption lower by direct simulation, not an architecture-family precision inclusion. New source bindings and diagnostics accompany this candidate. Independent LLM review, if successful, is not formal verification, external peer review, or novelty certification. No publication is performed.
