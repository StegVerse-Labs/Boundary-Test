# Boundary Test Extension Guide

## Purpose

This guide explains how to add new Boundary Test artifacts without weakening the review-only posture of this repository.

Extensions must preserve the distinction between review, comparison, conformance, interoperability, delegation, and execution authority.

## Extension Rule

A new artifact may support review or comparison.

A new artifact must not imply:

- GLM conformance
- GLM compatibility
- GLM adoption
- GLM endorsement
- StegVerse conformance by external artifacts
- runtime interoperability
- delegated authority
- execution authority
- consequence authority

## Adding A New Boundary Artifact

1. Create a new JSON artifact.
2. Include `artifact_type`, `artifact_version`, `artifact_id`, `issuer`, `purpose`, and `authority_scope`.
3. Include explicit `claims` when the artifact makes reviewable claims.
4. Include explicit `non_claims` when the artifact could otherwise be misread.
5. Set `authority_scope.inherits_authority_from` to an empty list unless the test is intentionally invalid-control.
6. Set `authority_scope.grants_authority_to` to an empty list unless the test is intentionally invalid-control.
7. Run schema validation.
8. Run Boundary Test regression.

## Adding A GLM Mapping

A GLM mapping may be added only as a mapping or comparison artifact unless the GLM author supplies an authoritative artifact.

Use wording such as:

```text
This artifact maps fields for boundary review only. It does not claim GLM conformance, adoption, endorsement, interoperability, or shared authority.
```

Do not use wording such as:

```text
This proves GLM compatibility.
This makes StegVerse GLM-compliant.
This authorizes interoperability.
This grants execution authority.
```

## Adding A New Fixture

A new fixture should declare:

- artifact paths
- expected independent discoverability
- whether co-discovery is allowed
- whether cross-reference is allowed
- whether authority inheritance is denied
- whether interoperability-by-adjacency is denied
- whether external validity dependency is denied

## Adding A New Invalid-Control Case

Invalid-control cases are allowed and encouraged when they prove the test rejects unsafe boundary behavior.

Invalid-control files must clearly state that they are deliberate test artifacts.

Expected invalid-control result:

```text
FAIL
```

## Required Commands Before Review

Run:

```bash
python validate_boundary_schemas.py
python run_boundary_test.py
python run_boundary_regression.py
```

## Expected Safe Result For GLM-Adjacent Review

```text
REVIEW-ONLY: independently discoverable, independently reviewable, no authority inheritance detected.
Boundary checks: PASS.
Conformance claim: NOT MADE.
Interoperability claim: NOT MADE.
Adoption claim: NOT MADE.
Execution authority: NOT GRANTED.
```

## Done Criteria For Extensions

An extension is ready when:

1. schema validation passes;
2. Boundary Test still returns REVIEW-ONLY for the prepared fixture;
3. regression still confirms invalid-control failure;
4. no new artifact creates an unintended conformance claim;
5. no new artifact creates interoperability by adjacency;
6. no new artifact creates authority inheritance unless it is explicitly invalid-control; and
7. reviewer-facing documentation remains clear that this repository is review-only.
