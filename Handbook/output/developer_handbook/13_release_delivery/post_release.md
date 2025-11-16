# Post-Release: Hotfix Rules, Incident Handling, and L3 Support

This page details the process and expectations for handling issues discovered after a product release, with particular focus on hotfix creation, incident management, and Level 3 (L3) engineering support. Adhering to these procedures ensures a stable product, minimises customer impact, and maintains the integrity of releases.

---

## Hotfix Rules

### Definition

A **hotfix** is an expedited change intended to address critical defects or security vulnerabilities in a released system. Unlike regular releases, hotfixes are applied outside the standard development or release cycles.

### When to Create a Hotfix

Hotfixes should only be considered when:

- The defect directly affects production or key customer environments.
- There is no reasonable workaround.
- The issue is classified as Severity 1 (Critical) or Severity 2 (High).
- Waiting for the next planned release poses unacceptable risk.

**Example:**  
A major authentication failure after deployment preventing all users from logging in qualifies for a hotfix. A minor typo in a UI does not.

### Hotfix Process

1. **Assessment:**
   - Triage the defect with product and dev leads.
   - Confirm severity and impact. Clearly document justification for hotfix.
   - Verify reproducibility and collect diagnostic data.

2. **Branching:**
   - Create a hotfix branch from the relevant release tag (never from `main` or other in-flight branches).
   - Isolate unrelated changes to minimise regression risk.

   ```
   git checkout -b hotfix/2024-05-auth-failure release/2024.05.1
   ```

3. **Development and Testing:**
   - Make changes minimal and focused.
   - Write or adjust automated tests to cover the defect.
   - Manually validate the fix in a production-like environment.
   - Ensure no non-essential features or refactoring are included.

4. **Code Review:**
   - Submit a pull request to the hotfix branch.
   - Assign at least two reviewers—ideally including someone familiar with the release.
   - Review scope and ensure no unrelated code is present.

5. **Release and Deployment:**
   - Tag the hotfix branch with a unique, sequenced version (`2024.05.1-hotfix.1`).
   - Follow the standard deployment playbook, but include rollback steps if not already present.
   - Communicate with stakeholders (Support, Product, Customer Success).

6. **Merge Forward:**
   - After deployment, integrate the hotfix changes back into `main` and future release branches to prevent regression.

### Rationale

Limiting hotfixes to critical issues reduces risk and avoids fragmenting codebases. Non-essential changes increase the chance of unintended side effects during a sensitive window.

---

## Incident Handling

### Definition

An **incident** is any unplanned interruption or degradation of system service. Proper incident handling contains impact, restores service quickly, and drives systematic improvement.

### Incident Workflow

1. **Detection and Escalation:**
   - Incidents may arise from monitoring alerts, customer tickets, or internal users.
   - Declare an incident if criteria match S1 or S2 definitions in the [Incident Severity Matrix].

2. **Ownership:**
   - Assign an Incident Commander (IC). The IC coordinates communications and resources.
   - Designate a Lead Engineer for technical troubleshooting.

3. **Investigation and Communication:**
   - Begin with high-level diagnosis to confirm/deny impact.
   - Provide regular, concise updates in the incident channel or call (every 15–30 minutes).

4. **Resolution:**
   - Prioritise restoring service—even if via workaround—before root cause analysis.
   - Document temporary measures.

5. **Post-Incident:**
   - Complete a Post-Incident Review (PIR) within 48 hours.
   - Document root cause, timeline, user impact, and remediation.
   - File follow-up tasks for durable fixes or improvements.

### Example Workflow

- **Alert:** PagerDuty notifies on API latency spike.
- **Escalation:** SRE declares S1 incident, assigns IC.
- **Response:** Lead Engineer consults logs, identifies overloaded cache node, shifts traffic, restores performance.
- **Post-Incident:** PIR reveals misconfigured scaling threshold; action item to audit autoscaling settings.

### Rationale

Prompt, structured incident response limits customer harm and prevents repeat occurrences. Clear roles ensure efficient collaboration and accountability.

---

## L3 (Level 3) Support

### Definition

L3 Support is engineering-driven assistance for issues escalated by Support teams. L3 typically addresses novel, complex, or code-related problems that require engineering diagnosis or fixes.

### Responsibilities

- Investigate and resolve issues beyond the scope of L1/L2 support (e.g., deep code bugs, rare edge cases).
- Provide detailed root cause analyses.
- Create and deploy code fixes, patches, or configuration changes if needed.
- Liaise with Support and Product to ensure end-to-end communication.

### Engagement Practice

1. **Issue Escalation:**
   - L3 engagement follows unsuccessful L1/L2 triage or when an issue may require a code change.
   - All escalations must include:
     - Complete reproduction steps.
     - Logs, error messages, and environment details.
     - Severity assessment.

2. **Investigation:**
   - Validate the reported issue in a test/staging environment.
   - Reproduce using customer or anonymised data (never real user data in non-production).
   - Engage relevant engineers if domain expertise is needed.

3. **Outcomes:**
   - If a hotfix is required, trigger the [Hotfix Process](#hotfix-rules).
   - If the issue can wait, schedule it into the next planned development cycle.
   - Update the original ticket with findings, planned actions, and affected versions.

4. **Closure:**
   - Confirm solution in production, or ensure workaround communicated.
   - Mark the ticket as resolved only when deployment is confirmed.

### Rationale

Prompt L3 engagement reduces time-to-resolution for complex issues, supports Customer Success, and ensures transparency. Structured escalation flow eliminates confusion and redundant effort.

---

## Related Documentation

- [Incident Severity Matrix]
- [Release Branching Strategy]
- [Deployment Playbook]
- [Post-Incident Review Template]

---

**Note:** All engineers must ensure every post-release action is logged and transparent. Recurring themes found in hotfixes or incidents should feed into the team's continuous improvement process.

---

This guidance aims to make expectations clear and reproducible. For clarification, contact the Release Manager or Engineering Lead.