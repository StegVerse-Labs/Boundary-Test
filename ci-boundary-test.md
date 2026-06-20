# Boundary Test CI

## Purpose

This repository includes a GitHub Actions workflow that automatically runs the Boundary Test verification path.

The workflow validates both:

1. the prepared review-only fixture; and
2. the invalid-control fixture.

## Workflow Path

Displayed path without the leading dot:

`github/workflows/boundary-test.yml`

Note: the actual repository path uses the standard GitHub Actions leading-dot directory.

## What The Workflow Runs

```bash
python run_boundary_test.py
python run_boundary_regression.py
```

## Expected Results

The review-only fixture should return:

```text
REVIEW-ONLY
```

The regression runner should confirm:

- normal fixture returns `REVIEW_ONLY`
- invalid-control fixture returns `FAIL`

## Trigger Conditions

The workflow runs on:

- push
- pull request
- manual dispatch

## Why This Matters

The Boundary Test is now reproducible without relying on a local manual run.

Any change to the artifacts, fixtures, or runners should preserve the expected review-only and invalid-control outcomes.
