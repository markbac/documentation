# Backlog Refinement

Backlog refinement is a structured, collaborative workflow for maintaining a healthy, actionable product backlog. This process ensures that upcoming work items are well-understood, appropriately sized, and prioritised, thus enabling the team to plan effectively and deliver value with minimal friction.

---

## Purpose of Backlog Refinement

Backlog refinement (sometimes called 'grooming') serves to:

- **Improve Clarity:** Clarify what each backlog item means and what is required for successful delivery.
- **Expose Unknowns Early:** Identify gaps in requirements, technical dependencies, or blocked work before planning begins.
- **Enable Reliable Estimation:** Ensure items are decomposed and understood well enough to be estimated accurately.
- **Support Prioritisation:** Confirm that the backlog is ordered according to current project goals and constraints.
- **Reduce Waste:** Minimise time spent wrestling with vague or unready work items during sprint planning.

A well-refined backlog is fundamental for predictable, sustainable delivery and a positive engineering workflow.

---

## Who Takes Part

Backlog refinement is a cross-functional, team responsibility. Key participants include:

- **Product Owner (or equivalent):** Maintains the backlog, clarifies intent, and prioritises items.
- **Engineers:** Bring technical insight, raise implementation risks, and help decompose work.
- **Designers (where applicable):** Clarify UX/UI requirements and identify design dependencies.
- **QA/Testing (optional, but valuable):** Anticipate testability and acceptance issues.

Invite subject matter experts when items touch unfamiliar areas.

---

## Refinement Workflow

A systematic refinement process should be followed, typically on a recurring cadence (e.g., weekly) and, where needed, ad hoc for urgent changes.

### 1. Preparation

- **Product Owner** reviews and prioritises backlog items, ensuring top items align with product goals.
- Items are flagged for refinement when new, unclear, or large.

**Example:**  
A user story, "As a user, I can reset my password via email," is identified as a high priority but is vague on technical approach and acceptance criteria.

### 2. Collaborative Discussion

The team reviews each candidate item, asking:

- **What does success look like?** (Clarify acceptance criteria.)
- **Are requirements testable, and is anything missing?**
- **What dependencies (internal or external) does this item have?**
- **Is the scope clear and achievable in a single sprint?**
- **Are there any technical constraints or known risks?**

This is the time for open questions, requirement clarification, and surfacing assumptions.

**Example Questions:**

- "Is email sending handled in-house or via an external service?"
- "What rate-limiting do we need to prevent abuse?"
- "Should users be able to reset passwords from both web and mobile?"

### 3. Decomposition (If Required)

If an item is too large or ambiguous (sometimes referred to as an 'Epic'), break it into smaller, more actionable pieces.

**Example:**  
"User password reset" may become:
- "Implement backend API for password reset"
- "Design email template"
- "UX flow for password reset in web app"
- "QA: Password reset error handling cases"

Each sub-item should be deliverable and estimable.

### 4. Estimation

Once items are clearly defined, the engineering team estimates them using the team's preferred method (e.g., Story Points, Time-based estimates).

- Unclear or un-estimable items signal a need for further clarification or decomposition.
- Estimates inform planning and expose hidden work or risk.

### 5. Final Checklist for Readiness

A backlog item is 'refined' and ready for a planning meeting when:

- The **description** and **acceptance criteria** are clear and unambiguous.
- **Dependencies** and **constraints** are identified.
- **Designs/wireframes** are attached or referenced if relevant.
- Relevant parties have had the opportunity to review and comment.
- The team agrees the item can be completed within a single sprint (unless intentionally larger for Epic tracking).

Use a Definition of Ready (DoR) to confirm consistency.

---

## Common Pitfalls and How to Avoid Them

- **Vague Acceptance Criteria:** Leads to misunderstandings and rework. Insist on specific, testable outcomes.
- **Technical Work Unaccounted For:** Backlog should include technical, non-user-facing tasks (e.g., migrations, upgrades) with clear scope.
- **Over-Refinement:** Avoid spending time detailing items that are unlikely to be worked on soon. Focus on the top N (as agreed by the team).

---

## Best Practices

- Time-box refinement sessions to prevent fatigue and stay focused.
- Keep the backlog visible and updated; agree on regular review cadence.
- Encourage all team members to contribute questions and raise risks.
- Periodically review recently delivered items to improve future refining.

---

## Summary

Refinement is a structured, ongoing team activity to ensure backlog items are clear, actionable, and accurately estimated before planning. Effective refinement reduces delivery risk, enables predictable planning, and creates shared understanding. Every team member has a role in maintaining a healthy and transparent backlog.

---

**Next:** [Estimation](./Estimation.md)