"""Stage4 ledgers. Main Bstar is exact D6; alternatives are separate complete vectors.
Author Prover, 2026-10-26. Bstar function attributed to Lead010 source
SHA256 3869642ae43f29d25990ecb89af19c5d936b79e6b5333f5f42c7996051db9b37.
No old diagnostics or old certificate functions are invoked.
"""
def clog2(x):
    assert x >= 1
    return (x - 1).bit_length()


def common_budget(N, b, d):
    assert N >= 6 and b >= 1 and d >= 6
    m, n, nm = N // 2, N + 1, N // 2 + 1
    h = clog2(256 * (N - 2))
    p = 4*h + 4*clog2(m + 4) + 64
    ell, tau = clog2(N + 2), (d + 1).bit_length()
    B, O = 128*p, 32*(b + ell + 8)
    g = lambda w: 1024*w*w
    WF, WO = 1024*B, 1024*O
    GF = 63*g(B) + 256*19*(h + 1) + 1024*B
    GO = 41*g(O) + 1024*O + 64*(b + 1)
    LF, LO, pre = 16*GF + 32, 16*GO + 32, 132
    depth = pre + LF + LO
    E = (256*p + 1024)*n*n + (4096*B + 1024)*n + 1024*(h + 1)
    attention = E*g(B)
    meta = 128*n*(ell + p + b + 16) + 256*n*(ell + h + b + tau + 32)
    masks = 4*n*n + 4*nm*nm
    a = (attention + GF + GO + meta + 1).bit_length() + ell + tau + 32
    V = B + O + a
    code = 4096*(g(B)*(B + a) + g(O)*(O + a)) + 256*(p + 1)*V*V
    slots = (pre + LF)*(WF + 1)**2 + LO*(WO + 1)**2
    coeff = (pre + LF)*(WF + 1)**2*B + LO*(WO + 1)**2*O
    holds = pre*n*WF + LF*WF + LO*WO
    stored = coeff + code + masks + meta
    work = 4*n*WF*B + 4*WO*O + meta
    online = 256*((pre + LF)*n*(WF + 1)**2*B*B + LO*(WO + 1)**2*O*O) + attention
    Blog = 8*p*p + 32
    Tlog = (32*p + 64)*g(Blog)
    agen = Blog + B + O + (stored + depth + 1).bit_length() + ell + b + tau + 32
    gen = Tlog + 1024*(ell + b + tau + p + 1)**2 + 4096*(stored + depth + 1)*agen**2
    wg = 64*Blog + 64*(ell + b + tau + p + 1) + 64*(stored + depth + 1)*agen
    return dict(parameters=dict(N=N, b=b, d=d, m=m, M=m-2, h=h, A=1 << h,
                                p=p, ell=ell, tau=tau, B=B, O=O),
                model='one-shot batch hybrid dense tokenwise tied; charged finite evaluator',
                depth=depth, width_per_token=max(WF, WO), total_heads=8,
                simultaneous_heads=4, value_width=8, qk_dimension=4,
                score_abs_max=2, frontend_word_bits=B, output_word_bits=O,
                cut_words=19, cut_word_bits=h+1, protected_control_bits=8,
                cut_data_bits=19*(h+1)+8, output_bits=3*(b+1),
                masks_bits=masks, metadata_bits=meta, code_bits=code,
                address_bits=a, dense_slots=slots, parameter_bits=coeff,
                identity_holds=holds, stored_bits=stored, working_bits=work,
                peak_bits=stored+work, finite_evaluator_word_steps=E,
                finite_evaluator_bit_steps=attention, online_bit_steps=online,
                generation=dict(address_bits=agen, bit_steps=gen,
                                scratch_bits=wg, peak_bits=stored+wg))


