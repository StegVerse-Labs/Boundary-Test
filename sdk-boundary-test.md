# SDK Boundary Test Option

## Purpose

This document defines a user-facing SDK option named `Boundary Test`.

The option lets any user evaluate whether governance artifacts can be discovered and reviewed together without creating implied authority inheritance, interoperability, conformance, delegation, or shared execution authority.

This is a review test only. It is not an execution authority test.

## User-Facing Option Name

`Boundary Test`

## User Instruction

Use this option when you want to test whether adjacent governance artifacts remain independently authoritative while still being discoverable and reviewable together.

The test should be selected when a user asks questions such as:

- Can these governance artifacts be reviewed together?
- Does this artifact inherit authority from another artifact?
- Does this comparison imply interoperability?
- Does discoverability create shared authority?
- Can an organization-index artifact reference another artifact without granting authority?

## Required User Inputs

A user should provide at least one of the following:

1. A governance artifact.
2. An organization-index artifact.
3. A boundary manifest.
4. A governance-layer manifest.
5. A comparison fixture.
6. A repository URL containing any of the above.

If only one artifact is supplied, the SDK should test whether the artifact clearly declares its own authority scope and non-claims.

If multiple artifacts are supplied, the SDK should test whether they remain independently reviewable and non-authorizing.

## Default Test Fixture

If the user does not provide their own fixture, the SDK may use the fixture in this repository:

- `organization-index.json`
- `stegverse-boundary-manifest.json`
- `glm-boundary-placeholder.json`
- `boundary-comparison-fixture.json`
- `five-question-resolution.md`
- `verify_boundary_fixture.py`

The GLM placeholder must be treated as a placeholder only. It must not be treated as Emanuel's GLM specification or as a claim of GLM conformance.

## Transition Table Validation

The Boundary Test maps to a review-only transition path:

1. Discovery
2. Boundary declaration
3. Adjacent governance review
4. Comparison
5. Human review
6. Deterministic review

The path intentionally terminates before execution authority or consequence.

Expected transition posture:

- ADMIT for review
- PASS for independent discoverability
- PASS for independent reviewability
- PASS for boundary preservation
- DENY for authority inheritance
- DENY for implied interoperability
- DENY for delegated authority

## Expected SDK Output

### PASS: Boundary Preserved

Use when all artifacts remain independently discoverable, independently reviewable, and mutually non-authorizing.

### FAIL: Authority Inheritance Detected

Use when any artifact inherits authority from another artifact without explicit admissible authority.

### FAIL: Delegated Authority Detected

Use when an artifact grants authority to another artifact without an explicit valid delegation model.

### FAIL: Interoperability Assumption Detected

Use when comparison or adjacency is treated as compatibility, interoperability, conformance, or adoption.

### FAIL: External Validity Dependency Detected

Use when one artifact requires another artifact to be valid despite being presented as independently authoritative.

### INCOMPLETE: Missing Boundary Declaration

Use when an artifact cannot be evaluated because claims, non-claims, or authority scope are missing.

## User Explanation Template

When the SDK presents this option to a user, it should explain:

> Boundary Test checks whether governance artifacts can be discovered and reviewed together without creating authority inheritance, interoperability assumptions, delegated authority, or execution authority. This test is for boundary review only. It does not prove runtime compatibility or conformance.

## Done Criteria

The SDK supports Boundary Test when:

1. The option is visible to the user as `Boundary Test`.
2. The user is told that the test is review-only.
3. The user is told what inputs are accepted.
4. The user is told what PASS and FAIL mean.
5. The SDK denies authority inheritance by default.
6. The SDK denies interoperability by adjacency.
7. The SDK can use this repository as the default fixture.
