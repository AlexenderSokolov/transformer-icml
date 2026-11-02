# C3 and mathematical C4: finite programs, complete charges, and same-source separation

Author: Prover, original stage4 responsibility member, 2026-10-26. Target obligation: `db94b7040a4dc4e7d80329a02169b80039a17e1130f74893edd2c85bd848cab8`. Contract: `38d15641fecff6dbee957b6e036c052ecb7f07e6354623e800f7a126cf5270ef`.

## 1. Scope, admitted inputs, and conclusion

This proof establishes the mathematical component C3/C4 specified by the stated obligation. It does not itself establish later independent fixed-version review or final combined acceptance.

The only predecessors are the following two current-project VALID admissions, read back through the native research state. Their evidence verdicts are PASS at LLM_CHECKED_PROOF level.

* Fact `abbd577c047db274`, evidence `57a7e25c0478712a0c403c84bf27ee712f28a88e604ff0d1413d39feb21333e7`: the one common unknown-parameter JOINT family of D1-D4 has, for every N>=3, b>=1, d>=6 and every admissible map, R_av<=12000000/N+256 eta²+3/Q and R_00<=1800000/(1+Nu)+256 eta²+3/Q². Its self-contained clean statistical argument and finite count/grid transfer have already been admitted. Full Bstar was expressly excluded there.
* Fact `1a1aca7dd84c60da`, evidence `3f262cc0c76a700ab4f0163c011154c4e8f51655f5be6e5a7964d50b9f158989`: for d>=6, u=2^(-d-16), N a power of two, M=N/2-2 and Mu²>=2^40, one public globally lawful deterministic Phi_* independent of t and decoder works against every common post-cut decoder of actual FULL19. For that decoder one t_* in {1/4,3/4} gives R_00>=3/64 and R_av>=3u/64. The actual finite observation law includes all small coordinates and both protected endpoints.

We use precisely those conclusions, not old Facts or historical root admissions. In particular, no clean estimator proof, distributional lower proof, or old minimax proof is repeated here. The remainder, including the primitive implementation, is proved below. The result is a common available vector Bstar for the two specified programs, not equality of expenditure or a resource lower bound for optimized encoders. Three expressly priced alternative encoders show why the fixed-encoder qualifier matters.

The source hierarchy is D1-D8 in this project's `inputs/STAGE_DEFINITIONS.md`, the actual admitted claims above, then locally checked constructions. Copied source proofs and the controller seed are provenance, not axioms. The prior diagnostic `a607ba0f8dab12f83e8d70e62c19311f8721c87b854b4661b23aaad40c2e70ee` correctly identified missing program/physical-port certificates in an earlier checkpoint. Sections 2-13 below supply them; it remains in the record.

## 2. Public parameters and physical representation

For N>=6 put m=floor(N/2), M=m-2>=1, n=N+1, n_m=m+1,

    h=ceil(log2(256(N-2))), A=2^h,
    p=4h+4ceil(log2(m+4))+64, R_s=2^p,
    ell=ceil(log2(N+2)), tau=bitlength(d+1), Q=2^b,
    B=128p, O=32(b+ell+8), g(w)=1024w²,
    W_F=1024B, W_O=1024O.

Here R_s is the exponential scale; R_payload used later is a number of payload bits. They are different quantities. N>=6 implies h>=10 and p>=116. Parameters are compiled from public N,b,d before observations arrive. No u or t is given to any builder or decoder.

An integer word of width w is stored in a declared w-bit physical field; signed computations use two nonnegative rails, with a comparison selecting the sign when required. A Boolean wire is a scalar channel whose numeric value is 0 or 1. In a neural bank this channel still consumes the full B-bit or O-bit physical scalar slot. We never identify one logical bit with one physical scalar's entire storage cost. Primitive packed bit registers in the finite evaluator also have their full physical word fields charged. All arithmetic products are retained at full width before division or a proved safe cast. Rolling physical banks, code, coefficients, masks and metadata are separate allocations.

The principal realization is the D6 one-shot batch hybrid: tokenwise tied dense affine/ReLU layers plus an explicitly paid finite attention evaluator. All N inputs and the synthetic query are resident before the cut. After extraction and physical clearing, only the query decoder banks remain active. Finite evaluator time is not neural depth, and its work is not unit-cost integer arithmetic. Dense coefficient arrays include their zero entries. The alternative encoders in section 12 have a separately priced static circuit implementation and do not borrow the main programs' budget.

## 3. Elementary finite primitives and their compilation

We give constructive upper bounds, counting Boolean gate/read/write steps. A fixed register address or a fixed wire endpoint is generated explicitly; no input-dependent address oracle is used.

For bits, NOT(x)=1-x, AND(x,y)=xy, XOR(x,y)=x+y-2xy and OR(x,y)=x+y-xy are finite truth tables. A ripple full adder computes t=x XOR y, sum=t XOR carry, carry'=(x AND y) OR (carry AND t), at most five binary gates per position. A borrow chain has the same bound. Keeping the final carry/borrow proves addition/subtraction and comparison without silent wraparound. Compare signed numbers by signs then unsigned magnitudes. A word MUX is one selector applied bitwise. Constants, shifts, copying and zeroing explicitly write each destination bit.

Unsigned multiplication uses w shift-and-add iterations. At iteration j the accumulator equals x times the j low bits of y; it stays below 2^(2w). Each iteration uses at most 2w MUX gates and a 2w-bit ripple addition, including carry. Full 2w-bit output is retained. Division reads all 2w numerator bits from high to low. If 0<=r<v before a step, z=2r+next_bit<2v<2^(w+1). Compare z with v, subtract v iff appropriate, and append that comparison bit to the quotient. Thus the temporary remainder has w+1 bits, the next remainder again satisfies 0<=r<v, and induction yields numerator=quotient*v+remainder after all 2w steps. The quotient has 2w bits until a range proof permits narrowing. This proves restoring division, including numerator 0, without assuming a small intermediate remainder before shifting.

One may use the following explicit bounds, with temporary copies and their zeroing included. These are deliberately larger than the ripple constructions just given:

| operation | Boolean/read/write steps |
|---|---:|
| CONST, COPY, a fixed SHL/SHR with full destination | 8w+8 |
| ADD/SUB including final carry/borrow | 16w+16 |
| unsigned comparison | 32w+32 |
| word MUX, unsigned MIN/MAX | 64w+64 |
| signed ADD/SUB/MIN/MAX, both rails | 256w+128 |
| full multiply | 64w²+64w |
| restoring division of a full 2w-bit numerator | 256w²+128w |

For example, multiplication's w iterations each have <=16w gate actions and <=16w temporary/copy/clear actions; doubling the margin gives its displayed bound. Division has 2w iterations, each with a (w+1)-bit subtract/compare, a (w+1)-bit MUX, quotient-bit write and temporary clearing, below 64w+64 actions; doubling again covers sign wrappers and full numerator/quotient registers. All table entries and the finite wrappers fit g(w)=1024w² for w>=2. Workspace at most 32w+32 bits suffices: two inputs, two rails when used, a 2w product/quotient, w+1 shifted remainder, subtract and carry banks, and a distinct output. Registers whose contents are no longer needed are overwritten, not merely removed from a language's namespace.

These bit circuits have exact ReLU realizations. AND=ReLU(x+y-1), NOT=ReLU(1-x), XOR=ReLU(x-y)+ReLU(y-x), OR=ReLU(x+y)-ReLU(x+y-1). The negative subtraction in the last formula produces a nonnegative bit on Boolean inputs. At most four affine/ReLU layers implement each gate; allowing two-rail routing, distinct destination writes, temporary zeroing and phase synchronization gives sixteen. All other live bits are held by explicit identity channels; cleared channels receive zero. A G-step register circuit with S live Boolean scalar channels therefore has depth <=16G+32 and width <=S+8. A fixed-slot output or an integer scalar can also be extracted into bits: descending j, use ReLU(z-(2^j-1))-ReLU(z-2^j), subtract 2^j times that bit from the remainder, and continue. For integer 0<=z<=2^h this uses h+1 bits, including the endpoint A. Even using 256 actions per extracted bit is sufficient. There is no omitted real-number rounding primitive.

All coefficients in these constructions are integers or the explicitly generated public rational score coefficients. The latter are stored by numerator and power-of-two scale in the finite evaluator, not by an uncharged floating-point log or exp. Signed rails and full products do not enlarge physical widths beyond the live-width allocations proved below.

## 4. Actual input, adapters, masks, features, and finite heads

Read exactly the N observed bits once into an owned input bank, create (1-X_i,X_i) by charged subtraction/copy, and append a synthetic query with zero symbol value. It is not an observation. Four zero-score singleton adapter heads have masks with one allowed key per row. On historical row i they select i-1 (or i if absent), i-2 (or i if absent), i, i. On query row N+1 they select m,m-1,N,N-1, respectively. The heads have value width 2. Their masks have 4n² stored bits. All keys are causal; the fallback masks are nonempty. A finite evaluator with W(0)=R_s returns a singleton's value exactly, including its zero value.

The historical rows now contain their current symbol and two local lags. The query contains E_m=(X_(m-1),X_m) from heads 2,1 and S_N=(X_(N-1),X_N) from heads 4,3. Form the two pair one-hots by four ANDs each. No future bit enters them. A fixed prefix buffer contains the eligible keys 3..m; its public crop and permutation descriptors are charged. The actual terminal query is routed to its query slot, never replaced by the prefix endpoint. Statistical computation can evaluate just this required query row; allocating full n_m-square masks is a conservative charge, not a change in the query time.

