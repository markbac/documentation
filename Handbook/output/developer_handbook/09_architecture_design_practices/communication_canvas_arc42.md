# Architecture Communication Canvas (arc42)

## Overview

The arc42 Architecture Communication Canvas is a lightweight, structured tool for documenting and discussing software architecture. It supports clear, systematic architectural thinking by prompting teams to consider and capture key architectural decisions and context. The canvas format encourages brevity and focus, aligning stakeholders on core architectural concerns without unnecessary detail.

arc42 is based on established best practices in software architecture and is widely adopted across industries. The canvas is particularly valuable during initial architecture workshops, design reviews, or when onboarding new team members.

---

## Why Use the arc42 Canvas?

- **Clarity and Focus:** condenses complex architectural topics into clear, manageable segments.
- **Stakeholder Alignment:** ensures all stakeholders have a shared understanding of architectural intent and priorities.
- **Documentation Discipline:** prompts teams to address critical aspects (e.g., constraints, quality goals) that are often overlooked.
- **Change Readiness:** provides a single-page reference for future adaptations or onboarding, reducing knowledge loss.

Without sufficient structure, architectural discussions can become unfocused, leading to misunderstandings and technical debt. The arc42 canvas provides that structure and ensures completeness.

---

## Structure of the arc42 Canvas

The canvas consists of the following key sections:

1. **Solution Context**
2. **Requirements**
3. **System Scope**
4. **Key Quality Goals**
5. **Stakeholders**
6. **Constraints**
7. **Architecture Strategy**
8. **Key Building Blocks**
9. **Risks and Technical Debt**
10. **Open Issues**

Each section serves a specific purpose in delivering a complete architectural overview.

---

## How to Use the Canvas: Step-by-Step Guidance

### 1. Solution Context

**What:**  
Describe the environment in which the system will operate. Identify external systems, users, or processes interacting with your solution.

**Why:**  
Understanding context prevents costly interface or integration oversights.

**How:**  
- Briefly list or diagram major external dependencies.
- Example: _"Integrates with the company's authentication service and receives data from the payment gateway."_

---

### 2. Requirements

**What:**  
Summarise the system’s fundamental functional requirements or use cases at a high level.

**Why:**  
Aligns the architecture with business needs and ensures irrelevant features are scoped out.

**How:**  
- Focus on major goals, not implementation detail.
- Example: _"Users can generate custom reports and export them as PDFs."_

---

### 3. System Scope

**What:**  
Define system boundaries—what is part of your system and what is not.

**Why:**  
Prevents ambiguity around responsibility and integration points.

**How:**  
- Explicitly mention inclusions and exclusions.
- Example: _"Handles data storage but does not include analytics dashboard (covered by BI team)."_

---

### 4. Key Quality Goals

**What:**  
State the most important quality attributes (e.g., reliability, performance, scalability).

**Why:**  
Quality goals drive architectural trade-offs and technology choices.

**How:**  
- Limit to 2–5 priorities.
- Example: _"System must support 99.99% availability and process transactions in under 2 seconds."_

---

### 5. Stakeholders

**What:**  
Identify key stakeholders and their roles.

**Why:**  
Addresses differing stakeholder expectations and communication needs.

**How:**  
- List roles, not just names.
- Example: _"Product Owner: defines priorities. Ops Team: maintains uptime."_  

---

### 6. Constraints

**What:**  
Document hard limitations or mandates (e.g., legal, technical, organisational).

**Why:**  
Constraints can fundamentally affect design decisions and feasibility.

**How:**  
- Capture only concrete, non-negotiable items.
- Example: _"Must use PostgreSQL due to enterprise license agreements."_

---

### 7. Architecture Strategy

**What:**  
Outline fundamental solution approaches (e.g., major patterns, integration styles).

**Why:**  
Clarifies rationale behind the overall architecture, aiding justification and critique.

**How:**  
- Briefly describe chosen strategies and alternatives considered (if any).
- Example: _"Event-driven microservices pattern to support future scaling requirements."_

---

### 8. Key Building Blocks

**What:**  
Summarise the major components and their responsibilities.

**Why:**  
Gives a high-level “map” for anyone new to the system.

**How:**  
- Use a list or a simple block diagram.
- Example: _"Web API, Data Processing Worker, Notification Service."_

---

### 9. Risks and Technical Debt

**What:**  
Identify known risks or areas of technical debt.

**Why:**  
Proactively highlights potential problem areas requiring mitigation or tracking.

**How:**  
- Include both current issues and foreseeable risks.
- Example: _"Legacy service integration may increase maintenance overhead."_

---

### 10. Open Issues

**What:**  
Track unresolved decisions, questions, or areas needing clarification.

**Why:**  
Enables transparent decision-making and clear follow-ups.

**How:**  
- Keep a living issues list as the architecture evolves.
- Example: _"Pending decision on log management solution."_

---

## Practical Example: Canvas Excerpt

| Section            | Example Entry                                        |
|--------------------|-----------------------------------------------------|
| Solution Context   | Interfaces with Auth0 and Stripe APIs                |
| Requirements       | Users manage subscriptions and payment methods       |
| System Scope       | Handles billing, excludes email notifications       |
| Key Quality Goals  | High availability, data security                    |
| Stakeholders       | Product Manager, SRE, End Users                     |
| Constraints        | Must deploy to GCP                                  |
| Architecture Strategy | Microservices with asynchronous communication   |
| Key Building Blocks| API Gateway, Billing Service, DB, Messaging Queue   |
| Risks/Tech Debt    | Insufficient test automation                        |
| Open Issues        | Finalise SSO provider                               |

---

## Application and Expectations

- **Be concise:** Each section is typically completed in 1–3 sentences or bullet points.
- **Collaborate:** Fill in the canvas collaboratively with engineers, product owners, and relevant stakeholders.
- **Update regularly:** Maintain as a living document—revisit after major architectural changes or when onboarding new team members.

---

## Summary

The arc42 Architecture Communication Canvas provides a robust yet lightweight framework for architectural clarity. By methodically addressing each section, teams ensure they have considered vital architectural aspects, documented their rationale, and are positioned to communicate effectively with all stakeholders. Use the canvas as a standard starting point for both new designs and ongoing architectural reviews.