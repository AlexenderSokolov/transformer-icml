# C1–C4 integrated theorem, composition proof and scientific synthesis v2

Lead, 2026-10-25. This version incorporates the actual native C1, C2 and C3
admissions, with no change to their admitted proof files. It replaces the
historical status of checkpoint v1 for this new synthesis only. C4 and the
stage root remain OPEN, acceptance=null. This composition is a fixed
review candidate, not a new native Fact or a completed final audit.
The precursor checkpoint v1 and every failed proof/review/queue are retained.

Root: d0bdd1d8bf611bb7a6e9c4bb14d8b14e5a71ae8cc5c97776fc079ac13c63b428.
Contract: d9e5e1f1efba187dfce2e80b395a1db533e89e8a97bd11c6f2f1e51d1ee9bb3e.

## 1. One experiment, one predictor family

In current D1, w=(1-u)/3, r=ut/w, 0<u<1/4, 1/4<=t<=3/4.
The stationary pair masses in order00,01,10,11 are (u,w,w,w), and next1
probabilities are (t,1/2,1-r,1/2). Observe X_1 through X_N, N>=3.
The target is the next symbol given actual S_N=(X_(N-1),X_N), from the
same observed history. Unknown u,t and pi are not algorithm inputs.
Natural-log risk R_N averages over this actual query; R_N,00 conditions
on S_N=00. Comparators may use the full history and independent seeds.

The common unquantized function uses uniform output for N<6 or rows01/11.
Otherwise m=floor(N/2), M=m-2, and only triples ending3..m estimate the
row selected by S_N. Write its selected counts C0,C1 and d=C0+C1+2.
Row00 estimates next1 by clip_[1/4,3/4]((C1+1)/d); row10 estimates
next0 by min(3/4,(C0+1)/d). No fixed positive lower clip is used on row10.

For Q=2^b, b>=1, one integer branch program implements the quantized
version. N<6, Q=2 and rows01/11 emit uniform. At row00 and Q>=4,
z1=min(3d,max(d,4(C1+1))), Z=4d and

    J=(2Qz1+Z) div (2Z),     output=(Q-J,J)/Q.

At row10, z0=min(3d,4(C0+1)), z1=4d-z0, Z=4d;
k_c=((Q-1)z_c+Z-1) div Z, residual e=Q-k0-k1 goes to coordinate1.
Thus output=(k0,k1+e)/Q. All emitted coordinates are positive and sum
exactly to one. Half ties round upward on row00; row10 uses the specified
canonical residual. Neither program selects parameters using the assessed
risk or unknown u. Q4, endpoints and zero counts are explicit proof cases.

## 2. Integrated finite inequalities and quantifiers

The admitted C1 Fact e418ec34b7dbc4a6 proves for that unquantized function

    R_N <=1000000/N,
    R_N,00 <=160000/(1+Nu),
    M_N >=3/[16384(N+6)],
    C_N(u) >=3/[16384(1+(N-2)u)].

C_N(u)'s lower comparison may even reveal u; the attaining function
does not know it. Every N>=3 is covered. The actual-terminal bridge is
for the whole prefix distribution, obtained from the stationary reverse
experiment and uniform minorization. It has no division by u. Predictable
martingales, spaced visits and deterministic row-stack lengths replace
the false conditional-binomial shortcut. Full-history testing includes
the reverse-path boundary drift. Ordinary pair detailed balance is false.

Native C2 Fact 4f0e99ed26dfeeeb proves that the same common
quantized program satisfies, for all N,Q,u,t,

    R_N <=6000000/N+3/Q,
    R_N,00 <=1000000/(1+Nu)+3/Q^2.

Writing delta_Q=-log(1-1/Q), its minimax lower inequalities are

    M_N,Q >=max{3/[16384(N+6)], delta_Q/3},
    C_N,Q(u) >=max{3/[16384(1+(N-2)u)], 1/(2Q^2)}.

The average lower uses a statistical testing witness and, separately,
t=1/2,u decreasing to0 for the representation witness. The latter is a
supremum over admissible positive u, not an attained law with u=0.
For each fixed u the conditional format witness is t=1/4+1/(2Q) when
Q>=4, or t=1/4 when Q=2. It forces loss >=1/(2Q^2) for each history
and seed. These are minimax floors, not floors at every fixed t. The
statistical and format witnesses are combined by max; converting max
to a constant-factor sum does not make them additive on one source.

The admitted statistical/format inequalities give average Theta(1/N+1/Q), and for every
fixed u conditional Theta(1/(1+Nu)+1/Q^2), with constants uniform in u.
The key row00 bridge is pointwise:

    kl(t,q1) <=(16/3)kl(t,a)+8/(3Q^2).