Write S_N=ab. At a prefix key write lag2=i, lag1=j, current=c, f=I{key=3}. MIX forms F_k=ReLU(lag1_k+f-1) and these four heads:

| head | score integer | values in order |
|---|---|---|
| P1 | I{i=a}L2+I{j=b}L2 | current0,current1,lag2_0,lag2_1 |
| P2 | I{i=a}L2+I{j=b}L3 | current0,current1,lag2_0,lag2_1 |
| T | I{i=b}L2 | lag1_0,lag1_1,F0,F1 |
| U | 0 | lag2_0,lag2_1,lag1_0,lag1_1,F0,F1,f |

Q/K scores can be formed in four coordinates: concatenate two binary query one-hots, and multiply the matching key indicator coordinates by the appropriate generated L2/R_s or L3/R_s; T uses two coordinates and U uses none. Thus QK dimension <=4. Each output numerator is floor(A sum W(S)V / sum W(S)), with no rounded intermediate sum. Their concatenation is exactly FULL19, in the D2 order reproduced in Appendix A. The five small slots are computed, not inferred from population identities.

JOINT instead forms eight triple bits by two ANDs per triple (or one three-input threshold). It uses one zero-score head, eight value coordinates, producing floor(A C_ijk/M). Eleven explicit zero words are appended. Counts are obtained by summing those paid features over 3..m. This is exact because W(0)=R_s; the positive denominator is MR_s. Both programs retain exactly the same eight endpoint control bits.

For concreteness, the following frontend layer allocation is available before recovery; blocks can be padded by explicit identities or zeros. It is an implementation bound, not a claim that a mathematical feature is supplied free.

| block | affine/ReLU/attention phase layers allowed |
|---|---:|
| input one-hots, positions, zero query and mask selection | 8 |
| projections, four singleton attention heads, residual routing | 16 |
| local flags, gated F, and/or sixteen triple ANDs, fanout | 16 |
| actual endpoint one-hots, crop and query routing | 16 |
| statistical Q/K/value projections and finite attention calls | 32 |
| concatenate 19 outputs, append zeros where required, retain controls | 16 |
| extraction interface, move to the designated port-preparation bank | 16 |
| reserved reset/identity layers | 8 |
| total | 128 |

Each AND uses one layer and its routing at most another; pair one-hots, projections and fixed crop copies each use at most four. Attention is a separately evaluated finite block, with its bit work below. Thus the stated layer allocations implement the named blocks. Four additional COPY/ERASE/channel-interface/READBACK phase layers give P_*=132. An h-dependent integer serialization is implemented by the paid finite evaluator, or by the recovery extraction reserve, never hidden in 128 layers. MIX uses 8 heads total, JOINT 5; at most 4 simultaneous, maximum value width 8.

### 4.1 Finite log coefficients and exponential evaluator

For q=2,3 let S_q=2 sum_(j=0)^(p-1) 1/((2j+1)q^(2j+1)). The exact integer L is floor(2^p S_q). Its generator uses the common denominator

    D_q=q^(2p-1) product_(j=0)^(p-1)(2j+1).

Each D_q/((2j+1)q^(2j+1)) is an integer. Sum twice these integers, shift by p, and divide by D_q. This is an exact finite algorithm for the stated L2 (q=3) and L3 (q=2), with full products. The odd product can be shared. One loop builds it and powers 4^p,9^p: multiply the three accumulators, increment odd by 2, increment/check the index, at most 6 operations per iteration. A second loop maintains q^(2j+1) for both q, forms the two denominators, performs two exact divisions, doubles/adds to the two sums, advances powers and indices, at most 13 operations per iteration. Final shifts, quotients, initializations and clearing need fewer than 64 operations. Hence both logs fit 32p+64 word operations. Public loop control is included in these allowances.

For p>=116, log2(D_q)<4p+p log2(2p)<2p². The sums, shifted sums, trial products, and q powers use fewer than 4p²+16 bits, so B_log=8p²+32 contains full intermediates and division remainders. The primitive construction gives T_log=(32p+64)g(B_log) and scratch <=64B_log bits. The coefficients are generated before input arrival and stored. The executable builder likewise computes them before acquisition, not inside the online head loop.

The geometric identity 2 sum_(j>=0) x^(2j+1)/(2j+1)=log((1+x)/(1-x)) follows by integrating 2/(1-x²) term by term for |x|<1. Its positive partial sums give L2/R_s<=log2 and L3/R_s<=log3. Every score s=S/R_s therefore lies in [0,log6], with log6<2 (e²>1+2+2+8/6>6). The finite recurrence T0=R_s, T_j=floor(T_(j-1) S/(jR_s)) for j=1..8p obeys 0<=T_j<=R_s s^j/j!, so

    R_s <= W(S)=sum T_j <= R_s exp(s) <=6R_s.

In particular W(0)=R_s exactly, not an approximate uniform weight. A recurrence product is <16R_s². The divisor jR_s<=8pR_s. A head's accumulated denominator and each value numerator are <=6nR_s; the A-scaled numerator <=6nAR_s. Their full bit lengths are <2p+h+ell+16<B/4. Scores, products, accumulators, quotient remainders, and all live word registers fit the B domain. The score bound is <=2 as a real rational score, not a claim that the scaled integer S is <=2.

### 4.2 Paid finite evaluator loop counts

Implement masks by public scans and read each allowed value with a bit MUX; no free indirect lookup is used. Four singleton scans cost <=128n²+256n word operations (each key uses at most 16 value/mask actions per head, plus row/index work within the bound). Projection/crop/flags add <=64n. Score/weight matrices are evaluated one query/key at a time with rolling S,T_j,W registers and 19 numerator accumulators; only the public masks, not all data-dependent n-square score arrays, are stored. All n input/value banks remain resident, so this evaluator reuse does not replace batch acquisition with a streaming model. A statistical head/key uses 8p recurrence iterations; each needs multiply, exact divide, sum, and index update/check, at most 6 word operations. There are at most 7 value accumulations, two score terms and constant mask/index preparation. Including reads and clearing, 64p+64 operations per head/key suffice. Four such heads over at most n² query/key pairs cost <=(256p+256)n²; final normalized outputs and resets cost <=256n. Allowing the remaining index/endpoint copies gives the convenient mixed bound

    E_M=(256p+512)n²+1024n.

The JOINT indicator/zero-score loop has no recurrence multiplication and fits 512n², including adapters and its eight accumulators. Later physical cut scans are bounded by 4096nB+1024(h+1) additional word actions (section 7). We may pay the sum of the mixed and joint allowances even though only one program is executed:

    E_*=(256p+1024)n²+(4096B+1024)n+1024(h+1),
    T_*=E_*g(B).

Loop operands and loop indices have their own fixed fields; a row/key scan uses O(ell) bits, a recurrence scan O(log p) bits, both far below B. Index increments, comparisons and resets are included above. This is a word-step accounting followed by the proved g(B) bit expansion, not a unit-cost model.

## 5. Closed-box recovery and guarded output

The literal operation tables appear in Appendix A. They define a program on every independent 19-tuple in [0,A]^19 and every legal pair of protected one-hots, even tuples not produced by any history. Interpret each DIV as the unsigned full-width quotient after the preceding guard, each signed subtraction on rails. The appendix tables are the 63-operation MIX recovery, 15 word operations plus two control ORs for JOINT (within 18), and 41 shared output operations.

Recover a,b and the two E_m bits by ORs of their one-hot controls. These <=4 bit operations are within extraction's reserve. In MIX, U1,U2,V,alpha lie in [0,A]. Thus den1=2A-U1 and den2=2A-U2 belong to [A,2A]. The full normalization numerators are respectively <=4A² and <=6A²; their quotients D1,D2 lie in [A,4A] and [A,6A]. DT=A+alpha lies in [A,2A]. For each c the scaled products PH0,PH,PQ1,PQ2 lie respectively in [0,2A],[0,2A],[0,4A],[0,6A]. All these are floors of full nonnegative products divided by A.

Consequently I=PH0-f and base=PH-nu lie in [-A,2A], boundary in [0,A], gplus in [-A,3A], g in [-3A,4A], diff in [-4A,6A], and H=diff-g in [-8A,9A]. This derivation uses no consistency between input slots. Clamp H first below by 0 and then above by A. For 0<=x<=A,

    floor((2M x+A)/(2A)) in [0,M].

Its full numerator is <=A(2M+1). Thus MIX's two selected snapped counts each lie in [0,M]. JOINT uses six MUXes to select two of the eight returned coordinates and the same snapping expression, with identical independent-box guards; the other eleven words are read/cleared even though not used for selection. No clean count is retained as a fallback. Endpoint products and normalizers are not bounded by O(A) before their divisions: the 6A² products are explicitly retained. All these magnitudes have <2h+ell+8 bits; signed rails and division workspace fit B.

Load only the final two counts and the query bits into the O domain. Counts have <=ell bits. Q and all b-dependent data are first instantiated there; b can be arbitrarily larger than p. Conversely d is not used by either readout. Its possibly huge descriptor is stored and generated as public metadata, not cast into a B word or examined during prediction.

Let C0,C1 be any two integers in [0,M]. They may sum to 2M. The shared table forms

    D=C0+C1+2, Z=4D, 2<=D<=2M+2=2m-2.

