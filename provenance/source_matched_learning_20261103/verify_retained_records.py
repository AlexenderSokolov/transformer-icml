#!/usr/bin/env python3
"""Read-only stdlib verification of two RETAINED later iid numeric archives.

API: verify_records(root) -> deterministic JSON-compatible report.
``root`` directly contains half_gate_iid_identifiability_20261103_1009.
Invalid input raises VerificationError. CLI prints a report to stdout only.
No imports or execution of archived programs; no records, randomness, sampling,
models, original outputs, files, or directories are created by this module.

This checks finite arithmetic for the saved 60 cases, not a universal proof.
The original diagnostic's missing exact-tail intermediates and failed-wrapper
transcript are NOT recovered by either later archive or by this verifier.
"""

from fractions import Fraction
import gzip
import hashlib
import io
import json
import os
import stat
import sys
import zlib

UNIT = 'half_gate_iid_identifiability_20261103_1009'
SOURCE_FILE = UNIT + '/comprehensive_records.jsonl'
REVIEW_FILE = UNIT + '/review_independent_20261103_1010/comprehensive_recheck_records.jsonl.gz'
M_VALUES = (8, 64, 1024, 4096, 16384)
THETA_NUMERATORS = (1, 2, 3)
ROWS = ('00', '01', '10', '11')
EXPECTED_CASES = frozenset((M, theta, row) for M in M_VALUES for theta in THETA_NUMERATORS for row in ROWS)
MAX_FILE_BYTES = 16 * 1024 * 1024
MAX_EXPANDED_BYTES = 24 * 1024 * 1024
MAX_LINE_BYTES = 1024 * 1024
MAX_DECIMAL_DIGITS = 60000
SOURCE_INT_KEYS = frozenset(('M', 'k', 'theta_num', 'theta_den', 'disjoint_pairs_n', 'match_p_num_over_16', 'mean_num', 'mean_den', 'threshold_num', 'threshold_den', 'last_included_count'))
SOURCE_KEYS = SOURCE_INT_KEYS | frozenset(('row', 'tail_denominator_decimal', 'tail_term_numerators_decimal', 'tail_numerator_decimal', 'comparison_bound', 'exact_rational_comparison_pass'))
INDEPENDENT_INT_KEYS = frozenset(('n', 'k', 'theta_num', 'theta_den', 'p_num', 'p_den', 'a', 'mean_num', 'mean_den', 'threshold_num', 'threshold_den', 'last'))
INDEPENDENT_DECIMAL_KEYS = frozenset(('denominator', 'numerator', 'bound_num', 'bound_den', 'left_cross_product', 'right_cross_product'))
INDEPENDENT_KEYS = INDEPENDENT_INT_KEYS | INDEPENDENT_DECIMAL_KEYS | frozenset(('terms', 'comparison'))


class VerificationError(ValueError):
    """The retained inputs are malformed, incomplete, unsafe, or inconsistent."""


def _require(condition, message):
    if not condition:
        raise VerificationError(message)


def _safe_read(root, relative):
    """Descriptor-relative traversal: reject every symlink and nonregular file.

    Requires POSIX O_NOFOLLOW/O_DIRECTORY; fail closed where unavailable.
    O_NONBLOCK avoids hanging when an input is a FIFO or other special file.
    Inputs are read through the checked descriptor, not reopened by pathname.
    """
    for flag in ('O_NOFOLLOW', 'O_DIRECTORY', 'O_NONBLOCK'):
        _require(hasattr(os, flag), 'safe descriptor traversal unavailable')
    try:
        root = os.fspath(root)
    except TypeError as exc:
        raise VerificationError('root must be a string or path-like object') from exc
    _require(type(root) is str and root and '\x00' not in root, 'invalid root path')
    _require('..' not in root.split('/'), 'parent traversal is forbidden')
    _require(not relative.startswith('/') and all(p not in ('', '.', '..') for p in relative.split('/')), 'invalid relative input path')
    absolute_root = os.path.abspath(root)
    parts = [p for p in absolute_root.split('/') if p]
    parts.extend(relative.split('/'))
    directory_flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = None
    file_fd = None
    try:
        fd = os.open('/', directory_flags)
        for component in parts[:-1]:
            next_fd = os.open(component, directory_flags, dir_fd=fd)
            os.close(fd)
            fd = next_fd
        file_fd = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
        before = os.fstat(file_fd)
        _require(stat.S_ISREG(before.st_mode), relative + ': not a regular file')
        _require(0 < before.st_size <= MAX_FILE_BYTES, relative + ': invalid file size')
        with os.fdopen(file_fd, 'rb') as handle:
            file_fd = None
            data = handle.read(MAX_FILE_BYTES + 1)
            after = os.fstat(handle.fileno())
        _require(len(data) <= MAX_FILE_BYTES, relative + ': exceeds file size bound')
        attributes = ('st_dev', 'st_ino', 'st_size', 'st_mtime_ns', 'st_ctime_ns')
        _require(all(getattr(before, a) == getattr(after, a) for a in attributes), relative + ': input changed during read')
        _require(len(data) == before.st_size, relative + ': incomplete input read')
        return data
    except (OSError, TypeError, ValueError) as exc:
        if isinstance(exc, VerificationError):
            raise
        raise VerificationError(relative + ': safe read failed (' + type(exc).__name__ + ')') from exc
    finally:
        if file_fd is not None:
            os.close(file_fd)
        if fd is not None:
            os.close(fd)


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        _require(key not in result, 'duplicate JSON object key')
        result[key] = value
    return result


