编排说明（非原文）：本文件保留冻结版本的完整科学论证、结论、限制与实际审查问题；只去除非科学流程信息，并把来源位置改为本包逻辑入口。下文的源哈希与行号仍指冻结输入，不等同于编排后文件身份。精确复制、省略和编辑区间见 COPY_MAP.json；来源入口见 SOURCE_INDEX.json。独立审查为独立上下文的 LLM 数学审查，不是形式验证。R001、R002 的非阻断性澄清另见 EDITORIAL_NOTES.md，未改动原数学正文。

# R001 independent mathematical review v1

## Verdict and useful result

**ACCEPT** the theorem at R001 lines 38–52 for all integer K>=2, M>=1,
0<beta<1, arbitrary initial pair law (including off stationary support), and
its stated fixed-algorithm certificate-transfer interpretation.

No substantive mathematical defect was found. The mixed-prefix occupation
bound, the original-add-one certificate U_mix, and the fixed S024 ALG bound
with final factor 3 follow from the supplied proof and verified recovered
interfaces. This is an independent review of the newly written R001, not
acceptance by historical reputation, recovery of absent S026–S032 bytes,
a novelty assessment, or formal verification.

**One nonblocking editorial issue:** line 183 uses `i` without defining it
inside R001. Its intended inherited meaning is
`i=min(1,sqrt(K/(M+1)))`, explicitly defined in S024. Add this definition
if making R001 independently readable. This does not affect the interior
theorem, which does not use i, and the cited endpoint statement is correct
with the inherited definition. No submitted proof bytes were edited.

## Review procedure and exact source bindings

Review date: 2026-10-30 UTC. All 199 frozen candidate lines were read.
The review checks symbolic arguments and actual scientific dependencies, not
author diagnostics. No numerical simulation or historical acceptance statement
is a premise. Hashes identify frozen readable inputs; see SOURCE_INDEX.json
for current public locations and COPY_MAP.json for editorial copy identities.

| ID | Exact path | SHA-256 | Content inspected / used |
|---|---|---|---|
| R001 | `proofs/R001_mixed_prefix_and_blind_transfer.md` | `e27867bef5a59ce76fd3e343e781b31d04ed52938cb12a5a294343b1d4434ad1` | All 199 lines, reviewed submission |
| S020 | `S020 (SOURCE_INDEX.json)` | `a478d1219c97b479f0c96d0124a6d3fff023e18a4177361a758003db4b1de8eb` | Full readable proof; in particular Sections 3–7 and event-stack Lemma 2 |
| S024 | `S024 (SOURCE_INDEX.json)` | `c84c9307ff2e72fdcb1a842de6e3db210d174aaaaa4dc4eca4f6c00a8aa27405` | Full readable proof; algorithm, general guard, radius, and endpoint upper |
| L1MAX | `L1MAX (SOURCE_INDEX.json)` | `b430fe3d176ecefc00ac575670ea13ffc5d5799f9e232a10375333a0547f44e4` | Full readable proof; independent original stacks, maximal tail, arbitrary-start 48 bound |
| S001 | `S001 (SOURCE_INDEX.json)` | `7fa8b2119f84d9f382da80516aa8b3c277ebd2c4587dffd58d24bf16b11a77d4` | Full readable proof; stationary terminal occupation with K^2/(L+1) |
| S018 | `S018 (SOURCE_INDEX.json)` | `0bd13ecdc9d33df0cd56a5367885fa6779ce6fcabf16caf59ecbf9ed8e7b4d46` | Full readable proof; legal midpoint and complete-history pair splitting |
| GU | `GU (SOURCE_INDEX.json)` | `f4abb8e565d58c5af9f6f52ca1e83fc78989dfeb70554e4d22ad1fab8308d275` | Full readable file; arbitrary-start first-w charging supplying L1MAX UC |
| S022 | `S022 (SOURCE_INDEX.json)` | `028f43ae12886781bfd3641712c66720d24c667b59ca22a74c5dbbea5b0a5774` | Full readable proof; fixed-g IID selector and disjoint-triple/restoration interfaces used by S024 endpoint claim |
| S005 | `S005 (SOURCE_INDEX.json)` | `54071248416106afcc8f51734bc8ed019135ec2502e02d6e49fd09a45e6065e6` | Sections 1–3 (first 150 file lines): all-row beta=1/IID equivalence and pooled upper; lower/separation proofs not needed |