For row00, z1=min(3D,max(D,4(C1+1))) belongs to [D,3D]. For Q>=4, J=floor((2Q z1+Z)/(2Z)) belongs to [1,Q-1], and Q-J is positive. This is nearest rounding with ties upward. At Q=4 the switches are exactly z1/Z=3/8 and 5/8, with the upper value at equality. There is no exceptional tie rule left unspecified.

For row10 let z0=min(3D,4(C0+1)), z1=Z-z0. Both are strictly positive and less than Z, with z0<=3D. Write x_c=(Q-1)z_c/Z. Their sum is the integer Q-1, and neither exceeds Q-1. Hence k_c=ceil x_c lies in [1,Q-1], k0+k1 is Q-1 or Q, and e=Q-k0-k1 is 1 or 0. The emitted pair (k0,k1+e)=(k0,Q-k0) is positive and sums to Q. The table implements ceil x by floor((integer_numerator+Z-1)/Z), preserving quotient/remainder exactly. For Q=2 or query01/11 the final MUX selects (Q/2,Q/2); all eagerly evaluated unused branches are still legal. At Q=2 the unused nearest candidate may be J=Q, but no denominator is zero or signed cast invalid. If both counts are zero, both active row branches give uniform. Snapped zero and small integers are therefore ordinary legal inputs, not exceptional missing cases.

The main nearest dividend satisfies

    2Qz1+Z <=(6Q+4)D <=(12Q+8)(m-1)<16mQ  (Q>=2).

Also 2Z=8D<16m, and each ceiling dividend is <QZ<=8Q(m-1)<8mQ. Thus b+ell+8 significant bits contain all these values; O=32(b+ell+8) leaves full product and shifted-remainder guards. The denominator literal Q, each numerator, and all their endpoint bits are explicitly written in (b+1)-bit fields, for exactly 3(b+1) emitted bits. A b-bit next-one code is not substituted for that port.

This establishes exact D4 program semantics on the closed boxes. C1 then applies to this JOINT program; C2 applies to this MIX program because it is one fixed common decoder of the returned FULL19 data. No nominal clean recovery theorem is needed to invoke C2's all-decoder conclusion.

## 6. Recovery live widths, two-domain transition, and active holds

A concrete recovery register layout keeps all input words and all table results until its own cleanup, rather than assuming an in-place optimization. MIX has 19 master words, four endpoint bits, and 63 named results: at most 86 B-word slots. Two rails for all of them occupy at most 172B Boolean scalar channels. Allow 32B+32 primitive scratch channels, 32B channels for public counters/phase registers, 19(h+1)+8 extracted data bits and at most 32B channels for extraction/copy temporaries. The sum is <384B for p>=116. JOINT is smaller. Reserving W_F=1024B scalar channels therefore pays every live register and spare port slot. A copy and cleanup of these live logical fields, including count routing, takes <1024B Boolean actions. Scalar extraction takes <=256*19(h+1) actions. Thus

    G_F=63g(B)+256*19(h+1)+1024B,
    L_F=16G_F+32

covers the complete recovery circuit, including the endpoint-bit ORs, signed temporaries, full products, and its own cleanup.

The shared output table has four inputs and 41 results. Two rails occupy 90O channels, scratch <=32O+32, public/control fields <=32O, and the guarded port and copy temporaries <32O. Hence <256O channels are live. Its copy/cleanup fits 1024O Boolean actions; 64(b+1) actions more than cover reading/writing the three guarded output fields and assembling Q-J if needed. Therefore

    G_O=41g(O)+1024O+64(b+1), L_O=16G_O+32,
    W_O=1024O

are sufficient.

For the width transition, first project onto the <=2ell+4 significant count/control bits. This intermediate bank is smaller than both W_F and W_O. Clear all other frontend channels, then expand into the output bank with zeros. The corresponding dense rectangular maps fit a W_F-square block and a W_O-square block, respectively; the extra 32 layers in L_F,L_O cover these moves. We do not require a W_F by W_O dense matrix charged at the wrong word width. When O<B, the counts are safely cast only after their [0,M] range has been proved; when O>B, no b-dependent value was previously stored in B.

Before extraction all n token banks are active for at most P_*=132 layers. After the cut and physical clearing, nonquery banks are released/reset and recovery operates on one query bank. Identity holds, including otherwise inactive register fields in the active bank, are therefore bounded by

    I_*=132nW_F+L_FW_F+L_OW_O.

The larger n factor in the recovery term of online work below is only an overcharge. It does not justify leaving a hidden n-token history bank active or charging streaming widths before the cut.

## 7. Actual cut: named banks, scans, and factorization

Allocate at most four frontend rolling banks, each of nW_F physical B-bit scalar slots. This includes input one-hots and their original owned input cells, all lags, flag/triple features, prefix/crop buffer, Q/K/value buffers, score and T_j registers, sums and denominators, clean masters, pair controls, residual and full product/remainder scratch, layer input/output copies, and public scan registers. Public constants/code are separate and source-independent. A fresh port region P, disjoint from all live clean data, fits in the spare frontend allocation: its only variable contents are nineteen closed (h+1)-bit integers and eight controls. Any surrounding physical padding is set to zero. There is no additional mutable source-dependent field in the external interface.

The executable schedule is as follows, with fixed public bounds.

1. COPY_TO_P: serialize the already quantized 19 words, including the endpoint bit for A, and the eight protected controls into the fresh port. Complete all writes before destroying any source. Write every unused physical padding bit to zero.
2. ERASE_ALL_OLD: scan the four rolling banks in a fixed lexicographic (bank,token,channel,bit) order, skipping only P and public constants. Overwrite every other physical data field with zero. This includes old endpoint controls, input/tail, master copies, intermediate counts, quotient/remainder scratch, old port-preparation copies, and both input/output activation banks from the preceding layer. Clear the scratch used by this scan; its indices are public. No history-dependent random seed exists in these deterministic programs.
3. External overwrite: expose only P's 19 integer words and its protected controls to Phi. The channel replaces the word contents in P, leaving the controls unchanged. Any original-code storage internal to the external channel is not predictor memory and is inaccessible to the decoder. The channel's own complexity is excluded by D3; its interface transfers are paid here.
4. READBACK: initialize the recovery bank, read all 19 returned words and eight controls, then zero the old returned port and its transfer temporaries. Only this returned-data bank enters the recovery circuit. After count extraction the output transition of section 6 clears recovery temporaries as well.

These are actual CONST/COPY/store scans, not a request for garbage collection or a proof that old variables are merely unused. There are 4nW_F=4096nB physical frontend scalar slots. One scan-step bundle per slot performs the full-width CONST, increments the short public channel/token/bank counters, compares their fixed endpoints, and advances or resets them. CONST plus at most six ADD/compare/reset actions costs <=512B+512 Boolean/read/write actions by section 3, strictly below g(B). Thus 4096nB charged word-step allowances suffice for the full scan, even counting skipped slots; loop control is not an additional unpriced operation. Initial port write, full readback, controls, padding, phase scratch and address resets fit 1024(h+1) further word operations: fewer than 16 actions per each of the 19(h+1)+8 meaningful port bits, with a factor of more than three left for scratch and representation conversion. A full-width physical write is expanded by g(B), which exceeds its B bit writes. The scan's transient primitive scratch is within the same four-bank allocation and is cleared by the primitive's own routine. During clearing, previously cleared words are not touched except by zeros or public indices. One may purge rolling copies in fixed order, reserving a distinct small public-only controller register; its final clear is charged. There is no layer input bank containing a forgotten clean duplicate when Phi acts.

The four phase layers account for parallel affine transfers and bank switching. The serial scans just counted are additionally included in E_*g(B), so their large bit cost is not hidden by the four-layer count. This also pays the scalar/bit representation of the returned integers. Physical port padding is invariant zero and is not an extra information channel. The external alphabet is exactly 19(h+1)+8 variable bits subject to the declared integer/one-hot constraints.

By induction on this schedule, immediately before Phi every source-dependent predictor location outside P is zero; immediately after readback every nonpublic input to recovery is a function only of the returned words and protected controls. Thus for either encoder the actual prediction has the factorization

    q = Decoder_(N,b,d)( Phi(Encoder_(N,b,d)(X_1..X_N), controls), controls ).

The decoder has no history argument, reread path, residual master, or retained clean random state. The factorization is pathwise, for every closed returned box, not just almost surely under one source. It is what licenses the use of the all-decoder C2 admission for MIX.

## 8. Complete principal Bstar ledger and construction of code/addresses

The budget here is exactly D6. The following definitions are part of this proof so that no external calculator carries a mathematical premise:

    Z_*=128n(ell+p+b+16)+256n(ell+h+b+tau+32),
    M_*=4n²+4n_m²,
    a_*=bitlength(T_*+G_F+G_O+Z_*+1)+ell+tau+32,
    V_*=B+O+a_*,
    K_*=4096[g(B)(B+a_*)+g(O)(O+a_*)]+256(p+1)V_*²,
    D_*=(132+L_F)(W_F+1)²+L_O(W_O+1)²,
    P_bits=(132+L_F)(W_F+1)²B+L_O(W_O+1)²O,
    U_*=P_bits+K_*+M_*+Z_*,
    W_run=4nW_FB+4W_OO+Z_*, peak_run=U_*+W_run,
    T_run=256[(132+L_F)n(W_F+1)²B²+L_O(W_O+1)²O²]+T_*.

