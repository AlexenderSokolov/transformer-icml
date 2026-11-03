#!/usr/bin/env python3
import json,pathlib,time,math
from run import D,evaluate_case,stats
records=json.loads((D/'data.json').read_text())
with (D/'followup_results.jsonl').open('w',buffering=1) as out:
    for item in records:
        m=item['M']
        if m not in (64,128):continue
        for k in sorted(set((math.isqrt(m),m//8))):
            h=item['word'];start=time.perf_counter();r=evaluate_case(h,k);r['entire_case_wall_s']=time.perf_counter()-start
            q=item['table'][int(h[-2:],2)]
            r.update(M=m,source_index=item['source_index'],post_selection_true_q=q,clean_abs_error=abs(stats(h)[3]-q),proposal_abs_error=abs(stats(r['proposal']['word'])[3]-q))
            if r['exact_dp']['status']=='ok':r['exact_abs_error']=abs(stats(r['exact_dp']['word'])[3]-q)
            out.write(json.dumps(r,sort_keys=True)+'\n')
            print(json.dumps(dict(M=m,source=item['source_index'],k=k,status=r['exact_dp']['status'],dp_sec=r['exact_dp']['wall_s'],wall_s=r['entire_case_wall_s'],states=r['exact_dp']['peak_states'],nodes=r['exact_dp']['nodes'],gap=r['exact_dp'].get('advantage_over_proposals'))),flush=True)
print('FOLLOWUP_COMPLETE',flush=True)
