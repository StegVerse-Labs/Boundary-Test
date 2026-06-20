# Boundary Test Examples

## Purpose

This directory contains example artifacts that demonstrate Boundary Test outcome classes.

Examples are instructional only. They are not GLM artifacts, they do not claim GLM conformance, and they do not create interoperability, adoption, endorsement, delegation, or execution authority.

## Examples

| File | Expected Outcome | Purpose |
|---|---|---|
| `review-only-clean-mapping.json` | `REVIEW_ONLY` | Shows a clean review-only mapping with explicit non-claims |
| `incomplete-missing-authority-scope.json` | `INCOMPLETE` | Shows an artifact that cannot be evaluated because authority scope is missing |

## Relationship To Core Fixtures

The core fixtures remain at the repository root.

These examples are not required for the prepared GLM-adjacent Boundary Test. They are included so SDK users can understand the difference between clean review-only behavior and incomplete artifacts.

## Safe Interpretation

A clean example means the artifact is structured for review.

It does not mean the artifact is compatible with GLM, endorsed by GLM, interoperable with GLM, or authorized for execution.