Depth is L_*=132+L_F+L_O and per-token width W_*=max(W_F,W_O). Further coordinates are total heads<=8, simultaneous<=4, values<=8, QK<=4, absolute score<=2, frontend/output word bits B/O, nineteen cut words of h+1 bits, eight protected bits, and 3(b+1) emitted bits.

We now justify every resource coordinate by a realization, not by comparison of two preexisting formulas.

**Masks and metadata.** Store four n-square singleton masks. MIX's four prefix statistical masks occupy <=4n_m² additional bits; JOINT needs only n_m². Source-dependent data never enter these masks. Public descriptors include the N positions and validity/crop flags, the fixed query and endpoint selectors, per-head dimensions and score/scale descriptions, output precision, word sizes, full loop endpoints, and d's compact descriptor. One explicit format allocates at most 64 records per token of length <=ell+p+b+16 for adapter/frontend descriptors and at most 128 records per token of length <=ell+h+b+tau+32 for crop/port/output descriptors, retaining a duplicate for generation/dispatch. This is bounded by Z_*. The actual list uses fewer than 32 records of each type: the four head key selectors and their dimensions, four statistical selectors/dimensions, input/query/crop flags, eight endpoint/control labels, nineteen port labels, and a fixed set of lengths/loop endpoints. Global public constants and output descriptors can be placed in the first token's spare records. The tau field pays the full representation of d, although no online arithmetic needs it. Thus M_* and Z_* contain the actual complete mask/metadata data, not placeholders for uncharged addresses.

**Addresses and scans.** Use segmented rectangular arrays with a fixed tuple of indices: bank, layer, token, channel, coefficient-column, bit. Each field is bounded by a_*: layer lengths are <=16(T_*+G_F+G_O+1)+96; word/gate indices are below that expression; token and column fields have logarithmic lengths bounded by the added ell+32. Port and mask offsets have at most 2ell+O(1) bits. Tuples of a fixed number of fields are included in each instruction's reserved record. We do not assert that a_* can address all U_* bits in one flat pointer when b is arbitrarily large. A flat offline output address is instead paid by A_gen below. Sequential scans increment the actual short loop fields (<=ell+log p+O(1) in the B evaluator, <=log O+O(1) in output); they do not read a padded tau-bit record at every online gate. Source-independent unused public descriptors remain in stored memory. This is necessary, for example, when d is huge and neither predictor uses it.

**Primitive library and executable loop code.** Store explicit wiring records for the finite primitive types from section 3, in each of the B and O domains. Including the auto-increment CLEAR_NEXT scan instruction just described, there are at most 24 types; each needs <=g(w) records, each <=64(w+a_*) bits including operation, fixed tuple endpoints, control bits and literal data. Their total is <=1536[g(B)(B+a_*)+g(O)(O+a_*)], below K_*'s 4096 multiple. The remaining margin pays dispatch, two-rail copies and public scan/clear routines. A library record is an explicitly wired Boolean operation, not a runtime unit-cost multiply. The unrolled neural recovery/output gates have their own dense parameters counted in P_bits; the shared finite evaluator calls this finite bit library and pays every gate in T_*.

The remaining loop code consists of the fixed 63/18/41 operation descriptions, adapters, the finite 8p recurrence schedule (including jR_s literals if precomputed), public copy/clear loops and score/normalization dispatch. At most 128(p+1) records of length <=2V_*² suffice: there are 8p recurrence entries, fewer than 256 other word instructions and loop templates, and fewer than 64 literal/field types. p>=116 supplies more than 128(p+1) record slots. Full literals, both word domains, all fixed address tuples and loop bounds fit their records because each needs at most a constant number (<=32) of V_* bits and V_*>=32. This gives 256(p+1)V_*². Fixed loops iterate the public bounds, perform counted increments/comparisons, and read masks by scans, not by an unspecified search. The code library is shared, not re-stored once per token or query. Its complete stored bits are included in K_*; no executable instruction is free metadata.

**Dense matrices, depths and holds.** Section 4 provides <=132 frontend/phase layers, section 6 <=L_F,L_O recovery/output layers and widths W_F,W_O. Store each tied tokenwise matrix once, including bias as an extra row/column and every zero coefficient. Their slots and coefficient bits are bounded by D_* and P_bits, respectively. Endpoint projections and the two-domain bridge use the same-square envelopes as shown in section 6. Coefficients fit their B or O physical words. In fact arithmetic-gate coefficients are small integers, extraction coefficients are at most 2^(h+1), and the output literals have <=b+2 bits. A dense partial sum therefore fits the word's guard: input magnitudes use <w/4 bits, the number of terms has log2(W_F+1)<B/4 or log2(W_O+1)<O/4, and the nonzero coefficients in a gate have the proved smaller bounds; zero entries add nothing. Exact full products are formed before the safe sum/cast. Section 6 proves the active identity-hold count I_*; coefficients for those identities are included among dense entries.

**Online bit work.** A dense multiply-add with w-bit fields uses a full 2w product (<=64w²+64w actions), full guarded accumulation and final cast. Reading operands/coefficient and writing/clearing scratch fit another 64w²+64w. For w>=B_min or O_min, 256w² is an upper bound. Evaluation includes zero coefficients and biases. Before the cut apply frontend dense layers at all n slots. Recovery only needs the query, but charging n slots for its L_F layers is allowed. Output has one active bank. This gives the first part of T_run. Add T_* for the separate finite evaluator, including its actual public scans and physical erasure. Output serialization, copies and resets are already in G_O, and thus in its dense evaluation. No arithmetic operation or loop search is declared free.

**Working, stored and simultaneous peak memory.** Four nW_F B-bit rolling frontend banks include all allocated physical data, even during copying before an old bank is erased; four W_O O-bit banks cover the output transition and its full-word scratch. The metadata working copy is Z_*. This is W_run, not a streaming count-width bank. U_* simultaneously contains dense parameters, code, masks and stored metadata. Therefore peak_run=U_*+W_run bounds simultaneous stored and live data. It does not replace memory by the tiny cut capacity. These allocations also cover the input, synthetic query, endpoint one-hots, all tail data before actual erasure, and the guarded output fields. All model coordinates have now been charged.

## 9. Offline generator, including every emitted coefficient and bit

Set

    B_log=8p²+32, T_log=(32p+64)g(B_log),
    A_gen=B_log+B+O+bitlength(U_*+L_*+1)+ell+b+tau+32,
    T_gen=T_log+1024(ell+b+tau+p+1)²
          +4096(U_*+L_*+1)A_gen²,
    W_gen=64B_log+64(ell+b+tau+p+1)
          +64(U_*+L_*+1)A_gen,
    peak_gen=U_*+W_gen.

A generator first derives h,p,word lengths and powers of two by binary scans/shifts; reading N,b,d and writing these fixed constants needs at most 1024(ell+b+tau+p+1)² bit actions, using schoolbook addition and multiplication where necessary. It computes the two logarithms by section 4.1. A JOINT generator may omit that work, but the same available budget retains it.

Next it enumerates the frontend block templates, the gate expansion of every table operation, and the dense entries in lexicographic layer/row/column/bit order. It writes zeros as well as nonzeros, identity coefficients, masks, public metadata and the two primitive libraries. A primitive gate-expansion iterator maintains the operation number, bit position, carry/product/division microstep, and fixed tuple addresses. Each emitted field requires at most eight additions/subtractions/comparisons or schoolbook products/divisions on A_gen-bit counters; in the dense-matrix iterator only comparisons with the finite gate endpoints and a literal write are needed. The elementary bounds of section 3, without its large all-purpose g wrapper, make each such fixed group cost <4096A_gen². Public mask entries are equality/inequality tests on position counters. The number of output-bit steps, program/layer delimiters and index advances is <=U_*+L_*+1 by emitting one bit per step and attaching delimiters to already allocated instruction/metadata records. Layer traversal adds the L_* allowance. Hence the displayed T_gen pays actual finite generation, not a unit-cost act of describing enormous matrices.

A_gen contains log2(U_*+L_*+1), so the flat generated-file address and all products used in its nested counters fit. The bound also contains B_log,B,O and complete public input lengths; no large address is squeezed into B. The working record stack can conservatively keep <=64 A_gen-bit words per output bit/layer, plus the logarithm and public-parameter scratch already specified, giving W_gen. Streaming emission could use much less but is not assumed. Retaining the generated program while this scratch exists costs U_*+W_gen. These are explicit finite upper bounds for work, scratch and peak, for every N,b,d in the domain.

## 10. N=3,4,5: early uniform program before all builders

The generator tests the public N first. If 3<=N<=5, it never constructs a prefix, frontend, error cut, or recovery program. It reads exactly the actual N input bits into owned cells, emits (Q/2,Q/2,Q) in three (b+1)-bit guarded fields, and overwrites the input cells. There is no call to a builder at max(N,6) and no invented sixth observation. It can ignore the observed values after charging their read. This is the same uniform branch in both programs.

For an explicit complete small-program ledger set ell_s=ceil log2(N+2)<=3, tau=bitlength(d+1), beta=32(b+11)=O(6,b), width=32 and depth=16. Use no heads, masks or cut. Store

    Z_s=128(ell_s+b+tau+16), K_s=4096(ell_s+b+tau+16),
    P_s=16*33²*beta, U_s=P_s+K_s+Z_s,
    W_s=4*32*beta+Z_s,
    T_s=256*16*33²*beta²+64(N+3(b+1)).

