# Code Review Checklist

This checklist sets out the minimum standards and expectations for reviewing code changes. Each point is accompanied by a rationale to clarify its importance and help ensure a consistent, maintainable, and robust codebase. All reviewers are expected to apply this checklist to every code review. Where particular considerations do not apply (e.g. no new tests are relevant), note this explicitly in the review.

---

## 1. **Correctness and Functionality**

- **Does the code do what it is intended to do?**  
  Confirm that the implemented change meets the requirement or user story precisely. Check that edge cases have been considered and handled appropriately.

  *Rationale*: Ensures the system behaves as expected and prevents regression or logical errors.

  *Example*: If a change is meant to filter out inactive users, verify that both active and inactive users are correctly processed, and that unexpected data does not slip through.

## 2. **Code Clarity and Style**

- **Is the code easily understandable by other engineers?**  
  Assess variable and function names for clarity and self-descriptiveness. Ensure the logic is straightforward; complex constructs should have adequate comments.

- **Does the code adhere to team or project style guides?**  
  Check for consistent indentation, brace style, naming conventions, and use of language idioms.

  *Rationale*: Clear, idiomatic code is easier to maintain, reduces onboarding friction, and lowers error rates.

  *Example*: Reject code with ambiguous names like `temp` or `foo`. Prefer descriptive names, such as `userLastLoginTime`.

## 3. **Testing and Test Coverage**

- **Are there sufficient automated tests?**  
  Verify that new logic is covered by appropriate tests (unit, integration, or system, as applicable). 

- **Are the tests meaningful and clear?**  
  Check tests for readability, relevance (covering both expected behaviour and edge cases), and maintainability.

- **Do all tests pass locally and in CI?**  
  Review should be blocked if tests do not pass.

  *Rationale*: Tests are the primary defence against regression and ambiguous requirements. High-quality, comprehensive tests reduce future troubleshooting burden.

  *Example*: For a new validation rule, insist on tests for both valid and invalid inputs, with clear expectation comments.

## 4. **Robustness and Error Handling**

- **Are errors and edge cases handled correctly?**  
  Confirm the code checks for all reasonably anticipated failure modes.

- **Is failure communicated clearly (e.g., through exceptions, error codes, or logging)?**  
  Ensure error messages are actionable and do not leak sensitive detail.

  *Rationale*: Robust error handling prevents silent failures, improves traceability, and enhances the end-user experience.

  *Example*: When reading from a file, ensure the code handles missing files, permission errors, and malformed data, and logs issues appropriately.

## 5. **Security and Data Privacy**

- **Are there any security implications to the change?**  
  Scrutinise for potential vulnerabilities (e.g., injections, improper permissions, data leakage).

- **Is sensitive data (such as credentials, tokens, personal data) handled in compliance with policies?**  
  Check data is not logged, stored insecurely, or improperly exposed.

  *Rationale*: Security oversights can have severe consequences, including data breaches or compliance violations.

  *Example*: Check for safe handling of user input, especially where it may be incorporated into queries or system commands.

## 6. **Performance and Efficiency**

- **Could changes introduce performance regressions?**  
  Consider algorithmic complexity, unnecessary data processing, or inefficient resource use.

- **Are there opportunities to improve performance without sacrificing clarity?**  
  Suggest simple improvements if they are clearly beneficial.

  *Rationale*: Poor performance can impact both users and operational costs. However, performance improvements should not compromise code maintainability.

  *Example*: Use efficient batch queries instead of per-row database accesses when retrieving multiple related records.

## 7. **Documentation and Comments**

- **Is code self-documenting where feasible?**  
  Prefer descriptive names and clear structure over excessive comments.

- **Are complex or non-obvious decisions documented?**  
  Request comments for algorithms, workarounds for known issues, or non-obvious trade-offs.

- **Is any user-facing documentation (README, API docs) updated if required?**  
  Ensure documentation reflects any changes to behaviour or usage.

  *Rationale*: Good documentation reduces support load and speeds onboarding.

  *Example*: For a new public API, require updates to endpoint documentation as part of the change.

## 8. **Dependencies and Configuration**

- **Are new dependencies justified, minimal, and compatible?**  
  Question new packages. Verify licensing, security, and compatibility with supported platforms.

- **Are configuration or environment changes clearly documented?**  
  Ensure new environment variables, configuration files, or build steps are described in relevant docs.

  *Rationale*: Unnecessary dependencies increase maintenance and security risk. Clear configuration prevents deployment failures.

  *Example*: A dependency added solely for a trivial utility function is typically unjustifiable; suggest an in-house implementation if appropriate.

## 9. **Backward Compatibility and Rollback**

- **Does the change preserve backwards compatibility when required?**  
  Confirm that public interfaces, stored data formats, and protocols are not broken unless explicitly agreed.

- **Is the change easy to roll back or revert in production?**  
  Complex, coupled, or non-idempotent changes may complicate rollback.

  *Rationale*: Reliable services depend on stability and the ability to recover quickly from problems.

  *Example*: If removing a field from an API response, agree a deprecation timeline and communicate widely.

## 10. **General Review Hygiene**

- **Is the pull request (PR) clearly described and scoped?**  
  Review PR title, summary, and description for clarity of intent and scope. Larger changes should be split by functionality.

- **Are unrelated changes included?**  
  Request separation of feature changes from e.g. formatting fixes.

- **Is the reviewer named and any required approvals in place?**  
  All code changes require a named reviewer, not the author, and (where applicable) approvals from subject matter experts or product owners.

  *Rationale*: Clear, focused PRs ease review, speed integration, and improve traceability.

  *Example*: A PR that mixes refactoring and new features should be split before merging.

---

## Summary Table

| Section                   | Key Questions                                                         |
|---------------------------|-----------------------------------------------------------------------|
| Correctness               | Does the code do what is intended, covering all edge cases?           |
| Clarity & Style           | Is the code readable and idiomatic?                                   |
| Testing                   | Is test coverage sufficient, clear, and passing?                      |
| Robustness                | Are errors and edge cases properly managed?                           |
| Security                  | Does the change introduce vulnerabilities or handle data safely?       |
| Performance               | Has performance been considered or improved for key paths?            |
| Documentation             | Is both code and user documentation up to date?                       |
| Dependencies              | Are new dependencies necessary, safe, and documented?                 |
| Compatibility/Rollback    | Is compatibility maintained, and can changes be reverted if needed?    |
| Review Hygiene            | Is the PR focused, well described, and correctly assigned?            |

---

**Reviewer Responsibility:**  
Use this checklist as an active aid, not a box-ticking exercise. If any item cannot be confidently answered, engage with the author for clarification or changes before approving the code.