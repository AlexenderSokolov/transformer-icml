#!/usr/bin/env python3
"""Validate public source identities, then replay exact finite diagnostics in a temporary copy."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile

STAGE = 'v10_research/legal_conditional_training_20261103'
PROV = 'provenance/legal_conditional_training_20261103'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


def main():
    require(not sys.flags.optimize, 'Optimized Python disables scientific assertions; use ordinary python3.')
    root = Path(__file__).resolve().parents[2]
    inventory_path = root
    for part in ('provenance', 'PUBLIC_INVENTORY.json'):
        inventory_path = inventory_path / part
        require(not inventory_path.is_symlink(), 'Symlink inventory path refused')
    require(inventory_path.is_file(), 'Missing public inventory')
    inventory = json.loads(inventory_path.read_text())
    rows = {f['path']: f for f in inventory['files']}
    require(len(rows) == len(inventory['files']), 'Duplicate inventory path')
    verified = {}

    def read(path):
        p = PurePosixPath(path)
        require(not p.is_absolute() and '..' not in p.parts and str(p) == path, 'Unsafe public path')
        require(path in rows, 'Path absent from public inventory: ' + path)
        current = root
        for part in p.parts:
            current = current / part
            require(not current.is_symlink(), 'Symlink input refused: ' + path)
        require(current.is_file(), 'Missing input: ' + path)
        data = current.read_bytes()
        require(identity(data) == {k: rows[path][k] for k in identity(data)}, 'Public identity mismatch: ' + path)
        verified[path] = data
        return data

    read(PROV + '/verify_public_replay.py')
    source_map = json.loads(read(PROV + '/SOURCE_EXPORT_MAP.json'))
    reconciliation = json.loads(read(PROV + '/PUBLIC_EXPORT_RECONCILIATION.json'))
    selected = {f['path']: f for f in source_map['files']}
    require(len(selected) == 28 and len(source_map['files']) == 28, 'Unexpected stage selection')
    for path, f in selected.items():
        data = read(path)
        require(f['original'] == f['public'] == identity(data) and not f['changed'], 'Selected scientific source changed')
    inherited = {f['path']: f for f in reconciliation['inherited_dependencies']}
    require(len(inherited) == 5, 'Unexpected inherited dependency set')
    for path, f in inherited.items():
        data = read(path)
        require(identity(data) == f['public'], 'Inherited public identity mismatch')
        if f['original'] != f['public']:
            old_map = json.loads(read(f['existing_identity_map']))
            matches = [m for m in old_map['files'] if m['path'] == path]
            require(len(matches) == 1 and matches[0]['original'] == f['original'] and
                    matches[0]['public'] == f['public'], 'Undeclared original/public pair')
        else:
            require(f['original'] == identity(data), 'Exact inherited identity mismatch')

    bound = []
    for line in verified[STAGE + '/SOURCE_HASHES.txt'].decode().splitlines():
        expected, path = line.split(None, 1)
        bound.append((path.strip(), expected))
    bound.extend(json.loads(verified[STAGE + '/review_independent/INPUT_BINDINGS.json']).items())
    mapped_count = 0
    for path, expected in bound:
        require(path in selected or path in inherited, 'Unresolved source binding: ' + path)
        entry = selected.get(path, inherited.get(path))
        require(entry['original']['sha256'] == expected, 'Unexpected original source hash: ' + path)
        require(identity(verified[path]) == entry['public'], 'Public source identity mismatch')
        mapped_count += entry['original'] != entry['public']
    require(len(bound) == 37 and mapped_count == 2, 'Unexpected source reconciliation counts')
    jobs = [
        ('check_fraction.py', ['check_fraction.log', 'review_independent/author_fraction_replay.log']),
        ('check_game_exact.py', ['check_game_exact.log', 'review_independent/author_game_replay.log']),
        ('check_flow.py', ['check_flow.log', 'review_independent/author_flow_replay.log']),
        ('review_independent/check_independent.py', ['review_independent/check_independent.log']),
    ]
    results = []
    with tempfile.TemporaryDirectory(prefix='legal-conditional-replay-') as tmp:
        work = Path(tmp)
        for path in sorted(set(selected) | set(inherited)):
            dest = work / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open('xb') as f:
                f.write(verified[path])
        for script, logs in jobs:
            proc = subprocess.run([sys.executable, '-I', str(work / STAGE / script)],
                                  cwd=work, capture_output=True, timeout=120, check=False)
            require(proc.returncode == 0 and not proc.stderr, 'Diagnostic failed: ' + script)
            for log in logs:
                require(proc.stdout == verified[STAGE + '/' + log], 'Archived output differs: ' + log)
            results.append({'script': script, 'matched_logs': logs, 'stdout_sha256': hashlib.sha256(proc.stdout).hexdigest()})
    for path, data in verified.items():
        require((root / path).read_bytes() == data, 'Public source changed during replay')
    print(json.dumps({'status': 'PASS', 'selected_sources': 28, 'inherited_dependencies': 5,
                      'binding_occurrences': len(bound), 'declared_inherited_pairs': mapped_count,
                      'verified_public_files': len(verified), 'diagnostics': results,
                      'scientific_sources_changed': False, 'training_performed': False}, indent=2))


if __name__ == '__main__':
    main()
