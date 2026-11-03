#!/usr/bin/env python3
"""Read-only, bounded full-trace byte/schema verification; optional exact reconstruction.

Run with Python 3.10+ on POSIX: python -I -B verify_full_trace.py ROOT
  --manifest-sha256 TRUSTED_SHA256 [--reconstruct-to NEW_ROOT]
The manifest anchor must come from a trusted release receipt or commit. This
helper never executes/imports archived programs or re-evaluates the science.
"""
import sys
if not sys.flags.isolated or not sys.dont_write_bytecode:
    print('{"status":"FAIL","error":"Run this helper with python -I -B."}')
    raise SystemExit(2)
import argparse
import hashlib
import json
import math
import os
import re
import stat

PREFIX = 'provenance/t1t2_unknown_u_20261103'
MANIFEST_PATH = PREFIX + '/FULL_TRACE_CHUNKS.json'
SOURCE_PATH = 'v10_research/route_a_bos_causal_compile_20261103_1411/full_trace_cases_v1.jsonl'
SOURCE_BYTES = 79712544
SOURCE_SHA256 = 'b2559d1d28cf43d54a42f12adff27b65d1fbdb113a2fc1ed13b347b9cc0f34cf'
SOURCE_ROWS = 1008
MAX_CHUNK = 4 * 1024 * 1024
MAX_LINE = 256 * 1024
MAX_JSON = 4 * 1024 * 1024
BINDING_HASHES = {
    'schema_sha256': '5d2e0cc8b598e4c7d53ac7974a5bbdfc366fd7aeef5cd581ab0189cfd9f0e0d2',
    'layout_sha256': '13e50cde5084938e28bf6cef2bcf5b639ab7954b2b16261884b214303f0fa1c4',
    'report_sha256': '79e81b718fbb89990d4a679fbd6fd5f1aec30a65e29ac8ddb9fb43cca5afec3a',
    'checker_sha256': '795823bb3aad9b96558a1ee09d29a32d2028a7d855aef75176e9f16862e82cdf',
}
BINDING_BYTES = dict(zip(BINDING_HASHES, (4387, 2974, 12199, 12203)))
BINDING_FILES = dict(zip(BINDING_HASHES, (
    'full_trace_schema_candidate_v1.html', 'trace_layout_candidate_v1.html',
    'no_bos_causal_compilation_reviewed_v4.html', 'full_trace_checker_candidate_v5.py')))

class VerificationError(ValueError):
    """An explicit safety, transport or retained-schema check failed."""

def require(ok, message):
    if not ok:
        raise VerificationError(message)

def fields(value, names):
    require(type(value) is dict and set(value) == set(names.split()), 'unexpected or missing schema field')

def integer(value, low=0, high=128):
    require(type(value) is int and low <= value <= high, 'invalid bounded integer')
    return value

def digest(value):
    require(type(value) is str and re.fullmatch('[0-9a-f]{64}', value) is not None, 'invalid SHA256')
    return value

def safe_path(path):
    require(type(path) is str and 0 < len(path) <= 512 and not path.startswith('/') and '\\' not in path, 'unsafe relative path')
    parts = path.split('/')
    require(len(parts) <= 20 and all(p not in ('', '.', '..') and all(32 <= ord(c) < 127 for c in p) for p in parts), 'unsafe path component')
    return path

def strict_json(raw, limit=MAX_JSON):
    require(type(raw) is bytes and 0 < len(raw) <= limit and not raw.startswith(b'\xef\xbb\xbf'), 'invalid JSON byte size or BOM')
    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, 'duplicate JSON object key')
            out[key] = value
        return out
    def parse_integer(value):
        require(len(value.lstrip('-')) <= 40, 'JSON integer too long')
        out = int(value)
        require(abs(out).bit_length() <= 128, 'JSON integer too large')
        return out
    def reject(value):
        raise VerificationError('floating and nonfinite JSON numbers are forbidden')
    try:
        out = json.loads(raw.decode('utf-8'), object_pairs_hook=pairs,
                         parse_int=parse_integer, parse_float=reject, parse_constant=reject)
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise VerificationError('invalid strict JSON') from exc
    budget = [0]
    def inspect(value, depth):
        budget[0] += 1
        require(depth <= 24 and budget[0] <= 100000, 'JSON structure limit')
        if type(value) is dict:
            require(len(value) <= 256, 'too many JSON object fields')
            for key, item in value.items():
                require(len(key) <= 512 and not any(0xD800 <= ord(c) <= 0xDFFF for c in key), 'invalid JSON key')
                inspect(item, depth + 1)
        elif type(value) is list:
            require(len(value) <= 8192, 'JSON array too long')
            for item in value:
                inspect(item, depth + 1)
        elif type(value) is str:
            require(len(value) <= 4096 and not any(0xD800 <= ord(c) <= 0xDFFF for c in value), 'invalid JSON string')
    inspect(out, 0)
    return out

