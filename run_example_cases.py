import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

EXAMPLES = [
    {
        "path": "examples/review-only-clean-mapping.json",
        "expected": "REVIEW_ONLY",
    },
    {
        "path": "examples/incomplete-missing-authority-scope.json",
        "expected": "INCOMPLETE",
    },
]


def load(path_name):
    path = BASE / path_name
    if not path.exists():
        return None, f"missing file: {path_name}"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except json.JSONDecodeError as exc:
        return None, f"invalid json in {path_name}: {exc}"


def evaluate_example(data):
    if "authority_scope" not in data:
        return "INCOMPLETE"

    scope = data["authority_scope"]
    if not isinstance(scope, dict):
        return "INCOMPLETE"

    if scope.get("inherits_authority_from") not in ([], None):
        return "FAIL"

    if scope.get("grants_authority_to") not in ([], None):
        return "FAIL"

    if "claims" not in data or "non_claims" not in data:
        return "INCOMPLETE"

    return "REVIEW_ONLY"


def main():
    results = []
    failures = []

    for example in EXAMPLES:
        data, error = load(example["path"])
        if error:
            actual = "INCOMPLETE"
            reason = error
        else:
            actual = evaluate_example(data)
            reason = None

        result = {
            "path": example["path"],
            "expected": example["expected"],
            "actual": actual,
        }
        if reason:
            result["reason"] = reason
        results.append(result)

        if actual != example["expected"]:
            failures.append(result)

    if failures:
        print(json.dumps({"examples": "FAIL", "results": results}, indent=2))
        raise SystemExit(1)

    print(json.dumps({"examples": "PASS", "results": results}, indent=2))


if __name__ == "__main__":
    main()
