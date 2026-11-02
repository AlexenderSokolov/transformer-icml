# Integrated stage4 C3/C4 executable integer semantics, Prover 2026-10-26.
# The Program/MIX63/output41 block below is copied from Prover stage3,
# complete source SHA256 187f81b8da04a20412c07dc2fdfbe7387836484e2bc57e873a0dd8045b785a56.
# The old certificate/small-N padding routine is deliberately not imported.
# Python execution is a semantic check, never a unit-cost resource claim.
"""C3 finite straight-line word programs and conservative resource functions.

All operations are specified in c3-resource-ledger-v1.md. Python is an
integer-semantics interpreter, not a unit-cost machine or gate-count oracle.
No source module is edited; generation and test entrypoints are elsewhere.
"""
from dataclasses import dataclass


@dataclass
class Program:
    inputs: list
    ops: list
    outputs: list

    def add(self, name, opcode, *args):
        self.ops.append((name, opcode, args))
        return name

    def run(self, values):
        env = dict(values)
        for name, op, args in self.ops:
            x = [env[a] if isinstance(a, str) else a for a in args]
            if op == 'CONST': value = x[0]
            elif op == 'ADD': value = x[0]+x[1]
            elif op == 'SUB': value = x[0]-x[1]
            elif op == 'SHL': value = x[0] << x[1]
            elif op == 'SHR': value = x[0] >> x[1]
            elif op == 'MUL': value = x[0]*x[1]
            elif op == 'DIV':
                assert x[0] >= 0 and x[1] > 0
                value = x[0]//x[1]
            elif op == 'MIN': value = min(x)
            elif op == 'MAX': value = max(x)
            elif op == 'EQ': value = int(x[0] == x[1])
            elif op == 'AND': value = x[0] & x[1]
            elif op == 'OR': value = x[0] | x[1]
            elif op == 'MUX':
                assert x[0] in (0, 1)
                value = x[1] if x[0] else x[2]
            else: raise ValueError(op)
            env[name] = value
        return [env[k] for k in self.outputs], env


MASTER_NAMES = ['q10','q11','v10','v11','q20','q21','v20','v21',
                'h0','h1','h00','h01','alpha0','alpha1','nu0','nu1',
                'f0','f1','rho']


def recovery_program(N):
    assert N >= 6
    m, M = N//2, N//2-2
    h = max(4, (256*(N-2)-1).bit_length())
    QA = 1 << h
    p = Program(MASTER_NAMES+['a','b','e0','e1'], [], ['C0','C1'])
    A = p.add
    A('zero','CONST',0); A('qa','CONST',QA)
    A('twoqa','SHL','qa',1); A('twoM','CONST',2*M)
    A('U1','MUX','a','v11','v10'); A('U2','MUX','a','v21','v20')
    A('V','MUX','b','nu1','nu0'); A('alpha','MUX','b','alpha1','alpha0')
    A('twov','SHL','V',1)
    for k, term in ((1,'V'),(2,'twov')):
        A(f'num{k}a','ADD','qa',term)
        A(f'num{k}','MUL','twoqa',f'num{k}a')
        A(f'den{k}','SUB','twoqa',f'U{k}')
        A(f'D{k}','DIV',f'num{k}',f'den{k}')
    A('DT','ADD','qa','alpha')
    A('matchE0','EQ','e0','b')
    for c in (0,1):
        s = str(c)
        for prefix, left, right in [('PH0','DT',f'h0{c}'),('PH','DT',f'h{c}'),
                                    ('PQ1','D1',f'q1{c}'),('PQ2','D2',f'q2{c}')]:
            A(prefix+'full'+s,'MUL',left,right)
            A(prefix+s,'DIV',prefix+'full'+s,'qa')
        A('I'+s,'SUB','PH0'+s,'f'+s)
        A('base'+s,'SUB','PH'+s,'nu'+s)
        A('matchE1'+s,'EQ','e1',c)
        A('J'+s,'AND','matchE0','matchE1'+s)
        A('boundary'+s,'MUX','J'+s,'rho','zero')
        A('gplus'+s,'ADD','base'+s,'boundary'+s)
        A('g'+s,'SUB','gplus'+s,'I'+s)
        A('diff'+s,'SUB','PQ2'+s,'PQ1'+s)
        A('H'+s,'SUB','diff'+s,'g'+s)
        A('lower'+s,'MAX','H'+s,'zero')
        A('A'+s,'MIN','lower'+s,'qa')
        A('snapfull'+s,'MUL','twoM','A'+s)
        A('snapnum'+s,'ADD','snapfull'+s,'qa')
        A('C'+s,'DIV','snapnum'+s,'twoqa')
    return p