A fixed parallel affine layer reads the <=5 input bits; a constant layer writes the three output words, explicit serial guarded-port writes cost the second term of T_s, and a reset layer clears the input/temporary cells. Sixteen layers and 32 scalar channels leave ample copies and literal slots. Full scalar storage is beta per channel. The code contains a short loop for the port bits, not a b-dependent number of neural layers. Let

    a_s=beta+bitlength(U_s+17)+ell_s+b+tau+32,
    Tgen_s=1024(ell_s+b+tau+1)²+4096(U_s+17)a_s²,
    Wgen_s=64(ell_s+b+tau+1)+64(U_s+17)a_s.

The same bit-by-bit generator proof charges its code, constants, output layout, work and peaks U_s+W_s and U_s+Wgen_s. Identity holds are at most 16*32. The exact 3(b+1) output writes are retained.

Every coordinate is <=Bstar(6,b,d): there n=7, ell=3, h=10, p=116, B=14848, O=beta. The large program has W_O>=1024beta>32 and L_O>=16*41*1024beta²>16. Its output parameter/work expressions alone dominate P_s and the dense part of T_s. The slack from replacing width 32 by 1024beta and depth 16 by L_O exceeds 64(5+3(b+1)), since beta>=32(b+11). Its Z_* has coefficients at least 896 on b and at least 1792 on tau, exceeding Z_s. Its K_* contains 4096g(O)(O+a_*), with a_*>=tau+32 and O>=32(b+11), which exceeds K_s. Frontend banks already exceed W_s's input storage, and the output banks exceed its output storage. Thus all stored, working and online peak sums are dominated. a_s<=A_gen because beta=O, U_s<=U_*, the added B_log+B+ell terms cover the fixed 17-layer difference, and ell_s<=3; the public-generation square and scratch terms are likewise dominated. Generation work/scratch/peak follow term by term. Zero heads/masks/cut and the 16*32 holds are smaller than their available coordinates. Bstar(6,b,d) is only the allowance used in these inequalities, not an executed six-input program.

## 11. Same Phi, same witness, finite strict gaps, and erratum

For any integer d>=32 choose exactly

    eta=2^-d, N=2^(2d+74), b=2d, Q=2^(2d), u=2^(-d-16).

Then m=2^(2d+73), M=2^(2d+73)-2 and

    Mu²=2^41-2^(-2d-31)>2^40, Nu=2^(d+58).

These are in both admitted domains. Invoke C2's single public globally admissible Phi_* for this tuple. Apply its all-decoder statement to the concrete MIX63+41 decoder proved above, including all its endpoint controls and erasure boundary. It supplies one t_* in {1/4,3/4} giving simultaneously MIX R_00>=3/64 and MIX R_av>=3u/64.

Now apply C1 to the one concrete JOINT18+41 family at precisely this same source (u,t_*) and the same global map Phi_*. Its input codes need not equal MIX's codes; C1 is uniform over all maps on its own actual cut, and Phi_* is lawful everywhere. There is no second witness selection. For the average upper,

    U_av=(12000000*2^-74+259)eta²<260eta²,
    U_av/(u/64)<260*2^(22-d)<=260/1024<1.

For the conditional upper, using 1800000<2^21 and Nu=2^(d+58),

    U_00<2^(-d-37)+2^(8-2d)+3*2^(-4d)
         <=2^-69+2^-56+3*2^-128<1/64.

Thus JOINT R_av<u/64 and R_00<1/64, while that same MIX has the two stated lower bounds. The gaps exceed u/32 and 1/32. Sections 2-10 put both programs within the same complete available Bstar vector at that tuple. The bounds need not be attained resource expenditures and imply no componentwise efficiency, optimal architecture separation, universal per-source dominance, or lower bound on all encoders.

The conditional erratum is retained explicitly. On this exact unchanged schedule,

    1800000/(1+Nu)
      =(1800000/2^58)*eta/(1+eta/2^58).

This term is bounded above and below by positive constant multiples of eta for d>=32; the other displayed conditional terms are 256eta²+3eta^4. The total displayed conditional upper expression is therefore Theta(eta), not O(eta²). Only its noise contribution is O(eta²); the average displayed upper is O(eta²). This is a statement about the upper expression, not a matching lower asymptotic rate for JOINT's risk. The original contrary sentence in source010 remains a historical error, not a premise silently repaired by changing N or Q.

## 12. Three finite alternative encoders, with complete separate charges

These are changes to the encoder and to what is computed before its cut. They are not new post-cut decoders of frozen FULL19, and hence do not contradict C2. No alternative is asserted to fit Bstar or to use the same expenditure. We give explicit constructions and finite vectors, including acquisition, full physical ports and generation.

### 12.1 Acquisition and pre-cut calculation

Use a separately generated, static, one-shot Boolean register circuit with dense ReLU simulation. It receives the same actual N bits once. Allocate source cells for input bits, their two one-hot coordinates, two local lag one-hots, and eight triple indicators: at most 15n logical cells, including the synthetic slot if used. Direct fixed wires from positions k-2,k-1,k are generated and paid; no pair/triple table is an input. Sixteen AND gates per eligible key create its eight triple bits. Eight initialized binary counters add those bits over k=3..m. A loop-expanded static circuit has these fixed wire endpoints; input-dependent lookup is unnecessary. Compute S_N and E_m by fixed endpoint copies and four pair ANDs each. This acquisition is not inherited for free from the main program.

For later accounting use

    kappa=min(d,h), ell_C=ceil(log2(M+1)), H=19(h+1)+8,
    beta=128(p+b+ell+tau+h+16), g_beta=1024beta².

All count and output arithmetic fits beta: counts use <=ell bits, Q uses b+1 bits, the gain full products below use <p+h+2ell+8 bits, and physical/address margins are explicit below. Every logical bit of the circuit is a beta-bit physical scalar. Count registers, rails, primitive full-product/remainder scratch and the precomputed-output table occupy fewer than 256beta logical cells; we reserve more than four times that amount below. For each symbol, <=16 local Boolean gates and <=8 beta-word additions, along with fixed copies/index actions, fit 512 word-equivalent primitive allowances. Fewer than 256 further allowances initialize/control the counters and evaluate the eight optional gain numerators/divisions. Thus

    G_acq=(512n+256)g_beta

pays one-shot acquisition and every count operation, and also the gain arithmetic if that alternative is used. Bulk initialization of allocated unused/source and physical rolling banks is separately included in the transfer reserve below; it is not charged to these 256 word operations.

**Gain encoder.** Set g=M/A as a public rational pair (M,A), and give the uniform head the exact rational values g times each triple indicator. Its complete integer evaluation for coordinate c is

    floor( A * [sum_k R_s M I_c(k)] / [A M R_s] ) = C_c.

The uncancelled numerator is A R_s M C_c and the denominator A M R_s; both are formed or, equivalently, generated by their explicitly charged product sequence before exact division. All factors are public except the paid counter C_c. This realizes the finite gain head without inserting an intermediate floor on the values. Multiplications, the gain literal's two physical words, exact division and serialization are in G_acq and the conversion reserve below. The first eight port words are these counts, the remaining eleven are initialized zero. Because C_c<=M<A the closed integer range is respected. For this alternative R_payload=8(h+1), with block width k=h+1; the general transfer schedule below places one complete count word in each of the first eight slots. We do not claim arbitrary such counts are locked: they obey the same D3 relative map, and returned counts are clamped to [0,M] before output. On the comparison schedule M is large, so this distinction is material. The identity j=C already shows the encoder's gain is not fixed by port capacity alone.

**Locked count packing.** If R_payload=8ell_C<=19kappa, serialize all eight exact counts, each in ell_C bits. Place successive kappa-bit chunks in the low bits of successive port words, filling a partial final chunk with zeros. Every word is <2^kappa<=A. Since d>=kappa, eta*j<1 for each such word; floor(eta*j)=0, even for j=0. Every globally admissible, arbitrarily correlated D3 map therefore fixes all these words pathwise. The full count payload is recovered exactly after readback. On the comparison schedule h=2d+82 and ell_C=2d+73, so kappa=d and the sufficient inequality is 16d+584<=19d, true for every integer d>=195. These formulas follow directly from M+1=2^(2d+73)-1 and 256(N-2) between 2^(2d+81) and 2^(2d+82). No independence of errors or repetition argument is used.

**Locked precomputed output.** Before the cut, select the two exact row counts and run the shared41 table, including all its positive-output branches. Let J be its next-one numerator; 1<=J<=Q-1, so it has a b-bit representation. When R_payload=b<=19kappa, pack these b bits in exactly the same low-bit scheme. After the cut the payload is locked and J is recovered exactly. The post-cut program forms Q-J by full subtraction and writes (Q-J,J,Q) with 3(b+1) guarded bits. This explicitly pays for computing the output before the error location and reconstructing its guarded port afterward. On the comparison schedule b=2d<=19d=19kappa for every d>=32. No full guarded output is falsely counted as b raw bits at the final port.

For arbitrary returned boxes, the gain/count decoders clamp each selected decoded count to [0,M] and use shared41. The output-packing decoder clamps a decoded b-bit J to [1,Q-1] before subtraction. These guards make even their unused off-image cases defined. On their lawful locked images the clamps change nothing. All three remain source-independent, with no u,t access.

### 12.2 Exact logical transfer and erasure kernel

