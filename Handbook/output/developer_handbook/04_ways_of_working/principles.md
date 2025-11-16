# Delivery Principles

This page outlines the foundational delivery principles for our engineering teams: **Work-In-Progress (WIP) Limits**, **Inspect-and-Adapt**, and the **Definition of Ready/Done**. Adhering to these principles ensures consistent, sustainable, and predictable delivery outcomes.

---

## 1. Work-In-Progress (WIP) Limits

### What Are WIP Limits?

WIP limits specify the maximum number of work items (e.g., stories, tasks, defects) that can be in progress at any one time for a given workflow stage, team, or individual.

### Why Set WIP Limits?

- **Focus:** Limiting WIP forces the team to concentrate on a manageable number of tasks, promoting quality and completion.
- **Flow Improvement:** It helps uncover bottlenecks early, as blocked work becomes visible more quickly.
- **Reduced Multitasking:** Minimises context switching, which adversely affects productivity and quality.
- **Predictability:** Improves forecasting by smoothing out the delivery pace.

### How to Apply WIP Limits

1. **Set Initial Limits:** Determine the maximum number of stories or tasks permissible in each workflow column (e.g., “In Development”, “In Review”). Start conservatively; you can adjust later.
2. **Enforce Consistency:** Apply limits rigorously — do not exceed them ‘just this once’. Pressure to breach a limit is a signal to swarm or resolve a blockage, not to ignore the constraint.
3. **Visualise on Board:** Make WIP limits explicit on the task board. For example, show “In Review (Max 3)”.
4. **Adjust as Needed:** Review limits periodically (e.g., at retrospectives). Tighten if work frequently stalls; looser if people are idle for significant periods.

#### Example

If the “In Testing” column has a WIP limit of 2, and both slots are occupied:
- No further items may move into “In Testing” until at least one is completed.
- If developers finish another story, they help test or address test blockers instead of starting new work.

---

## 2. Inspect-and-Adapt

### What Is Inspect-and-Adapt?

Inspect-and-adapt is an iterative practice of reflecting on how work is performed, identifying improvement areas, and making incremental changes. It underpins continuous improvement.

### Why It Matters

- **Early Detection of Issues:** Regular reviews catch problems before they escalate.
- **Team Growth:** Provides structured opportunities to refine processes, tools, and collaborations.
- **Adaptability:** Maintains alignment as priorities, challenges, or team composition change.

### How to Implement Inspect-and-Adapt

1. **Regular Retrospectives:** Hold retrospectives at predictable cadences (e.g., end of each sprint, every two weeks).
2. **Fact-Based Discussion:** Focus on observable data from metrics (e.g., cycle time, defect rates) and direct experience.
3. **Actionable Outcomes:** Each session should result in concrete, assignable actions for improvement.
4. **Follow-up:** Track and review previous action items in subsequent sessions to ensure they are completed or revisited.

#### Example

After observing that stories repeatedly stall in “Code Review”, the team agrees to:
- Pair on reviews when a bottleneck forms.
- Encourage smaller pull requests to speed up the process.
Implement these changes, then review their effect in the next retrospective.

---

## 3. Definition of Ready & Definition of Done

### What Are Definitions of Ready and Done?

- **Definition of Ready (DoR):** The criteria that a work item must meet before it is accepted into development.
- **Definition of Done (DoD):** The criteria that a work item must satisfy to be considered complete.

These definitions ensure shared understanding and quality standards.

### Why They Matter

- **Clarity:** Reduces ambiguity on when work can start or finish.
- **Quality Assurance:** Ensures work is not started with missing information or finished with incomplete deliverables.
- **Efficient Handover:** Streamlines transitions between workflow stages, reducing rework and handoffs.

### How to Define and Use

#### Definition of Ready

1. **Gather Requirements:** Ensure stories or tasks specify acceptance criteria, designs, dependencies, and necessary test cases.
2. **Team Agreement:** The team must agree the item meets the DoR before moving it to “Ready for Development”.
3. **Revisit Regularly:** Adjust criteria based on recurring blockers or missed information.

##### Example DoR Checklist

- Story has clear acceptance criteria.
- Designs are attached or linked.
- Dependencies are identified and resolved.
- Test approach discussed.

#### Definition of Done

1. **Quality Criteria:** Confirm the item meets coding, testing, documentation, and deployment standards.
2. **Verification:** Work must be demonstrated, peer-reviewed, tested, and approved as per DoD.
3. **Team Ownership:** All team members must understand and apply the DoD without exception.

##### Example DoD Checklist

- Code peer reviewed and merged.
- Automated and manual tests passed.
- Documentation updated.
- Deployed to test/staging environment.
- Product Owner/customer sign off (if required).

---

## Summary

- **WIP Limits** optimise flow and focus.
- **Inspect-and-Adapt** ensures the team learns and improves continuously.
- **Definition of Ready/Done** enforces clarity, quality, and shared standards.

Consistently applying these delivery principles leads to sustainable, predictable, and high-quality outcomes across engineering teams.