No claimed historical S026–S032 acceptance enters the dependency chain.
The main interior theorem uses no minimax lower interface. Neither S020's
historical comparison arguments nor S024's other regime claims are needed
to make R001's central inference.

## 1. Experiment, algorithm, and legal residual (R001 lines 8–76)

The full observation, M departure counts, actual terminal pair, half-L1 TV,
and arbitrary initialization match the recovered interfaces. The pooled
count denominator M+K and terminal-row add-one are the S024 definitions.
The guard selects pooling on ties, and triangle inequality proves
`ell_ALG<=ell_q+rho(J)` pathwise, without any independence assumption.
Since rho<=g, L1MAX proves the 49g general bound for this exact rule.

The unique legal two-step path gives
`P^2((a,b),(c,d))=theta_ab(c)theta_bc(d)`. Summing minorization over d
therefore gives theta_ab(c)>=beta p(c) for EVERY row. The residual T is
nonnegative, normalized, homogeneous, and a legal one-symbol table even
outside supp(pi). The equality of pi's coordinate marginals follows from
stationarity under the shift and makes p the second marginal as well.

Independent symbol labels with success output p have marginal emission
law beta p+delta T=theta on every departure, hence recover the entire
original history. Conditional only on no successes G, labels leave an
ordinary T trajectory with initial law mu. For every row,
`theta_s-T_s=beta(p-T_s)`, so TV(theta_s,T_s)<=beta. Apply the general
add-one theorem to the T-target experiment and then use this pointwise
target difference. The resulting conditional upper is at most
`min(1,48g+beta)`; multiplication by P(G)=delta^M yields A.
This is not a conditional original-theta concentration assertion.
The radius bound on G is independently delta^M g<=A.

## 2. Last success and first-w charging (lines 78–101)

For last symbol success at departure j, only that label and the following
M-1-j failures are constrained. All earlier labels are unrestricted; thus
the prefix has its ordinary P law, not a T or stationary prefix law.
The success emits a fresh p symbol independently of that prefix, so the
post-success pair has law nu_j tensor p. Conditional on that pair and this
label event, future emissions follow T independently of the earlier
prefix. This establishes the stated factorization for every j, including
j=0 and j=M-1.

The suffix begins at pair time j+1 and has l=M-1-j departures. Its counted
times are j+1,...,M-1, a literal subset of the original departure times
with identical endpoint Y_M. Hence full J dominates the suffix count;
this comparison does not assert monotonicity of empirical row error.

For fixed b and w, all f_l(b) are prefix marginal probabilities of one T
chain started at delta_b tensor p. On each path a given pair is flagged
only on its first w occurrences, counting l=0 as its first possible
occurrence. Summing over K^2 pair states proves (3). A finite path through
M-1 suffices; the stated infinite-path extension causes no problem and
provides no data to ALG. No recurrence, positive rows, or stationarity is
needed. The dependence of f_l on the fixed w is implicit and consistent.

## 3. Mixed-prefix improvement (lines 103–123)

Q=(P^2-beta Pi)/delta is a stochastic pair kernel, not a putative legal
one-symbol table. Stationarity gives pi Q=pi, and stochasticity gives
Q Pi=Pi; also Pi Q=Pi. Thus
`(P^2)^k=(1-delta^k)Pi+delta^k Q^k`.
Multiplication by the final P when j is odd preserves pi and proves the
formula at line 106, including k=0 and off-support mu. Taking the second
marginal yields a probability vector xi_j; it may depend on j and on the
source and initial law.

