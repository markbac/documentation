# Collaboration Interfaces

This page defines the standards and practices for establishing clear, effective collaboration interfaces between organisational teams. Effective collaboration interfaces are crucial to support reliable handshakes, transparent input/output management, and robust dependency handling. Proper interface management minimises ambiguity, reduces delivery risk, and enables teams to act independently within well-defined boundaries.

---

## 1. Team Handshakes

### 1.1 Definition

A team handshake is a mutually understood agreement describing how two or more teams collaborate at defined boundaries. It formalises expectations on responsibilities, ownership, timing, and communication channels.

### 1.2 Why It Matters

- Reduces misunderstandings and duplicated effort.
- Makes gaps and overlaps in ownership visible.
- Facilitates onboarding and transition by documenting interfaces.
- Supports auditability and traceability of handover points.

### 1.3 Key Elements

A proper handshake must include:

- **Contacts**: Named individuals responsible for each side of the interface.
- **Scope**: The boundary of responsibilities; what is (and is not) included.
- **Communication protocol**: How teams communicate (e.g., regular standups, tickets, documentation updates).
- **Escalation path**: How to resolve disagreements or blockers.
- **Review cycle**: How frequently the handshake should be reviewed and updated.

#### Example: Backend & Frontend Team Handshake

- Contacts: Backend lead (A. Smith), Frontend lead (J. Jones)
- Scope: REST API endpoints v1.0 (backend provides, frontend consumes)
- Communication: Weekly alignment call; JIRA tickets for new requirements
- Escalation: Product owner mediation
- Review cycle: Quarterly, or after major release

---

## 2. Inputs and Outputs

### 2.1 Definition

Inputs and outputs specify what each team provides to, and expects from, others at defined interfaces. This encompasses not just data or code, but also artefacts such as documentation, test reports, or service level agreements (SLAs).

### 2.2 Why It Matters

- Prevents ambiguous or informal dependencies.
- Explicit contracts reduce integration failures.
- Clear expectations support autonomous development.

### 2.3 Documenting Inputs and Outputs

For each interface, document:

- **Input expectations**: Format, timing, frequency, and quality standards for all artefacts the team consumes.
- **Output promises**: Deliverables the team will provide, with timing, interfaces (APIs, files, reports), and exit criteria.
- **Versioning and change management**: How breaking changes are communicated and managed.

#### Example: Data Science and Data Engineering

- Inputs (Data Science): Curated, daily-updated dataset in agreed schema
- Outputs (Data Engineering): Automated data pipeline, test coverage reports, data quality metrics
- Versioning: Schema changes require minimum two-week notice + backward compatibility validation

---

## 3. Dependency Management

### 3.1 Definition

Dependency management is the proactive identification, documentation, coordination, and mitigation of delivery dependencies between teams.

### 3.2 Why It Matters

- Exposes blockers or bottlenecks early.
- Aligns roadmaps and reduces slippage caused by uncoordinated dependencies.
- Facilitates critical path tracking and enables contingency planning.

### 3.3 Managing Dependencies

#### Identification

- Catalogue all dependencies for each deliverable or milestone.
- Use dependency mapping tools or shared spreadsheets/visual boards.

#### Documentation

- Each dependency record must include: owner, dependent team, nature of dependency (input, resource, approval), due dates, and risk assessment.

#### Routine Checks

- Review dependencies at least fortnightly in cross-team syncs.
- Escalate unresolved or slipping dependencies per the escalation path in the handshake.

#### Risk Mitigation

- Use buffer time for critical dependencies.
- Propose and document fallback options where high risk is identified.

#### Example: Platform and Application Teams

- Dependency: Application team needs authentication APIs from Platform team by 1st September.
- Documentation: Dependency logged in shared tracker; both teams’ leads notified.
- Risk: API delivery at risk due to upstream refactoring – fallback is to use legacy API with feature limitation.

---

## 4. Expectations and Best Practices

- Explicitly define all collaboration interfaces in a living document accessible to all parties.
- Do not assume informal agreements suffice.
- Update interfaces when there are significant project, personnel, or scope changes.
- Keep lines of communication open, and escalate actively when needed.
- Encourage regular retrospective reviews to improve the interface over time.

---

By systematically defining and managing collaboration interfaces, teams ensure predictability, efficiency, and accountability. This approach fosters a culture of ownership and continuous improvement, reducing friction and supporting the timely, reliable delivery of organisational goals.