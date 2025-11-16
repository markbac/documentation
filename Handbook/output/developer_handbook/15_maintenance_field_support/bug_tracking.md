# Bug Tracking

Effective bug tracking is essential for maintaining system reliability, supporting field operations, and ensuring timely resolution of defects. This page outlines the procedures for classifying, collecting evidence for, and triaging bugs. Adhering to these guidelines ensures predictability in support, transparency with stakeholders, and faster root-cause analysis.

---

## 1. Severity Policies

Severity categorisation determines the priority of remedial action. It ensures alignment across engineering, support, and customer-facing teams.

### Severity Levels

- **Critical (S1):**  
  System is down or a key function is unavailable; no viable workaround exists.  
  _Example:_ Data loss during normal operations.

- **High (S2):**  
  Major functionality is severely impaired or intermittent; a workaround exists but is not practical or reliable.  
  _Example:_ Payment processing occasionally fails for valid transactions.

- **Medium (S3):**  
  Partial loss of non-essential functionality, or an issue with a straightforward and effective workaround.  
  _Example:_ UI displays minor formatting errors, but core functions proceed.

- **Low (S4):**  
  Cosmetic issues or minor inconveniences that do not impede operations.  
  _Example:_ Typos in user messages, misaligned buttons.

#### Why It Matters

Consistent severity assignment:
- Aligns engineering priorities with business and customer impact.
- Reduces time wasted on debate and escalations.
- Enables accurate reporting on system reliability.

---

## 2. Evidence Collection

Robust evidence is necessary to reproduce and resolve bugs efficiently. Partial or unclear reports significantly slow resolution and lead to misclassification of issues.

### Required Evidence for a Bug Report

Every new bug must be documented with:

1. **Summary and Context:**  
   - Clear, concise description of the problem and its impact.
   - System version, environment (production, staging, etc.), and affected components.

2. **Steps to Reproduce:**  
   - Ordered list of exact actions needed to observe the bug.
   - Include data or user context if relevant.  
   _Example:_  
     1. Log in as user with role X.  
     2. Submit order for product Y.  
     3. Observe error on confirmation page.

3. **Expected vs. Actual Behaviour:**  
   - Explicitly state what should have happened and what actually occurred.

4. **Supporting Evidence:**  
   - Log files (with timestamps and anonymised sensitive information).
   - Screenshots, videos, or terminal output.
   - Network traces if applicable.
   - Error message(s), stack trace(s), and relevant configuration data.

5. **Frequency and Recurrence:**  
   - Is the issue always present or intermittent? State observed pattern.

### Common Pitfalls to Avoid

- Omitting environment details (e.g., "works on my machine" problems).
- Failing to distinguish root cause from symptoms (let logs inform theory, not vice versa).
- Excluding user context or failing to anonymise sensitive data.

#### Why It Matters

Comprehensive evidence:
- Minimises unnecessary back-and-forth.
- Allows immediate assignment and replication by development.
- Protects customer data privacy.
- Provides auditable history for post-mortem and reliability reporting.

---

## 3. Triage Process

Triage is the process of reviewing, prioritising, and routing new bugs to the appropriate team or individual. Consistent triage maintains support quality and transparency.

### Triage Workflow

1. **Initial Review:**  
   - Confirm completeness and clarity of bug report and evidence.
   - Assign or correct severity.

2. **Assignment:**  
   - Route to the appropriate engineering owner (feature/component lead).

3. **Label and Track:**  
   - Add relevant tags (e.g., “UI”, “backend”, “regression”).
   - Link to related incidents (if triggered by field report or monitoring).

4. **Communication:**  
   - Update reporter with status, especially if information is missing.
   - Notify stakeholders for Critical and High severity bugs.

5. **Ownership and Follow-Up:**  
   - Assigned owner is responsible for regular updates and progressing the fix or workaround.

### Escalation and Reassessment

- Bugs can move between severities if new evidence emerges.
- Escalation paths for Critical and High severity issues must be defined (see [Incident Management](./incident-management.md)).

#### Why It Matters

Structured triage:
- Ensures urgent issues are never overlooked.
- Facilitates transparent communication across teams.
- Reduces duplication and lost reports.
- Allows for metrics-based process improvement.

---

## 4. Example: End-to-End Bug Report

**Title:** "Cannot Submit Order from Mobile (S2)"  
**Summary:** On version 2.4.8, order submission fails for mobile users only. Error “502 Bad Gateway” is returned after tapping ‘Submit’.  
**Steps to Reproduce:**  
1. Use Chrome on Android (v13.1).  
2. Log in to account X.  
3. Add items to cart and tap ‘Submit’.  
**Expected:** Order confirmation page displays.  
**Actual:** “502 Bad Gateway” error appears.  
**Logs (attached):** show network timeout after POST to /api/checkout.  
**Frequency:** 100% on mobile, 0% on desktop.  
**Other notes:** Associated with release 2.4.8; started after push last night.

---

## Summary of Expectations

- Assign severity according to the documented scale — do not improvise.
- Collect and attach all relevant evidence, anonymising sensitive data.
- Rigorously follow the triage and assignment procedure.
- Communicate status and escalate per guidelines for higher severity issues.

Adherence to these practices reduces time to resolution, improves field support reliability, and enables data-driven improvements to our products and processes.