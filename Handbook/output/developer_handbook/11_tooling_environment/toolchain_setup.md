# Toolchain Setup

This page documents the required procedures and rationale for installing and verifying the SDK and toolchain, ensuring development environments are consistent with Continuous Integration (CI).

---

## Overview

Correct setup of the software development kit (SDK) and associated toolchain is essential for deterministic builds, efficient development, and reliable CI integration. Discrepancies between local and CI environments are a leading cause of “it works on my machine” failures. This page details how to establish, verify, and maintain a toolchain that guarantees parity and reproducibility, avoiding subtle environment-related defects.

---

## 1. Toolchain Components

For our purposes, the *toolchain* refers to the collection of software required to build, test, and package software reliably. This typically includes:

- The core SDK (e.g., language runtimes, compilers, base libraries)
- Build tools (e.g., `make`, `cmake`, `gradle`, `npm`)
- Dependency managers (e.g., `pip`, `yarn`, `cargo`)
- Linters and formatters (where applicable)
- Platform-specific tools (emulators, device SDKs, etc.)

**Note:** All specific tool versions must match those specified in project documentation and CI configuration files.

---

## 2. SDK Installation

### a. Local Environment

1. **Reference the CI Configuration:**
   - Start by reviewing `Dockerfile`, `.github/workflows/`, or CI manifests (e.g., `circle.yml`, `Jenkinsfile`).
   - Identify exact SDK versions and any environment variables or flags used during builds.

2. **Use Version Managers Where Possible:**
   - For languages with active managers (e.g., `pyenv` for Python, `nvm` for Node.js, `sdkman` for JVM), prefer these to installing system-wide.
   - This enables easy switching, strict version alignment, and isolation from other system projects.

   **Example:**  
   To match Node.js version 20.5.0 in CI:
   ```shell
   nvm install 20.5.0
   nvm use 20.5.0
   ```

3. **Install Dependencies:**
   - If the project uses a lockfile (e.g., `package-lock.json`, `Pipfile.lock`), always install via the lockfile:
     ```shell
     npm ci            # Enforces dependency versions
     pip install -r requirements.txt
     ```
   - If custom build images or scripts are used in CI, replicate their steps locally.

4. **Configure Path and Environmental Variables:**
   - Confirm any required environment variables are set (e.g., `JAVA_HOME`, `ANDROID_HOME`).
   - Use project `.env` files or system profile scripts judiciously (do not hardcode secrets).

### b. Automated / Onboarding Scripts

- Use bootstrapping scripts (`./setup.sh`, `Makefile`, etc.) for consistency and to reduce manual error.
- Scripts must perform all steps required to match the CI setup, including:
  - Tool installation and version checks
  - Dependency installation
  - Environment variable initialisation

#### Example (Partial `setup.sh`):
```bash
#!/bin/sh
nvm install 20.5.0
nvm use 20.5.0
npm ci
```

**Expectation:**  
Every engineer must be able to onboard or reset their toolchain solely with the provided scripts and documentation.

---

## 3. Verification

### a. Version Checks

After installing, always verify versions:

```shell
node --version               # Expect: v20.5.0
npm --version                # Match CI
python --version             # Match requirements
```

**Tip:**  
Automate this verification with a script (e.g., `./check-versions.sh`) that fails if deviations are found.

### b. Reproducibility Test

- Run the exact build and test commands used in CI locally.
- Build results (artifacts, output, test pass/fail) must identical between local and CI runs.
- If not, revisit differences in tool versions, OS packages, or configuration.

---

## 4. CI Parity: Why It Matters

Maintaining parity between development and CI environments prevents undetected integration failures, “works for me” bugs, and wasted troubleshooting time. CI is the definitive source of a working build; local environments must be meticulously synchronised to this standard.

**Common issues from poor parity:**
- Failing CI builds due to out-of-date dependencies or incompatible tool versions.
- Local tests passing while CI reports errors due to subtle environmental differences.
- Deployment or runtime failures caused by mismatched binary builds.

---

## 5. Maintenance and Updates

- Any update to tool versions in CI *must* be reflected in onboarding scripts and developer documentation immediately.
- Changes in SDK/toolchain should trigger a review of all relevant configuration and lockfiles.
- Use automated tools (e.g., Dependabot, Renovate) where safe, but always check parity after any automated update.

---

## 6. Troubleshooting

- **Issue:** CI passes, but local build fails  
  **Action:** Re-run setup scripts; verify all tool versions; clean and reinstall dependencies.
- **Issue:** Local tests pass, CI tests fail  
  **Action:** Check for uncommitted lockfiles, local-only dependencies, versioning inconsistencies, or missing environmental variables.
- **Issue:** Difficulties installing a specific SDK version  
  **Action:** Refer to CI’s Dockerfile or image; use exact base images or containers locally if required.

---

## 7. Summary of Expectations

- The local environment *must not* diverge from CI in any material way.
- Install all tools as per the documented version, using scripts and managers.
- Verify setup with exact version checks and by reproducing CI builds locally.
- Address environment failures by comparing local and CI tooling/configuration step by step.

**If any necessary action is unclear or not covered, update this page immediately to prevent ambiguity for future team members.**

---

**Next:** See the [Environment Replication](./environment_replication.md) page for containerisation and advanced parity strategies.