def output_program(N,bits):
    """All candidates evaluated and muxed; same output as lazy source branches."""
    assert N >= 3 and bits >= 1
    p = Program(['C0','C1','a','b'], [], ['out0','out1'])
    A = p.add
    A('zero','CONST',0); A('one','CONST',1); A('two','CONST',2)
    A('Q','CONST',1 << bits); A('U','SHR','Q',1)
    A('publicUniform','CONST',int(N<6 or bits==1))
    A('D','ADD','C0','C1'); A('d','ADD','D','two')
    A('twod','SHL','d',1); A('threed','ADD','twod','d')
    A('Z','SHL','d',2); A('twoZ','SHL','Z',1); A('twoQ','SHL','Q',1)
    A('c1plus','ADD','C1','one'); A('raw1','SHL','c1plus',2)
    A('lower1','MAX','d','raw1'); A('z1','MIN','threed','lower1')
    A('nearfull','MUL','twoQ','z1'); A('nearnum','ADD','nearfull','Z')
    A('J','DIV','nearnum','twoZ'); A('near0','SUB','Q','J')
    A('c0plus','ADD','C0','one'); A('raw0','SHL','c0plus',2)
    A('z0ceil','MIN','threed','raw0'); A('z1ceil','SUB','Z','z0ceil')
    A('Qminus','SUB','Q','one'); A('Zminus','SUB','Z','one')
    for c in (0,1):
        A(f'ceilfull{c}','MUL','Qminus',f'z{c}ceil')
        A(f'ceilnum{c}','ADD',f'ceilfull{c}','Zminus')
        A(f'k{c}','DIV',f'ceilnum{c}','Z')
    A('ksum','ADD','k0','k1'); A('residual','SUB','Q','ksum')
    A('ceil1','ADD','k1','residual')
    A('selected0','MUX','a','k0','near0')
    A('selected1','MUX','a','ceil1','J')
    A('uniform','OR','publicUniform','b')
    A('out0','MUX','uniform','U','selected0')
    A('out1','MUX','uniform','U','selected1')
    return p


def clog2(x):
    assert x >= 1
    return (x-1).bit_length()


def parameters(N, bits, d):
    assert N >= 6 and bits >= 1 and d >= 6
    m = N//2
    h = clog2(256*(N-2))
    p = 4*h+4*clog2(m+4)+64
    return dict(N=N, b=bits, d=d, n=N+1, m=m, M=m-2, h=h, A=1<<h,
                p=p, R=1<<p, ell=clog2(N+2), tau=(d+1).bit_length())


def full_multiply(x, y, width):
    assert 0 <= x < 1<<width and 0 <= y < 1<<width
    acc = 0
    for j in range(width):
        acc += (x if ((y>>j)&1) else 0) << j
        assert 0 <= acc < 1<<(2*width)
    return acc


def restoring_divide(numerator, denominator, width):
    assert 0 <= numerator < 1<<(2*width)
    assert 0 < denominator < 1<<width
    quotient = remainder = 0
    for j in range(2*width-1, -1, -1):
        shifted = (remainder<<1) | ((numerator>>j)&1)
        assert shifted < 1<<(width+1)
        bit = int(shifted >= denominator)
        remainder = shifted-denominator if bit else shifted
        quotient = (quotient<<1) | bit
        assert 0 <= remainder < denominator
    assert numerator == quotient*denominator+remainder
    return quotient, remainder


