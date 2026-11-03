"""Create an isolated public replay copy, with one declared metadata-hash reconciliation.

This does not run training, reseal code, or modify the repository. It refuses an
existing destination and verifies exact published input identities before copying.
"""
from pathlib import Path
import argparse, hashlib, json, shutil

if not __debug__:
    raise RuntimeError("Integrity preparation requires Python assertions: do not use -O or PYTHONOPTIMIZE")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(repository, destination):
    repository = repository.resolve()
    destination = destination.resolve()
    if destination.exists() or repository == destination or repository in destination.parents or destination in repository.parents:
        raise ValueError("Choose a nonexistent isolated directory outside the published repository")
    provenance = repository / "provenance/empirical_position_20261103"
    source_map_path = provenance / "SOURCE_EXPORT_MAP.json"
    inventory = json.loads((repository / "provenance/PUBLIC_INVENTORY.json").read_text())
    inventory_map = {row["path"]: row for row in inventory["files"]}
    source_map_relative = source_map_path.relative_to(repository).as_posix()
    assert digest(source_map_path) == inventory_map[source_map_relative]["sha256"]
    source_map = json.loads(source_map_path.read_text())
    by_path = {row["path"]: row for row in source_map["files"]}
    for row in source_map["files"]:
        relative = Path(row["path"])
        assert not relative.is_absolute() and ".." not in relative.parts
        source = repository / relative
        assert source.is_file() and source.stat().st_size == row["public"]["bytes"]
        assert digest(source) == row["public"]["sha256"]
        assert inventory_map[row["path"]]["sha256"] == row["public"]["sha256"]
    destination.mkdir()
    for row in source_map["files"]:
        target = destination / row["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(repository / row["path"], target)
        assert target.stat().st_size == row["public"]["bytes"]
        assert digest(target) == row["public"]["sha256"]
    pilot = destination / "v10_research/learned_position_pilot_20261103"
    seal_path = pilot / "PRE_RUN_HASHES.json"
    original_seal_bytes = seal_path.read_bytes()
    seal = json.loads(original_seal_bytes)
    plan_key = "v10_research/learned_position_pilot_20261103/PLAN.md"
    plan = by_path[plan_key]
    assert seal["files"]["PLAN.md"] == plan["original"]["sha256"]
    assert digest(pilot / "PLAN.md") == plan["public"]["sha256"]
    for name, expected in seal["files"].items():
        if name != "PLAN.md":
            assert digest(pilot / name) == expected
    (pilot / "PRE_RUN_HASHES.historical.json").write_bytes(original_seal_bytes)
    seal["files"]["PLAN.md"] = plan["public"]["sha256"]
    seal_path.write_text(json.dumps(seal, indent=2) + "\n")
    for name, expected in seal["files"].items():
        assert digest(pilot / name) == expected
    calibration = destination / "v10_research/readout_conditioning_calibration_20261103"
    calibration_seal = json.loads((calibration / "PRE_RUN_HASHES.json").read_text())
    for name, expected in calibration_seal["files"].items():
        assert digest(calibration / name) == expected
    receipt = {
        "status": "ISOLATED_COPY_PREPARED_NOT_RUN",
        "source_map_sha256": digest(source_map_path),
        "files_copied": len(source_map["files"]),
        "only_working_seal_change": {
            "file": "v10_research/learned_position_pilot_20261103/PRE_RUN_HASHES.json",
            "key": "files.PLAN.md",
            "original_expected_sha256": plan["original"]["sha256"],
            "public_expected_sha256": plan["public"]["sha256"],
            "reason": "Exact declared non-scientific prose export difference; all other sealed inputs remain exact",
        },
        "historical_seal_sha256": hashlib.sha256(original_seal_bytes).hexdigest(),
        "working_seal_sha256": digest(seal_path),
        "limits": "The original seal timestamp describes the historical protocol, not a new trusted seal of the exported prose. Training and numerical verification have not been run by this preparation script.",
    }
    (destination / "PUBLIC_REPLAY_RECONCILIATION.json").write_text(json.dumps(receipt, indent=2) + "\n")
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    repository = Path(__file__).resolve().parents[2]
    print(json.dumps(prepare(repository, args.destination), indent=2))
