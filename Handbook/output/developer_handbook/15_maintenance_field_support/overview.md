# Maintenance and Field Support: Overview

## Introduction

This page outlines the structure and responsibilities of maintenance and field support within our engineering organisation. It explains support tiers, escalation flows, and delineates Level 2 (L2) and Level 3 (L3) support functions. Proper understanding and adherence to these processes are critical to maintaining service reliability, meeting contractual obligations, and ensuring rapid resolution of customer issues.

---

## Support Tiers

The support model is structured into three tiers, each with distinct roles and responsibilities.

### Level 1 (L1): First-Line Support

- **Scope**: Customer-facing teams or help desks handling routine queries, basic troubleshooting, and non-technical issues.
- **Examples of Activities**:
  - Password resets.
  - User guidance on application features.
  - Gathering preliminary incident data.
- **Expectation**: Prompt initial triage. Escalate technical or unresolved issues with appropriate diagnostic information.

### Level 2 (L2): Second-Line Support

- **Scope**: Specialised operational support, often handled by product or field engineers with in-depth system knowledge but not directly responsible for development.
- **Responsibilities**:
  - Technical troubleshooting and root cause identification for complex or persistent issues.
  - Remote diagnosis using logs, monitoring tools, or direct system interrogation.
  - Implementing approved configuration changes and hotfixes.
  - Providing workarounds to restore service where possible.
  - Preparing detailed incident reports and capturing lessons learned.
- **Expectation**: L2 should resolve all but the most complex issues or those requiring codebase changes. Escalate problems outside their remit to L3 with complete context.

### Level 3 (L3): Third-Line/Engineering Support

- **Scope**: Deep technical specialists (typically developers or architects) with code-level or architectural knowledge.
- **Responsibilities**:
  - Analysing incidents that originate from defects, complex integration issues, or architectural weaknesses.
  - Developing patches, fixes, or product modifications.
  - Advising on product limitations, unsupported scenarios, or required design changes.
- **Expectation**: L3 is a last-resort tier, intended only for issues beyond the capability of L1/L2. L3 intervention is typically expected to result in an engineering deliverable (code patch, design document, etc).

---

## Support Flows and Escalation

Clear escalation protocols ensure issues are addressed efficiently and responsibility is transparent at every stage.

### Escalation Flow

1. **Incident Received by L1**
   - L1 attempts resolution.
   - If unresolved or out of scope, escalates to L2 with all relevant information.

2. **L2 Diagnosis**
   - L2 investigates using system knowledge and operational tools.
   - L2 may involve additional data gathering or consultation with field technicians.
   - If L2 can resolve, incident is closed or returned with a documented solution.
   - If the issue is due to a product bug, code-level failure, or architectural constraint, escalate to L3.

3. **L3 Involvement**
   - L3 analyses, reproduces, and determines code or design fixes.
   - L3 communicates back solutions or required changes to L2 for field implementation.
   - In exceptional cases, L3 may interact directly with the field for critical, high-severity incidents, but always coordinates via L2.

### Rationale

Each tier ensures the right expertise is applied to the problem, avoids over-committing engineering resources, and supports clear communication to the customer. Proper logging and documentation at each step facilitate future root cause analysis and knowledge transfer.

---

## L2 and L3 Responsibilities: Detailed Guidance

### L2 Support: Guidance and Boundaries

- **When to Resolve**: Whenever the issue relates to configuration, deployment, known product limitations, customer environment, or non-code system issues.
- **Tools Used**: Monitoring dashboards, log aggregators, configuration panels, APIs for health/status checks.
- **Example**: L2 investigates a customer report of slow performance. Upon inspection, they find a misconfigured cache parameter and resolve the issue without escalation.

**Why this matters**: Effective L2 resolution reduces mean time to resolution (MTTR), minimises customer disruption, and allows engineering to focus on development rather than routine support.

### When to Escalate to L3

- **Indicators for Escalation**:
  - Evidence of product defect or bug (e.g., reproducible crash, data corruption).
  - Unsupported scenario or feature limitation unresolvable in the field.
  - Security vulnerability or data privacy risk.
- **Preparation**: L2 should gather precise logs, system states, step-by-step reproduction, and relevant environment data to prevent unnecessary back-and-forth.

**Example**: L2 finds a system repeatedly crashes when uploading a specific file type, with clear log errors pointing to application code. After confirming no configuration resolution is possible, issue is escalated with all supporting evidence.

---

## Practical Example: Escalation Flow

1. Customer submits a ticket reporting data synchronisation failures.
2. L1 collects basic details and verifies user is following standard procedures.
3. L1 escalates to L2 due to error messages seen in logs.
4. L2 uses diagnostics to determine data packet loss between regional nodes; applies configuration fix to optimise retries.
5. Issue persists; deeper log analysis reveals unhandled exception in synchronisation module.
6. L2 documents findings and escalates to L3 with complete logs and reproduction steps.
7. L3 identifies a concurrency bug, develops and tests a patch.
8. Patch is relayed back to L2 for deployment. L2 monitors system to confirm resolution.

---

## Summary of Expectations

- **L1**: Triage and resolve simple issues. Escalate when required.
- **L2**: Thoroughly investigate all operational/system issues, implement fixes, escalate to L3 only for confirmed product/development faults.
- **L3**: Apply engineering changes to resolve design or code faults, communicate actionable output.

**Key Principles**:

- Escalate only with thorough analysis and documentation.
- Minimise time spent at each tier; unblock the next level as quickly as possible.
- Maintain detailed records for all escalated incidents.

Following these guidelines ensures issues are resolved by the most appropriate team, maximising efficiency, service quality, and knowledge retention across the organisation.