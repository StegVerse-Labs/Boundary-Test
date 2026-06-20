# Boundary Test

## Purpose

This repository is the neutral boundary-test fixture area for formal governance testing.

All formal testing datasets must enter through the governed SDK ingestion path before they are routed into any demonstration, sandbox, standing-proof, runner, or GLM boundary test. The required invariant is:

```text
StegVerse-org/StegVerse-SDK
→ manifest-bound dataset
→ receipt-bound intake
→ declared formal testing route
→ route-specific result receipt
```

This keeps every input dataset manifest-bound and receipt-bound before any downstream test consumes it. No formal test route should accept unbound datasets, fixtures, governance artifacts, GLM-style declarations, admissibility packets, sandbox task packets, or standing-proof artifacts.

## Canonical Formal Testing Route

```text
Dataset / fixture / governance artifact
→ StegVerse-org/StegVerse-SDK ingestion
→ manifest + receipt binding
→ route declaration
→ one or more formal testing routes
→ route-specific result receipt
```

| Route | Repository | Purpose |
|------|------------|---------|
| Public demo validation | `StegVerse-org/stegverse-demo-suite` | Reproducible public validation and explainable demo scenarios. |
| Formal demo runner | `StegVerse-org/demo-suite-runner` | GCAT/BCAT formalism probes and deterministic runner scenarios. |
| Rigorous sandbox testing | `StegGhost/entity-sandbox-runner` | Adversarial, entity, and bounded sandbox testing without outside-sandbox authority. |
| Standing proof | `StegVerse-Labs/Standing-Proof-Engine` | Commit-time standing, stale-state replay, authority rebinding, and consequence-binding proof. |
| GLM boundary case | `StegVerse-Labs/Boundary-Test` | Boundary declaration, non-claim preservation, and manifest composability validation after private-review-first concerns are resolved. |

## Route Rule

```text
SDK ingests.
GLM declares boundaries.
Demo-suite demonstrates.
Demo-suite-runner probes formalism behavior.
Sandbox stresses.
SPE proves standing.
Receipts bind every transition.
```

## GLM Test Case Posture

The GLM boundary test case must be handled as an SDK-ingested formal test case, not as an isolated public claim.

```text
GLM-like boundary declaration
→ neutral private fixture
→ SDK manifest / receipt binding
→ boundary-test route declaration
→ non-claim validation
→ optional downstream comparison only after private-review-first clearance
```

The GLM route is allowed to test boundary declaration and manifest composability. It must not imply external adoption, endorsement, compatibility, conformance, delegated authority, shared execution authority, or authority inheritance.

## Current Status

```text
status: neutralized_pending_private_review
publication_posture: do_not_treat_as_external_standard_fixture
review_posture: private_review_first
testing_posture: sdk_ingested_manifest_receipt_bound_route
```

## Current Boundary Rule

No public file, directory, placeholder, issuer reference, review step, or test-plan language in this repository should use a third-party standard name or personal attribution before private review has occurred and naming concerns have been addressed.

## Correct Working Order

```text
1. Draft privately.
2. Bind the dataset or fixture through SDK manifest / receipt intake.
3. Declare the formal testing route.
4. Share privately with the relevant reviewer.
5. Resolve naming, attribution, and boundary concerns.
6. Publish only after those concerns are settled.
```

## Non-Claims

This repository does not claim:

- compatibility with any external governance framework;
- endorsement by any external reviewer;
- adoption of any external standard;
- certification;
- conformance;
- interoperability;
- delegated authority;
- shared execution authority;
- authority inheritance;
- personal participation by any reviewer.

## Scope

This repository should not be used as a public validation request, public comparison fixture, or public review target until the private-review-first sequence has been completed.

Within that constraint, this repository may define neutral, SDK-ingested boundary fixtures for later testing across the formal route map.

## Next Safe Step

Prepare any future boundary fixture privately, with neutral filenames and no personal issuer references. Bind the fixture through SDK manifest / receipt intake before routing it to Boundary-Test, demo-suite, entity-sandbox-runner, Standing-Proof-Engine, or any GLM-style composability test.
