# Requirements

## Introduction

Requirements are the foundation of successful engineering projects. A requirement precisely defines what a system, product, or component must do or how it must perform. Well-written requirements guide design, development, verification, and validation activities. Conversely, poorly defined requirements introduce confusion, errors, and rework.

This page explains in detail how to write and verify good requirements, ensuring they are actionable, clear, and testable.

---

## What Is a Requirement?

A requirement is a formal statement of needed functionality, property, or constraint for a particular system or component. Requirements typically answer the question: “What must this product or system do, or what conditions must it comply with?”

- **Example**: “The system shall allow users to reset their password by email within 5 minutes.”

---

## Why Good Requirements Matter

- **Guidance**: They direct design and implementation.
- **Communication**: Provide a common understanding between stakeholders (developers, testers, management, and customers).
- **Verification**: Form the basis for testing and acceptance criteria.
- **Project Scope**: Prevent scope creep and manage expectations.

---

## Characteristics of Good Requirements

Writing good requirements is not simply about documenting needs, but ensuring that each requirement is:

1. **Correct**: Expresses stakeholder intent accurately.
2. **Unambiguous**: Only one possible interpretation.
3. **Complete**: Addresses all necessary aspects; contains all relevant detail.
4. **Consistent**: Does not conflict with other requirements or itself.
5. **Verifiable**: It is possible to check (by analysis, demonstration, test, or inspection) whether the requirement is met.
6. **Necessary**: Relates directly to a stakeholder need or system purpose; not extraneous.
7. **Feasible**: Realistic given system constraints (technical, cost, schedule, etc.).
8. **Traceable**: Can be uniquely identified and referenced.

---

## Writing Good Requirements

### Use Specific and Measurable Language

- Avoid vague terms like “fast”, “easy”, “sufficient”, or “user-friendly”.
- State measurable criteria: quantities, time limits, accuracy, etc.

**Example**  
_Vague_: “The system should respond quickly.”  
_Clear_: “The system shall respond to user requests within 2 seconds under normal load.”

### Use the Correct Structure

A common and effective format is:

> [Subject] **shall** [action or quality] [additional conditions, limitations, or performance criteria].

**Examples**:
- “The API shall return a response within 300 milliseconds for standard queries.”
- “The application shall support up to 500 concurrent users.”

### Each Requirement States a Single Need

Avoid combining multiple needs in a single requirement (no “and/or” ambiguity).

**Poor**: “The system shall export reports as PDF and email notifications to users.”
**Good**:

- “The system shall export reports as PDF files.”
- “The system shall email notifications to users upon completion of report export.”

### Avoid Implementation Details

Requirements describe *what* is needed, not *how* to fulfil it (unless mandated).

**Poor**: “The server shall use MongoDB to store user data.”
**Good**: “The system shall store user data persistently.”

Implementation choices are determined during design unless specific solutions are required (and justified).

### Use Consistent Terminology

Refer to entities, actions, and conditions using the same terms throughout the document. Define terms if necessary.

---

## Verifying Requirements

Verification is the process of confirming that requirements are clear, valid, and practical before development begins.

### Review Process

1. **Inspection**: Team reviews each requirement for the characteristics listed earlier.
2. **Walkthroughs**: Stakeholders (including testers) walk through requirements, discussing interpretation and edge cases.
3. **Test Criteria Definition**: Develop acceptance tests or verification methods for each requirement.

### Example Verification Table

| Requirement                                         | Verification Method         | Notes                          |
|-----------------------------------------------------|----------------------------|--------------------------------|
| The device shall weigh less than 500 grams.         | Measurement                | Use calibrated scale           |
| The web app shall support 1,000 concurrent users.   | Load Testing               | Require defined use cases      |
| All user data shall be encrypted at rest.           | Code Review, Inspection    | Verify encryption in database  |

### Traceability

Assign each requirement a unique identifier (e.g., “REQ-1234”) to allow for reference and linking across specifications, implementation, and testing artefacts.

---

## Common Pitfalls and How to Avoid Them

- **Ambiguity**: Use precise language; test by asking reviewers to paraphrase the requirement.
- **Over-Specification**: Avoid dictating design or technology unless required.
- **Multiple Conditions**: Write separate requirements for distinct needs.
- **Incomplete Requirements**: Check for missing constraints (e.g., performance, reliability).
- **Inconsistent Terminology**: Maintain a glossary or controlled vocabulary.

---

## Summary Checklist

Use this checklist for each requirement:

- [ ] Expresses a single, specific need
- [ ] Unambiguous and clear
- [ ] Measurable and verifiable
- [ ] Necessary for the intended outcome
- [ ] Technically feasible
- [ ] Uses consistent terminology
- [ ] Traceable by unique identifier

---

## Conclusion

Well-written requirements are a non-negotiable foundation for engineering success. They enable accurate planning, reliable implementation, unambiguous testing, and a shared understanding across the team. Apply the guidance on this page to ensure all requirements you author or review are fit for immediate, error-free use.