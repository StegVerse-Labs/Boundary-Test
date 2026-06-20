import json
import shutil
import tempfile
from pathlib import Path

import run_boundary_test

BASE = Path(__file__).resolve().parent

NORMAL_REQUIRED = {
    "organization-index.json": "organization-index.json",
    "stegverse-boundary-manifest.json": "stegverse-boundary-manifest.json",
    "glm-boundary-placeholder.json": "glm-boundary-placeholder.json",
    "boundary-comparison-fixture.json": "boundary-comparison-fixture.json",
}

INVALID_REQUIRED = {
    "organization-index.json": "organization-index.json",
    "negative-control-boundary-manifest.json": "stegverse-boundary-manifest.json",
    "glm-boundary-placeholder.json": "glm-boundary-placeholder.json",
    "invalid-control-comparison-fixture.json": "boundary-comparison-fixture.json",
}


def copy_fixture(mapping, target):
    for source_name, target_name in mapping.items():
        shutil.copyfile(BASE / source_name, target / target_name)


def evaluate_in_temp(mapping):
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        copy_fixture(mapping, tmp_path)
        old_base = run_boundary_test.BASE
        try:
            run_boundary_test.BASE = tmp_path
            return run_boundary_test.evaluate()
        finally:
            run_boundary_test.BASE = old_base


def main():
    normal = evaluate_in_temp(NORMAL_REQUIRED)
    invalid = evaluate_in_temp(INVALID_REQUIRED)

    failures = []

    if normal.get("top_level_outcome") != "REVIEW_ONLY":
        failures.append({
            "case": "normal_fixture",
            "expected": "REVIEW_ONLY",
            "actual": normal,
        })

    if invalid.get("top_level_outcome") != "FAIL":
        failures.append({
            "case": "invalid_control_fixture",
            "expected": "FAIL",
            "actual": invalid,
        })

    if failures:
        print(json.dumps({"regression": "FAIL", "failures": failures}, indent=2))
        raise SystemExit(1)

    print(json.dumps({
        "regression": "PASS",
        "normal_fixture": normal,
        "invalid_control_fixture": invalid,
    }, indent=2))


if __name__ == "__main__":
    main()
