#!/usr/bin/env python3
"""Verify the complete public archive using retained values and deterministic enumeration only.

No random-number generator, model initialization, old sampler, compiled executable,
network access or write to the checkout is used. Historical omitted records remain omitted.
"""
import builtins
import collections
import gzip
import hashlib
import itertools
import json
import math
import posixpath
import sys
import types
from fractions import Fraction
from pathlib import Path, PurePosixPath

PROV = 'provenance/four_counter_and_gate_pilot_20261103'
UNITS = ('v10_research/four_counter_dp_20261103', 'v10_research/exact_dp_pilot_20261103', 'v10_research/exact_dp_pilot_review_20261103')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(data):
    return {'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob_sha1':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}


def check_retained_records(read):
    P = 'v10_research/exact_dp_pilot_20261103/'
    data = json.loads(read(P+'data.json').decode())
    initial = [json.loads(s) for s in read(P+'results.jsonl').decode().splitlines()]
    follow = [json.loads(s) for s in read(P+'followup_results.jsonl').decode().splitlines()]
    raw = json.loads(read(P+'randomness_replayed.json').decode())
    tests = [json.loads(s) for s in read(P+'test_cases.jsonl').decode().splitlines()]
    states = json.loads(read(P+'test_random_states.json').decode())
    oracle = [json.loads(s) for s in gzip.decompress(read(P+'test_oracle_candidates.jsonl.gz')).decode().splitlines()]
    assert (len(data),len(initial),len(follow),len(raw),len(tests),len(states),len(oracle)) == (12,36,9,12,448,32,5976)

    def stats(w):
        m=len(w)-2; j=c=d=0
        for i in range(m):
            if w[i:i+2] == w[-2:]:
                j+=1; c+=int(w[i+2]); d+=i<m//2
        a=c/j if j and 512*d>=j else int(w[-2])
        eps=1/math.sqrt(m)
        return j,c,d,(1-2*eps)*a+eps

    def score(p,q):
        return -p*math.log(q)-(1-p)*math.log1p(-q)

    def legal(h,z,k):
        return len(h)==len(z) and z[-2:]==h[-2:] and sum(a!=b for a,b in zip(h[:-2],z[:-2]))<=k

    def proposals(h,k):
        m=len(h)-2
        for family in ('training','heldout'):
            # For these recorded k values the rational flooring is also exactly the
            # NumPy linspace/floor index list; this is independently checked against
            # every retained candidate, rather than assumed for arbitrary inputs.
            inds=[range(s,s+k) for s in [0,(m-k)//2,m-k]] if family=='training' else [range(s,s+k) for s in [(m-k)//4,3*(m-k)//4]]+[[i*(m-1)//(k-1) for i in range(k)] if k>1 else [0]]
            yield family,0,h
            index=1
            for positions in inds:
                for op in range(3):
                    z=list(h)
                    for i in positions:
                        z[i]=str(op) if op<2 else str(1-int(z[i]))
                    yield family,index,''.join(z)
                    index+=1

    uniforms=0
    for d,a in zip(data,raw):
        assert all(d[k]==a[k] for k in ('M','source_index','start_pair','table','word'))
        assert len(a['uniforms'])==a['M']==len(a['before_each_uniform_states'])
        z=[a['start_pair']//2,a['start_pair']%2]
        for u in a['uniforms']:
            assert 0<=u<1
            z.append(int(u<a['table'][2*z[-2]+z[-1]]))
        assert ''.join(map(str,z))==d['word']
        uniforms+=len(a['uniforms'])
    assert uniforms==720

    maxerr=0.;candidate_count=0
    for row in initial+follow:
        h=row['h'];m=row['M'];k=row['k'];j,c,d,q=stats(h);p=(c+1)/(j+2)
        assert abs(p-row['clean_b'])<1e-14
        source=next(x for x in data if x['M']==m and x['source_index']==row['source_index'])
        assert source['word']==h
        assert row['post_selection_true_q']==source['table'][int(h[-2:],2)]
        generated=list(proposals(h,k));saved=row['proposal']['candidates']
        assert len(generated)==len(saved)==20
        scores=[]
        for (family,index,z),entry in zip(generated,saved):
            assert (family,index,z)==(entry['family'],entry['index'],entry['word']) and legal(h,z,k)
            s=score(p,stats(z)[3]);assert abs(s-entry['objective'])<1e-12;maxerr=max(maxerr,abs(s-entry['objective']));scores.append(s);candidate_count+=1
        index=max(range(len(scores)),key=scores.__getitem__)
        assert index==row['proposal']['selected']
        assert row['proposal']['word']==generated[index][2]
        assert abs(row['proposal']['objective']-scores[index])<1e-12
        dp=row['exact_dp'];assert dp['status']=='ok'
        z=dp['word'];assert legal(h,z,k)
        jj,cc,dd,qq=stats(z);assert (jj,cc,dd)==(dp['j'],dp['c'],dp['d'])
        obj=score(p,qq);assert abs(obj-dp['objective'])<1e-12;maxerr=max(maxerr,abs(obj-dp['objective']))
        assert abs(obj-scores[index]-dp['advantage_over_proposals'])<1e-12 and obj>=scores[index]-1e-12
        truth=row['post_selection_true_q']
        for key,word in [('clean_abs_error',h),('proposal_abs_error',row['proposal']['word']),('exact_abs_error',z)]:
            assert abs(row[key]-abs(stats(word)[3]-truth))<1e-14

    count=0
    for i,t in enumerate(tests):
        h=t['h'];m=len(h)-2;k=t['k'];j,c,_,_=stats(h);p=(c+1)/(j+2);best=-1.;near=[]
        assert t['status']=='pass' and legal(h,t['word'],k)
        for n in range(k+1):
            for flips in itertools.combinations(range(m),n):
                z=list(h)
                for x in flips:z[x]=str(1-int(z[x]))
                z=''.join(z);jj,cc,dd,q=stats(z);s=score(p,q);a=oracle[count]
                assert (a['case'],a['flips'],a['word'],a['j'],a['c'],a['d'])==(i,list(flips),z,jj,cc,dd)
                assert abs(a['q']-q)<1e-15 and abs(a['objective']-s)<1e-15
                if s>best+1e-12:best=s;near=[z]
                elif abs(s-best)<=1e-12:near.append(z)
                count+=1
        assert abs(t['objective']-best)<1e-12 and abs(t['oracle_best']-best)<1e-12
        assert abs(score(p,stats(t['word'])[3])-best)<1e-12 and t['oracle_maximizer_count']==len(near)
    assert count==len(oracle)
    for i,state in enumerate(states):
        block=tests[320+4*i:324+4*i]
        assert len(block)==4 and all(t['h']==state['h'] for t in block)
        assert [t['k'] for t in block]==[0,1,2,3]
        assert state['M']==len(state['h'])-2

    def summary(rows):
        return {'count':len(rows),'statuses':dict(collections.Counter(r['exact_dp']['status'] for r in rows)),
                'positive_gap':sum(r['exact_dp']['advantage_over_proposals']>1e-12 for r in rows),
                'tied_gap':sum(abs(r['exact_dp']['advantage_over_proposals'])<=1e-12 for r in rows),
                'source_error_dp_greater':sum(r['exact_abs_error']>r['proposal_abs_error']+1e-12 for r in rows),
                'source_error_dp_smaller':sum(r['exact_abs_error']+1e-12<r['proposal_abs_error'] for r in rows),
                'source_error_equal':sum(abs(r['exact_abs_error']-r['proposal_abs_error'])<=1e-12 for r in rows),
                'max_gap':max(r['exact_dp']['advantage_over_proposals'] for r in rows),
                'internal_cpp_wall_range_s':[min(r['exact_dp']['wall_s'] for r in rows),max(r['exact_dp']['wall_s'] for r in rows)],
                'max_peak_states':max(r['exact_dp']['peak_states'] for r in rows),
                'max_nodes':max(r['exact_dp']['nodes'] for r in rows)}

    return {'data_words':len(data),'saved_reconstruction_uniforms':uniforms,
            'initial':summary(initial),'followup':summary(follow),'proposal_entries':candidate_count,
            'max_recomputed_objective_discrepancy':maxerr,'test_rows':len(tests),
            'retrospective_oracle_rows_checked':len(oracle),'retrospective_test_state_records_word_bindings_checked':len(states),
            'rng_state_evolution_validated':False,'full_45_case_optima_recomputed':False}


def check_four_counter(read):
    path = UNITS[0] + '/four_counter.py'
    module = types.ModuleType('verified_four_counter')
    exec(compile(read(path), path, 'exec'), module.__dict__)
    maps = witnesses = word_masks = 0
    for m in range(2, 7):
        for h in itertools.product((0, 1), repeat=m+2):
            brute = {}
            for mask in itertools.product((0, 1), repeat=m):
                z = tuple(h[i] ^ mask[i] for i in range(m)) + h[m:]
                selected = [(i, z[i+2]) for i in range(m) if z[i:i+2] == h[-2:]]
                bank = (len(selected), sum(v for i,v in selected),
                        sum(i < m//2 for i,v in selected), sum(v for i,v in selected if i < m//2))
                cost = sum(mask)
                brute[bank] = min(brute.get(bank, m+1), cost)
                word_masks += 1
            for k in range(m+1):
                expected = {b:c for b,c in brute.items() if c <= k}
                got = module.solve_banks(h, k, witnesses=True)
                require({b:c for b,(c,z) in got.items()} == expected, 'Four-counter map discrepancy')
                for b,(c,z) in got.items():
                    require(z[-2:] == h[-2:] and sum(x != y for x,y in zip(z,h)) == c <= k,
                            'Illegal four-counter witness')
                    selected = [(i,z[i+2]) for i in range(m) if z[i:i+2] == h[-2:]]
                    actual = (len(selected),sum(v for i,v in selected),sum(i<m//2 for i,v in selected),sum(v for i,v in selected if i<m//2))
                    require(actual == b, 'Witness bank discrepancy')
                    witnesses += 1
                maps += 1
    h = (0,0,0,0,0)
    expected_bank = (1,0,0,0)
    cost,witness = module.solve_banks(h, 1, True)[expected_bank]
    score,returned,bank = module.maximize(h, 1, lambda x:int(x[0] == Fraction(1,3)))
    require(witness == (0,1,0,0,0) and cost == 1 and score == 0 and bank[0]-bank[1] != 1,
            'Expected float/rational counterexample changed')
    text = ('h=00000 k=1: implementation returns ' + ''.join(map(str,returned)) + ' score ' + str(score) + ' bank ' + str(bank) + '\n'
            + 'exact rational utility optimum 1 attained by ' + ''.join(map(str,witness)) + ' bank ' + str(expected_bank) + '\n')
    require(text.encode() == read(UNITS[0]+'/review_independent/float_counterexample.log'),
            'Archived float counterexample output differs')
    return {'complete_bank_maps':maps,'literal_word_masks':word_masks,'legal_witnesses':witnesses,
            'range':'M=2 through 6, every history and budget', 'float_counterexample_log_byte_identical':True,
            'pilot_model_input_comparisons_rerun':False, 'random_model_initializations':0,
            'generic_exact_rational_utility_claim':False}


def main():
    require(not sys.flags.optimize, 'Optimized Python disables scientific assertions; use ordinary python3.')
    root = Path(__file__).resolve().parents[2]
    invpath = root
    for part in ('provenance','PUBLIC_INVENTORY.json'):
        invpath = invpath / part
        require(not invpath.is_symlink(), 'Symlink inventory path refused')
    require(invpath.is_file(), 'Missing public inventory')
    inventory = json.loads(invpath.read_text())
    rows = {f['path']:f for f in inventory['files']}
    require(len(rows) == len(inventory['files']), 'Duplicate inventory path')
    verified = {}

    def read(path):
        p = PurePosixPath(path)
        require(not p.is_absolute() and '..' not in p.parts and str(p) == path, 'Unsafe public path')
        require(path in rows, 'Path absent from public inventory: '+path)
        current = root
        for part in p.parts:
            current = current / part
            require(not current.is_symlink(), 'Symlink input refused: '+path)
        require(current.is_file(), 'Missing input: '+path)
        data = current.read_bytes()
        require(identity(data) == {k:rows[path][k] for k in identity(data)}, 'Public identity mismatch: '+path)
        verified[path] = data
        return data

    read(PROV+'/verify_public_archive.py')
    source_map = json.loads(read(PROV+'/SOURCE_EXPORT_MAP.json'))
    reconciliation = json.loads(read(PROV+'/PUBLIC_EXPORT_RECONCILIATION.json'))
    safety = json.loads(read(PROV+'/REPLAY_SAFETY.json'))
    read(PROV+'/PUBLIC_REPLAY.md')
    read(PROV+'/PUBLICATION_SCOPE_AND_CHECKS.json')
    selected = {f['path']:f for f in source_map['files']}
    require(len(selected) == len(source_map['files']) == 54, 'Unexpected source selection')
    for path,f in selected.items():
        require(identity(read(path)) == f['public'], 'Selected public identity mismatch')
        require(f['changed'] == (f['original'] != f['public']), 'Inconsistent source identity map')
    deps = {f['path']:f for f in reconciliation['inherited_dependencies']}
    require(len(deps) == 1, 'Unexpected runtime dependency set')
    for path,f in deps.items():
        require(identity(read(path)) == f['original'] == f['public'], 'Inherited dependency mismatch')
    bound=[]
    for path in selected:
        name=PurePosixPath(path).name
        if name=='INPUT_BINDINGS.json':
            bound.extend(json.loads(verified[path]).items())
        elif name=='SHA256SUMS' or name.endswith('SHA256.txt'):
            for line in verified[path].decode().splitlines():
                expected,relative=line.split(maxsplit=1)
                target=posixpath.normpath(posixpath.join(posixpath.dirname(path),relative.strip().lstrip('*')))
                bound.append((target,expected))
    mapped=0
    for path,expected in bound:
        require(path in selected or path in deps,'Unresolved binding: '+path)
        entry=selected.get(path,deps.get(path))
        require(entry['original']['sha256']==expected,'Unexpected original binding: '+path)
        require(identity(verified[path])==entry['public'],'Public source binding mismatch')
        mapped += entry['original'] != entry['public']
    require(len(bound)==65 and mapped==5,'Unexpected historical binding counts')
    require(safety['new_scientific_random_draws_performed']==0,'Unsafe replay declaration')
    # Defence in depth: no scientific PRNG/model framework can be imported by
    # the only original module executed below. It itself imports only itertools.
    original_import=builtins.__import__
    def guarded_import(name,*args,**kwargs):
        require(name.split('.')[0] not in ('random','numpy','torch','secrets','subprocess'),
                'Sampling/model/process import refused: '+name)
        return original_import(name,*args,**kwargs)
    builtins.__import__=guarded_import
    try:
        records=check_retained_records(read)
        four=check_four_counter(read)
    finally:
        builtins.__import__=original_import
    for path,data in verified.items():
        require((root/path).read_bytes()==data,'Public source changed during validation')
    print(json.dumps({'status':'PASS','selected_sources':54,'verified_public_files':len(verified),
                      'historical_bindings':len(bound),'declared_export_pair_occurrences':mapped,
                      'retained_record_checks':records,'deterministic_four_counter_checks':four,
                      'scientific_prng_calls':0,'new_model_initializations':0,'native_executable_runs':0,
                      'original_rng_states_recovered':False,'all_45_case_optima_recomputed':False,
                      'checkout_writes':False},indent=2))


if __name__=='__main__':
    main()