This is a checked implementation of the new controller seed, expanded here so the seed is not a premise. Let R_payload=R, block width k, and choose a source bank of W logical cells containing the payload, the eight controls, every other source-bearing register and every pre-cut scratch copy. Its unused cells are initialized zero. For gain, k=h+1 and R=8(h+1); for the locked alternatives, k=kappa and R<=19k. Let

    place(i)=floor(i/k)(h+1)+(i mod k), 0<=i<R.

Allocate a fresh full port P of H cells, a fresh full returned temporary T of H cells, and U of R+8 cells. A logical READ or WRITE is one action; COPY is two actions. Use this fixed program:

| stage | operation | logical actions |
|---|---|---:|
| 1 | write zero to every P cell, including all h+1 high positions and 8 controls | H |
| 2 | copy source payload bit i to P[place(i)] for i=0..R-1 | 2R |
| 3 | copy all 8 protected controls to P's last 8 cells | 16 |
| 4 | overwrite every old source/scratch cell, not only payload cells | W |
| 5 | external D3 overwrite on the 19 integers; protected controls unchanged | 0 predictor actions |
| 6 | initialize all U cells to zero | R+8 |
| 7 | initialize every T cell, then READ/WRITE all H returned P cells into T | 3H |
| 8 | overwrite all P cells | H |
| 9 | copy T[place(i)] to U[i], and all 8 controls from T to U | 2R+16 |
| 10 | overwrite all T cells | H |
| total | | K=6H+5R+W+40 |

In particular, initialization and readback cost H, not 19k. This remains valid when h is enormously larger than kappa. K<=8(H+R+W+8) follows by subtraction, but we use the exact K. For R=0 all loops still have their stated endpoints, and the controls/high bits are handled identically.

After stage 4, only P can contain source-dependent data. For locked packing its words have zero high bits and lie below 2^kappa, hence the full returned words equal those sent, including their high bits. In every case stage 7 reads all h+1 bits of all nineteen returned integers, not merely the payload positions. Stages 8 and 10 erase both full interface copies. At exit U is a function solely of the returned P and protected controls, while all old source, P and T cells are zero. The decoder factorization follows by this explicit invariant. Nothing is recovered from an old pre-cut count/output bank.

The source bank includes the actual input, local features, all counters, precomputed J/Q-J if any, gain temporaries, accumulator copies, and compiler scratch. Logical aliases are resolved into named physical allocations: either they refer to one field, or every duplicate is listed in W or the physical-bank purge below. The kernel is not implemented by assigning a new Python list and assuming the old list vanished. The accompanying interpreter checks value/phase semantics only; the following finite compiler is the physical implementation and cost proof.

### 12.3 Physical compilation and full alternative ledger

Use the following uniform, deliberately large finite vector for each available alternative. Its source-bank and circuit bounds are

    W=16n+1024beta+4R+H+64,
    S=W+2H+R+8+64beta,
    K=6H+5R+W+40,
    G_pre=I{OUTPUT_PACK}*64g_beta+16(R+8),
    G_post=(16 if OUTPUT_PACK else 96)g_beta+64(b+1)+16(R+8),
    T_transfer=(K+20S+1024)g_beta,
    G=G_acq+G_pre+T_transfer+G_post,
    L=16G+64, C=S+8.

W holds the <=15n input/feature bits, all arithmetic/precomputed-output rails and scratch (<=256beta, with another identical copy if needed), <=2R serialized payload/copy cells and the protected endpoints; its larger reserves also cover phase-controller temporaries. S adds full P,T,U banks and 64beta additional public/gate scratch. There is no live count stack beyond this allocation. This proves live width rather than assuming a count register supplied by an oracle.

Pre-output selection needs six MUXes and <=4 control ORs, followed by 41 operations; 64g_beta pays them and their wrapper. Serialization takes <=16(R+8) bit/copy actions, including bit order and zero padding. For the gain/count post-decoder, eight deserializations, two count clamps, six selection MUXes, shared41 and control copies fit 96 primitive allowances plus the separately displayed serialization term. The output-only post-decoder needs a clamp, full Q-J subtraction, literal Q and field copies, fewer than 16 primitive allowances. The 64(b+1) term pays all guarded output reads/writes. The pre-output computation is thus separately visible in G_pre; it is not charged as free reuse of a clean output at the cut.

For physical execution allocate four C-channel rolling banks, each scalar beta bits. A full-word sweep step includes the CONST/COPY, at most six short-counter increment/compare/reset actions, and fixed bank selection; it costs <=512beta+512<g_beta, so its index control is included in each stated allowance. Each logical transfer action is implemented with explicit full-width reads/writes using section 3's primitives, costing at most g_beta; high physical padding is written zero. K is only the logical kernel's action count. Five additional groups, each bounded by four S-word sweeps, pay (i) initialization of all physical rolling banks, (ii) the pre-cut purge of every non-P field, (iii) the obsolete returned/temporary-bank purge after readback, (iv) final nonoutput cleanup, and (v) retained-field copies and bank handoffs. Each sweep writes complete beta-bit physical scalar fields. The 1024 extra allowances pay the eight spare channels per bank, public-address controller/latch clearing and final index resets. This is why T_transfer uses K+20S+1024, a strengthened physical reserve beyond the seed's logical K; no extra sweep is passed off as one bit or as language garbage collection.

Stop the pre-cut executor after P is prepared, then scan every non-P physical field, including a prior layer's input copy. Keep only the designated P cells; scratch is cleared by the primitive itself, and scan indices are public. After full readback and unpack, stop the transfer executor and purge obsolete physical copies, keeping only U's designated returned-data fields. A fresh bank handoff copies its retained fields before purging the source, and is charged to the fifth group. The retained fields total less than S in each handoff, and there are at most four such handoffs (source-to-port, returned-port-to-temporary, temporary-to-U, U-to-output). At the external channel instant all physical non-P source-bearing scalar fields, not just their active low bits, are zero. ReLU dense coefficients and code are public, so retaining them is harmless and paid.

Convert the G Boolean/read/write primitive expansion to the static ReLU register circuit of section 3. We permit 64 rather than 32 end/phase layers. Every inactive logical channel is held explicitly while active, including port bits; all zeros are stored/evaluated as dense entries. This static circuit spans the actual whole input in one batch and has width C, not a streaming width. Its memory charges use beta per scalar channel. We do not replace the main programs' principal hybrid with this different alternative ledger.

For complete stored/code/address costs define

    Z0=256n(ell+b+tau+p+h+32),
    a=bitlength(G+S+L+Z0+1)+ell+tau+32,
    Kcode=64(G+K+S+1)(beta+a)+4096g_beta(beta+a),
    Z=Z0+16K(a+1),
    P_alt=L(C+1)²beta,
    U_alt=P_alt+Kcode+Z,
    W_alt=4Cbeta+Z+64a,
    peak_alt=U_alt+W_alt,
    T_alt=256L(C+1)²beta²+T_transfer.

Identity holds are LC, dense coefficient slots L(C+1)², physical scalar word bits beta, full interface bits H, and emitted bits 3(b+1). The capacity condition controls only R; it does not remove the H terms in W,S,K or generation. Z0 contains fixed input/endpoint/feature and phase descriptors. A complete transfer trace stores at most 16(a+1) bits per READ/WRITE action, including a fixed tuple of endpoints and operation tags, giving the second part of Z. Kcode stores the explicit gate/phase program, its logical register addresses and full-width literal records, as well as the finite primitive library. Unlike the shared main ledger we even allow a separate record per expanded step, making the alternative price intentionally generous.

All actual field addresses fit a. They are fixed circuit/array indices, not source-dependent random pointers. Since beta>=128(p+b+ell+tau+h+16), and log2 G is bounded by ell plus a fixed multiple of log2 beta plus log2(H+R+1)+32, one has a<beta: indeed R<=19(h+1)+b, H<=20(h+2)+8, S<=16n+2048beta+128(H+R+1), and g_beta=1024beta²; substituting into G gives log2 G<ell+6 log2 beta+64, hence a<3ell+tau+6 log2 beta+112<beta for beta>=128(116+1+3+3+10+16). Thus loop-controller arithmetic has no uncharged larger word. The scalar width beta, not the short payload bit width, is charged for every physical register.

The gates use fixed wiring; generated indices and phase scans are explicit. The standard full-word dense multiply-add proof gives the first part of T_alt. The extra T_transfer separately charges physical sweeps/interface handling even if their logical actions already appear among compiled gates. This double payment is allowed and avoids hiding serial erasure inside circuit depth. Four rolling banks plus a working descriptor copy and public controller registers give W_alt. U_alt is simultaneously resident, so the stated peak includes both stored code and active data.

The complete offline alternative generator uses

    A_alt=beta+a+bitlength(U_alt+L+G+1)+ell+b+tau+h+p+64,
    Emit=U_alt+L+G+K+1,
    Tgen_alt=1024(ell+b+tau+p+h+1)²+4096 Emit A_alt²,
    Wgen_alt=64(ell+b+tau+p+h+1)+64 Emit A_alt,
    peakgen_alt=U_alt+Wgen_alt.

