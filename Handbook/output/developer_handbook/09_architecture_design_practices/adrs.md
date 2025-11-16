# Architecture Decision Records (ADRs)

Architecture Decision Records (ADRs) provide a consistent, auditable way to document significant technical decisions in an engineering project. This page describes the purpose, structure, and practical management of ADRs, with concrete guidelines and examples for effective use.

---

## Purpose and Rationale

Engineering projects involve numerous, often complex, architectural decisions. These decisions can profoundly affect everything from system quality to future maintenance cost. However, without systematic documentation, the context and reasoning behind these decisions is easily lost—especially as teams evolve.

**ADRs ensure:**
- **Knowledge continuity:** New and existing team members understand why systems are designed as they are.
- **Traceable intent:** Each major decision and its context is recorded, making it easier to revisit or challenge assumptions.
- **Consistent decision-making:** Facilitates structured, explicit evaluation of options, risks, and trade-offs.

---

## What to Document as an ADR

Not all decisions need an ADR. ADRs should be created for decisions that:
- Affect the system architecture or its long-term maintainability.
- Change interfaces, infrastructure, or key technology choices.
- Impact data models, communication patterns, or fundamental workflows.
- Are non-obvious, controversial, or likely to be revisited.

**Do not** use ADRs for minor or routine change details; these belong in code comments or pull request descriptions.

---

## ADR Structure

A standard ADR uses a simple, repeatable template. The template below covers essential elements and supports consistency across the team.

### Template Example

```markdown
# <Decision Title>

**Status:** {Proposed | Accepted | Superseded | Deprecated | Rejected}  
**Context:** <Background, constraints, relevant information>  
**Decision:** <What was decided?>  
**Consequences:** <What happens because of this decision?>  
**Alternatives:** <What other options were considered and why were they rejected?>
```

### Section Details

- **Title:** A concise description of the architectural issue/decision.
- **Status:** Reflects the ADR's current state (see [Managing ADRs](#managing-adrs)).
- **Context:** Explains *why* this decision was needed, including constraints, goals, and any relevant history.
- **Decision:** Clearly state *what* has been decided, without ambiguity.
- **Consequences:** Discusses both positive and negative effects, including technical debt, work required, or risks created/resolved.
- **Alternatives:** Identify the serious options considered and briefly summarise the rationale for rejecting them.

#### Practical Example

```markdown
# Choose PostgreSQL for Transactional Data Storage

**Status:** Accepted  
**Context:**  
The system requires a reliable, ACID-compliant data store for financial transactions. Writes and reads occur at moderate scale. We require strong data integrity guarantees and transactional support.

**Decision:**  
PostgreSQL will be adopted as the primary database for transactional data.

**Consequences:**  
- Leverages team experience with SQL and PostgreSQL.
- Ensures robust ACID compliance.
- Introduces operational overhead in managing PostgreSQL clusters.
- Locks out document-based or NoSQL data models for this core data.

**Alternatives:**  
- **MongoDB:** Lacks full ACID guarantees and mature transaction support in required version.
- **MySQL:** Team has less experience; PostgreSQL offers features needed for this workload.
```

---

## Writing Effective ADRs

- **Be clear and specific.** Use unambiguous language; include enough context so a reader unfamiliar with the decision understands its motivation.
- **Focus on rationale.** Clearly explain *why* a particular choice was made, not just *what* was chosen.
- **Balance brevity and completeness.** The ADR should be self-contained, but avoid unnecessary repetition or unrelated topics.
- **Consider longevity.** Assume the ADR will be referred to months or years later, potentially by someone with limited background in the project.

---

## Managing ADRs

### Location and Naming

- Store ADRs in a dedicated directory at the project root, e.g. `docs/adr/` or `architecture/adr/`.
- Use sequential numbering and descriptive filenames:  
  `0001-choose-postgresql-for-transactional-storage.md`

### Status Management

Each ADR must clearly indicate its status:
- **Proposed:** Under discussion, not yet formally adopted.
- **Accepted:** Decision is in force and being implemented.
- **Superseded:** Replaced by a newer ADR; reference the successor.
- **Deprecated:** No longer relevant, but not necessarily replaced.
- **Rejected:** Considered but not adopted.

Update ADR statuses as new decisions replace or invalidate old ones, maintaining historical integrity.

### Referencing and Linking

- Reference ADR numbers in commit messages, pull requests, or other documentation to clarify why changes are made.
- If one ADR supersedes or relates to another, add explicit links.

### Review and Evolution

- Regularly review ADRs during retrospectives or architectural reviews.
- If a decision changes, write a new ADR explaining the change; do not rewrite history.

---

## Expectations and Best Practices

- Creating an ADR is a required step when making any significant architectural decision.
- All ADRs must follow the structured template provided.
- The ADR directory should be reviewed by all relevant stakeholders.
- ADR discussions and reviews should be open and collaborative.
- Use version control—ADRs are part of project source and history.
- Periodically audit for outdated or superseded ADRs, and update statuses accordingly.

---

By consistently documenting architectural decisions with ADRs, teams create transparency, reduce ambiguity, and provide a clear technical rationale for the project’s evolution. This practice is fundamental to high-quality, sustainable engineering work.