# User Stories

User stories are a core component of agile engineering processes, serving to capture and communicate functional requirements from the user's perspective. This page details how to compose effective user stories, the INVEST quality criteria, and the creation and use of acceptance criteria.

---

## Purpose of User Stories

User stories provide a concise, user-focused statement of a desired capability, enabling the engineering team to understand the "what" and "why" of a requirement without prescribing "how" it should be solved. They facilitate communication between stakeholders and development teams, guide implementation, and act as reference points for testing and acceptance.

---

## Structure of a User Story

A user story is usually written in the following format:

> As a `<type of user>`, I want `<some goal or capability>`, so that `<some reason or benefit>`.

### Example

> As a registered user, I want to reset my forgotten password, so that I can regain access to my account without administrator intervention.

**Explanation:**
- **Who?** "Registered user" — captures the relevant audience.
- **What?** "Reset my forgotten password" — describes the desired capability.
- **Why?** "Regain access to my account without administrator intervention" — clarifies the intended value.

---

## Why Good User Stories Matter

- **Clarity:** Well-structured stories ensure all stakeholders share a common understanding.
- **Alignment:** Stories built from the user’s perspective maintain focus on user value, preventing technical implementation from overshadowing business needs.
- **Planning:** Stories sized correctly facilitate estimation, prioritisation, and incremental delivery.
- **Quality:** Stories with clear acceptance criteria enable objective validation and reduce ambiguity.

---

## The INVEST Criteria

A user story should meet the INVEST criteria:

| Criterion      | Description                                                                  |
|----------------|-------------------------------------------------------------------------------|
| **Independent**   | The story should stand alone; it can be developed and delivered separately. |
| **Negotiable**    | The story captures intent, not a contract; implementation details can be adjusted. |
| **Valuable**      | The story delivers clear value to the user or customer.                      |
| **Estimable**     | The team can estimate the effort required; uncertainties are identified.      |
| **Small**         | The scope is limited enough for delivery within a single iteration (usually a few days). |
| **Testable**      | Clear conditions exist to verify completion; acceptance criteria are explicit. |

### Practical Example

A user story failing INVEST might be:

> As a user, I want a flexible system.

- It lacks detail (not **Estimable** or **Testable**).
- Implementation or value is unclear (**Valuable** and **Negotiable** unmet).

A compliant user story:

> As a content editor, I want to schedule articles for future publication, so that I can manage content visibility in advance.

---

## Acceptance Criteria

**Acceptance criteria** define conditions that must be true for the story to be considered complete. They serve several functions:
- Remove ambiguity by describing functional and, if relevant, non-functional requirements.
- Guide developers and testers on expected outcomes.
- Serve as the basis for acceptance testing.

### How to Write Acceptance Criteria

- State each criterion as a discrete, verifiable statement.
- Use clear, unambiguous language.
- Where helpful, employ the "Given/When/Then" format from Behaviour Driven Development (BDD).

#### Example Acceptance Criteria

_For the story: "As a registered user, I want to reset my forgotten password, so that..."_

- Given I am on the login page, when I click "Forgot password", then I am prompted to enter my email address.
- When I enter a registered email address, a password reset link is emailed to me.
- When I click the password reset link, I am navigated to a form where I can set a new password.
- The new password must meet documented security requirements.
- After successfully resetting the password, I can log in using the new password.

---

## Writing User Stories in Practice

### Steps to Follow

1. **Identify the User or Persona**
   - Consider actual end users whenever possible.
2. **State the Desired Capability**
   - Be specific about what the user wants to achieve.
3. **Explain the Reason or Value**
   - Clarify the outcome or benefit to prevent "solutionising".
4. **Check Against INVEST**
   - Review and revise until all INVEST criteria are met.
5. **Define Acceptance Criteria**
   - Specify how success will be verified.
6. **Review with Stakeholders**
   - Discuss and iterate based on feedback or questions.

---

## Common Pitfalls to Avoid

- **Overly Broad Stories:** Break down large ("epic") stories into smaller, deliverable units.
- **Technical Tasks Masquerading as Stories:** User stories must represent user-facing value, not internal tasks.
- **Vague Acceptance Criteria:** Ensure every acceptance criterion is clear and testable.

---

## Summary

- User stories articulate user needs, goals, and value in a concise format.
- The INVEST criteria provide a standard for quality and readiness.
- Acceptance criteria establish the definitive scope and provide testability.
- Well-crafted user stories enhance delivery predictability, user satisfaction, and team alignment.

---

**Next Steps:** Apply these guidelines during backlog refinement and story writing sessions. Review each user story for compliance before it enters development.