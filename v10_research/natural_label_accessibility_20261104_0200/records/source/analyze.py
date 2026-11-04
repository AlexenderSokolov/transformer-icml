"""All fixed cells and paired differences; no checkpoint/seed filtering."""
import json
from pathlib import Path
import numpy as np
from experiment import ROOT, check_sources, summarize
from capture import require_receipt, dump, make_archive, verify_local_payload

def screening(natural,teacher,threshold,delta):
    n=np.asarray(natural,dtype=float);t=np.asarray(teacher,dtype=float)
    if n.shape!=(4,) or t.shape!=(4,):raise ValueError('four independent paired replicas required')
    count=int((n<=threshold).sum());med=float(np.median(n-t))
    return {'replicates_at_or_below_threshold':count,'median_paired_natural_minus_teacher':med,'passes_descriptive_screen':bool(count>=3 and med<=delta),'threshold_nats':threshold,'paired_median_threshold_nats':delta,'not_power_justified':True}

def main():
    cfg,binding=check_sources();out=ROOT/'analysis'
    cells={};primary={c:[] for c in cfg['conditions']};pairs={};baselines={};receipts=[]
    for r in range(cfg['replicates']):
        input_hash=None
        for c in cfg['conditions']:
            d=ROOT/'runs'/f'rep{r}'/c
            receipts.append(require_receipt(d/'receipt.json',d/'output.zip','output',binding))
            verify_local_payload(d,d/'output.zip')
            completed=json.loads((d/'COMPLETED.json').read_text())
            if completed.get('status')!='COMPLETE' or completed.get('steps')!=cfg['steps'] or (d/'FAILURE.txt').exists():raise ValueError('incomplete or failed fit')
            started=json.loads((d/'STARTED.json').read_text())
            if started.get('replicate')!=r or started.get('condition')!=c or started.get('source_manifest_sha256')!=binding:raise ValueError('output identity mismatch')
            h=started.get('input_archive_sha256')
            if not isinstance(h,str) or len(h)!=64:raise ValueError('missing input identity')
            if input_hash is not None and h!=input_hash:raise ValueError('conditions use different input bundles')
            input_hash=h
            cells[f'rep{r}_{c}']=json.loads((d/'summary.json').read_text())
            primary[c].append(float(np.mean([cells[f'rep{r}_{c}'][str(M)]['model']['kl_B']['all']['mean'] for M in cfg['train_horizons']])))
        for M in cfg['test_horizons']:
            base=ROOT/'runs'/f'rep{r}'
            with np.load(base/cfg['conditions'][0]/f'evaluation_M{M}.npz',allow_pickle=False) as a:
                baselines[f'rep{r}_M{M}']={name:cells[f'rep{r}_{cfg["conditions"][0]}'][str(M)][name] for name in ['Bayes','KT','unigram','half','empirical_JC']}
            for a,b in [('uniform_y','uniform_B'),('learned_y','learned_B'),('learned_y','uniform_y'),('learned_B','uniform_B')]:
                with np.load(base/a/f'evaluation_M{M}.npz',allow_pickle=False) as aa,np.load(base/b/f'evaluation_M{M}.npz',allow_pickle=False) as bb:
                    for key in ['J','C','B','y','p_terminal']:
                        if not np.array_equal(aa[key],bb[key]):raise ValueError('paired test examples differ: '+key)
                    rare=aa['J']<=cfg['rare_J_max'];row={}
                    for metric in ['kl_B','kl_source','abs_B','abs_source','ce_label']:
                        diff=aa['model_'+metric]-bb['model_'+metric]
                        row[metric]={'all':summarize(diff),'rare_J_le_3':summarize(diff[rare])}
                    pairs[f'rep{r}_M{M}_{a}_minus_{b}']=row
    screens={pool:screening(primary[pool+'_y'],primary[pool+'_B'],cfg['primary_threshold_nats'],cfg['natural_minus_teacher_median_threshold_nats']) for pool in ['uniform','learned']}
    primary_pairs={a+'_minus_'+b:(np.array(primary[a])-np.array(primary[b])).tolist() for a,b in [('uniform_y','uniform_B'),('learned_y','learned_B'),('learned_y','uniform_y'),('learned_B','uniform_B')]}
    result={'primary_replicate_means':primary,'primary_paired_differences':primary_pairs,'screening':screens,'cells':cells,'paired_per_example':pairs,'baselines':baselines,'output_capture_receipts':receipts,'scope':'Four independent complete experiments. Conditional per-example MC SE is not training-variability uncertainty. No full Transformer, learning-rate theorem, or novel Markov-ICL claim.'}
    out.mkdir(exist_ok=False)
    dump(out/'all_results.json',result)
    lines=['# Natural-label accessibility: bounded exploratory results','', 'All sixteen fixed fits are retained. Primary values are KL(B || q), equal-weighted over M=32,64. Each column is one independent dataset, initialization and minibatch replicate.','', '| Condition | Replicate 0 | Replicate 1 | Replicate 2 | Replicate 3 |','|---|---:|---:|---:|---:|']
    for c,v in primary.items():lines.append('| '+c+' | '+' | '.join(f'{x:.8f}' for x in v)+' |')
    lines+=['','## Predeclared descriptive screens']
    for p,s in screens.items():lines.append(f'- {p}: {s["replicates_at_or_below_threshold"]}/4 at or below 0.02 nats; median natural-minus-teacher {s["median_paired_natural_minus_teacher"]:.8f}; screen {"passes" if s["passes_descriptive_screen"] else "does not pass"}.')
    lines+=['','## Paired primary differences']
    for p,v in primary_pairs.items():lines.append('- '+p+': '+', '.join(f'{x:.8f}' for x in v))
    lines+=['','## Scope and limitations','- Supplied local triple features and terminal query; this is not an end-to-end Transformer. Uniform pooling already supplies sufficient statistics.','- Bayes-target fits use explicit B supervision; natural-label fits use sampled y only. Both are kept distinct.','- M=128 is out of training length. Full per-cell, rare-row, baseline and paired errors and conditional Monte Carlo SE are in all_results.json; per-example records are in each captured output.','- Four independent replicas do not support strong general training-effect inference. Thresholds are screening rules, not power-justified tests. No hyperparameter or seed selection was performed.','- Neither these outcomes nor failures recover the missing original 20:35 pilot.','- Broad Markov in-context learning is prior art (Edelman et al. 2024; Lepage et al. 2025). No novelty claim is made.']
    (out/'REPORT.md').write_text('\n'.join(lines)+'\n')
    make_archive(out,['all_results.json','REPORT.md'],out/'analysis.zip','analysis',binding)
    print((out/'REPORT.md').read_text())

if __name__=='__main__':main()
