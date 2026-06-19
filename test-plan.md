# Boundary Test Plan

## Goal

Verify that StegVerse and GLM-adjacent governance artifacts can be reviewed together without creating unintended authority claims.

## Manual Review

1. Open `organization-index.json`.
2. Confirm it points to the StegVerse boundary manifest.
3. Confirm it does not claim GLM authority or compatibility.
4. Open `stegverse-boundary-manifest.json`.
5. Confirm claims and non-claims are explicit.
6. Open `glm-boundary-placeholder.json`.
7. Replace it with Emanuel's GLM artifact or map its fields if available.
8. Open `boundary-comparison-fixture.json`.
9. Confirm expected results prohibit authority inheritance and interoperability claims.
10. Read `five-question-resolution.md`.
11. Confirm all five questions resolve without relying on implied interoperability.

## Automated Review

Run:

```bash
python verify_boundary_fixture.py
```

## Passing Result

The test passes only if:

- all referenced files exist
- all artifacts are independently discoverable
- all artifacts have empty `inherits_authority_from`
- all artifacts have empty `grants_authority_to`
- the fixture prohibits authority inheritance
- the fixture prohibits interoperability claims
- the fixture prohibits external validity dependency

## Failing Result

The test fails if any artifact:

- inherits authority from another artifact
- grants authority to another artifact
- requires another artifact to be valid
- claims compatibility without an explicit external conformance basis
- claims interoperability by adjacency
