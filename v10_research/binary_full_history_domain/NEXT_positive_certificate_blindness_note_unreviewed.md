# Parked next-question note: AB001's clean family has a positive certificate

2026-11-02. UNREVIEWED scope refinement, not a new theorem, not part of AF001, and not an accepted proof dependency. Root requested that it be parked rather than launched as another standalone result. The next assigned priority is robust companding/packing of the balanced sufficient statistics, not additional narrow certificate variants.

## Actual derivation

Read the accepted AB001 family without changing its bytes. For M>=64, r=1/(2M), a in[1/M,1/4], write e=1-a, b=r e/a and tau=r. Its stationary law is(e/2,a/2,a/2,e/2), and its pair square is

    [e²,       ea,       a(1-b),   r e]
    [(1-b)e,   (1-b)a,   b r,      b(1-r)]
    [e²,       ea,       a(1-b),   r e]
    [r e,      r a,      (1-r)r,   (1-r)²].

Dividing each column by the corresponding stationary mass, the potentially smallest entries are exactly

    2r=1/M,
    2br/a=2r²(1-a)/a².

All others are at least2r: b<=1/2, e>=3/4, a<=1/4 and r<=1/128 suffice directly. The displayed small values actually occur, so the exact maximal two-step coefficient for this family is

    beta_*(a)=min{2r,2r²(1-a)/a²}.

The second expression decreases over the a interval and is24r²=6/M² at a=1/4. Because M>=64, 2r>=6/M². Hence the whole clean family appears to lie in D_2(6/M²), not merely D_2(0), as the accepted AB001 statement conservatively claimed.

If independently checked, its same-map lower could therefore be relabeled at the positive clean certificate1/M² (or6/M²), while retaining its null at1/M. The contradiction still uses only clean risk at actual k=0 and the null's smaller attacked benchmark. Thus the necessity of supplied beta could be illustrated using two strictly positive certificate labels. No estimator or adversary would receive the hidden source table.

## Provenance and limitations

The accepted AB001 proof is binary_budget_adaptation/AB001_joint_blindness_obstruction.md, SHA865b65e296c39c632aa619c1d2588ad8b9d221efd6e8d799c8b15814b40a1e3d. Its claim that no positive certificate was asserted remains unchanged historical text. This note arose only after AF001's frozen proof; AF001 uses the already accepted beta0/1/M example and does not rely on this refinement.

No fresh full independent review or exact diagnostic was commissioned for this note. The all-sixteen partition, precise class relabeling and resulting consequence would need that process before acceptance. This does not classify arbitrary beta-blind public domains, change AF001, or create a new publication claim. It is preserved solely as a possible future question; no further variant is launched in this phase.
