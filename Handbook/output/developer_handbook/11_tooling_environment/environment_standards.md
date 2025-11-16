# Environment Standards

This page defines the standards for development and deployment environments within the engineering organisation. Adhering to these standards ensures reliability, repeatability, and security across all workflows. This document covers required practices around OS images, dependency pinning, and tooling baselines.

---

## 1. Operating System Images

### 1.1. Approved OS Images

All project environments—whether for local development, CI pipelines, or production—must utilise OS images from the centrally maintained and approved list (see [Internal OS Image Catalogue](#)). These images are built and managed by the platform team to:

- Ensure security patches are applied promptly.
- Maintain compatibility with required toolchains.
- Reduce variability across environments.

Do **not** use ad hoc or community-sourced images in any official workflow.

#### Example

- **Correct**: Using the approved `ubuntu-22.04-lts-engineering` image for CI jobs.
- **Incorrect**: Pulling `ubuntu:latest` or an unlisted community image directly from Docker Hub.

### 1.2. Version Pinning of OS Images

Always reference OS images by their explicit, immutable tag (e.g., `ubuntu-22.04-lts-engineering@sha256:...`) rather than mutable tags like `latest` or simply a version number. This practice maintains reproducibility and prevents inadvertent environment changes.

#### Example

```yaml
# Correct
image: ubuntu-22.04-lts-engineering@sha256:abcd1234...

# Incorrect
image: ubuntu-22.04-lts-engineering
```

## 2. Dependency Pinning

### 2.1. Runtime and Build Dependency Pinning

All system, language, and build tool dependencies must be **explicitly pinned** to a specific version within your project. This mitigates:

- "Works on my machine" issues due to environmental drift.
- Build failures arising from sudden dependency updates.
- Security risks from unvetted, new dependency versions.

#### Practical Implementation

- For **Python projects**, use a `requirements.txt` or `poetry.lock` file to lock versions.
- For **Node.js projects**, commit a reliable `package-lock.json` or `yarn.lock`.
- For **Ubuntu-based systems**, use apt's version specification, e.g. `build-essential=12.4ubuntu1`.

**Never** use version specifiers such as `*`, `latest`, or open-ended ranges unless there is a documented justification and a specific business need. 

### 2.2. Documenting Dependencies

Document all externally relevant dependencies in your project’s README and maintainers should periodically audit them. This fosters transparency and simplifies onboarding and incident response.

## 3. Tooling Baselines

### 3.1. Standard Tooling Versions

Across the organisation, specific versions of compilers, interpreters, and developer tools must be used, as maintained in the [Engineering Tooling Baseline](#). This includes (but is not limited to):

- Programming language runtimes (e.g., Python, Node.js, Java)
- Build tooling (e.g., Maven, Gradle, Make)
- CI/CD utilities (e.g., Docker, kubectl)
- Security and static analysis tools

Updating tool versions requires following the prescribed review and testing process to avoid breaking changes.

### 3.2. Local Development Environments

Leverage environment management solutions where appropriate:
- **pyenv** or **asdf** for Python or multi-language setups.
- **Docker** or **podman** for ephemeral, self-contained environments.

Local developer environments **must** mirror CI and production versions for all core dependencies and tooling, as verified by onboarding scripts or validation checks provided in each repository.

#### Example

A `.tool-versions` file for asdf:

```
python 3.10.6
nodejs 18.16.0
```

## 4. Rationale: Why These Standards Matter

- **Reliability:** Stable, immutable environments reduce incidents caused by unintended changes or upgrades.
- **Reproducibility:** Explicit pinning allows any engineer (or automation system) to recreate a known-good environment, making debugging and compliance straightforward.
- **Security:** Controlling OS images and tool versions enables timely patching and vulnerability management.
- **Efficiency:** Reducing environmental variability prevents time loss diagnosing environment-dependent bugs and accelerates onboarding.

## 5. Expectations and Enforcement

- Environments that deviate from these standards will not be accepted in CI pipelines or deployment workflows.
- New projects must adopt the latest approved standards at inception.
- Existing projects should prioritise migration to these standards as part of ongoing technical debt work.
- The platform team audits environment configurations quarterly, and critical deviations will trigger remediation tasks.

---

If you are unsure whether a tool, dependency, or image meets the standards, consult the platform team or refer to the authoritative catalogues and baseline documentation linked above.