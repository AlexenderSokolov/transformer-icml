#!/usr/bin/env python3
"""Verify ordered public archive parts and rebuild one ZIP. Standard library only.
No extraction, network access, scientific evaluation or execution of archived code.
"""
import argparse,hashlib,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--manifest',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 m=json.loads(a.manifest.read_text(encoding='utf8'))
 if m.get('schema')!='v10-research-zip-parts-v1':raise ValueError('Unsupported manifest schema')
 root=a.manifest.resolve().parent;archive=m['archive'];parts=m['parts'];seen=set();expected=archive['path']+'.part'
 for n,r in enumerate(parts,1):
  name=r['path'];q=Path(name)
  if q.is_absolute() or '..' in q.parts or '\\' in name or '\0' in name or name in seen:raise ValueError('Unsafe or duplicate part name')
  if name!=expected+str(n).zfill(4):raise ValueError('Parts must be complete and ordered')
  seen.add(name);source=root/q
  if source.is_symlink() or not source.is_file():raise ValueError('Missing or linked part: '+name)
  b=source.read_bytes()
  if len(b)!=r['bytes'] or hashlib.sha256(b).hexdigest()!=r['sha256']:raise ValueError('Part integrity failure: '+name)
 if a.output.exists() or a.output.is_symlink():raise ValueError('Output already exists; refusing overwrite')
 h=hashlib.sha256();size=0
 with a.output.open('xb') as out:
  for r in parts:
   b=(root/r['path']).read_bytes()
   if len(b)!=r['bytes'] or hashlib.sha256(b).hexdigest()!=r['sha256']:raise ValueError('Part changed after initial verification')
   out.write(b);h.update(b);size+=len(b)
 if size!=archive['bytes'] or h.hexdigest()!=archive['sha256']:raise ValueError('Archive mismatch; output is not certified')
 print(json.dumps({'output':str(a.output),'bytes':size,'sha256':h.hexdigest(),'status':'exact_archive_rebuilt','scope':'Transport integrity only; archive contents were not executed.'},indent=2))
if __name__=='__main__':main()
