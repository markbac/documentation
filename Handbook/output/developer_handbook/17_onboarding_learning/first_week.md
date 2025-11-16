# First Week

**Objective**: This page provides clear, actionable guidance for engineers during their first week, ensuring effective onboarding and rapid progress towards productivity.

---

## Overview

The first week is critical for establishing a foundation for your success. Rapid familiarisation with tools, processes, and the team will minimise onboarding friction and maximise your early contributions. This guide outlines essential activities, explains their purpose, and offers practical steps and examples where relevant.

---

## Day 1: Setup and Orientation

### Workstation and Account Provisioning

**What to do**:  
- Collect your assigned hardware and confirm its specifications match your requirements.
- Complete device setup as per the [Device Setup Guide].
- Ensure access to necessary internal systems by confirming logins for:
  - Email
  - Chat (e.g., Slack, Teams)
  - Company Wiki/Documentation
  - Version Control (e.g., GitHub, GitLab)
  - CI/CD systems
  - Issue Tracker (e.g., Jira)

**Why it matters**:  
Prompt and correct setup prevents delays when engaging with your team and systems. Early resolution of access issues avoids bottlenecks later in onboarding.

### Introductions and Expectations

**What to do**:  
- Attend a welcome briefing with your team lead or manager.
- Receive an overview of team responsibilities, current projects, and immediate expectations.
- Introduce yourself on relevant chat channels and stand-ups.

**Why it matters**:  
Early context aids understanding of priorities and communication norms. Building initial relationships accelerates knowledge transfer and trust.

---

## Days 2–3: Environment Familiarisation

### Codebase Access and Local Setup

**What to do**:  
- Clone the main repositories associated with your team.
- Follow the environment setup instructions ([see: Local Development Setup]).
- Run the full test suite to ensure your environment mirrors CI.

**Why it matters**:  
Verifying local parity with production and CI/CD environments prevents subtle bugs and improves efficiency. Early troubleshooting is best handled before active feature work begins.

**Example**:  
If working on a Python microservice, ensure the same Python version and dependencies are installed (`python --version`, `pip freeze`). Run tests using the prescribed command, e.g., `pytest`.

### Process Documentation Review

**What to do**:  
- Read current engineering processes, including coding standards, pull request workflows, and deployment procedures.
- Mark any points of confusion to clarify with your onboarding buddy or team lead.

**Why it matters**:  
Understanding these processes reduces errors, avoids rework, and ensures consistency across the engineering team.

### Team and Project Context

**What to do**:  
- Review the architecture overview and any high-level design documentation.
- Examine the current and recent issues/merge requests in the tracker to observe workflow patterns.
- Attend or watch the most recent relevant sprint planning or demos.

**Why it matters**:  
Early exposure to both technical and process context clarifies how your contributions fit into broader team goals.

---

## Days 4–5: Hands-On Contributions

### First Task Selection

**What to do**:  
- With your lead or onboarding buddy, select a straightforward, well-contained task (e.g., minor bug fix, documentation improvement).
- Confirm acceptance criteria and delivery expectations.

**Why it matters**:  
An immediate, achievable contribution builds confidence and verifies your system access and understanding of workflow.

### Implementing and Submitting Your First Change

**What to do**:  
- Create a feature branch using the standard naming conventions.
- Implement the change, keeping commits small and well-documented.
- Create a pull/merge request, following the team's template and guidelines.
- Actively seek feedback, promptly address review comments, and merge upon approval.

**Why it matters**:  
This process validates your understanding of the development, review, and deployment process. It also introduces you to your team's feedback and collaboration culture.

**Example**:  
Suppose you are assigned a documentation typo fix.  
1. Create a branch: `git checkout -b docs/fix-typo-readme`
2. Make the correction.
3. Commit with a clear message: `git commit -m "docs: fix typo in README"`
4. Push and open a merge request, filling out the PR template.
5. Respond to reviewer feedback and merge after approval.

---

## End of First Week: Review and Next Steps

### Structured Check-In

**What to do**:  
- Attend a one-on-one with your lead or onboarding buddy.
- Review your experiences: what went smoothly, what required clarification, and any blockers encountered.
- Confirm understanding of next steps and identify areas for further learning or contribution.

**Why it matters**:  
Regular feedback mechanisms ensure any gaps are addressed early, setting the stage for ongoing development.

---

## Summary Checklist

- [ ] Device and accounts set up with confirmed access.
- [ ] Tools and codebase running locally; tests pass.
- [ ] Read and understood core engineering processes.
- [ ] Engaged with team; attended relevant meetings.
- [ ] Completed and merged your first small contribution.
- [ ] Held a feedback session to clarify next steps.

---

## Supporting Resources

If any process is unclear, consult:
- Assigned onboarding buddy or team lead
- [Engineering Handbook main page]
- [Team documentation index]

---

**Effective onboarding in the first week provides the momentum for all future contributions. Follow the outlined steps to become productive with confidence and clarity.**