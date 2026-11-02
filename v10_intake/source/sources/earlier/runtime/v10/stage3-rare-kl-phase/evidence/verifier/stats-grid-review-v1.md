# Independent fixed-version C1/C2 review v1

Verifier, 2026-10-25. This is a discussion review of the exact bytes below,
under the current project's PROBLEM.md D1–D7. It is not a native admission.

**C1 verdict: PASS, mathematical review only.** No load-bearing gap or
mandatory mathematical repair found for obligation
`1dd6b3b9191952ba424db347dab176cd3336d5399831f867f595a13a40e5ce25`.

**C2 verdict: CONDITIONAL PASS, conditional on the stated C1 theorem.**
No additional mathematical repair found for obligation
`8b179af3ef2fe36eca7503ff37e9baca6ba118d546cf884db6ad7e4da0d0b6f8`.
The conditional quantization proof and all format lower bounds are valid.
Native C2 submission must await C1 admission and use its returned Fact ID.

**C3, C4 and stage root: not certified.** In particular this review does
not certify the implementation checkpoint, count recovery, physical query
adapter, full resource ledger, baseline cost certificate or stage completion.

## 1. Fixed inputs and evidence boundary

Paths below are relative to the project root. SHA256 hashes were checked
before and after the independent diagnostics. No pinned input was edited.

| Input | SHA256 |
|---|---|
| PROBLEM.md | `efc51898a4a702040f9048e2f53121ec59020586b12221fd57e1015940ec5751` |
| outputs/001-conditional-grid/prover/c1-proof-v1.md | `5884ffc213a0aaa950b48f881abd4519440800737485b5c3aae9d293c38fb38d` |
| outputs/001-conditional-grid/prover/c2-proof-v1.md | `a008ec575571973d7df08ece2468c901744a6c3680df08b15a008c38ff1d7105` |
| outputs/001-conditional-grid/counter/adversarial-review-v1.md | `b9273b1e96d5fd16d5eaaa5ed8ce75e8385cd57d6ec9dbe2589582a54f86ad64` |
| outputs/001-conditional-grid/lead/stats-grid-review-v1.md | `b682098e988151e907df8c508c901742f2d3ee18569b8c376ca32cd904083592` |
[Non-scientific operational metadata omitted.]

The Counter script was inspected only at its diagnostic/endpoint references,
not used or imported as a correctness oracle:
`counter/check_adversarial_v1.py` SHA256
`06c15bf5a46002fe7d866345de9b5f3a0205160fddd3232033715c21bfad0092`
(under the same output directory). No old source009 proof or verdict was
used as a premise. No literature retrieval or primary-source novelty audit
was performed in this bounded C1/C2 review.

Euler research_state was read at start and before report completion. The
second readback is recorded in native-state-v1.json: all five obligations
are OPEN with empty evidence_refs; evidence and all_evidence are empty;
acceptance is null. Read-only team members/messages confirmed the current
assignment and the Lead/Prover/Counter roles. No scheduling call was made.
The main proof + fixed Counter report + Lead review gate is satisfied by
these inspected bytes; their verdicts were not inherited.

## 2. C1: experiment, stationarity and actual-terminal bridge

The reviewed theorem concerns exactly the D1 family, with canonical
coordinates (next0,next1), pi=(u,w,w,w), w=(1-u)/3 and r=ut/w. It uses
the actual S_N from the observed history, not an independent query.
The algorithm knows neither u nor t. It estimates using triples at 3..m
only, m=floor(N/2), then selects the row using S_N. The discarded suffix
contributes no estimation samples.

Direct multiplication gives pi P=pi. Together with shift-compatible pair
transitions this initializes a stationary symbolic process. Every finite
binary history has positive probability. With alpha=3u/(1-u),
0<alpha<1 and 3u/4<=r<3/4, the proposed paths establish
P²(x,10)>=1/8, P³(x,00)>=3u/32 and P³(x,01)>=1/32.
The reverse kernel computed from pi_j P(j,i)/pi_i is exactly the displayed
R=σPσ, where σ exchanges01 and10. Thus R³(x,10)>=1/32 and

    TV(R^g(s,.),pi) <= (31/32)^floor(g/3) = d_g.