def _small_json_integer(value):
    _require(len(value) <= 18, 'oversized JSON integer')
    return int(value)


def _no_json_float(value):
    raise VerificationError('floating-point and nonfinite JSON values are forbidden')


def _load(root, relative, compressed=False):
    data = _safe_read(root, relative)
    digest = hashlib.sha256(data).hexdigest()
    stream = gzip.GzipFile(fileobj=io.BytesIO(data), mode='rb') if compressed else io.BytesIO(data)
    objects = []
    expanded = 0
    expanded_hash = hashlib.sha256()
    try:
        with stream:
            while True:
                line = stream.readline(MAX_LINE_BYTES + 1)
                if not line:
                    break
                expanded += len(line)
                _require(len(line) <= MAX_LINE_BYTES, relative + ': line size bound exceeded')
                _require(expanded <= MAX_EXPANDED_BYTES, relative + ': expanded size bound exceeded')
                _require(len(objects) < len(EXPECTED_CASES), relative + ': extra records')
                _require(line.endswith(b'\n'), relative + ': truncated or nonterminated record')
                _require(line.strip(), relative + ': blank record')
                expanded_hash.update(line)
                record = json.loads(line.decode('utf-8'), object_pairs_hook=_unique_object,
                                    parse_int=_small_json_integer,
                                    parse_float=_no_json_float, parse_constant=_no_json_float)
                _require(type(record) is dict, relative + ': record is not an object')
                objects.append(record)
    except (OSError, EOFError, UnicodeError, json.JSONDecodeError, RecursionError, zlib.error) as exc:
        raise VerificationError(relative + ': decoding failed (' + type(exc).__name__ + ')') from exc
    _require(len(objects) == len(EXPECTED_CASES), relative + ': expected exactly 60 records')
    return objects, {'path': relative, 'sha256': digest, 'stored_bytes': len(data),
                     'expanded_bytes': expanded, 'expanded_sha256': expanded_hash.hexdigest()}


def _integer_fields(record, keys, label):
    for key in sorted(keys):
        _require(type(record[key]) is int, label + ': ' + key + ' must be an integer, not bool')


def _decimal(value, label):
    """Parse bounded canonical unsigned decimals without global digit-limit changes."""
    _require(type(value) is str and 0 < len(value) <= MAX_DECIMAL_DIGITS, label + ': invalid decimal length or type')
    _require(all('0' <= char <= '9' for char in value), label + ': invalid decimal characters')
    _require(value == '0' or value[0] != '0', label + ': noncanonical decimal')
    number = 0
    # Each int conversion stays below Python's default large-decimal limit.
    # No interpreter-global set_int_max_str_digits call is needed.
    for index in range(0, len(value), 9):
        chunk = value[index:index + 9]
        number = number * (10 ** len(chunk)) + int(chunk)
    return number


