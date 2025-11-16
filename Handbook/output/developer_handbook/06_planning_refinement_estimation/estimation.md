# Estimation

Accurate estimation is foundational to effective engineering planning, delivery predictability, and stakeholder trust. This page provides detailed guidance on estimation approaches, calibration techniques, and the policies you are expected to follow within our engineering teams.

---

## Why Estimation Matters

Estimation enables teams to:

- **Plan sprints and releases realistically**, avoiding overcommitment or underutilisation.
- **Communicate reliably with stakeholders**, providing clarity on timelines and resourcing needs.
- **Identify technical uncertainty and risk early** through sizing and comparison.
- **Retrospect and improve** by comparing estimates against actuals, refining understanding and process.

Flawed or careless estimation leads to missed deadlines, overwork, loss of credibility, and the accumulation of technical debt.

---

## Approaches to Estimation

There are several proven approaches to estimation, each with strengths and caveats. Teams may blend these as appropriate for their context.

### 1. Relative Estimation (Story Points)

Relative estimation measures work in comparison to other known items, using an abstract scale such as story points (commonly Fibonacci: 1, 2, 3, 5, 8, 13). The focus is on comparative effort, complexity, and uncertainty — not absolute time.

**When to use:** In agile contexts for backlog items, especially when detailed uncertainty makes time-based estimates unreliable.

#### How to Apply:

- **Establish a Reference Story**: Select a well-understood, average-sized story—assign it a mid-scale value (e.g., 3 points).
- **Estimate New Work by Comparison**: Discuss as a team and assign points by comparing new work to the reference story.
- **Focus on Effort and Complexity, Not Person-Hours**: Consider factors like unknowns, review effort, dependencies, and testing complexity.

**Example:**

| Story                              | Points |
|------------------------------------|--------|
| Add form validation                | 2      |
| Integrate third-party payment API  | 5      |
| Refactor authentication module     | 8      |

### 2. Time-Based Estimation (Ideal Hours or Days)

Time-based estimation measures the expected effort in hours or days, assuming no interruptions (“ideal time”).

**When to use:** For well-understood, discrete tasks or where explicit scheduling is required.

#### How to Apply:

- **Break Work Into Small, Well-Scoped Tasks**: Tasks larger than two days should be split if possible.
- **Estimate Ideal Effort, Not Calendar Time**: For example, “this task requires 6 hours of focused work.”
- **Clarify Assumptions**: Note dependencies and external factors that might affect actual delivery.

**Example:**

| Task                                | Ideal Hours |
|-------------------------------------|-------------|
| Set up CI pipeline                  | 3           |
| Write integration test for payments | 4           |

### 3. T-Shirt Sizing

An alternative quick sizing method using buckets (e.g., S, M, L, XL). Useful in early backlog refinement or for high-level roadmap planning.

**When to use:** When little detail is available but rough sizing aids prioritisation.

---

## Estimation Calibration

Estimation is not a one-off exercise but an iterative process that improves with feedback and calibration.

### Techniques for Calibration

- **Compare Estimates to Actuals**: Regularly review completed work to assess accuracy.
- **Hold Estimation Retrospectives**: As a team, discuss sources of inaccuracy and refine your approach.
- **Update Reference Stories**: If reference stories no longer reflect average work, select new ones.
- **Document Known Unknowns**: Capture what was missed in initial estimation to build collective wisdom.

### Team Velocity (for Story Points)

Track completed story points per sprint to establish a sustainable team “velocity” baseline. Use average velocity to forecast future capacity, but be wary of using velocity as a productivity metric.

---

## Policies and Expectations

- **Estimate Collaboratively:** All team members involved in delivery should participate. Diverse perspectives reduce individual bias and surface hidden complexity.
- **Re-Estimate as Work Evolves:** If significant details or requirements change, update estimates promptly.
- **Expose and Communicate Confidence:** Be explicit about low-confidence or high-risk estimates. Use wider ranges or flagging when needed.
- **Avoid Single-Engineer Estimation for Significant Tasks:** Major features or architectural changes should always receive group scrutiny.
- **Break Down Large Work:** Items that cannot be confidently estimated should be decomposed or require technical spike investigations.
- **Do Not Use Estimation as a Performance Target:** Estimates are for planning and risk management, not individual assessment.

---

## Practical Example: Applying Estimation in a Sprint

1. **Backlog Refinement:** The team reviews new stories, assigns story points using reference stories, and discusses uncertainties.
2. **Sprint Planning:** The team uses recent velocity (e.g., ~21 points per sprint) to select a reasonable volume of work.
3. **Ongoing Adjustment:** During the sprint, if a story is found to be considerably larger in scope, the team flags and re-sizes or re-scopes as necessary.
4. **Sprint Review/Retrospective:** After completion, original estimates are compared to actual effort. Outliers are discussed for continuous improvement.

---

## Summary

- Choose estimation approaches suited to the level of uncertainty and granularity required.
- Involve the full delivery team for broad perspective and risk identification.
- Calibrate estimates over time, learning from past inaccuracies.
- Use estimates to inform planning, not as targets or performance measures.
- Communicate clearly about estimation confidence and revisit estimates as work evolves.

When applied consistently, robust estimation practices improve predictability, transparency, and team health. Adopt these methods as standard and seek guidance when new estimation challenges arise.