This is a valid uniform minorization argument; it does not assert ordinary
pair-chain reversibility. The edge00->01 and absent reverse edge01->00
already disprove ordinary detailed balance.

The telescoping forward/reverse path identity proves the entire conditional
backward experiment, not just a terminal marginal. Given actual S_N=s,
S_m has law R^g(s,.). Conditional on S_m, the earlier reverse path has the
same kernel as in a stationary prefix. That path determines all of X_1^m.
Data processing therefore bounds TV of the **entire prefix** by d_g, with
no division by pi_s. Counts and prefix endpoint retain their dependence.

The row losses have valid deterministic caps: log4 for00,
log max(M+2,4) for10, and zero for01/11. The TV comparison is applied to
these unquantized losses. It yields C1.14 before output precision enters;
there is no independence assumption or hidden log Q factor.

## 3. C1: dependent counts, constants and all upper-bound branches

Each increment of Z=C-pD is predictable-row times centered successor.
Conditioning on the information before that successor makes it mean zero;
cross terms vanish at the deterministic horizon. Hence
E Z²=p(1-p)ED and ED=M pi_s. This is not a conditional-binomial claim.

For spaced visits the conditional success probability is at least p.
Iterating its conditional MGF gives the stated exp(-Bp/8) tail without
independence. B=floor((M-1)/3)>=M/6 for M>=6 gives the row00 tail
exp(-Mu/512) below Mu/128. For row10, M>=64 gives
d=floor(floor((M-1)/2)/16), with d>=M/128 and d>=1, and the
exp(-M/256) visit tail.
Both thresholds are proof devices, never algorithm inputs.

The independent row-stack construction reproduces the path law by revealing
only used bits. Its needed inclusion is pathwise:
{D>=d,C<pd/2} is contained in {B_s(d)<pd/2}. The latter uses a
deterministic number of iid stack bits and has probability <=exp(-pd/8).
No distribution for C conditional on random D is asserted, and the stack
does not provide extra data to the estimator.

| Upper-bound step | Independent check |
|---|---|
| Row00 projection and martingale variance | C1.20 follows from q(1-q)>=3/16, projection and (A+B)²<=2A²+2B². |
| Row00 good event | Multiplication by 1+x, x=Mu, gives 49152(x+1)(x+4)/(x+256)²<=49152. |
| Row00 complement | (1+x)e^(-x/512)<257 and log4<3/2 give <386. Thus K00<=50000/(1+Mu). |
| Row10 clipping | When clipping occurs, v>3/4>p; (p-v)²/v is increasing there. This gives C1.22. |
| Row10 G event | 16M/d²+8/d<=263168/M, retaining the p in E Z²<=pM. |
| Row10 H event | Its loss is bounded by [y log_+(256y)+2y+4]/d, y=pd. Multiplying the stack tail gives <=108/d<=13824/M. The rare p log term is retained. |
| Row10 J event | A genuine KL cap times the visit tail gives <=65536/M. |
| Row10 total | 263168+13824+65536=342528; M>=64 gives <=400000/(M+1). |

For 1<=M<6 the row00 cap proves its claimed bound directly. For
1<=M<64 the row10 cap <=log65<5 proves its bound directly. D=0 gives
uniform prediction in either row. No exceptional zero-count path is lost.

