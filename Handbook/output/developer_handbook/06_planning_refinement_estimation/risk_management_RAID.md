# Risk Management (RAID)

Effective risk management is critical to the success of any engineering project. The RAID framework provides a structured approach to identifying, capturing, and managing *Risks*, *Assumptions*, *Issues*, and *Dependencies* throughout the project lifecycle. This section details the purpose, process, and best practices for RAID in engineering projects, enabling consistent and actionable management of uncertainties.

---

## Overview of RAID

RAID stands for:

- **Risks** – Potential events or conditions that could impact project objectives if they materialise.
- **Assumptions** – Statements taken as true for planning purposes, though they may not be fully validated.
- **Issues** – Current events or problems requiring resolution.
- **Dependencies** – Relationships or prerequisites involving resources, external teams, systems, or deliverables.

Tracking these elements systematically allows teams to anticipate challenges, coordinate activities, and make informed decisions, reducing the likelihood and impact of negative outcomes.

---

## Why RAID Matters

Thorough RAID management:

- Prevents avoidable delays and failures by increasing transparency.
- Enables proactive rather than reactive responses.
- Facilitates collaboration and responsibility across teams.
- Provides evidence-based updates and status reports for stakeholders.

Neglecting RAID increases project risk, resulting in missed deadlines, unexpected costs, compromised quality, and dissatisfied stakeholders.

---

## How to Apply RAID

### 1. Identification

Regularly identify new Risks, Assumptions, Issues, and Dependencies:

- During project planning, refinement sessions, or retrospectives.
- When new information becomes available or project parameters change.
- Through structured brainstorming, stakeholder interviews, and review of project documentation.

**Example:**  
While scoping a payment integration, the team notes a third-party API will be used that is still in beta. This is both a dependency (on the API’s availability) and a risk (potential instability).

### 2. Documentation

Capture each RAID item in a central, accessible RAID log (e.g., a table or spreadsheet in your team’s project workspace).

For each item, record the following (as relevant):

- **ID/Reference**
- **Description**: Clear, concise statement.
- **Type**: Risk, Assumption, Issue, or Dependency.
- **Owner**: Individual responsible for monitoring or action.
- **Impact**: Description or rating (e.g., high/medium/low).
- **Probability** (Risks): Likelihood of occurring.
- **Status**: Open, mitigated, resolved, etc.
- **Actions**: Steps to resolve, mitigate, or validate.
- **Due Date/Review Date**

**Example RAID Entry:**

| ID   | Type   | Description                                  | Owner   | Impact | Probability | Status  | Actions                         |
|------|--------|----------------------------------------------|---------|--------|-------------|---------|---------------------------------|
| R001 | Risk   | API downtime may disrupt payment processing  | R. Singh| High   | Medium      | Open    | Identify fallback, monitor API  |

### 3. Assessment and Prioritisation

Assess each item for likelihood (where relevant) and potential impact. Use this assessment to:

- Prioritise high-impact/high-likelihood risks and urgent issues.
- Sequence work to address critical dependencies early.
- Focus validation efforts on key assumptions.

**Example:**  
If a third-party system integration is a dependency for multiple deliverables, prioritise early engagement and testing with that system to reduce compounded risk.

### 4. Mitigation and Action

For each item:

- **Risks:** Develop and implement mitigation or contingency plans. Assign clear owners.
- **Assumptions:** Plan validation or revisit as the project evolves; avoid building critical paths on untested assumptions.
- **Issues:** Investigate promptly and resolve or escalate as needed.
- **Dependencies:** Confirm readiness, schedule integration points, and communicate externally as necessary.

**Practical Actions:**
- Schedule a technical spike to validate an assumption about data migration feasibility.
- Engage with an external vendor to formalise delivery dates for a dependent library.

### 5. Ongoing Review

- Update the RAID log at least every sprint or major milestone.
- Review RAID items in team meetings or stand-ups.
- Communicate significant changes to stakeholders.
- Close or archive resolved items, retaining them for post-mortem analysis.

---

## Best Practices

- **Keep the RAID log lean:** Prioritise items that materially affect outcomes; avoid cluttering with trivial notes.
- **Ensure clear ownership:** Each item must have a responsible person.
- **Promote visibility:** RAID logs should be accessible; update status and outcomes clearly, not just initially.
- **Integrate into workflows:** Make RAID review a standard agenda item in planning and retrospectives.
- **Distinguish clearly:** Avoid conflating risks (potential) with issues (current); do not treat unvalidated assumptions as confirmed facts.

---

## Common Pitfalls

- **RAID as a checkbox exercise:** Creating logs but not actioning or reviewing them.
- **Failure to challenge assumptions:** Proceeding without validation can lead to missed risks or hidden dependencies.
- **Unassigned actions:** Items without owners or deadlines rarely progress.
- **Poor communication:** Not escalating significant risks or dependencies in time.

---

## Summary

Systematic RAID management underpins successful project delivery by making uncertainties visible and actionable. Use the RAID log as a living document. Review and update it regularly, assign ownership, and embed RAID practice into day-to-day engineering processes. This ensures informed, proactive management of risks, assumptions, issues, and dependencies throughout the project lifecycle.