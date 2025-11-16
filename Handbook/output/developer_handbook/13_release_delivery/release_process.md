# Release Process

This page details the standard process for releasing software, with clear gate criteria, required evidence, and release mechanics. Follow these steps to ensure every release meets quality, security, and delivery expectations.

---

## 1. Overview

A predictable and rigorous release process is essential for shipping reliable software. Each release must satisfy defined criteria before it is delivered to users. This ensures that releases are stable, well-documented, and meet both functional and non-functional requirements.

---

## 2. Release Gates

Release gates are quality and compliance checkpoints. Each gate represents a critical aspect of readiness that must be met before proceeding to the next stage or release approval. Skipping any step is not permitted unless a formal exception is reviewed and recorded.

### 2.1 Code Completeness

#### Criteria
- All intended features, bug fixes, and enhancements for this release cycle are implemented.
- No known critical or high-severity issues remain open.

#### Evidence
- All user stories and tickets in the release scope are marked as ‘Done’ in the tracking system (e.g., Jira, Azure Boards).
- A `CHANGELOG.md` entry summarises all changes.

### 2.2 Code Review

#### Criteria
- All code changes are peer-reviewed by one or more qualified engineers not responsible for the original implementation.
- All review comments are addressed or explicitly resolved.

#### Evidence
- Pull requests are merged only after code review approval on the repository (e.g., GitHub, GitLab).
- Review discussions are resolved or explained in the PR record.

### 2.3 Automated Testing

#### Criteria
- All automated tests (unit, integration, end-to-end) must pass.
- Required minimum code coverage threshold is met, or exceptions are justified with risk assessment.

#### Evidence
- CI pipeline run demonstrates all tests have passed.
- Coverage report is available and referenced from the release ticket (e.g., link to CI artefact).

### 2.4 Manual Testing

#### Criteria
- All in-scope features are verified by manual exploratory and scenario-based testing.
- Regression testing performed on high-risk areas.

#### Evidence
- Test cases and exploratory notes are recorded in the test management tool or documented as attachments to the release record.

### 2.5 Security and Compliance

#### Criteria
- All dependencies are scanned for vulnerabilities (OWASP, CVEs).
- All critical and high vulnerabilities are addressed, or explicit sign-off is recorded for accepted risks.
- Data privacy and compliance checks (e.g., GDPR impact) are complete.

#### Evidence
- Security scan reports are archived against release artefacts.
- Compliance checklist is provided and reviewed.

### 2.6 Documentation Update

#### Criteria
- Release documentation is updated: user guides, API documentation, installation steps, and troubleshooting guides.
- Release notes written for customers and internal stakeholders.

#### Evidence
- Links to updated documentation and release notes are attached to the release ticket.

### 2.7 Stakeholder Approval

#### Criteria
- Product owner and, where applicable, legal/compliance have approved the release.

#### Evidence
- Approvals recorded in the tracking or approval system.

---

## 3. Release Mechanics

Describe the exact steps used to prepare, create, and deliver a release artefact.

### 3.1 Versioning

Use [Semantic Versioning](https://semver.org/) for all releases. Each release must increment the version number following these rules:
- Major: Breaking API or behaviour changes.
- Minor: Backwards-compatible feature additions.
- Patch: Backwards-compatible bug fixes.

**Example:**  
Move from 2.3.1 to 2.4.0 when adding a feature; to 3.0.0 if introducing a breaking change.

### 3.2 Branching Strategy

Maintain a `main` or `master` branch for production releases. Use release branches (`release/x.y.z`) for staging and preparation.

**Example:**
- Create `release/2.4.0` branch; finalise changes and testing here before merging to `main`.

### 3.3 Tagging and Artefacts

- Tag the release commit in version control (`git tag v2.4.0`).
- Build release artefacts from the tagged commit only.
- Attach or publish artefacts (binaries, container images, installation packages) in the designated distribution repository.
- Verify artefact integrity (e.g., checksums, signatures) before making public.

### 3.4 Deployment

Follow deployment checklist specific to your environment (staging, production, etc.):
- Ensure configuration changes and secrets are in place and correct.
- Roll out to staging or canary environments first for smoke testing.
- Monitor for issues before full production roll-out.

### 3.5 Post-Release Validation

After deployment:
- Confirm system health and monitor logs/metrics for anomalies.
- Conduct targeted tests to confirm successful deployment.
- Update status dashboard and notify stakeholders.

---

## 4. Practical Example

**Release of Version 1.3.0 for "Acme Service":**

1. All tickets in Jira release 1.3.0 are marked ‘Done’.
2. All PRs for 1.3.0 receive peer review and are merged to `release/1.3.0`.
3. Jenkins pipeline runs all tests, passes with 95% coverage.
4. Manual tests executed as per the test plan; issues logged and retested after fixes.
5. GitHub Dependabot report reviewed; only moderate vulnerabilities present, documented for next cycle.
6. API docs and README updated; release notes prepared in Confluence.
7. Product Owner and Security sign-off recorded in Jira.
8. Tag `v1.3.0` created; Docker image pushed to registry.
9. Staging deployment passes smoke and regression tests; released to production.
10. Monitoring dashboard shows all systems healthy post-release.

---

## 5. Summary

Adhering to this release process ensures software is thoroughly validated, secure, and well-communicated. Each step is designed to minimise risk, protect users, and provide a clear audit trail for every change delivered.

**Always document exceptions and lessons learnt after each release for continuous improvement.**