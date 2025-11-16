# Sprint Planning

Sprint Planning is a structured event that sets the trajectory for the upcoming iteration. Its purpose is to determine what can be delivered during the sprint, clarify how the team will accomplish the work, and ensure that the scope is aligned with the team's real capacity.

This page details how to approach Sprint Planning, focusing on planning goals, capacity thinking, and scope control, with actionable guidance suitable for direct adoption.

---

## Overview

Sprint Planning is a collaborative activity, typically occurring at the start of a sprint. The outcome is a clear sprint goal, a well-defined set of backlog items (often called the sprint backlog), and an initial plan for delivery.

Effective Sprint Planning enables:

- Clear alignment on objectives
- Predictable delivery
- High team morale (by avoiding over-commitment)
- Early identification of risk and blockers

---

## Planning Goals

### Defining the Sprint Goal

The sprint goal provides a unifying objective for the team. It should be:

- Concise: Summarises what the sprint will achieve in 1–2 sentences.
- Measurable: Allows the team to determine if it has met its ambition by the end of the sprint.
- Relevant: Directly connected to business or product priorities.

**Why it matters**: Without a clear goal, sprints become a checklist of unrelated tasks, reducing focus and making it harder to judge success.

**Example**:
> "Implement user authentication flows (registration, login, password reset) for the main web app."

### Selecting Backlog Items

Only consider items that contribute to the sprint goal. Use the following criteria:

- Accessibility: Items must be ready for implementation (refined, with clear acceptance criteria).
- Dependencies: Upstream dependencies need resolution or clear mitigation.
- Value: Each item must directly support the sprint goal.

---

## Capacity Thinking

### Understanding Team Capacity

Capacity estimation involves calculating the team's realistic ability to deliver work in the sprint. This is not simply a function of calendar days; it accounts for:

- Team member availability (holidays, planned absences, training)
- Non-development work (meetings, code reviews, incident response)
- Shared responsibilities (support rotas, mentoring)

**Practical Steps**:

1. **Determine base days**: Multiply the number of working days in the sprint by the number of team members.
2. **Subtract known absences**: Remove days for holidays and predicted non-project commitments.
3. **Buffer for overhead**: Deduct percentage (commonly 10–20%) for recurring non-feature work.

**Example Calculation**:

- Two-week sprint (10 working days)
- 5 developers
- 2 developers on holiday for 2 days each
- 15% buffer for meetings and support

1. Base: 10 days × 5 people = 50 days
2. Holidays: 4 days absent; 50 – 4 = 46 days
3. Buffer: 15% of 46 = 6.9; 46 – 6.9 = ~39 developer-days capacity

### Why Capacity Thinking Matters

Overcommitting leads to failed sprints, reduced morale, and eroded trust in team predictability. Undercommitting wastes team potential. Consistently estimating capacity leads to sustainable, reliable delivery.

---

## Scope Control

### Prioritising and Limiting Scope

Only commit to the amount of work that fits the calculated capacity. If there is excess work, clearly prioritise:

1. High-value or high-urgency items
2. Items with low uncertainty
3. Tasks that unblock subsequent work

**Commitment Approach**:

- The team collectively decides what is achievable, based on capacity and item complexity.
- Where uncertainty exists (e.g., new technology or vague requirements), consider splitting stories or allocating explicit time for investigation.

### Explicitly Defining Done

Revisit and confirm the team’s Definition of Done. Ensure every backlog item selected for the sprint can meet this standard within the sprint timebox.

### Managing Scope Creep

- Lock the sprint backlog once Planning ends. New work should only be added through an agreed, usually exceptional, process.
- If unexpected work arises (e.g., urgent production issue), immediately reassess the sprint backlog with the team and stakeholders.

---

## Practical Process

1. **Review Product Backlog**: Product Owner presents refined candidate items for the sprint.
2. **Discuss Sprint Goal**: Align on a sprint goal reflecting business value.
3. **Estimate Capacity**: Account for availability, overhead, and buffer.
4. **Select Work**: Pull in items until capacity is filled, prioritising by relation to the sprint goal and readiness.
5. **Plan Delivery**: Outline initial tasks; identify possible bottlenecks or dependencies.
6. **Confirm Commitment**: Team reviews whether the amount of selected work is realistic and collectively commits.

---

## Key Expectations

- Outcomes are clear: sprint goal, backlog items, delivery plan.
- Commitments are based on real capacity, not aspiration.
- Scope is fixed unless formally adjusted.
- All team members are involved, with agreement on what will be delivered.

---

## Common Pitfalls to Avoid

- Underestimating non-coding work and overfilling the sprint.
- Accepting unrefined or ambiguous items.
- Failing to buffer for interruptions or support work.
- Allowing unchecked scope changes after Planning.

---

## Summary

Effective Sprint Planning requires clear goals, honest assessment of capacity, and disciplined scope control. Doing so leads to predictable delivery, satisfied stakeholders, and a sustainable team pace. Always revisit these principles before each sprint to maintain high standards and delivery confidence.