# Commit Practices

This page defines our standards for structuring commits, ensuring traceability, and writing commit messages. Adherence to these practices maintains a healthy project history, aids debugging, and enables effective collaboration across the engineering team.

---

## 1. Commit Structure

### 1.1. Atomicity

**Each commit must represent a single logical change.**  
Avoid combining unrelated changes, as this makes code review, reversion, and historical analysis significantly harder.

- *Do not*: Fix a typo in one file and refactor a function in another within the same commit.
- *Do*: If correcting a comment and fixing a bug, create separate commits for each.

### 1.2. Scope

Commits should be as small as possible, but as large as necessary to maintain context and compile/test successfully. Never commit code that breaks build integrity or test suites (unless the purpose is to fix those very tests).

- *Do*: If changing a function’s signature, update all immediate usages in the same commit.
- *Do not*: Leave the codebase in a partially implemented state across several commits.

### 1.3. Reviewability

Group changes to enhance readability and review agility. Avoid excessive whitespace or reformatting in a commit that also contains behavioural changes; preserve clarity by splitting such changes.

- *Do*: First commit: reformat code only. Second commit: introduce logic changes.
- *Do not*: Hide logic changes among unrelated formatting.

---

## 2. Traceability Rules

### 2.1. Link to Tracking System

All commits affecting deliverables, bug fixes, or tracked work must reference the relevant task or ticket ID in the message (e.g., JIRA, GitHub Issue).

- *Why*: This ensures every change can be traced to its original requirement, discussion, or reported bug, aiding audits and change management.

**Example:**  
```
Fix out-of-bounds error in parsing routine

JIRA-142: Array index could exceed size if input malformed. Added boundary checks and tests.
```

### 2.2. Ownership and Author Information

Ensure all commits are attributed to the correct author via configured Git credentials. Team-level committer accounts are discouraged except in rare, approved cases.

- *Why*: Attribution supports accountability and aids downstream communication when context is needed about a change.

---

## 3. Commit Messages

### 3.1. Structure

Commit messages **must** be clear, concise, and provide enough context to understand the purpose and impact of the change—even when viewed outside the current branch or in isolation.

**Standard format:**
```
<Short summary (max 50 characters, imperative present tense)>

<Detailed explanation (wrap at 72 chars), if needed.>
<Reference to tracking system ID(s), if applicable.>
```

- **Short Summary**:  
  - Capitalise the first word.
  - Do *not* end with a period.
  - Use the imperative mood (e.g., “Add validation to input forms”).

- **Detailed Explanation**:  
  - Explain *what* and *why*, avoid restating the code.
  - Note side-effects, breaking changes, or prerequisites if relevant.

### 3.2. Good Examples

```markdown
Add bounds checking to YAML parser

JIRA-142: Prevents crash on malformed input as described in issue. Unit
tests included to validate expected behaviour.
```

```markdown
Refactor UserService dependencies

Simplify constructor to use dependency injection, removing manual
instantiation. All related tests updated. No external API impact.
```

### 3.3. Bad Examples

- `fixed bug`
- `stuff`
- `changes`
- `Update`

Such messages convey no value and hinder future understanding or auditing.

---

## 4. Practical Commit Practices

- **Stage only intended changes:** Review with `git diff --staged` before committing.
- **Do not commit secrets or sensitive data:** Exclude credentials, keys, or proprietary data from commits.
- **Commit frequently, but not excessively:** Prefer small, logical commits. Do not treat version control as a backup for untested work-in-progress.
- **Amend or squash to tidy history:** When collaborating closely, rewrite commits before merging to improve clarity and maintain a coherent project history. Use rebase and squash responsibly.
- **Use signed commits where required:** Sign commits to verify authorship if mandated by project policy.

---

## Summary Table

| Practice          | Guidance                                                                                |
|-------------------|----------------------------------------------------------------------------------------|
| Atomic commits    | Each change should be a single logical unit                                             |
| Traceability      | Reference all relevant issue/ticket IDs in commit messages                              |
| Message quality   | Use clear, imperative summaries; include detail and context where needed                |
| Scope             | Commits must be buildable/testable and avoid mixing unrelated changes                   |
| Attribution       | Set correct author information for every commit                                         |
| Practical hygiene | Review staged changes, avoid secrets, amend tidy histories, sign if required            |

---

Consistently following these practices creates an auditable, understandable, and maintainable version history that underpins a high-quality development workflow.