def identity(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)

class SafeTree:
    """Descriptor-relative POSIX access: no symlink component or special file."""
    def __init__(self, root):
        require(hasattr(os, 'O_NOFOLLOW') and hasattr(os, 'O_DIRECTORY') and os.open in os.supports_dir_fd, 'safe POSIX file access unavailable')
        self.fd = None
        fd = None
        try:
            root = os.fspath(root)
            require(type(root) is str and root and '\x00' not in root and '..' not in root.split('/'), 'unsafe root')
            absolute = root if root.startswith('/') else os.getcwd() + '/' + root
            fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            for part in absolute.split('/')[1:]:
                if part in ('', '.'):
                    continue
                nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                os.close(fd)
                fd = nxt
            self.fd, fd = fd, None
        except (OSError, ValueError, TypeError) as exc:
            raise VerificationError('root must be an accessible non-symlink directory') from exc
        finally:
            if fd is not None:
                os.close(fd)

    def __enter__(self):
        return self

    def __exit__(self, *unused):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

    def directory(self, path):
        safe_path(path)
        fd = os.dup(self.fd)
        try:
            for part in path.split('/'):
                nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                os.close(fd)
                fd = nxt
            result, fd = fd, None
            return result
        except OSError as exc:
            raise VerificationError('unsafe or missing directory: ' + path) from exc
        finally:
            if fd is not None:
                os.close(fd)

    def blocks(self, path, limit):
        safe_path(path)
        parent = fd = None
        try:
            parts = path.split('/')
            parent = self.directory('/'.join(parts[:-1])) if len(parts) > 1 else os.dup(self.fd)
            fd = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
            before = os.fstat(fd)
            require(stat.S_ISREG(before.st_mode) and 0 <= before.st_size <= limit, 'input must be a bounded regular file')
            size = 0
            while True:
                block = os.read(fd, min(65536, limit + 1 - size))
                if not block:
                    break
                size += len(block)
                require(size <= limit, 'input grew beyond limit')
                yield block
            after = os.fstat(fd)
            require(identity(before) == identity(after) and size == before.st_size, 'input changed during read')
        except OSError as exc:
            raise VerificationError('unsafe or unreadable file: ' + path) from exc
        finally:
            if fd is not None:
                os.close(fd)
            if parent is not None:
                os.close(parent)

    def read(self, path, limit=MAX_JSON):
        return b''.join(self.blocks(path, limit))

def rational(value):
    fields(value, 'numerator denominator')
    n = integer(value['numerator'], -(2**128 - 1), 2**128 - 1)
    d = integer(value['denominator'], 1, 2**128 - 1)
    require(math.gcd(n, d) == 1, 'noncanonical rational')
    return n, d

def numeric(value):
    if type(value) is int:
        integer(value, -(2**128 - 1), 2**128 - 1)
    else:
        rational(value)

def array(value, count=None, limit=128):
    require(type(value) is list and len(value) <= limit and (count is None or len(value) == count), 'invalid array shape')
    return value

def bits(value, count):
    array(value, count)
    for bit in value:
        integer(bit, 0, 1)

def sparse(value, dimension):
    fields(value, 'dimension entries')
    require(integer(value['dimension'], 1, 128) == dimension, 'sparse dimension mismatch')
    previous = -1
    for entry in array(value['entries']):
        array(entry, 2)
        index = integer(entry[0], 0, dimension - 1)
        require(index > previous, 'sparse indices must be sorted and unique')
        require(rational(entry[1])[0] != 0, 'sparse entry must be nonzero')
        previous = index

