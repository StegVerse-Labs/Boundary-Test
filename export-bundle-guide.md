# Export Bundle Guide

## Purpose

The export bundle generator creates a portable reviewer package for the Boundary Test repository.

The package includes the core fixtures, review documents, SDK option files, runners, schemas, templates, examples, and a generated comparison report.

## Command

Run:

```bash
python generate_export_bundle.py
```

Expected output:

```text
PASS: wrote dist/boundary-test-v0.1.0.zip
```

## Generated Files

Displayed paths:

```text
dist/boundary-test-v0.1.0/
dist/boundary-test-v0.1.0.zip
```

The exported directory includes an `export-manifest.json` file with SHA-256 hashes for exported files.

## Safe Interpretation

A generated export bundle is a review package only.

It does not establish GLM conformance, GLM compatibility, adoption, endorsement, runtime interoperability, delegated authority, execution authority, or consequence authority.

## Recommended Use

Use the export bundle when sending Boundary Test materials to a reviewer who wants a portable copy of the fixture package.
