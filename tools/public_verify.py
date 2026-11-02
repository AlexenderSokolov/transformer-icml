#!/usr/bin/env python3
"""Check the exact public file inventory. This does not prove mathematics."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath

INVENTORY = 'provenance/PUBLIC_INVENTORY.json'

def verify(root):
    root = Path(root).resolve()
    rows = json.loads((root / INVENTORY).read_text(encoding='utf-8'))['files']
    expected = {}
    for row in rows:
        name = row['path']
        relative = PurePosixPath(name)
        if relative.is_absolute() or '..' in relative.parts or '\\' in name or str(relative) != name:
            raise ValueError('Unsafe inventory path: ' + name)
        if name in expected or name == INVENTORY:
            raise ValueError('Duplicate or self-referential inventory entry: ' + name)
        expected[name] = row
    actual = set()
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if '.git' in relative.parts or '__pycache__' in relative.parts:
            continue
        if path.is_symlink():
            raise ValueError('Symlink is not allowed: ' + relative.as_posix())
        if path.is_file() and relative.as_posix() != INVENTORY:
            actual.add(relative.as_posix())
    if actual != set(expected):
        raise ValueError('Inventory membership mismatch: missing=' + repr(sorted(set(expected) - actual)) + '; extra=' + repr(sorted(actual - set(expected))))
    total = 0
    for name, row in expected.items():
        data = (root / name).read_bytes()
        if len(data) != row['bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError('Byte/hash mismatch: ' + name)
        total += len(data)
    return {'status': 'PASS', 'files_verified': len(expected), 'bytes_verified': total, 'scope': 'Exact public bytes and membership; not a scientific replay or formal proof.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(verify(args.root), ensure_ascii=False, indent=2))