def assertion_keys(n):
    names = set('output_simplex second_mask second_projection second_normalization second_residual_and_zero_components independent_match_count error_contamination error_eta n3_or_zero_count_recorded exception_free'.split())
    for i in range(1, n + 1):
        for lag in (1, 2):
            for name in ('normalization', 'mask', 'projection'):
                names.add(f'copy_{i}_{lag}_{name}')
            if i - lag >= 1:
                names.add(f'copy_{i}_{lag}_margin')
        for name in ('attention_residual', 'ffn_residual', 'value', 'bit_retained', 'oracle_edge'):
            names.add(f'{name}_{i}')
        for kind in ('K', 'Q'):
            for pattern in ('00', '01', '10', '11'):
                names.add(f'gate_{i}_{kind}_{pattern}')
    return names

def attention(value, edges, head_dim, second=False):
    common = 'Q_coefficient_ln2 edges numerator denominator output'
    extra = 'probabilities pre_residual_state output_projection_write zero_head_write zero_ffn_write post_residual_state' if second else 'lag'
    fields(value, common + ' ' + extra)
    sparse(value['Q_coefficient_ln2'], head_dim)
    for name in ('numerator', 'denominator', 'output'):
        rational(value[name])
    require(value['denominator']['numerator'] > 0, 'saved attention denominator must be positive')
    for j, edge in enumerate(array(value['edges'], edges), 1):
        fields(edge, 'j K V dot_coefficient_ln2 score_coefficient_ln2 row_max_coefficient_ln2 row_shift_coefficient_ln2 centered_coefficient_ln2 weight numerator_contribution denominator_contribution' + (' first_flag match' if second else ''))
        require(integer(edge['j'], 1, 8) == j, 'saved edge order')
        sparse(edge['K'], head_dim)
        for name in ('V', 'dot_coefficient_ln2', 'score_coefficient_ln2', 'weight', 'numerator_contribution', 'denominator_contribution'):
            rational(edge[name])
        for name in ('row_max_coefficient_ln2', 'row_shift_coefficient_ln2', 'centered_coefficient_ln2'):
            numeric(edge[name])
        require(edge['weight']['numerator'] >= 0, 'negative saved weight')
        if second:
            for name in ('first_flag', 'match'):
                require(rational(edge[name]) in ((0, 1), (1, 1)), 'saved flag must be zero or one')

