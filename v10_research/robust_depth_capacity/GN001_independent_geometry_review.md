# GN001 independent geometry review

2026-11-02. Reviewer task: adversarial check of the shifted/clipped recursive map, independently of the author's eventual theorem. Read RG001 as background only; no RG001 file was edited. **Geometry PASS**, conditional on the explicit construction below. This is not a review of FA arithmetic, statistical quantifiers, or the final complete GN001 statement.

## 1. Exact phase calculation (including the final endpoint)

Let N=2^k with k>=1, j>=2, L=N^(j-1), eta=1/(2L+2). Let W_k(x)=T^(k-1)(T_ext(x)), where T_ext(x)=2x−4relu(x−1/2)+4relu(x−1). The first tent is extended, not every subsequent tent. The input lies in [0,1+eta/(2N)]. Its first output lies in [0,1], so all subsequent ordinary tents are valid.

For t=(i+r)/N, i=0,...,N−1 and 0<=r<=1, write

    u(t)=clip((W_k(t+eta/(2N))−eta/2)/(1−eta),0,1).

The standard triangular-wave identity, extended across t=1 by T_ext, gives exactly

    u((i+r)/N) = r/(1−eta)            if i even and r<=1−eta;
                 1−r/(1−eta)         if i odd and r<=1−eta;
                 1                  if i even and r>=1−eta;
                 0                  if i odd and r>=1−eta.

For clarity, the triangle turns at r=1−eta/2, not 1−eta; clipping creates the earlier endpoint arrival. Across the triangle turn and until r=1 its value stays inside the region clipped to the same endpoint. At a row boundary the two formulas agree. At t=1, N is even, the last row is odd, and u(1)=0. There is no initial flat segment.

Keep the RP/RG staircase with amplification L. The exact phase identity is

    S((i+r)/N)=i/N                         for r<=1−eta;
               i/N+(r−1+eta)/(N eta)      for r>=1−eta.

Thus during u's entire flat portion S is strictly moving; during S's flat portion u is strictly moving. Their junction has no time interval of stationarity.

## 2. Inductive simplicity and absence of stationary plateaus

Set P_1(t)=t and P_j(t)=(P_(j−1)(u_j(t)),S_j(t)). Suppose P_(j−1) traces its ordered simple edge list injectively over [0,1]. In each plane x_j=i/N the new map traverses precisely one full copy, forward for i even and backward for i odd. It then traverses a connector of length 1/N in the new coordinate. There is no copy at x_j=1. The copy occupies [(i)/N,(i+1−eta)/N], with no omitted initial subinterval; the connector occupies [(i+1−eta)/N,(i+1)/N]. These intervals tile [0,1] and have positive lengths. Recursive child intervals also tile their copy. Hence all affine edge intervals tile [0,1] without gaps; no stationary interval exists at any level.

Every new copy lies in a distinct plane. A connector touches a neighboring copy only at that copy's prescribed endpoint. Adjacent connectors have different anchors: the two child endpoints are (0,...,0) and (0,...,0,1), at distance 1. Other connectors have disjoint nonadjacent outer-coordinate intervals. Consequently the edge list has no repeated vertex or nonlocal edge contact. Each vertex has one parameter preimage, including t=0 and t=1. This proves global injectivity, not just absence of constant intervals.

## 3. Separation and local inverse

Every geometric vertex belongs to the N-grid; every edge is axis aligned and has length at least 1/N. Nonincident edges in one copy inherit separation >=1/N. Edges in distinct copy planes have this separation in the new coordinate. Connectors with nonadjacent outer intervals are likewise separated; adjacent connectors have anchors distance 1. A connector versus a copy outside its two neighboring planes is separated in the outer coordinate. Inside either neighboring plane, any nonincident child edge is >=1/N from the connector anchor: an axis-aligned grid segment not containing a given grid vertex has distance >=1/N from it, and simplicity excludes containment. This completes the induction. Incident successive edges are perpendicular (including a reversed copy's endpoint edge and its new-axis connector).

Let v_j be the minimum positive speed. Copy speeds are multiplied by N/(1−eta_j), and connector speed is 1/eta_j=2N^(j−1)+2. Thus

    v_1=1,  v_j>=min{N v_(j−1)/(1−eta_j),1/eta_j}>=N^(j−1).

At vertices a two-sided derivative need not exist; this is irrelevant. For any s,t with delta=||P_J(s)−P_J(t)||_2<1/N, containing edges must be equal or incident, since every pair of nonincident edges is separated by at least 1/N. The unique connecting subpath consists of one straight segment or two perpendicular partial segments. Its arclength is <=sqrt(2) delta. Integrating inverse speeds on this subpath (with zero-duration vertices) gives

    |s−t| <= sqrt(2) delta / N^(J−1).

This holds also at shared vertices and global endpoints. At delta=0 injectivity gives s=t. **No additive N^(−J) plateau term is needed.** Strict delta<1/N is important; the proof does not claim this local statement beyond the separation scale.

## 4. Exact independent finite diagnostics

`GN001_independent_geometry.py` independently implements both the ReLU/tent formula and recursively generated rational edge/time tables using Python Fraction. Executed successfully; JSON output is `GN001_independent_geometry.json`.

Ten cases cover N=2,4,8,16 and dimensions 2 through 5 (not every combination). Checks include shifted phase identities and staircase phases at regular rational points and critical eta points, t=0/1, formula-vs-edge-table agreement at endpoints/interiors, positive duration and full interval tiling, unique vertices, axis alignment, perpendicular incidents, exact minimum-speed inequality, all pairs of nonincident edges, and squared local-inverse inequality for sampled incident-edge points. These finite tests corroborate rather than replace the preceding general proof.

No counterexample was found. A downstream arithmetic proof must not treat the new eta-dependent coefficients as dyadic/exact: the geometric construction is rational, and its finite evaluator needs a paid approximation certificate. This review does not authorize reusing RG001's special dyadic exact-arithmetic argument.