It uses Pinsker in the direction (t-a)^2<=kl(t,a)/2, followed by the
interior quadratic KL upper bound. No mixing-TV error is squared.
Row10 uses coordinate domination q_c>=(1-1/Q)a_c. These arguments
apply before taking actual-terminal conditional expectations.

The first-order subcurve is t=(1-u)/(1+2u)>1/2; upper bounds include
it, and all specified lower witnesses avoid it. At each fixed positive u,
expected conditional KL tends to zero as N,Q increase. The triangular
sequence u_N=1/(N+1) is a different quantifier. In particular, already
from admitted C1, inf_q sup_(u,t) R_N,00 >=3/16384 at every finite N:
for each q first take sup_t at each u, then let u decrease to0, and only
then take inf_q. No interchange of inf/sup or fixed-law inconsistency
is being asserted. The same obstruction holds with unrestricted outputs.

## 2a. Composition proof and explicit common order constants

Let A_N be the unquantized function in section1, G_(N,Q) its integer
branch function, and H_(N,Q) the decoded C3 guarded-output implementation.
These names denote functions of a finite binary history, not new source
processes. C1 proves the risk claims for A_N. C2 uses exactly A_N's row
estimates and proves the grid claims for G_(N,Q), with native predecessor
C1. C3 is a deterministic construction, independently valid for every
binary history, with no statistical predecessor or source parameters.

For N>=6, C3's actual-query adapter binds S_N and E_m separately, recovers
the two exact selected triple counts on3..m, and evaluates exactly the
same integer normalization and readout as G_(N,Q). The N<6 branch is
uniform on both sides. For every Q, the Q2,01,11 branches agree;
for row00 the identical integer quotient enforces half-up ties, and for
row10 the identical ceiling/residual rule uses canonical(next0,next1).
Thus H_(N,Q)(x)=G_(N,Q)(x) for EVERY history x, as decoded vectors.
This is the pathwise premise needed to transfer the risk, including at
histories whose probability depends on u,t. It does not require an
independent terminal query or conditioning counts to be binomial.

In particular, for any D1 law, the losses are equal pointwise before
expectation. On {S_N=00} they are still equal; this event has probability
u>0, so their conditional expectations are equal as well. No extra mixing
error, factor1/u or floating-point tolerance is introduced by this
composition. The single finite H_(N,Q), with its paid C3 interface, attains
both C2 upper bounds for all N,Q,u,t. The eight-counter baseline has the
same decoded risks and identical words within the SAME C3 output port.

C2's compact b-bit next1 port, its2b two-numerator port and its3b+1
literal-denominator port differ from C3's guarded3(b+1) literal-Q port
(or2(b+1) when Q is omitted). Each encodes the same strictly positive
Q-grid vector and has paid writes/storage. No claim equates their raw
strings or lengths. Consequently the output-format minimax comparison
applies to the decoded C3 predictor without changing the source or target;
C2's small local converter cost cannot replace C3's whole-history ledger.

Explicit constant-factor order comparisons follow without choosing a
common lower witness. For N>=3, N+6<=3N, and delta_Q>=1/Q. Hence

    (1/32768)(1/N+1/Q)
      <= M_(N,Q) <= 6000000/N+3/Q.

Indeed the admitted lower bound is at least
max{1/(16384N),1/(3Q)}, which is at least
1/(32768N)+1/(6Q). This max-to-sum operation is on the supremum risks;
it does not add two losses on a single source. At every fixed u,
1+(N-2)u<=1+Nu, so likewise

    (3/32768)(1/(1+Nu)+1/Q^2)
      <= C_(N,Q)(u) <= 1000000/(1+Nu)+3/Q^2.

The stronger separate max inequalities in section2 remain available,
including the known-u full-history randomized lower comparator. The same
unknown-u family H supplies both upper bounds. Unquantized C1 also gives
1/(16384N)<=M_N<=1000000/N and
3/[16384(1+Nu)]<=C_N(u)<=160000/(1+Nu).
These are uniform order bounds with explicit nonoptimal constants, not
exact minimax values, sharp feasibility thresholds or architecture lower
bounds. The lower comparator class is unrestricted full observed history
subject only to its stated output format, not a class with C3's resource
budget. Internal Q_A and b remain independent design quantities.

## 3. Output port, actual causal implementation and resources

C2 v2 adds the previously missing local cost statement. A fixed public
b-bit next1 numerator port determines the full binary vector; optional
two-numerator and explicit-denominator ports emit 2b and 3b+1 bits.
Complement reconstruction, writes and addresses are charged. With
K=b+ceil(log2(N+1))+6, the local converter has sufficient sequential
cost 3000000K^3 bit operations and 256K live bits. These admitted local
bounds cover the converter; the full history-processing cost is separate.