def small_uniform_cost(N,b,d):
    assert 3<=N<=5 and b>=1 and d>=6
    ell=clog2(N+2);tau=(d+1).bit_length()
    beta=32*(b+clog2(8)+8)
    width=32
    depth=16
    metadata=128*(ell+b+tau+16)
    code=4096*(ell+b+tau+16)
    params=depth*(width+1)**2*beta
    stored=params+code+metadata
    work=4*width*beta+metadata
    steps=256*depth*(width+1)**2*beta*beta+64*(N+3*(b+1))
    a=beta+(stored+depth+1).bit_length()+ell+b+tau+32
    gen=1024*(ell+b+tau+1)**2+4096*(stored+depth+1)*a*a
    wg=64*(ell+b+tau+1)+64*(stored+depth+1)*a
    return dict(N=N,b=b,d=d,mode='EARLY_UNIFORM_NO_FRONTEND',depth=depth,
                width=width,total_heads=0,cut_words=0,protected_control_bits=0,
                output_bits=3*(b+1),masks_bits=0,metadata_bits=metadata,
                code_bits=code,parameter_bits=params,identity_holds=depth*width,
                stored_bits=stored,working_bits=work,peak_bits=stored+work,
                online_bit_steps=steps,generation=dict(address_bits=a,bit_steps=gen,
                scratch_bits=wg,peak_bits=stored+wg))


def alternative_budget(N,b,d,kind):
    assert N>=6 and b>=1 and d>=6 and kind in ('GAIN','COUNT_PACK','OUTPUT_PACK')
    q=common_budget(N,b,d)['parameters']
    n=N+1;h=q['h'];p=q['p'];ell=q['ell'];tau=q['tau'];M=q['M']
    kappa=min(d,h);ellC=clog2(M+1);H=19*(h+1)+8
    R=8*(h+1) if kind=='GAIN' else 8*ellC if kind=='COUNT_PACK' else b
    capacity=19*(h+1) if kind=='GAIN' else 19*kappa
    if R>capacity:
        return dict(kind=kind,available=False,payload_bits=R,capacity=capacity)
    beta=128*(p+b+ell+tau+h+16)
    g=lambda w:1024*w*w
    W=16*n+1024*beta+4*R+H+64
    S=W+2*H+R+8+64*beta
    K=6*H+5*R+W+40
    acq=(512*n+256)*g(beta)
    pre=(64*g(beta) if kind=='OUTPUT_PACK' else 0)+16*(R+8)
    post=(16 if kind=='OUTPUT_PACK' else 96)*g(beta)+64*(b+1)+16*(R+8)
    # Initialization, pre-cut purge, returned-copy purge, final cleanup,
    # and retained-field handoffs: five groups of four physical banks.
    transfer=(K+20*S+1024)*g(beta)
    G=acq+pre+transfer+post
    L=16*G+64;C=S+8
    z0=256*n*(ell+b+tau+p+h+32)
    a=(G+S+L+z0+1).bit_length()+ell+tau+32
    code=64*(G+K+S+1)*(beta+a)+4096*g(beta)*(beta+a)
    meta=z0+16*K*(a+1)
    par=L*(C+1)**2*beta
    stored=par+code+meta
    work=4*C*beta+meta+64*a
    online=256*L*(C+1)**2*beta*beta+transfer
    agen=beta+a+(stored+L+G+1).bit_length()+ell+b+tau+h+p+64
    emit=stored+L+G+K+1
    gen=1024*(ell+b+tau+p+h+1)**2+4096*emit*agen*agen
    wg=64*(ell+b+tau+p+h+1)+64*emit*agen
    return dict(kind=kind,available=True,model='SEPARATELY_PAID_STATIC_ONE_SHOT_DENSE_BIT_REGISTER_CIRCUIT',
                N=N,b=b,d=d,h=h,kappa=kappa,ell_C=ellC,payload_bits=R,
                capacity=capacity,full_port_bits=H,source_logical_cells=W,
                circuit_logical_cells=S,physical_scalar_bits=beta,
                exact_logical_transfer_actions=K,acquisition_gate_bound=acq,
                precut_output_and_conversion_gate_bound=pre,
                physical_transfer_and_duplicate_erasure_bit_bound=transfer,
                postcut_readout_and_guarded_output_gate_bound=post,
                total_gate_bound=G,depth=L,width=C,address_field_bits=a,
                identity_holds=L*C,dense_slots=L*(C+1)**2,
                parameter_bits=par,code_bits=code,metadata_bits=meta,
                stored_bits=stored,working_bits=work,peak_bits=stored+work,
                online_bit_steps=online,output_bits=3*(b+1),
                generation=dict(address_bits=agen,bit_steps=gen,scratch_bits=wg,
                                peak_bits=stored+wg))

