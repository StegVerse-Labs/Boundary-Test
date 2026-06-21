---
name: Boundary Violation
description: Report suspected authority inheritance, implied interoperability, or another boundary violation.
title: "Boundary violation: "
labels: ["boundary-violation"]
---

## Suspected Violation

Select all that apply:

- [ ] authority inheritance by adjacency
- [ ] delegated authority without valid delegation model
- [ ] implied interoperability
- [ ] implied conformance
- [ ] implied adoption or endorsement
- [ ] external validity dependency
- [ ] unclear claims or non-claims
- [ ] missing authority scope

## Affected File Or Artifact

Name the file, artifact, fixture, or documentation section.

## Why This May Be Unsafe

Explain how the current language or structure could create unintended authority, conformance, interoperability, adoption, endorsement, delegation, execution authority, or consequence authority.

## Expected Safer Outcome

Select one:

- [ ] REVIEW-ONLY with clearer non-claims
- [ ] FAIL boundary check
- [ ] INCOMPLETE until authority scope is clarified
- [ ] Remove or rewrite artifact

## Suggested Fix

Propose the smallest change that preserves review-only behavior.

## Non-Claims Reminder

This issue should not be interpreted as claiming GLM conformance, GLM compatibility, GLM adoption, GLM endorsement, runtime interoperability, delegated authority, execution authority, or consequence authority.
