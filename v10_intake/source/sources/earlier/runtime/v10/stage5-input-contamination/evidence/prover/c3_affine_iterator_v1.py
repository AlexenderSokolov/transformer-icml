"""C3 new primitive/renderer splice, standalone finite transcription.

Python is a specification/check runner, never the cost model. The accompanying
proof supplies universal step, space and full-generator bounds. No old module
or diagnostic is imported. Gate operands are public register indices.
"""
from dataclasses import dataclass
from itertools import product
import hashlib
import json
from pathlib import Path


@dataclass(frozen=True)
class Gate:
    op: str
    args: tuple
    dst: int


def bit_value(op, v):
    if op == 'AND': return v[0] & v[1]
    if op == 'OR': return v[0] | v[1]
    if op == 'XOR': return v[0] ^ v[1]
    if op == 'NAND': return 1 - (v[0] & v[1])
    if op == 'NOT': return 1-v[0]
    if op == 'COPY': return v[0]
    if op == 'CONST0': return 0
    if op == 'CONST1': return 1
    if op == 'MUX': return v[1] if v[0] else v[2]
    raise ValueError(op)


def row_terms(g, phase, row, W):
    """Literal sparse row description; equal column indices are not merged here."""
    s0, s1 = W-2, W-1
    assert g.dst < s0 and all(0 <= i < s0 for i in g.args)
    if row == W: return ((W, 1),)  # stored affine convention, not a live cell
    if phase == 0:
        if row not in (s0, s1): return ((row, 1),)
        if g.op in ('AND', 'OR', 'XOR', 'NAND'):
            return ((g.args[0], 1), (g.args[1], 1), (W, -1)) if row == s0 else ()
        if g.op == 'MUX':
            c, x, y = g.args
            return ((c, 1), (x, 1), (W, -1)) if row == s0 else ((y, 1), (c, -1))
        return ()
    if row in (s0, s1): return ()
    if row != g.dst: return ((row, 1),)
    if g.op == 'AND': return ((s0, 1),)
    if g.op == 'OR': return ((g.args[0], 1), (g.args[1], 1), (s0, -1))
    if g.op == 'XOR': return ((g.args[0], 1), (g.args[1], 1), (s0, -2))
    if g.op == 'NAND': return ((W, 1), (s0, -1))
    if g.op == 'MUX': return ((s0, 1), (s1, 1))
    if g.op == 'NOT': return ((W, 1), (g.args[0], -1))
    if g.op == 'COPY': return ((g.args[0], 1),)
    return ((W, 1),) if g.op == 'CONST1' else ()


def coefficient(g, phase, row, column, W):
    return sum(v for c, v in row_terms(g, phase, row, W) if c == column)


def coefficient_bits(gates, W, beta):
    """Gate -> phase -> row -> column -> signed encoding bit, zeros included.

    Six bounded counters: gate macro supplies one current descriptor; the
    remaining five levels are explicit. A negative coefficient uses two's
    complement beta-bit encoding. Decoding is signed before exact MAC.
    """
    for g in gates:
        for phase in range(2):
            for row in range(W+1):
                terms = row_terms(g, phase, row, W)
                for col in range(W+1):
                    c = sum(v for j, v in terms if j == col)
                    assert -2 <= c <= 2
                    encoded = c if c >= 0 else (1 << beta)+c
                    for bit in range(beta):
                        yield (encoded >> bit) & 1


def clear(start, length):
    for i in range(length): yield Gate('CONST0', (), start+i)


def add_gate_iterator(x, y, dst, width, scratch):
    """In-place-safe ripple ADD, full carry at scratch+5 until final clear."""
    t, u, v, carry, nxt, final = range(scratch, scratch+6)
    yield Gate('CONST0', (), carry)
    for i in range(width):
        yield Gate('XOR', (x+i, y+i), t)
        yield Gate('AND', (x+i, y+i), u)
        yield Gate('AND', (carry, t), v)
        yield Gate('XOR', (t, carry), dst+i)
        yield Gate('OR', (u, v), nxt)
        yield Gate('COPY', (nxt,), carry)
    yield Gate('COPY', (carry,), final)
    # For this unsigned primitive the caller separately proves a safe cast.
    yield from clear(scratch, 6)


def sub_gate_iterator(x, y, dst, width, scratch, borrow_dst):
    t, nx, nt, u, v, borrow, nxt = range(scratch, scratch+7)
    yield Gate('CONST0', (), borrow)
    for i in range(width):
        yield Gate('XOR', (x+i, y+i), t)
        yield Gate('NOT', (x+i,), nx)
        yield Gate('AND', (nx, y+i), u)
        yield Gate('NOT', (t,), nt)
        yield Gate('AND', (nt, borrow), v)
        yield Gate('XOR', (t, borrow), dst+i)
        yield Gate('OR', (u, v), nxt)
        yield Gate('COPY', (nxt,), borrow)
    yield Gate('COPY', (borrow,), borrow_dst)
    yield from clear(scratch, 7)


def mul_iterator(w):
    """Inputs [0,w),[w,2w); complete product [2w,4w)."""
    out, addend, scratch = 2*w, 4*w, 6*w
    yield from clear(out, 2*w)
    for j in range(w):
        for i in range(2*w):
            if j <= i < j+w:
                yield Gate('AND', (i-j, w+j), addend+i)
            else:
                yield Gate('CONST0', (), addend+i)
        yield from add_gate_iterator(out, addend, out, 2*w, scratch)
    yield from clear(addend, 2*w+6)


