# Schema Validation

## Purpose

Schema validation confirms that Boundary Test JSON artifacts contain the structural fields required for review and SDK use.

This validation is structural only. It does not create GLM conformance, interoperability, adoption, endorsement, delegated authority, or execution authority.

## Schemas

| Schema | Purpose |
|---|---|
| `schemas/boundary-artifact.schema.json` | Defines the expected shape for boundary artifacts |
| `schemas/comparison-fixture.schema.json` | Defines the expected shape for comparison fixtures |

## Local Validation

Run:

```bash
python validate_boundary_schemas.py
```

Expected result:

```text
PASS: boundary artifact and comparison fixture schemas validated.
```

## What Is Checked

The validator checks that boundary artifacts include:

- `artifact_type`
- `artifact_version`
- `artifact_id`
- `issuer`
- `purpose`
- `authority_scope`
- `authority_scope.inherits_authority_from`
- `authority_scope.grants_authority_to`

The validator checks that comparison fixtures include:

- `fixture_type`
- `fixture_version`
- `test_name`
- `artifacts`
- `expected_results`
- expected authority-inheritance, interoperability, and external-validity flags

## Relationship To Boundary Test

Schema validation answers:

> Is the artifact shaped well enough to be evaluated?

Boundary Test answers:

> Does the artifact preserve boundary independence without authority inheritance?

A schema pass is required before a boundary result should be trusted, but it is not itself a boundary pass.
