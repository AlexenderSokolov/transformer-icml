# Universal binary cross-excursion inequalities

2026-11-02. Author observation; not an optimal-risk theorem.

For any stationary homogeneous binary second-order source write

    a=theta_00(1), b=theta_01(1),
    e=theta_10(0), t=theta_11(0),
    y=Pi00, x=Pi01=Pi10, w=Pi11.

Stationarity gives ya=xe and wt=xb. The equality Pi01=Pi10 follows from stationarity of the one-symbol marginal (or crossing flux). Under all-state P²>=beta Pi, the two special cells are

    P²(10,01)=ea >=beta x,
    P²(01,10)=bt >=beta x.

When x>0 and y>0, substitute a=xe/y and cancel x to get

    e² >= beta y.

When x>0 and w>0, substitute t=xb/w to get

    b² >= beta w.

For y=0 or w=0 the respective inequality is automatic. Thus these inequalities hold whenever x>0. They need not hold when x=0: e or b can then belong to unsupported rows, though all-state certification still imposes other restrictions.

Consequences: when the stationary mass of waiting state00 is at least c>0, every genuine crossing excursion has hazard e>=sqrt(c beta) at state10. A three-symbol first-order construction can reset with hazard O(beta), but an actual binary pair chain of this type cannot. This is broader than the specific BI001 witness: it uses only binary stationarity and the all-state two-step certificate. It does not prove that every informative active run visits10 frequently, nor any matching prediction upper. Those missing claims are essential before identifying sqrt(beta) as the optimal binary precision cutoff.