For N>=6, M+1>=N/4 and u/(1+Mu)<=1/(M+1). The weighted two-row
contribution is <800000/N. The reverse remainder satisfies
d_g<=2e^(-N/192) and is <=73728/N, proving R_N<=1000000/N.
Also N<=2M+5 and u<1/4 give 1+Nu<=3(1+Mu). The scaled conditional
row contribution is <=150000; its scaled mixing remainder is <75.
Thus R_N,00<=160000/(1+Nu). The displayed maximum
144 exp(-47/48) used for that remainder is correct. For N=3,4,5 the
algorithm is explicitly uniform and binary KL<=log2 proves both bounds;
no M<=0 count lemma is invoked.

## 4. C1: full-history lower bounds and quantifiers

The full history conditional on S_N=00 is in bijection with an R-chain
Y_0..Y_n, n=N-2, started at00. Its occupation drift is exactly

    t U00 = 1-Pr(Y_n=00)+alpha*t U01.

The boundary term is essential and is retained. Consequently
U00<=1/t+alpha*n. For t0,t1 in [5/16,7/16], Delta=t1-t0,
the transition KL bounds 5Delta² and 5alpha Delta² imply

    KL(P_t0^00 || P_t1^00) <= 40(1+nu)Delta².

There is no stationary-initial KL term in this conditional experiment:
the reverse initial state is the same fixed00. All n reverse transitions
are included. Taking Delta=1/(32sqrt(1+nu)), centered at3/8, gives
TV<=sqrt5/16<1/4. Thresholding the comparator's next1 coordinate at3/8
and using Bernoulli Pinsker on errors yields

    max_i R_N,00(u,t_i;q) >= 3/[16384(1+(N-2)u)].

The testing argument covers every full-history output and any common
source-independent conditional randomization kernel. The test's acceptance
probability is a [0,1]-valued function of history, so randomization does
not reduce the lower bound. Known u is shared in both experiments and
does not invalidate it. Zero outputs only make relevant losses infinite.

Only after this conditional test is complete is the common terminal mass
u applied. This gives the average lower 3u/[16384(1+(N-2)u)]. Choosing
u=1/8 gives M_N>=3/[16384(N+6)]. These arguments apply for every N>=3.

The first-order condition is t=1-alpha*t, hence
t=(1-u)/(1+2u); it lies in the domain exactly when u>=1/10 and is
always >1/2. Upper bounds include it; all statistical testing witnesses
have t<1/2 and avoid it. At every fixed positive u, expected conditional
KL tends to zero. With u_N=1/(N+1), N>=4, and t chosen at each N from
{11/32,13/32}, the test gives a conditional lower >=1/2048. This is a
triangular obstruction to uniform consistency, not a fixed-law or
almost-sure inconsistency assertion. No single fixed t is claimed to
maximize every finite-N risk.

## 5. C2: one integer program and the pointwise rounding bridge

The z0,z1 formulas recover exactly the two C1 rational branches. The
row00 numerator J is the next1 numerator, so the actual output is
(Q-J,J)/Q. Integer division of 2Qz1+Z by2Z gives nearest rounding with
half-up ties. For dyadic Q>=4, Q/4<=J<=3Q/4; the closed clipped
endpoints are fixed and |J/Q-a|<=1/(2Q). Q=4 has exactly the stated
three intervals, with3/8 and5/8 assigned upwards.

For row10, ceil((Q-1)z_c/Z) sums to Q-1 or Q. The residual is0 or1,
always assigned to canonical coordinate1. Both numerators are in1..Q-1,
sum exactly to Q and satisfy q_c>=(1-1/Q)a_c. D=0 gives z0=z1=4,
and both converters return uniform. Single-successor zero counts,
clipping, endpoints and Q=4 cause no undefined operation. Euclidean
integer division is a finite algorithm, not a real floor oracle.

The program handles Q=2, N=3,4,5 and rows01/11 by the specified uniform
branches. Q=2 is the unique positive-grid output. Its conditional00
loss is <=1/4<3/Q², and its average loss is <=log2<3/Q.
Small N is covered by the statistical constants. Every output coordinate
is >=1/Q and the simplex identity is exact; therefore KL<=log Q too.
Full physical count recovery and resource costs are still C3 obligations.