def log_integer(p, q):
    """Exact common-denominator generator; q=3 gives L2, q=2 gives L3."""
    assert p >= 1 and q in (2,3)
    odd_product = 1
    for j in range(p):
        odd_product *= 2*j+1
    power = q
    for _ in range(p-1):
        power *= q*q
    denominator = power*odd_product
    term_power = q
    total = 0
    for j in range(p):
        td = (2*j+1)*term_power
        quotient, remainder = divmod(denominator, td)
        assert remainder == 0
        total += 2*quotient
        term_power *= q*q
    scaled = total << p
    value = scaled//denominator
    assert max(denominator, total, scaled, term_power).bit_length() <= 8*p*p+32
    return value


def finite_weight(score, p):
    R = 1<<p
    term = total = R
    for j in range(1,8*p+1):
        term = (term*score)//(j*R)
        total += term
    return total


def joint_program(N):
    assert N >= 6
    a = 1<<clog2(256*(N-2))
    names = [f'j{i}{j}{c}' for i in (0,1) for j in (0,1) for c in (0,1)]
    p = Program(names+['a','b'], [], ['C0','C1'])
    add = p.add
    for c in (0,1):
        add(f'left{c}','MUX','b',f'j01{c}',f'j00{c}')
        add(f'right{c}','MUX','b',f'j11{c}',f'j10{c}')
        add(f'selected{c}','MUX','a',f'right{c}',f'left{c}')
    add('qa','CONST',a);add('twoqa','SHL','qa',1);add('twoM','CONST',2*(N//2-2))
    for c in (0,1):
        add(f'full{c}','MUL','twoM',f'selected{c}')
        add(f'num{c}','ADD',f'full{c}','qa')
        add(f'C{c}','DIV',f'num{c}','twoqa')
    assert len(p.ops)==15  # two control ORs, then one reserved operation =18.
    return p


def build(N, bits, d, kind='MIX', hooks=None):
    """The early branch precedes every frontend, cut and recovery builder."""
    assert N >= 3 and bits >= 1 and d >= 6 and kind in ('MIX','JOINT')
    if N < 6:
        return dict(kind='UNIFORM', N=N, b=bits, d=d,
                    phases=['READ_ACTUAL_INPUT','INIT_OUTPUT','WRITE_GUARDED_OUTPUT','CLEAR_INPUT'],
                    words=(1<<(bits-1),1<<(bits-1),1<<bits))
    hooks = hooks or {}
    for name in ('frontend','cut','recovery'):
        if name in hooks:
            hooks[name]()
    public=parameters(N,bits,d)
    if kind=='MIX':
        # Builder/generator work, before any observation is acquired.
        public['L2']=log_integer(public['p'],3)
        public['L3']=log_integer(public['p'],2)
    return dict(kind=kind, public=public,
                phases=['READ','ADAPTERS','FEATURES','FINITE_HEADS','COPY_PORT',
                        'ERASE_ALL_OLD','EXTERNAL_OVERWRITE','READBACK','RECOVERY','OUTPUT'],
                recovery=recovery_program(N) if kind=='MIX' else joint_program(N),
                output=output_program(N,bits))


def _pair_one_hot(a,b):
    return [int((a,b)==(i,j)) for i in (0,1) for j in (0,1)]


def acquire(history, public, kind):
    """Concrete singleton bindings and finite query-head semantics."""
    N,m,M,A,p = [public[k] for k in ('N','m','M','A','p')]
    assert len(history)==N and set(history) <= {0,1}
    x = [[1-c,c] for c in history]+[[0,0]]
    records=[]
    for i in range(1,N+2):
        keys=(m,m-1,N,N-1) if i==N+1 else (i-1 if i>1 else i,i-2 if i>2 else i,i,i)
        heads=[]
        for key in keys:
            value=[0,0]
            for j in range(1,N+2):
                mask=int(j==key)
                for c in (0,1):value[c] |= mask & x[j-1][c]
            heads.append(value)
        records.append(dict(current=x[i-1][:], lag1=heads[0],lag2=heads[1],h3=heads[2],h4=heads[3]))
    q=records[-1]
    a,b=q['h4'][1],q['h3'][1]
    e0,e1=q['lag2'][1],q['lag1'][1]
    controls=_pair_one_hot(a,b)+_pair_one_hot(e0,e1)
    features=[]
    for k in range(3,m+1):
        z=records[k-1]
        l2,l1,c=z['lag2'][1],z['lag1'][1],z['current'][1]
        features.append([l2,l1,c,int(k==3)])
    if kind=='JOINT':
        sums=[0]*8
        for i,j,c,_ in features:sums[4*i+2*j+c]+=1
        code=[A*c//M for c in sums]+[0]*11
        scratch={'sums':sums}
    else:
        L2,L3=public['L2'],public['L3']
        nums=[[0]*v for v in (4,4,4,7)];den=[0]*4
        for l2,l1,c,f in features:
            scores=[int(l2==a)*L2+int(l1==b)*L2,
                    int(l2==a)*L2+int(l1==b)*L3,int(l2==b)*L2,0]
            bits=lambda z:[1-z,z]
            vals=[bits(c)+bits(l2),bits(c)+bits(l2),bits(l1)+[f*(1-l1),f*l1],
                  bits(l2)+bits(l1)+[f*(1-l1),f*l1,f]]
            for k in range(4):
                W=finite_weight(scores[k],p);den[k]+=W
                for c,v in enumerate(vals[k]):nums[k][c]+=W*v
        code=[A*z//den[k] for k in range(4) for z in nums[k]]
        scratch={'numerators':nums,'denominators':den}
    assert len(code)==19 and all(0<=v<=A for v in code)
    # Enumerated semantic data banks; the proof allocates full physical bounds.
    banks={'input':history,'onehots':x,'records':records,'features':features,
           'scratch':scratch,'clean_masters':code,'old_controls':controls}
    return code,controls,banks


def _erase_bank(bank):
    """Explicit stores to all modeled cells; never a garbage-collection erasure."""
    keys=list(bank) if isinstance(bank,dict) else range(len(bank))
    for i in keys:
        if isinstance(bank[i],(list,dict)):_erase_bank(bank[i])
        else:bank[i]=0


def _bank_zero(bank):
    vals=bank.values() if isinstance(bank,dict) else bank
    return all(_bank_zero(v) if isinstance(v,(list,dict)) else v==0 for v in vals)


def _external_checked_channel(channel,old,ctl,A,d):
    """Diagnostic validation belongs to the external channel, not the decoder."""
    result=list(channel(old,ctl))
    assert len(result)==19
    for x,y in zip(old,result):
        radius=0 if d>=x.bit_length() else x>>d
        assert 0<=y<=A and abs(y-x)<=radius
    return result


def cut_and_readback(code, controls, banks, public, channel):
    P=code[:];Pctl=controls[:]
    _erase_bank(banks)
    for i in range(len(code)):code[i]=0
    for i in range(len(controls)):controls[i]=0
    assert _bank_zero(banks)
    # Original input of channel exists only inside the external channel call.
    returned=_external_checked_channel(channel,tuple(P),tuple(Pctl),public['A'],public['d'])
    for i,v in enumerate(returned):P[i]=v
    for i in range(len(returned)):returned[i]=0
    T=P[:];U=Pctl[:]
    for i in range(len(P)):P[i]=0
    for i in range(len(Pctl)):Pctl[i]=0
    return T,U,{'all_old_banks_zero':True,'old_port_zero':not any(P+Pctl),
                'visible_words':len(T),'protected_bits':len(U)}


def decode(words, controls, public, kind):
    assert len(words)==19 and len(controls)==8
    assert sum(controls[:4])==sum(controls[4:])==1
    a=controls[2]|controls[3];b=controls[1]|controls[3]
    e0=controls[6]|controls[7];e1=controls[5]|controls[7]
    N,bits,M,A=[public[k] for k in ('N','b','M','A')]
    assert all(0<=v<=A for v in words)
    if kind=='MIX':
        values=dict(zip(MASTER_NAMES,words));values.update(a=a,b=b,e0=e0,e1=e1)
        counts,env=recovery_program(N).run(values)
    else:
        names=joint_program(N).inputs[:8]
        values=dict(zip(names,words[:8]));values.update(a=a,b=b)
        counts,env=joint_program(N).run(values)
    assert all(0<=c<=M for c in counts)
    result,oenv=output_program(N,bits).run(dict(C0=counts[0],C1=counts[1],a=a,b=b))
    Q=1<<bits
    assert sum(result)==Q and all(1<=v<Q for v in result)
    assert oenv['nearnum']<16*public['m']*Q
    return tuple(result+[Q]),{'recovery':env,'output':oenv}


def run(history,bits,d,kind='MIX',channel=lambda words,controls:words,hooks=None):
    program=build(len(history),bits,d,kind,hooks)
    if program['kind']=='UNIFORM':
        actual_input=list(history)
        assert set(actual_input)<={0,1}
        out=program['words']
        for i in range(len(actual_input)):actual_input[i]=0
        return out,{'early_uniform':True,'input_read':len(history),'input_cleared':True}
    owned_history=list(history)  # one actual input read; external caller's data is not decoder memory.
    code,controls,banks=acquire(owned_history,program['public'],kind)
    words,ctrl,trace=cut_and_readback(code,controls,banks,program['public'],channel)
    out,_=decode(words,ctrl,program['public'],kind)
    return out,trace


def transfer_kernel(payload,controls,h,kappa,source_width,channel):
    """Exact ten-phase logical READ/WRITE schedule; physical compilation is separate."""
    assert h>=1 and 1<=kappa<=h+1 and len(payload)<=19*kappa
    assert len(controls)==8 and source_width>=len(payload)+8
    assert set(payload+controls)<={0,1}
    R=len(payload);H=19*(h+1)+8
    old=payload[:]+controls[:]+[1]*(source_width-R-8)
    P=[None]*H;T=[None]*H;U=[None]*(R+8)
    actions=0;phases=[]
    def zero(bank):
        nonlocal actions
        for i in range(len(bank)):bank[i]=0;actions+=1
    def copy(src,i,dst,j):
        nonlocal actions
        dst[j]=src[i];actions+=2
    def end(name,previous):phases.append((name,actions-previous))
    place=lambda i:(i//kappa)*(h+1)+(i%kappa)
    t=actions;zero(P);end('INIT_P_FULL',t)
    t=actions
    for i in range(R):copy(old,i,P,place(i))
    end('PLACE_PAYLOAD',t)
    t=actions
    for i in range(8):copy(old,R+i,P,19*(h+1)+i)
    end('COPY_CONTROLS',t)
    t=actions;zero(old);end('CLEAR_ALL_SOURCE',t)
    words=[sum(P[i*(h+1)+j]<<j for j in range(h+1)) for i in range(19)]
    returned=list(channel(tuple(words),tuple(P[-8:])))
    assert len(returned)==19 and all(0<=v<=1<<h for v in returned)
    for i,v in enumerate(returned):
        for j in range(h+1):P[i*(h+1)+j]=(v>>j)&1
    # The external channel owns the temporary tuple/returned words above.
    phases.append(('EXTERNAL_OVERWRITE',0))
    t=actions;zero(U);end('INIT_U',t)
    t=actions;zero(T)
    for i in range(H):copy(P,i,T,i)
    end('FULL_READBACK',t)
    t=actions;zero(P);end('CLEAR_RETURNED_P',t)
    t=actions
    for i in range(R):copy(T,place(i),U,i)
    for i in range(8):copy(T,19*(h+1)+i,U,R+i)
    end('UNPACK',t)
    t=actions;zero(T);end('CLEAR_T',t)
    assert actions==6*H+5*R+source_width+40
    assert not any(old+P+T)
    return U,dict(actions=actions,phases=phases,H=H,R=R,W=source_width,
                  all_other_logical_banks_zero=True)


def alternative_program(N,bits,d,kind):
    """Public finite loop IR; every loop below has an explicit fixed bound.

    The integrated proof supplies bit/physical compilation and the separate
    ledger. Source addresses are fixed by the generator, never supplied counts.
    An IR instruction naming a kernel includes its complete loop body above.
    """
    from c3c4_ledger_v1 import alternative_budget
    budget=alternative_budget(N,bits,d,kind)
    if not budget['available']:return budget
    q=parameters(N,bits,d);h=q['h'];M=q['M'];H=budget['full_port_bits']
    ellC=clog2(M+1);R=budget['payload_bits'];k= h+1 if kind=='GAIN' else min(d,h)
    acquisition=[('INIT_ALL_SOURCE',budget['source_logical_cells']),
        ('READ_ACTUAL_INPUT_ONCE',N),('BIND_FIXED_ADJACENT_BITS',N),
        ('MAKE_8_TRIPLE_BITS_BY_16_ANDS',q['M']),
        ('ACCUMULATE_8_COUNTS_FULL',q['M']),('MAKE_S_E_ONEHOTS',8)]
    if kind=='GAIN':
        conversion=[('GAIN_LITERAL_NUM_DEN',M,q['A']),
            ('UNIFORM_HEAD_FULL_NUMERATOR',8,q['A']*(1<<q['p'])*M),
            ('UNIFORM_HEAD_EXACT_DENOMINATOR',q['A']*M*(1<<q['p'])),
            ('DIVIDE_FULL_AND_SERIALIZE_COUNTS',8,h+1)]
        post=[('DESERIALIZE_RETURNED_8',h+1),('SELECT_2_AND_CLAMP_0_M',M),
              ('SHARED_41',output_program(N,bits).ops)]
    elif kind=='COUNT_PACK':
        conversion=[('SERIALIZE_8_COUNTS',ellC)]
        post=[('DESERIALIZE_RETURNED_8',ellC),('SELECT_2_AND_CLAMP_0_M',M),
              ('SHARED_41',output_program(N,bits).ops)]
    else:
        conversion=[('SELECT_2_COUNTS',),('SHARED_41_PRECUT',output_program(N,bits).ops),
                    ('SERIALIZE_NEXT_ONE',bits)]
        post=[('DESERIALIZE_NEXT_ONE',bits),('CLAMP_1_Q_MINUS_1',1<<bits),
              ('SUBTRACT_Q_MINUS_J',1<<bits)]
    return dict(kind=kind,public=q,budget=budget,acquisition=acquisition,
        conversion=conversion,
        transfer=[('INIT_P_FULL',H),('PLACE',R,k,h+1),('COPY_CTL',8),
                  ('CLEAR_ALL_SOURCE',budget['source_logical_cells']),
                  ('PURGE_PHYSICAL_ROLLING_COPIES',4*budget['circuit_logical_cells']),
                  ('EXTERNAL_OVERWRITE',19,h+1,8),('INIT_U',R+8),
                  ('INIT_AND_FULL_READBACK_T',H),('CLEAR_P',H),
                  ('UNPACK',R,k,h+1),('COPY_CTL_FROM_T',8),('CLEAR_T',H),
                  ('PURGE_OLD_PHYSICAL_RETURN_COPIES',4*budget['circuit_logical_cells'])],
        post=post+[('WRITE_GUARDED_Q_MINUS_J_J_Q',3*(bits+1)),
                   ('CLEAR_NONOUTPUT_DATA',budget['circuit_logical_cells'])])