def _same_typed(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return left.keys() == right.keys() and all(_same_typed(left[k], right[k]) for k in left)
    if type(left) is list:
        return len(left) == len(right) and all(_same_typed(a, b) for a, b in zip(left, right))
    return left == right


def _check_source(record):
    label = 'source record'
    _require(record.keys() == SOURCE_KEYS, label + ': unexpected or missing fields')
    _integer_fields(record, SOURCE_INT_KEYS, label)
    M = record['M']
    theta_numerator = record['theta_num']
    row = record['row']
    _require(type(row) is str, label + ': row is not text')
    key = (M, theta_numerator, row)
    _require(key in EXPECTED_CASES, label + ': case outside declared finite grid')
    label = 'case ' + str(key)
    _require(record['theta_den'] == 4, label + ': wrong declared theta denominator')
    theta = Fraction(theta_numerator, 4)
    n = M // 4
    k = M // 1024
    ones = row.count('1')
    p = theta ** ones * (1 - theta) ** (2 - ones)
    a_rational = 16 * p
    _require(a_rational.denominator == 1, label + ': match probability not representable over 16')
    a = a_rational.numerator
    mu = n * p
    threshold = Fraction(M, 512) + 2 * k
    # Strict cutoff independently expressed as ceil(threshold) - 1.
    last = -((-threshold.numerator) // threshold.denominator) - 1
    expected_ints = {'k': k, 'disjoint_pairs_n': n, 'match_p_num_over_16': a,
                     'mean_num': mu.numerator, 'mean_den': mu.denominator,
                     'threshold_num': threshold.numerator, 'threshold_den': threshold.denominator,
                     'last_included_count': last}
    for field, expected in expected_ints.items():
        _require(record[field] == expected, label + ': ' + field + ' mismatch')
    _require(record['comparison_bound'] == '(1023/1024)^M', label + ': comparison label mismatch')
    _require(record['exact_rational_comparison_pass'] is True, label + ': comparison flag is not true')
    # These are checked only at the retained parameter cases, not universally.
    _require(M >= 8 and 0 <= k <= M // 1024, label + ': illegal M or corruption budget')
    _require(Fraction(1, 4) <= theta <= Fraction(3, 4) and p >= Fraction(1, 16), label + ': illegal source parameter')
    _require(2 * n - 1 < M and 2 * (n - 1) < M // 2, label + ': disjoint pairs violate protected/half boundaries')
    _require(n >= Fraction(M, 8) and mu >= Fraction(M, 128), label + ': mean lower bound fails')
    _require(threshold <= Fraction(M, 256) <= mu / 2, label + ': threshold bound fails')
    _require(mu / 8 >= Fraction(M, 1024), label + ': exponential constant bound fails')
    # Independent arithmetic implementation: binomial term recurrence, not comb.
    # t_0=(16-a)^n, t_{j+1}=t_j*(n-j)*a/((j+1)*(16-a)).
    values = record['tail_term_numerators_decimal']
    _require(type(values) is list and len(values) == min(n, last) + 1, label + ': incomplete term list')
    term = pow(16 - a, n)
    total = 0
    parsed_terms = []
    for j, saved in enumerate(values):
        actual = _decimal(saved, label + ': term ' + str(j))
        _require(actual == term, label + ': term ' + str(j) + ' arithmetic mismatch')
        parsed_terms.append(actual)
        total += actual
        if j + 1 < len(values):
            term, remainder = divmod(term * (n - j) * a, (j + 1) * (16 - a))
            _require(remainder == 0, label + ': binomial recurrence not integral')
    denominator = pow(16, n)
    _require(_decimal(record['tail_denominator_decimal'], label + ': denominator') == denominator, label + ': denominator mismatch')
    _require(_decimal(record['tail_numerator_decimal'], label + ': total') == total, label + ': sum mismatch')
    _require(0 <= total <= denominator, label + ': invalid tail probability')
    bound_num = pow(1023, M)
    bound_den = pow(1024, M)
    left = total * bound_den
    right = bound_num * denominator
    _require(left <= right, label + ': exact rational comparison fails')
    return key, {'n': n, 'k': k, 'theta_num': theta.numerator, 'theta_den': theta.denominator,
                 'p_num': p.numerator, 'p_den': p.denominator, 'a': a,
                 'mean_num': mu.numerator, 'mean_den': mu.denominator,
                 'threshold_num': threshold.numerator, 'threshold_den': threshold.denominator,
                 'last': last, 'denominator': denominator, 'terms': parsed_terms,
                 'numerator': total, 'bound_num': bound_num, 'bound_den': bound_den,
                 'left_cross_product': left, 'right_cross_product': right, 'comparison': True}


def _check_review(record, sources, calculations):
    _require(record.keys() == {'source_record', 'independent', 'status'}, 'review record: unexpected or missing fields')
    _require(record['status'] == 'PASS', 'review record: status is not PASS')
    embedded = record['source_record']
    _require(type(embedded) is dict and embedded.keys() == SOURCE_KEYS, 'review embedded source: bad schema')
    _integer_fields(embedded, SOURCE_INT_KEYS, 'review embedded source')
    _require(type(embedded['row']) is str, 'review embedded source: invalid row')
    key = (embedded['M'], embedded['theta_num'], embedded['row'])
    _require(key in sources, 'review embedded source: unexpected case')
    _require(_same_typed(embedded, sources[key]), 'review embedded source does not exactly match retained source')
    independent = record['independent']
    _require(type(independent) is dict and independent.keys() == INDEPENDENT_KEYS, 'review independent: bad schema')
    _integer_fields(independent, INDEPENDENT_INT_KEYS, 'review independent')
    expected = calculations[key]
    for field in sorted(INDEPENDENT_INT_KEYS):
        _require(independent[field] == expected[field], 'review independent: ' + field + ' mismatch')
    for field in sorted(INDEPENDENT_DECIMAL_KEYS):
        _require(_decimal(independent[field], 'review independent: ' + field) == expected[field], 'review independent: ' + field + ' mismatch')
    values = independent['terms']
    _require(type(values) is list and len(values) == len(expected['terms']), 'review independent: incomplete terms')
    for j, (saved, actual) in enumerate(zip(values, expected['terms'])):
        _require(_decimal(saved, 'review term ' + str(j)) == actual, 'review independent: term arithmetic mismatch')
    _require(independent['comparison'] is True, 'review independent: comparison flag is not true')
    return key


def verify_records(root):
    """Validate archived values and completeness; never write or run archived code."""
    source_records, source_info = _load(root, SOURCE_FILE)
    review_records, review_info = _load(root, REVIEW_FILE, compressed=True)
    sources = {}
    calculations = {}
    term_count = 0
    for record in source_records:
        key, expected = _check_source(record)
        _require(key not in sources, 'duplicate source case')
        sources[key] = record
        calculations[key] = expected
        term_count += len(expected['terms'])
    _require(sources.keys() == EXPECTED_CASES, 'source finite-grid coverage incomplete')
    reviewed = set()
    for record in review_records:
        key = _check_review(record, sources, calculations)
        _require(key not in reviewed, 'duplicate review case')
        reviewed.add(key)
    _require(reviewed == EXPECTED_CASES, 'review finite-grid coverage incomplete')
    return {
        'schema': 'iid-retained-record-verification-v1',
        'status': 'PASS',
        'inputs': [source_info, review_info],
        'coverage': {
            'M_values': list(M_VALUES), 'theta_numerators_over_4': list(THETA_NUMERATORS),
            'rows': list(ROWS), 'declared_cases': len(EXPECTED_CASES),
            'source_records': len(sources), 'later_review_records': len(reviewed),
            'source_term_values_checked': term_count, 'later_review_term_values_checked': term_count,
            'embedded_source_term_values_matched': term_count,
            'source_tail_sums_checked': len(sources), 'source_tail_denominators_checked': len(sources),
            'later_review_bound_values_checked': 2 * len(reviewed),
            'later_review_cross_products_checked': 2 * len(reviewed),
            'exact_rational_comparisons_checked': len(sources),
            'parameter_legality_and_constant_cases_checked': len(sources),
            'missing_cases': [], 'duplicate_cases': []},
        'completeness': {
            'declared_later_source_grid_complete': True,
            'declared_later_review_grid_complete': True,
            'retained_term_arrays_complete_for_strict_cutoff': True,
            'original_exact_tail_intermediates_recovered': False,
            'original_failed_wrapper_transcript_recovered': False},
        'checks': [
            'Strict UTF-8 JSONL with unique keys, exact schemas, finite integer values, and canonical decimal strings.',
            'Declared 60-case Cartesian grid, legal parameters, protected disjoint-pair indices, saved mean and threshold constants.',
            'All retained binomial numerators checked by an exact recurrence independent of the original comb implementation.',
            'Tail denominator, term sum, rational bound numerator/denominator, and saved cross-products checked using integers.',
            'All later review embedded sources matched by exact types and values; all independent values and PASS flags checked.'],
        'scope_limits': [
            'Finite retained-record verification, not a proof over all M, theta, corruption budgets, words, or attacks.',
            'No samples, original diagnostic reruns, model initializations, original scripts, or new experimental records.',
            'Later comprehensive and review archives do not recover the original diagnostic missing exact tails or failed-wrapper log.',
            'No general order-two learning lower bound, novelty, asymptotic theorem, or citation validation is established here.',
            'This module reads only the two numeric archives; the outer inventory must bind other source, note, review, and log files.']}


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print('usage: python -B verify_iid_retained_v2.py ROOT', file=sys.stderr)
        return 2
    try:
        report = verify_records(args[0])
    except (VerificationError, TypeError, ValueError) as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(report, sort_keys=True, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
