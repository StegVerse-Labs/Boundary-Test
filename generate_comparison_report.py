import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPORT_PATH = BASE / "comparison-report.md"

COMMANDS = [
    ("Repository status", [sys.executable, "generate_status.py"]),
    ("Schema validation", [sys.executable, "validate_boundary_schemas.py"]),
    ("Example validation", [sys.executable, "run_example_cases.py"]),
    ("Boundary test", [sys.executable, "run_boundary_test.py"]),
    ("Regression test", [sys.executable, "run_boundary_regression.py"]),
]


def read_text(path_name):
    path = BASE / path_name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def read_json(path_name):
    text = read_text(path_name)
    if not text:
        return {}
    return json.loads(text)


def run_command(label, command):
    completed = subprocess.run(
        command,
        cwd=BASE,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "label": label,
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def fenced(text):
    if not text:
        return "```text\n(no output)\n```"
    return "```text\n" + text + "\n```"


def main():
    version = read_text("VERSION").strip() or "UNKNOWN"
    status = read_json("STATUS.json")
    manifest = read_json("boundary-test-manifest.json")
    fixture = read_json("boundary-comparison-fixture.json")
    commands = [run_command(label, command) for label, command in COMMANDS]

    all_passed = all(item["returncode"] == 0 for item in commands)

    lines = [
        "# Boundary Test Comparison Report",
        "",
        "## Report Status",
        "",
        f"- Repository: `StegVerse-Labs/Boundary-Test`",
        f"- Version: `{version}`",
        f"- Generated verification posture: `{'PASS' if all_passed else 'FAIL'}`",
        f"- Expected top-level outcome: `{status.get('top_level_expected_outcome', 'REVIEW_ONLY')}`",
        f"- Review posture: `{status.get('review_posture', 'review_only_fixture')}`",
        "",
        "## Primary Review Question",
        "",
        manifest.get(
            "primary_question",
            "Can adjacent governance artifacts be discovered and reviewed together while remaining independent sources of authority?",
        ),
        "",
        "## Expected GLM-Adjacent Result",
        "",
        "```text",
        "REVIEW-ONLY: independently discoverable, independently reviewable, no authority inheritance detected.",
        "Boundary checks: PASS.",
        "Conformance claim: NOT MADE.",
        "Interoperability claim: NOT MADE.",
        "Adoption claim: NOT MADE.",
        "Execution authority: NOT GRANTED.",
        "```",
        "",
        "## Non-Claims",
        "",
    ]

    for item in status.get("non_claims", manifest.get("non_claims", [])):
        lines.append(f"- {item}")

    lines.extend([
        "",
        "## Fixture Expectations",
        "",
    ])

    expected = fixture.get("expected_results", {})
    for key in sorted(expected):
        lines.append(f"- `{key}`: `{expected[key]}`")

    lines.extend([
        "",
        "## Verification Commands",
        "",
    ])

    for result in commands:
        lines.extend([
            f"### {result['label']}",
            "",
            f"Command: `{result['command']}`",
            "",
            f"Return code: `{result['returncode']}`",
            "",
            "Stdout:",
            "",
            fenced(result["stdout"]),
            "",
        ])
        if result["stderr"]:
            lines.extend(["Stderr:", "", fenced(result["stderr"]), ""])

    lines.extend([
        "## Final Interpretation",
        "",
        "This report supports review-only comparison of adjacent governance artifacts.",
        "",
        "A passing report does not establish GLM conformance, GLM compatibility, adoption, endorsement, runtime interoperability, delegated authority, execution authority, or consequence authority.",
        "",
        "The prepared fixture remains admissible for review only.",
        "",
    ])

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT_PATH.name}")
    print("PASS: comparison report generated." if all_passed else "FAIL: comparison report generated with failing checks.")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
