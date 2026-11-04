"""Post-run validation only. No RNG calls, new training, or frozen-file writes.
Every saved state is checked in place, rather than advancing a new trajectory.
"""
import argparse, hashlib, json, os, sys, time, traceback
from pathlib import Path
import numpy as np
import core
import capture
import experiment

ROOT = Path(__file__).resolve().parent
BINDING = '79b7c4937ac91d48e5eea9a2f4fe6c1b13d6568a6d8ba4f5ca038bfe07d503b6'


def check(condition, description):
    if not condition:
        raise AssertionError(description)


def exact(actual, expected, description):
    check(np.array_equal(actual, expected), description)


def close(actual, expected, description, tolerance=2e-11):
    actual, expected = np.asarray(actual), np.asarray(expected)
    check(actual.shape == expected.shape, description + ': shape')
    delta = float(np.max(np.abs(actual - expected))) if actual.size else 0.
    check(np.isfinite(actual).all() and np.isfinite(expected).all() and delta <= tolerance,
          description + ': max absolute error ' + str(delta))
    return delta


def frozen_sources():
    check(capture.sha(ROOT / 'SOURCE_MANIFEST.json') == BINDING, 'source manifest changed')
    manifest = json.loads((ROOT / 'SOURCE_MANIFEST.json').read_text())
    for entry in manifest['files']:
        check(capture.sha(ROOT / entry['path']) == entry['sha256'], 'source changed: ' + entry['path'])
    return len(manifest['files'])


def captured(directory, kind):
    archive = directory / ('input.zip' if kind == 'input' else 'output.zip')
    receipt = capture.require_receipt(directory / 'receipt.json', archive, kind, BINDING)
    capture.verify_local_payload(directory, archive)
    upload = json.loads((directory / 'upload_result.json').read_text())
    check(upload['status'] == 'succeeded', 'actual upload was not successful')
    check(upload['library_file_id'] == receipt['library_file_id'], 'upload/receipt identity mismatch')
    check(upload['file_size_bytes'] == archive.stat().st_size, 'uploaded byte length mismatch')
    readbacks = list((directory / 'roundtrip').glob('*.zip'))
    check(len(readbacks) == 1, 'ambiguous or absent materialized readback')
    readback = readbacks[0]
    check(os.getxattr(readback, 'user.library-file-id').decode() == receipt['library_file_id'], 'readback identity xattr mismatch')
    check(capture.sha(readback) == capture.sha(archive), 'actual readback hash mismatch')
    capture.verify_archive(readback)
    return {'library_file_id': receipt['library_file_id'], 'sha256': receipt['archive_sha256'],
            'bytes': receipt['archive_bytes'], 'members': receipt['member_count'],
            'readback_path': str(readback.relative_to(ROOT))}


def independent_forward_gradient(params, H, U, M, target, learned):
    # Separate direct implementation: log(count)+score softmax, scalar CE chain
    # rule, and explicit query-group score accumulation.
    S = params[:64].reshape(2, 4, 8)
    W, b, v, bias = params[64:736].reshape(21,32), params[736:768], params[768:800], params[800]
    pools = []
    for head in range(2):
        if learned:
            logcounts = np.full(H.shape, -np.inf, dtype=float)
            np.log(H, out=logcounts, where=H > 0)
            logits = logcounts + S[head, U]
            mass = np.exp(logits - logits.max(axis=1, keepdims=True))
            pools.append(mass / mass.sum(axis=1, keepdims=True))
        else:
            pools.append(H / M)
    pool = np.stack(pools, axis=1)
    features = np.concatenate((pool.reshape(len(H),16), np.eye(4)[U], np.ones((len(H),1))/M), axis=1)
    hidden = np.tanh(features @ W + b)
    sigmoid = 1 / (1 + np.exp(-(hidden @ v + bias)))
    eta = 1 / (M+2)**2
    q = eta + (1-2*eta)*sigmoid
    if target is None:
        return q
    deriv = ((1-target)/(1-q) - target/q) * (1-2*eta)*sigmoid*(1-sigmoid) / len(H)
    dh = deriv[:,None]*v*(1-hidden**2)
    gradient = np.zeros_like(params)
    gradient[64:736] = (features.T @ dh).reshape(-1)
    gradient[736:768] = dh.sum(axis=0)
    gradient[768:800] = hidden.T @ deriv
    gradient[800] = deriv.sum()
    if learned:
        dpool = (dh @ W.T)[:,:16].reshape(len(H),2,8)
        ds = pool*(dpool-(dpool*pool).sum(axis=2,keepdims=True))
        gS = gradient[:64].reshape(2,4,8)
        for head in range(2):
            for query in range(4):
                gS[head,query] = ds[U==query,head].sum(axis=0)
    loss = np.mean(-target*np.log(q) - (1-target)*np.log1p(-q))
    return q, float(loss), gradient


