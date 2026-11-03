#!/usr/bin/env python3
"""Deterministic exact-rational checkpoint norm/bound extraction; no RNG/model construction."""
import hashlib,json,os,platform,sys
from fractions import Fraction as F
from decimal import Decimal,localcontext,ROUND_CEILING
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SOURCE=ROOT/'v10_research/learned_position_pilot_20261103'
u=F(1,2**53)
def gamma(n):
    assert n*u<1
    return n*u/(1-n*u)
def dec(x):
    with localcontext() as c:
        c.prec=14;c.rounding=ROUND_CEILING
        return str(Decimal(x.numerator)/Decimal(x.denominator))
def exact(x):return F.from_float(float(x))
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def calc(path,M):
    with np.load(path,allow_pickle=False) as z:
        assert str(z['mode'])=='half'
        W=[[exact(y) for y in row] for row in z['W']]
        v=[exact(y) for y in z['v']];b=[exact(y) for y in z['b']];c=exact(z['c'][0])
    assert len(W)==9 and len(W[0])==len(v)==len(b)==32
    assert all(np.isfinite(float(y)) for row in W for y in row) and all(np.isfinite(float(y)) for y in v+b+[c])
    n=[M,M,M//2,M//2,M-M//2,M-M//2]
    d=[u+(1+u)*gamma(x-1) for x in n]+[F(0),F(0),u/F(M)]
    # Given |x_i| <= 1+d_i and |tanh output|<=1+tau.
    coeff=[sum(abs(v[j])*abs(W[i][j]) for j in range(32)) for i in range(9)]
    rail=sum(coeff[i]*d[i] for i in range(9))
    absdot=[sum((1+d[i])*abs(W[i][j]) for i in range(9)) for j in range(32)]
    aff=[gamma(9)*s+u*((1+gamma(9))*s+abs(b[j])) for j,s in enumerate(absdot)]
    affine=sum(abs(v[j])*aff[j] for j in range(32))
    V=sum(abs(y) for y in v)
    output=gamma(32)*V+u*((1+gamma(32))*V+abs(c))
    # coefficient of tau in output-dot rounding; |hhat|<=1+tau.
    tau_coeff=V*(1+gamma(32)+u*(1+gamma(32)))
    return {'M':M,'delta_full':dec(d[0]),'delta_first':dec(d[2]),'delta_second':dec(d[4]),
            'six_rail_lipschitz':dec(sum(coeff[:6])),'ninth_rail_lipschitz':dec(coeff[8]),'v_l1':dec(V),
            'rail_logit_error':dec(rail),'affine_logit_error':dec(affine),
            'output_dot_logit_error_at_tau_zero':dec(output),'logit_error_at_tau_zero':dec(rail+affine+output),
            'tanh_abs_error_coefficient':dec(tau_coeff)}
paths=sorted(SOURCE.glob('*/checkpoints/half_edit_*.npz'))
assert len(paths)==10,paths
out={'scope':'Conditional algebraic upper bounds; NOT backend certification; all rational sums exact and decimals rounded upward',
     'unit_roundoff':'2^-53','numpy':np.__version__,'python':sys.version,'platform':platform.platform(),
     'checkpoints':[]}
for p in paths:
    out['checkpoints'].append({'path':str(p.relative_to(ROOT)),'sha256':h(p),'results':[calc(p,m) for m in (64,128,256,1025)]})
out['input_hashes']={str(p.relative_to(ROOT)):h(p) for p in [SOURCE/'pilot.py',ROOT/'v10_research/float_bank_deterministic_20261103/REPORT.md',ROOT/'v10_research/float_bank_deterministic_20261103/review_independent/REVIEW.md',ROOT/'v10_research/four_counter_dp_20261103/ADDITIVE_CORRECTION.md']}
(OUT/'bounds.json').write_text(json.dumps(out,indent=2)+'\n')
print('CHECKPOINTS',len(paths),'HORIZONS',4)
for x in out['checkpoints']:
 print(x['path'], 'S=',x['results'][0]['six_rail_lipschitz'],'M64=',x['results'][0]['logit_error_at_tau_zero'],'M256=',x['results'][2]['logit_error_at_tau_zero'],'M1025=',x['results'][3]['logit_error_at_tau_zero'])
print('Assertions and JSON write: PASS')