def div_iterator(w):
    """Numerator [0,2w), positive divisor [2w,3w), full quotient [3w,5w).

    A (w+1)-bit shifted remainder and full-width subtraction are retained.
    Old numerator and divisor remain intact. All temporary registers clear.
    """
    q, rem, diff, den = 3*w, 5*w, 6*w+1, 7*w+2
    scratch, borrow, take = 8*w+3, 8*w+10, 8*w+11
    yield from clear(q, 2*w)
    yield from clear(rem, w+1)
    for i in range(w): yield Gate('COPY', (2*w+i,), den+i)
    yield Gate('CONST0', (), den+w)
    for j in range(2*w-1, -1, -1):
        for i in range(w, 0, -1): yield Gate('COPY', (rem+i-1,), rem+i)
        yield Gate('COPY', (j,), rem)
        yield from sub_gate_iterator(rem, den, diff, w+1, scratch, borrow)
        yield Gate('NOT', (borrow,), take)
        for i in range(w+1): yield Gate('MUX', (take, diff+i, rem+i), rem+i)
        yield Gate('COPY', (take,), q+j)
    yield from clear(rem, 3*w+12)


def word(bits, start, width):
    return sum(bits[start+i] << i for i in range(width))


def put(bits, start, width, value):
    for i in range(width): bits[start+i]=(value >> i) & 1


def execute(gates, bits):
    for g in gates: bits[g.dst]=bit_value(g.op, [bits[a] for a in g.args])
    return bits


def dense_execute_gate(g, state, W):
    """Test the COMPLETE dense matrix at every entry, including held zeros."""
    v=list(state)+[1]
    for ph in range(2):
        v=[max(0, sum(coefficient(g, ph, r, c, W)*v[c]
                       for c in range(W+1))) for r in range(W+1)]
    assert v[-1] == 1
    return v[:-1]


def checks():
    # New splice checks, not the seed's exhaustive isolated-gate alias suite.
    tests=0
    maximum={}
    for w in (2, 3, 5):
        mg=list(mul_iterator(w)); dg=list(div_iterator(w))
        maximum[str(w)]={'multiply_gates':len(mg),'divide_gates':len(dg),
                         'max_register':max(g.dst for g in mg+dg)}
        assert len(mg) <= 64*w*w+64*w
        assert len(dg) <= 256*w*w+128*w
        # Extremal products plus deterministic varied inputs.
        pairs={(0,0),(0,(1<<w)-1),((1<<w)-1,(1<<w)-1)}
        pairs.update((i % (1<<w),(7*i+3) % (1<<w)) for i in range(16))
        for x,y in sorted(pairs):
            v=[1]*(32*w+32);put(v,0,w,x);put(v,w,w,y)
            execute(mg,v)
            assert word(v,2*w,2*w)==x*y
            assert not any(v[4*w:6*w+6])
            tests+=1
        cases={(0,1),((1<<(2*w))-1,1),((1<<(2*w))-1,(1<<w)-1)}
        cases.update(((17*i+5) % (1<<(2*w)),1+i % ((1<<w)-1)) for i in range(24))
        for num,den in sorted(cases):
            v=[1]*(32*w+32);put(v,0,2*w,num);put(v,2*w,w,den)
            execute(dg,v)
            assert word(v,3*w,2*w)==num//den
            assert not any(v[5*w:8*w+12])
            tests+=1
    # Entire in-place multiply and full restoring-division trajectories through
    # literal dense matrices: catches primitive aliases -> renderer handoff.
    dense_gates=0
    W=40; w=2
    for kind,gates,num,den in [('MUL',list(mul_iterator(w)),3,3),
                              ('DIV',list(div_iterator(w)),15,2)]:
        v=[0]*W
        if kind=='MUL': put(v,0,w,num);put(v,w,w,den)
        else:put(v,0,2*w,num);put(v,2*w,w,den)
        v[-2:]=[5,7]  # renderer scratch cannot assume old zero values
        for g in gates:
            expect=v.copy();expect[g.dst]=bit_value(g.op,[v[a] for a in g.args])
            expect[-2:]=[0,0]
            v=dense_execute_gate(g,v,W)
            assert v==expect
            dense_gates+=1
        assert word(v,2*w if kind=='MUL' else 3*w,2*w)==(num*den if kind=='MUL' else num//den)
    # Bit emitter colliding columns are summed before signed encoding. Decode
    # every emitted coefficient, not just the nonzero locations.
    W=6;beta=8;g=Gate('XOR',(1,1),1)
    stream=list(coefficient_bits([g],W,beta))
    assert len(stream)==2*(W+1)**2*beta
    off=0
    for ph,r,c in product(range(2),range(W+1),range(W+1)):
        encoded=sum(stream[off+i]<<i for i in range(beta));off+=beta
        signed=encoded-(1<<beta) if encoded & (1<<(beta-1)) else encoded
        assert signed==coefficient(g,ph,r,c,W)
    return {'status':'PASS_NEW_SPLICE_CHECKS_ONLY','primitive_cases':tests,
            'full_dense_gate_transitions':dense_gates,'emitted_coefficient_bits':len(stream),
            'counts':maximum,'old_diagnostics_run':False,'admission':False}


if __name__=='__main__':
    target=Path(__file__).with_name('c3-splice-check-results-v1.json')
    if target.exists(): raise SystemExit('Fixed results exist; do not rerun unchanged checks.')
    result=checks()
    result['program_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