It enumerates input binding wires, sixteen triple gates per key, all counter/output primitives, all physical zeroing/transfer sweeps, and each dense matrix coefficient including zeros. It computes place(i) by full integer quotient/remainder on public i,k (section 3), explicitly writes full h+1-bit word layouts and all high zeros, and emits final output reconstruction. Gain's public M,A,R_s literals are generated by shifts/products and stored; no logarithm is needed for a score-zero gain head. Payload bit indices, full physical words and the actual three guarded output fields are all enumerated. At most eight schoolbook A_alt-bit arithmetic/index operations per emitted field fit 4096A_alt², just as in section 9; Emit additionally pays expansion and transfer-trace records. The initial public calculation is bounded by the displayed square term. Keeping all generated data and a conservative 64 A_alt-bit words of scratch per emitted field gives the displayed scratch/peak bounds. Thus there is no free packing conversion, code generation or offline memory.

These formulas specify explicit finite cost for each alternative, not merely O(R+19kappa). They retain h even when h>>kappa, acquisition even when counts/output are exact, the full nineteen-word port even for R=b, physical duplicate erasure, Q-J, guarded writes, addresses, holds, stored code, and both online and generation peaks. They establish the D7 counterconstructions with their correct limited scope.

## 13. Fixed primary mapping and provenance boundaries

Only the three fixed primary sources in the copied bounded map are used for contextual attribution. None supplies a new probabilistic/resource premise; the arithmetic and program arguments above are self-contained.

1. Nicholas J. Higham, *The Accuracy of Floating Point Summation*, SIAM J. Sci. Comput. 14(4), 783-799 (1993), pinned author's copy. PDF pp.2-3 / journal pp.784-785, (1.2),(2.3)-(2.5), and PDF p.6 / journal p.788, (3.6), support the operationwise relative-roundoff/summation-and-cancellation context. They do not prove a discrete integer cut, this source's risk, or architecture separation.
2. Pierre Blanchard, Desmond J. Higham and Nicholas J. Higham, *Accurately Computing the Log-Sum-Exp and Softmax Functions*, MIMS EPrint 2019.16, fixed May 15, 2020 manuscript at the archived /2765/3/ version. Algorithm 3.1, PDF p.7/internal p.6, and Theorem 3.3/(3.6), PDF p.9/internal p.8, concern positive normalization of fixed inputs under the specified arithmetic assumptions without overflow/underflow. They are not results about arbitrary correlated integer maps or this charged finite program.
3. Tim van Erven and Peter Harremoës, *Rényi Divergence and Kullback-Leibler Divergence*, arXiv:1206.2459v2, April 24, 2014. Equations (6)-(7), PDF p.2, give the classical order-two divergence/chi-square identity, and Theorem 30/(52)-(53), PDF p.17, the variational relation. The Jensen/KL bridge is classical background already handled inside C1, not novelty evidence or an unproved resource/statistical input here.

We make no publication-novelty claim, learned-transformer/IEEE/all-layer robustness claim, practical-constant claim, arbitrary-reencoder lower, equal-expenditure claim, or optimized neural advantage claim. In particular the old absolute-noise Dot identities, deterministic periodic histories, and older minimax roots do not enter this proof.

## 14. Evidence handling and reproducible artifacts

The complete operation tables below, the explicit loop/generator descriptions above and the formulas constitute the proof body. No mathematical claim depends on opening the companion code or running its tests. The accompanying Python is an exact-integer semantic interpreter and finite ledger calculator; host-language objects, arbitrary-size arithmetic and garbage collection are not used as the physical cost model.

`c3c4_program_v1.py` preserves the source-stage3 MIX63/shared41 operation text with attribution, implements full product/restoring division, finite coefficients/weights, the actual finite heads, destructive-bank semantic checks, early uniform builder, the ten-stage transfer kernel and an explicit alternative loop IR. `c3c4_ledger_v1.py` gives D6 and the separate complete ledgers above. The bounded new checks cover the changed primitive/closed-box/erasure/kernel/early-builder interfaces, not old unchanged statistical diagnostics. Their results are implementation checks, never a native Fact or PASS verdict.

Complete pinned source bytes, author/version lineage and byte-level hashes are recorded in the companion manifest and source snapshot. The core source hashes are reproduced in Appendix B. Differences from the source implementation are preserved: the old small-N certificate that invoked recovery at max(N,6) is not imported; logs are builder-generated; physical all-bank erasure and full-H kernel are explicit; the seed's exact logical K is kept while physical initialization/duplicate purges/final cleanup receive the separate K+20S+1024 reserve. [Non-scientific operational metadata omitted.] This submission uses exactly the two native predecessors in section 1. Only the gateway's actual verdict can admit this component; a local check does not do so.

## Appendix A. Complete fixed straight-line tables

The interpreter has exact integer CONST/ADD/SUB/SHL/SHR/MUL/DIV/MIN/MAX/EQ/AND/OR/MUX semantics; MUX(s,x,y) returns x for s=1, otherwise y. DIV is floor division with the positive divisors proved in section 5. Each named result is a distinct SSA register until cleanup. In these tables `a,b` are the two query bits (public output precision is encoded only in Q); `e0,e1` are the prefix endpoint bits. The output table register `d` means C0+C1+2, not the public noise exponent. `QA` in the copied source means the present A.

MIX master inputs in fixed order: q10, q11, v10, v11, q20, q21, v20, v21, h0, h1, h00, h01, alpha0, alpha1, nu0, nu1, f0, f1, rho. The two selected output registers are C0,C1. JOINT inputs are j000,j001,j010,j011,j100,j101,j110,j111 and a,b; eleven other returned words are still fully read and cleared. Shared output has inputs C0,C1,a,b and emits out0,out1 plus the separately written literal Q.

### MIX recovery: exactly 63 word operations

| # | destination | instruction and operands |
|---:|---|---|
| 1 | zero | CONST 0 |
| 2 | qa | CONST A |
| 3 | twoqa | SHL qa, 1 |
| 4 | twoM | CONST 2M |
| 5 | U1 | MUX a, v11, v10 |
| 6 | U2 | MUX a, v21, v20 |
| 7 | V | MUX b, nu1, nu0 |
| 8 | alpha | MUX b, alpha1, alpha0 |
| 9 | twov | SHL V, 1 |
| 10 | num1a | ADD qa, V |
| 11 | num1 | MUL twoqa, num1a |
| 12 | den1 | SUB twoqa, U1 |
| 13 | D1 | DIV num1, den1 |
| 14 | num2a | ADD qa, twov |
| 15 | num2 | MUL twoqa, num2a |
| 16 | den2 | SUB twoqa, U2 |
| 17 | D2 | DIV num2, den2 |
| 18 | DT | ADD qa, alpha |
| 19 | matchE0 | EQ e0, b |
| 20 | PH0full0 | MUL DT, h00 |
| 21 | PH00 | DIV PH0full0, qa |
| 22 | PHfull0 | MUL DT, h0 |
| 23 | PH0 | DIV PHfull0, qa |
| 24 | PQ1full0 | MUL D1, q10 |
| 25 | PQ10 | DIV PQ1full0, qa |
| 26 | PQ2full0 | MUL D2, q20 |
| 27 | PQ20 | DIV PQ2full0, qa |
| 28 | I0 | SUB PH00, f0 |
| 29 | base0 | SUB PH0, nu0 |
| 30 | matchE10 | EQ e1, 0 |
| 31 | J0 | AND matchE0, matchE10 |
| 32 | boundary0 | MUX J0, rho, zero |
| 33 | gplus0 | ADD base0, boundary0 |
| 34 | g0 | SUB gplus0, I0 |
| 35 | diff0 | SUB PQ20, PQ10 |
| 36 | H0 | SUB diff0, g0 |
| 37 | lower0 | MAX H0, zero |
| 38 | A0 | MIN lower0, qa |
| 39 | snapfull0 | MUL twoM, A0 |
| 40 | snapnum0 | ADD snapfull0, qa |
| 41 | C0 | DIV snapnum0, twoqa |
| 42 | PH0full1 | MUL DT, h01 |
| 43 | PH01 | DIV PH0full1, qa |
| 44 | PHfull1 | MUL DT, h1 |
| 45 | PH1 | DIV PHfull1, qa |
| 46 | PQ1full1 | MUL D1, q11 |
| 47 | PQ11 | DIV PQ1full1, qa |
| 48 | PQ2full1 | MUL D2, q21 |
| 49 | PQ21 | DIV PQ2full1, qa |
| 50 | I1 | SUB PH01, f1 |
| 51 | base1 | SUB PH1, nu1 |
| 52 | matchE11 | EQ e1, 1 |
| 53 | J1 | AND matchE0, matchE11 |
| 54 | boundary1 | MUX J1, rho, zero |
| 55 | gplus1 | ADD base1, boundary1 |
| 56 | g1 | SUB gplus1, I1 |
| 57 | diff1 | SUB PQ21, PQ11 |
| 58 | H1 | SUB diff1, g1 |
| 59 | lower1 | MAX H1, zero |
| 60 | A1 | MIN lower1, qa |
| 61 | snapfull1 | MUL twoM, A1 |
| 62 | snapnum1 | ADD snapfull1, qa |
| 63 | C1 | DIV snapnum1, twoqa |

### JOINT selection/snapping: 15 word operations plus two control ORs, bounded by 18

