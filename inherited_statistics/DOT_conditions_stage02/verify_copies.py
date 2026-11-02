#!/usr/bin/env python3
"""Verify delivered hashes and, optionally, exact excerpts of provided originals."""
import argparse
import hashlib
import json
from pathlib import Path

def digest(data):
    return hashlib.sha256(data).hexdigest()

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--sources", type=Path, help="Directory containing the original source files (searched recursively).")
args = parser.parse_args()
root = Path(__file__).resolve().parent
mapping = json.loads((root / "COPY_MAP.json").read_text(encoding="utf-8"))
count = 0
for record in mapping["records"]:
    output = (root / record["output"]).read_bytes()
    assert digest(output) == record["output_sha256"], record["output"]
    original = None
    if args.sources is not None:
        matches = [p for p in args.sources.rglob(record["source"])
                   if p.is_file() and digest(p.read_bytes()) == record["source_sha256"]]
        assert matches, "Missing exact original: " + record["source"]
        original = matches[0].read_bytes()
    body = []
    for span in record["spans"]:
        data = output[span["output_byte_start"]:span["output_byte_end"]]
        assert digest(data) == span["sha256"], record["output"]
        if original is not None:
            start, end = span["source_byte_start"], span["source_byte_end"]
            assert 0 <= start < end <= len(original), record["source"]
            assert data == original[start:end], record["source"]
            assert span["source_line_start"] == original[:start].count(b"\n") + 1
            assert span["source_line_end"] == original[:end - 1].count(b"\n") + 1
        body.append(data)
        count += 1
    assert digest(b"".join(body)) == record["copied_body_sha256"]
scope = "exact original-source equality" if args.sources is not None else "delivered-byte consistency only (originals not supplied)"
print(f"PASS: {len(mapping['records'])} files, {count} spans; {scope}.")
