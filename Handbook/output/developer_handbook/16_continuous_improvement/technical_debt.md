# Technical Debt

Technical debt refers to the implied cost of additional work caused by choosing an easy or limited solution now instead of a better, often more time-consuming approach. While the presence of technical debt is typical in engineering projects, its unmanaged accumulation severely impacts product quality, team velocity, and operational stability.

This page describes practical methods for cataloguing, budgeting, and remediating technical debt. Apply this guidance to ensure technical debt remains a controlled aspect of engineering, not an unchecked liability.

---

## 1. What Is Technical Debt?

Technical debt arises whenever we compromise the maintainability, extensibility, or reliability of software to meet short-term goals. While sometimes expedient, such decisions accrue "interest": over time, the cost of change increases, understanding declines, and risk grows. Typical sources include:

- **Incomplete or missing tests**
- **Outdated dependencies**
- **Duplicated or poorly structured code**
- **Unclear documentation**
- **Workarounds ("hacks") for missing features**
- **Shortcuts taken under time pressure**
- **Lack of automation (manual steps in delivery, testing, or deployment)**

**Example**:  
A team omits error handling to meet a release date, noting they will "add it later". Every future task that touches this code pays a penalty: added complexity, outages, and more time spent refactoring.

---

## 2. Why Catalogue Technical Debt?

Ignoring technical debt allows hidden issues to accumulate, reducing engineering efficiency and causing unpredictable failures. Cataloguing technical debt:

- **Makes it visible and actionable**: Hidden debt cannot be managed.
- **Informs planning and prioritisation**: Enables data-driven decisions about where to invest limited time.
- **Improves transparency**: Stakeholders understand both current state and long-term risks.
- **Reduces risk**: Known issues are less likely to cause unplanned outages.

---

## 3. How to Catalogue Technical Debt

### 3.1 Establish a Debt Register

Maintain a centralised, searchable list of known technical debts. This register should live alongside or within the team’s backlog (e.g., JIRA components, Confluence pages, GitHub issues).

**Each entry must include**:

- **Description**: What is the debt and how does it manifest?
- **Location**: System/class/module affected.
- **Impact**: How does it impede development, quality, or user experience?
- **Cause**: Why was the decision taken?
- **Risk Assessment**: Likelihood and consequence of leaving unaddressed.
- **Remediation Proposal**: Concrete steps to fix.
- **Estimate**: Effort required to address (in story points or hours).
- **Date Added** and **Review Cadence**: To ensure ongoing visibility.

**Example Register Entry**:

| Field         | Example                                                                           |
|---------------|-----------------------------------------------------------------------------------|
| Description   | API error handling is inconsistent between modules                                |
| Location      | `services/api/`                                                                   |
| Impact        | Causes unpredictable failures; complicates support; error logs are unclear        |
| Cause         | Initial release prioritised speed; exception handling was deferred                |
| Risk          | High: Customer incidents; debugging difficulty                                   |
| Proposal      | Refactor all API modules to use standard error handler; add missing test cases    |
| Estimate      | 4 days                                                                            |
| Date Added    | 2024-05-10                                                                        |
| Review        | Review in next technical debt triage                                              |

---

### 3.2 Identify Debt Proactively

Catalogue debt as part of:

- **Code reviews**: Note any shortcuts, anti-patterns, or code smells.
- **Retrospectives**: Reflect on past sprints/releases for accumulated debt.
- **Incident post-mortems**: Record any technical debt contributing to outages.
- **Regular audits**: Periodically review key systems for maintainability and quality.

---

## 4. Budgeting for Technical Debt

Unallocated work on technical debt will not occur; it must be planned and prioritised like feature work.

### 4.1 Set Clear Budget Policies

Define what proportion of team capacity will be spent addressing debt. Common models:

- **Fixed Percentage**: E.g., “Allocate 20% of sprint capacity to technical debt.”
- **Rotating Investment**: E.g., “Each sprint, select one high-priority debt issue to address.”
- **Policy-Based**: E.g., “Critical/security-related debt is addressed before all else.”

**Choose a model suitable for your team's context and product lifecycle.** 

### 4.2 Debt Remediation vs. Business Value

Balance must be struck between reducing debt and delivering user-facing value. Use data from the debt register (e.g., frequent pain points, customer incidents) to justify prioritisation to stakeholders.

**Example**:  
If a recurrent deployment failure traces to a legacy script with known technical debt, prioritise remediation over new feature delivery to prevent further disruption.

---

## 5. Remediating Technical Debt

### 5.1 Integrate Remediation into Development Workflow

- **Include debt items as explicit backlog work**: Assign owners, estimates, and clear definitions of done.
- **Don’t batch all debt together**: Smaller, discrete items are less likely to be postponed than one “big cleanup”.
- **Review progress in sprint reviews**: Celebrate reductions in the backlog; discuss blockers transparently.

### 5.2 Align Remediation with Related Feature Work

Whenever a feature touches an area of code with known debt, prefer to pay down local debt first. This avoids increasing debt by layering new code atop flawed foundations.

**Example**:  
Before adding new endpoints to an outdated REST API, refactor and test existing routes for consistency.

### 5.3 Track and Communicate Progress

- **Review debt items regularly**: Remove or reprioritise as context changes.
- **Publish metrics**: Share reduction in debt (count, estimated effort, or risk impact) quarterly or per sprint.
- **Maintain shared ownership**: Avoid “debt belongs to platform team” mentality; all engineers contribute.

---

## 6. Expectations and Responsibilities

- **All engineers**: Identify, document, and remediate technical debt as part of day-to-day work.
- **Tech leads/Engineering Managers**: Triage, prioritise, and ensure debt work receives scheduled capacity.
- **Stakeholders**: Informed of the necessity, risk, and ongoing progress of debt reduction.

---

## 7. Summary

Technical debt is not inherently negative, but unmanaged debt erodes productivity and trust. Proactively catalogue, budget for, and remediate technical debt as a standard engineering practice. Transparency and discipline in addressing debt ensure software remains maintainable, scalable, and robust as it evolves.