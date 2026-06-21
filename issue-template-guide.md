# Issue Template Guide

## Purpose

This repository includes issue templates for structured Boundary Test review.

The templates are designed to keep future feedback aligned with the repository's review-only posture.

## Template Paths

Displayed paths without the leading dot:

- `github/ISSUE_TEMPLATE/boundary-review.md`
- `github/ISSUE_TEMPLATE/artifact-proposal.md`
- `github/ISSUE_TEMPLATE/boundary-violation.md`

Note: the actual repository paths use GitHub's standard leading-dot directory.

## Template Uses

| Template | Use |
|---|---|
| Boundary Review | Ask whether an artifact or fixture preserves boundary independence |
| Artifact Proposal | Propose a new artifact, fixture, schema, example, or documentation file |
| Boundary Violation | Report suspected authority inheritance, implied interoperability, or unclear claims |

## Required Posture

All issues should preserve the distinction between:

- review
- comparison
- conformance
- interoperability
- adoption
- endorsement
- delegation
- execution authority
- consequence authority

No issue template should be interpreted as creating GLM conformance, GLM compatibility, external framework adoption, runtime interoperability, delegated authority, or execution authority.
