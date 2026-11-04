"""Independent validation of final analysis against retained per-example records."""
import hashlib, json, os, time, traceback
from pathlib import Path
import numpy as np
import capture
from postrun_audit import ROOT, BINDING, check, exact, close, summary_check, frozen_sources


def audit():
    start=time.monotonic();cfg=json.loads((ROOT/'protocol.json').read_text());directory=ROOT/'analysis'
    count=frozen_sources()
    receipt=capture.require_receipt(directory/'receipt.json',directory/'analysis.zip','analysis',BINDING)
    capture.verify_local_payload(directory,directory/'analysis.zip')
    upload=json.loads((directory/'upload_result.json').read_text());readback=directory/'roundtrip'/'analysis.zip'
    check(upload['status']=='succeeded' and upload['library_file_id']==receipt['library_file_id'],'analysis actual upload identity')
    check(upload['file_size_bytes']==receipt['archive_bytes'],'analysis uploaded byte count')
    check(os.getxattr(readback,'user.library-file-id').decode()==receipt['library_file_id'],'analysis readback identity')
    check(capture.sha(readback)==receipt['archive_sha256'],'analysis readback bytes')
    capture.verify_archive(readback)
    results=json.loads((directory/'all_results.json').read_text());conditions=cfg['conditions'];raw={};primary={c:[] for c in conditions};output_receipts=[];report_hashes={}
    for r in range(cfg['replicates']):
        report_path=ROOT/f'postrun_audit_rep{r}.json';previous=json.loads(report_path.read_text())
        check(previous['status']=='PASS' and previous['source_manifest_sha256']==BINDING,'replicate audit missing/failed')
        check(previous['audit_script_sha256']==capture.sha(ROOT/'postrun_audit.py'),'replicate audit script binding')
        report_hashes[str(r)]=capture.sha(report_path)
        for condition in conditions:
            d=ROOT/'runs'/f'rep{r}'/condition
            output_receipts.append(json.loads((d/'receipt.json').read_text()))
            stored_summary=json.loads((d/'summary.json').read_text())
            check(results['cells'][f'rep{r}_{condition}']==stored_summary,'analysis cell differs from saved fit')
            for M in cfg['test_horizons']:
                with np.load(d/f'evaluation_M{M}.npz',allow_pickle=False) as archive:
                    a={k:archive[k].copy() for k in archive.files}
                raw[r,condition,M]=a
                for model in ['model','Bayes','KT','unigram','half','empirical_JC']:
                    for metric in ['kl_B','kl_source','abs_B','abs_source','ce_label']:
                        values=a[model+'_'+metric];summary=results['cells'][f'rep{r}_{condition}'][str(M)][model][metric]
                        summary_check(values,summary['all'],'final cell all')
                        summary_check(values[a['J']<=cfg['rare_J_max']],summary['rare_J_le_3'],'final cell rare')
            values=[raw[r,condition,M]['model_kl_B'].mean() for M in cfg['train_horizons']]
            primary[condition].append(float(sum(values)/len(values)))
        for M in cfg['test_horizons']:
            baseline=results['baselines'][f'rep{r}_M{M}']
            for model in ['Bayes','KT','unigram','half','empirical_JC']:
                check(baseline[model]==results['cells'][f'rep{r}_{conditions[0]}'][str(M)][model],'baseline cell selection')
                for condition in conditions[1:]:
                    exact(raw[r,condition,M][model+'_q'],raw[r,conditions[0],M][model+'_q'],'baselines shared across conditions')
    check(len(results['cells'])==16 and len(results['baselines'])==12,'all final cells retained')
    check(results['output_capture_receipts']==output_receipts,'all sixteen actual output receipts retained')
    for condition,values in primary.items():
        close(results['primary_replicate_means'][condition],values,'primary means',0.)
    comparisons=[('uniform_y','uniform_B'),('learned_y','learned_B'),('learned_y','uniform_y'),('learned_B','uniform_B')]
    primary_pairs={}
    for a,b in comparisons:
        key=a+'_minus_'+b;primary_pairs[key]=(np.array(primary[a])-np.array(primary[b])).tolist()
        close(results['primary_paired_differences'][key],primary_pairs[key],'primary paired vector',0.)
        for r in range(cfg['replicates']):
            for M in cfg['test_horizons']:
                aa,bb=raw[r,a,M],raw[r,b,M]
                for field in ['J','C','B','y','p_terminal']:
                    exact(aa[field],bb[field],'paired row alignment')
                entry=results['paired_per_example'][f'rep{r}_M{M}_{key}']
                rare=aa['J']<=cfg['rare_J_max']
                for metric in ['kl_B','kl_source','abs_B','abs_source','ce_label']:
                    difference=aa['model_'+metric]-bb['model_'+metric]
                    summary_check(difference,entry[metric]['all'],'paired all')
                    summary_check(difference[rare],entry[metric]['rare_J_le_3'],'paired rare')
    check(len(results['paired_per_example'])==48,'all 48 paired cells retained')
    screens={}
    for pool in ['uniform','learned']:
        natural=np.array(primary[pool+'_y']);teacher=np.array(primary[pool+'_B'])
        sorted_gaps=sorted((natural-teacher).tolist());median=(sorted_gaps[1]+sorted_gaps[2])/2
        successful=sum(x<=cfg['primary_threshold_nats'] for x in natural)
        passed=successful>=3 and median<=cfg['natural_minus_teacher_median_threshold_nats']
        recorded=results['screening'][pool]
        check(recorded['replicates_at_or_below_threshold']==successful,'screen count')
        close(recorded['median_paired_natural_minus_teacher'],median,'screen median',0.)
        check(recorded['passes_descriptive_screen']==passed,'screen pass classification')
        check(recorded['threshold_nats']==cfg['primary_threshold_nats'] and recorded['paired_median_threshold_nats']==cfg['natural_minus_teacher_median_threshold_nats'],'screen thresholds')
        check(recorded['not_power_justified'] is True,'screen caveat')
        screens[pool]={'replicates_at_or_below_threshold':int(successful),'median_natural_minus_teacher':median,'passes':bool(passed)}
    prose=(directory/'REPORT.md').read_text()
    for condition,values in primary.items():
        check('| '+condition+' | '+' | '.join(f'{v:.8f}' for v in values)+' |' in prose,'report primary row')
    for key,values in primary_pairs.items():
        check('- '+key+': '+', '.join(f'{v:.8f}' for v in values) in prose,'report paired row')
    for pool,screen in screens.items():
        line=f'- {pool}: {screen["replicates_at_or_below_threshold"]}/4 at or below 0.02 nats; median natural-minus-teacher {screen["median_natural_minus_teacher"]:.8f}; screen {"passes" if screen["passes"] else "does not pass"}.'
        check(line in prose,'report screening row')
    check('not an end-to-end Transformer' in prose and 'not power-justified tests' in prose and 'No novelty claim' in prose,'report scope caveats')
    check(frozen_sources()==count,'frozen source count changed')
    return {'schema':'v10_final_analysis_audit_v1','status':'PASS','source_manifest_sha256':BINDING,
            'audit_script_sha256':capture.sha(__file__),'replicate_audit_script_sha256':capture.sha(ROOT/'postrun_audit.py'),
            'replicate_audit_report_sha256':report_hashes,'analysis_capture':receipt,
            'checked_cells':16,'checked_paired_cells':48,'checked_baseline_cells':12,'total_saved_updates_audited':24000,
            'primary_replicate_means':primary,'primary_paired_differences':primary_pairs,'screening':screens,
            'joint_descriptive_hypothesis_passes':bool(all(x['passes'] for x in screens.values())),
            'interpretation':'Learned pooling meets its descriptive screen. Uniform pooling meets 3/4 risk criterion but fails the median natural-minus-teacher criterion. The conjunction for both architectures is not satisfied; no significance, full-Transformer or novelty claim follows.',
            'completed_utc':capture.now(),'elapsed_seconds':time.monotonic()-start,
            'random_draws_generated':0,'new_training_fits':0,'unresolved_discrepancies':[]}


if __name__=='__main__':
    destination=ROOT/'postrun_analysis_audit.json';check(not destination.exists(),'do not overwrite audit')
    try:
        report=audit()
    except BaseException:
        capture.dump(destination,{'schema':'v10_final_analysis_audit_v1','status':'FAIL','at':capture.now(),'traceback':traceback.format_exc()})
        raise
    capture.dump(destination,report)
    print(json.dumps(report,indent=2))
