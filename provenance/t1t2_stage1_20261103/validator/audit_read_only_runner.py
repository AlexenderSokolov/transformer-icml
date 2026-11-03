#!/usr/bin/env python3
"""Test harness: deny writes/network/process actions during retained checks."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
sys.dont_write_bytecode=True
here=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('retained_validator',here/'verify_retained_records.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
root=Path(sys.argv[1]);before={r['path']:hashlib.sha256((root/r['path']).read_bytes()).hexdigest() for r in v.FILE_SPECS}
observed={'opens':0,'mutations_denied':0,'network_or_process_denied':0}
def audit(event,args):
    if event=='open':
        observed['opens']+=1
        mode=args[1];flags=args[2]
        if (isinstance(mode,str) and any(x in mode for x in 'wax+')) or (isinstance(flags,int) and flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND)):
            observed['mutations_denied']+=1;raise RuntimeError('write attempted')
    if event in ('os.remove','os.rename','os.mkdir','os.rmdir','os.chmod','os.chown','os.link','os.symlink','os.truncate','os.utime'):
        observed['mutations_denied']+=1;raise RuntimeError('mutation attempted')
    if event.startswith(('socket.','subprocess.')) or event in ('os.system','os.exec','os.posix_spawn'):
        observed['network_or_process_denied']+=1;raise RuntimeError('network/process attempted')
sys.addaudithook(audit)
result=v.verify_records(root)
after={r['path']:hashlib.sha256((root/r['path']).read_bytes()).hexdigest() for r in v.FILE_SPECS}
if before!=after:raise RuntimeError('input content changed')
print(json.dumps({'result':result,'audit':observed,'all_input_hashes_unchanged':True,'input_sha256':after},sort_keys=True,indent=2))
