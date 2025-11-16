# Features

## Overview

This page defines the concept of a **Feature** within the product development process, explains its relationship to requirements, and provides practical guidance on decomposing and documenting features. It is intended to ensure a shared, rigorous understanding that enables traceability, effective breakdown for implementation, and consistent linkage between user needs and engineering work.

---

## What Is a Feature?

A **Feature** is a distinct, deliverable unit of product functionality that satisfies one or more stakeholder requirements. Features offer meaningful value to users or customers—they are not merely technical components, but capabilities or behaviours visible at the product level.

Features *translate* requirements (which state business needs or problems) into functional terms that can be designed, implemented, tested, and validated. They exist at a level above individual user stories or technical tasks and should be clearly described, actionable, and testable.

### Example

- **Requirement**: Users must be able to recover their password if forgotten.
- **Feature**: Password Reset—allow users to initiate a password reset via email.

---

## Why Feature Definition Matters

Precise, thoughtful feature definition is critical to:

- **Traceability:** Linking business requirements to design, implementation, and test artefacts.
- **Alignment:** Making sure stakeholders, designers, and engineering teams share a common understanding of what is being built.
- **Decomposition:** Supporting effective breakdown into user stories or tasks for estimation, planning, and delivery.
- **Verification:** Developing acceptance criteria and test cases that are directly traceable to features ensures work is fit for purpose.

Poorly defined features result in miscommunication, rework, scope creep, and gaps between requirements and the resulting product.

---

## Feature Decomposition

### Step 1: Identify Features from Requirements

Each feature should be explicitly derived from one or more business or system requirements. Start by examining requirement statements and look for product-level capabilities implied by those needs.

**Example:**

- Requirement: "The system must allow users to manage their personal profile information."
- Feature Candidate: "Profile Management" (includes viewing, editing, and updating user details).

### Step 2: Decompose High-Level Features

A high-level feature may encapsulate several distinct user needs or functions. Break down such features if:

- Functionality can be delivered independently.
- The capability is significant enough to require separate design, development, or testing effort.
- Stakeholders expect delivery in phases or increments.

Decompose until each feature is:

- Clearly defined in scope (“what”, not “how”).
- Feasible to implement and test in a single release or milestone.
- Valuable from a user or system perspective.

**Example:**

- High-Level Feature: "Notifications."
    - Decomposed Features:
        - "Email Notifications"
        - "In-app Notifications"
        - "Push Notifications"

### Step 3: Define Clear Acceptance Criteria

Each feature must include objective, testable acceptance criteria. This ensures features are *done* only when they fully meet the intended requirement.

---

## Documenting Features

A features list or catalogue should include for each feature:

- **Identifier** (unique and persistent, e.g., FTR-001)
- **Title** (concise, descriptive)
- **Description** (clear, complete explanation of scope and intent)
- **Related Requirements** (references to the originating requirement(s))
- **Acceptance Criteria** (list, measurable and testable)
- **Dependencies / Constraints** (as needed)
- **Stakeholder** (owner/responsible business function)

**Sample Feature Entry:**

| Field               | Example                                                     |
|---------------------|------------------------------------------------------------|
| Identifier          | FTR-007                                                     |
| Title               | Email-based Password Reset                                  |
| Description         | Enables users to reset their password via a time-limited link sent to their registered email address. |
| Related Requirement | REQ-002: "Users must be able to recover their accounts."    |
| Acceptance Criteria | - Password reset link is sent to the registered email.<br>- Link expires after 60 minutes.<br>- Only valid for one-time use. |
| Dependencies        | Outbound email infrastructure available.                   |
| Stakeholder         | Product Owner                                              |

---

## Linking Features to Requirements

Every feature **must** be explicitly traced to at least one business or system requirement. This linkage enables:

- Verification that all requirements are addressed.
- Impact analysis if requirements change.
- Traceability during audits or reviews.

Maintain bidirectional links (from requirement → feature, and feature → requirement) in your tracking system, documentation, or requirements management tool.

---

## Summary of Expectations

- Define features as discrete, valuable units of functionality, not just technical deliverables.
- Ensure features originate from clearly stated requirements, and maintain clear traceability.
- Decompose high-level features until each is actionable, testable, and of appropriate scope.
- Document each feature thoroughly, including acceptance criteria and related requirements.
- Manage features in a transparent, accessible catalogue that supports traceability throughout the engineering lifecycle.

Proper feature definition and management are non-negotiable prerequisites for efficient, effective product engineering and reliable delivery of stakeholder value.