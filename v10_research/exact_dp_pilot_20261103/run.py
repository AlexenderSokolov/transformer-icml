#!/usr/bin/env python3
"""Sealed microbenchmark: attack(h,k) is explicitly source/label blind."""
import hashlib,json,os,pathlib,platform,subprocess,sys,time
D=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(D.parent/'learned_position_pilot_20261103'))
import numpy as np
import pilot
from test_dp import ce,run_dp,stats,target

def proposals_attack(h,k):
    begin=time.perf_counter();w=np.array([[int(c) for c in h]],dtype=np.int8);candidates=[]
    for family in ['training','heldout']:
        proposals=pilot.proposals(w,k,family)[:,0,:]
        for idx,z in enumerate(proposals):
            word=''.join(map(str,z));obj=ce(target(h),stats(word)[3])
            candidates.append(dict(family=family,index=idx,word=word,objective=obj))
    selected=max(range(len(candidates)),key=lambda i:candidates[i]['objective'])
    return dict(wall_s=time.perf_counter()-begin,candidates=candidates,selected=selected,word=candidates[selected]['word'],objective=candidates[selected]['objective'])

def legal(h,k,z):return len(h)==len(z) and h[-2:]==z[-2:] and sum(a!=b for a,b in zip(h[:-2],z[:-2]))<=k

def evaluate_case(h,k):
    # No source table, true label or label-derived quantity is in this interface.
    prop=proposals_attack(h,k);dp=run_dp(h,k)
    assert legal(h,k,prop['word'])
    if dp['status']=='ok':
        assert legal(h,k,dp['word'])
        assert abs(dp['objective']-ce(target(h),stats(dp['word'])[3]))<1e-12
        assert dp['objective']+1e-12>=prop['objective']
        dp['advantage_over_proposals']=dp['objective']-prop['objective']
    return dict(h=h,k=k,clean_b=target(h),proposal=prop,exact_dp=dp)

def data():
    rng=np.random.default_rng(845120)
    tables=[[.5,.5,.5,.5],[.15,.5,.5,.85],[.03,.5,.5,.97]]
    out=[]
    for m in [16,32,64,128]:
        for si,table in enumerate(tables):
            start=int(rng.integers(0,4));p=np.asarray([table]);w=pilot.simulate_words(p,np.asarray([start]),m,rng=rng)[0]
            out.append(dict(M=m,source_index=si,start_pair=start,table=table,word=''.join(map(str,w))))
    return out

def main():
    records=data();(D/'data.json').write_text(json.dumps(records,indent=2)+'\n')
    assert json.loads((D/'test_results.log').read_text())['status']=='PASS'
    with (D/'results.jsonl').open('w',buffering=1) as output:
        for item in records:
            for k in [1,2,4]:
                h=item['word']
                result=evaluate_case(h,k)  # source table is not an attack input
                # Score only after both attacks have completed selection.
                table=item['table'];qtrue=table[int(h[-2:],2)]
                result.update(M=item['M'],source_index=item['source_index'],post_selection_true_q=qtrue,
                    clean_abs_error=abs(stats(h)[3]-qtrue),
                    proposal_abs_error=abs(stats(result['proposal']['word'])[3]-qtrue))
                if result['exact_dp']['status']=='ok':result['exact_abs_error']=abs(stats(result['exact_dp']['word'])[3]-qtrue)
                output.write(json.dumps(result,sort_keys=True)+'\n')
                print(json.dumps(dict(M=item['M'],source=item['source_index'],k=k,exact=result['exact_dp']['status'],sec=result['exact_dp']['wall_s'],states=result['exact_dp']['peak_states'],gap=result['exact_dp'].get('advantage_over_proposals'))),flush=True)
    print('BENCHMARK_COMPLETE',flush=True)
if __name__=='__main__':main()
