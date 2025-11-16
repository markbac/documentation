# Docs-as-Code

This page outlines best practices for implementing Docs-as-Code principles within engineering projects. It provides detailed guidance on repository structure, review workflow, and link management rules, ensuring documentation is robust, maintainable, and traceable.

---

## Overview

Docs-as-Code treats documentation with the same rigour as software code. Documentation is stored in version control, reviewed using structured workflows, and subject to the same traceability and quality controls as source code. This approach enhances accuracy, facilitates collaboration, and ensures documentation evolves alongside software.

---

## 1. Repository Structure

### 1.1. Co-location vs. Dedicated Documentation Repositories

**Co-location (within code repositories):**
- Use when documentation tightly couples to a single codebase or component.
- Simplifies synchronisation of docs and code changes.
- Example: Place documentation in a top-level `/docs` directory.

**Dedicated documentation repositories:**
- Use for cross-cutting project guides, overarching architecture documents, or when multiple codebases are referenced.
- Avoids duplication; clarifies document ownership.

**Recommendation:** Choose co-location for component-level or API docs. Use dedicated repositories for system-wide or process documentation.

### 1.2. Standard Directory Structure

Use a clear, consistent directory structure within documentation repos or `/docs` directories:

```
/docs
  /architecture
  /design
  /how-to
  /reference
  /release-notes
  /guides
```

- **/architecture:** System diagrams, high-level overviews.
- **/design:** Low-level specifications, decision records.
- **/how-to:** Task-based step-by-step guides.
- **/reference:** API details, configuration options.
- **/release-notes:** Versioned change logs.
- **/guides:** Tutorials, onboarding material.

**Why this matters:** Standardisation reduces onboarding time, prevents misplacement of documents, and supports automated discovery and publishing.

---

## 2. Review Workflow

### 2.1. Documentation as Pull Requests (PRs)

- All documentation changes must be submitted as PRs, not direct commits to main branches.
- PR descriptions should summarise scope, intent, and links to related tickets (if any).

### 2.2. Required Reviewers

- At least one subject matter expert and one peer reviewer (not identical roles).
- For architecture or cross-team docs, solicit a reviewer from each relevant team.
- Use version control tools to enforce review before merge (e.g., branch protection rules).

### 2.3. Approval Criteria

- Technical accuracy and clarity.
- Structure aligns with directory and style guidance.
- Links are valid (see Link rules).
- Where diagrams or artefacts are included, source files (e.g., `.drawio`, `.svg`) are present.
- Traceability to code, ticket, or decision records is documented if relevant.

### 2.4. Traceability

- Reference code PRs, tickets, or decision records directly within documentation PRs (e.g., “Relates to #42”).
- Update documentation in the same PR as code changes where possible.
- For large documentation tasks, maintain a checklist or task list in the PR.

**Why this matters:** Review workflows ensure documentation is accurate, current, and trusted. Traceability links maintain historical context and fulfil audit requirements.

---

## 3. Link Rules

### 3.1. Internal Links

- Use **relative links** (`../reference/configuration.md`) for documents within the same repository.
- Avoid absolute paths, as they break during renaming or restructuring.

**Example:**

```markdown
See [Configuration Reference](../reference/configuration.md) for details.
```

### 3.2. External Links

- Use full URLs and include a brief descriptor.
- Link to stable, official sites only.
- Record date accessed for standards or specifications likely to change.

**Example:**

```markdown
See [OpenAPI Specification (v3.1)](https://spec.openapis.org/oas/v3.1.0) (accessed 20 June 2024).
```

### 3.3. Link Checking

- Use automated link checkers (CI jobs) to flag broken links on every PR and scheduled basis.

### 3.4. Link Maintenance

- Refactor links proactively during file or directory renames.
- For deprecations, replace links or include a redirect note.

**Why this matters:** Proper link management prevents documentation rot, ensures users find the correct references, and supports maintainability.

---

## 4. Practical Guidelines

- **Each document must have a clear purpose and ownership.**
- **All diagrams or non-text artefacts should include editable source files.**
- **Apply the same standards of versioning and traceability to documentation as to code.**
- **Automate checks for formatting, spelling, and broken links.**
- **Adopt a changelog or release-notes pattern for significant documentation shifts.**

---

## Summary

Applying Docs-as-Code ensures engineering documentation is reliable, traceable, and evolves alongside the systems it describes. Adhering to these repository structures, workflows, and link rules guarantees consistency, reduces friction, and upholds a high standard across all project documentation.