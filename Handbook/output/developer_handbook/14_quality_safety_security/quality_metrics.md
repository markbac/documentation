# Quality Metrics

This page defines the essential metrics for measuring and improving the quality, safety, and security of our engineering outputs. Emphasis is placed on DORA metrics, defect density, and mean time between failure (MTBF) surrogates. Understanding and consistently applying these metrics ensures that engineering teams deliver reliable, maintainable, and secure software.

---

## Table of Contents

- [Overview](#overview)
- [DORA Metrics](#dora-metrics)
  - [Deployment Frequency](#deployment-frequency)
  - [Lead Time for Changes](#lead-time-for-changes)
  - [Change Failure Rate](#change-failure-rate)
  - [Time to Restore Service](#time-to-restore-service)
- [Defect Density](#defect-density)
  - [Calculation](#calculation)
  - [Application](#application)
- [MTBF Surrogates](#mtbf-surrogates)
  - [Definition and Relevance](#definition-and-relevance)
  - [Typical Surrogate Metrics](#typical-surrogate-metrics)
- [Expectations and Best Practices](#expectations-and-best-practices)

---

## Overview

Robust measurement is foundational to software quality. Well-defined metrics allow teams to:

- Detect trends and regressions in quality or delivery capability.
- Identify bottlenecks and root causes.
- Set explicit improvement goals.
- Communicate quality status both internally and externally.

This page prescribes a focused set of actionable metrics. Each is explained with calculation guidance, rationale, and typical use.

---

## DORA Metrics

DORA (DevOps Research and Assessment) metrics are a proven set of indicators for software delivery performance. They are widely adopted in modern engineering practices and provide actionable insights into both velocity and stability.

### Deployment Frequency

**Definition:**  
The number of deployments to production (or equivalent environments) per unit of time, typically measured per day or week.

**Why it matters:**  
Higher deployment frequency indicates a team's ability to deliver value quickly, respond to change, and reduce batch size. It signals both agility and confidence in the deployment process.

**How to measure:**  
Count the number of successful, user-impacting deployments completed in a given measurement period.

> **Example**: If your service is deployed to production 10 times in a week, your weekly deployment frequency is 10.

**Best Practice:**  
Automate deployment tracking via CI/CD tooling. Ensure what constitutes a "deployment" is clearly documented per team/product.

---

### Lead Time for Changes

**Definition:**  
The elapsed time from code committed to running successfully in production.

**Why it matters:**  
Shorter lead times reduce the gap between development and customer impact, decrease risk, and improve responsiveness to problems or opportunities.

**How to measure:**  
- Record the timestamp when code is committed (e.g., merged to mainline/main branch).
- Record the timestamp when the same code is deployed and live in production.
- The difference is the lead time for each change.
- Aggregate (often using the median) for the measurement period.

> **Example**: If you commit a feature at 10:00 on Monday and it is deployed at 14:00 on Tuesday, the lead time for that change is 1 day and 4 hours.

**Best Practice:**  
Where possible, automate timestamps in version control and deployment logs. Report typical lead times (e.g., median, 90th percentile).

---

### Change Failure Rate

**Definition:**  
The proportion of deployments that cause a production failure, degradation, or require urgent remediation (e.g., rollback, patch).

**Why it matters:**  
This measures the stability and quality of changes. A high rate indicates insufficient testing, change management, or risky deployment practices.

**How to measure:**  
- Count the number of production deployments in a period.
- Count how many of these deployments resulted in failure or required immediate remediation.
- Divide the number of failed deployments by the total deployments; express as a percentage.

> **Example**: Out of 20 deployments, if 2 required rollback due to errors, the change failure rate is 10%.

**Best Practice:**  
Define what constitutes a "failure" (typically includes outages, degradations, and urgent fixes). Avoid counting minor, non-urgent bugs.

---

### Time to Restore Service

**Definition:**  
The time required to restore service during an unplanned outage or critical impairment.

**Why it matters:**  
This reflects organisational ability to respond and recover from failures, thereby reducing user impact and reputational risk.

**How to measure:**  
- Record the time between detection of a failure and full restoration of the affected service.
- Aggregate as a median or 90th percentile over a measurement interval.

> **Example**: If an incident starts at 09:43 and service is restored at 10:58, the time to restore is 1 hour 15 minutes.

**Best Practice:**  
Automate incident start and end time collection where feasible. Review outlier events to drive learning and process improvement.

---

## Defect Density

Defect density measures the number of confirmed defects relative to the size of the codebase, helping teams track overall quality and spot problematic areas.

### Calculation

**Defect Density = Number of Confirmed Defects / KLOC (thousand lines of code)**

- **Confirmed defects**: Issues verified as actual bugs post-release or in-system integration/test.
- **KLOC**: Thousand lines of code, typically measured excluding generated or third-party code.

> **Example**:  
> - 50 post-release bugs in a codebase of 100 KLOC.  
> - Defect density = 50 / 100 = **0.5 defects per KLOC**.

**Note:**  
KLOC is a blunt instrument and may not reflect complexity, so always supplement with qualitative analysis.

### Application

- **Trend monitoring**: Use to track quality across releases or components.
- **Target setting**: Establish context-appropriate thresholds based on system criticality.
- **Component comparison**: Identify modules with unusually high defect concentrations.

**Best Practice:**  
Log all post-release bugs in a visible tracking system. Calculate defect density regularly; review high-density areas.

---

## MTBF Surrogates

MTBF (Mean Time Between Failures) is a classic reliability measure but is often impractical for software systems. Instead, use surrogate metrics that reliably indicate operational robustness.

### Definition and Relevance

**MTBF** quantifies the average operational time between one system outage and the next. For software, “failures” are more complex, often spanning application errors, service outages, or critical degradations.

Surrogate metrics decouple the principle (maximise time between failures) from impractical direct measurements. They focus on observable indicators of reliability.

### Typical Surrogate Metrics

- **Incidents per time period:** Track the number of significant incidents (e.g., Severity 1 and 2) per week or month.
- **Mean time between incidents:** Aggregate time between detected and resolved incidents.
- **Availability/Uptime (%):** Express system reliability as a percentage over a fixed period (e.g., "99.95% uptime last quarter").

> **Example:**  
> If a service experienced 2 critical incidents in March, and total uptime was 744 hours (total hours in March),  
> - Mean time between incidents = 744 / 2 = **372 hours**
> - Uptime reported as 99.7% if downtime totalled 2 hours during the period.

**Best Practice:**  
- Define incident severity ratings with clear, objective criteria.
- Automate incident logging where possible.
- Track and report trends, not just point-in-time numbers.

---

## Expectations and Best Practices

- **Track Core Metrics:** All product teams must report DORA metrics, defect density, and a suitable reliability surrogate.
- **Automate Collection:** Integration with CI/CD, version control, and incident management systems is the standard for accuracy and consistency.
- **Regular Review:** Review metrics at least monthly to catch regressions and verify improvement efforts.
- **Data Integrity:** Use clear definitions for all metrics and ensure consistent measurement methodologies across teams.
- **Response:** Investigate significant negative trends promptly, treating metrics as an input to retrospectives and quality improvement.

---

_Maintaining high quality, safety, and security depends on disciplined tracking of these metrics and acting on the insights they provide. Direct questions or requests for guidance to your quality lead or engineering manager._