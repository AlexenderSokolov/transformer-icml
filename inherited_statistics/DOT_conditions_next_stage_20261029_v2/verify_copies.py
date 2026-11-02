#!/usr/bin/env python3
"""Read-only integrity verification; optionally compare with supplied originals.
This checks bytes and hashes, not mathematical correctness. No network or writes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile
import io
import stat
from pathlib import PurePosixPath

def digest(b):
    return hashlib.sha256(b).hexdigest()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def interval(entry, prefix, size):
    a, b = entry[prefix + '_byte_start'], entry[prefix + '_byte_end']
    require(isinstance(a, int) and isinstance(b, int) and 0 <= a < b <= size,
            'Invalid ' + prefix + ' interval')
    return a, b

def partition(parts, size, label):
    position = 0
    for a, b in sorted(parts):
        require(a == position, 'Gap or overlap in ' + label)
        position = b
    require(position == size, 'Incomplete ' + label)

def original_for(record, supplied):
    if supplied is None:
        return None
    matches = [p for p in supplied.rglob(record['source'])
               if p.is_file() and digest(p.read_bytes()) == record['source_sha256']]
    require(bool(matches), 'Missing exact original: ' + record['source'])
    return matches[0].read_bytes()

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--sources', type=Path, help='Root containing supplied original source basenames and bytes')
args = parser.parse_args()
root = Path(__file__).absolute().parent
public_paths = list(root.rglob('*'))
require(all(not p.is_symlink() for p in public_paths), 'Public symlink')
manifest = (root / 'SHA256SUMS.txt').read_text(encoding='utf-8')
manifest_names = set()
for line in manifest.splitlines():
    h, name = line.split('  ', 1)
    require(name not in manifest_names, 'Duplicate public manifest name')
    path = PurePosixPath(name)
    require(not path.is_absolute() and '..' not in path.parts, 'Unsafe public path')
    require(digest((root / name).read_bytes()) == h, 'Public hash differs: ' + name)
    manifest_names.add(name)
actual_names = {p.relative_to(root).as_posix() for p in public_paths if p.is_file()}
require(actual_names == manifest_names | {'SHA256SUMS.txt'}, 'Public inventory differs')
mapping = json.loads((root / 'COPY_MAP.json').read_text(encoding='utf-8'))
count = 0
for r in mapping['records']:
    output = (root / r['output']).read_bytes()
    require(len(output) == r['output_bytes'] and digest(output) == r['output_sha256'], r['output'])
    original = original_for(r, args.sources)
    if original is not None:
        require(len(original) == r['source_bytes'], r['source'])
    srcparts, dstparts, body = [], [], []
    last_source = last_output = 0
    for span in r['spans']:
        a, b = interval(span, 'source', r['source_bytes'])
        c, d = interval(span, 'output', len(output))
        require(a >= last_source and c >= last_output, 'Unordered copied spans')
        require(b-a == d-c, 'Copy span size mismatch')
        data = output[c:d]
        require(digest(data) == span['sha256'], 'Copy span hash mismatch')
        if original is not None:
            require(data == original[a:b], 'Source bytes differ: ' + r['source'])
            require(span['source_line_start'] == original[:a].count(b'\n')+1, 'First touched line mismatch')
            require(span['source_line_end'] == original[:b-1].count(b'\n')+1, 'Last touched line mismatch')
        srcparts.append((a,b)); dstparts.append((c,d)); body.append(data)
        last_source, last_output = b, d
        count += 1
    require(digest(b''.join(body)) == r['copied_body_sha256'], 'Concatenated copied body mismatch')
    for omitted in r['omitted_source_spans']:
        a, b = interval(omitted, 'source', r['source_bytes'])
        srcparts.append((a,b))
        if original is not None:
            require(digest(original[a:b]) == omitted['sha256'], 'Omitted interval hash mismatch')
            require(omitted['source_line_start'] == original[:a].count(b'\n')+1, 'Omitted first line mismatch')
            require(omitted['source_line_end'] == original[:b-1].count(b'\n')+1, 'Omitted last line mismatch')
    for added in r['editorial_output_spans']:
        a, b = interval(added, 'output', len(output))
        require(digest(output[a:b]) == added['sha256'], 'Editorial interval hash mismatch')
        dstparts.append((a,b))
    partition(srcparts, r['source_bytes'], 'source coverage for '+r['source'])
    partition(dstparts, len(output), 'output coverage for '+r['output'])
def verify_archive(data, expected_manifest=None):
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        names=z.namelist()
        require(len(names)==len(set(names)), 'Duplicate archive member')
        for info in z.infolist():
            name=PurePosixPath(info.filename)
            require(not name.is_absolute() and '..' not in name.parts and not info.is_dir(), 'Unsafe or non-file member')
            require(not stat.S_ISLNK(info.external_attr >> 16), 'Archive symlink')
        require(z.testzip() is None, 'Archive CRC failure')
        manifests=[n for n in names if n.endswith('/SHA256SUMS.txt')]
        require(len(manifests)==1, 'Archive manifest ambiguity')
        mname=manifests[0]; prefix=mname[:-len('SHA256SUMS.txt')]
        manifest=z.read(mname)
        if expected_manifest is not None:
            require(digest(manifest)==expected_manifest, 'Archive manifest identity differs')
        expected={mname}; payloads=[]
        for line in manifest.decode('utf-8').splitlines():
            h,name=line.split('  ',1)
            require(prefix+name not in expected, 'Duplicate archive manifest entry')
            data2=z.read(prefix+name)
            require(digest(data2)==h, 'Inherited payload differs: '+name)
            expected.add(prefix+name)
            if name.endswith('.zip'):
                payloads.append(data2)
        require(set(names)==expected, 'Archive inventory differs')
        return len(names)+sum(verify_archive(b) for b in payloads)

nested_count=0
for r in mapping['binary_copies']:
    output=(root/r['output']).read_bytes()
    require(len(output)==r['output_bytes']==r['source_bytes'], 'Binary length mismatch')
    require(digest(output)==r['source_sha256']==r['output_sha256'], 'Binary identity differs')
    original=original_for(r,args.sources)
    if original is not None:
        require(original==output, 'Original archive differs')
    nested_count += verify_archive(output,r['archive_manifest_sha256'])

for record in mapping['records']+mapping['binary_copies']:
    require(record['output'] in manifest_names, 'Mapped output omitted from manifest')
scope='exact source equality and touched-line checks' if args.sources else 'delivered-byte consistency only; originals not supplied'
print(f'PASS: {len(mapping["records"])} scientific copies, {count} exact spans, {len(mapping["binary_copies"])} unchanged archive; {nested_count} nested files; {scope}.')
