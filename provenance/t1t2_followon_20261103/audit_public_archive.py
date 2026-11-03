#!/usr/bin/env python3
"""Audit the new pinned archive checker for writes, processes, and extra execution.

Run: python -I -B audit_public_archive.py PUBLIC_ROOT TRUSTED_MANIFEST_SHA256
This executes only the new wrapper and its hash-pinned retained-record checker.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

if not sys.flags.isolated or not sys.dont_write_bytecode:
    raise SystemExit('Use python -I -B')
HERE=Path(__file__).parent
SOURCE=HERE/'verify_public_archive.py'
WRAPPER_SHA256='e9048f6ea2d9c171b31755eda3d34e283f6dfe679576c5f0dad82f304b3ca2ad'
if hashlib.sha256(SOURCE.read_bytes()).hexdigest()!=WRAPPER_SHA256:
    raise SystemExit('wrapper pin mismatch')
spec=importlib.util.spec_from_file_location('pinned_outer_checker',SOURCE)
checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
observed={'opens':0,'mutations_attempted':0,'network_or_process_attempted':0,'pinned_helper_compiles':0,'pinned_helper_executes':0}

def audit(event,args):
    if event=='open':
        observed['opens']+=1;mode=args[1];flags=args[2]
        if (isinstance(mode,str) and any(x in mode for x in 'wax+')) or (isinstance(flags,int) and flags&(os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND)):
            observed['mutations_attempted']+=1;raise RuntimeError('write attempted')
    if event in ('os.remove','os.rename','os.mkdir','os.rmdir','os.chmod','os.chown','os.link','os.symlink','os.truncate','os.utime'):
        observed['mutations_attempted']+=1;raise RuntimeError('mutation attempted')
    if event.startswith(('socket.','subprocess.')) or event in ('os.system','os.exec','os.posix_spawn'):
        observed['network_or_process_attempted']+=1;raise RuntimeError('network or process attempted')
    if event=='compile':
        data,filename=args
        if filename!=checker.MODULE_PATH or hashlib.sha256(data).hexdigest()!=checker.MODULE_SHA256:
            raise RuntimeError('unpinned compilation attempted')
        observed['pinned_helper_compiles']+=1
    if event=='exec':
        if args[0].co_filename!=checker.MODULE_PATH:
            raise RuntimeError('unexpected code execution')
        observed['pinned_helper_executes']+=1

if len(sys.argv)!=3:raise SystemExit('Expected PUBLIC_ROOT TRUSTED_MANIFEST_SHA256')
sys.addaudithook(audit)
result=checker.verify_archive(sys.argv[1],sys.argv[2])
print(json.dumps({'wrapper_sha256':WRAPPER_SHA256,'audit':observed,'result':result},sort_keys=True,indent=2))