def validate_row(row, index):
    fields(row, 'schema schema_sha256 layout_sha256 report_sha256 checker_sha256 case_index N bits eta b c failure_stage bit_vector D head_dim model_dim layout projection_maps input_states first_attention first_ffn second_attention oracle assertions partial_work passed stage_status')
    require(row['schema'] == 'one_hot_full_trace_v1', 'unsupported retained row schema')
    require(integer(row['case_index'], 1, SOURCE_ROWS) == index, 'saved record index')
    for field, expected in BINDING_HASHES.items():
        require(row[field] == expected, 'historical source hash differs: ' + field)
    n = integer(row['N'], 3, 8)
    word = row['bits']
    require(type(word) is str and len(word) == n and set(word) <= {'0', '1'}, 'saved binary word shape')
    bits(row['bit_vector'], n)
    require(row['bit_vector'] == [int(bit) for bit in word], 'saved bit vector mismatch')
    eta = rational(row['eta'])
    require(eta in ((1, 4), (1, 32)), 'saved eta outside archive scope')
    expected_index = sum(2 * (1 << k) for k in range(3, n)) + (0 if eta == (1, 4) else 1 << n) + int(word, 2) + 1
    require(index == expected_index, 'saved coverage identity/order mismatch')
    integer(row['b'], 4, 8)
    integer(row['c'], 7, 9)
    integer(row['D'], 1, 128)
    hd = integer(row['head_dim'], 1, 128)
    md = integer(row['model_dim'], 1, 128)
    require(row['failure_stage'] is None and row['partial_work'] is None, 'saved row is incomplete')
    fields(row['stage_status'], 'case_setup first_attention first_ffn second_attention_and_oracle')
    require(all(v == 'completed' for v in row['stage_status'].values()), 'saved stage is not completed')
    require(type(row['assertions']) is dict and set(row['assertions']) == assertion_keys(n), 'saved assertion names')
    require(all(value is True for value in row['assertions'].values()) and row['passed'] is True, 'saved pass status is not true')
    layout = row['layout']
    fields(layout, 'one x v z positions copy1 copy2 K Q Y output')
    for name, value in layout.items():
        if name in ('positions', 'K', 'Q'):
            array(value, 2)
            start, end = (integer(x, 0, md - 1) for x in value)
            require(start <= end, 'reversed layout interval')
            require(end - start + 1 == (n if name == 'positions' else 4), 'layout interval shape')
        else:
            integer(value, 0, md - 1)
    maps = row['projection_maps']
    fields(maps, 'offn o1_lag1 o1_lag2 o2 q1_lag1 q1_lag2 k1_lag1 k1_lag2 v1 q2 k2 v2')
    for name, triples in maps.items():
        out_dim, in_dim = (md, 9) if name == 'offn' else ((md, hd) if name.startswith('o') else (hd, md))
        seen = set()
        for triple in array(triples):
            array(triple, 3)
            pair = (integer(triple[0], 0, out_dim - 1), integer(triple[1], 0, in_dim - 1))
            require(pair not in seen, 'duplicate saved projection coordinate')
            seen.add(pair)
            rational(triple[2])
    for value in array(row['input_states'], n):
        sparse(value, md)
    array(row['first_attention'], n)
    array(row['first_ffn'], n)
    for i, (a, ffn) in enumerate(zip(row['first_attention'], row['first_ffn']), 1):
        fields(a, 'i heads pre_residual_state output_projection_writes post_attention_residual_state')
        require(integer(a['i'], 1, n) == i, 'saved attention position order')
        for lag, head in enumerate(array(a['heads'], 2), 1):
            attention(head, i, hd)
            require(integer(head['lag'], 1, 2) == lag, 'saved head lag order')
        for value in array(a['output_projection_writes'], 2):
            sparse(value, md)
        for name in ('pre_residual_state', 'post_attention_residual_state'):
            sparse(a[name], md)
        fields(ffn, 'i gates Y_input_x Y_z Y_hinge Y ffn_features pre_residual_state ffn_write post_residual_state')
        require(integer(ffn['i'], 1, n) == i, 'saved FFN position order')
        require(a['pre_residual_state'] == row['input_states'][i - 1] and a['post_attention_residual_state'] == ffn['pre_residual_state'], 'saved state continuity mismatch')
        for name in ('Y_input_x', 'Y_z', 'Y_hinge', 'Y'):
            rational(ffn[name])
        sparse(ffn['ffn_features'], 9)
        for name in ('pre_residual_state', 'ffn_write', 'post_residual_state'):
            sparse(ffn[name], md)
        for gindex, gate in enumerate(array(ffn['gates'], 8)):
            fields(gate, 'type pattern input_1 input_2 sum preactivation_1 preactivation_2 hinge_1 hinge_2 output oracle destination')
            require(gate['type'] == ('K' if gindex < 4 else 'Q'), 'saved gate type order')
            bits(gate['pattern'], 2)
            require(gate['pattern'] == [gindex % 4 // 2, gindex % 2], 'saved gate pattern order')
            integer(gate['destination'], 0, md - 1)
            integer(gate['oracle'], 0, 1)
            for name in ('input_1', 'input_2', 'sum', 'preactivation_1', 'preactivation_2', 'hinge_1', 'hinge_2', 'output'):
                rational(gate[name])
    a = row['second_attention']
    attention(a, n, hd, second=True)
    for name in ('pre_residual_state', 'output_projection_write', 'zero_head_write', 'zero_ffn_write', 'post_residual_state'):
        sparse(a[name], md)
    require(a['pre_residual_state'] == row['first_ffn'][-1]['post_residual_state'], 'saved terminal state continuity')
    require(not a['zero_head_write']['entries'] and not a['zero_ffn_write']['entries'], 'saved zero component contains entries')
    for probability in array(a['probabilities'], 2):
        num, den = rational(probability)
        require(0 <= num <= den, 'saved probability outside unit interval')
    oracle = row['oracle']
    fields(oracle, 'target candidates J C add_one absolute_error contamination_bound')
    bits(oracle['target'], 2)
    j_count = integer(oracle['J'], 0, n - 2)
    integer(oracle['C'], 0, j_count)
    for name in ('add_one', 'absolute_error', 'contamination_bound'):
        require(rational(oracle[name])[0] >= 0, 'negative saved oracle quantity')
    for j, candidate in enumerate(array(oracle['candidates'], n - 2), 3):
        fields(candidate, 'j pair match value')
        require(integer(candidate['j'], 3, n) == j, 'saved candidate order')
        bits(candidate['pair'], 2)
        require(type(candidate['match']) is bool, 'saved candidate match must be boolean')
        integer(candidate['value'], 0, 1)
    # No projections, score/exponential/hinge evaluations, arithmetic replay or
    # matching of raw input bits against oracle candidates occurs here.

class Coverage:
    def __init__(self):
        self.rows = self.n3 = self.zero = self.assertions = 0
        self.counts = {}

    def accept(self, row, index):
        require(index == self.rows + 1, 'nonsequential row callback')
        validate_row(row, index)
        self.rows += 1
        self.n3 += row['N'] == 3
        self.zero += row['oracle']['J'] == 0
        self.assertions += len(row['assertions'])
        key = str(row['N']) + ':1/' + str(row['eta']['denominator'])
        self.counts[key] = self.counts.get(key, 0) + 1

    def finish(self):
        require(self.rows == 1008 and self.n3 == 16 and self.zero == 236 and self.assertions == 157248, 'retained coverage/status census mismatch')
        require(self.counts == {str(n) + ':1/' + str(d): 1 << n for n in range(3, 9) for d in (4, 32)}, 'retained coverage groups mismatch')
        return {'rows': self.rows, 'recorded_passed': self.rows, 'recorded_failed': 0,
                'N3_records': self.n3, 'recorded_J_zero': self.zero,
                'recorded_true_assertions': self.assertions, 'coverage': self.counts}

def validate_transport(source, chunks):
    fields(source, 'path bytes sha256 rows')
    safe_path(source['path'])
    integer(source['bytes'], 1, 128 * 1024 * 1024)
    integer(source['rows'], 1, 2048)
    digest(source['sha256'])
    array(chunks, limit=64)
    require(chunks, 'missing chunks')
    offset = 0
    next_row = 1
    paths = set()
    for index, chunk in enumerate(chunks, 1):
        fields(chunk, 'path index offset bytes first_record last_record sha256')
        path = safe_path(chunk['path'])
        require(path not in paths and path != source['path'], 'duplicate chunk or logical source path')
        paths.add(path)
        require(integer(chunk['index'], 1, 64) == index, 'chunk index order')
        require(integer(chunk['offset'], 0, 128 * 1024 * 1024) == offset, 'chunk offset gap or overlap')
        offset += integer(chunk['bytes'], 1, MAX_CHUNK)
        require(integer(chunk['first_record'], 1, 2048) == next_row, 'chunk record gap or overlap')
        next_row = integer(chunk['last_record'], next_row, 2048) + 1
        digest(chunk['sha256'])
    require(offset == source['bytes'] and next_row == source['rows'] + 1, 'chunk source totals mismatch')

def stream_chunks(tree, source, chunks, row_callback=None, output_fd=None):
    """Verify bounded chunks, optionally copy the same raw bytes. No reserialization."""
    validate_transport(source, chunks)
    total = row_index = 0
    combined = hashlib.sha256()
    for chunk in chunks:
        count = 0
        part_hash = hashlib.sha256()
        pending = bytearray()
        require(row_index + 1 == chunk['first_record'], 'chunk first record mismatch')
        for block in tree.blocks(chunk['path'], MAX_CHUNK):
            count += len(block)
            total += len(block)
            part_hash.update(block)
            combined.update(block)
            if output_fd is not None:
                rest = memoryview(block)
                while rest:
                    written = os.write(output_fd, rest)
                    require(written > 0, 'short reconstruction write')
                    rest = rest[written:]
            pending.extend(block)
            while True:
                end = pending.find(b'\n')
                if end < 0:
                    break
                require(end + 1 <= MAX_LINE, 'saved JSON line exceeds bound')
                raw = bytes(pending[:end + 1])
                del pending[:end + 1]
                require(raw != b'\n' and b'\r' not in raw, 'empty line or unexpected carriage return')
                row_index += 1
                require(row_index <= source['rows'], 'too many saved rows')
                row = strict_json(raw, MAX_LINE)
                if row_callback is not None:
                    row_callback(row, row_index)
            require(len(pending) <= MAX_LINE, 'saved JSON line exceeds bound')
        require(not pending, 'chunk must end on an original newline')
        require(count == chunk['bytes'] and part_hash.hexdigest() == chunk['sha256'], 'chunk byte/hash mismatch')
        require(row_index == chunk['last_record'], 'chunk last record mismatch')
    require(total == source['bytes'] and combined.hexdigest() == source['sha256'] and row_index == source['rows'], 'concatenated source identity mismatch')
    return {'bytes': total, 'sha256': combined.hexdigest(), 'rows': row_index, 'chunks': len(chunks)}

def validate_bindings(tree, bindings):
    array(bindings, 4)
    seen = set()
    cached_maps = {}
    for binding in bindings:
        fields(binding, 'field original_path original_sha256 public_path public_bytes public_sha256 source_map')
        field = binding['field']
        require(type(field) is str and field in BINDING_HASHES and field not in seen, 'duplicate or unknown source binding')
        seen.add(field)
        expected_path = SOURCE_PATH.rsplit('/', 1)[0] + '/' + BINDING_FILES[field]
        require(binding['original_path'] == binding['public_path'] == expected_path, 'source binding path mismatch')
        require(binding['original_sha256'] == BINDING_HASHES[field], 'original source binding hash mismatch')
        digest(binding['public_sha256'])
        integer(binding['public_bytes'], 1, MAX_JSON)
        reference = binding['source_map']
        fields(reference, 'path sha256 source_record_id')
        safe_path(reference['path'])
        digest(reference['sha256'])
        require(type(reference['source_record_id']) is str and re.fullmatch('[A-Z0-9_-]{1,64}', reference['source_record_id']), 'invalid source record ID')
        key = (reference['path'], reference['sha256'])
        if key not in cached_maps:
            raw = tree.read(reference['path'])
            require(hashlib.sha256(raw).hexdigest() == reference['sha256'], 'source map hash mismatch')
            source_map = strict_json(raw)
            require(type(source_map) is dict and source_map.get('schema') in ('t1t2-unknown-u-source-export-v1', 't1t2-followon-source-export-v1') and type(source_map.get('files')) is list, 'invalid referenced source map')
            require(type(source_map.get('source_count')) is int and source_map['source_count'] == len(source_map['files']) <= 1024, 'invalid source-map record count')
            cached_maps[key] = source_map['files']
        entries = [item for item in cached_maps[key] if type(item) is dict and item.get('source_record_id') == reference['source_record_id']]
        require(len(entries) == 1, 'source-map record is missing or ambiguous')
        entry = entries[0]
        fields(entry, 'source_record_id path original public changed' + (' storage' if 'storage' in entry else ''))
        for identity_name in ('original', 'public'):
            fields(entry[identity_name], 'bytes sha256 git_blob_sha1')
            integer(entry[identity_name]['bytes'], 0, MAX_JSON)
            digest(entry[identity_name]['sha256'])
            require(type(entry[identity_name]['git_blob_sha1']) is str and re.fullmatch('[0-9a-f]{40}', entry[identity_name]['git_blob_sha1']), 'invalid source-map Git identity')
        require(entry['original']['bytes'] == BINDING_BYTES[field], 'source-map original byte size mismatch')
        require(type(entry['changed']) is bool and entry['changed'] == (entry['original'] != entry['public']), 'source-map changed status mismatch')
        if 'storage' in entry:
            fields(entry['storage'], 'kind path')
            require(entry['storage'] == {'kind': 'file', 'path': expected_path}, 'invalid ordinary source binding storage')
        require(entry.get('path') == expected_path and type(entry.get('original')) is dict and type(entry.get('public')) is dict, 'source-map path or identity mismatch')
        require(entry['original'].get('sha256') == binding['original_sha256'], 'source-map original binding mismatch')
        require(entry['public'].get('sha256') == binding['public_sha256'] and entry['public'].get('bytes') == binding['public_bytes'] and type(entry['public'].get('bytes')) is int, 'source-map public binding mismatch')
        raw = tree.read(expected_path)
        require(len(raw) == binding['public_bytes'] and hashlib.sha256(raw).hexdigest() == binding['public_sha256'], 'public source binding byte/hash mismatch')
        require(hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest() == entry['public']['git_blob_sha1'], 'public source binding Git identity mismatch')
    require(seen == set(BINDING_HASHES), 'incomplete original source bindings')

def load_manifest(tree, trusted_sha256):
    digest(trusted_sha256)
    raw = tree.read(MANIFEST_PATH)
    require(hashlib.sha256(raw).hexdigest() == trusted_sha256, 'trusted chunk manifest hash mismatch')
    manifest = strict_json(raw)
    fields(manifest, 'schema source chunks bindings')
    require(manifest['schema'] == 't1t2-full-trace-chunks-v1', 'unsupported chunk manifest schema')
    source = manifest['source']
    validate_transport(source, manifest['chunks'])
    require(source == {'path': SOURCE_PATH, 'bytes': SOURCE_BYTES, 'sha256': SOURCE_SHA256, 'rows': SOURCE_ROWS}, 'manifest differs from pinned original full trace')
    for index, chunk in enumerate(manifest['chunks'], 1):
        require(chunk['path'] == PREFIX + '/full_trace_chunks/part' + str(index).zfill(3) + '.jsonl', 'noncanonical public chunk path')
    validate_bindings(tree, manifest['bindings'])
    return manifest

def reconstruct(tree, source, chunks, destination):
    """Write ONLY raw verified source bytes inside an exclusively NEW root.

    The caller verifies the entire archive before calling this function. This
    function verifies chunk bytes again while copying to detect later changes.
    On failure the partial output file is unlinked; newly made empty directories
    may remain as evidence. No existing file or directory is overwritten.
    """
    validate_transport(source, chunks)
    try:
        destination = os.fspath(destination)
        require(type(destination) is str and destination and '\x00' not in destination and '..' not in destination.split('/'), 'unsafe destination')
        require(not destination.endswith('/'), 'destination must name a NEW directory')
        parent_path, name = os.path.split(destination)
        safe_path(name)
        require('/' not in name, 'invalid destination name')
        with SafeTree(parent_path or '.') as parent:
            # mkdir is intentionally exclusive, including an existing symlink.
            os.mkdir(name, mode=0o700, dir_fd=parent.fd)
            root_fd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent.fd)
        fd = file_fd = None
        made_file = False
        filename = source['path'].split('/')[-1]
        try:
            fd = os.dup(root_fd)
            for part in source['path'].split('/')[:-1]:
                os.mkdir(part, mode=0o700, dir_fd=fd)
                nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                os.close(fd)
                fd = nxt
            file_fd = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=fd)
            made_file = True
            stream_chunks(tree, source, chunks, output_fd=file_fd)
            os.fsync(file_fd)
            require(os.fstat(file_fd).st_size == source['bytes'], 'reconstruction size mismatch')
            os.close(file_fd)
            file_fd = None
            made_file = False
        finally:
            if file_fd is not None:
                os.close(file_fd)
            if made_file:
                os.unlink(filename, dir_fd=fd)
            if fd is not None:
                os.close(fd)
            os.close(root_fd)
        return source['path']
    except OSError as exc:
        raise VerificationError('reconstruction destination must be new, exclusive and writable; no symlink ancestors') from exc

def verify(root, trusted_sha256, destination=None):
    with SafeTree(root) as tree:
        manifest = load_manifest(tree, trusted_sha256)
        coverage = Coverage()
        result = stream_chunks(tree, manifest['source'], manifest['chunks'], coverage.accept)
        result.update(coverage.finish())
        result['status'] = 'PASS_ARCHIVED_BYTES_AND_SAVED_SCHEMA_ONLY'
        result['source_path'] = SOURCE_PATH
        result['historical_source_bindings'] = 'four original hashes resolved through pinned source-map files'
        result['scientific_replay'] = False
        result['reconstructed'] = False
        if destination is not None:
            result['reconstructed_path'] = reconstruct(tree, manifest['source'], manifest['chunks'], destination)
            result['reconstructed'] = True
        return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', help='public archive root; read-only by default')
    parser.add_argument('--manifest-sha256', required=True, help='externally trusted FULL_TRACE_CHUNKS.json SHA256')
    parser.add_argument('--reconstruct-to', help='explicitly create this NEW exclusive directory and original-relative full trace file')
    args = parser.parse_args()
    try:
        result = verify(args.root, args.manifest_sha256, args.reconstruct_to)
    except (VerificationError, OSError, ValueError, TypeError, KeyError, RecursionError) as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
