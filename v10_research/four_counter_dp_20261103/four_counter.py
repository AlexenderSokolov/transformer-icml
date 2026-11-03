"""Exact minimum-edit selected-row count bank for the pilot's half pooling."""
from itertools import product


def _validate(h, k):
    h = tuple(h); m = len(h) - 2
    if m < 2 or any(x not in (0, 1) for x in h):
        raise ValueError('half pooling requires a binary word with M >= 2')
    if not isinstance(k, int) or not 0 <= k <= m:
        raise ValueError('require integer 0 <= k <= M')
    return h, m


def feature_bank(z):
    """(J,C1,D,E), with successor 1 (not 1-first(u))."""
    z = tuple(z); m = len(z)-2; l = m//2; u = z[-2:]
    if m < 2 or any(x not in (0,1) for x in z):
        raise ValueError('invalid word')
    J = C = D = E = 0
    for i in range(m):
        if z[i:i+2] == u:
            J += 1; C += z[i+2]
            if i < l:
                D += 1; E += z[i+2]
    return J, C, D, E


def model_inputs(m, terminal, bank):
    """Order exactly matches Model.forward: six flattened rails, terminal, 1/M."""
    J, C, D, E = bank; l = m//2; r = m-l
    return ((J-C)/m, C/m, (D-E)/l, E/l,
            (J-D-C+E)/r, (C-E)/r, *terminal, 1/m)


def solve_banks(h, k, witnesses=False):
    """Map every reachable bank to minimum edit cost (and optionally witness)."""
    h, m = _validate(h, k); l = m//2; u = h[-2:]
    # Key = current two symbols, four counters. Values = least cost.
    layer = {}
    for a,b in product((0,1), repeat=2):
        cost=(a != h[0])+(b != h[1])
        if cost <= k: layer[(a,b,0,0,0,0)] = cost
    parents = []
    for t in range(2,m+2):
        nxt = {}; par = {}; i = t-2
        for state, cost in layer.items():
            a,b,J,C,D,E = state
            for c in ((0,1) if t < m else (h[t],)):
                newcost = cost + (c != h[t])
                if newcost > k: continue
                selected = (a,b) == u
                first = selected and i < l
                key = (b,c,J+selected,C+selected*c,D+first,E+first*c)
                if key not in nxt or newcost < nxt[key]:
                    nxt[key] = newcost; par[key] = (state,c)
        layer = nxt
        if witnesses: parents.append(par)
    banks = {}
    for state,cost in layer.items():
        bank = state[2:]
        if bank not in banks or cost < banks[bank][0]: banks[bank]=(cost,state)
    if not witnesses: return {bank: item[0] for bank,item in banks.items()}
    result = {}
    for bank,(cost,state) in banks.items():
        chars=[]
        for par in reversed(parents):
            state,c = par[state]; chars.append(c)
        result[bank]=(cost, tuple(state[:2])+tuple(reversed(chars)))
    return result


def maximize(h, k, utility):
    """Return value, minimizing-cost witness, bank. Utility must compare exactly."""
    h,m = _validate(h,k)
    banks=solve_banks(h,k,witnesses=True)
    bank=max(banks, key=lambda b: utility(model_inputs(m,h[-2:],b)))
    return utility(model_inputs(m,h[-2:],bank)), banks[bank][1], bank