Native C3 Fact a47d648004a9a607 derives these inputs from actual finite heads.
Physical query position is N+1. Four paid singleton heads first bind
local lags, E_m and S_N; only then is the prefix/query buffer routed.
Four statistical heads use keys3..m: two itemwise product-match heads,
a partial-match head and a uniform head. Their19 coordinates recover
the desired frequencies by a flow identity with E_m at its boundary.
S_N selects the row; substituting it for E_m is invalid.

The finite coefficient/log/exp evaluator, signed recovery and count snap
are part of the computation, not exact real oracles. With

    h=max(4,ceil(log2(256(N-2)))), Q_A=2^h,
    p=4h+4ceil(log2(m+4))+64,
    ell_C3=ceil(log2(N+2)), v=b+ell_C3+8,
    B=128p, O=32v,

the admitted deterministic construction proves master error <=2/Q_A and recovered frequency error
<=76/Q_A, which is strictly below half a count. Q_A and p do not depend
on output Q. Closed masters require h+1 numerator bits; log3 requires
p+1 numerator bits. The local count converter and the C3 guarded-word
interface encode the same positive simplex output, with any padding,
second coordinate or denominator explicitly paid.

The exact complete sufficient cost functions are the fixed C3 appendix
A1–A21 and its machine-readable certificate, not hidden Big-O constants.
It supplies 63 recovery and41 readout word instructions, each expanded
using g(w)=1024w^2 elementary steps; the principal hybrid resource tuple
has two attention layers, eight total heads, maximum four simultaneous
heads, QK dimension<=4 and finite scores in[0,2]. Its recovery/readout
depth and per-token/query width have orders O(p^2+v^2) and O(p+v), with
the extremely large explicit constants in that appendix.

These orders alone are not a complete resource report. The fixed package retains the full stored parameters, masks, positions, routing, holds,
offline generation, online operations, working and peak memory formulas.
The hybrid evaluator's internal arithmetic is paid separately; the
flattened circuit expands it into depth. Sparse neural identities and
shared register-memory operations are different cost columns. Tokenwise
width is not global array width. Global dense and padded batch bounds
pay all input banks and dense zeros. The certificate is an explicit
constructive upper bound, not a benchmark or a materialized huge matrix.

The charged eight-counter baseline consumes all N symbols, updates
triples only through m, retains actual S_N and uses the same integer
readout. Exact counts on both sides imply identical output words for
every path. Sequential input width and one-shot full-history width are
distinct: the latter retains an additional2N+2ell_C3 input/index bank
through the count circuit. No optimized architecture dominance follows
from this output identity or from a loose sufficient cost certificate.

## 4. Primary comparison and retained failures

The pinned map counter/sources/primary-map-v1.md records exact PDF hashes,
versions and locations. There is no additional retrieval in this checkpoint.

| Primary | Assumptions, estimator and risk | Relation to this stage |
|---|---|---|
| Han–Jana–Wu,2106.13947v2, Thm3/Cor4 pp4–5, Thm22/24 pp39–40 | Full-history add-one parametric results have ordinary reversible first-order gap assumptions; the full stationary binary second-order class has logN/N minimax risk. | D1 is a specific subclass and its pair chain is not ordinarily reversible. Neither theorem supplies the present same-family statistical result, conditional00 quantifiers or charged grid program. |
| Paulin,1212.2015v5, Props3.15/3.16 p18 and surrounding concentration assumptions | Path-event comparison with an additive TV term; uniform ergodicity controls decay. Other point-start L2 bounds carry a1/pi(s) factor. | Standard tool neighbors for the reverse whole-prefix bridge; no direct unknown-source predictor, conditional KL classification or output/bit-cost theorem. |
| Geiger–Boecherer, Entropy18(7):262,2016, Alg1/Prop1 pp2–3, Lem1 p4, Prop2 p5, eq10 p6 | Given a target, greedy M-type approximation minimizes the same-direction KL, with support and stationary weighted known-kernel approximation statements. | Direct probability-quantization prior. It does not establish this unknown-law sample-size/terminal-conditioned experiment or the finite causal implementation. Our nearest converter need not be targetwise KL optimal. |

These comparisons are specific nonimplications under pinned assumptions,
not a proof of publication novelty or a complete literature search.
Nearest-grid rounding is not exact KL minimization: at t=37/100,Q=4,
the loss at1/4 exceeds that at1/2 since2^100>3^63. Source extraction
ambiguities are not promoted to established errata or usable premises.

Other retained failures are: conditional-binomial counting at random
visits; ordinary pair detailed balance; replacing E_m with S_N; omitting
the closed endpoint bit; a nonstrict half-count snap radius; uncharged
re-storage; using nominal count sum bounds for arbitrary closed masters;
and the old8mQ nearest dividend guard. Fixed lower clipping of row10,
swapped alphabet coordinates and moving a zero-output statement from
average risk to another terminal conditional risk also fail in the
recorded examples. None licenses silently revising the contract.

