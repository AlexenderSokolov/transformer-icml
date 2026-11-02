#!/usr/bin/env python3
"""Read-only end-to-end binding verification for RE001 handoff."""
from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent;ROOT=D.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
review=json.loads((D/'RE001_independent_review_bindings.json').read_text())
assert review['status']=='PASS'
for path,expected in review['sha256'].items():
 assert sha(D/path)==expected,path
 checks.append(path)
sources=json.loads((D/'RE001_source_bindings.json').read_text())
for path,expected in sources['files'].items():
 assert sha(ROOT/path)==expected,path
 checks.append(path)
author=json.loads((D/'RE001_diagnostics.json').read_text())
assert author['status']=='PASS'
for path,expected in author['sha256'].items():
 assert sha(ROOT/path)==expected,path
 checks.append(path)
independent=json.loads((D/'RE001_independent_checks.json').read_text())
assert independent['status']=='PASS'
assert independent['theorem_sha256']==sha(D/'RE001_theorem.md')
assert independent['script_sha256']==sha(D/'RE001_independent_checks.py')
print(json.dumps({'status':'PASS','checked_bindings':len(checks)+2,'theorem_sha256':sha(D/'RE001_theorem.md'),'review_sha256':sha(D/'RE001_independent_review.md'),'note':'Binding verification, not formal mathematical verification or root acceptance'},indent=2))