Let kbar=floor((M-1)/2). Since k<=kbar and 0<delta<1,
`delta^l(1-delta^k)<=1-delta^kbar`. Since
`l+k=floor((M-1+l)/2)>=kbar`, the other coefficient is at most qbar.
For nonnegative f_l, the stationary component therefore contributes at
most beta(1-qbar)K^2 w after summing b with p(b). For the other component,
xi_j(b)<=1 permits a sum over all K b's and contributes at most
beta qbar K^3 w. Their sum is exactly b_mix w.

There is no interchange of maximum and sum, no replacement of xi_j by a
fixed or independent law, and no assertion that p tensor p is stationary
for T. The extra factor K on the nonstationary component is honestly paid.
The floor inequalities also cover M=1, where qbar=1.

## 4. Joint labels, original stacks, and occupation interfaces (lines 125–152)

S020 uses anchor p0=M mod 2, leaving an initial ordinary departure when
needed and then r pair blocks ending exactly at M. Its first-success
suffix has length L_j=2(r-j), not M-2j for odd M. A block keeps the unique
midpoint (b,c) between (a,b) and (c,d). The mixture endpoint probability
is the full original two-emission product, including zero-probability
blocks. Conditional only on first-success event E_j, the successful
endpoint is pi and future unconstrained labels yield an ordinary P path.
No prefix or midpoint is additionally conditioned on. This justifies (6)
by S001 and literal suffix-count inclusion. The L_j=0 final atom is kept
and handled by the cap, not an invalid use of a positive-length theorem.

For each positive-probability full history h, let k_sym(.|h) and
k_pair(.|h) be the two finite conditional label kernels from their valid
constructions. The law
`P_original(h) k_sym(l_sym|h) k_pair(l_pair|h)`
has each required history-label marginal. Kernels at null histories can
be arbitrary. This conditional product need not make labels independent
unconditionally; nothing in R001 requires such independence.

Attaching that joint kernel after generating h from independent original
row stacks preserves their unconditional product marginal. S020 Lemma 2
can consequently be applied to E=E0 intersect Hplus, an event on the
finite augmented space, without conditioning concentration on labels.
Intersection only reduces both mass and count probability, yielding (5)
with q=q0 and c=b_mix/q0. All quantities are positive in the interior,
and q0<=1, including q0=1 when r=0.

S020 Lemma 2 then gives exactly
`min(q0,80 sqrt(q0 b_mix [K+log(1/q0)]))=B`.
For E_j use c=K^2/(L_j+1), giving exactly the corresponding term of S.
The covering is valid: E0 and all E_j partition the space; E0 is covered
by G and E. G may also meet E_j, but nonnegative losses permit this
overcount. Thus E ell_q<=A+B+S, and the independent L1MAX bound supplies
the minimum defining U_mix for the SAME original q.

## 5. Verification of the inherited event-loss bridge

S020 Section 5 supplies the exact event form used here, not a statement
conditioned on event H. I checked the proof against L1MAX:

- deterministic-prefix maxima use 2M independent symbols per row;
- the original path consumes at most M and the row identity is pathwise;
- the unconditional tail is
  P(Z_v>sqrt(8Kv)+sqrt(8v log K)+t)<=exp(-t^2/(4v));
- for an arbitrary event of probability at most z, tail integration uses
  min(z,exp(-t^2/(4v))), not a conditional tail;
- dyadic layers H intersect {v<=J<2v} have probability at most
  q min(1,2cv), using integer threshold 2v;
- the two deterministic series estimates 7 sqrt(A) and 12 sqrt(A)
  support the displayed empirical constant 66;
- zero counts and the smoothing term contribute at most 1 and 2 further
  multiples of q sqrt(c(K+log(1/q))), leaving slack below 80;
- the independent loss cap gives the minimum with q.

The arbitrary-start 48g theorem itself applies to every legal table, not
only tables in a positive-beta class. Its GU count bound follows from
first-w charging plus maximum-over-starts suffix domination with K^2
states and coefficient K^4/(M+1). The deterministic-prefix L1MAX proof,
its Holder summation, and smoothing give the stated constant below 48.
This closes the applicability of that theorem to residual T in Section 1.
S001's stationary coefficient K^2/(L+1) is separately justified by its
finite-window stationary charging proof, not obtained by falsely making
an arbitrary start stationary.