For every individual history on row00, t,a,q1 belong to [1/4,3/4]. Thus

    kl(t,q1) <= (16/3)(t-q1)²
             <= (16/3)kl(t,a)+8/(3Q²).

Pinsker is used in the correct direction to bound (t-a)² by kl(t,a)/2.
This inequality precedes conditioning on actual S_N=00; it neither
squares a TV bound nor changes the joint experiment. Applying C1 gives
(2560000/3)/(1+Nu)+8/(3Q²), below the advertised conditional upper.

Row10's coordinate domination gives the pointwise KL increment
delta_Q=-log(1-1/Q)<=2/Q. Weighting by the actual stationary masses
u,w, then using nonnegative C1 row losses, gives

    R_N(q) <= (16/3) R_N(a)+delta_Q+2/(3Q²)
           <=6000000/N+3/Q.

The same parameter-independent program attains this bound and
R_N,00<=1000000/(1+Nu)+3/Q² simultaneously. No choice between
algorithms depending on the assessed risk or unknown parameters occurs.

## 6. C2: representation witnesses, randomization and max lower bounds

For each fixed u and Q>=4, t_Q=1/4+1/(2Q) is a legitimate D1 target
halfway between grid values. Every grid next1 coordinate, on every
history and almost every seed, is at distance >=1/(2Q). For Q=2,
t_Q=1/4 has the same distance from1/2. Pinsker yields >=1/(2Q²)
pointwise. Since Pr(S_N=00)=u>0, the conditional lower follows even
when u is known. These witnesses have t<=3/8 and avoid the first-order
curve. The claim is a sup_t minimax floor, not a floor at every t.

For the average format witness take t=1/2 and positive u decreasing to0.
On terminal10, q1<=1-1/Q, so

    KL((r,1-r)||q) >= (1-r)delta_Q-h2(r).

Multiplication by terminal mass w and a supremum over allowed positive u
give delta_Q/3. The explicit lower expression is independent of the
predictor and seed, so no predictor-dependent limit is exchanged with an
expectation. u=0 is not asserted to be an admissible or attaining law.
For every allowed u this witness also avoids the first-order curve.

Grid predictors form a subclass of the C1 comparators. Combining the
statistical and format bounds gives precisely

    M_N,Q >= max{3/[16384(N+6)], delta_Q/3},
    C_N,Q(u) >= max{3/[16384(1+(N-2)u)], 1/(2Q²)}.

These use different witnesses. The max-to-sum consequences with constants
1/32768 and3/32768 are correct; they are not an additive lower bound on
one source. The average order1/N+1/Q and conditional order
1/(1+Nu)+1/Q² follow with uniform numerical constants. Randomizing grid
outputs cannot bypass the per-seed format inequalities. Averaging outputs
would itself have to satisfy the prescribed output grid.

## 7. Counter's additional counterexamples and their scope

| Counterexample | Independent assessment |
|---|---|
| Random D does not give a binomial C conditional on D | Exact enumeration of all16 length4 histories gives Pr(C=1 given D=1)=11/16 at u=1/8,t=3/8. C1 uses the valid martingale/stack arguments instead. |
| Swapped output coordinates | At t=a=1/4,Q=4, correct next1 is1/4. Swapping gives KL=(log3)/2. C2 explicitly outputs (Q-J,J)/Q. |
| Nearest grid need not minimize target KL | Recomputed kl(.37,.25)=.03521293857591873, greater than kl(.37,.5)=.03419149987688258. C2 claims an order bound, not exact KL optimality. |
| Fixed positive lower clip on row10 | For r tending to0 and q0>=tau in (0,1), minimum row KL tends to -log(1-tau)>0; terminal mass tends to1/3. C1/C2 do not apply such a clip. |
| Prefix endpoint cannot be replaced by S_N | For10001110, m=4, E_m=00 and S_N=10; direct prefix selected counts are(1,0). Thus the endpoints really differ. Counter's reported finite-frontend wrong count(2,0) is a retained C3 failure witness, not a C3 certificate supplied by this review. |
| A zero output on another terminal row need not make conditional00 risk infinite | The rule outputting(0,1) only on10 and uniform elsewhere has infinite average loss but finite conditional00 loss. C2 section8 correctly limits its conditional claim to histories ending00. |
| Symbolic reversal is not ordinary detailed balance | pi00 P(00,01)=ut>0 while pi01 P(01,00)=0. Both the proof and review preserve the distinction. |
| Minimax format floor is not a per-law floor | At u=1/8,t=1/4,Q=4, a source-independent constant output(3,1)/4 has zero conditional00 loss. The midpoint supremum witness remains valid. |

