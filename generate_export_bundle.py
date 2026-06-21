import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
DIST = BASE / "dist"
EXPORT_DIR = DIST / "boundary-test-v0.1.0"
ZIP_PATH = DIST / "boundary-test-v0.1.0.zip"
MANIFEST_PATH = EXPORT_DIR / "export-manifest.json"

FILES = [
    "README.md",
    "VERSION",
    "STATUS.json",
    "CHANGELOG.md",
    "release-notes-v0.1.0.md",
    "repository-index.md",
    "reviewer-handoff.md",
    "release-readiness-checklist.md",
    "boundary-test-manifest.json",
    "organization-index.json",
    "stegverse-boundary-manifest.json",
    "glm-boundary-placeholder.json",
    "boundary-comparison-fixture.json",
    "five-question-resolution.md",
    "test-plan.md",
    "boundary-test-option.json",
    "boundary-test-outcomes.json",
    "sdk-boundary-test.md",
    "boundary-test-user-guide.md",
    "verify_boundary_fixture.py",
    "run_boundary_test.py",
    "run_boundary_regression.py",
    "validate_boundary_schemas.py",
    "run_example_cases.py",
    "generate_status.py",
    "generate_comparison_report.py",
    "comparison-report-guide.md",
    "schema-validation.md",
    "example-validation.md",
    "invalid-control-notes.md",
    "negative-control-boundary-manifest.json",
    "invalid-control-comparison-fixture.json",
    "schemas/boundary-artifact.schema.json",
    "schemas/comparison-fixture.schema.json",
    "templates/boundary-artifact-template.json",
    "templates/comparison-fixture-template.json",
    "examples/README.md",
    "examples/review-only-clean-mapping.json",
    "examples/incomplete-missing-authority-scope.json",
]


def sha256(path):
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def run_report():
    subprocess.run(
        [sys.executable, "generate_comparison_report.py"],
        cwd=BASE,
        check=True,
    )


def clean():
    if EXPORT_DIR.exists():
        shutil.rmtree(EXPORT_DIR)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def copy_files():
    copied = []
    for relative_name in FILES + ["comparison-report.md"]:
        source = BASE / relative_name
        if not source.exists():
            raise FileNotFoundError(f"missing export file: {relative_name}")
        target = EXPORT_DIR / relative_name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        copied.append(relative_name)
    return copied


def write_manifest(files):
    manifest = {
        "package": "Boundary Test export bundle",
        "version": "0.1.0",
        "repository": "StegVerse-Labs/Boundary-Test",
        "top_level_expected_outcome": "REVIEW_ONLY",
        "review_posture": "review_only_fixture",
        "non_claims": [
            "GLM conformance",
            "GLM compatibility",
            "GLM adoption",
            "GLM endorsement",
            "runtime interoperability",
            "delegated authority",
            "execution authority",
            "consequence authority",
        ],
        "files": [
            {
                "path": name,
                "sha256": sha256(EXPORT_DIR / name),
            }
            for name in files
        ],
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def zip_bundle():
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(EXPORT_DIR.rglob("*")):
            if path.is_file():
                bundle.write(path, path.relative_to(DIST))


def main():
    run_report()
    clean()
    files = copy_files()
    write_manifest(files)
    zip_bundle()
    print(f"PASS: wrote {ZIP_PATH.relative_to(BASE)}")


if __name__ == "__main__":
    main()
