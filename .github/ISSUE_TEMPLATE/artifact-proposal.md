---
name: Artifact Proposal
description: Propose a new Boundary Test artifact, fixture, mapping, schema, or example.
title: "Artifact proposal: "
labels: ["artifact-proposal"]
---

## Proposed Artifact

Name and describe the proposed artifact.

## Artifact Type

Select one:

- [ ] boundary artifact
- [ ] comparison fixture
- [ ] example artifact
- [ ] invalid-control artifact
- [ ] schema
- [ ] SDK descriptor
- [ ] documentation

## Intended Use

Explain how this artifact supports review-only Boundary Test behavior.

## Authority Scope

What authority does the artifact claim?

What authority does it explicitly not claim?

## Required Non-Claims

Confirm the artifact does not imply:

- [ ] GLM conformance
- [ ] GLM compatibility
- [ ] external framework adoption
- [ ] external endorsement
- [ ] runtime interoperability
- [ ] delegated authority
- [ ] execution authority
- [ ] consequence authority

## Expected Outcome

Select one:

- [ ] REVIEW_ONLY
- [ ] PASS boundary check
- [ ] FAIL boundary check
- [ ] INCOMPLETE

## Validation Plan

Which commands should still pass after this artifact is added?

```bash
python validate_boundary_schemas.py
python run_example_cases.py
python run_boundary_test.py
python run_boundary_regression.py
```