None of these counterexamples refutes the fixed C1/C2 claims. They constrain
extensions that the reviewed proofs explicitly avoid.

## 8. Independent diagnostics, repair status and handoff

New check_stats_grid_v1.py imports no project predictor, old test or model.
It enumerates four rational laws including a first-order law, boundary t
values and a small u, with all binary histories of lengths3..10. Exact
Fraction arithmetic verifies8,160 forward/reverse path factorizations,
80 entire-prefix TV bridges,128 unconditional martingale moment pairs,
and100 reverse occupation drift identities. Seven small full-history
conditional KL/chain-rule comparisons use floating point (tolerance
2e-12). For all count pairs D<=80 and Q in{2,4,8,16,32,64},19,926
cases verify integer clipping/conversion and coordinate domination;
row00 pointwise KL diagnostics use tolerance2e-13. Midpoint distances
through Q=1024, both Q4 half ties and the counterexamples above were
also checked. All passed. These finite diagnostics supplement the analytic
review; they neither prove all N,Q nor certify C3.

Reproduce with:

    python3 outputs/001-conditional-grid/verifier/check_stats_grid_v1.py

| New diagnostic artifact | SHA256 |
|---|---|
| check_stats_grid_v1.py | `fbcc3cb849fb69ec88e9801cfc7f966bae4ba33527ac115bf96b6b34715a3e35` |
| check-results-v1.json | `577194f8c4913e61a65750dc94b540e68663878000e23240b5e60159e73ef553` |
| native-state-v1.json | `697c79ff6c6d52fd6ea4f79f14647f51569b9ea485726616c0f9dde992ffd0e9` |

Mandatory mathematical repair hints: **none for C1; none for C2 assuming
the exact C1 theorem.** Preserve all branches, coordinate conventions,
actual-terminal conditioning, randomized comparator class and max lower
witnesses on submission. C1 can now be submitted by Prover to its exact
obligation. C2 then requires C1's actual returned native Fact identifier
as predecessor, not this report, an obligation ID, hash or old-project Fact.

Actual new Fact IDs=[]; actual new Evidence IDs=[]; submit_proof calls=0;
final_audit calls=0. No research-graph status or route was changed and no
new obstacle was manufactured. Existing diagnostic
`9fc456884c8bc452db60e856c443ae1cce960862deb0d3e9a5b28028859ed6d6`
is historical dispatch gating, not a refutation; the fixed Counter/Lead
review conditions are now met. Existing diagnostic
`0def94abb5dd20e9fc11024c4f656ce7f0d77ef78740e17ef61155836d95a99d`
still describes the separate full C3/C4 evidence/synthesis work; this report
does not close it. No old queues, failures, roots or source files were edited.

[Non-scientific operational metadata omitted.]
dimensions are UNLIMITED, and the Lead's explicit zero-GPU final-audit
reservation is pinned above. GPU used0; no continued-research switch,
external retrieval, model CLI or replacement agent was used. The staged
review does not establish architecture/internal-precision necessity,
optimized neural advantage, practical constants, noise reliability,
learnability or publication novelty, and does not complete the v10 mother
problem or its T1–T3 program.
