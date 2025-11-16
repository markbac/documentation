# Build and Integration

This page describes the development workflow for building and integrating software within our engineering teams. It covers continuous integration (CI) rules, the build graph, versioning practices, and artefact management. Adhering to these guidelines ensures reliability, reproducibility, and traceability across the development life cycle.

---

## 1. Continuous Integration (CI) Rules

### Purpose

Continuous Integration automates the build and validation process to detect integration issues as early as possible. Its purpose is to guarantee that every code change results in a clearly defined, reliable artefact and does not break shared functionality.

### Key Rules

**a. Every Change Must Trigger a Build**  
Every merge or direct commit to the main integration branch (usually `main` or `develop`) triggers a CI build.  
*Why: This ensures all code entering shared branches has passed validation, preventing 'broken builds' for other developers.*

**b. Builds Must Be Deterministic**  
Given the same input, a build must produce identical artefacts.
*Why: Non-deterministic builds obscure regressions and break reproducibility.*

**c. All Tests Must Pass**  
No commit may enter the main branch unless all automated tests pass for the relevant configuration(s).
*Why: This maintains reliability and prevents undetected regressions.*

**d. Fast Feedback Loops**  
CI pipelines should run in parallel and be optimised for speed without compromising coverage.  
*Why: Rapid feedback minimises time wasted waiting for validation and encourages small, frequent integrations.*

**Practical Example**  
Suppose the repository uses both unit and integration tests. Structure the CI to first run unit tests (quick) and, in parallel, integration tests (slower). Only if both pass does the build artefact proceed to artefact storage or deployment.

---

## 2. Build Graph

### Overview

The build graph defines the dependency structure among build targets (e.g., libraries, applications, containers). It explicitly records which artefacts depend on which others, and in what order builds proceed.

### Why the Build Graph Matters

- **Efficiency**: Building only changed and downstream targets saves time.
- **Correctness**: Ensures dependencies are up-to-date and no stale artefacts remain.
- **Traceability**: Clear dependency chains aid debugging and auditing.

### Build Graph Principles

1. **Explicit Dependency Declaration**  
   Every target must declare its dependencies in the build system (e.g., in `BUILD` files, Makefiles, or equivalent).
2. **Fine-Grained Targets**  
   Divide large builds into small, composable targets.
3. **No Hidden Dependencies**  
   Do not allow side-effects or implicit assumptions. All dependencies must be declared.

**Practical Example**  
If `module-c` depends on `module-b`, which in turn depends on `module-a`, the build system should ensure `module-a` is built before `module-b`, and `module-b` before `module-c`. If only `module-a` changes, the build graph triggers rebuilds of `module-a`, `module-b`, and `module-c`, but not unrelated modules.

---

## 3. Versioning

### Semantics of Versioning

A robust versioning strategy conveys meaning about code and artefact changes.

**a. Semantic Versioning (SemVer)**  
Adopt SemVer: `MAJOR.MINOR.PATCH`  
- Increment MAJOR: incompatible API changes
- Increment MINOR: backwards-compatible feature additions
- Increment PATCH: backwards-compatible bug fixes

**b. Pre-release and Build Metadata**  
Use pre-release labels (`1.2.3-alpha`) for unstable versions, and include build metadata (`1.2.3+20240613.abcdef`) for traceability.

### Version Pinning

- **Lock Third-party Dependencies:** Use `lock` files (e.g. `package-lock.json` or `Pipfile.lock`) to guarantee that builds use the same dependencies each time.
- **Avoid "Latest" Tags:** Never reference a dependency as `latest` or via floating tags in production builds.

### Practical Versioning Example

When a developer adds a non-breaking feature to `lib-foo`, version it as `1.1.0`. If another developer then fixes a bug in this version, bump to `1.1.1`. For an incompatible API change, release as `2.0.0`.

---

## 4. Artefacts

### Artefact Definition

An artefact is any output of the build process intended for distribution or deployment (e.g., binaries, container images, archives).

### Artefact Management

**a. Artefact Storage**  
- All artefacts must be stored in a central, versioned registry (e.g. Artifactory, S3, or similar).
- Artefacts are identified by their version, build timestamp, commit SHA, or a unique identifier.

**b. Immutability**  
- Once stored, artefacts must remain immutable. Never overwrite artefacts with the same version label.

**c. Traceability**  
- Each artefact must be traceable back to its exact source code state (e.g., by tagging with the Git commit SHA).
- Build logs and metadata must be retained for auditability.

**d. Artefact Promotion**  
- Artefacts built in CI should be promoted across environments (e.g., dev → staging → production) by reference, not rebuilt.
- This ensures the artefact tested is exactly the artefact deployed.

**Practical Example**  
A pipeline might build `myapp:1.3.0-abcdef` (where `abcdef` is the commit SHA), upload it to the artefact store, and use exactly that artefact throughout staging and production to guarantee consistency.

---

## Summary Checklist

- [ ] All code changes trigger a CI process
- [ ] CI builds are fast, deterministic, and test-complete
- [ ] All build dependencies are explicit and versioned
- [ ] Use semantic versioning and lock all dependencies
- [ ] Produced artefacts are immutable and traceable
- [ ] Artefacts are promoted across environments by reference, not by rebuilding

---

## See Also

- [Testing and Quality Assurance](./testing-and-qa.md)
- [Environment Promotion Flow](./environment-promotion.md)
- [Dependency Management](./dependency-management.md)