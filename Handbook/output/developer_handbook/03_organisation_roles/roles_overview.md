# Roles Overview

This page outlines the primary engineering disciplines within the organisation, clarifies their core functional responsibilities, and establishes practical boundaries between roles. Clear definition of roles reduces confusion, improves collaboration, and streamlines accountability. This page must be read and understood by all technical team members and leads.

## Purpose of Role Definitions

Defining roles and their respective boundaries ensures that:

- Team members understand their scope of authority and responsibility.
- Dependencies and hand-off points between disciplines are explicit.
- Ambiguity and duplicated effort are avoided.
- Decision-making processes are unambiguous, leading to efficient project delivery.

## Core Engineering Disciplines

### 1. **Product Management (PM)**

**Responsibilities:**
- Defines the product vision, strategy, and roadmap based on user needs and business objectives.
- Owns the prioritisation of features, bug fixes, and technical work for delivery.
- Facilitates requirements gathering and documentation with stakeholders.

**Boundaries:**
- PMs do not dictate technical implementation, but set requirements and priorities.
- Final authority on acceptance criteria and release timelines.

**Rationale:**
Product Managers ensure the engineering team builds the right thing, not just builds things right. They provide the “what” and “why” of product development, leaving the “how” to engineering.

**Example:**  
The PM prioritises a new authentication feature and sets usability requirements, but the engineering team decides how it is securely implemented.

---

### 2. **Software Engineering (SWE)**

**Responsibilities:**
- Designs, implements, tests, and maintains software applications or services.
- Ensures code quality, adherence to standards, and maintainability.
- Participates in code reviews and knowledge sharing.

**Boundaries:**
- Software Engineers do not define product priorities or user requirements.
- Responsible for technical design, within constraints set by PMs and architects.
- May raise technical concerns that impact feasibility, but PMs arbitrate trade-offs.

**Rationale:**
Software Engineers focus on delivering robust, scalable, and maintainable solutions as specified by the requirements, maximising technical effectiveness without overstepping into product definition.

**Example:**  
The SWE team chooses the programming language and technical stack for a feature, ensuring performance and reliability without changing the product scope defined by the PM.

---

### 3. **Quality Assurance (QA)**

**Responsibilities:**
- Develops and maintains test plans, cases, and automated test suites.
- Validates application behaviour meets requirements.
- Reports defects with clear replication steps and severity ratings.

**Boundaries:**
- QA does not modify production code (except in dedicated test automation repos).
- Verification focuses on functional correctness and user acceptance criteria, not design choices.

**Rationale:**
QA acts as the last line of defence before release, ensuring that what is delivered matches both functional and quality expectations. Their external perspective is critical for objective assessment.

**Example:**  
QA reviews acceptance criteria set by the PM and tests the new feature accordingly, but does not make changes to the application’s implementation.

---

### 4. **DevOps/Site Reliability Engineering (SRE)**

**Responsibilities:**
- Designs, implements, and maintains deployment pipelines, infrastructure, and monitoring.
- Ensures operational reliability, scalability, and performance of services in production.
- Responds to incidents and drives root cause analysis and resolution.

**Boundaries:**
- SREs provide infrastructure and automation but do not build application features.
- May propose platform changes that affect application design, which require consultation with SWEs.

**Rationale:**
DevOps and SRE roles focus on enabling engineering teams to deploy and operate systems efficiently and safely, ensuring service continuity.

**Example:**  
SRE configures alerting for new services and maintains monitoring, while collaborating with SWEs to resolve operational issues detected post-release.

---

### 5. **User Experience (UX)/Design**

**Responsibilities:**
- Conducts user research and produces user flows, wireframes, and prototypes.
- Specifies design patterns, interaction models, and visual standards.
- Validates usability and accessibility.

**Boundaries:**
- UX does not develop or deploy code.
- Designs must align with both product constraints provided by PM and technical constraints from SWEs.

**Rationale:**
UX ensures solutions are usable and consistent, integrating stakeholder feedback and user insights while balancing feasibility.

**Example:**  
UX creates a prototype for a checkout flow. Engineers consult with UX if technical constraints necessitate design adjustments.

---

## Cross-Discipline Boundaries and Handoffs

Clear communication is essential at boundaries between disciplines. Typical hand-offs include:

- **Requirements (PM → SWE/UX):** Requirements are documented and clarified before development begins.
- **Design (UX → SWE):** Final designs are provided in sufficient detail, with open channels for clarifications.
- **Implementation (SWE ↔ SRE):** SWEs inform SREs of new service requirements; SREs feedback platform constraints early.
- **Testing (SWE → QA):** Once a feature is ready, code and documentation are handed to QA for validation.
- **Acceptance/Release (QA/PM):** QA verifies acceptance criteria; PMs sign off on releasability based on business priorities.

## Role Overlap and Escalation

Some overlap is inevitable, especially in smaller teams. When boundaries create conflict or ambiguity:

- First, escalate to leads from relevant functions for clarification.
- Document agreements for future reference.
- Where persistent overlap exists, advocate for re-defining roles or processes.

## Summary Table

| Role               | Owns What                                | Does Not Own | Key Hand-off Points     |
|--------------------|------------------------------------------|--------------|------------------------|
| Product Management | Product vision, priorities               | Technical design | Requirements to UX/SWE |
| Software Engineering | Technical implementation                | Product scope | Code/test artefacts to QA |
| Quality Assurance  | Testing, defect triage                   | Product/design decisions | Defect reports to SWE/PM |
| DevOps/SRE         | Infrastructure, CI/CD, monitoring        | App features  | Platform feedback to SWE |
| UX/Design          | User research, flows, prototypes         | Production code | Designs to SWE         |

---

## Conclusion

Each engineering discipline has distinct responsibilities and boundaries, all contributing to a cohesive, effective, and accountable technical organisation. Familiarity and respect for these boundaries are fundamental to high-performance engineering and the consistent delivery of quality outcomes. For any queries or unresolved role conflicts, contact your functional lead or the engineering management team.