| # | destination | instruction and operands |
|---:|---|---|
| 1 | left0 | MUX b, j010, j000 |
| 2 | right0 | MUX b, j110, j100 |
| 3 | selected0 | MUX a, right0, left0 |
| 4 | left1 | MUX b, j011, j001 |
| 5 | right1 | MUX b, j111, j101 |
| 6 | selected1 | MUX a, right1, left1 |
| 7 | qa | CONST A |
| 8 | twoqa | SHL qa, 1 |
| 9 | twoM | CONST 2M |
| 10 | full0 | MUL twoM, selected0 |
| 11 | num0 | ADD full0, qa |
| 12 | C0 | DIV num0, twoqa |
| 13 | full1 | MUL twoM, selected1 |
| 14 | num1 | ADD full1, qa |
| 15 | C1 | DIV num1, twoqa |

### Shared output: exactly 41 word operations

| # | destination | instruction and operands |
|---:|---|---|
| 1 | zero | CONST 0 |
| 2 | one | CONST 1 |
| 3 | two | CONST 2 |
| 4 | Q | CONST Q=2^b_public |
| 5 | U | SHR Q, 1 |
| 6 | publicUniform | CONST I{b_public=1} (N>=6) |
| 7 | D | ADD C0, C1 |
| 8 | d | ADD D, two |
| 9 | twod | SHL d, 1 |
| 10 | threed | ADD twod, d |
| 11 | Z | SHL d, 2 |
| 12 | twoZ | SHL Z, 1 |
| 13 | twoQ | SHL Q, 1 |
| 14 | c1plus | ADD C1, one |
| 15 | raw1 | SHL c1plus, 2 |
| 16 | lower1 | MAX d, raw1 |
| 17 | z1 | MIN threed, lower1 |
| 18 | nearfull | MUL twoQ, z1 |
| 19 | nearnum | ADD nearfull, Z |
| 20 | J | DIV nearnum, twoZ |
| 21 | near0 | SUB Q, J |
| 22 | c0plus | ADD C0, one |
| 23 | raw0 | SHL c0plus, 2 |
| 24 | z0ceil | MIN threed, raw0 |
| 25 | z1ceil | SUB Z, z0ceil |
| 26 | Qminus | SUB Q, one |
| 27 | Zminus | SUB Z, one |
| 28 | ceilfull0 | MUL Qminus, z0ceil |
| 29 | ceilnum0 | ADD ceilfull0, Zminus |
| 30 | k0 | DIV ceilnum0, Z |
| 31 | ceilfull1 | MUL Qminus, z1ceil |
| 32 | ceilnum1 | ADD ceilfull1, Zminus |
| 33 | k1 | DIV ceilnum1, Z |
| 34 | ksum | ADD k0, k1 |
| 35 | residual | SUB Q, ksum |
| 36 | ceil1 | ADD k1, residual |
| 37 | selected0 | MUX a, k0, near0 |
| 38 | selected1 | MUX a, ceil1, J |
| 39 | uniform | OR publicUniform, b |
| 40 | out0 | MUX uniform, U, selected0 |
| 41 | out1 | MUX uniform, U, selected1 |

Control extraction is a=ctl[2] OR ctl[3], b=ctl[1] OR ctl[3], e0=ctl[6] OR ctl[7], e1=ctl[5] OR ctl[7], with zero-based indices. JOINT needs only the first two ORs; MIX needs all four, paid within extraction. The primitive library implements every instruction, including the two signed H subtractions and all full-product divisions. At N<6 none of these tables is built or executed.

## Appendix B. Full-byte source identity and attribution

* `PROBLEM.md` — current project contract; 23007 bytes; SHA256 `34f29e9aa714e81bbd9c92408930d0ce38c051f92f42e1e9ebf7f8158b5a8fab`.
* `inputs/STAGE_DEFINITIONS.md` — current D1-D8; 16936 bytes; SHA256 `1648c98212f71be946dfc8b39ab54497fbad41649bbe3fedc03296c401b8c0ca`.
* `inputs/CONTROLLER_C3C4_PACKING_SEED.md` — responsibility controller, logical transfer seed; 5448 bytes; SHA256 `222ced93b60c7d04720f25577d3dd5a197ac970f2ab14432e9a0aeaa7b3944de`.
* `inputs/CONTROLLER_RUNTIME_NOTE.md` — responsibility controller, runtime/audit instructions; 1007 bytes; SHA256 `1d2f1c59783c277780a887ac7a1270d99281ce4194850184599ae86f54e445bf`.
* `outputs/001-relative-code/lead/admission-and-resource-interface-v1.md` — Lead stage4, native admission/interface; 8579 bytes; SHA256 `b8fb69dd269ae5f0bfc4dabdd189a16254f7bbad9af4833cc3100944d7df7ed8`.
* `outputs/001-relative-code/lead/mathematical-checkpoint-v1.md` — Lead stage4, fixed checkpoint; 20695 bytes; SHA256 `df163b669169b0d59eb28d643b204e76e730dab6795da73e668ab22a27baa564`.
* `outputs/001-relative-code/lead/checkpoint-manifest-v1.json` — Lead stage4, source manifest; 4368 bytes; SHA256 `74dffab4c716bd109dd6e5ce0a8af135c7d863d672a77ef2bb5acd8fc4af6c64`.
* `outputs/001-relative-code/verifier/checkpoint-review-v1.md` — Verifier stage4, bounded discussion, not Fact; 16444 bytes; SHA256 `401e78c99f38d2f9f25311707f5c27bf7791fea44ef986177f8d12695d2d04f9`.
* `outputs/001-relative-code/prover/c1-proof-v2.md` — Prover stage4, accepted C1 local bytes; 44213 bytes; SHA256 `f8f6a56b4b458ff3d0033fa8cd29d27e3e32067dd643c2a9e51ba411ed6dadcf`.
* `outputs/001-relative-code/counter/c2-proof-v1.md` — Counter stage4, accepted C2 local bytes; 22150 bytes; SHA256 `4fd828ae9a535b297134f8f513955e0cbb9cb0225eb25d081df5b101c9e8887e`.
* `inputs/source-stage3/outputs/001-conditional-grid/prover/c3-proof-v1.md` — Prover stage3, primitive/program source only; 58094 bytes; SHA256 `68dcb797dfe0e2103d2f35034311efa97d9ae496dedf4eafc67c600b34a8679c`.
* `inputs/source-stage3/outputs/001-conditional-grid/prover/c3_word_program_v1.py` — Prover stage3, fixed MIX63/shared41 definitions; 12473 bytes; SHA256 `187f81b8da04a20412c07dc2fdfbe7387836484e2bc57e873a0dd8045b785a56`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/cost-ledger-v1.md` — Counter010, joint/cost construction source; 17539 bytes; SHA256 `fe3807a72a4d2cbc12d7518296ae5f5d951f43aa9852ebd391bfb5733b1332ec`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/joint_port_cost_v1.py` — Counter010, finite cost implementation source; 7721 bytes; SHA256 `e2896e22217a6ecab58d08d362e36abacfdf700898e2824231ea67c5f441f7de`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/lead/common_budget_risk_gap_v1.py` — Lead010, explicit common-vector calculator source; 7321 bytes; SHA256 `3869642ae43f29d25990ecb89af19c5d936b79e6b5333f5f42c7996051db9b37`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/lead/common-budget-risk-gap-v1.md` — Lead010, comparison and corrected-expression lineage; 14174 bytes; SHA256 `6815c773851eff90863df3d85edb75471bbe46fa7ca35ef63c8b88974418833b`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/sources/primary-map-v1.json` — Counter010 bounded claim map; 3415 bytes; SHA256 `9666ac99f68373d87c7f45c3f343c5edc9ec4d727b6fb3787132e7f0866e2b2d`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/sources/higham-1993-summation.pdf` — Nicholas J. Higham, 1993 pinned primary; 2089150 bytes; SHA256 `2b8ce0e34cbededa56096c1896df2714f9e00c99bdde7fe9a880d7a29db57a8b`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/sources/higham-1993-summation.txt` — pinned extraction of Higham1993; 41857 bytes; SHA256 `ddc40966e6ca76d3a08a64a5e969052af0af7753b1f816c85146d83aef405e4d`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/sources/blanchard-higham-higham-lse-softmax.pdf` — Blanchard/D.J.Higham/N.J.Higham, fixed May2020 primary; 634671 bytes; SHA256 `8c079ad2fd71e1ec7c2cae149ac48dd2c079eda7900095deaad59f244f99ab0a`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/sources/blanchard-higham-higham-lse-softmax.txt` — pinned extraction of fixed BHH primary; 42044 bytes; SHA256 `9c1eaae6ae315a3e71c486a124addea8c5146cfd91ff75c8b838b56fc800c77c`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/sources/van-erven-harremoes-1206.2459v2.pdf` — van Erven/Harremoes, arXiv v2 primary; 994194 bytes; SHA256 `f59d9ba87db4099093f313d6309f8ab68925cb8638d8acbc1d5fcd87d4b5bb27`.
* `inputs/source-stage3/outputs/010-relative-noise-probe/counter/sources/van-erven-harremoes-1206.2459v2.txt` — pinned extraction of arXiv v2 primary; 114762 bytes; SHA256 `1d062988666f95bf05eb69385457cc26291e38d40e74409d3dc7e94751009bd5`.

The C1/C2 canonical evidence-content hashes are respectively `5038dd6457fb762e181e606ab9131e389c8831fe3919511dee51b8a69edb7e25` and `0904b8be7898b9723a11c8c87b11231fb48a63e05661a11d94918937e0611ba8`. They identify gateway content and are not the local file-byte hashes above. Neither historical source hashes nor the checkpoint review are extra predecessors.
