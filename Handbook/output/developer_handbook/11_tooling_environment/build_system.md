# Build System

## Overview

The build system constitutes the backbone of our software delivery pipeline. It encompasses scripts, configuration, and tooling to transform source code and dependencies into deployable artefacts. Robust build systems enable *reproducibility*, ease *onboarding*, and facilitate *automation*. This page details requirements, best practices, and practical steps for achieving reliable builds through reproducibility, containerisation, and well-defined toolchains.

---

## Reproducible Builds

### What Is a Reproducible Build?

A reproducible build guarantees that, given the same source code and build environment, repeated invocations produce identical artefacts (byte-for-byte). This ensures that any engineer, CI system, or automated process obtains consistent results, facilitating debugging, compliance, and rollbacks.

### Why Is Reproducibility Important?

- **Debugging:** Identical builds simplify the investigation of defects, as artefacts can be traced back to known source points.
- **Security:** Reproducibility mitigates the risk of compromised builds introducing unverified binaries.
- **Compliance:** Regulatory and customer requirements may demand provenance for every release.
- **Collaboration:** Parallel efforts across teams and environments remain synchronised if builds are consistent.

### Core Requirements

To achieve reproducible builds, adhere to the following:

- **Pin Dependency Versions:** All dependencies (libraries, frameworks, build tools) must have explicit, version-pinned references. Avoid version wildcards.
    - *Example:* In Python, prefer `requirements.txt` with explicit version numbers.
- **Control Build Inputs:** Ensure environmental factors (e.g., environment variables, file system state, timestamps) do not affect artefact generation.
    - *Example:* Tools like `SOURCE_DATE_EPOCH` can fix build timestamps.
- **Eliminate Non-determinism:** Remove or control sources of randomness during builds (e.g., random ordering, unseeded RNG).
- **Stateless Builds:** Assume the build runs on a clean environment with no cross-build state.

---

## Containerisation

### Role of Containers in Builds

Containerisation encapsulates the build environment, ensuring that all build steps run under defined, isolated conditions. Adopting Docker or equivalent container tooling for builds prevents "it works on my machine" scenarios by:

- **Standardising Tool Versions:** All team members and CI/CD systems use identical compilers, interpreters, and utilities.
- **Isolating Dependencies:** External system libraries and toolchains are shielded from host variations.

### Core Expectations

- **Maintain a Dockerfile or Base Image:** Each service or component must include a version-controlled Dockerfile specifying the build environment, or reference a managed base image.
    - *Example:*
        ```Dockerfile
        FROM python:3.11-slim
        RUN pip install --require-hashes -r requirements.txt
        ```
- **Build Inside Containers by Default:** Local and CI builds should invoke commands within containers unless technical constraints exist.
    - *Practical approach:* Use `docker-compose` or `make` targets for a straightforward build entry point.
- **Document Host Assumptions:** If certain tools (e.g., `docker`, `make`) are required on the host, these must be minimal, clearly documented, and stable across platforms.
- **Audit Image Updates:** Dependabot or scheduled CI processes should check for base image and dependency security updates.

---

## Toolchains

### Definition and Scope

A toolchain encompasses the compilers, interpreters, build tools, and auxiliary utilities required to turn source code into artefacts. Consistency in toolchains forestalls unexpected discrepancies and build failures.

### Toolchain Management

- **Declare All Tools and Versions:** List all required tools and versions in the repository documentation (`README.md` or equivalent).
    - *Example:* Java 17, Maven 3.9.0, Node.js 18.15.0.
- **Automate Tool Provisioning:** Avoid manual installations. Use scripts (or containerised setups) to ensure all necessary binaries are installed and accessible in the build stage.
    - *Example:* For Java builds, include `apt-get install openjdk-17-jdk` in the Dockerfile.
- **Vendor or Pin Non-repository Tools:** If a build depends on tools not available via the chosen container image or base distribution, fetch and vendor them at explicit versions as part of the build process.
- **Avoid Global Host Dependencies:** Never rely on tools implicitly present on developer laptops or CI workers.

---

## Practical Examples

### Containerised Build with Make and Docker

A recommended setup combines `Makefile` targets with Docker builds, keeping local and CI usage consistent:

```Makefile
.PHONY: build
build:
    docker build -t myapp-build .
    docker run --rm -v $(PWD):/src myapp-build bash -c "cd /src && ./scripts/build.sh"
```

- Developers invoke `make build` regardless of OS or local package versions.
- The `Dockerfile` describes the build environment; `build.sh` executes necessary steps.

### Pinning Python Dependencies

```txt
# requirements.txt
flask==2.2.5
requests==2.31.0
# requirements.txt generated from poetry.lock or pipenv lock
```
Using `pip install --require-hashes -r requirements.txt` enforces both the version and the exact artefact hash.

---

## Summary of Expectations

- All code must be built reproducibly: identical inputs yield identical outputs.
- Build systems must use containerisation to control the environment.
- All toolchains must be explicitly defined and version-pinned.
- Builds must not depend on developer-specific or external machine state.
- Processes and commands for local and CI builds must be aligned and fully automated.

Adhering to these principles ensures reliable and predictable builds, accelerates team onboarding, and strengthens the integrity of deliverables.