"""Check console/checkpoint metrics/declared screen after the main author reconciliation."""
import json,csv,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent;O=P/'confirmation_v1';res=json.loads((O/'results.json').read_text());csvrows=list(csv.DictReader((O/'checkpoint_metrics.csv').open()));messages=[]
for line in (P/'confirmation_console.log').read_text().splitlines():
 try:messages.append(json.loads(line))
 except json.JSONDecodeError:pass
rows=[x for x in messages if isinstance(x,dict) and {'arm','seed','step'}<=x.keys()];assert len(rows)==len(csvrows)==24
maxdelta=0.
for a,b in zip(rows,csvrows):
 assert (a['arm'],a['seed'],a['step'])==(b['arm'],int(b['seed']),int(b['step']))
 for k in a:
  if k in ['arm','seed','step']:continue
  maxdelta=max(maxdelta,abs(float(a[k])-float(b[k])));assert abs(float(a[k])-float(b[k]))<1e-12,(k,a[k],b[k])
for s in res['screen']:
 seed=s['seed'];a=next(r for r in res['final_metrics'] if r['seed']==seed and r['arm']=='corrected');b=next(r for r in res['final_metrics'] if r['seed']==seed and r['arm']=='rare_boost')
 assert abs(s['rare_heldout_error_ratio']-b['rare_heldout_mean_abs_error']/a['rare_heldout_mean_abs_error'])<1e-15
 assert abs(s['natural_KL_increase']-(b['natural_mean_KL']-a['natural_mean_KL']))<1e-15
 assert s['collision_max_error']==b['collision_max_abs_error']
 assert s['pass']==(b['rare_heldout_mean_abs_error']<=.8*a['rare_heldout_mean_abs_error'] and b['natural_mean_KL']-a['natural_mean_KL']<=.002 and b['collision_max_abs_error']<=.05)
assert res['screen_all_pass']==all(s['pass'] for s in res['screen'])
assert any(isinstance(x,dict) and x.get('status')=='done' and x.get('screen')==res['screen'] for x in messages)
print(json.dumps({'console_checkpoint_rows':len(rows),'max_console_checkpoint_CSV_discrepancy':maxdelta,'all_screen_rows_recomputed':len(res['screen']),'console_sha256':hashlib.sha256((P/'confirmation_console.log').read_bytes()).hexdigest(),'status':'author_supplement_passed_not_independent_audit'},indent=2))