The actual C2 v1 failure for missing local output costs remains recorded
as b97ba0738f1848747bd400c3e74405482a403fe463232e79f62fa7068938d708.
It demonstrates that the earlier discussion reviews did not discharge
every contract item. V2 retained the rates and supplied the missing finite
port/arithmetic statement; its later native admission closes C2 without
deleting or relabeling that real failure.

## 5. Ordinary-Chinese synthesis and mother-problem boundary

00虽然少见，但在00已经发生的条件下，两种后继概率都与0、1保持固定距离。
估计和舍入的小误差在这里产生平方量级的KL损失，所以其输出精度项是1/Q²。
10却很常见，其中一种后继概率可以任意接近0。正网格至少要给它1/Q的概率，
从另一项拿走的质量造成一阶损失；10的出现质量又趋近1/3，因此平均风险仍有
1/Q项。一个按实际情境分支的未知参数算法可以同时达到这两种不同的风险界。

增加输出位数可以减少舍入损失，不能补出没观察到的稀有情境证据。固定正u时，
更长的历史最终能积累证据；若要求有限历史同时覆盖任意小的u，总有证据不足
的来源。这不是一个固定世界的预测必然失败，也不是内部位数或层数的下界。

Evidence-bounded contribution: mechanism/risk classification and finite
implementation integration on D1; publication novelty remains unproved.
T1 obtains an explicit actual-terminal expected-KL result on this family;
T2 links history and output precision with sufficient full cost functions.
T3's perturbation-entry models, cumulative reliability, mechanism-related
necessary resources and robust same-budget structural improvements remain
mother-problem questions. Broader process families, learning the construction,
unknown order and hidden-state extensions also remain open. No parked
candidate or old accepted root is reopened by listing them.

## 6. Exact evidence dependencies and remaining stage gates

The following actual receipts and full scope readbacks were checked by
Lead against the current native research state. Evidence level is
LLM_CHECKED_PROOF; it is not formal verification.

| Unit | Fact ID | Evidence ID | Native predecessors |
|---|---|---|---|
| C1 | e418ec34b7dbc4a6 | 4857f1b1b5d10ab74a979362e3d0c3068c9634016e4ce6b6a0609ed577eb2eea | [] |
| C2 v2 | 4f0e99ed26dfeeeb | a4152a1fc70cbd2d4ece0bea8390fb68c0ed76beb4e11a8d9dd495a8250764ee | [e418ec34b7dbc4a6] |
| C3 v1 | a47d648004a9a607 | 3e576827ab335e24f661561d9aa89f035a36925f450dd2daf0be3b166ab3cd27 | [] |

C2/C3 request text equals the complete fixed proof files, including C3's
A–K appendix. Native Fact content includes a scope/dependency wrapper,
so its content hash differs from the submitted proof-file hash. Both are
retained, not interchanged. The raw receipts' auxiliary undefined-symbol
lists have been retained as returned; native accepted=true, PASS and
DISCHARGED establish acceptance, not a synthetic glossary repair.

The fixed review verifier/c2-cost-and-c3-review-v1.md independently checks
C2's genuine local-cost repair and the complete nominal C3 construction;
its report hash is ab5f63f81d689e85695e610b49e7ea115a7c270f7c317c62867b3c14345687ef.
Earlier C1/statistical discussion and Counter reports are pinned sources
of review, not substitute Fact IDs. No old-project Fact was imported.

C4 still requires review of this exact composition/synthesis package,
followed by native admission with the actual three predecessors above.
The existing C4 obstacle0def94abb5dd20e9fc11024c4f656ce7f0d77ef78740e17ef61155836d95a99d
is addressed by the complete code/cost package and pinned primary map,
but its required full-package review and admission have not yet occurred.
It is preserved as a historical diagnostic. Root remains OPEN and must
receive a conjunction proof and then a SEPARATE native final_audit using
the explicit reserved resource vector. This document neither asserts a
future review verdict nor claims that audit has already happened.

Old Counter C4 task [redacted routing identifier] never started;
[Non-scientific operational metadata omitted.] All eight historical
[Non-scientific operational metadata omitted.]
source authors/hashes and parked research candidates remain unchanged.
Neither controller counters nor graph closure states were manually reset.

[Non-scientific operational metadata omitted.]
sections1–5 give the scientific result, mechanism and limitations; this
section gives native IDs and pending gates. After actual stage acceptance,
the handoff must additionally report the real root Fact/Evidence and audit
acceptance, without editing accepted roots or closing mother-problem
monitoring. Current status is C1–C3 admitted, C4/root pending. The remaining
T1/T2/T3 questions in section5 continue regardless of stage SOLVED.