## 6. Event radius and final factor (lines 154–181)

For 0<t<g<=1, x=4096K/t^2-K is positive. Because J is integer,
`J<x` is exactly `J<ceil(x)`, including when x itself is integer.
Moreover ceil(x)<=x+1<=4096K/t^2. The strict event rho(J)>t is therefore
precisely the event used in (7); the atom at rho=g does not disturb layer
cake over (0,g).

Integrating min(q,4096bK/t^2) gives at most qg and at most
128 sqrt(qbK). The split point z=64 sqrt(bK/q) and both cases in R001
are correct. If b=0, using w=M+1 indeed forces P(F)=0, since J<=M.
For 0<q<=1 the comparison with
D(q,b)=min(q,80 sqrt(qb[K+log(1/q)])) is valid in both branches:
when D=q the radius cap suffices; otherwise 128/80=8/5 and
K<=K+log(1/q) suffice. No assumption of equality P(F)=q is needed.

For E and E_j the D values are respectively B and the summands of S.
The same nonnegative cover plus the G radius bound yields
E rho<=A+(8/5)(B+S). Adding original-rule risk and using pathwise guard
safety gives 2A+(13/5)(B+S). The coefficients 2 and 13/5 are each <=3.
Independently, if u_g=1 the loss cap controls risk by 3u_g; if u_g<1,
u_g=48g and 49g=(49/48)u_g<=3u_g. Therefore the displayed minimum of
risk bounds is at most both 3(A+B+S) and 3u_g, proving the actual chained
inequality in line 49, not merely a looser consequence for the risk.
All quantities belong to the same fixed ALG and source experiment.

M=1 has r=0, E0 the whole space, no E_j, q0=qbar=1, and G plus Hplus
already covers everything. All logarithms and denominators used in the
interior theorem remain defined. Zero counts, sparse pi, both horizon
parities, and off-support starts introduce no omitted cases.

## 7. Dependency wording, endpoints, and scope (lines 27–36, 182–199)

The R001 dependency descriptions correspond to actual recovered text.
S020 Sections 3–7 do contain the named charging, aligned splitting,
event-loss lemma, and success-sum bounds. The moderate-log simplification
is available but is NOT silently assumed for the all-parameter theorem;
R001 retains the exact logarithmic S expression. S024 Sections 1,4,5 give
the exact ALG, general guard guarantee, and count-radius technique.
No missing historical unit is required to prove the displayed results.

Beta=0 and beta=1 are not substituted into residual divisions or the
interior formula. The separate general bound is valid at beta=0.
At beta=1, summing the all-row minorization and using normalization
forces theta_ab=p for all rows, including off-support rows. The IID
output law with arbitrary initial pair then supports the recovered S024
858i claim. I checked the S024 endpoint route through S022's disjoint
triples, pathwise restoration, and fixed-g selector; S005 supplies the
all-row IID equivalence and pooled upper. The notation i omission is
recorded above; it is the only requested editorial correction.

At M=K^5, beta=log(K)/K^5 as K grows, q0 and qbar are asymptotic to
K^(-1/2); b_mix is asymptotic to (log K)K^(-5/2), and
K+log(1/q0) is asymptotic to K. Consequently the uncapped B branch is
asymptotic to 80 sqrt(log K)/K and eventually lies below q0. This confirms
that the stated upper certificate contains such a term. It supplies no
statistical lower bound and does not settle whether a better argument
can remove that term. R001 correctly avoids either inference.

The result transfers THIS explicit original-rule certificate to a single
beta-blind algorithm. It does not prove that U_mix equals minimax risk,
that all beta regimes are matched, or that the missing historical proofs
were correct. The final prospective paragraph makes no new theorem claim.

## Final disposition

**ACCEPT, with the nonblocking local-definition nit for i at line 183.**
No mathematical revision is required for the stated interior theorem.
No unresolved scientific dependency for that theorem remains. Proof bytes were left unchanged.
