"""Finite singleton/uniform attention evaluator, binary gate readout.

Datapath add/compare/division are bit circuits. Python controls only public
loop schedules, routing, representation input/output, and validation.
No statistical table is passed across prefix's return boundary.
"""
class Bits:
    def __init__(self, width):
        assert width >= 1
        self.w = width
    def enc(self, x):
        assert 0 <= x < (1 << self.w)
        return tuple((x >> i) & 1 for i in range(self.w))
    def val(self, x):
        return sum(b << i for i,b in enumerate(x))
    def mux(self, s, x, y):
        return tuple((s & a) | ((1-s) & b) for a,b in zip(x,y))
    def _add(self, x, y, carry):
        out=[]
        for a,b in zip(x,y):
            v=a^b
            out.append(v^carry)
            carry=(a&b)|(v&carry)
        return tuple(out),carry
    def add(self,x,y):
        return self._add(x,y,0)[0]
    def sub(self,x,y):
        return self._add(x,tuple(1-b for b in y),1)
    def ge(self,x,y):
        return self.sub(x,y)[1]
    def shift(self,x,k):
        assert 0<=k<self.w
        return (0,)*k+x[:self.w-k]
    def div(self,x,y):
        # Total circuit. y=0 returns all-one quotient; caller selects guard.
        rem=(0,)*self.w
        q=[0]*self.w
        for i in range(self.w-1,-1,-1):
            rem=(x[i],)+rem[:-1]
            diff,carry=self.sub(rem,y)
            rem=self.mux(carry,diff,rem)
            q[i]=carry
        return tuple(q),rem


def metadata(M):
    assert M>=1
    n=M+3
    copy1=tuple((t-1 if t>=1 else t,) for t in range(n))
    copy2=tuple((t-2 if t>=2 else t,) for t in range(n))
    # The nonquery rows deliberately use causal singleton self masks.
    # No prefix-normalization output from those rows is used at the cut.
    uniform=tuple((t,) if t<n-1 else tuple(range(2,M+2)) for t in range(n))
    half=tuple(int(2<=t<2+M//2) for t in range(n))
    return (copy1,copy2,uniform),half


def prefix(z,h):
    z=tuple(z)
    assert len(z)>=3 and h>=0 and all(x in (0,1) for x in z)
    M=len(z)-2; n=M+3
    w=(M+3).bit_length()+h+16
    b=Bits(w); Q=1<<h
    masks,half=metadata(M)
    raw=z+(0,)
    l1=tuple(raw[keys[0]] for keys in masks[0])
    l2=tuple(raw[keys[0]] for keys in masks[1])
    values=[]
    for t in range(n):
        rail=[]
        for a in (0,1):
            for c in (0,1):
                row=(1-(l2[t]^a)) & (1-(l1[t]^c))
                rail.extend((row,row & (raw[t]^a),row & half[t]))
        values.append(tuple(rail))
    # Full token batch. Active-key list traversal is the declared sparse-mask
    # evaluator; dense mask scanning is a separately costed representation.
    bank=None
    for t in range(n):
        keys=masks[2][t]
        denom=b.enc(2*len(keys))
        numerators=[]
        for j in range(12):
            acc=b.enc(0)
            for key in keys:
                acc=b.add(acc,b.enc(values[key][j]))
            # nearest dyadic, ties upward: floor((2Q acc+L)/(2L)).
            numerator=b.add(b.shift(acc,h+1),b.enc(len(keys)))
            quotient,_=b.div(numerator,denom)
            numerators.append(b.val(quotient))
        if t==n-1:
            bank=tuple(numerators)
    endpoint=(l2[-1],l1[-1])
    # Only these rails survive the logical cut. All source/feature/accumulator
    # arrays go out of scope. No secure physical RAM sanitization is claimed.
    return {'bank':bank,'endpoint':endpoint,'h':h}


def replace_bank(cut,bank):
    bank=tuple(bank); Q=1<<cut['h']
    assert len(bank)==12 and all(isinstance(x,int) and 0<=x<=Q for x in bank)
    return {'bank':bank,'endpoint':cut['endpoint'],'h':cut['h']}


def readout(cut,r):
    h=cut['h']; assert r>=0
    bank=cut['bank']; endpoint=cut['endpoint']
    assert len(bank)==12 and len(endpoint)==2
    assert all(isinstance(x,int) and 0<=x<=(1<<h) for x in bank)
    assert all(x in (0,1) for x in endpoint)
    b=Bits(h+r+16); zero=b.enc(0); one=b.enc(1)
    # Bit-mux all four rows: no data-dependent bank address is free.
    selected=[zero,zero,zero]
    for a in (0,1):
        for c in (0,1):
            select=(1-(endpoint[0]^a)) & (1-(endpoint[1]^c))
            for j in range(3):
                selected[j]=b.mux(select,b.enc(bank[3*(2*a+c)+j]),selected[j])
    J,C,D=selected
    C=b.mux(b.ge(C,J),J,C); D=b.mux(b.ge(D,J),J,D)
    gate=b.ge(J,one) & b.ge(b.shift(D,9),J)
    safeJ=b.mux(gate,J,one)
    quotient,_=b.div(b.shift(C,r),safeJ)
    quotient=b.mux(gate,quotient,zero)
    complement=b.sub(b.enc(1<<r),quotient)[0]
    # d=1-endpoint[0]; return probabilities of symbols 0,1 as numerators.
    p0=b.mux(endpoint[0],quotient,complement)
    p1=b.mux(endpoint[0],complement,quotient)
    return b.val(p0),b.val(p1)


def evaluate(z,h,r,replacement=None):
    n=len(z)+1
    cut=prefix(z,h)
    if replacement is not None:
        cut=replace_bank(cut,replacement)
    # Public q-type gating clears nonquery input rails. The shared suffix is
    # still executed at every token; only the q output is retained.
    blank={'bank':(0,)*12,'endpoint':(0,0),'h':h}
    output=None
    for t in range(n):
        current=readout(cut if t==n-1 else blank,r)
        if t==n-1: output=current
    return output


def scalar_grid_bits(H,h):
    """Paid ReLU scalar-to-bit circuit, exact only on the declared h-grid.

    Fraction input permits an exact scalar evaluator in the tests. Each max
    below is one ReLU, not an integer floor or host bit-extraction operation.
    The caller guarantees H is a canonical grid scalar in [0,1].
    """
    assert h>=0 and 0<=H<=1
    A=(1<<h)*H
    rails=[0]*(h+1)
    for j in range(h,-1,-1):
        threshold=1<<j
        bit=max(0,A-(threshold-1))-max(0,A-threshold)
        rails[j]=bit
        A=A-threshold*bit
    return tuple(rails)
