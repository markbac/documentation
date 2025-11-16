# End-to-End Process

This page documents the complete lifecycle flow for engineering work, including key stages (gates) and required artefacts. The process enables consistent, predictable delivery and ensures all aspects of work—from initial idea to operational handover—are considered, controlled, and communicated.

---

## 1. Overview

An end-to-end process ensures that every piece of work traverses a clearly defined set of stages, each with explicit exit criteria (gates). Each gate requires completion of specific, auditable artefacts. This systematic approach:

- Reduces ambiguity on status and expectations,
- Ensures cross-functional alignment,
- Identifies and manages risks early,
- Promotes consistent, repeatable outcomes.

This guidance is applicable to both small and large engineering initiatives, though scale and detail may vary. Minor changes may use lightweight artefacts, while major projects will demand fuller documentation.

---

## 2. Lifecycle Stages

The standard lifecycle for engineering work comprises the following stages:

1. **Idea**
2. **Initiation**
3. **Design**
4. **Implementation**
5. **Verification**
6. **Deployment**
7. **Closure**

Each stage has a corresponding gate with required artefacts and approval criteria.

---

### 2.1. Idea

**Purpose:** Define the problem or opportunity, capturing the genesis for change.

**Key Activities:**

- Articulate the business or technical problem.
- Capture who is affected and potential value.
- Log basic scope and constraints.

**Required Artefacts:**

- Problem Statement
- Initial Stakeholder List

**Gate:** Entry to Initiation requires sign-off from a relevant domain or product owner confirming the problem's value and alignment.

**Why it matters:** Unclear, misaligned, or poorly motivated work wastes time and dilutes focus. Early clarity streamlines downstream decision-making.

**Practical Example:** A support engineer identifies manual data checks causing delays. They log a problem statement: "Manual steps in onboarding add two days per customer."

---

### 2.2. Initiation

**Purpose:** Refine scope, confirm feasibility, and secure sponsorship.

**Key Activities:**

- Assess technical and resource feasibility.
- Identify primary stakeholders and dependencies.
- Estimate high-level impact (time, effort, cost).

**Required Artefacts:**

- Feasibility Assessment
- Stakeholder Map
- Initial Risk List

**Gate:** Entry to Design requires approval from project sponsors and architectural lead, ensuring high-level alignment and resource availability.

**Why it matters:** Feasibility checks prevent loss of effort on impossible or non-viable problems and uncover hidden dependencies early.

---

### 2.3. Design

**Purpose:** Decide *how* the work will be done. Define the solution.

**Key Activities:**

- Select preferred architectural/design approach.
- Produce detailed technical designs and diagrams.
- Review designs with relevant experts.

**Required Artefacts:**

- Solution Design Document (SDD) or Architecture Decision Record (ADR)
- Updated Risk and Dependency Log
- Acceptance Criteria

**Gate:** Design review and sign-off by domain experts, lead engineers, and (if appropriate) information security.

**Why it matters:** Design phase transforms intent into executable plans, exposing flaws before costly build work. Shared artefacts avoid local, undocumented decision-making.

**Practical Example:** The team chooses between building an in-house ETL pipeline or integrating with an existing tool, documenting trade-offs and rationale.

---

### 2.4. Implementation

**Purpose:** Transform designs into working solutions.

**Key Activities:**

- Code, configure, and integrate components per design.
- Develop tests: unit, integration, and end-to-end.
- Document implementation specifics (readmes, API docs).

**Required Artefacts:**

- Source Code Repository (with branching, reviews, issue tracking)
- Implementation Readme or Technical Notes
- Test Evidence (for completed requirements)

**Gate:** Code reviews (typically by peer and tech lead); must meet coding standards, coverage thresholds, and pass all agreed test cases.

**Why it matters:** Structured, peer-reviewed implementation reduces production defects and technical debt.

---

### 2.5. Verification

**Purpose:** Confirm the solution works as intended.

**Key Activities:**

