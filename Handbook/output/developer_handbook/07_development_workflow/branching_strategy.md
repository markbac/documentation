# Branching Strategy

This page details our branching strategy, with specific guidance on working with long-lived feature branches, rebasing, and the Pull Request (PR) lifecycle. Understanding and adhering to these practices is crucial for maintaining an efficient, collaborative, and stable development environment.

---

## Table of Contents

- [Branch Types and Purposes](#branch-types-and-purposes)
- [Working with Long-Lived Feature Branches](#working-with-long-lived-feature-branches)
  - [When to Use a Long-Lived Feature Branch](#when-to-use-a-long-lived-feature-branch)
  - [Synchronising with Mainline](#synchronising-with-mainline)
  - [Example Workflow](#example-workflow)
- [Rebasing: Concept and Practice](#rebasing-concept-and-practice)
  - [Why Rebase?](#why-rebase)
  - [How to Rebase Safely](#how-to-rebase-safely)
- [Pull Request Lifecycle](#pull-request-lifecycle)
  - [Creating a PR](#creating-a-pr)
  - [Review Process and Expected Standards](#review-process-and-expected-standards)
  - [Updating a PR](#updating-a-pr)
  - [Merging a PR](#merging-a-pr)
- [Common Scenarios and Guidance](#common-scenarios-and-guidance)
- [Summary of Expectations](#summary-of-expectations)

---

## Branch Types and Purposes

| Branch type        | Purpose                                                      |
|--------------------|-------------------------------------------------------------|
| `main`             | Production-ready, stable codebase. All deployments originate here. |
| `feature/*`        | Isolated development of a new feature or significant change.         |
| `bugfix/*`         | Targeted fixes for specific issues.                                 |
| `release/*`        | Preparation and staging for production releases.                      |
| `hotfix/*`         | Rapid fixes directly to `main` for critical production issues.        |

---

## Working with Long-Lived Feature Branches

### When to Use a Long-Lived Feature Branch

Use a long-lived feature branch (e.g., `feature/epic-integration`) for large development efforts that:

- Span multiple sprints or weeks.
- Involve multiple engineers.
- Require ongoing integration with changes from `main`.

Short-lived branches (single-tasks, non-blocking work) should favour rapid merge to avoid complexity.

**Rationale:**  
Long-lived feature branches enable team collaboration and encapsulate complex work without destabilising `main`. However, they risk diverging significantly, leading to challenging merges, if not maintained carefully.

---

### Synchronising with Mainline

Regularly synchronise your feature branch with the latest changes from `main` to:

- Avoid large, conflict-heavy merges at the end of the effort.
- Surface integration issues early.
- Keep your branch close to the current state of production.

**Recommended Practice:**

- Pull from `main` and rebase onto it at least once per sprint, or immediately after significant `main` changes affecting your area.
- Resolve conflicts promptly and communicate anything non-trivial to the team.
- Avoid merging `main` into your feature branch unless a rebase is impractical due to commit volume or history rewriting concerns.

---

### Example Workflow

1. **Branch Creation**
    ```sh
    git checkout main
    git pull
    git checkout -b feature/epic-integration
    ```

2. **Daily Development**
    ```sh
    # Regular commits for work in progress
    git add .
    git commit -m "Implement authentication step 1"
    ```

3. **Synchronise with Main**
    ```sh
    git fetch origin
    git rebase origin/main
    # Resolve conflicts if present, then continue
    git rebase --continue
    ```

4. **Push and Share Progress**
    ```sh
    git push -f origin feature/epic-integration
    # Use --force-with-lease to minimise risk for others working on the branch
    ```

---

## Rebasing: Concept and Practice

### Why Rebase?

Rebasing applies your branch’s changes on top of the latest remote branch, yielding a *linear, comprehensible history* and reducing redundant or tangled merge commits. This:

- Makes future integration with `main` more predictable.
- Simplifies code review by presenting a straightforward narrative of changes.
- Prevents the cumulative build-up of merge conflict debt.

**Important:** Only rebase branches that you and your collaborators control. Avoid rebasing shared branches with external dependencies to prevent disrupting colleagues' work.

---

### How to Rebase Safely

1. **Fetch Latest Mainline**
    ```sh
    git fetch origin
    ```

2. **Rebase**
    ```sh
    git rebase origin/main
    ```
    - Resolve any conflicts as they appear; use `git status` to track progress.
    - Use descriptive commit messages after conflict resolution.

3. **Force-Push with Lease**
    ```sh
    git push --force-with-lease
    ```
    - `--force-with-lease` ensures you do not overwrite others’ commits on the branch.

4. **Coordinate**
    - Notify other collaborators before (and after) rebasing and pushing, so they can synchronise local changes.

---

## Pull Request Lifecycle

### Creating a PR

- Open a pull request from your feature or bugfix branch to the intended target (typically `main` or its release branch).
- Ensure your branch is rebased to the tip of the target branch to minimise integration surprises.

**PR Checklist:**

- The branch builds and tests pass in CI.
- The scope and intent are clearly described.
- All relevant code owners or stakeholders are requested for review.

---

### Review Process and Expected Standards

- Reviewers validate:
    - Code correctness and maintainability.
    - Adherence to project and style guidelines.
    - Sufficient test coverage and documentation.
- Use the review conversation to clarify intent, propose alternatives, and catch integration edge cases early.

**Turnaround:** PRs should generally reach review within one working day, with reviewers responding within the next.

---

### Updating a PR

- Amend commits where clarification or rework is required.
- Rebase onto the latest target branch when new changes have landed in `main` during the review period:
    ```sh
    git fetch origin
    git rebase origin/main
    git push --force-with-lease
    ```
- Add clarifying comments in the PR to highlight changes requested by reviewers.

---

### Merging a PR

- Only merge when:
    - All required checks and reviews have passed.
    - The branch remains up to date with `main` (i.e., no merge conflicts).
- Use "Squash and Merge" for single-purpose branches, or a regular merge for larger, audit-trail-preserving features with well-structured histories.
- Delete the branch after merging to keep the repository tidy.

---

## Common Scenarios and Guidance

- **Multiple Engineers on a Feature Branch:** Communicate before rebasing. Ensure everyone has synchronised their workspaces (`git pull --rebase`) before force-pushing.
- **Breaking Changes in Main:** Rebase frequently to adapt incrementally.
- **Hotfixes Required Mid-Feature:** Isolate hotfixes on a separate branch from `main` while coordinating with the feature branch for future synchronisation.
- **Legacy Feature Merges:** If rebasing is impractical (for very large or sensitive histories), request guidance from the tech-lead for alternative merge-based approaches, documenting reasoning in the PR.

---

## Summary of Expectations

- Use feature branches for all non-trivial work.
- Rebase regularly against `main`, not merging from it, to reduce conflicts and promote clean history.
- Coordinate and communicate during rebases, especially for shared branches.
- Ensure PRs are rebased, buildable, and reviewed before merging.
- Merge promptly after approval and clean up obsolete branches.

Following this strategy keeps our repository history linear, minimises integration pain, and ensures shared progress. If in doubt, coordinate with the team and err on the side of frequent, clean integration.