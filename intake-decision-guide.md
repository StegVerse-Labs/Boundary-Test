# Intake Decision Guide

## Purpose

This guide helps classify incoming Boundary Test issues, pull requests, and review notes.

Classification is procedural only. It does not create conformance, interoperability, adoption, endorsement, delegated authority, execution authority, or consequence authority.

## Intake Questions

### 1. Is the request asking whether an artifact preserves boundary independence?

Classify as: boundary review.

### 2. Is the request proposing a new artifact, fixture, schema, example, or documentation page?

Classify as: artifact proposal.

### 3. Is the request warning that something implies authority, conformance, interoperability, adoption, endorsement, delegation, execution, or consequence?

Classify as: boundary violation.

### 4. Is the request changing JSON structure or validation logic?

Classify as: schema.

### 5. Is the request changing user-facing Boundary Test behavior?

Classify as: sdk.

### 6. Is the request changing verification automation?

Classify as: ci.

### 7. Is the request changing version, release notes, or readiness status?

Classify as: release.

## Required Follow-Up

For any boundary-sensitive item, confirm:

```bash
python generate_status.py
python validate_boundary_schemas.py
python run_example_cases.py
python run_boundary_test.py
python run_boundary_regression.py
```

## Safe Default

If unsure, classify as boundary review and require explicit non-claims before accepting the change.
