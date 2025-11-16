# Build Identification

Build identification ensures that every deliverable, release, or deployment can be traced, verified, and managed effectively. This page provides clear, actionable guidance on applying versioning schemes (SemVer, CalVer), embedding build metadata, and producing a Software Bill of Materials (SBOM) as part of your release and delivery process.

---

## 1. Purpose and Importance of Build Identification

Effective build identification underpins reliability and traceability in software engineering:

- **Traceability:** Allows precise mapping between delivered bytes, source code, dependencies, and configuration.
- **Rollbacks & Audits:** Enables accurate rollback, reproduction, and investigation of issues.
- **Automation:** Facilitates CI/CD, deployment management, and dependency resolution.
- **Customer Support:** Simplifies diagnosis and communication of issues encountered in the field.
- **Security & Compliance:** Supports vulnerability management by tracking component versions and provenance.

---

## 2. Versioning: Semantic Versioning (SemVer) and Calendar Versioning (CalVer)

### 2.1 Semantic Versioning (SemVer)

**Definition:**  
SemVer is a versioning scheme that encodes meaning about the underlying code and what has been modified from one version to the next.

**Format:**  
`MAJOR.MINOR.PATCH`, e.g. `2.5.1`

- **MAJOR**: Incremented for incompatible API changes.
- **MINOR**: Incremented for adding functionality in a backwards-compatible manner.
- **PATCH**: Incremented for backwards-compatible bug fixes.

**When to use:**  
Use SemVer for libraries, APIs, or products where interface stability is significant and users may programmatically react to breaking changes.

**Rationale:**  
SemVer enables consumers and integrators to understand at a glance:
- Whether an update can be safely adopted.
- If dependent integrations may break.

**Example:**  
- `1.4.2` (backwards-compatible bug fix)
- `2.0.0` (breaking change to public API)

### 2.2 Calendar Versioning (CalVer)

**Definition:**  
CalVer encodes the release date into the version number.

**Format:**  
Common patterns include `YYYY.MM.DD` (`2024.06.13`) or `YYYY.MM` (`2024.06`).

**When to use:**  
Use CalVer for applications, products or artefacts where time-based releases matter more than API guarantees — for example, client applications, system images, or regularly scheduled updates.

**Rationale:**  
CalVer removes ambiguity from time-based releases and supports rapid, frequent delivery where strict API compatibility has lower priority.

**Example:**  
- `2024.06.1` (first release in June 2024)
- `24.6` (June 2024 major release)

### 2.3 Choosing a Scheme

- Use **SemVer** for libraries and modules with published interfaces.
- Use **CalVer** for products and clients released on a routine schedule.
- Never mix SemVer and CalVer in the same series for a component.

Define your versioning policy in your repository documentation and ensure that build pipelines enforce it.

---

## 3. Build Metadata

Build metadata supplies additional context beyond the version number, conveying details necessary for full traceability.

### 3.1 Typical Metadata Fields

- **Commit Reference:** The source control commit hash (e.g., Git SHA) the build was generated from.
- **Build Timestamp:** The date and time (preferably in UTC and ISO 8601 format) of the build.
- **Build Number/ID:** An auto-incremented number, unique per build.
- **Builder Identity:** The username or service responsible for the build, where appropriate.
- **Branch/Tag:** The source branch or tag in VCS.

### 3.2 Embedding Metadata

**How to embed metadata:**

- **As part of artefact file names:** e.g., `myapp-1.5.3+20240613.gitabcdef.tar.gz`.
- **In application manifests/config files:** e.g., JSON, XML, or YAML.
- **With version info commands:** e.g., exposing `myapp --version` that prints version and build metadata.
- **As build artefact annotations:** e.g., in Docker image labels.

**Best Practices:**

- Always record at least the commit hash and build timestamp.
- For reproducible builds, capture enough metadata to reconstruct the build context.
- Ensure tools, scripts, and build pipelines automate metadata generation and embedding.

**Example:**

```json
{
  "version": "2.7.1",
  "commit": "abcdef1234567890",
  "build_time": "2024-06-13T11:45:00Z",
  "branch": "release/2.7",
  "builder": "ci-system"
}
```

---

## 4. Software Bill of Materials (SBOM)

An SBOM is a machine-readable inventory of all components, libraries, and direct dependencies used to build a software artefact.

### 4.1 Why produce an SBOM?

- **Vulnerability Management:** Rapidly correlate artefacts with published vulnerabilities (CVEs).
- **Compliance:** Meet requirements for supply chain transparency.
- **Incident Response:** Quickly identify shipped versions and their constituent parts.

### 4.2 What to include

Your SBOM must capture:

- All runtime dependencies (direct and, where possible, transitive).
- Component names, versions, and cryptographic checksums.
- Licence information (for dependency compliance).
- Build system and environment details (optional, for stricter compliance).

### 4.3 SBOM Formats

Common formats:

- **SPDX** (Software Package Data Exchange): Widely accepted and tool-supported.
- **CycloneDX:** Specifically designed for software supply chains.

**Choose the format mandated by your compliance or customer requirements.**

### 4.4 Practical Generation and Distribution

- Automate SBOM generation as a build step using tools appropriate for your language or platform.
- Include the SBOM as an artefact alongside builds.
- For container images, embed or attach the SBOM in standard image labels or as associated files in your artefact repository.

**Example command (CycloneDX for Python):**

```shell
cyclonedx-py -o sbom.json
```

Include artefact and SBOM pairing in your release documentation.

---

## 5. Engineering Expectations

- Apply the chosen versioning scheme consistently. Transitions or exceptions must be documented and justified.
- Every release artefact must be uniquely identifiable with a version and embedded metadata.
- Every production build must generate and publish an SBOM.
- The build identification process must be automated and included in CI/CD.

---

## 6. Summary Checklist

- [ ] **Version assigned** according to documented scheme (SemVer/CalVer)
- [ ] **Build metadata** captured and embedded
- [ ] **SBOM** generated and attached to artefact
- [ ] **Release documentation** updated with identification details

---

**Reference this page whenever defining, producing, or verifying released or delivered software artefacts.**