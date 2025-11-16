# Traceability Matrix

A traceability matrix is a structured document or spreadsheet that establishes a clear relationship between two or more sets of artefacts. Most commonly, it maps requirements to their corresponding design elements, implementation components, test cases, or verification results. The traceability matrix is a core part of effective systems engineering and is fundamental for demonstrating compliance, managing change, and ensuring coverage across the development lifecycle.

---

## 1. Purpose and Importance

**Why use a traceability matrix?**
- **Completeness**: Ensures all requirements have been addressed by design, implementation, and verification activities.  
- **Change Impact Analysis**: Allows teams to see the downstream impact of changing or removing a requirement.
- **Demonstrating Compliance**: Provides auditors and stakeholders with clear proof that requirements are fulfilled and verified.
- **Defect Tracking & Coverage**: Enables quick identification of gaps or duplications in test coverage or implementation.
- **Lifecycle Management**: Supports bi-directional tracking as requirements evolve, traceably linking to derived artefacts at each stage.

**In brief**: A well-maintained traceability matrix minimises risk, supports regulatory compliance, and helps teams deliver what is actually required.

---

## 2. How to Generate a Traceability Matrix

### 2.1 Identify Source and Target Artefacts

Determine which artefacts to trace:
- **Source**: Typically requirements (e.g., system requirements, user stories, standards clauses).
- **Target**: Could be lower-level requirements, architectural components, code modules, test cases, or verification results.

**Example**: Mapping System Requirements (source) to Test Cases (target).

### 2.2 Gather Artefact Identifiers

Ensure each artefact has a unique, stable identifier:
- Requirements: `REQ-001`, `REQ-002`
- Test Cases: `TC-001`, `TC-002`
Use consistent labelling conventions for easy reference and automation.

### 2.3 Construct the Matrix

Create a table where:
- Rows represent source artefacts.
- Columns represent target artefacts (or vice versa, depending on preference and tool support).
- Cells are marked (e.g., 'X', reference, or hyperlink) where a relationship exists.

**Example Table (Requirements to Test Cases):**

| Requirement ID | Requirement Description   | TC-001 | TC-002 | TC-003 |
|----------------|--------------------------|--------|--------|--------|
| REQ-001        | User logs in             | X      |        | X      |
| REQ-002        | Password reset function  |        | X      |        |
| REQ-003        | Audit trail              |        |        | X      |

> **Tip**: For large projects, generate the matrix using tooling (e.g., Requirements Management tools) rather than manual spreadsheets to avoid errors and maintain synchronisation.

### 2.4 Define Relationship Criteria

Before linking, define what constitutes a valid trace:
- Is it direct implementation/verification, or can it be indirect?
- Are partial fulfilments (e.g., multiple test cases for one requirement) marked differently?

Document these criteria for consistency.

---

## 3. Validating the Traceability Matrix

### 3.1 Completeness Checks

- **Forward Traceability**: Every requirement should link to at least one downstream artefact (e.g., test case, design document).
- **Backward Traceability**: Every downstream artefact (e.g., test case) should link to an upstream requirement.

### 3.2 Consistency and Accuracy

- Confirm that all links are correct and up-to-date.  
- Ensure changes in artefacts prompt updates in the matrix.

### 3.3 Gap and Orphan Analysis

- **Gaps**: Identify requirements with no associated targets (unimplemented).
- **Orphans**: Identify targets with no associated requirements (out of scope, or undocumented requirements).

### 3.4 Audit and Peer Review

- Schedule formal reviews of the matrix for correctness.
- Resolve ambiguities or errors found.

---

## 4. Publishing and Maintaining Traceability Artefacts

### 4.1 Publishing Expectations

- Generate and publish the traceability matrix as part of your project baseline or phase gate deliverables.
- Store it in an accessible location (e.g., project repository or central documentation tool) with version control.
- Clearly reference in summary and handover documents.

### 4.2 Ongoing Maintenance

- Update the matrix promptly as requirements, implementations, or test cases change.
- Use integrated toolchains or scripts to automate updates where feasible.
- Establish responsibility: assign a team member or role to own the artefact.

### 4.3 Communicating Traceability Status

- Summarise coverage and known gaps in project status reports.
- Alert relevant teams when incompleteness or discrepancies are detected.

---

## 5. Examples and Good Practice

### 5.1 Minimal Example (Markdown Table)

For a project with three requirements and two test cases:

| Requirement ID | Description                  | TC-01 | TC-02 |
|----------------|-----------------------------|-------|-------|
| REQ-01         | System boots in 2 seconds   | X     |       |
| REQ-02         | Supports multi-user login   |       | X     |
| REQ-03         | Exports data in CSV format  | X     | X     |

### 5.2 Automated Tool Output Example

Consider exporting relationships from a requirements tool (e.g., DOORS, Jama, Jira plugins) to CSV or direct HTML for traceability documentation.

---

## 6. Core Expectations

- Use a traceability matrix for all projects with formal requirements.
- Keep it current and accurate throughout the project lifecycle.
- Rigorously validate and review traceability artefacts before major releases or audits.
- Document any deliberate gaps (with clear rationale).
- Prefer automated generation and validation where available to reduce overhead and human error.

---

Clarity and rigour in traceability support robust engineering, reduce defects, and provide confidence to customers and regulators that all requirements have been adequately addressed and demonstrated.