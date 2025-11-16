# Traceability

Traceability is the practice of systematically tracking requirements, features, and user stories throughout the project lifecycle. Effective traceability enables teams to demonstrate that all requirements are addressed, changes are managed, and impacts are understood. This is critical for maintaining quality, consistency, and regulatory compliance in engineering projects.

---

## 1. Purpose of Traceability

The primary objectives of traceability are:

- **Verification**: Confirming that each requirement is implemented and tested.
- **Impact Analysis**: Assessing implications of changes to requirements or features before implementation.
- **Compliance**: Demonstrating fulfilment of regulatory, legal, or contractual obligations.
- **Transparency**: Providing clear visibility into progress, coverage, and gaps.

Without robust traceability, projects are susceptible to missed requirements, redundant efforts, uncontrolled change, and audit failures.

---

## 2. Key Traceability Artefacts

Traceability typically involves:

- **Requirements**: Functional, non-functional, and regulatory statements specifying what the system must do.
- **Features/User Stories**: Breakdown of requirements into deliverable increments.
- **Designs**: Architectural and detailed design elements derived from requirements.
- **Test Cases**: Verification steps associated with requirements and features.
- **Change Requests & Defects**: Modifications or findings linked back to original requirements.

---

## 3. Traceability Matrices

A **traceability matrix** is a tabular mapping showing the relationships between two or more artefact types (such as requirements and test cases).

### 3.1 Types of Matrices

- **Forward Traceability**: Links requirements → features → test cases (ensuring every requirement is implemented and tested).
- **Backward Traceability**: Links test cases → features → requirements (ensuring every implementation item can be justified by a requirement).
- **Bidirectional Traceability**: Combines both, allowing navigation in either direction.

### 3.2 Structure Example

| Requirement ID | User Story IDs | Design Ref | Test Case IDs   |
|----------------|---------------|------------|-----------------|
| REQ-001        | US-01, US-02  | DS-03      | TC-01, TC-05    |
| REQ-002        | US-03         | DS-01      | TC-03           |

**Best Practice:** Maintain this linkage in a central repository (e.g., Jira, DOORS, spreadsheet) with unique, persistent IDs for each artefact.

---

## 4. Cross-Referencing Rules

### 4.1 Establish Unique Identifiers

Assign every artefact (requirement, story, design, test case) a unique, immutable ID. IDs are essential for effective referencing and consistent updating across artefacts and tools.

### 4.2 Explicit Linking

Whenever a new artefact is created (e.g., a user story derived from a requirement), explicitly record the source and destination IDs in both artefacts. Where tools support automatic linkage, always verify the integrity of connections.

### 4.3 Trace Consistently

Apply the same cross-referencing conventions throughout the project. This includes:

- Using consistent field names for references.
- Recording links at every decomposition (requirement → story, story → design, etc.).
- Confirming links are updated whenever artefacts are changed, split, or merged.

### 4.4 Coverage Verification

Regularly audit matrices to ensure:

- Every requirement traces to at least one design, implementation item, and test case.
- Every feature, user story, or change request traces back to a requirement.
- No orphaned artefacts (items with no traceable link).

---

## 5. Practical Example

Suppose REQ-1005 specifies "The system must log all login attempts." The trace might be constructed as follows:

- **Requirement**: REQ-1005 ("log login attempts").
- **User Stories**: US-201 ("capture successful logins"), US-202 ("capture failed logins"), both referencing REQ-1005.
- **Design Element**: DS-303 ("audit log subsystem"), referenced by US-201 and US-202.
- **Test Cases**: TC-411 ("test successful login logging"), TC-412 ("test failed login logging"), each referencing both the user story and the original requirement.

This structure enables:

- Proving to auditors that REQ-1005 is fully implemented and tested.
- Assessing the impact if REQ-1005 changes (quickly identifying all related stories, designs, and test cases).
  
---

## 6. Expectations and Maintenance

- **Authoring**: When creating any artefact, establish traces to all relevant upstream and downstream items.
- **Updating**: When modifying, splitting, or deprecating artefacts, update the traceability records accordingly.
- **Review**: Before major milestones or releases, review and reconcile all traceability links and matrices.
- **Tooling**: Use supported project management or requirements tools where possible to automate linkage and reporting.
- **Documentation**: Ensure traceability matrices and linkages are kept current and included in your project documentation deliverables.

---

## 7. Summary Checklist

- [ ] Assign unique IDs to all requirements, features, and test cases.
- [ ] Create and maintain traceability matrices linking all relevant artefacts.
- [ ] Explicitly cross-reference artefacts at every decomposition or implementation level.
- [ ] Regularly verify coverage and completeness of all trace links.
- [ ] Update traces promptly after any change to artefacts.

---

Establishing and maintaining robust traceability is essential for sound engineering practice. When rigorously applied, it safeguards quality, manages risk, and enables confidence in both the engineering process and the delivered system.