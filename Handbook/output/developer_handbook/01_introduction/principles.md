# Core Principles

This page describes the core engineering principles that underpin our work. These principles define the standards we adhere to as an organisation, guide our decision-making, and ensure that our engineering outcomes are robust, traceable, and deliver incremental value. They are applicable to all engineers, regardless of domain or seniority.

---

## Reliability

**What:**  
Reliability means designing and operating systems, processes, and code so they function correctly, predictably, and continuously meet their intended purpose with minimal failure or downtime.

**Why it matters:**  
Reliable systems minimise business disruption, ensure customer trust, and reduce costs associated with unscheduled maintenance and incident response.

**How to achieve it:**
- **Explicit error handling:** Always check for and handle potential failure modes. For example, when reading from an external API, check for timeouts, retries, and graceful degradation.
- **Automated testing:** Implement comprehensive automated tests (unit, integration, end-to-end) to catch regressions before deployment.
- **Monitoring and alerting:** Instrument systems with clear, actionable monitoring. Set up alerts to detect anomalies before they escalate.
- **Progressive delivery:** Use staged rollouts or canary deployments to limit the blast radius of unforeseen failures.
- **Documentation:** Document assumptions, dependencies, and known failure points so that future maintainers understand system risks.

**Example:**  
If designing a payment processing system, reliability demands that every transaction is either fully completed or rolled back, with clear logs and notifications in the event of failure.

---

## Traceability

**What:**  
Traceability is the ability to trace each piece of work, code change, or operational decision back to its origin—whether that is a business requirement, bug report, or security incident. This encompasses source control, documentation, record-keeping, and audit trails.

**Why it matters:**  
Traceability improves accountability, eases auditing, accelerates debugging, and enables regulatory compliance. It allows any engineer to understand the provenance and rationale for decisions, reducing guesswork when investigating issues or reviewing code.

**How to achieve it:**
- **Source control discipline:** Ensure all code is committed to version control, with descriptive commit messages that reference relevant tickets or context.
- **Linking changes to requirements:** Use ticketing systems to document why changes are being made and link them to code reviews and deployments.
- **Audit trails:** Log significant operational actions (such as configuration changes or database migrations) with timestamps and responsible users.
- **Documentation updates:** Keep documentation current with system changes, including rationales for non-obvious decisions.

**Example:**  
If a bug is reported by a customer, an engineer should be able to quickly find the original requirement, the code that implemented it, the ticket tracking the bug fix, and the deployment note that released the fix.

---

## Incremental Delivery

**What:**  
Incremental delivery means breaking work down into small, independently valuable units that are delivered frequently. Each increment should be functional and, where possible, releasable to users.

**Why it matters:**  
Delivering in increments reduces risk, speeds up feedback loops, and ensures the team can respond quickly to changing requirements or customer feedback. Large, monolithic releases increase the chance of failure and slow learning.

**How to achieve it:**
- **Thin slicing:** Break features into the smallest deployable units that deliver value or learning. For instance, release a backend API before the full user interface is ready.
- **Continuous integration:** Integrate and test changes frequently to identify conflicts or regressions early.
- **Frequent releases:** Favour multiple small releases over fewer large releases to make troubleshooting easier and revert failures with minimal impact.
- **Feedback and iteration:** Actively solicit user or stakeholder feedback on each increment, and prioritise fixes and improvements based on real usage.
- **Feature toggles:** Isolate incomplete or risky features via feature flags to enable safe deployment without exposing unfinished work to users.

**Example:**  
When introducing a new user profile section, start with read-only profile viewing, deploy it, gather feedback, then follow up with profile editing in a separate release.

---

## Summary

Reliability, traceability, and incremental delivery form the foundation of our engineering culture. Each principle supports robust, maintainable, and valuable systems. Engineers are expected to understand and apply these principles in daily work, seek clarification when unsure, and uphold them as the default way we deliver value and ensure excellence.