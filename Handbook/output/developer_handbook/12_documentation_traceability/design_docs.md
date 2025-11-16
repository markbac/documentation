# Design Documents: When to Create High-Level Design Docs, ADRs, and RFCs

This page explains clear guidance for when and how to use High-Level Design Documents (HLDs), Architecture Decision Records (ADRs), and Requests for Comments (RFCs) in our engineering workflows. Understanding the purpose and correct usage of each document ensures our work is well-justified, traceable, and easy to follow—both now and in the future.

---

## Overview

| Document Type                        | Main Purpose                                                 | Typical Use Cases                                             |
| ------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------- |
| **High-Level Design Document (HLD)**  | Describe and justify system/component architecture before implementation. | New service designs, major refactors, significant feature builds. |
| **Architecture Decision Record (ADR)**| Record a specific technical decision, including context and alternatives considered. | Choosing a storage engine, deciding on a library or protocol. |
| **Request for Comments (RFC)**        | Propose and gather feedback on a significant technical change or policy. | Introducing a new API, changing deployment processes.         |

---

## High-Level Design Documents (HLDs)

### What

A High-Level Design Document lays out the architecture, significant components, and interactions for a system or major feature. It contextualises the problem, articulates requirements, explores viable approaches, and defines the chosen solution with diagrams or pseudocode where useful.

### Why

- Ensures all stakeholders align on what is being built and *why*.
- Forces thought into interfaces, scaling, risks, and dependencies up front.
- Enables effective code and security review, future maintenance, and onboarding.

### When to Use

Write an HLD **prior to implementation** when:

- Designing a new service, application, or subsystem.
- Making major architectural changes (e.g., migrating from monolith to microservices).
- Introducing a significant new feature with cross-cutting concerns or dependencies.
- Performing a large-scale refactor that alters component responsibilities.

**Example:**  
You are planning to implement distributed caching across multiple microservices. An HLD should detail high-level API changes, cache invalidation strategies, and affected deployment architectures.

---

## Architecture Decision Records (ADRs)

### What

An ADR is a concise, versioned log entry recording *one specific architectural or technical decision*. It captures the context, considered options (with pros and cons), the decision taken, and its consequences.

### Why

- Makes reasoning for non-obvious decisions transparent and easy to revisit.
- Documents the alternatives and their trade-offs, helping avoid repeated debate.
- Serves as a historical source of truth when revisiting or questioning decisions.

### When to Use

Create an ADR whenever you make a *non-trivial technical or architectural decision* at the codebase, project, or platform level. Typical triggers include:

- Choosing one third-party library or technology over another.
- Adopting a particular database schema or communication protocol.
- Deciding not to implement a feature or fix a known issue.

ADRs should not detail *entire architectures* or full-feature designs—they are for *specific decisions*.

**Example:**  
Selecting PostgreSQL over MongoDB for a new service due to transaction requirements and team expertise. An ADR should record the context, considered databases, rationale, and any implications for future scaling.

---

## Requests for Comments (RFCs)

### What

An RFC is a structured proposal circulated to solicit feedback and build consensus around *significant* technical changes that may affect multiple teams, interfaces, or workflows.

### Why

- Engages all relevant stakeholders early, surfacing concerns and improvements.
- Documents both the proposal and the discussion, ensuring traceability.
- Increases the quality and adoption of the solution by gathering diverse perspectives.

### When to Use

Draft an RFC **when the proposed change is broad in scope**, including:

- API changes that affect downstream consumers.
- Company-wide technical standards or processes.
- Deprecation or migration plans with multi-team impact.
- New tools or frameworks intended for adoption beyond a single project.

**Example:**  
Before introducing a new organisation-wide authentication mechanism, create an RFC detailing the motivation, approach, migration plan, and impact on existing services. Circulate for broad input before implementation begins.

---

## Choosing the Right Document

When in doubt, start by assessing:

1. **Scope:**  
   - Is it about a *system design*? → HLD.
   - Is it a *single technical decision* in context? → ADR.
   - Is it a *cross-team or company-wide proposal*? → RFC.

2. **Audience:**  
   - *Immediate team/implementation detail?* → HLD or ADR.
   - *Wider engineering or stakeholder groups?* → RFC.

3. **Longevity and Traceability:**  
   - *Will people need to understand or revisit this rationale later?*  
     If yes, capture it in ADR or reference from HLD/RFC as needed.

---

## Practical Examples Summary

- **HLD:** "Designing a new image processing pipeline"—captures requirements, possible designs, chosen architecture, and risk analysis.
- **ADR:** "Decision to use Redis pub/sub for inter-service notifications"—records context, alternatives, and consequences.
- **RFC:** "Proposal to standardise error response formats across all APIs"—introduces the proposal for organisation-wide debate and refinement.

---

## Expectations

- **Do not skip documentation**; ensure every major architectural change, decision, and broad proposal is properly captured.
- **Reference ADRs in HLDs** (and vice versa) where appropriate to provide traceability.
- **Use clear, succinct language**, and include diagrams or data flows in HLDs and RFCs to clarify where helpful.
- **Version and date all documents**. Use changelogs if amending RFCs or HLDs post-approval.

---

By following these guidelines, we ensure technical clarity, decision traceability, and smooth knowledge transfer for both current and future engineers.