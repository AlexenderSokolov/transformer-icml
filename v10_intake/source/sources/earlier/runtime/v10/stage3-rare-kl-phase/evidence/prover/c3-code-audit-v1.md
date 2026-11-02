# C3 pinned code equivalence audit v1

Prover, 2026-10-25. This is an audit of the specified finite integer
function, not native evidence or a measurement of Python wall-clock costs.
Pinned input: `lead/integer_predictor_v1.py`, SHA256
`5eae6f7c009cd5e612c74274117109099b249a54dbdd62a6ee15e3da093662d6`.
The source file and its author/provenance are unchanged. New audit code,
results and the complete resource certificate are under `prover/`.

## Function-level all-input correspondence

| Pinned function | Audited invariant and proof location |
|---|---|
| `clog2` | `(x-1).bit_length()` equals ceil(log2 x) for positive integer x; no floating log. Its public arguments are positive. |
| `multiply` | After loop j, acc=sum_(k<j) bit_k(b)*a*2^k. At termination acc=a*b<2^(2width); complete products retained. The nominal operands satisfy each declared guard. |
| `divide` | The processed dividend prefix equals the processed quotient prefix times d plus rem, with0<=rem<d. After shifting, rem<2d, so one conditional subtraction suffices. Induction yields Euclidean quotient/remainder; d>0 throughout the actual program. |
| `generated_logs` | Its exact Fraction sum is the same rational as main-proof section4's common-denominator numerator divided by D_q. Final floor is the same Euclidean division. Only the resulting pair is needed online for a fixed N; arbitrary multi-N Python caching is not part of the finite resource claim. |
| `exp_weight` | Exactly main(10), including T0 in the total,8p steps, full product and one floor per step. `p+4` multiplication inputs cover score<2R and term<=6R; `2p+10` division-dividend bits cover the full product. |
| `adapter` | In zero-based Python indices the physical query index is N. Its keys `(m-1,m-2,N-1,N-2)` are the one-based m,m-1,N,N-1. The first two heads give E_m in lag order, last two give S_N; records keep only first m observations. All singleton edges are causal, masks are scanned, and the synthetic zero token is never an eligible statistical key. |
| `finite_counts` head loop | `records[2:]` is exactly keys3..m. Values are `(x,lag2)`, `(lag1,flag*lag1)` or `(lag2,lag1,flag*lag1,flag)`; all are query-independent bits. Scores match the P1,P2,T,U table and use the two generated finite coefficients. Accumulation and final division implement main(12). |
| `finite_counts` readout | The19 coordinates are ordered exactly as `MASTER_NAMES`. The alpha/nu/U selections and DT,D1,D2 match the first19 word operations. Its per-c loop matches the22 operations per coordinate: four full product/divisions, signed boundaries/difference, clip, snap. No count table is an input or readout bypass. |
| `positive_readout` | Lazy uniform branches agree with the straight-line output program's final mux. Its row00 dividend and quotient equal main(1), with next1 J returned in coordinate1. Row10 equals main(2), residual always to coordinate1. `2*v` division guard is generous; new numerator itself fits v and is <16mQ. |
| `d3_predict` | N<6 takes the constant branch and never calls M<=0 recovery. For N>=6 it calls the nominal finite frontend even if Q=2 or the final selected row is constant; the certificate charges this larger execution. Its probability output is the first returned component. Debug metadata in the second component is not an additional predictor input. |
| `direct_predict` | Eight counters consume the full observed sequence; only i=2,...,m-1 (Python indexing) update a counter. The final last pair selects exactly the same two prefix counts. It uses the same `positive_readout`. Main section8 proves all-path output equality. |

The source's `wrong_endpoint` option defaults to false and is false in
`d3_predict`; it is called true only as a negative diagnostic. No assertion,
Fraction-based sanity check or debug dictionary value changes the first
returned numerator vector. The finite circuit implements its integer
semantics without these debugging checks. We do not assert that running
the arbitrary-precision Python interpreter itself has the certificate's
fixed-width machine cost.

The neural graph may evaluate unused historical statistical rows with
the stated causal masks, whereas the reference computes only the query
row. Those unused outputs have no edge to the decoder. The resource
functions conservatively pay for all rows and explicit masks, so this
extension changes neither output nor the claimed upper cost bound.

## New independent bounded diagnostics

`check_c3_v1.py` reads the pinned code without executing an old main or
writing source caches (`sys.dont_write_bytecode=True`). Its fresh finite
evaluator creates the same19 head masters from the declared weights and
values, generates the log integers through the *different* common-
denominator construction, and executes the newly listed word program.
Direct counts appear only in the diagnostic oracle and the separate
strong-baseline function, never as an input to the finite head evaluator.

The fixed result reports:

- 63 recovery and41 output operations; unique result names and all use-before-definition checks pass.
- 480 exact Fraction flow-identity cases: all binary prefixes of lengths3..6 and all four queries.
- 820 output cases covering N=3,4,5,6,8,12, all counts0..M per coordinate (including nonnominal sum2M), all terminal rows, and b=1,2,3,8,64.
- 518 finite-grid expansion cases, including every endpoint numerator through h=8.
- 4680 small-width exact multiply/divide cases.
- 144 arbitrary closed-grid master fixtures checking signed ranges and snapped counts in[0,M].
- Six actual finite-head paths: 000000,111111,10001110,00111100,11111100,101010101010. These include M=1, distinct prefix/terminal endpoints and a selected row with zero visits. Their19 master errors are checked against exact ideal rational heads; recovered counts and output words agree with the pinned code and direct baseline.

The resource certificate instantiates all explicit functions at (N,b)=
(3,1),(8,2),(64,8),(8,1024). These are exact integer evaluations of
proved upper-bound formulas, not an enumeration of the enormous circuit
layouts. The proof includes an explicit compiler; no complete dense
matrix artifact of those oversized bounds is claimed to have been built.

## Actual corrections and remaining limits

No load-bearing correctness error was found in the pinned Lead integer
program. The checkpoint's '<64 blocks' was unverified; the complete
operation graph is now listed and independently interpreted. The new
readout graph has41 word operations, while recovery has63; these counts
refer to named instructions with the stated gate compilation, not free
word operations. The complete resource upper bounds replace, rather
than silently certify, the checkpoint's provisional small constants.

Total-word guards explicitly allow h+1 for closed-grid masters, p+1 for
the log3 numerator, signed intermediate ranges, nonnominal C0+C1<=2M,
and the new <16mQ dividend. The shared register interpreter, sparse
neural execution (which pays identity copies), tokenwise dense batch,
globally dense batch and fully flattened circuit now have separate costs.
The baseline's one-shot count width is W_C+2N+2ell, not its streaming
width W_C. All source002/005 and current Counter failure witnesses are
preserved in main section9 with their exact scope.

Open gates are independent fixed-version checking of this new full
certificate, then Lead's decision about native submission. No unclosed
mathematical lemma is knowingly used as a premise in the candidate;
that is a Prover assessment, not a verifier verdict. It does not establish
minimal costs, measured hardware performance, noise reliability or any
advantage over optimized strong baselines. Fact IDs=[], Evidence IDs=[].