- Execute functional, non-functional, and security testing.
- Validate acceptance criteria from design.
- Collate defect logs and confirm resolution.

**Required Artefacts:**

- Test Results Report (showing all acceptance criteria met)
- Security and Compliance Sign-off (if relevant)
- User Acceptance Test (UAT) sign-off (if required)

**Gate:** Test review and sign-off by testing leads and (optionally) product owner.

**Why it matters:** Rigorous verification minimises live failures, supports compliance, and provides traceability.

---

### 2.6. Deployment

**Purpose:** Place the solution into its operational environment securely and confidently.

**Key Activities:**

- Prepare deployment plan (timings, rollback, communication).
- Execute deployment using approved pipeline/tooling.
- Confirm post-deployment health checks.

**Required Artefacts:**

- Deployment Plan (including rollback strategy)
- Change Management Approval / CAB Record
- Deployment Confirmation

**Gate:** Approval to deploy, confirmation of change management procedures, and post-deployment sign-off.

**Why it matters:** Structured deployment reduces risk of outages, provides audit trail, and supports rapid recovery if issues occur.

---

### 2.7. Closure

**Purpose:** Complete the activity and hand over for ongoing operation.

**Key Activities:**

- Document any outstanding risks or technical debt.
- Complete lessons learned / post-mortem.
- Update operational support manuals.
- Confirm handover to support and/or business owners.

**Required Artefacts:**

- Handover Document (support contacts, operational details)
- Lessons Learned Report
- Final Risk Register

**Gate:** Project closure checklist, transfer of ownership to support or business.

**Why it matters:** Proper closure ensures nothing is left behind, and learnings are captured to improve future work.

---

## 3. Artefacts: Expectations and Ownership

All artefacts should be:

- Version-controlled (where possible),
- Easily accessible to all relevant stakeholders,
- Sufficiently detailed to support audit, handover, and re-use.

Artefact ownership is typically with the team delivering the work, but sign-offs must come from appropriate stakeholders as described above.

---

## 4. Exceptions and Lightweight Processes

For very minor changes (e.g., a one-line code fix), artefacts and gates may be compressed, but *never omitted* entirely. For example, a bugfix:

- May have the 'Design' gate combined with a short code review,
- Testing evidence may be a ticket comment rather than a formal report.

Use judgement, but always ensure the core intent of each stage is preserved.

---

## 5. Frequently Asked Questions

**Q: Do all projects need full documentation for each artefact?**  
A: No, the scale and rigour should be proportionate, but every stage must be represented and key decisions documented.

**Q: Who approves gates?**  
A: Gatekeepers are as described above—generally a mix of product, technical, and compliance leads, depending on the gate.

**Q: What if urgent work requires bypassing a gate?**  
A: Escalate to your engineering manager or process owner. Retrospective documentation is required if skipping ahead due to exceptional circumstances.

---

## 6. Summary Table

| Stage          | Gatekeeper(s)                  | Key Artefacts                                |
|----------------|-------------------------------|----------------------------------------------|
| Idea           | Domain/Product Owner           | Problem Statement, Stakeholder List          |
| Initiation     | Sponsor, Architectural Lead    | Feasibility Assessment, Stakeholder Map      |
| Design         | Technical/Domain Experts       | SDD/ADR, Risks, Acceptance Criteria          |
| Implementation | Tech Lead, Peer Reviewers      | Code, Readme, Test Evidence                  |
| Verification   | Test Lead, (Product Owner)     | Test Report, UAT Sign-off, Security Sign-off |
| Deployment     | Change/Release Board           | Deployment Plan, CAB Record                  |
| Closure        | Project Manager/Support Lead   | Handover Docs, Lessons Learned, Risk Log     |

---

## 7. See Also

- [Architecture Decision Records (ADR) Standards](./architecture-decision-records)
- [Coding Standards](./coding-standards)
- [Release Management Process](./release-management)

---

**Adherence to the end-to-end process is mandatory unless process owners explicitly approve an exception.** For questions, consult your delivery or technical lead.