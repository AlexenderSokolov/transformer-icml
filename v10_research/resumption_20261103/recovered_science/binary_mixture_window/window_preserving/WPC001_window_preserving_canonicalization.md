# WPC001 — Window-preserving loop canonicalization (author candidate)

2026-11-02. New deterministic candidate; not independently reviewed or accepted. No earlier candidate or accepted artifact is modified. No publication or full probabilistic obstruction is claimed.

## Statement and exact indexing

Let X=(X_0,...,X_{M+1}) be binary, with Y_i=(X_i,X_{i+1}), i=0,...,M, Y_0=11 and Y_M=00. Let 2<=r and 2r<=M+2. Put l=r-2 and h=M-r+2. Freeze edges with departure indices i<l or i>=h. Thus the frozen initial path spells exactly the first r symbols, and the frozen final path spells exactly the last r symbols. There are f_total=2r-4 frozen edges. The movable interior consists of edges l,...,h-1 and vertices Y_l,...,Y_h.

Delete only interior 111 and 000 loops. Let A and B be their respective counts, and let S_0,...,S_L be the resulting interior skeleton vertices, retaining every other edge in its original order.

A sufficient condition is:

    there exist p<q with S_p=11 and S_q=00.             (O)

This is equivalent to an 11 visit before a later 00 visit in the original interior path: deleting self-loops cannot remove a distinct-state visit or reverse their order.

Under (O), insert all A copies of the 111 loop at S_p and all B copies of the 000 loop at S_q. Retain the skeleton and frozen paths. Call the resulting word C_r(X). It has the same length, all eight triple counts, both endpoint pairs, and actual first/last-r symbols as X. In particular its windows need not equal the constant windows of any null input.

Write J=J00(X), c=J01(X)+J10(X), with departures i=0,...,M-1, and x^(J)=1^(M+2-J)0^J. Then

    d_H(C_r(X),x^(J)) <= 3c+4r-5 <= 3c+4r.           (1)

For a strict-k attack it suffices that 3c+4r<=k; alternatively check actual distance pointwise. If J>=2 the null input and output both end00, so their entire Hamming distance is on the editable first M symbols. No preservation of null-input windows is required by final-pair protection.

## Minimal condition for this particular relocation scheme

If A>0 and B>0, (O) is necessary and sufficient for placing the entire movable111 block before the entire movable000 block while retaining the interior nonloop skeleton and frozen edges. If A=0 or B=0, no ordering condition is needed: insert the nonempty loop type at any skeleton visit to its state, which necessarily exists because such loops were removed there. If both vanish, use identity. The same bound (1) holds in these degenerate cases by regarding the absent 1 block as occurring at the start or the absent 0 block as occurring at the end.

Failure of (O) with A,B>0 is not a claim that every possible histogram/window-preserving transformation fails; it only blocks this specified retain-nonloops-and-concentrate scheme. Global endpoints11/00 alone do not imply (O) for a truncated interior (see counterexample below).

## Proof of preservation

An edge is the triple X_i X_{i+1} X_{i+2}. Deleting a self-loop keeps the same current pair, and inserting it at a vertex of that pair yields a valid path. The interior length is unchanged after reinserting exactly A+B edges; therefore the frozen suffix still begins at the original absolute index h. The frozen prefix and suffix edges and their endpoint symbols are unchanged, proving exact preservation of the actual first/last-r symbols. Unfrozen boundary-crossing triples need not remain at their original positions; their preservation is only at the aggregate histogram level. Every edge either remains or is reinserted exactly once with its original triple label. Thus the full triple histogram is unchanged. No assertion about interior r-pattern counts is made.

## Hamming lemma for two ordered blocks

Suppose a binary word of length N contains, in order, a distinguished block of A ones and a distinguished block of B zeros. All remaining symbols comprise o ones and z zeros, at arbitrary locations; N=A+B+o+z. Let j=B+q, where q>=0 and j<=N. Then

    d_H(word,1^(N-j)0^j) <= max(z+q, 2o+z-q).       (2)

If at least one distinguished 1 lies after the target cut, all distinguished zeros lie after the cut. Hence the number of zeros before the cut is at most z. Since the word has B+z zeros, the mismatch count equals twice the zeros before the cut plus j-(B+z), giving at most z+q. Otherwise all distinguished ones are before the cut, so ones after the cut number at most o. The alternative mismatch identity is twice these ones plus (B+z)-j, giving at most 2o+z-q. Empty blocks are covered by these same cases or by taking the corresponding case vacuous. The proof uses positions, not assumed contiguity of the remaining symbols.

## Exact count bounds

Let u=N001, v=N011, p=N010, w=N101. Endpoint flow at00 and11 gives

    N100=u+1, N110=v+1,
    c=p+v+u+1+w.                                  (3)

Let f_1 and f_0 be the frozen111 and000 counts. They obey f_1+f_0<=2r-4. After distinguishing the two inserted loop blocks, every remaining 1 is either one of the initial two symbols, the appended symbol of a nonloop edge, or a frozen111 loop. Similarly for remaining zeros. Consequently the exact values are

    o=2+u+v+w+f_1=c+1-p+f_1,
    z=p+u+v+2+f_0=c+1-w+f_0,
    q=J-B=u+f_0.                                  (4)

The last equation uses J=N000+N001 and B=N000-f_0. In particular q>=0. Substitution in (2) gives

    z+q=c+1-w+u+2f_0 <=2c+2f_0,
    2o+z-q=3c+3-2p-w-u+2f_1 <=3c+3+2f_1.

Here u<=c-1 by (3), and c>=1 because a path from11 to00 crosses a mixed state. Since f_i<=2r-4, both bounds are at most 3c+4r-5. This proves (1), with all two-symbol/departure corrections retained.

## Concrete failure of automatic ordering

For M=8, r=4, the word 1100001100 has global endpoints11/00. Its interior vertices at indices2,...,6 are 00,00,00,01,11; it has no interior11-before00. This example only refutes automatic (O); its movable111 count is zero, so the degenerate relocation rule still applies.

For a failure with both movable loop types positive, use X=11000011100, M=9,r=4. Interior vertices at indices2,...,7 are 00,00,00,01,11,11. Here A=1 and B=2, yet no ordered11-before00 visits exist. The frozen final path goes11->10->00. Thus the nondegenerate condition is genuinely additional.

## Scope

This lemma removes the deterministic need for constant clean windows. A separate probabilistic argument must establish an ordered interior visit event under the relevant conditioned clean law and must retain all endpoint/mass/certificate accounting. No such probability bound, all-sublinear-width obstruction, sharp threshold, or full-history statement is established here. The companion enumeration is finite corroboration, not proof or independent review.
