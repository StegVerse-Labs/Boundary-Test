# Repository Index

## Purpose

This index gives reviewers, SDK users, and future tooling a single navigation point for the Boundary Test repository.

The repository is a review-only fixture. It does not claim GLM conformance, GLM compatibility, external framework adoption, interoperability, delegated authority, execution authority, or endorsement.

## Start Here

| File | Role |
|---|---|
| `README.md` | Repository overview |
| `reviewer-handoff.md` | External reviewer starting point |
| `release-readiness-checklist.md` | Ready-to-send criteria |
| `boundary-test-user-guide.md` | User-facing Boundary Test guide |
| `sdk-boundary-test.md` | SDK option instructions |

## Core Boundary Artifacts

| File | Role |
|---|---|
| `organization-index.json` | Discovery declaration |
| `stegverse-boundary-manifest.json` | Boundary declaration |
| `glm-boundary-placeholder.json` | Placeholder adjacent governance artifact |
| `boundary-comparison-fixture.json` | Positive comparison fixture |
| `five-question-resolution.md` | Human review resolution |
| `test-plan.md` | Manual and automated test plan |

## SDK and Outcome Artifacts

| File | Role |
|---|---|
| `boundary-test-option.json` | Machine-readable SDK option descriptor |
| `boundary-test-outcomes.json` | Machine-readable outcome taxonomy |
| `run_boundary_test.py` | SDK-style runner for prepared fixture |
| `verify_boundary_fixture.py` | Deterministic positive fixture verifier |

## Invalid-Control Artifacts

| File | Role |
|---|---|
| `negative-control-boundary-manifest.json` | Deliberately invalid authority-linkage artifact |
| `invalid-control-comparison-fixture.json` | Invalid-control comparison fixture |
| `invalid-control-notes.md` | Explanation of invalid-control purpose |
| `run_boundary_regression.py` | Regression runner for positive and invalid-control paths |

## CI Artifacts

| File | Role |
|---|---|
| `ci-boundary-test.md` | CI workflow explanation |
| `github/workflows/boundary-test.yml` | GitHub Actions workflow path displayed without leading dot |

Note: the actual workflow path uses the standard GitHub Actions leading-dot directory.

## Expected Review Result

For the prepared GLM-adjacent fixture, the expected top-level result is:

```text
REVIEW-ONLY
```

The boundary checks may pass, but the repository must not be interpreted as establishing GLM conformance, GLM compatibility, adoption, endorsement, or interoperability.

## Local Commands

```bash
python run_boundary_test.py
python run_boundary_regression.py
```

## Recommended Reviewer Path

1. Read `reviewer-handoff.md`.
2. Read `five-question-resolution.md`.
3. Inspect the JSON boundary artifacts.
4. Run the local commands.
5. Confirm the invalid-control fixture fails as expected.
