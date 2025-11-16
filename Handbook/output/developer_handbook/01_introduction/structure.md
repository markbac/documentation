# Handbook Structure

This page describes the structure of the engineering handbook and offers detailed guidance on how teams should navigate and contribute to it. Clear understanding of the handbook’s organisation ensures consistency, discoverability, and utility for all team members, from new joiners to experienced engineers.

---

## Purpose of the Handbook

The handbook serves as the centralised, authoritative resource for engineering practices, processes, standards, and reference materials across the organisation. Its consistent structure enables quick orientation, supports onboarding, and reinforces best practices. Well-organised documentation reduces miscommunication, duplication of effort, and technical debt.

---

## Structural Overview

The handbook is organised into the following sections, each serving a distinct purpose:

1. **Introduction**
    - Outlines the handbook’s goals, scope, and how to use it.
2. **Guides**
    - Step-by-step instructions for completing common engineering tasks.
    - Example: “Deploying a New Microservice to Production”.
3. **Standards**
    - Organisation-wide rules and requirements, such as code style conventions or review protocols.
    - Example: “Python Coding Standard”, “Pull Request Review Checklist”.
4. **Reference**
    - Definitive information not covered in guides or standards, including architectural background, tool documentation, and glossary terms.
    - Example: “AWS Account Structure Overview”, “Glossary of Terms”.
5. **Decision Records**
    - A historical record of significant technical decisions and the rationale behind them.
    - Example: “ADR-001: Adopt Kubernetes for Service Orchestration”.
6. **Team-specific Addenda** (where applicable)
    - Documented variations or supplements maintained by specific teams, with clear links to central policies.

This hierarchy is reflected in the wiki’s navigation, with each section further subdivided where necessary. The use of consistent naming conventions and page templates further improves clarity and searchability.

---

## How to Navigate the Handbook

Before starting a task or making a decision, locate the relevant section in the handbook:

- **For How-To Questions:** Consult the *Guides* section. These offer practical, actionable steps.
- **For Rules and Expectations:** Refer to *Standards*, which define what must or must not be done.
- **For Factual Information or Background:** Use the *Reference* section.
- **For Decision Context or Rationale:** Search in *Decision Records* (ADRs).
- **For Team-Specific Practices:** Check if your team maintains an addendum, but always start with organisation-wide material.

**Example workflow**:  
If deploying infrastructure changes:
1. Begin with the “Infrastructure Deployment Guide”.
2. Consult “Terraform Standards” for required practices.
3. Review reference pages on “AWS Accounts” if needed.
4. Check ADRs for any recent decision affecting deployments.
5. If you belong to a specialised team (e.g., Platform), consult your addenda for approved exceptions.

---

## Why the Structure Matters

A well-defined structure prevents ambiguity and duplication:
- **Efficiency:** Engineers find authoritative answers faster.
- **Consistency:** Minimum standards are applied evenly across teams.
- **Accountability:** Decision records ensure transparency over past choices.
- **Onboarding:** New joiners can trace the rationale behind our ways of working.

Each section has a defined purpose. Avoid placing content in inappropriate sections (e.g., don’t mix guides and standards), as this creates confusion and undermines trust in the documentation.

---

## Maintenance and Contributions

Teams are responsible for:
- Maintaining the accuracy and relevance of content, especially in their area of expertise or ownership.
- Proposing changes using the handbook’s established contribution process (see the “Contributing” guide).
- Ensuring additions fit the structural conventions and use the approved templates.
- Linking related content appropriately rather than duplicating information.

**Example:**  
If updating the “Pull Request Review Checklist”, place the edits under *Standards*, not within specific project documentation. Reference this checklist from any relevant guide, e.g., “Submitting a Pull Request”.

---

## Summary

- Always start with the top-level section that matches your need: Guides (how-to), Standards (rules), Reference (facts), Decision Records (rationale), or Addenda (team-specific).
- Follow structure and naming conventions to ensure reliability and clarity.
- Regular maintenance and proper use of sections make the handbook effective for everyone.

Adhering to this structure ensures the handbook remains a trusted, up-to-date engineering resource.