def independent_metrics(p, B, y, q):
    def divergence(t):
        return t*np.log(t/q) + (1-t)*np.log((1-t)/(1-q))
    return {'kl_B': divergence(B), 'kl_source': divergence(p), 'abs_B': abs(B-q),
            'abs_source': abs(p-q), 'ce_label': -y*np.log(q)-(1-y)*np.log1p(-q)}


def summary_check(values, actual, description):
    check(actual['n'] == len(values), description + ': n')
    if len(values):
        close(actual['mean'], values.mean(), description + ': mean')
    else:
        check(actual['mean'] is None, description + ': empty mean')
    if len(values)>1:
        close(actual['mc_se'], values.std(ddof=1)/np.sqrt(len(values)), description + ': SE')
    else:
        check(actual['mc_se'] is None, description + ': undefined SE')


def audit(rep):
    started = time.monotonic()
    cfg = json.loads((ROOT/'protocol.json').read_text())
    for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
        check(os.environ.get(name)=='1', name + ' must be 1')
    check(rep in range(cfg['replicates']), 'replicate out of range')
    report = {'schema':'v10_postrun_audit_v1', 'status':'IN_PROGRESS', 'replicate':rep,
              'source_manifest_sha256':BINDING, 'audit_script_sha256':capture.sha(__file__),
              'purpose':'Validation of retained data and state transitions only; no random draws or new training trajectory.',
              'source_entries_verified_before':frozen_sources(), 'captures':{}, 'inputs':{}, 'conditions':{}}
    inp = ROOT/'runs'/f'rep{rep}'/'inputs'
    report['captures']['input'] = captured(inp,'input')
    metadata = json.loads((inp/'STARTED.json').read_text())
    check(metadata['replicate']==rep and metadata['source_manifest_sha256']==BINDING, 'input metadata mismatch')
    check(json.loads((inp/'COMPLETED.json').read_text())['status']=='COMPLETE', 'input incomplete')
    check(not (inp/'FAILURE.txt').exists(), 'input failed')
    data = {}; seed_records = json.loads((inp/'RNG_STATES.json').read_text())
    for split, horizons, n, offset in [('train',cfg['train_horizons'],cfg['train_per_horizon'],10),('test',cfg['test_horizons'],cfg['test_per_horizon'],20)]:
        for i,M in enumerate(horizons):
            key = f'{split}_M{M}'
            with np.load(inp/(key+'.npz'),allow_pickle=False) as saved:
                a = {k:saved[k].copy() for k in saved.files}
            p, starts, draws = a['p'], a['starts'], a['draws']
            check(p.shape==(n,4) and starts.shape==(n,) and draws.shape==(n,M+1),key+': raw dimensions')
            check(np.all((p>=0)&(p<1)) and np.all((draws>=0)&(draws<1)) and np.all((starts>=0)&(starts<4)),key+': raw ranges')
            full=np.empty((n,M+3),dtype=np.int8);full[:,0]=starts//2;full[:,1]=starts%2
            for step in range(M+1):
                row=2*full[:,step]+full[:,step+1]
                full[:,step+2]=draws[:,step]<p[np.arange(n),row]
            exact(a['words'],full[:,:-1],key+': words')
            exact(a['y'],full[:,-1],key+': withheld labels')
            w=full[:,:-1]
            triples=4*w[:,:-2]+2*w[:,1:-1]+w[:,2:]
            H=np.bincount((np.arange(n)[:,None]*8+triples).reshape(-1),minlength=n*8).reshape(n,8)
            U=2*w[:,-2]+w[:,-1];C=H[np.arange(n),2*U+1];J=H[np.arange(n),2*U]+C;B=(C+1)/(J+2)
            for name,value in [('H',H),('U',U),('J',J),('C',C),('B',B)]:
                exact(a[name],value,key+': '+name)
            exact(H.sum(axis=1),np.full(n,M),key+': count totals')
            seed=cfg['seed_base']+1000*rep+offset+i
            check(seed_records[key]['seed']==seed,key+': seed record')
            check(seed_records[key]['before']['bit_generator']=='PCG64' and seed_records[key]['after']['bit_generator']=='PCG64',key+': generator record')
            data[key]=a
            report['inputs'][key]={'episodes':n,'horizon':M,'exact_reconstruction':True,'rare_terminal_rows':int((J<=cfg['rare_J_max']).sum())}
    # Build the natural-label empirical table without calling the training helper.
    table={}
    for M in cfg['train_horizons']:
        a=data[f'train_M{M}']
        for j,c,label in zip(a['J'],a['C'],a['y']):
            pair=(int(j),int(c));count,ones=table.get(pair,(0,0));table[pair]=(count+1,ones+int(label))
    saved_table={(a['J'],a['C']):(a['n'],a['ones']) for a in json.loads((inp/'empirical_table.json').read_text())}
    check(table==saved_table,'empirical label table mismatch')
    with np.load(inp/'optimization.npz',allow_pickle=False) as a:
        init=a['initial_parameters'].copy();batches=a['batches'].copy();horizons=a['horizons'].copy()
    check(init.shape==(801,) and batches.shape==(cfg['steps'],cfg['batch_size']), 'optimizer retained dimensions')
    exact(init[:64],np.zeros(64),'initial scores')
    exact(horizons,np.array([cfg['train_horizons'][i%2] for i in range(cfg['steps'])]),'alternating horizons')
    check(np.all((batches>=0)&(batches<cfg['train_per_horizon'])),'batch index range')
    for condition in cfg['conditions']:
        directory=ROOT/'runs'/f'rep{rep}'/condition
        report['captures'][condition]=captured(directory,'output')
        completed=json.loads((directory/'COMPLETED.json').read_text());meta=json.loads((directory/'STARTED.json').read_text())
        check(completed['status']=='COMPLETE' and completed['steps']==cfg['steps'] and not (directory/'FAILURE.txt').exists(),condition+': incomplete/failed')
        check(meta['replicate']==rep and meta['condition']==condition and meta['source_manifest_sha256']==BINDING,condition+': identity')
        check(meta['input_archive_sha256']==report['captures']['input']['sha256'],condition+': input binding')
        states={name:np.load(directory/(name+'.npy'),mmap_mode='r',allow_pickle=False) for name in ['parameters','gradients','first_moments','second_moments']}
        for name,value in states.items():
            check(value.shape==(cfg['steps']+(name!='gradients'),801) and value.dtype==np.float64 and np.isfinite(value).all(),condition+': '+name+' shape/finite')
        exact(states['parameters'][0],init,condition+': shared initialization')
        exact(states['first_moments'][0],np.zeros(801),condition+': initial m')
        exact(states['second_moments'][0],np.zeros(801),condition+': initial v')
        steps=[json.loads(line) for line in (directory/'steps.jsonl').read_text().splitlines()]
        check(len(steps)==cfg['steps'],condition+': committed step count')
        target_name=condition.split('_')[1];learned=condition.startswith('learned')
        max_gradient=max_loss=max_metric=max_prediction=0.
        for M in cfg['train_horizons']:
            loader=experiment.load_training(inp/f'train_M{M}.npz',target_name)
            check(set(loader)=={'H','U','J','C','target'},condition+': loader target isolation')
            exact(loader['target'],data[f'train_M{M}'][target_name],condition+': loader target')
        for i,record in enumerate(steps):
            M=int(horizons[i]);a=data[f'train_M{M}'];batch=batches[i]
            p=states['parameters'][i];H=a['H'][batch];U=a['U'][batch];target=a[target_name][batch]
            loss,g=core.loss_grad(p,H,U,M,target,learned)
            exact(g,states['gradients'][i],condition+': exact gradient step '+str(i+1))
            close(record['batch_loss_before_update'],loss,condition+': loss log',0.)
            _,independent_loss,independent_gradient=independent_forward_gradient(p,H,U,M,target,learned)
            max_gradient=max(max_gradient,close(g,independent_gradient,condition+': independent gradient'))
            max_loss=max(max_loss,close(loss,independent_loss,condition+': independent loss'))
            # Recompute one transition from the stored prior state, never by advancing another trajectory.
            newp,newm,newv=core.adam_step(p,g,states['first_moments'][i],states['second_moments'][i],i+1,cfg['optimizer'])
            for name,value in [('parameters',newp),('first_moments',newm),('second_moments',newv)]:
                exact(value,states[name][i+1],condition+': exact '+name+' transition '+str(i+1))
            check(record['step']==i+1 and record['M']==M,condition+': step metadata')
            close(record['gradient_l2'],np.linalg.norm(g),condition+': gradient norm',0.)
        if not learned:
            for name,array in states.items():
                exact(array[:,:64],np.zeros_like(array[:,:64]),condition+': frozen uniform scores '+name)
        summary=json.loads((directory/'summary.json').read_text());final=states['parameters'][-1]
        for M in cfg['test_horizons']:
            a=data[f'test_M{M}'];ptrue=a['p'][np.arange(len(a['U'])),a['U']];rare=a['J']<=cfg['rare_J_max']
            with np.load(directory/f'evaluation_M{M}.npz',allow_pickle=False) as saved:
                for key in ['J','C','B','y']:
                    exact(saved[key],a[key],condition+': evaluation '+key)
                exact(saved['p_terminal'],ptrue,condition+': true terminal row')
                pred={'model':core.predict(final,a['H'],a['U'],M,learned),'Bayes':a['B'],
                      'KT':(a['C']+.5)/(a['J']+1),'unigram':(a['words'].sum(axis=1)+1)/(M+4),
                      'half':np.full(len(ptrue),.5),
                      'empirical_JC':np.array([(table.get((int(j),int(c)),(0,0))[1]+1)/(table.get((int(j),int(c)),(0,0))[0]+2) for j,c in zip(a['J'],a['C'])])}
                independent_q=independent_forward_gradient(final,a['H'],a['U'],M,None,learned)
                max_prediction=max(max_prediction,close(pred['model'],independent_q,condition+': independent final prediction'))
                for name,q in pred.items():
                    exact(saved[name+'_q'],q,condition+': saved '+name+' prediction')
                    for metric,values in independent_metrics(ptrue,a['B'],a['y'],q).items():
                        max_metric=max(max_metric,close(saved[name+'_'+metric],values,condition+': '+name+' '+metric))
                        summary_check(values,summary[str(M)][name][metric]['all'],condition+': summary all')
                        summary_check(values[rare],summary[str(M)][name][metric]['rare_J_le_3'],condition+': summary rare')
        report['conditions'][condition]={'status':'PASS','saved_update_transitions_checked':cfg['steps'],
            'exact_gradient_and_adam_state_match':True,'shared_initialization_and_batch_validation':True,
            'independent_gradient_max_abs_error':max_gradient,'independent_loss_max_abs_error':max_loss,
            'independent_final_prediction_max_abs_error':max_prediction,'independent_metric_max_abs_error':max_metric,
            'all_evaluation_horizons_checked':cfg['test_horizons'],
            'primary_kl_B':float(np.mean([summary[str(M)]['model']['kl_B']['all']['mean'] for M in cfg['train_horizons']]))}
        print('AUDIT PASS',rep,condition,flush=True)
    report.update(status='PASS',completed_utc=capture.now(),elapsed_seconds=time.monotonic()-started,
                  source_entries_verified_after=frozen_sources(),random_draws_generated=0,new_training_fits=0,
                  unresolved_discrepancies=[])
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--replicate',type=int,required=True);args=parser.parse_args()
    destination=ROOT/f'postrun_audit_rep{args.replicate}.json'
    check(not destination.exists(),'audit report already exists; do not overwrite')
    try:
        result=audit(args.replicate)
    except BaseException:
        result={'schema':'v10_postrun_audit_v1','status':'FAIL','replicate':args.replicate,
                'source_manifest_sha256':BINDING,'audit_script_sha256':capture.sha(__file__),
                'at':capture.now(),'traceback':traceback.format_exc()}
        capture.dump(destination,result)
        raise
    capture.dump(destination,result)
    print(json.dumps(result,indent=2))
