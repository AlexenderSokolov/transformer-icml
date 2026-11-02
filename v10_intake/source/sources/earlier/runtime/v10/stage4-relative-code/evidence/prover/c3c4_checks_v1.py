"""New implementation checks only: no old statistical/minimax diagnostics."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import c3c4_program_v1 as P
import c3c4_ledger_v1 as L


def verify():
    checks={}
    n=0
    for w in (2,3,4):
        for x in range(1<<w):
            for y in range(1<<w):
                assert P.full_multiply(x,y,w)==x*y;n+=1
        for x in range(1<<(2*w)):
            for y in range(1,1<<w):
                assert P.restoring_divide(x,y,w)==divmod(x,y);n+=1
    checks['full_product_and_shifted_remainder_cases']=n
    for p in (3,7,16):
        for q in (2,3):
            exact=sum((Fraction(2,(2*j+1)*q**(2*j+1)) for j in range(p)),Fraction())*(1<<p)
            assert P.log_integer(p,q)==exact.numerator//exact.denominator
        assert P.finite_weight(0,p)==1<<p
    checks['new_common_denominator_generator_cases']=6
    called=[]
    def forbidden():
        called.append('called')
        raise AssertionError('small-N reached a prohibited builder')
    for N in (3,4,5):
        for b in (1,2,1000):
            for kind in ('MIX','JOINT'):
                out,trace=P.run([i%2 for i in range(N)],b,6,kind,
                                hooks={k:forbidden for k in ('frontend','cut','recovery')})
                assert out==(1<<(b-1),1<<(b-1),1<<b)
                assert trace['early_uniform'] and trace['input_read']==N
    assert not called
    checks['early_uniform_no_builder_cases']=18
    guard_cases=0
    for N in (6,19):
        for b in (1,2,17):
            public=P.parameters(N,b,6);A=public['A']
            boxes=[[0]*19,[A]*19,[A if i%2 else 0 for i in range(19)],
                   [0 if i%2 else A for i in range(19)]]
            for words in boxes:
                for s in range(4):
                    for e in range(4):
                        controls=[int(i==s) for i in range(4)]+[int(i==e) for i in range(4)]
                        for kind in ('MIX','JOINT'):
                            out,env=P.decode(words,controls,public,kind)
                            assert out[0]+out[1]==out[2]
                            if kind=='MIX':
                                for c in (0,1):
                                    assert -8*A<=env['recovery'][f'H{c}']<=9*A
                            guard_cases+=1
    checks['new_closed_box_decoder_cases']=guard_cases
    pipeline=[]
    for history in ([0]*6,[1,0,1,0,0,1],[0,1,0,0,1,0,1,1,0,0,1]):
        for kind in ('MIX','JOINT'):
            A=P.parameters(len(history),2,6)['A']
            for direction in (-1,1):
                def channel(words,ctl):
                    sign=direction if ctl[0] else -direction
                    return tuple(max(0,min(A,x+sign*(x>>6))) for x in words)
                out,trace=P.run(history,2,6,kind,channel)
                assert trace['all_old_banks_zero'] and trace['old_port_zero']
                assert trace['visible_words']==19 and trace['protected_bits']==8
                pipeline.append(dict(N=len(history),kind=kind,port=out,erasure=trace))
    checks['new_destructive_pipeline_cases']=pipeline
    kernels=[]
    for h,kappa,R in ((10,6,0),(10,6,31),(1024,6,114),(12,12,228)):
        payload=[(i*7+1)%2 for i in range(R)];controls=[1,0,0,0,0,0,1,0]
        W=R+8+37
        def law(words,ctl):
            return [min(1<<h,x+(0 if kappa>=x.bit_length() else x>>kappa)) for x in words]
        out,tr=P.transfer_kernel(payload,controls,h,kappa,W,law)
        assert out==payload+controls
        assert tr['actions']==6*(19*(h+1)+8)+5*R+W+40
        assert tr['all_other_logical_banks_zero']
        kernels.append(tr)
    checks['complete_H_high_bits_full_readback_kernels']=kernels
    # New concrete alternative payload/readout interfaces and full physical IR.
    alternate_runs=[]
    for history in ([0]*6,[0,1,0,0,1,1,0,1,0,1,0,0]):
        N=len(history);public=P.parameters(N,5,6);M=public['M'];A=public['A']
        counts=[0]*8
        for j in range(2,public['m']):
            counts[4*history[j-2]+2*history[j-1]+history[j]]+=1
        a,b=history[-2:];e0,e1=history[public['m']-2:public['m']]
        controls=P._pair_one_hot(a,b)+P._pair_one_hot(e0,e1)
        clean,_=P.output_program(N,5).run(dict(C0=counts[4*a+2*b],C1=counts[4*a+2*b+1],a=a,b=b))
        for kind in ('GAIN','COUNT_PACK','OUTPUT_PACK'):
            ir=P.alternative_program(N,5,6,kind);ledger=ir['budget']
            assert ledger['available']
            h=public['h'];R=ledger['payload_bits'];k=h+1 if kind=='GAIN' else min(6,h)
            width=h+1 if kind=='GAIN' else P.clog2(M+1)
            if kind=='GAIN':
                acquired=[(A*(1<<public['p'])*M*c)//(A*M*(1<<public['p'])) for c in counts]
                assert acquired==counts
            if kind=='OUTPUT_PACK':payload=[(clean[1]>>j)&1 for j in range(5)]
            else:payload=[(c>>j)&1 for c in counts for j in range(width)]
            assert len(payload)==R
            # Identity is lawful for gain; maximal positive legal displacement
            # leaves both packed variants fixed, including every high bit.
            def law(words,ctl):
                return list(words) if kind=='GAIN' else [min(A,x+(x>>6)) for x in words]
            u,tr=P.transfer_kernel(payload,controls,h,k,ledger['source_logical_cells'],law)
            assert u[:R]==payload and u[R:]==controls
            if kind=='OUTPUT_PACK':J=sum(u[j]<<j for j in range(5));emitted=(32-J,J,32)
            else:
                recovered=[sum(u[c*width+j]<<j for j in range(width)) for c in range(8)]
                ans,_=P.output_program(N,5).run(dict(C0=min(M,recovered[4*a+2*b]),C1=min(M,recovered[4*a+2*b+1]),a=a,b=b))
                emitted=tuple(ans+[32])
            assert emitted==tuple(clean+[32])
            assert ledger['physical_transfer_and_duplicate_erasure_bit_bound']==(tr['actions']+20*ledger['circuit_logical_cells']+1024)*1024*ledger['physical_scalar_bits']**2
            alternate_runs.append(dict(N=N,kind=kind,output=emitted,full_H=tr['H'],logical_K=tr['actions']))
    checks['new_alternative_payload_IR_readout_cases']=alternate_runs
    # These compare the NEW early branch, not the old nominal certificate.
    small=[]
    for N,b,d in ((3,1,6),(5,1000,6),(4,2,1<<1024)):
        s=L.small_uniform_cost(N,b,d);z=L.common_budget(6,b,d)
        for k in ('depth','metadata_bits','code_bits','parameter_bits','identity_holds',
                  'stored_bits','working_bits','peak_bits','online_bit_steps'):
            assert s[k]<=z[k],k
        assert s['width']<=z['width_per_token']
        for k in ('address_bits','bit_steps','scratch_bits','peak_bits'):
            assert s['generation'][k]<=z['generation'][k],k
        small.append(dict(N=N,b=b,d_bitlength=d.bit_length(),dominated=True))
    checks['new_small_N_ledger_checks']=small
    alternatives=[]
    for d in (32,194,195):
        N=1<<(2*d+74);b=2*d
        for kind in ('GAIN','COUNT_PACK','OUTPUT_PACK'):
            z=L.alternative_budget(N,b,d,kind)
            if kind=='COUNT_PACK':assert z['available']==(d>=195)
            else:assert z['available']
            if z['available']:
                assert z['physical_scalar_bits']>1
                assert z['full_port_bits']==19*(z['h']+1)+8
                assert z['peak_bits']==z['stored_bits']+z['working_bits']
                assert z['generation']['peak_bits']==z['stored_bits']+z['generation']['scratch_bits']
            alternatives.append(z)
    checks['new_complete_alternative_ledgers']=alternatives
    return dict(status='CHECKS_PASS_NOT_NATIVE_EVIDENCE',scope='New code/closed-box/erasure/early-branch/kernel/alternative-ledger checks only; universal proof is in integrated text.',checks=checks)


if __name__=='__main__':
    result=verify()
    target=Path(__file__).with_name('c3c4-check-results-v1.json')
    with target.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'categories':list(result['checks'])}))
